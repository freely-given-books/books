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

from tei_extract import R, T, collapse, local, following_trailers, p_runs
import layout

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


CLOSERS = set(".,;:!?)]")


def curl(markup):
    """Curl straight quotes in rendered XHTML the way Typst does (its
    SmartQuoter): within a paragraph it remembers which quotes are open; a
    single quote after a letter is an apostrophe unless a single quotation
    is open; a quote after a digit is a prime unless one of its kind is
    open; an open quote of the same kind closes unless the quote follows a
    space or an opening bracket; anything else opens a quotation. Works
    across tags ("<em>Simon</em>'s" closes), so it runs on whole paragraphs,
    headings and notes rather than on text fragments; a block tag (p, li,
    a heading ...) starts a new paragraph."""
    out, prev, i, stack = [], " ", 0, []
    while i < len(markup):
        c = markup[i]
        if c == "<":
            j = markup.index(">", i)
            tag = markup[i:j + 1]
            if BLOCK_TAG.match(tag):
                prev, stack = " ", []
            out.append(tag)
            i = j + 1
            continue
        if c == "&":
            j = markup.find(";", i)
            ent = markup[i:j + 1]
            out.append(ent)
            prev = html.unescape(ent)[-1:] or prev
            i = j + 1
            continue
        if c in "'\"":
            double = c == '"'
            opened = stack[-1] if stack else None
            if prev.isnumeric() and opened != double:
                c = "\u2033" if double else "\u2032"
            elif not double and opened is not False and prev.isalpha():
                c = "\u2019"
            elif opened == double and not prev.isspace() and prev not in "([{":
                stack.pop()
                c = "\u201d" if double else "\u2019"
            else:
                stack.append(double)
                c = "\u201c" if double else "\u2018"
        out.append(c)
        prev = c
        i += 1
    return "".join(out)


def finish(blocks):
    """Rendered blocks with their quotes curled, each a paragraph or more."""
    return [curl(b) for b in blocks]


BLOCK_TAG = re.compile(r"<(p|li|h[1-6]|blockquote|div|aside|section|td|th)[\s>/]")


# list/@rend (a Typst numbering pattern) as an HTML <ol type>
OL_TYPE = {"1.": "1", "1)": "1", "I.": "I", "i.": "i", "i)": "i",
           "A.": "A", "a.": "a", "a)": "a"}


