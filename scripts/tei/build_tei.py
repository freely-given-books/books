#!/usr/bin/env python3
"""
Build an enriched TEI edition of an EEBO-TCP text.

  python3 build_tei.py SOURCE.xml OUT.xml [--review DIR] [--report FILE]

Starting from the untouched TCP transcription, this adds editorial layers
*inside* the same file, without removing anything from the original:

  <choice><abbr>fro&#x304;</abbr><expan>from</expan></choice>   macron abbreviations
  <supplied reason="illegible" ...>eu</supplied>                  reconstructed letters
  <choice><orig>mariage</orig><reg>marriage</reg></choice>        modern spelling

and, if --review points at a folder of reviewed Typst chapters (the
dedication.typ + chapter-NN.typ layout used in freely-given-books), aligns
that reviewed text against the automatic modernization and records every
review decision as its own <reg resp="#editor">, so the enriched file
reproduces the reviewed reading text while keeping the 1609 original
extractable word for word.
"""

import argparse
import copy
import difflib
import re
import unicodedata
from datetime import date
import sys
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).parent))
from teitok import NS, T, Tok, local, tokenize, iter_stream  # noqa: E402
from spelling import (modernize_word_lower, apply_case_pattern,  # noqa: E402
                      GRAMMAR_EXCEPTIONS)
import reviewparse  # noqa: E402

XML_NS = "http://www.w3.org/XML/1998/namespace"

# ---------------------------------------------------------------------------
# Book-specific editorial tables (A09377, Christian Oeconomie)
# ---------------------------------------------------------------------------

# Macron abbreviations default to a suppressed "n"; these document-order
# indices expand to "m" instead (checked by hand against context).
MACRON_M = {4, 29, 31, 35, 51, 53, 62, 72, 75, 78, 79, 81, 87, 88, 93,
            109, 113, 115, 132, 141, 144, 146, 151}

# Illegible <gap>s reconstructed from context, keyed by document-order
# index of non-duplicate gaps: (letters, certainty, evidence note).
GAP_FIXES = {
    3: ("eu", "high", "1 Tim. 2:8, 'pray every where'"),
    4: ("w", "high", "1 Tim. 2:8, 'without wrath'"),
    5: ("st", "high", "custome"),
    6: ("ti", "high", "times"),
    7: ("t", "high", "Gen. 18:19, 'that they keep'"),
    8: ("t", "high", "Gen. 18:19, 'righteousness'"),
    9: ("G", "high", "citation Gen. 18. 19."),
    11: ("i", "high", "it is"),
    12: ("e", "high", "maxim: diu deliberandum quod semel statuendum"),
    13: ("t", "high", "maxim: diu deliberandum quod semel statuendum"),
    14: ("b", "high", "canon-law formula: in verbis de praesenti"),
    15: ("praesenti", "medium", "canon-law formula: in verbis de praesenti"),
    16: ("i", "high", "de iure, glossed 'in regard of right'"),
    17: ("u", "high", "lawfull"),
    19: ("5", "low", "Augustine, De Civ. Dei lib. 15 cap. 16 (digit uncertain)"),
    20: ("a", "high", "in stead"),
    21: ("o", "high", "blood"),
    22: ("o", "high", "Epistol."),
    24: ("e", "high", "cousin-german"),
    25: ("it", "medium", "it forbiddeth"),
    26: ("en", "high", "children"),
    27: ("e", "high", "the mother"),
    28: ("i", "high", "Marie"),
    29: ("i", "high", "maxim: cuius nuptias inire non licet"),
    30: ("g", "high", "maxim: eius nec coniugis licet"),
    31: ("r", "high", "formerly"),
    32: ("nta", "high", "maintaining"),
    34: ("r", "high", "mariage (this text's spelling)"),
    36: ("su", "high", "succeeding"),
    37: ("r", "high", "seueritie"),
    38: ("8", "medium", "Matt. 18:15, on rebuking a brother"),
}

LOWERCASE_COMMON_NOUNS = {
    "family", "familie", "contract", "marriage", "mariage", "society",
    "societie", "societies", "common", "line", "case", "nature", "rules",
    "rule", "argument", "author", "education", "sacrament", "baptisme",
    "baptism", "concubine", "bride", "wife", "wiues", "wives", "children",
    "husbands", "husband", "master", "masters", "servant", "servants",
    "seruant", "seruants", "goodwife", "mother", "image", "signe", "sign",
    "generall", "general", "proper", "honour", "honor", "mistresse",
    "mistress", "state", "states", "commonwealth", "parent", "parents",
}

ROMAN_RE = re.compile(r"^(?=[IVXLC]+$)M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",
                      re.I)


# ---------------------------------------------------------------------------
# Word strings
# ---------------------------------------------------------------------------

