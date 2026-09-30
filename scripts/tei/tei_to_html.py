#!/usr/bin/env python3
"""
Render an (enriched) EEBO-TCP TEI file as XHTML: the ebook renderer.

  python3 tei_to_html.py EDITION.tei.xml OUT.html [--layer reg|orig] [options]

tei_epub.py uses this module to build the EPUB; run on its own it writes the
whole book as one XHTML file, handy for previewing in a browser.

The text comes from the same renderer as tei_extract.py (same --layer and
audit options), so the ebook and the Typst chapters read identically.
Each division becomes a <section> with an <h3> head and its own notes at
the end as EPUB 3 footnotes (noteref + aside), numbered through the book.
Greek and Hebrew runs get lang (and dir) so readers pick a font that has
them.

Options:
  --front FILE   XHTML fragment (title page, licence ...) placed before the text
  --title TEXT   <title> of the document (default: the TEI title)
  --css FILE     stylesheet to link; repeatable
  plus --layer, --expand, --mark-supplied, --only-auto, --show-gaps as in
  tei_extract.py
"""

import argparse
import copy
import html
import re
from pathlib import Path

from lxml import etree

from tei_extract import R, T, collapse, local

GREEK = "Ͱ-Ͽἀ-῿"
HEBREW = "֐-׿"
MARKS = "̀-ͯ"
SCRIPT_RUNS = [
    (re.compile(f"[{GREEK}][{GREEK}{MARKS}]*(?:\\s+[{GREEK}][{GREEK}{MARKS}]*)*"),
     '<span lang="grc">{}</span>'),
    (re.compile(f"[{HEBREW}]+(?:\\s+[{HEBREW}]+)*"),
     '<span lang="he" dir="rtl">{}</span>'),
]
NOTEREF_GAP = re.compile(r'\s+(<a class="noteref")')


def smart_quotes(s):
    """Curl straight quotes the way Typst does for markup: after a letter or
    closing punctuation a quote closes, otherwise it opens."""
    s = re.sub(r"(?<=[\w.,;:!?)\]])'", "\u2019", s)
    s = s.replace("'", "\u2018")
    s = re.sub(r'(?<=[\w.,;:!?)\]])"', "\u201d", s)
    return s.replace('"', "\u201c")


class HtmlR(R):
    """R with XHTML output. Notes are collected per division by the caller."""

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.notes = []          # (number, body) for the current division
        self.note_no = 0

    def esc(self, s):
        s = smart_quotes(s)
        s = html.escape(s, quote=False)
        for rx, wrap in SCRIPT_RUNS:
            s = rx.sub(lambda m: wrap.format(m.group(0)), s)
        return s

    def sup(self, inner):
        return f"<sup>{inner}</sup>"

    def emph(self, inner):
        return f"<em>{inner}</em>"

    def footnote(self, body):
        self.note_no += 1
        n = self.note_no
        self.notes.append((n, body))
        return (f'<a class="noteref" id="nr-{n}" href="#fn-{n}" '
                f'epub:type="noteref" role="doc-noteref"><sup>{n}</sup></a>')

    def text(self, el):
        return NOTEREF_GAP.sub(r"\1", collapse(self.inline(el)).strip())

    def para(self, el, cls=None):
        t = self.text(el)
        if not t:
            return []
        attr = f' class="{cls}"' if cls else ""
        return [f"<p{attr}>{t}</p>"]

    def list_html(self, lst, depth=0):
        numbered = lst.get("type") == "numbered"
        out = []
        head = lst.find(T + "head")
        if head is not None and depth == 0:
            out.append(f"<p class=\"list-head\"><strong>{self.text(head)}</strong></p>")
        items = []
        for item in lst.findall(T + "item"):
            body = etree.Element("item-body")
            body.text = item.text
            subs = []
            for c in item:
                if local(c) == "list":
                    subs.append(c)
                    if c.tail:
                        prev = body[-1] if len(body) else None
                        if prev is not None:
                            prev.tail = (prev.tail or "") + c.tail
                        else:
                            body.text = (body.text or "") + c.tail
                else:
                    body.append(copy.deepcopy(c))
            txt = NOTEREF_GAP.sub(r"\1", collapse(self.inline(body, numbered)).strip())
            if numbered and self.layer == "orig":
                # printed numerals stay in the text, as run-in paragraphs
                if txt:
                    out.append(f"<p>{txt}</p>")
                for s in subs:
                    out += self.list_html(s, depth + 1)
                continue
            inner = "".join("".join(self.list_html(s, depth + 1)) for s in subs)
            if not txt and inner and items:
                # a text-less item holding a sub-list: the TCP's way of hanging
                # a branch of a genealogy under the item before it
                items[-1] = items[-1][:-len("</li>")] + inner + "</li>"
            elif txt or inner:
                items.append(f"<li>{txt}{inner}</li>")
        if items:
            tag = "ol" if numbered else "ul"
            cls = ' class="roman"' if numbered else ""
            out.append(f"<{tag}{cls}>" + "".join(items) + f"</{tag}>")
        return out

    def blocks(self, div):
        out = []
        for c in div:
            if not isinstance(c.tag, str):
                continue
            n = local(c)
            if n in ("head", "pb"):
                continue
            if n == "list":
                out += self.list_html(c)
            elif n == "closer":
                signed = c.find(T + "signed")
                if signed is None:
                    continue
                his = [x for x in signed if local(x) == "hi"]
                if his:
                    last = his[-1]
                    before = etree.Element("x")
                    before.text = signed.text
                    for x in signed:
                        if x is last:
                            break
                        before.append(copy.deepcopy(x))
                    out.append(f'<p class="closer">{self.text(before)}</p>')
                    right = collapse(self.node(last)).strip()
                    out.append(f'<p class="signature">{right}</p>')
                else:
                    out += self.para(signed, "signature")
            elif n == "trailer":
                if self.layer == "orig":
                    out += self.para(c, "trailer")
            elif n == "div":
                out += self.blocks(c)
            else:
                out += self.para(c)
        return out

    def heading(self, div):
        heads = div.findall(T + "head")
        if div.get("type") == "chapter":
            sub = next((h for h in heads if h.get("type") == "sub"), None)
            first = next((h for h in heads if h.get("type") is None), None)
            if self.layer == "reg":
                t = self.text(sub).rstrip(".") if sub is not None else ""
                return [f"<h3>{div.get('n')}. {t}</h3>"]
            out = [f"<h3>{self.text(first)}</h3>"] if first is not None else []
            if sub is not None:
                out.append(f'<p class="subhead"><em>{self.text(sub)}</em></p>')
            return out
        ed = next((h for h in heads if h.get("type") == "edition"), None)
        printed = next((h for h in heads if h.get("type") is None), None)
        h = ed if (self.layer == "reg" and ed is not None) else printed
        return [f"<h3>{self.text(h)}</h3>"] if h is not None else []

    def division(self, div, ident):
        """Lines for one division, its notes at the end as EPUB 3 footnotes:
        readers that support it show a note as a pop-up and hide the aside,
        the rest show the notes after the chapter."""
        self.notes = []
        head = self.heading(div)
        self.title = re.sub(r"<[^>]+>", "", head[0]) if head else ident
        out = [f'<section id="{ident}">'] + head + self.blocks(div)
        if self.notes:
            out.append('<section class="notes">')
            for n, body in self.notes:
                body = NOTEREF_GAP.sub(r"\1", body)
                out.append(f'<aside id="fn-{n}" class="note" epub:type="footnote" '
                           f'role="doc-footnote"><p><a href="#nr-{n}" '
                           f'role="doc-backlink">{n}.</a> {body}</p></aside>')
            out.append("</section>")
        out.append("</section>")
        return out


