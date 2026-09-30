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
        self.expand = expand
        self.mark = mark_supplied
        self.only_auto = only_auto

    # -- inline ----------------------------------------------------------
    def inline(self, el, in_numbered=False):
        kids = list(el)
        lead = el.text or ""
        if kids and noise(lead, None, kids[0], leading=True):
            lead = ""
        parts = [("t", esc(lead))]
        for i, c in enumerate(kids):
            parts.append(("n" if local(c) == "note" else "e", self.node(c, in_numbered)))
            nxt = kids[i + 1] if i + 1 < len(kids) else None
            raw_tail = c.tail or ""
            if noise(raw_tail, c, nxt):
                raw_tail = ""
            parts.append(("t", esc(raw_tail)))
        out = []
        for i, (k, s) in enumerate(parts):
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
            t = esc(c.text or "")
            return f"⟨{t}⟩" if self.mark else t
        if n == "gap":
            if c.get("reason") == "duplicate":
                return ""
            d = c.find(T + "desc")
            return esc(d.text if d is not None and d.text else "•")
        if n == "g":
            ref = c.get("ref")
            if ref in ("char:EOLhyphen", "char:EOLunhyphen"):
                return ""
            if ref == "char:abque":
                return "ꝗ"
            return esc(c.text or "")
        if n == "hi":
            inner = self.inline(c, in_numbered)
            if c.get("rend") == "sup":
                return f"#super[{inner}]"
            if not inner.strip():
                return inner
            lead = inner[:len(inner) - len(inner.lstrip())]
            trail = inner[len(inner.rstrip()):]
            return f"{lead}#emph[{block_start_escape(inner.strip())}]{trail}"
        if n == "note":
            body = collapse(self.inline(c)).strip()
            return f"#footnote[{block_start_escape(body)}]" if body else ""
        if n == "label":
            if self.layer == "reg" and in_numbered:
                return ""
            return self.inline(c)
        if n == "expan":                                   # TCP <expan><am/><ex/>
            if self.layer == "orig" and not self.expand:
                am = c.find(T + "am")
                return "".join(self.node(x) for x in am) if am is not None else ""
            ex = c.find(T + "ex")
            return esc(ex.text or "") if ex is not None else ""
        if n in ("pb", "lb", "milestone", "fw"):
            return ""
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
                return esc(reg.text or "")
            return self.inline(orig)
        if abbr is not None and expan is not None:
            if self.layer == "reg" or self.expand:
                if self.only_auto and expan.get("resp") and expan.get("resp") != "#auto":
                    return self.inline(abbr)
                return esc(expan.text or "")
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
                    lines.append("  " * depth + "- " + txt)
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


def div_blocks(r, div):
    """Render the non-heading content of a division as Typst lines."""
    lines = []
    enum_set = False
    for c in div:
        if not isinstance(c.tag, str):
            continue
        n = local(c)
        if n in ("head", "pb"):
            continue
        if n == "p":
            t = r.para(c)
            if t:
                lines += [t, ""]
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
            if r.layer == "orig":
                lines += [f"#align(center)[{r.para(c)}]", ""]
        elif n == "div":
            lines += div_blocks(r, c)
        else:
            t = r.para(c)
            if t:
                lines += [t, ""]
    return lines


def heading_lines(r, div):
    heads = div.findall(T + "head")
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
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for div in root.iter(T + "div"):
        typ = div.get("type")
        if typ == "dedication":
            name = "dedication.typ"
        elif typ == "chapter":
            name = f"chapter-{int(div.get('n')):02d}.typ"
        else:
            continue
        lines = heading_lines(r, div) + div_blocks(r, div)
        while lines and lines[-1] == "":
            lines.pop()
        (out / name).write_text("\n".join(lines) + "\n", encoding="utf-8")
        n += 1
    print(f"wrote {n} files to {out} ({a.layer} layer)")


if __name__ == "__main__":
    main()