def piece_text(p, tok, mode):
    """mode: 'dipl' (as printed/transcribed) or 'exp' (abbreviations
    expanded, reconstructed letters supplied)."""
    if isinstance(p, str):
        return p
    if isinstance(p, tuple):              # ("noise", ws)
        return ""
    n = local(p)
    if n == "g":
        ref = p.get("ref")
        if ref == "char:cmbAbbrStroke":
            if mode == "dipl":
                return p.text or "̄"
            idx = next(i for i, e in tok.macrons if e is p)
            return "m" if idx in MACRON_M else "n"
        if ref == "char:abque":
            return "ꝗ" if mode == "dipl" else "que"
        return ""                          # EOL(un)hyphen
    if n == "gap":
        idx = next(i for i, e in tok.gaps if e is p)
        desc = p.find(T + "desc")
        d = desc.text if desc is not None and desc.text else "•"
        if mode == "exp" and idx in GAP_FIXES:
            return GAP_FIXES[idx][0]
        return d
    if n == "expan":
        if mode == "dipl":
            am = p.find(T + "am")
            return "".join(piece_text(c, tok, mode) for c in am) if am is not None else ""
        ex = p.find(T + "ex")
        return ex.text if ex is not None else ""
    # hi rend=sup, seg decorInit: plain text content
    return "".join(p.itertext())


SUP_EXPANSIONS = {"e": "the", "t": "that", "u": "thou"}


def word_strings(tok):
    tok.orig = "".join(piece_text(p, tok, "dipl") for p in tok.pieces)
    tok.expanded = "".join(piece_text(p, tok, "exp") for p in tok.pieces)
    # y with superscript letter (the thorn contraction): y^e = the, y^t = that
    m = re.fullmatch(r"([yY])([etu])", tok.orig)
    if m and any(not isinstance(p, (str, tuple)) and local(p) == "hi" for p in tok.pieces):
        e = SUP_EXPANSIONS[m.group(2)]
        tok.expanded = e.capitalize() if m.group(1) == "Y" else e


def auto_reg(tok, sentence_start, heading=False):
    """Automatic modern spelling for one word of main text."""
    w = tok.expanded
    if any(not isinstance(p, (str, tuple)) and local(p) == "hi" for p in tok.pieces):
        return w                     # y^e -> the (already expanded)
    if not re.fullmatch(r"[A-Za-z']+", w):
        return w
    low = w.lower()
    if ROMAN_RE.match(w) and w.isupper():
        return w                     # list labels I. II. III.
    # decorated initial artifact: CHristian -> Christian
    if len(w) > 2 and w[0].isupper() and w[1].isupper() and w[2:].islower():
        w = w[0] + w[1:].lower()
    if low in GRAMMAR_EXCEPTIONS:
        mod = low
    else:
        mod = modernize_word_lower(low)
    if heading:
        return apply_case_pattern(w, mod)
    if sentence_start:
        return mod[:1].upper() + mod[1:] if not w.isupper() or len(w) == 1 \
            else apply_case_pattern(w, mod)
    if w[:1].isupper() and mod in LOWERCASE_COMMON_NOUNS:
        return mod
    return apply_case_pattern(w, mod)


# ---------------------------------------------------------------------------
# Rebuild an element from (possibly annotated) tokens
# ---------------------------------------------------------------------------

class Builder:
    def __init__(self, el):
        self.el = el

    def text(self, s):
        if not s:
            return
        if len(self.el):
            last = self.el[-1]
            last.tail = (last.tail or "") + s
        else:
            self.el.text = (self.el.text or "") + s

    def elem(self, e):
        e.tail = None
        self.el.append(e)


def put_pieces(b, pieces, tok, keep_noise=False):
    for p in pieces:
        if isinstance(p, str):
            b.text(p)
        elif isinstance(p, tuple):
            # pretty-print indentation inside a word is not a real space;
            # drop it so the enriched file reads correctly without heuristics
            if keep_noise:
                b.text(p[1])
        else:
            n = local(p)
            if n == "gap":
                idx = next(i for i, e in tok.gaps if e is p)
                if idx in GAP_FIXES or idx in tok.extra.get("gapfill", {}):
                    b.elem(make_supplied(p, idx, tok))
                    continue
            b.elem(p)


def make_supplied(gap, idx, tok):
    fill = tok.extra.get("gapfill", {}).get(idx)
    if fill is not None:
        letters, cert, note, resp = fill
    else:
        letters, cert, note = GAP_FIXES[idx]
        resp = "#auto"
    s = etree.Element(T + "supplied")
    s.set("reason", gap.get("reason", "illegible"))
    s.set("cert", cert)
    s.set("resp", resp)
    s.text = letters
    # keep the original <gap> inside for full provenance
    g = copy.deepcopy(gap)
    g.tail = None
    s.append(etree.Comment(" " + note + " "))
    s.append(g)
    s[-1].tail = None
    return s


def rebuild(el, toks):
    for c in list(el):
        el.remove(c)
    el.text = None
    b = Builder(el)
    for t in toks:
        emit(b, t)


