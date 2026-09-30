#!/usr/bin/env python3
"""
Extract Typst chapters from an (enriched) EEBO-TCP TEI file.

  python3 tei_extract.py EDITION.tei.xml OUTDIR --layer reg|orig [options]

--layer reg    the modern reading text: every <choice> gives its <reg>
               (or <expan>), editorial lists and headings are used.
--layer orig   the text as printed: every <choice> gives its <orig>
               (or <abbr>, with the macron shown), printed headings,
               printed list numerals.

Options:
  --expand            in the orig layer, show abbreviations expanded
                      (fro̅ -> from) instead of with the macron
  --mark-supplied     wrap reconstructed letters in ⟨ ⟩
  --only-auto         in the reg layer, ignore the editor's decisions and use
                      only the machine pass (for auditing the review)
  --show-gaps         in the orig layer, show illegible print as the TCP
                      transcribers marked it (•, 〈…〉) instead of the
                      reconstructed letters

Writes dedication.typ and chapter-NN.typ in OUTDIR (the layout used by
books/william-perkins/christian-economy in freely-given-books). Works on
the untouched TCP file too (it simply has no <choice> elements).
"""

import argparse
import copy
import re
from pathlib import Path

from lxml import etree

import layout

NS = "http://www.tei-c.org/ns/1.0"
T = "{%s}" % NS
ESC_RE = re.compile(r"([\\#\$\*_`<>@\[\]])")


def local(el):
    return etree.QName(el).localname if isinstance(el.tag, str) else None


def esc(s):
    return ESC_RE.sub(r"\\\1", s)


def block_start_escape(s):
    """Typst treats '1. ', '- ', '+ ', '= ' and '//' at the start of a
    block as markup; escape them."""
    s = re.sub(r"^(\d+)\.(\s)", r"\1\\.\2", s)
    s = re.sub(r"^([-+=])(\s)", r"\\\1\2", s)
    s = re.sub(r"^/(/)", r"\\/\1", s)
    return s


