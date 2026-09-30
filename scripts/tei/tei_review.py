#!/usr/bin/env python3
"""
A side-by-side reading copy of an enriched TEI edition: the text as printed
on the left, the edition on the right, block by block, every editorial
change marked. Open the HTML file in a browser; hover over a marked word to
see what was printed, what the machine proposed and who decided.

  python3 tei_review.py EDITION.tei.xml OUT.html [--before FILE] [--after FILE]

It is for reading only. Make changes in chapters/typ and rebuild the TEI
(build_tei.py --review), then run this again.

Both columns come from the ebook renderer (tei_to_html.HtmlR), so they read
exactly as the ebook does: the left column is the orig layer (with printed
page numbers), the right the reg layer. One row is one block of the TEI; a
block the edition runs on from the one before is marked with a return
arrow instead of being joined, so the rows stay aligned.

Modern matter that is not in the TEI (a foreword, an abbreviations guide)
can be shown too, with the same --before/--after files as tei_epub.py: a
.typ file is rendered with Typst's HTML export, a .html file is a fragment.
It fills the edition column; the printed column says it is not in print.
"""

import argparse
import collections
import html
import re
from pathlib import Path

from lxml import etree

from tei_extract import R, T, collapse, local, following_trailers
from tei_to_html import HtmlR, curl, NOTEREF_GAP, tei_title
from tei_epub import typst_page

TYPES = [  # (class, label, shown by default)
    ("t-emendation", "wording", True),
    ("t-grammar", "grammar (thou, hath, -eth)", True),
    ("t-spelling", "spelling", True),
    ("t-case", "capitals", True),
    ("t-punctuation", "punctuation", True),
    ("t-spacing", "spacing", False),
    ("t-abbr", "abbreviations", False),
    ("t-supplied", "supplied letters", True),
    ("t-italic", "italics", False),
    ("t-note", "notes", True),
]


class Plain(R):
    """Plain text of a TEI fragment, for tooltips."""

    def esc(self, s):
        return s

    def after_call(self, prev):
        return False

    def sup(self, inner):
        return inner

    def emph(self, inner):
        return inner

    def footnote(self, body):
        return ""


def plain(layer, el, root_moved):
    p = Plain(layer)
    p.moved = root_moved
    t = collapse(p.inline(el) if len(el) or el.text else "").strip()
    return t or "(nothing)"


class ReviewR(HtmlR):
    """HtmlR with every <choice>, <supplied> and changed italic wrapped in a
    marked span, page breaks shown in the orig column and notes collected
    per row."""

    def __init__(self, layer, prefix, printed_year):
        super().__init__(layer)
        self.prefix = prefix
        self.year = printed_year

    def footnote(self, body):
        self.note_no += 1
        n = self.note_no
        self.notes.append((n, body))
        return (f'<a class="noteref" id="{self.prefix}nr-{n}" '
                f'href="#{self.prefix}fn-{n}"><sup>{n}</sup></a>')

    def marked(self, inner, cls, tip):
        tip = html.escape(tip, quote=True).replace("\n", "&#10;")
        if not inner.strip():
            inner = '<span class="gone">‸</span>' if self.layer == "reg" else inner
        return f'<span class="ch {cls}" title="{tip}">{inner}</span>'

    def choice(self, c):
        inner = super().choice(c)
        orig, abbr = c.find(T + "orig"), c.find(T + "abbr")
        if orig is not None:
            regs = c.findall(T + "reg")
            if not regs:
                return inner
            ed = [x for x in regs if x.get("resp") == "#editor"]
            au = [x for x in regs if x.get("resp") == "#auto"]
            reg = (ed or au or regs)[0]
            who = "editor" if ed else "machine"
            typ = reg.get("type") or "spelling"
            printed = plain("orig", orig, self.moved)
            modern = plain("reg", reg, self.moved)
            tip = f"{self.year}: {printed}\nedition: {modern}"
            if ed and au:
                tip += f"\nmachine proposed: {plain('reg', au[0], self.moved)}"
            tip += f"\n{typ}, by the {who}"
            return self.marked(inner, f"t-{typ} {'ed' if ed else 'auto'}", tip)
        if abbr is not None:
            expan = c.find(T + "expan")
            ed = expan is not None and expan.get("resp") == "#editor"
            tip = (f"printed: {plain('orig', abbr, self.moved)}\n"
                   f"expanded: {(expan.text or '') if expan is not None else ''}\n"
                   f"abbreviation, by the {'editor' if ed else 'machine'}")
            return self.marked(inner, f"t-abbr {'ed' if ed else 'auto'}", tip)
        return inner

    def node(self, c, in_numbered=False):
        if not isinstance(c.tag, str):
            return ""
        n = local(c)
        if n == "pb" and self.layer == "orig" and c.get("n"):
            return f' <span class="pb">p.&#160;{html.escape(c.get("n"))}</span> '
        out = super().node(c, in_numbered)
        if n == "supplied":
            why = " ".join(x.text.strip() for x in c
                           if isinstance(x, etree._Comment) and x.text)
            ed = c.get("resp") == "#editor"
            tip = (f"supplied: letters lost in print ({c.get('reason', '')}), "
                   f"certainty {c.get('cert', '?')}, by the "
                   f"{'editor' if ed else 'machine'}" + (f"\n{why}" if why else ""))
            return self.marked(out, f"t-supplied {'ed' if ed else 'auto'}", tip)
        if n == "hi" and c.get("ana") in ("#print-only", "#edition-only"):
            tip = ("italic in print, roman in the edition"
                   if c.get("ana") == "#print-only"
                   else "roman in print, italic in the edition")
            return self.marked(out, "t-italic ed", tip)
        if n == "note" and out and c.get("ana") in ("#edition-only", "#print-only"):
            n_, body = self.notes[-1]
            what = ("added by the editor" if c.get("ana") == "#edition-only"
                    else "dropped from the edition")
            self.notes[-1] = (n_, f'{body} <span class="ch t-note ed">[{what}]</span>')
        if n == "note" and out and c.get("target") and self.layer == "orig":
            n_, body = self.notes[-1]
            self.notes[-1] = (n_, f'{body} <span class="ch t-note ed">'
                                  f'[moved in the edition]</span>')
        if n == "anchor" and out:
            n_, body = self.notes[-1]
            self.notes[-1] = (n_, f'{body} <span class="ch t-note ed">'
                                  f'[moved here by the editor]</span>')
        return out

    def take_notes(self):
        notes, self.notes = self.notes, []
        if not notes:
            return ""
        items = "".join(
            f'<li id="{self.prefix}fn-{n}"><a href="#{self.prefix}nr-{n}">{n}.</a> '
            f'{curl(NOTEREF_GAP.sub(r"\1", body))}</li>' for n, body in notes)
        return f'<ol class="notes">{items}</ol>'


