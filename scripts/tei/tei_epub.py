#!/usr/bin/env python3
"""
Build an EPUB 3 straight from an (enriched) EEBO-TCP TEI file.

  python3 tei_epub.py EDITION.tei.xml OUT.epub --title T --author A \\
      [--front FRONT.html] [--cover COVER.jpg] [--css FILE ...] [--layer reg|orig]

One XHTML file per division (front matter, dedication, each chapter), text
rendered by tei_to_html.py. Notes are EPUB 3 footnotes (noteref + aside), so
readers that support it show them as pop-ups; others show them after the
chapter. Includes a nav document and an NCX table of contents for older
readers. Images referenced by the front matter are copied in, resolved
relative to the front-matter file.

Options:
  --front FILE       XHTML fragment for the front matter (its own file)
  --cover FILE       cover image; gets a cover page and cover-image property
  --css FILE         stylesheet, linked from every page; repeatable, in order
  --lang CODE        language of the text (default en)
  --identifier ID    dc:identifier (default: a UUID derived from title+author,
                     stable across rebuilds)
  --modified STAMP   dcterms:modified, e.g. 2026-09-30T00:00:00Z (default:
                     SOURCE_DATE_EPOCH if set, else now)
  plus --layer, --expand, --mark-supplied, --only-auto, --show-gaps as in
  tei_extract.py
"""

import argparse
import html
import os
import re
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from lxml import etree

from tei_to_html import add_text_args, divisions, renderer, xhtml

MEDIA = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
         ".gif": "image/gif", ".svg": "image/svg+xml", ".css": "text/css",
         ".xhtml": "application/xhtml+xml", ".ncx": "application/x-dtbncx+xml"}
FIXED_TIME = (1980, 1, 1, 0, 0, 0)          # zip entry times: reproducible builds
CONTAINER = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""


def esc(s):
    return html.escape(s, quote=True)


def modified_stamp(arg):
    if arg:
        return arg
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    t = datetime.fromtimestamp(int(epoch), timezone.utc) if epoch else datetime.now(timezone.utc)
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def local_images(fragment, base):
    """src paths in a fragment that point at local files, resolved on disk."""
    out = []
    for src in re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', fragment):
        if re.match(r"[a-z]+:", src) or src.startswith("/") or ".." in Path(src).parts:
            continue
        out.append((src, base / src))
    return out


def nav_doc(title, entries, landmarks, lang, css):
    toc = "".join(f'<li><a href="{f}">{esc(t)}</a></li>' for f, t in entries)
    marks = "".join(f'<li><a epub:type="{k}" href="{f}">{esc(t)}</a></li>'
                    for k, f, t in landmarks)
    body = [f'<nav epub:type="toc" id="toc" role="doc-toc"><h3>Contents</h3><ol>{toc}</ol></nav>',
            f'<nav epub:type="landmarks" id="landmarks" hidden="hidden"><ol>{marks}</ol></nav>']
    return xhtml(title, body, css, lang)


def ncx_doc(title, ident, entries):
    points = "".join(
        f'<navPoint id="np-{i}" playOrder="{i}"><navLabel><text>{esc(t)}</text>'
        f'</navLabel><content src="{f}"/></navPoint>'
        for i, (f, t) in enumerate(entries, 1))
    doc = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
           f'<head><meta name="dtb:uid" content="{esc(ident)}"/>'
           '<meta name="dtb:depth" content="1"/></head>'
           f"<docTitle><text>{esc(title)}</text></docTitle>"
           f"<navMap>{points}</navMap></ncx>\n")
    etree.fromstring(doc.encode("utf-8"))
    return doc