class HtmlR(R):
    """R with XHTML output. Notes are collected per division by the caller."""

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.notes = []          # (number, body) for the current division
        self.note_no = 0

    def esc(self, s):
        s = html.escape(s, quote=False)
        for rx, wrap in SCRIPT_RUNS:
            s = rx.sub(lambda m: wrap.format(m.group(0)), s)
        return s

    def after_call(self, prev):
        return False

    def sup(self, inner):
        return f"<sup>{inner}</sup>"

    def emph(self, inner):
        return f"<em>{inner}</em>"

    def linebreak(self):
        return "<br/>"

    def smallcaps(self, inner):
        how = getattr(self, "settings", {}).get("SMALLCAPS")
        if how == "strong":
            return f"<strong>{inner}</strong>"
        if how == "smallcaps":
            return f'<span class="smallcaps">{inner}</span>'
        return inner

    def footnote(self, body):
        self.note_no += 1
        n = self.note_no
        self.notes.append((n, body))
        return (f'<a class="noteref" id="nr-{n}" href="#fn-{n}" '
                f'epub:type="noteref" role="doc-noteref"><sup>{n}</sup></a>')

    def text(self, el):
        """Inline XHTML of el; quotes stay straight until the block it goes
        into is finished (finish()), since a run-on block joins another."""
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

        def flush_items():
            out.extend(self._ol(lst, items))
            items.clear()
        for item in lst.findall(T + "item"):
            body = etree.Element("item-body")
            body.text = item.text
            subs = []
            for c in item:
                if local(c) in ("list", "p"):
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

            def sub_html(s):            # a list or a paragraph inside the item
                if local(s) == "list":
                    return self.list_html(s, depth + 1)
                t = self.text(s)
                return [f"<p>{t}</p>"] if t else []
            if self.layer == "orig" and (numbered and lst.get("subtype") != "printed" or
                                         lst.get("type") == "bulleted"):
                # printed numerals stay in the text, as run-in paragraphs
                if txt:
                    out.append(f"<p>{txt}</p>")
                for s in subs:
                    out += sub_html(s)
                continue
            pieces = []
            for s in subs:
                if self.layer == "reg" and local(s) == "p" and s.get("prev"):
                    t = self.text(s)        # runs on from the text before it
                    sp = "" if s.get("rend") == "run-on" else " "
                    if pieces and pieces[-1].endswith("</p>"):
                        pieces[-1] = pieces[-1][:-len("</p>")] + sp + t + "</p>"
                    elif t:
                        txt = (txt + sp + t).strip()
                    continue
                pieces += sub_html(s)
            inner = "".join(pieces)
            if not txt and inner and items:
                # a text-less item holding a sub-list: the TCP's way of hanging
                # a branch of a genealogy under the item before it
                items[-1] = items[-1][:-len("</li>")] + inner + "</li>"
            elif self.layer == "reg" and item.get("rend") == "paragraph":
                flush_items()                   # a printed item set as a paragraph
                out.append(f"<p>{txt}</p>")
                out.extend([inner] if inner else [])
            elif txt or inner:
                items.append(f"<li>{txt}{inner}</li>")
        flush_items()
        return out

    def _ol(self, lst, items):
        """The <ol>/<ul> for a run of rendered items."""
        out = []
        numbered = lst.get("type") == "numbered"
        if items:
            if numbered and self.layer == "orig":
                numbered = False                 # printed list: numerals are text
            tag = "ol" if numbered else "ul"
            cls = ' class="roman"' if numbered and self.enum == "I." and \
                not lst.get("rend") else ""
            if numbered and lst.get("rend"):       # the edition's own numbering
                cls = f' type="{OL_TYPE.get(lst.get("rend"), "1")}"'
            first = lst.find(T + "item")
            if numbered and first is not None and first.get("n"):
                cls += f' start="{first.get("n")}"'
            out.append(f"<{tag}{cls}>" + "".join(items) + f"</{tag}>")
        return out

    def add_block(self, out, c, html_):
        """Like tei_extract.add_block: a block with @prev (the review ran it
        on from the block before) joins that paragraph in the reg layer."""
        empty = self.__dict__.setdefault("empty_blocks", set())
        if not html_:
            if c.get("{http://www.w3.org/XML/1998/namespace}id"):
                empty.add(c.get("{http://www.w3.org/XML/1998/namespace}id"))     # nothing to run on into
            return
        if c.get("prev") and c.get("prev")[1:] in empty:
            out.append(html_)
        elif self.layer == "reg" and c.get("prev") and out and \
                re.search(r"</li></[ou]l>$", out[-1]):
            # runs on into the last item of the list before
            inner = re.sub(r"^(<blockquote>)?<p[^>]*>|</p>(</blockquote>)?$", "", html_)
            k = out[-1].rindex("</li>")
            sp = "" if c.get("rend") == "run-on" else " "
            out[-1] = out[-1][:k] + sp + inner + out[-1][k:]
        elif self.layer == "reg" and c.get("prev") and out and \
                out[-1].endswith(("</p>", "</p></blockquote>")):
            inner = re.sub(r"^(<blockquote>)?<p[^>]*>|</p>(</blockquote>)?$", "", html_)
            end = "</p></blockquote>" if out[-1].endswith("</blockquote>") else "</p>"
            sp = "" if c.get("rend") == "run-on" else " "
            out[-1] = out[-1][:-len(end)] + sp + inner + end
        else:
            out.append(html_)

    def trailer(self, c):
        if self.layer == "orig":
            return self.para(c, "trailer")
        if c.get("ana") == "#in-edition":
            return self.para(c)
        return []

    def split_p(self, p):
        """A paragraph with block lists or tables: text, block, text."""
        out = []
        for kind, el in p_runs(p, self.layer == "reg"):
            if kind == "text":
                out += self.para(el)
            elif local(el) == "table":
                out += self.table_html(el)
            else:
                out += self.list_html(el)
        return out

    def table_html(self, table):
        """As tei_extract.table_lines: labels as paragraphs, branches as a
        list (reg layer); rows as printed (orig layer)."""
        out, items = [], []

        def flush():
            if items:
                out.append('<ol class="brace">' + "".join(items) + "</ol>")
                items.clear()
        if self.layer == "reg":
            for marker, cells in layout.table_reading(table)[1]:
                t = self.text_of(cells)
                if not t:
                    continue
                if marker == "+":
                    items.append(f"<li>{t}</li>")
                else:
                    flush()
                    out.append(f"<p>{t}</p>")
        else:
            for row in table.findall(T + "row"):
                t = self.text_of(row.findall(T + "cell"))
                if t:
                    out.append(f"<p>{t}</p>")
        flush()
        return out

    def text_of(self, els):
        return NOTEREF_GAP.sub(r"\1", collapse(
            " ".join(self.inline(e) for e in els)).strip())

    levels = None             # layout mode: {div type: heading level}
    enum = "I."               # TYPST_ENUM: numbering of lists the review made
    verse_linebreaks = False   # VERSE_LINEBREAKS: verse lines broken as printed
    quote_block = False       # QUOTE_BLOCK: the print template sets #quote as a
                              # block (no marks); else as an inline quotation
    run_in = set()

    def div_html(self, div, level):
        """Layout mode: a division's heads (h{level+1}, or a bold run-in
        paragraph for RUN_IN_DIVS) and its content."""
        out = []
        for h in div.findall(T + "head"):
            t = self.text(h)
            if not t:
                continue
            if div.get("type") in self.run_in:
                out.append(f'<p class="runin"><strong>{t}</strong></p>')
            else:
                out.append(f"<h{min(level + 1, 6)}>{t}</h{min(level + 1, 6)}>")
        return out + self.blocks(div, level)

    def layout_file(self, f, ident):
        """Layout mode: one file of the layout as a section, like division()."""
        self.notes = []
        title = f["title"]
        out = [f'<section id="{ident}">']
        if title:
            out.append(f"<h3>{html.escape(title, quote=False)}</h3>")
        for el in f["parts"]:
            if local(el) == "div":
                out += self.div_html(el, self.levels.get(el.get("type"), 2))
            else:
                self.blocks([el], 2, out)      # may run on from the block before
        out = finish(out)
        heads = [re.sub(r"<[^>]+>", "", x) for x in out if re.match(r"<h[1-6]>", x)]
        self.title = title or (heads[0] if heads else ident)
        out += self.notes_section()
        out.append("</section>")
        return out

    def notes_section(self):
        if not self.notes:
            return []
        out = ['<section class="notes">']
        for n, body in self.notes:
            body = curl(NOTEREF_GAP.sub(r"\1", body))
            out.append(f'<aside id="fn-{n}" class="note" epub:type="footnote" '
                       f'role="doc-footnote"><p><a href="#nr-{n}" '
                       f'role="doc-backlink">{n}.</a> {body}</p></aside>')
        out.append("</section>")
        return out

    def blocks(self, div, level=2, out=None):
        """HTML of a division's blocks: finished (quotes curled) when
        returned, or added unfinished to `out` when given, for the caller to
        finish once every block that may run on has joined."""
        if out is None:
            return finish(self.blocks(div, level, []))
        for c in div:
            if not isinstance(c.tag, str):
                continue
            n = local(c)
            if n in ("head", "pb", "speaker"):
                continue
            if n == "sp":
                # the speaker ("Christian:") opens the speech's first paragraph
                inner = self.blocks(c, level)
                spk = c.find(T + "speaker")
                name = self.text(spk) if spk is not None else ""
                k = next((i for i, x in enumerate(inner) if x.startswith("<p")), None)
                if name and k is not None and inner[k].startswith(("<p>", '<p class="')):
                    j = inner[k].index(">") + 1
                    inner[k] = inner[k][:j] + name + " " + inner[k][j:]
                elif name:
                    inner.insert(0, f"<p>{name}</p>")
                out += inner
                continue
            if n == "label" and c.get("type") == "head":
                if self.layer == "reg":       # a heading the edition adds
                    h = min(int(c.get("n", "3")) + 1, 6)
                    out.append(f"<h{h}>{self.text(c)}</h{h}>")
                continue
            if n == "epigraph" and self.layer == "reg":
                ref = self.text_of(c.findall(T + "bibl"))
                body = self.text_of([q for q in c if local(q) in ("q", "p")])
                if c.get("rend") == "quote":      # set as a quotation
                    t = " ".join(x for x in (ref, body) if x)
                    if t and self.quote_block:
                        out.append(f"<blockquote><p>{t}</p></blockquote>")
                    elif t:
                        out.append(f'<p class="quote">\u201c{t}\u201d</p>')
                    continue
                out.append('<div class="epigraph">' +
                           (f'<p class="epigraph-ref">{ref}</p>' if ref else "") +
                           (f'<p class="epigraph-text">{body}</p>' if body else "") + "</div>")
                continue
            if n == "p" and layout.p_blocks(c, self.layer == "reg"):
                out += self.split_p(c)
                continue
            if n == "p" or \
                    (n == "q" and c.get("rend") == "quote" and c.find(T + "p") is None):
                t = self.text(c)
                if t and self.layer == "reg" and c.get("rend") == "quote":
                    if self.quote_block:
                        self.add_block(out, c, f"<blockquote><p>{t}</p></blockquote>")
                    else:
                        t = f"\u201c{t}\u201d"      # as Typst sets #quote[...]
                        self.add_block(out, c, f'<p class="quote">{t}</p>')
                elif t:
                    self.add_block(out, c, f"<p>{t}</p>")
                else:
                    self.add_block(out, c, "")      # remembered as empty
                continue
            if n == "list" and self.layer == "reg" and c.get("rend") == "inline":
                self.add_block(out, c, f"<p>{self.text(c)}</p>")   # in the sentence
            elif n == "list":
                out += self.list_html(c)
            elif n == "quote":
                # a quotation block of the source: one paragraph, as Typst sets
                # #quote[...] with its lines run together
                # (VERSE_LINEBREAKS: verse lines broken as printed; in a
                # section made of verse a stanza is a plain paragraph)
                parts = []
                br = "<br/>" if self.verse_linebreaks else " "
                for x in c:
                    if not isinstance(x.tag, str):
                        continue
                    if local(x) == "lg":
                        lines = [self.text(l) for l in x if isinstance(l.tag, str)]
                        parts.append(br.join(l_ for l_ in lines if l_))
                    else:
                        parts.append(self.text(x))
                t = " ".join(p_ for p_ in parts if p_)
                if t and layout.verse_division(c):
                    out.append(f'<p class="verse">{t}</p>')
                elif t:
                    out.append(f"<blockquote><p>{t}</p></blockquote>")
            elif n == "lg" and self.layer == "reg" and c.get("rend") == "paragraphs":
                for x in c:             # verse set a line to a paragraph
                    if isinstance(x.tag, str) and local(x) == "l":
                        for h in self.para(x):
                            self.add_block(out, x, h)
            elif n in ("closer", "opener") and getattr(self, "settings", {}).get("CLOSER_PLAIN"):
                for x in c:             # salute, signature ...: plain paragraphs
                    if isinstance(x.tag, str) and local(x) != "pb":
                        for h in self.para(x):
                            self.add_block(out, x, h)
            elif n == "closer" and layout.closer_lines(c, self.layer) is not None:
                for x in layout.closer_lines(c, self.layer):
                    for h in self.para(x):
                        self.add_block(out, x, h)
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
                out += self.trailer(c)
            elif n == "div" and self.levels is not None:
                out += self.div_html(c, self.levels.get(c.get("type"), level + 1))
            elif n == "div" or (n == "q" and c.find(T + "p") is not None):
                out += self.blocks(c)
            else:
                for h in self.para(c) or [""]:
                    self.add_block(out, c, h)
        return out

    def heading(self, div):
        heads = div.findall(T + "head")
        ed = next((h for h in heads if h.get("type") == "edition"), None)
        if div.get("type") == "chapter" and self.layer == "reg" and ed is not None:
            return [f"<h3>{self.text(ed)}</h3>"]
        if div.get("type") == "chapter":
            sub = next((h for h in heads if h.get("type") == "sub"), None)
            first = next((h for h in heads if h.get("type") is None), None)
            if self.layer == "reg" and sub is None and first is not None:
                return [f"<h3>{self.text(first)}</h3>"]     # a single plain head
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
        head = finish(self.heading(div))
        self.title = re.sub(r"<[^>]+>", "", head[0]) if head else ident
        out = [f'<section id="{ident}">'] + head + self.blocks(div)
        for tr in following_trailers(div):
            out += finish(self.trailer(tr))
        if self.notes:
            out.append('<section class="notes">')
            for n, body in self.notes:
                body = curl(NOTEREF_GAP.sub(r"\1", body))
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