class R:
    def __init__(self, layer, expand=False, mark_supplied=False, only_auto=False,
                 show_gaps=False):
        self.show_gaps = show_gaps
        self.layer = layer
        self.moved = {}             # anchor id -> note placed there by the review
        self.expand = expand
        self.mark = mark_supplied
        self.only_auto = only_auto

    def index(self, root):
        """Notes the review moved: note[@target] is shown at its anchor in
        the reg layer and where it was printed in the orig layer."""
        for n in root.iter(T + "note"):
            tgt = n.get("target")
            if tgt and tgt.startswith("#"):
                self.moved[tgt[1:]] = n

    def note_shown(self, c):
        ana = c.get("ana")
        if self.layer == "reg":
            return ana != "#print-only" and not c.get("target")
        return ana != "#edition-only"

    # -- output format (Typst); tei_to_html.py overrides these ----------
    def esc(self, s):
        return esc(s)

    def after_call(self, prev):
        """Does prev end a Typst call (#emph[..], #footnote[..]), so that a
        following ( or [ would be read as more arguments?"""
        return prev.endswith("]") and not prev.endswith("\\]")

    def sup(self, inner):
        return f"#super[{inner}]"

    def emph(self, inner):
        return f"#emph[{block_start_escape(inner)}]"

    def footnote(self, body):
        return f"#footnote[{block_start_escape(body)}]"

    # -- inline ----------------------------------------------------------
    def inline(self, el, in_numbered=False):
        kids = list(el)
        lead = el.text or ""
        if kids and noise(lead, None, kids[0], leading=True):
            lead = ""
        parts = [("t", self.esc(lead))]
        for i, c in enumerate(kids):
            parts.append(("n" if local(c) in ("note", "anchor") else "e",
                          self.node(c, in_numbered)))
            nxt = kids[i + 1] if i + 1 < len(kids) else None
            raw_tail = c.tail or ""
            if noise(raw_tail, c, nxt):
                raw_tail = ""
            parts.append(("t", self.esc(raw_tail)))
        out = []
        for i, (k, s) in enumerate(parts):
            if k != "n" and s and s[0] in "([" and self.after_call("".join(out)):
                s = "\\" + s                 # "#emph[x](y)" would call emph again
            if k == "n" and s:
                before = "".join(out)
                after = "".join(x for _, x in parts[i + 1:])
                # footnote anchored between two words: keep the words apart
                if before[-1:].isspace() and after[:1].isalnum():
                    s += " "
            out.append(s)
        return "".join(out)

    def node(self, c, in_numbered=False):
        if not isinstance(c.tag, str):
            return ""                                    # comments
        n = local(c)
        if n == "choice":
            return self.choice(c)
        if n == "supplied":
            if self.show_gaps and self.layer == "orig":
                g = c.find(T + "gap")
                if g is not None:
                    return self.node(g)
            t = self.esc(c.text or "")
            return f"⟨{t}⟩" if self.mark else t
        if n == "gap":
            if c.get("reason") == "duplicate":
                return ""
            d = c.find(T + "desc")
            return self.esc(d.text if d is not None and d.text else "•")
        if n == "g":
            ref = c.get("ref")
            if ref in ("char:EOLhyphen", "char:EOLunhyphen"):
                return ""
            if ref == "char:abque":
                return "ꝗ"
            return self.esc(c.text or "")
        if n == "hi":
            inner = self.inline(c, in_numbered)
            if c.get("rend") == "sup":
                return self.sup(inner)
            ana = c.get("ana")
            if (ana == "#print-only" and self.layer == "reg") or \
                    (ana == "#edition-only" and self.layer == "orig"):
                return inner                 # italic in one layer only
            if not inner.strip():
                return inner
            lead = inner[:len(inner) - len(inner.lstrip())]
            trail = inner[len(inner.rstrip()):]
            return f"{lead}{self.emph(inner.strip())}{trail}"
        if n == "note":
            if not self.note_shown(c):
                return ""
            body = collapse(self.inline(c)).strip()
            return self.footnote(body) if body else ""
        if n == "anchor":
            note = self.moved.get(c.get("{http://www.w3.org/XML/1998/namespace}id"))
            if self.layer != "reg" or note is None:
                return ""
            body = collapse(self.inline(note)).strip()
            return self.footnote(body) if body else ""
        if n == "label":
            if self.layer == "reg" and in_numbered:
                return ""
            return self.inline(c)
        if n == "expan":                                   # TCP <expan><am/><ex/>
            if self.layer == "orig" and not self.expand:
                am = c.find(T + "am")
                return "".join(self.node(x) for x in am) if am is not None else ""
            ex = c.find(T + "ex")
            return self.esc(ex.text or "") if ex is not None else ""
        if n in ("pb", "lb", "milestone", "fw"):
            return ""
        if n == "table" and self.layer == "reg":
            # read into its sentence, column by column (layout.table_reading)
            _mode, blocks = layout.table_reading(c)
            return " ".join(self.inline(cell) for _m, cells in blocks for cell in cells)
        return self.inline(c, in_numbered)                 # seg, q, bibl, ...

    def choice(self, c):
        orig = c.find(T + "orig")
        regs = c.findall(T + "reg")
        reg = None
        if regs:
            ed = [x for x in regs if x.get("resp") == "#editor"]
            au = [x for x in regs if x.get("resp") == "#auto"]
            if self.only_auto:
                reg = au[0] if au else None
                if reg is None and orig is not None:
                    return self.inline(orig)
            else:
                reg = (ed or au or regs)[0]
        abbr, expan = c.find(T + "abbr"), c.find(T + "expan")
        if orig is not None and reg is not None:
            if self.layer == "reg":
                return self.inline(reg) if len(reg) else self.esc(reg.text or "")
            return self.inline(orig)
        if abbr is not None and expan is not None:
            if self.layer == "reg" or self.expand:
                if self.only_auto and expan.get("resp") and expan.get("resp") != "#auto":
                    return self.inline(abbr)
                return self.esc(expan.text or "")
            return self.inline(abbr)
        return self.inline(c)

    def auto_reading(self, orig):
        """In --only-auto mode, an editor reg falls back to the printed word
        (the machine pass either left it or it was an editor emendation)."""
        return self.inline(orig)

    # -- blocks ----------------------------------------------------------
    def para(self, el):
        return block_start_escape(collapse(self.inline(el)).strip())

    def list_block(self, lst, depth=0, lines=None):
        lines = [] if lines is None else lines
        numbered = lst.get("type") == "numbered"
        head = lst.find(T + "head")
        if head is not None and depth == 0:
            lines.append(f"#strong[{collapse(self.inline(head)).strip()}]")
            lines.append("")
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
            text_parts = [self.inline(body, numbered)]
            txt = collapse("".join(text_parts)).strip()
            if txt:
                if numbered and self.layer == "reg":
                    lines.append("  " * depth + "+ " + txt)
                elif numbered:
                    lines.append(txt)
                    lines.append("")
                else:
                    lines.append("  " * depth + "- " + block_start_escape(txt))
            for s in subs:
                self.list_block(s, depth + 1, lines)
        return lines


def collapse(s):
    return re.sub(r"\s+", " ", s)


def noise(text, prev, nxt, leading=False):
    """XML indentation that is not a real space: whitespace-only text with a
    newline between two g/gap elements (or before a first g/gap child).
    Only matters for raw TCP files; the enriched file has none inside words."""
    if not text or text.strip() or "\n" not in text:
        return False
    j = ("g", "gap", "supplied")
    if leading:
        return nxt is not None and local(nxt) in j
    return prev is not None and nxt is not None and local(prev) in j and local(nxt) in j