def opf_doc(a, ident, modified, items, spine):
    manifest = "".join(
        f'<item id="{i}" href="{h}" media-type="{m}"' + (f' properties="{p}"' if p else "") + "/>"
        for i, h, m, p in items)
    spine_xml = "".join(f'<itemref idref="{i}"/>' for i in spine)
    cover_meta = '<meta name="cover" content="cover-image"/>' if a.cover else ""
    doc = ('<?xml version="1.0" encoding="utf-8"?>\n'
           f'<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
           f'unique-identifier="bookid" xml:lang="{a.lang}">'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
           f'<dc:identifier id="bookid">{esc(ident)}</dc:identifier>'
           f"<dc:title>{esc(a.title)}</dc:title>"
           f"<dc:creator>{esc(a.author)}</dc:creator>"
           f"<dc:language>{a.lang}</dc:language>"
           f'<meta property="dcterms:modified">{modified}</meta>{cover_meta}'
           f'</metadata><manifest>{manifest}</manifest>'
           f'<spine toc="ncx">{spine_xml}</spine></package>\n')
    etree.fromstring(doc.encode("utf-8"))
    return doc


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tei")
    ap.add_argument("out")
    ap.add_argument("--title", required=True)
    ap.add_argument("--author", required=True)
    ap.add_argument("--front")
    ap.add_argument("--cover")
    ap.add_argument("--css", action="append", default=[])
    ap.add_argument("--lang", default="en")
    ap.add_argument("--identifier")
    ap.add_argument("--modified")
    add_text_args(ap)
    a = ap.parse_args()

    ident = a.identifier or f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, a.title + '|' + a.author)}"
    css_names = []
    files = {}                                   # name in OEBPS -> bytes
    items = []                                   # (id, href, media-type, properties)
    for i, c in enumerate(a.css):
        name = f"style-{i}{Path(c).suffix}" if Path(c).name in css_names else Path(c).name
        css_names.append(name)
        files[name] = Path(c).read_bytes()
        items.append((f"css-{i}", name, "text/css", None))

    spine, entries, landmarks = [], [], []

    def page(ident_, name, title, body):
        files[name] = xhtml(title, body, css_names, a.lang).encode("utf-8")
        items.append((ident_, name, "application/xhtml+xml", None))
        spine.append(ident_)

    if a.cover:
        cover = Path(a.cover)
        cname = "cover" + cover.suffix.lower()
        files[cname] = cover.read_bytes()
        items.append(("cover-image", cname, MEDIA[cover.suffix.lower()], "cover-image"))
        page("cover", "cover.xhtml", a.title,
             [f'<section id="cover" epub:type="cover" class="cover">'
              f'<img src="{cname}" alt="{esc(a.title)}"/></section>'])
        landmarks.append(("cover", "cover.xhtml", "Cover"))

    if a.front:
        front = Path(a.front)
        frag = front.read_text(encoding="utf-8").strip()
        for n, (src, path) in enumerate(local_images(frag, front.parent)):
            if src not in files:
                files[src] = path.read_bytes()
                items.append((f"img-{n}", src, MEDIA[path.suffix.lower()], None))
        page("front", "front.xhtml", a.title, [frag])
        landmarks.append(("titlepage", "front.xhtml", "Title Page"))

    r = renderer(a)
    root = etree.parse(a.tei).getroot()
    for n, (div_id, head, lines) in enumerate(divisions(root, r)):
        name = f"{div_id}.xhtml"
        page(div_id, name, head, lines)
        entries.append((name, head))
        if n == 0:
            landmarks.append(("bodymatter", name, "Start of Content"))

    files["nav.xhtml"] = nav_doc(a.title, entries, landmarks, a.lang, css_names).encode("utf-8")
    items.append(("nav", "nav.xhtml", "application/xhtml+xml", "nav"))
    files["toc.ncx"] = ncx_doc(a.title, ident, entries).encode("utf-8")
    items.append(("ncx", "toc.ncx", MEDIA[".ncx"], None))
    opf = opf_doc(a, ident, modified_stamp(a.modified), items, spine)

    with zipfile.ZipFile(a.out, "w") as z:
        def put(name, data, method=zipfile.ZIP_DEFLATED):
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = method
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
        put("mimetype", b"application/epub+zip", zipfile.ZIP_STORED)   # must be first
        put("META-INF/container.xml", CONTAINER.encode("utf-8"))
        put("OEBPS/content.opf", opf.encode("utf-8"))
        for name, data in files.items():
            put(f"OEBPS/{name}", data)
    print(f"wrote {a.out}: {len(entries)} divisions, {r.note_no} notes ({a.layer} layer)")


if __name__ == "__main__":
    main()