def rows(div, o, m):
    """(orig html, reg html, css class) for each block of a division."""
    out, page = [], ""
    for c in div:
        if not isinstance(c.tag, str):
            continue
        n = local(c)
        if n == "head":
            continue
        if n == "pb":
            if c.get("n"):
                page = f'<span class="pb">p.&#160;{html.escape(c.get("n"))}</span> '
            continue
        if n == "div" or (n == "q" and c.find(T + "p") is not None):
            if n == "div":
                oh, mh = o.heading(c), m.heading(c)
                if oh or mh:
                    out.append(("".join(oh), "".join(mh), "head"))
            out += rows(c, o, m)
            continue
        ob, mb = "".join(o.blocks([c])), "".join(m.blocks([c]))
        if not ob and not mb:
            continue
        if mb and c.get("prev"):
            mb = ('<span class="runon" title="the edition runs this on from the '
                  'paragraph before">↩ runs on</span>' + mb)
        out.append((page + ob + o.take_notes(), mb + m.take_notes(), ""))
        page = ""
    return out


def counts(div):
    c = collections.Counter()
    for reg in div.iter(T + "reg"):
        if reg.get("resp") == "#editor":
            c[reg.get("type") or "spelling"] += 1
    return c


CSS = """
:root { --bg:#fbfaf7; --fg:#222; --muted:#6b6b6b; --rule:#dedbd2; --panel:#f1eee6;
  --ed:#fde68a; --edln:#b45309; --auto:#7aa2d6; --gone:#c2410c; --pb:#8b7e66; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg:#1c1b19; --fg:#e7e4dc; --muted:#a19d93; --rule:#3a3833; --panel:#26241f;
  --ed:#5b4a12; --edln:#f5b041; --auto:#6c93c9; --gone:#fb923c; --pb:#b3a78d; } }
:root[data-theme="dark"] { --bg:#1c1b19; --fg:#e7e4dc; --muted:#a19d93; --rule:#3a3833;
  --panel:#26241f; --ed:#5b4a12; --edln:#f5b041; --auto:#6c93c9; --gone:#fb923c; --pb:#b3a78d; }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--fg);
  font:17px/1.55 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif; }
header.top { position:sticky; top:0; z-index:5; background:var(--panel);
  border-bottom:1px solid var(--rule); padding:8px 16px;
  font:14px/1.4 system-ui,sans-serif; }
header.top h1 { font-size:16px; margin:0 0 4px; }
.controls { display:flex; flex-wrap:wrap; gap:4px 14px; align-items:center; }
.controls label { white-space:nowrap; cursor:pointer; }
.controls select { font:inherit; }
nav.toc { padding:12px 16px; font:14px/1.6 system-ui,sans-serif; }
nav.toc a { color:inherit; }
main { max-width:1500px; margin:0 auto; padding:0 16px 80px; }
section.div { margin-top:36px; }
section.div > h2 { font-size:22px; margin:0 0 4px; }
.meta { font:13px/1.5 system-ui,sans-serif; color:var(--muted); margin-bottom:10px; }
.meta code { font-size:12px; }
.row { display:grid; grid-template-columns:1fr 1fr; gap:28px;
  padding:10px 0; border-top:1px solid var(--rule); }
.row.head { font-weight:600; }
.colhead { position:sticky; top:var(--hdr,64px); z-index:4; background:var(--bg);
  font:600 12px/1 system-ui,sans-serif; letter-spacing:.06em; text-transform:uppercase;
  color:var(--muted); padding:8px 0; border-top:none; }
.row p, .row h3 { margin:0 0 .5em; }
.row h3 { font-size:1em; }
.row ul, .row ol { margin:0 0 .5em; padding-left:1.6em; }
.orig { color:var(--fg); opacity:.88; }
.ch { border-radius:2px; }
.ch.ed { background:var(--ed); box-shadow:inset 0 -1px 0 var(--edln); }
.ch.auto { text-decoration:underline dotted var(--auto); text-underline-offset:3px; }
body.no-auto .ch.auto { text-decoration:none; }
.gone { color:var(--gone); font-weight:700; }
.pb { font:11px system-ui,sans-serif; color:var(--pb); border:1px solid var(--pb);
  border-radius:3px; padding:0 3px; vertical-align:2px; white-space:nowrap; }
body.no-pages .pb { display:none; }
.row.modern > .orig { font:italic 14px/1.4 system-ui,sans-serif; color:var(--muted); }
.reg section.notes { font-size:14px; line-height:1.45; color:var(--muted);
  border-top:1px dashed var(--rule); margin-top:.6em; padding-top:4px; }
.reg section.notes p { margin:0 0 .3em; }
.reg h2, .reg h3 { font-size:1.1em; margin:.2em 0 .5em; }
.runon { font:12px system-ui,sans-serif; color:var(--muted); margin-right:6px; }
ol.notes { font-size:14px; line-height:1.45; color:var(--muted); margin:.4em 0 0;
  padding-left:0; list-style:none; border-top:1px dashed var(--rule); padding-top:4px; }
ol.notes a, a.noteref { color:inherit; text-decoration:none; }
a.noteref sup { color:var(--edln); }
body.only-orig .row > .reg, body.only-reg .row > .orig { display:none; }
body.only-orig .row, body.only-reg .row { grid-template-columns:1fr; max-width:760px; }
@media (max-width:760px) {
  .row { grid-template-columns:1fr; gap:6px; }
  .row > .orig { border-left:3px solid var(--rule); padding-left:8px; font-size:15px; }
  .colhead { display:none; }
}
"""