def emit(b, t):
    if t.kind in ("space", "noise"):
        b.text(t.pieces[0])
    elif t.kind == "atom":
        b.elem(t.el)
    elif t.kind == "container":
        rebuild(t.el, t.children)
        b.elem(t.el)
    elif t.kind == "group":
        ch = etree.Element(T + "choice")
        o = etree.SubElement(ch, T + "orig")
        ob = Builder(o)
        for sub in t.children:
            emit(ob, sub)
        r = etree.SubElement(ch, T + "reg")
        r.text = t.reg
        r.set("resp", t.resp)
        if t.rtype:
            r.set("type", t.rtype)
        b.elem(ch)
    elif t.kind == "punct":
        p = t.pieces[0]
        if t.reg is not None and t.reg != t.orig:
            ch = etree.Element(T + "choice")
            o = etree.SubElement(ch, T + "orig")
            ob = Builder(o)
            (ob.elem if not isinstance(p, str) else ob.text)(p)
            r = etree.SubElement(ch, T + "reg")
            r.text = t.reg
            r.set("resp", t.resp)
            if t.rtype:
                r.set("type", t.rtype)
            b.elem(ch)
        else:
            (b.elem if not isinstance(p, str) else b.text)(p)
    elif t.kind == "word":
        emit_word(b, t)


def emit_word(b, t):
    has_abbr = bool(t.macrons) or any(
        not isinstance(p, (str, tuple)) and local(p) in ("expan",) for p in t.pieces)
    has_sup = any(not isinstance(p, (str, tuple)) and local(p) == "hi" for p in t.pieces)
    changed = t.reg is not None and t.reg != t.extra.get("expan", t.expanded)

    def put_orig(target):
        ob = Builder(target)
        if has_abbr or has_sup:
            ch = etree.SubElement(target, T + "choice")
            a = etree.SubElement(ch, T + "abbr")
            put_pieces(Builder(a), t.pieces, t)
            e = etree.SubElement(ch, T + "expan")
            e.text = t.extra.get("expan", t.expanded)
            if t.extra.get("expan_resp"):
                e.set("resp", t.extra["expan_resp"])
        else:
            put_pieces(ob, t.pieces, t)

    auto = t.extra.get("auto_reg")
    if t.resp == "#editor" and auto is not None and auto != t.reg:
        changed = True
    if changed:
        ch = etree.Element(T + "choice")
        o = etree.SubElement(ch, T + "orig")
        put_orig(o)
        r = etree.SubElement(ch, T + "reg")
        r.text = t.reg
        r.set("resp", t.resp or "#auto")
        if t.rtype:
            r.set("type", t.rtype)
        # keep the machine's proposal next to the editor's decision
        base = t.extra.get("expan", t.expanded)
        if t.resp == "#editor" and auto is not None and auto not in (t.reg, base):
            r2 = etree.SubElement(ch, T + "reg")
            r2.text = auto
            r2.set("resp", "#auto")
            r2.set("type", "spelling")
        b.elem(ch)
    elif has_abbr or has_sup:
        tmp = etree.Element("tmp")
        put_orig(tmp)
        for c in list(tmp):
            b.elem(c)
    else:
        put_pieces(b, t.pieces, t)


# ---------------------------------------------------------------------------
# Reading stream (what the modern text says, token by token)
# ---------------------------------------------------------------------------

SPLIT_RE = reviewparse.TOKEN_RE
BLOCK_MARK = {"p": "¶", "item": "-", "signed": "¶", "trailer": "¶"}


def compute_auto(toks):
    """Fill tok.orig/expanded/reg for every word/punct token.

    Main text gets automatic modern spelling with the same sentence-case
    rules the earlier Typst renderer used (so an unreviewed file reads the
    same as before): the first word of a paragraph/item/signature, or the
    first word after a . ! or ?, is capitalized; a short list of common
    nouns that the 1609 printing capitalized mid-sentence is lowercased.
    Footnotes are left in original spelling (abbreviations expanded only).
    Division headings keep their printed case pattern."""
    state = {"start": True}

    def walk(ts, in_note, in_head):
        for t in ts:
            if t.kind == "container":
                n = local(t.el)
                if n in ("p", "item", "signed", "trailer") or n == "head":
                    state["start"] = True
                # legacy quirk kept for continuity: an italic boundary right
                # after a full stop did not start a new sentence
                is_emph = n == "hi" and t.el.get("rend") != "sup"
                if is_emph:
                    state["start"] = False
                saved = state["start"]
                is_div_head = n == "head" and t.el.getparent() is not None \
                    and local(t.el.getparent()) == "div"
                walk(t.children, in_note or n == "note", in_head or is_div_head)
                if n == "note":
                    state["start"] = saved
                if is_emph:
                    state["start"] = False
            elif t.kind == "word":
                word_strings(t)
                t.resp, t.rtype = "#auto", "spelling"
                if in_note:
                    t.reg = t.expanded
                    continue
                if in_head:
                    t.reg = auto_reg(t, False, heading=True)
                else:
                    t.sent_start = state["start"]
                    t.reg = auto_reg(t, state["start"])
                    if re.search(r"[A-Za-z]", t.expanded):
                        state["start"] = False
            elif t.kind == "punct":
                p = t.pieces[0]
                t.orig = p if isinstance(p, str) else (p.text or "")
                t.reg = t.orig
                if not in_note and not in_head:
                    state["start"] = t.orig in ".!?"
    walk(toks, False, False)


