#!/usr/bin/env python3
"""
thml_to_tei.py: a CCEL ThML file as TEI in the subset the pipeline reads.

CCEL (ccel.org) publishes its texts as ThML, an HTML-like XML. A book's
untouched ThML is its provenance, as the TCP file is for an EEBO book
(source/<id>.thml.xml); the tools read it through sources.load(), which
converts it with this module in memory, so there is no intermediate file.

  ThML                         TEI
  div1                         div[@type="chapter"][@n], numbered in order
  div2, div3 ... inside it     div[@type="section"][@n], numbered per parent
  div1 "Title Page"            front/titlePage (docTitle, byline/docAuthor,
                               epigraph)
  div1 "Contents", "Indexes"   div[@type="contents"], div[@type="index"]
                               (CCEL's own apparatus; SKIP_DIVISIONS)
  h1-h4 (first in a div)       head
  h1-h4 after the text began   signed (at the end of the div) or
                               p[@rend="center"]
  p                            p (@class Centered or text-align:center
                               -> @rend="center")
  p opening with a small-caps  sp/speaker + p (CCEL's dialogue labels,
  "Name:" (span.sc)            "Christian:"; as a TCP text encodes them)
  blockquote                   quote (its p's kept)
  verse / l                    quote / lg / l
  note                         note[@place="foot"]
  span.sc (small capitals)     seg[@rend="smallcaps"]
  br                           lb
  i / em, b / strong           hi[@rend="italic"] / hi[@rend="bold"]
  scripRef                     ref[@type="scripture"][@cRef] (OSIS reference)
  ThML ids                     @xml:id ccel-<id>

The text itself is kept exactly, straight quotes and "--" included: the
machine pass records any typographic change (TYPOGRAPHY in editorial.py).
CCEL texts carry no page or line information, so the TEI is
paragraph-faithful, not line-faithful; the header says so.

  python3 thml_to_tei.py grace.thml.xml [out.xml]   # write the TEI, to look at
"""

import copy
import re
import sys
from pathlib import Path

from lxml import etree

NS = "http://www.tei-c.org/ns/1.0"
T = "{%s}" % NS
XML_NS = "http://www.w3.org/XML/1998/namespace"


def tei(tag, parent=None, text=None, **attrs):
    el = etree.Element(T + tag) if parent is None else etree.SubElement(parent, T + tag)
    if text:
        el.text = text
    for k, v in attrs.items():
        if v is not None:
            el.set("{%s}id" % XML_NS if k == "xml_id" else k, v)
    return el


def xid(el):
    i = el.get("id")
    return f"ccel-{i}" if i else None


def first(el, path):
    found = el.find(path)
    return " ".join("".join(found.itertext()).split()) if found is not None else None


INLINE = {"i": ("hi", "italic"), "em": ("hi", "italic"),
          "b": ("hi", "bold"), "strong": ("hi", "bold")}


def inline(src, dst):
    """Copy src's text and inline children into dst (text kept exactly)."""
    dst.text = src.text
    for c in src:
        if not isinstance(c.tag, str):
            continue                      # comments, processing instructions
        n = c.tag
        if n == "br":
            el = tei("lb", dst)
        elif n in INLINE:
            tag, rend = INLINE[n]
            el = tei(tag, dst, rend=rend)
            inline(c, el)
        elif n == "scripRef":
            osis = c.get("osisRef", "")
            el = tei("ref", dst, type="scripture",
                     cRef=osis.split(":", 1)[1] if ":" in osis else None)
            inline(c, el)
        elif n == "note":
            el = tei("note", dst, place="foot", n=c.get("n"), xml_id=xid(c))
            inline(c, el)
        elif n in ("span", "a", "font", "sup", "sub", "name", "added", "foreign"):
            el = tei("hi" if n in ("sup", "sub") else "seg", dst,
                     rend=n if n in ("sup", "sub") else
                     "smallcaps" if c.get("class") == "sc" else None)
            inline(c, el)
        else:
            raise ValueError(f"ThML <{n}> inside a paragraph is not handled yet "
                             f"(id {c.get('id')})")
        el.tail = c.tail