def div_blocks(r, div, level=2):
    """Render the non-heading content of a division as Typst lines."""
    lines = []
    enum_set = False
    for c in div:
        if not isinstance(c.tag, str):
            continue
        n = local(c)
        if n in ("head", "pb"):
            continue
        if n == "p" and layout.p_blocks(c):
            lines += split_p_lines(r, c)
        elif n == "p":
            t = r.para(c)
            if t and r.layer == "reg" and c.get("rend") == "quote":
                t = f"#quote[{t}]"
            add_block(r, lines, c, t)
        elif n == "list":
            if c.get("type") == "numbered" and r.layer == "reg" and not enum_set:
                lines += ['#set enum(numbering: "I.")', ""]
                enum_set = True
            lines += r.list_block(c)
            lines.append("")
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
                left = collapse(r.inline(before)).strip()
                right = collapse(r.node(last)).strip()
                lines += ["#linebreak()", "#linebreak()", "",
                          f"#align(left)[{left}]", "", f"#align(right)[{right}]", ""]
            else:
                lines += [f"#align(right)[{r.para(signed)}]", ""]
        elif n == "trailer":
            lines += trailer_lines(r, c)
        elif n == "div" and getattr(r, "levels", None) is not None:
            lines += div_lines(r, c, r.levels.get(c.get("type"), level + 1))
        elif n == "div" or (n == "q" and c.find(T + "p") is not None):
            lines += div_blocks(r, c)       # a quotation made of paragraphs too
        else:
            add_block(r, lines, c, r.para(c))
    return lines


def p_runs(p):
    """A paragraph split around its block children (layout.p_blocks):
    [("text", element holding a run of inline content) | ("block", element)].
    The runs are copies, so the paragraph itself is not changed."""
    blocks = layout.p_blocks(p)
    idx = {i for i, c in enumerate(p) if c in blocks}
    src = copy.deepcopy(p)
    out = []
    run = etree.Element(src.tag)
    run.text = src.text
    for i, child in enumerate(list(src)):
        if i not in idx:
            run.append(child)                 # moves it, tail and all
            continue
        out.append(("text", run))
        tail, child.tail = child.tail, None
        out.append(("block", child))
        run = etree.Element(src.tag)
        run.text = tail
    out.append(("text", run))
    return out


def table_lines(r, table):
    """A table as the edition sets it: in the reg layer a brace's labels as
    lines and its branches as a list (layout.table_reading); in the orig
    layer row by row, as printed."""
    lines = []
    if r.layer == "reg":
        _mode, blocks = layout.table_reading(table)
        for marker, cells in blocks:
            t = collapse(" ".join(r.inline(c) for c in cells)).strip()
            if not t:
                continue
            if marker == "+":
                lines.append("+ " + t)
            else:
                if lines and lines[-1] != "":
                    lines.append("")
                lines += [block_start_escape(t), ""]
    else:
        for row in table.findall(T + "row"):
            t = collapse(" ".join(r.inline(c) for c in row.findall(T + "cell"))).strip()
            if t:
                lines += [block_start_escape(t), ""]
    if lines and lines[-1] != "":
        lines.append("")
    return lines


def split_p_lines(r, p):
    lines = []
    for kind, el in p_runs(p):
        if kind == "text":
            t = r.para(el)
            if t:
                lines += [t, ""]
        elif local(el) == "table":
            lines += table_lines(r, el)
        else:
            lines += r.list_block(el) + [""]
    return lines


def div_lines(r, div, level):
    """Layout mode: a division with its heads (a heading line at `level`, or
    a bold run-in paragraph for RUN_IN_DIVS) and all it contains."""
    lines = []
    for h in div.findall(T + "head"):
        t = collapse(r.inline(h)).strip()
        if not t:
            continue
        if div.get("type") in r.run_in:
            lines += [f"#strong[{block_start_escape(t)}]", ""]
        else:
            lines += [f"{'=' * level} {t}", ""]
    return lines + div_blocks(r, div, level)


def part_lines(r, el, level):
    """Layout mode: one part of a file, a division or a loose block."""
    if local(el) == "div":
        return div_lines(r, el, r.levels.get(el.get("type"), level))
    return div_blocks(r, _Loose(el), level)


class _Loose:
    """Iterates as a division holding one element, without moving it."""

    def __init__(self, el):
        self.el = el

    def __iter__(self):
        return iter([self.el])


def add_block(r, lines, c, t):
    """A paragraph-like block; in the reg layer one with @prev (the review
    ran it on from the block before) joins that block's paragraph."""
    if not t:
        return
    if r.layer == "reg" and c.get("prev") and len(lines) >= 2 and lines[-1] == "":
        lines[-2] += " " + t
    else:
        lines += [t, ""]