def stream(toks, skip_heads=True):
    """Flatten tokens to [(text, kind, tok, container_path)]; kind 'w' or 'm'."""
    out = []

    def walk(ts, path):
        for t in ts:
            if t.kind == "container":
                n = local(t.el)
                if skip_heads and n == "head" and local(t.el.getparent()) == "div":
                    continue
                # an item that only wraps a nested list continues the
                # previous item (that is how the Typst lists are nested)
                list_only = n == "item" and all(
                    c.kind in ("space", "noise") or
                    (c.kind == "container" and local(c.el) == "list")
                    for c in t.children)
                if n in BLOCK_MARK and not list_only:
                    out.append((BLOCK_MARK[n], "m", t, path))
                walk(t.children, path + (t,))
            elif t.kind in ("word", "punct"):
                txt = t.reg if t.reg is not None else t.orig
                for s in SPLIT_RE.findall(txt or ""):
                    out.append((s, "w", t, path))
    walk(toks, ())
    return out


# ---------------------------------------------------------------------------
# Alignment with the reviewed text
# ---------------------------------------------------------------------------

class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        self.p[self.find(a)] = self.find(b)


def align(src, tgt, report, label):
    """src: stream entries; tgt: [(text, kind)]. Returns (clusters,
    structure_ops). Each cluster: (list of Tok in order, target text list)."""
    a = [s[0] for s in src]
    b = [t[0] for t in tgt]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    uf = UF()
    tok_order = []
    seen = set()
    for s in src:
        if s[1] == "w" and id(s[2]) not in seen:
            seen.add(id(s[2]))
            tok_order.append(s[2])
    # target words assigned per source word-token (by id), in order
    tgt_for = {}
    struct = []

    def add_tgt(tok, words):
        tgt_for.setdefault(id(tok), []).extend(words)

    for op, i1, i2, j1, j2 in sm.get_opcodes():
        S = src[i1:i2]
        R = tgt[j1:j2]
        Sw = [s for s in S if s[1] == "w"]
        Rw = [r[0] for r in R if r[1] == "w"]
        Sm = [s for s in S if s[1] == "m"]
        Rm = [r[0] for r in R if r[1] == "m"]
        if op == "equal":
            for s, r in zip(S, R):
                if s[1] == "w":
                    add_tgt(s[2], [r[0]])
            continue
        # structure markers
        if Sm or Rm:
            # position: the first source word after this op
            nxt = next((s for s in src[i1:] if s[1] == "w"), None)
            struct.append({"src_marks": [s[0] for s in Sm], "tgt_marks": Rm,
                           "at": nxt, "S": S, "R": R, "label": label})
        if Sw:
            for s in Sw:
                uf.union(id(s[2]), id(Sw[0][2]))
            add_tgt(Sw[0][2], Rw)
            for s in Sw[1:]:
                add_tgt(s[2], [])
        elif Rw:
            # pure insertion: attach to the previous source word token
            prev = next((s for s in reversed(src[:i1]) if s[1] == "w"), None)
            if prev is None:
                prev = next((s for s in src[i2:] if s[1] == "w"), None)
            if prev is not None:
                add_tgt(prev[2], Rw)
                uf.union(id(prev[2]), id(prev[2]))
                report.append(f"[{label}] insertion after '{prev[0]}': {' '.join(Rw)}")
    # build clusters in reading order
    clusters = {}
    order = []
    for t in tok_order:
        r = uf.find(id(t))
        if r not in clusters:
            clusters[r] = []
            order.append(r)
        clusters[r].append(t)
    result = []
    for r in order:
        ts = clusters[r]
        cur = []
        for t in ts:
            cur.extend(SPLIT_RE.findall(t.reg if t.reg is not None else t.orig or ""))
        new = []
        for t in ts:
            new.extend(tgt_for.get(id(t), []))
        if cur != new:
            result.append((ts, new))
    return result, struct


# ---------------------------------------------------------------------------
# Applying review decisions
# ---------------------------------------------------------------------------

NO_SPACE_BEFORE = set(".,;:!?)]’'")
NO_SPACE_AFTER = set("([")


def join_tokens(ts):
    out = ""
    for t in ts:
        if not out:
            out = t
        elif t[:1] in NO_SPACE_BEFORE or out[-1:] in NO_SPACE_AFTER \
                or unicodedata.category(t[:1]).startswith("M"):
            out += t
        else:
            out += " " + t
    return out


def classify(old, new):
    if old.lower() == new.lower():
        return "case"
    if " " in new or " " in old:
        return "emendation"
    return "spelling"


