"""
Tokenizer for EEBO-TCP TEI mixed content.

Walks a TEI element's mixed content (text + inline elements) and splits it
into tokens without losing anything: every character and every element of
the source ends up in exactly one token, so the element can be rebuilt from
its tokens (optionally with <choice> wrappers added around some of them).

A *word* can span inline elements: a line-break hyphen
(<g ref="char:EOLhyphen"/>), a macron abbreviation mark
(<g ref="char:cmbAbbrStroke">), an illegible-text <gap>, a superscript
(y<hi rend="sup">e</hi>), a decorated initial (<seg rend="decorInit">),
or an <expan>. Container elements (hi, note, list, ...) are tokenized
recursively and appear as a single Container token in their parent.
"""

import re
from lxml import etree

NS = "http://www.tei-c.org/ns/1.0"
T = "{%s}" % NS

WORD_RE = re.compile(r"[\w'’]+|\s+|.", re.S)


def local(el):
    return etree.QName(el).localname if isinstance(el.tag, str) else None


def is_join_atom(el):
    """Elements that can sit inside a word."""
    n = local(el)
    if n == "g":
        return el.get("ref") in ("char:EOLhyphen", "char:EOLunhyphen",
                                 "char:cmbAbbrStroke", "char:abque",
                                 "char:V")          # Ʋ, a capital U/V letter form
    if n == "gap":
        return el.get("reason") != "duplicate"
    if n == "hi":
        return el.get("rend") == "sup"
    if n == "seg":
        return el.get("rend") == "decorInit"
    if n in ("expan", "supplied", "choice"):
        return True
    return False


def is_standalone_atom(el):
    """Elements that are neither word-internal nor containers."""
    n = local(el)
    if not isinstance(el.tag, str):          # comments / PIs
        return True
    if n in ("pb", "lb", "milestone", "fw"):
        return True
    if n == "gap" and el.get("reason") == "duplicate":
        return True
    if n == "g" and el.get("ref") == "char:punc":
        return True
    return False


class Tok:
    __slots__ = ("kind", "pieces", "el", "children", "parent", "idx",
                 "orig", "expanded", "reg", "resp", "rtype", "macrons",
                 "gaps", "in_note", "extra", "sent_start")

    def __init__(self, kind, pieces=None, el=None):
        self.kind = kind          # word | space | noise | punct | atom | container
        self.pieces = pieces or []  # list of str | element (word/punct/space)
        self.el = el              # element for atom/container/element-punct
        self.children = None      # token list for containers
        self.parent = None
        self.idx = None
        self.orig = None
        self.expanded = None
        self.reg = None
        self.resp = None
        self.rtype = None
        self.macrons = []         # list of (global_index, element)
        self.gaps = []            # list of (global_index, element)
        self.in_note = False
        self.extra = {}
        self.sent_start = False

    def __repr__(self):
        return f"<{self.kind} {self.orig!r}->{self.reg!r}>"


def _ws_noise(prev_el, next_el, text, leading):
    """Pretty-print indentation that is not a real space (see CLAUDE.md
    lesson 5): whitespace-only, contains a newline, and sits between two
    g/gap elements, or is an element's leading text before a g/gap."""
    if text.strip() or "\n" not in text:
        return False
    joinable = ("g", "gap")
    if leading:
        return next_el is not None and local(next_el) in joinable
    return (prev_el is not None and next_el is not None
            and local(prev_el) in joinable and local(next_el) in joinable)


def tokenize(el, counters, in_note=False, parent_tok=None):
    """Tokenize the direct mixed content of `el`, recursing into
    containers. `counters` tracks document-order indices of macrons and
    non-duplicate gaps. Returns a list of Tok."""
    items = []
    kids = list(el)
    if el.text:
        nxt = kids[0] if kids else None
        items.append(("noise" if _ws_noise(None, nxt, el.text, True) else "t", el.text))
    for i, c in enumerate(kids):
        items.append(("e", c))
        if c.tail:
            nxt = kids[i + 1] if i + 1 < len(kids) else None
            items.append(("noise" if _ws_noise(c, nxt, c.tail, False) else "t", c.tail))

    toks = []
    cur = None

    def close():
        nonlocal cur
        if cur is not None:
            toks.append(cur)
            cur = None

    for kind, val in items:
        if kind == "t":
            for m in WORD_RE.finditer(val):
                s = m.group(0)
                if re.match(r"[\w'’]", s):
                    if cur is None:
                        cur = Tok("word")
                    cur.pieces.append(s)
                elif s.isspace():
                    close()
                    toks.append(Tok("space", [s]))
                else:
                    close()
                    toks.append(Tok("punct", [s]))
        elif kind == "noise":
            if cur is not None:
                cur.pieces.append(("noise", val))
            else:
                toks.append(Tok("noise", [val]))
        else:
            c = val
            if not isinstance(c.tag, str):
                close()
                toks.append(Tok("atom", el=c))
            elif is_join_atom(c):
                if cur is None:
                    cur = Tok("word")
                cur.pieces.append(c)
                # count macrons/gaps inside this atom in document order
                for d in c.iter():
                    if not isinstance(d.tag, str):
                        continue
                    if local(d) == "g" and d.get("ref") == "char:cmbAbbrStroke":
                        cur.macrons.append((counters["macron"], d))
                        counters["macron"] += 1
                    if local(d) == "gap" and d.get("reason") != "duplicate":
                        cur.gaps.append((counters["gap"], d))
                        counters["gap"] += 1
            elif is_standalone_atom(c):
                close()
                if local(c) == "g":           # char:punc -> punctuation
                    toks.append(Tok("punct", [c]))
                else:
                    toks.append(Tok("atom", el=c))
            else:
                close()
                ct = Tok("container", el=c)
                ct.children = tokenize(c, counters,
                                       in_note or local(c) == "note", ct)
                toks.append(ct)
    close()
    for i, t in enumerate(toks):
        t.parent = parent_tok
        t.idx = i
        t.in_note = in_note
    return toks


def iter_stream(toks):
    """Depth-first reading-order iteration over word/punct tokens (and
    containers, yielded as ('open', tok) / ('close', tok) markers)."""
    for t in toks:
        if t.kind == "container":
            yield ("open", t)
            yield from iter_stream(t.children)
            yield ("close", t)
        else:
            yield ("tok", t)