def trailer_lines(r, c):
    """FINIS and the like: printed centred in the orig layer; in the reg
    layer only if the review kept it (ana="#in-edition")."""
    if r.layer == "orig":
        return [f"#align(center)[{r.para(c)}]", ""]
    if c.get("ana") == "#in-edition":
        return [r.para(c), ""]
    return []


def following_trailers(div):
    out, sib = [], div.getnext()
    while sib is not None and local(sib) == "trailer":
        out.append(sib)
        sib = sib.getnext()
    return out


def book_settings(tei_path):
    """Optional Typst settings from the book's source/editorial.py (next to
    the TEI): TYPST_PREAMBLE, a line put at the top of every chapter file,
    and TYPST_HEADING, a format string for chapter headings in the reg layer
    with {n}, {title} (head type=edition) and {short} (head type=short)."""
    import runpy
    ed = Path(tei_path).parent / "editorial.py"
    ns = runpy.run_path(str(ed)) if ed.exists() else {}
    return {k: ns[k] for k in ("TYPST_PREAMBLE", "TYPST_HEADING") if k in ns}


def heading_lines(r, div):
    heads = div.findall(T + "head")
    ed = next((h for h in heads if h.get("type") == "edition"), None)
    tpl = getattr(r, "settings", {}).get("TYPST_HEADING")
    if div.get("type") == "chapter" and r.layer == "reg" and ed is not None and tpl:
        short = next((h for h in heads if h.get("type") == "short"), None)
        title = collapse(r.inline(ed)).strip()
        return [tpl.format(n=div.get("n"), title=title,
                           short=collapse(r.inline(short)).strip() if short is not None
                           else title), ""]
    if div.get("type") == "chapter":
        sub = next((h for h in heads if h.get("type") == "sub"), None)
        first = next((h for h in heads if h.get("type") is None), None)
        if r.layer == "reg":
            t = collapse(r.inline(sub)).strip().rstrip(".") if sub is not None else ""
            return [f"== {div.get('n')}. {t}", ""]
        out = []
        if first is not None:
            out.append(f"== {collapse(r.inline(first)).strip()}")
        if sub is not None:
            out.append(f"#emph[{collapse(r.inline(sub)).strip()}]")
        return out + [""]
    ed = next((h for h in heads if h.get("type") == "edition"), None)
    printed = next((h for h in heads if h.get("type") is None), None)
    h = ed if (r.layer == "reg" and ed is not None) else printed
    return [f"== {collapse(r.inline(h)).strip()}", ""] if h is not None else []


def layout_file_lines(r, f, cfg, pre):
    """Layout mode: the Typst lines of one file (its title, then its parts)."""
    r.levels, run_in = layout.div_levels(cfg)
    r.run_in = run_in
    tpl = cfg.get("TYPST_HEADING")
    lines = list(pre)
    if f["title"]:
        title = esc(f["title"])
        short = esc(f["short"]) if f["short"] else title
        lines += [tpl.format(n="", title=title, short=short) if tpl
                  else f"== {title}", ""]
    for el in f["parts"]:
        lines += part_lines(r, el, 3)
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tei")
    ap.add_argument("outdir")
    ap.add_argument("--layer", choices=["reg", "orig"], default="reg")
    ap.add_argument("--expand", action="store_true")
    ap.add_argument("--mark-supplied", action="store_true")
    ap.add_argument("--only-auto", action="store_true")
    ap.add_argument("--show-gaps", action="store_true")
    a = ap.parse_args()
    r = R(a.layer, a.expand, a.mark_supplied, a.only_auto, a.show_gaps)
    root = etree.parse(a.tei).getroot()
    r.index(root)
    r.settings = book_settings(a.tei)
    pre = [r.settings["TYPST_PREAMBLE"], ""] if "TYPST_PREAMBLE" in r.settings else []
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    cfg = layout.settings(a.tei)
    files = layout.book_layout(root, cfg)
    if files is not None:
        for f in files:
            path = out / f["file"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(layout_file_lines(r, f, cfg, pre)) + "\n",
                            encoding="utf-8")
        print(f"wrote {len(files)} files to {out} ({a.layer} layer)")
        return
    n = 0
    for div in root.iter(T + "div"):
        typ = div.get("type")
        if typ == "dedication":
            name = "dedication.typ"
        elif typ == "chapter":
            name = f"chapter-{int(div.get('n')):02d}.typ"
        else:
            continue
        lines = pre + heading_lines(r, div) + div_blocks(r, div)
        for tr in following_trailers(div):
            lines += trailer_lines(r, tr)
        while lines and lines[-1] == "":
            lines.pop()
        (out / name).write_text("\n".join(lines) + "\n", encoding="utf-8")
        n += 1
    print(f"wrote {n} files to {out} ({a.layer} layer)")


if __name__ == "__main__":
    main()