def centred(src):
    return (src.get("class") or "").lower() == "centered" or \
        re.search(r"text-align:\s*center", src.get("style") or "") is not None


def speaker(src):
    """The span.sc "Name:" opening a dialogue paragraph, or None."""
    first = next((c for c in src if isinstance(c.tag, str)), None)
    if first is None or first.tag != "span" or first.get("class") != "sc" or \
            (src.text or "").strip() or len(first):
        return None
    return first if (first.text or "").strip().endswith(":") else None


def block(src, dst):
    """One ThML block element as TEI, appended to dst."""
    n = src.tag
    if n == "p" and speaker(src) is not None:
        span = speaker(src)
        sp = tei("sp", dst, xml_id=xid(src))
        tei("speaker", sp, span.text, xml_id=xid(span))
        sp[-1].tail = " "
        p = tei("p", sp, rend="center" if centred(src) else None)
        rest = copy.copy(src)
        rest.remove(rest[0])
        rest.text = (span.tail or "").lstrip()
        inline(rest, p)
    elif n == "p":
        p = tei("p", dst, xml_id=xid(src), rend="center" if centred(src) else None)
        inline(src, p)
    elif n == "blockquote":
        q = tei("quote", dst, xml_id=xid(src))
        blocks(src, q)
    elif n == "verse":
        q = tei("quote", dst, xml_id=xid(src))
        lg = tei("lg", q)
        lg.text = src.text
        for c in src:
            if not isinstance(c.tag, str):
                continue
            if c.tag != "l":
                raise ValueError(f"ThML <verse> holds <{c.tag}> (id {c.get('id')})")
            l_ = tei("l", lg, xml_id=xid(c))
            inline(c, l_)
            l_.tail = c.tail
    elif re.fullmatch(r"h[1-6]", n):
        h = tei("head", dst, xml_id=xid(src))
        inline(src, h)
    elif re.fullmatch(r"div\d?", n):
        division(src, dst, "section", str(1 + sum(
            1 for c in dst if isinstance(c.tag, str) and c.tag == T + "div")))
    else:
        raise ValueError(f"ThML block <{n}> is not handled yet (id {src.get('id')})")


APPARATUS = {"contents": "contents", "indexes": "index", "index": "index"}


def division(d, parent, typ, n):
    """A ThML div (any level) as a TEI div, appended to parent."""
    typ = APPARATUS.get((d.get("title") or "").strip().lower(), typ)
    div = tei("div", parent, type=typ, n=n, xml_id=xid(d))
    blocks(d, div)
    # a heading after the text began is not the division's title: at the
    # end it is a signature (the Apology's "JOHN BUNYAN."), else centred
    kids = [c for c in div if isinstance(c.tag, str)]
    for k, c in enumerate(kids):
        if c.tag == T + "head" and any(x.tag != T + "head" for x in kids[:k]):
            if all(x.tag == T + "head" for x in kids[k:]):
                c.tag = T + "signed"
            else:
                c.tag = T + "p"
                c.set("rend", "center")
    return div


def blocks(src, dst):
    """src's block children as TEI in dst, the space between them kept."""
    dst.text = src.text
    for c in src:
        if not isinstance(c.tag, str):
            continue
        if (c.tag == "a" and not len(c) and not (c.text or "").strip()) or \
                c.tag == "insertIndex":
            # an empty link target, CCEL's index marker: only the space stays
            if len(dst):
                dst[-1].tail = (dst[-1].tail or "") + (c.tail or "")
            else:
                dst.text = (dst.text or "") + (c.tail or "")
            continue
        block(c, dst)
        dst[-1].tail = c.tail