def ancestors(tok):
    a = []
    p = tok.parent
    while p is not None:
        a.append(p)
        p = p.parent
    return a


def in_container(tok, names):
    return any(local(a.el) in names for a in ancestors(tok))


def recompute_word(t):
    word_strings(t)
    # expanded with editor gap fills
    parts = []
    for p in t.pieces:
        if not isinstance(p, (str, tuple)) and local(p) == "gap":
            idx = next(i for i, e in t.gaps if e is p)
            if idx in t.extra.get("gapfill", {}):
                parts.append(t.extra["gapfill"][idx][0])
                continue
        parts.append(piece_text(p, t, "exp"))
    t.expanded = "".join(parts)


def try_gapfill(t, target):
    """If a word containing illegible <gap>s was filled in by the editor,
    work out the letters that go in the gap."""
    if len(t.gaps) != 1:
        return False
    idx, gap = t.gaps[0]
    pre, post, seen = "", "", False
    for p in t.pieces:
        if p is gap:
            seen = True
            continue
        s = piece_text(p, t, "exp")
        if seen:
            post += s
        else:
            pre += s
    if target.startswith(pre) and target.endswith(post) and \
            len(target) >= len(pre) + len(post):
        letters = target[len(pre):len(target) - len(post)] if post else target[len(pre):]
        t.extra.setdefault("gapfill", {})[idx] = (
            letters, "high", "filled in by the editor from the page image", "#editor")
        recompute_word(t)
        return True
    return False


def try_macron_flip(t, target):
    """The editor corrected an n/m macron expansion (e.g. 'fron' -> 'from')."""
    for i, (idx, g) in enumerate(t.macrons):
        was_m = idx in MACRON_M
        letter = "n" if was_m else "m"
        parts = []
        for p in t.pieces:
            if p is g:
                parts.append(letter)
            else:
                parts.append(piece_text(p, t, "exp"))
        cand = "".join(parts)
        low = cand.lower()
        auto = apply_case_pattern(cand, modernize_word_lower(low))
        if target.lower() in (cand.lower(), auto.lower()):
            t.extra["expan"] = cand
            t.extra["expan_resp"] = "#editor"
            t.expanded = cand
            return True
    return False


def apply_to_token(t, target, log, label):
    if t.kind == "word" and "auto_reg" not in t.extra:
        t.extra["auto_reg"] = t.reg
    if t.kind == "punct":
        log.append((label, "punctuation", t.orig, target))
        t.reg, t.resp, t.rtype = target, "#editor", "punctuation"
        return
    old = t.reg
    if t.gaps and try_gapfill(t, target):
        log.append((label, "gap", old, target))
        t.reg, t.resp, t.rtype = target, "#editor", "spelling"
        return
    if t.macrons and try_macron_flip(t, target):
        log.append((label, "expansion", old, target))
        t.reg, t.resp, t.rtype = target, "#editor", "spelling"
        return
    t.reg, t.resp, t.rtype = target, "#editor", classify(old or "", target)
    log.append((label, t.rtype, old, target))


def apply_clusters(clusters, log, unresolved, label):
    for ts, new in clusters:
        if any(in_container(t, ("trailer",)) for t in ts):
            continue
        # roman list labels are handled as structure
        if len(ts) == 2 and not new and ts[0].kind == "word" and \
                ROMAN_RE.match(ts[0].expanded or "") and ts[1].orig == ".":
            continue
        parts = [SPLIT_RE.findall(t.reg if t.reg is not None else t.orig or "") for t in ts]
        if len(ts) == 1:
            apply_to_token(ts[0], join_tokens(new), log, label)
            continue
        if all(len(p) == 1 for p in parts) and len(new) == len(ts):
            for t, n in zip(ts, new):
                if [n] != SPLIT_RE.findall(t.reg or t.orig or ""):
                    apply_to_token(t, n, log, label)
            continue
        # several source tokens -> one emendation spanning them
        par = ts[0].parent
        sibs = par.children if par is not None else None
        if sibs is None or any(t.parent is not par for t in ts):
            unresolved.append((label, " ".join(t.reg or t.orig for t in ts), join_tokens(new)))
            continue
        i0, i1 = ts[0].idx, ts[-1].idx
        span = sibs[i0:i1 + 1]
        g = Tok("group")
        g.children = span
        g.reg = join_tokens(new)
        g.resp, g.rtype = "#editor", "emendation"
        g.parent = par
        g.orig = "".join(x.orig or "".join(p for p in x.pieces if isinstance(p, str))
                         for x in span)
        sibs[i0:i1 + 1] = [g]
        for k, x in enumerate(sibs):
            x.idx = k
        log.append((label, "emendation", " ".join(t.reg or t.orig for t in ts), g.reg))


# ---------------------------------------------------------------------------
# Structure: paragraphs split and run-in "I. ... II. ..." made into lists
# ---------------------------------------------------------------------------