def add_text_args(ap):
    """The text options shared with tei_extract.py."""
    ap.add_argument("--layer", choices=["reg", "orig"], default="reg")
    ap.add_argument("--expand", action="store_true")
    ap.add_argument("--mark-supplied", action="store_true")
    ap.add_argument("--only-auto", action="store_true")
    ap.add_argument("--show-gaps", action="store_true")


def renderer(a):
    return HtmlR(a.layer, a.expand, a.mark_supplied, a.only_auto, a.show_gaps)


def tei_title(root):
    t = root.find(f"{T}teiHeader/{T}fileDesc/{T}titleStmt/{T}title")
    return collapse("".join(t.itertext())).strip() if t is not None else ""


def divisions(root, r):
    """(id, heading text, lines) for the dedication and each chapter."""
    for div in root.iter(T + "div"):
        typ = div.get("type")
        if typ == "dedication":
            ident = "dedication"
        elif typ == "chapter":
            ident = f"chapter-{int(div.get('n')):02d}"
        else:
            continue
        lines = r.division(div, ident)
        yield ident, html.unescape(r.title), lines


def xhtml(title, body, css=(), lang="en"):
    """A complete XHTML document; raises if it is not well-formed."""
    links = "".join(f'<link rel="stylesheet" type="text/css" href="{html.escape(c)}"/>'
                    for c in css)
    doc = ("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE html>\n"
           '<html xmlns="http://www.w3.org/1999/xhtml" '
           f'xmlns:epub="http://www.idpf.org/2007/ops" lang="{lang}" xml:lang="{lang}">\n'
           f'<head><meta charset="utf-8"/><title>{html.escape(title)}</title>{links}</head>\n'
           "<body>\n" + "\n".join(body) + "\n</body>\n</html>\n")
    etree.fromstring(doc.encode("utf-8"))
    return doc


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tei")
    ap.add_argument("out")
    add_text_args(ap)
    ap.add_argument("--front")
    ap.add_argument("--title")
    ap.add_argument("--css", action="append", default=[])
    a = ap.parse_args()
    r = renderer(a)
    root = etree.parse(a.tei).getroot()
    body = []
    if a.front:
        body.append(Path(a.front).read_text(encoding="utf-8").strip())
    for _, _, lines in divisions(root, r):
        body += lines
    Path(a.out).write_text(xhtml(a.title or tei_title(root), body, a.css),
                           encoding="utf-8")
    print(f"wrote {a.out}: {r.note_no} notes ({a.layer} layer)")


if __name__ == "__main__":
    main()