def title_page(d, front):
    """A ThML "Title Page" div as front/titlePage: the first heading is the
    title, a "By" line and the heading after it the byline, a paragraph
    holding a scripture reference the epigraph, other lines subtitles."""
    tp = tei("titlePage", front, xml_id=xid(d))
    blocks = [c for c in d if isinstance(c.tag, str)]
    byline = None
    for c in blocks:
        text = " ".join("".join(c.itertext()).split())
        if re.fullmatch(r"h[1-6]", c.tag) and tp.find(T + "docTitle") is None:
            el = tei("titlePart", tei("docTitle", tp), type="main", xml_id=xid(c))
        elif c.tag == "p" and text.lower() == "by":
            byline = tei("byline", tp, xml_id=xid(c))
            inline(c, byline)
            continue
        elif re.fullmatch(r"h[1-6]", c.tag) and byline is not None:
            el = tei("docAuthor", byline, xml_id=xid(c))
            byline[-1].tail = None
            if byline.text:
                byline.text = byline.text + " "
            byline = None
        elif c.tag == "p" and c.find(".//scripRef") is not None:
            el = tei("p", tei("epigraph", tp), xml_id=xid(c))
        else:
            el = tei("titlePart", tp, type="sub", xml_id=xid(c))
        inline(c, el)


def header(thml, path):
    h = thml.find("ThML.head")
    title = first(h, ".//DC.Title") or first(h, ".//title") or Path(path).stem
    author = first(h, ".//DC.Creator[@sub='Author']") or first(h, ".//DC.Creator")
    hdr = tei("teiHeader")
    fd = tei("fileDesc", hdr)
    ts = tei("titleStmt", fd)
    tei("title", ts, title)
    if author:
        tei("author", ts, author)
    ps = tei("publicationStmt", fd)
    tei("publisher", ps, first(h, ".//DC.Publisher") or "Christian Classics Ethereal Library")
    for tag, path_ in (("date", ".//DC.Date"), ("idno", ".//bookID")):
        v = first(h, path_)
        if v:
            tei(tag, ps, v)
    tei("p", tei("availability", ps), first(h, ".//DC.Rights") or "Public domain.")
    sd = tei("sourceDesc", fd)
    bibl = tei("bibl", sd)
    tei("title", bibl, title)
    if author:
        tei("author", bibl, author)
    src_info = first(h, ".//printSourceInfo/published") or first(h, ".//DC.Source")
    if src_info:
        tei("note", bibl, src_info)
    tei("note", bibl, f"Converted from the CCEL ThML file {Path(path).name} by "
        "scripts/tei/thml_to_tei.py. The text is kept exactly; CCEL gives no page "
        "or line information, so this transcription is paragraph-faithful, not "
        "line-faithful.")
    ed = tei("encodingDesc", hdr)
    tei("p", tei("projectDesc", ed),
        "ThML from the Christian Classics Ethereal Library (ccel.org), "
        "converted to TEI P5 for the Freely Given Books pipeline.")
    lu = tei("langUsage", tei("profileDesc", hdr))
    tei("language", lu, "English", ident=first(h, ".//DC.Language") or "en")
    rd = tei("revisionDesc", hdr)
    tei("change", rd, f"Converted from CCEL ThML ({Path(path).name}).")
    return hdr


def convert(path):
    """The TEI (an lxml ElementTree) for a ThML file."""
    parser = etree.XMLParser(load_dtd=False, resolve_entities=False, no_network=True)
    thml = etree.parse(str(path), parser).getroot()
    root = etree.Element(T + "TEI", nsmap={None: NS})
    root.append(header(thml, path))
    text = tei("text", root)
    front = None
    body = tei("body", text)
    n = 0
    for d in thml.find("ThML.body"):
        if not isinstance(d.tag, str):
            continue
        if not re.fullmatch(r"div\d", d.tag):
            raise ValueError(f"ThML.body holds <{d.tag}>; expected div1 ...")
        title = d.get("title") or ""
        if title.lower() == "title page":
            if front is None:
                front = etree.Element(T + "front")
                text.insert(0, front)
            title_page(d, front)
            continue
        apparatus = (d.get("title") or "").strip().lower() in APPARATUS
        n += 0 if apparatus else 1
        division(d, body, "chapter", None if apparatus else str(n))
    return etree.ElementTree(root)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    tree = convert(sys.argv[1])
    out = etree.tostring(tree, xml_declaration=True, encoding="UTF-8", pretty_print=False)
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_bytes(out)
    else:
        sys.stdout.buffer.write(out)


if __name__ == "__main__":
    main()