def contains(ct, tok):
    if ct is tok:
        return True
    if ct.kind in ("container", "group") and ct.children:
        return any(contains(c, tok) for c in ct.children)
    return False


def new_container(tag, like=None):
    el = etree.Element(T + tag)
    if like is not None:
        for k, v in like.attrib.items():
            el.set(k, v)
    t = Tok("container", el=el)
    t.children = []
    return t


def relink(ct):
    for k, c in enumerate(ct.children):
        c.parent, c.idx = ct, k


def has_content(ts):
    return any(t.kind not in ("space", "noise") for t in ts)


def split_container(ct, tok):
    kids = ct.children
    i = next(k for k, c in enumerate(kids) if contains(c, tok))
    c = kids[i]
    if c is tok or c.kind == "group":
        left, right = kids[:i], kids[i:]
    else:
        cl, cr = split_container(c, tok)
        left = kids[:i] + ([cl] if has_content(cl.children) else [])
        right = [cr] + kids[i + 1:]
    r = new_container(local(ct.el), like=ct.el)
    ct.children, r.children = left, right
    relink(ct)
    relink(r)
    return ct, r


def block_of(tok):
    a = tok.parent
    while a is not None and not (a.el.getparent() is not None and
                                 local(a.el.getparent()) == "div"):
        a = a.parent
    return a


def wrap_label(labels):
    """Put the printed list numeral (e.g. 'II' + '.') in a <label>,
    wherever it sits (directly in the item or inside an italic run)."""
    par = labels[0].parent
    if par is None or labels[1].parent is not par:
        return False
    kids = par.children
    i0 = next(k for k, c in enumerate(kids) if c is labels[0])
    i1 = next(k for k, c in enumerate(kids) if c is labels[1])
    lab = new_container("label")
    lab.children = kids[i0:i1 + 1]
    relink(lab)
    par.children = kids[:i0] + [lab] + kids[i1 + 1:]
    relink(par)
    return True


def restructure(splits, log):
    """splits: list of (tok, kind, label_toks, order, file). kind '+' or '¶'."""
    by_block = {}
    for s in splits:
        b = block_of(s[0])
        if b is None or local(b.el) != "p":
            log.append((s[4], "skipped", f"new {s[1]} before '{s[0].orig}'",
                        "not a paragraph (e.g. a list heading); kept as is"))
            continue
        by_block.setdefault(id(b), (b, []))[1].append(s)
    for b, pts in by_block.values():
        pts.sort(key=lambda s: s[3])
        div = b.parent
        cleaned = [(b, None)]
        cur = b
        for tok, kind, labels, _o, _f in pts:
            _left, right = split_container(cur, tok)
            cleaned.append((right, (kind, labels)))
            cur = right
        # first segment keeps the original kind (ordinary paragraph)
        out = []
        lst = None
        first = True
        for ct, meta in cleaned:
            if first:
                first = False
                if has_content(ct.children):
                    out.append(ct)
                continue
            kind, labels = meta
            if kind == "+":
                item = new_container("item")
                kids = ct.children
                if labels:
                    wrap_label(labels)
                    kids = ct.children
                item.children = kids
                relink(item)
                if lst is None:
                    lst = new_container("list")
                    lst.el.set("type", "numbered")
                    lst.el.set("change", "#review")
                    out.append(lst)
                if lst.children:
                    lst.children.append(Tok("space", ["\n"]))
                lst.children.append(item)
                relink(lst)
            else:
                lst = None
                p = new_container("p")
                p.children = ct.children
                relink(p)
                out.append(p)
        # replace b in its div with out (separated by newlines)
        i = div.children.index(b)
        repl = []
        for k, t in enumerate(out):
            if k:
                repl.append(Tok("space", ["\n"]))
            repl.append(t)
        div.children[i:i + 1] = repl
        relink(div)
        log.append((pts[0][4], "split", "paragraph",
                    f"{len(cleaned) - 1} split(s) at " +
                    ", ".join((s[2][0].orig if s[2] else s[0].orig) for s in pts)))


def collect_splits(struct, stream_index, log):
    splits = []
    for s in struct:
        at = s["at"]
        if at is None:
            continue
        tok = at[2]
        Sw = [x for x in s["S"] if x[1] == "w"]
        order = stream_index.get(id(tok), 0)
        if s["tgt_marks"] == ["+"] and not s["src_marks"]:
            labels = []
            if len(Sw) >= 2 and ROMAN_RE.match(Sw[0][0]) and Sw[1][0] == ".":
                labels = [Sw[0][2], Sw[1][2]]
            splits.append((labels[0] if labels else tok, "+", labels, order, s["label"]))
        elif s["tgt_marks"] == ["¶"] and not s["src_marks"]:
            if in_container(tok, ("closer", "signed", "trailer")):
                continue
            splits.append((tok, "¶", [], order, s["label"]))
        elif s["src_marks"] == ["-"] and not s["tgt_marks"]:
            continue          # list nesting shown differently; list kept as-is
        elif s["src_marks"] == ["¶"] and not s["tgt_marks"] and \
                in_container(tok, ("trailer",)):
            continue
        else:
            log.append(("structure", "unresolved", str(s["src_marks"]),
                        str(s["tgt_marks"]) + " at " + (tok.orig or "")))
    return splits