JS = """
const b = document.body;
function hdr(){ document.documentElement.style.setProperty('--hdr',
  document.querySelector('header.top').offsetHeight + 'px'); }
addEventListener('resize', hdr); hdr();
document.querySelectorAll('input[data-t]').forEach(i => {
  const f = () => b.classList.toggle('hide-' + i.dataset.t, !i.checked);
  i.addEventListener('change', f); f(); });
const auto = document.getElementById('auto');
const fa = () => b.classList.toggle('no-auto', !auto.checked);
auto.addEventListener('change', fa); fa();
const pages = document.getElementById('pages');
const fp = () => b.classList.toggle('no-pages', !pages.checked);
pages.addEventListener('change', fp); fp();
const cols = document.getElementById('cols');
cols.addEventListener('change', () => {
  b.classList.toggle('only-orig', cols.value === 'orig');
  b.classList.toggle('only-reg', cols.value === 'reg'); });
"""


def page(title, year, sections, toc):
    hide = "".join(
        f"body.hide-{t} .ch.{t}{{background:none;box-shadow:none;text-decoration:none}}"
        f"body.hide-{t} .ch.{t} .gone{{display:none}}" for t, _, _ in TYPES)
    boxes = "".join(
        f'<label><input type="checkbox" data-t="{t}"{" checked" if on else ""}> {lab}</label>'
        for t, lab, on in TYPES)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} (side by side)</title>