def renderer(a, root=None):
    r = HtmlR(a.layer, a.expand, a.mark_supplied, a.only_auto, a.show_gaps)
    if root is not None:
        r.index(root)
    return r


def tei_title(root):
    t = root.find(f"{T}teiHeader/{T}fileDesc/{T}titleStmt/{T}title")
    return collapse("".join(t.itertext())).strip() if t is not None else ""


def file_ident(name):
    """An XHTML id / file stem for a layout file (vol-1/01-x.typ -> vol-1-01-x)."""
    return re.sub(r"[^A-Za-z0-9]+", "-", re.sub(r"\.typ$", "", name)).strip("-")


def divisions(root, r, cfg=None):
    """(id, heading text, lines) for the dedication and each chapter, or for
    each file of the book's LAYOUT (cfg: the book's editorial.py settings)."""
    files = layout.book_layout(root, cfg or {})
    r.enum = (cfg or {}).get("TYPST_ENUM", "I.")
    r.quote_block = (cfg or {}).get("QUOTE_BLOCK", False)
    r.verse_linebreaks = (cfg or {}).get("VERSE_LINEBREAKS", False)
    if (cfg or {}).get("SMALLCAPS"):
        r.settings = dict(getattr(r, "settings", {}), SMALLCAPS=cfg["SMALLCAPS"])
    if (cfg or {}).get("CLOSER_PLAIN"):
        r.settings = dict(getattr(r, "settings", {}), CLOSER_PLAIN=True)
    if files is not None:
        r.levels, r.run_in = layout.div_levels(cfg)
        for f in files:
            if f.get("part"):
                # a part page before the file (its title an h2; the files
                # after it nest under it in the contents)
                pid = "part-" + re.sub(r"[^a-z0-9]+", "-", f["part"].lower()).strip("-")
                title = html.escape(f["part"], quote=False)
                yield pid, f["part"], [f'<section id="{pid}" class="part">',
                                       f"<h2>{title}</h2>", "</section>"]
            ident = file_ident(f["file"])
            lines = r.layout_file(f, ident)
            yield ident, html.unescape(r.title), lines
        return
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
    root = etree.parse(a.tei).getroot()
    r = renderer(a, root)
    body = []
    if a.front:
        body.append(Path(a.front).read_text(encoding="utf-8").strip())
    for _, _, lines in divisions(root, r, layout.settings(a.tei)):
        body += lines
    Path(a.out).write_text(xhtml(a.title or tei_title(root), body, a.css),
                           encoding="utf-8")
    print(f"wrote {a.out}: {r.note_no} notes ({a.layer} layer)")


if __name__ == "__main__":
    main()