# ---------------------------------------------------------------------------
# Book-specific repair of the review copy (not adopted as review edits)
# ---------------------------------------------------------------------------

CH05_LIST = """+ Whole brothers, that is, brothers by the same father and mother, or half brothers, that is, brethren by the same father, but not by the same mother. Again whole sisters by the same father or mother, or half sisters by one of them and not by both.
+ The brothers children or cousin germans; that is, the uncles sons or daughters, or the aunts sons or daughters. The sisters children, or cousin germans; that is, the aunts sons or daughters, which are the children of two sisters.
+ The cousin german, the son of the great uncle by the fathers or mothers side, and the cousin german the son of the great aunt, by the fathers or mothers side. The cousin-german the daughter of the great uncle, by the fathers or mothers side, and the cousin german, the daughter of the great aunt by the same sides."""


def repair_review(name, text, log):
    if name == "chapter-05.typ":
        start = text.find("Kinsmen of this line, are,\n")
        if start >= 0:
            s2 = text.find("\n", start) + 1
            end = text.find("daughter of the great aunt by the same sides.", s2)
            if end > 0 and " brothers, that is, brothers by the same fat\n" in text[s2:end]:
                end += len("daughter of the great aunt by the same sides.")
                text = text[:s2] + "\n" + CH05_LIST + text[end:]
                log.append(("chapter-05.typ", "repair",
                            "'Kinsmen of this line, are,' list",
                            "damaged block (words cut mid-line) rebuilt from the "
                            "source as items I-III; please check"))
    return text


# ---------------------------------------------------------------------------
# TEI header additions
# ---------------------------------------------------------------------------

def add_header(root, editor_name):
    hdr = root.find(T + "teiHeader")
    fd = hdr.find(T + "fileDesc")
    ts = fd.find(T + "titleStmt")
    for xid, resp, name in (
            ("editor", "review of modernized spelling, emendations, list structure",
             editor_name),
            ("auto", "automatic spelling modernization, abbreviation expansion and "
             "reconstruction of illegible letters (build_tei.py)", "Machine pass")):
        rs = etree.SubElement(ts, T + "respStmt")
        r = etree.SubElement(rs, T + "resp")
        r.text = resp
        n = etree.SubElement(rs, T + "name")
        n.set("{%s}id" % XML_NS, xid)
        n.text = name
    ed = hdr.find(T + "encodingDesc")
    if ed is None:
        ed = etree.Element(T + "encodingDesc")
        hdr.insert(list(hdr).index(fd) + 1, ed)
    decl = etree.SubElement(ed, T + "editorialDecl")
    paras = [
        "This file is the EEBO-TCP transcription with editorial layers added "
        "inline; nothing of the transcription has been removed.",
        "choice/orig holds the text as printed; choice/reg holds the modern "
        "reading. reg/@resp says who decided it (#auto = machine, #editor = "
        "reviewed by hand); reg/@type is spelling, case, punctuation or emendation. "
        "Where the editor overrode the machine, the editor's reg comes first and "
        "the machine's proposal follows as a second reg[@resp='#auto'].",
        "choice/abbr + choice/expan: macron abbreviations (e.g. frō = from) "
        "and superscript contractions (yᵉ = the).",
        "supplied: letters or words lost to illegible print, with @cert and a "
        "comment giving the evidence; the TCP gap element is kept inside.",
        "Spelling regularized: u/v, i/j, silent final e, doubled consonants, "
        "-ie to -y, -nesse to -ness, and a word list. Grammatical forms "
        "(hath, doth, thou, thee, thy, ye, shalt, wilt, art, hast, dost) are "
        "retained. Footnote text is left in original spelling.",
        "list[@change='#review']: run-in enumerations (I. ... II. ...) set out as "
        "numbered lists; the printed numerals are kept in label.",
        "head[@type='edition']: section title used by this edition; the printed "
        "heading is kept in the preceding head. @change='#review' points at "
        "the revisionDesc entry for these structural changes.",
        "Line breaks are those of the TCP transcription (newlines in the text; "
        "g[@ref='char:EOLhyphen'] marks a word hyphenated at line end). "
        "pb/@n is the printed page, pb/@facs the page image.",
    ]
    for ptxt in paras:
        p = etree.SubElement(decl, T + "p")
        p.text = ptxt
    rd = hdr.find(T + "revisionDesc")
    if rd is None:
        rd = etree.SubElement(hdr, T + "revisionDesc")
    ch = etree.Element(T + "change")
    ch.set("{%s}id" % XML_NS, "review")
    ch.set("when", date.today().isoformat())
    ch.set("who", "#editor")
    ch.text = "Enriched edition built from the TCP file and the reviewed Typst chapters."
    ch.tail = rd.text
    rd.insert(0, ch)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("out")
    ap.add_argument("--review", help="folder with dedication.typ, chapter-NN.typ")
    ap.add_argument("--report", help="write a Markdown report of review decisions")
    ap.add_argument("--editor", default="Courtney Allen Hicks")
    args = ap.parse_args()

    src = etree.parse(args.source)
    tree = copy.deepcopy(src)
    root = tree.getroot()
    text = root.find(".//" + T + "text")
    toks = tokenize(text, {"macron": 0, "gap": 0})
    compute_auto(toks)

    divs = []

    def find(ts):
        for t in ts:
            if t.kind == "container":
                if local(t.el) == "div" and t.el.get("type") in ("dedication", "chapter"):
                    divs.append(t)
                find(t.children)
    find(toks)

    log, unresolved, all_splits = [], [], []
    if args.review:
        R = Path(args.review)
        files = ["dedication.typ"] + [f"chapter-{i:02d}.typ" for i in range(1, 19)]
        order = 0
        for d, f in zip(divs, files):
            raw = repair_review(f, (R / f).read_text(), log)
            heads, tg = reviewparse.parse_typ(raw)
            # headings
            sub = [c for c in d.children if c.kind == "container" and
                   local(c.el) == "head" and c.el.get("type") == "sub"]
            if sub and heads:
                title = re.sub(r"^\d+\.\s*", "", heads[0])
                hs = stream(sub[0].children, skip_heads=False)
                if hs and hs[-1][0] == ".":
                    hs = hs[:-1]
                ht = [(x, "w") for x in SPLIT_RE.findall(title)]
                hc, _ = align(hs, ht, [], f + " heading")
                apply_clusters(hc, log, unresolved, f + " heading")
            elif heads and d.el.get("type") == "dedication":
                d.extra["edition_head"] = heads[0]
            s = stream(d.children)
            index = {}
            for k, e in enumerate(s):
                index.setdefault(id(e[2]), order + k)
            order += len(s)
            ins = []
            cl, st = align(s, tg, ins, f)
            apply_clusters(cl, log, unresolved, f)
            all_splits += collect_splits(st, index, log)
        restructure(all_splits, log)

    rebuild(text, toks)
    for d in divs:
        if d.extra.get("edition_head"):
            h = etree.Element(T + "head")
            h.set("type", "edition")
            h.set("change", "#review")
            h.text = d.extra["edition_head"]
            first = d.el.find(T + "head")
            idx = list(d.el).index(first) + 1 if first is not None else 0
            h.tail = first.tail if first is not None else "\n"
            d.el.insert(idx, h)
    add_header(root, args.editor)
    tree.write(args.out, xml_declaration=True, encoding="UTF-8")

    if args.report:
        write_report(args.report, log, unresolved)
    print(f"wrote {args.out}: {len(log)} review decisions, "
          f"{len(unresolved)} unresolved")