<style>{CSS}{hide}</style></head>
<body>
<header class="top"><h1>{html.escape(title)}: printed {year} and edition</h1>
<div class="controls"><span>Mark editor changes:</span>{boxes}
<label><input type="checkbox" id="auto"> underline machine changes</label>
<label><input type="checkbox" id="pages" checked> printed pages</label>
<label>show <select id="cols"><option value="both">both columns</option>
<option value="orig">printed only</option><option value="reg">edition only</option></select></label>
</div></header>
<nav class="toc">{toc}</nav>
<main>{sections}</main>
<script>{JS}</script>
</body></html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tei")
    ap.add_argument("out")
    ap.add_argument("--chapters", default="chapters/typ",
                    help="where the editable files are, as shown on the page")
    ap.add_argument("--before", action="append", default=[],
                    help="modern page before the text (.typ or .html); repeatable")
    ap.add_argument("--after", action="append", default=[],
                    help="modern page after the text; repeatable")
    ap.add_argument("--typst-root",
                    help="Typst --root for .typ pages (default: the book folder)")
    a = ap.parse_args()
    root = etree.parse(a.tei).getroot()
    date = root.find(f".//{T}sourceDesc//{T}date")
    m_ = re.search(r"1[5-8]\d\d", "".join(date.itertext()) if date is not None else "")
    year = m_.group(0) if m_ else "print"
    o, m = ReviewR("orig", "o-", year), ReviewR("reg", "m-", year)
    o.index(root)
    m.index(root)
    sections, toc = [], []
    typst_root = Path(a.typst_root) if a.typst_root else Path(a.tei).resolve().parent.parent
    notes_used = [0]

    def modern(path, where):
        path = Path(path)
        if path.suffix == ".typ":
            frag, k = typst_page(path, typst_root, notes_used[0] + 1)
            notes_used[0] += k
        else:
            frag = path.read_text(encoding="utf-8").strip()
        ident = f"{where}-{re.sub(r'[^a-z0-9]+', '-', path.stem.lower())}"
        h = re.search(r"<h[1-6][^>]*>(.*?)</h[1-6]>", frag, re.S)
        name = html.unescape(re.sub(r"<[^>]+>", "", h.group(1))).strip() if h else path.stem
        sections.append(
            f'<section class="div" id="{ident}"><h2>{html.escape(name)}</h2>'
            f'<div class="meta">modern matter, not in the {year} text and not in the TEI'
            f' · edit <code>{html.escape(str(path))}</code></div>'
            f'<div class="row modern"><div class="orig">Not in the {year} printing.</div>'
            f'<div class="reg">{frag}</div></div></section>')
        toc.append(f'<a href="#{ident}">{html.escape(name)}</a>')

    for f in a.before:
        modern(f, "before")
    for div in root.iter(T + "div"):
        typ = div.get("type")
        if typ == "dedication":
            ident = "dedication"
        elif typ == "chapter":
            ident = f"chapter-{int(div.get('n')):02d}"
        else:
            continue
        mh = m.heading(div)
        oh = o.heading(div)
        name = re.sub(r"<[^>]+>", "", mh[0]) if mh else ident
        c = counts(div)
        summary = ", ".join(f"{v} {k}" for k, v in c.most_common()) or "none"
        body = [f'<section class="div" id="{ident}"><h2>{name}</h2>',
                f'<div class="meta">edit in <code>{html.escape(a.chapters)}/{ident}.typ'
                f'</code> · editor decisions: {summary}</div>',
                f'<div class="row colhead"><div>Printed {year}</div><div>Edition</div></div>',
                f'<div class="row head"><div class="orig">{"".join(oh)}</div>'
                f'<div class="reg">{"".join(mh)}</div></div>']
        rs = rows(div, o, m)
        for tr in following_trailers(div):
            rs.append(("".join(o.blocks([tr])), "".join(m.blocks([tr])), ""))
        for ob, mb, cls in rs:
            body.append(f'<div class="row {cls}"><div class="orig">{ob}</div>'
                        f'<div class="reg">{mb}</div></div>')
        body.append("</section>")
        sections.append("\n".join(body))
        toc.append(f'<a href="#{ident}">{html.escape(html.unescape(name))}</a>')
    for f in a.after:
        modern(f, "after")
    Path(a.out).write_text(
        page(tei_title(root), year, "\n".join(sections), " · ".join(toc)),
        encoding="utf-8")
    extra = len(a.before) + len(a.after)
    print(f"wrote {a.out}: {len(sections) - extra} divisions, {extra} modern pages")


if __name__ == "__main__":
    main()