REPORT_NOTES = [
    "chapter-05.typ: the #linebreak() before 'Concerning affinity' is layout, "
    "not text, so it is not stored in the TEI. Add it back in your template "
    "or the extracted file if you want the extra space.",
    "chapter-10 heading: your title drops ', and of due benevolence'. The "
    "printed heading is kept in orig; the shortened title is your reg.",
    "In the orig layer, the run-in lists you set out (I. ... II. ...) come out "
    "as separate paragraphs with their printed numerals. Extract the "
    "untouched TCP file itself for the exact 1609 paragraphing.",
]


def write_report(path, log, unresolved):
    from collections import Counter, defaultdict
    kinds = Counter(k for _, k, *_ in log)
    lines = ["# Review decisions carried into the enriched TEI", ""]
    lines += ["## Please check", ""] + [f"- {n}" for n in REPORT_NOTES] + [""]
    lines.append("| kind | count |")
    lines.append("| --- | --- |")
    for k, n in kinds.most_common():
        lines.append(f"| {k} | {n} |")
    lines.append("")
    groups = defaultdict(list)
    for e in log:
        groups[e[1]].append(e)
    for k in ["repair", "unresolved", "split", "skipped", "gap", "expansion",
              "emendation", "punctuation", "case", "spelling"]:
        if k not in groups:
            continue
        lines.append(f"## {k}")
        lines.append("")
        if k in ("spelling", "case"):
            c = Counter((e[2], e[3]) for e in groups[k])
            for (a, b), n in sorted(c.items(), key=lambda x: (-x[1], x[0])):
                lines.append(f"- {a} → {b}" + (f" (×{n})" if n > 1 else ""))
        else:
            for e in groups[k]:
                lines.append(f"- [{e[0]}] {e[2]} → {e[3]}")
        lines.append("")
    if unresolved:
        lines.append("## not applied")
        lines.append("")
        for f, a, b in unresolved:
            lines.append(f"- [{f}] {a} → {b}")
    Path(path).write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
