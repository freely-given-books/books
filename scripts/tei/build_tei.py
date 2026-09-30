#!/usr/bin/env python3
"""
Build an enriched TEI edition of an EEBO-TCP text.

  python3 build_tei.py SOURCE.xml OUT.xml [--review DIR] [--report FILE] [--tables FILE]

Book-specific tables (macron n/m, reconstructed gaps, nouns to lowercase,
report notes) live in the book's source/editorial.py, found next to SOURCE.

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
# Book-specific editorial tables: loaded from the book's source/editorial.py
# (see load_tables); these are the defaults for a book that has none.
# ---------------------------------------------------------------------------

# Macron abbreviations default to a suppressed "n"; these document-order
# indices expand to "m" instead (checked by hand against context).
MACRON_M = set()

# Illegible <gap>s reconstructed from context, keyed by document-order
# index of non-duplicate gaps: (letters, certainty, evidence note).
GAP_FIXES = {}

# Capitalized common nouns lowercased when not sentence-initial.
LOWERCASE_COMMON_NOUNS = set()

# Notes shown under "Please check" at the top of the report.
REPORT_NOTES = []


def load_tables(path):
    """Replace the tables above with those defined in a book's editorial.py."""
    import runpy
    ns = runpy.run_path(str(path))
    g = globals()
    for name in ("MACRON_M", "GAP_FIXES", "LOWERCASE_COMMON_NOUNS", "REPORT_NOTES"):
        if name in ns:
            g[name] = ns[name]

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
        if ref == "char:V":
            return p.text or "Ʋ"
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
    # long s and the hooked capital Ʋ (U/V) are letter forms, not spellings
    w = tok.expanded.replace("ſ", "s").replace("Ʋ", "U")
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
    elif t.kind == "spacing":
        ch = etree.Element(T + "choice")
        o = etree.SubElement(ch, T + "orig")
        o.text = t.pieces[0] or None
        r = etree.SubElement(ch, T + "reg")
        r.text = t.reg or None
        r.set("resp", "#editor")
        r.set("type", "spacing")
        b.elem(ch)
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
        fill_reg(r, t)
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
            fill_reg(r, t)
            r.set("resp", t.resp)
            if t.rtype:
                r.set("type", t.rtype)
            b.elem(ch)
        else:
            (b.elem if not isinstance(p, str) else b.text)(p)
    elif t.kind == "word":
        emit_word(b, t)
    for el in t.extra.get("notes_after", []) if t.kind in ("word", "punct") else []:
        b.elem(el)


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
        fill_reg(r, t)
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
                    t.reg = t.expanded.replace("ſ", "s")
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
                # a quotation standing between paragraphs is a block of its
                # own, unless it is made of paragraphs itself
                block_q = n == "q" and t.el.getparent() is not None and \
                    local(t.el.getparent()) == "div" and t.el.find(T + "p") is None
                if (n in BLOCK_MARK or block_q) and not list_only:
                    out.append((BLOCK_MARK.get(n, "¶"), "m", t, path))
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


def align(src, tgt, report, label, owner=None):
    """src: stream entries; tgt: [(text, kind)]. Returns (clusters,
    structure_ops). Each cluster: (list of Tok in order, target text list,
    target indices). If `owner` is a dict it is filled with
    target index -> source Tok that received that target word."""
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
    idx_for = {}
    struct = []

    def add_tgt(tok, words, idxs):
        tgt_for.setdefault(id(tok), []).extend(words)
        idx_for.setdefault(id(tok), []).extend(idxs)
        if owner is not None:
            for j in idxs:
                owner[j] = tok

    for op, i1, i2, j1, j2 in sm.get_opcodes():
        S = src[i1:i2]
        R = tgt[j1:j2]
        Sw = [s for s in S if s[1] == "w"]
        Rw = [r[0] for r in R if r[1] == "w"]
        Rwi = [j1 + k for k, r in enumerate(R) if r[1] == "w"]
        Sm = [s for s in S if s[1] == "m"]
        Rm = [r[0] for r in R if r[1] == "m"]
        if op == "equal":
            for k, (s, r) in enumerate(zip(S, R)):
                if s[1] == "w":
                    add_tgt(s[2], [r[0]], [j1 + k])
            continue
        # structure markers
        if Sm or Rm:
            def runs(seq, j0=None):
                out, cur = [], []
                for k, e in enumerate(seq):
                    if e[1] == "m":
                        out.append(cur)
                        cur = []
                    else:
                        cur.append((e, (j0 + k) if j0 is not None else None))
                out.append(cur)
                return out
            s_runs, r_runs = runs(S), runs(R, j1)
            if len(Sm) != len(Rm) and (not Sm or not Rm):
                # breaks on one side only (a paragraph split or merge):
                # cut the other side's words at the matching places
                many, one = (s_runs, r_runs) if Sm else (r_runs, s_runs)
                flat = one[0]
                mw = [e[0].lower() for run in many for e, _ in run]
                ow = [e[0].lower() for e, _ in flat]
                wm = difflib.SequenceMatcher(None, mw, ow, autojunk=False)
                wops = wm.get_opcodes()

                def cut(p):
                    for op, a1, a2, b1, b2 in wops:
                        if a1 <= p <= a2:
                            if op == "equal":
                                return b1 + (p - a1)
                            return b1 + round((p - a1) * (b2 - b1) / max(1, a2 - a1))
                    return len(ow)
                cuts, p = [], 0
                for run in many[:-1]:
                    p += len(run)
                    cuts.append(cut(p))
                pieces, last = [], 0
                for c in cuts + [len(flat)]:
                    c = max(c, last)
                    pieces.append(flat[last:c])
                    last = c
                if Sm:
                    r_runs = pieces
                else:
                    s_runs = pieces
            # where the structure change applies: the first source word of
            # the second run
            later = [e for run in s_runs[1:] for e, _ in run]
            nxt = later[0] if later else \
                next((s for s in src[i2:] if s[1] == "w"), None)
            if Sm and not later:
                k = next(k for k, s in enumerate(S) if s[1] == "m")
                nxt = next((s for s in src[i1 + k:] if s[1] == "w"), None)
            struct.append({"src_marks": [s[0] for s in Sm], "tgt_marks": Rm,
                           "at": nxt, "S": S, "R": R, "label": label})
            if len(s_runs) == len(r_runs):
                prev = next((s for s in reversed(src[:i1]) if s[1] == "w"), None)
                for n, (sr, rr) in enumerate(zip(s_runs, r_runs)):
                    words = [e[0] for e, _ in rr]
                    idxs = [j for _, j in rr]
                    if sr:
                        toks = [e[2] for e, _ in sr]
                        for t in toks:
                            uf.union(id(t), id(toks[0]))
                        add_tgt(toks[0], words, idxs)
                        for t in toks[1:]:
                            add_tgt(t, [], [])
                        prev = sr[-1][0]
                    elif words:
                        # inserted words: before a break they end the
                        # previous block; after one they begin the next
                        host = prev
                        if n > 0:
                            host = next((e for run in s_runs[n + 1:] for e, _ in run), None) \
                                or next((s for s in src[i2:] if s[1] == "w"), None) or prev
                        if host is not None:
                            add_tgt(host[2], words, idxs)
                            uf.union(id(host[2]), id(host[2]))
                continue
        if Sw:
            for s in Sw:
                uf.union(id(s[2]), id(Sw[0][2]))
            add_tgt(Sw[0][2], Rw, Rwi)
            for s in Sw[1:]:
                add_tgt(s[2], [], [])
        elif Rw:
            # pure insertion: attach to the previous source word token
            prev = next((s for s in reversed(src[:i1]) if s[1] == "w"), None)
            if prev is None:
                prev = next((s for s in src[i2:] if s[1] == "w"), None)
            if prev is not None:
                add_tgt(prev[2], Rw, Rwi)
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
        new, idxs = [], []
        for t in ts:
            new.extend(tgt_for.get(id(t), []))
            idxs.extend(idx_for.get(id(t), []))
        if cur != new:
            result.append((ts, new, idxs))
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


def join_sp(words, sps=None):
    """Join review words with the spacing the review had (sps[k]: space
    before word k), or by punctuation rules when that is unknown."""
    if sps is None:
        return join_tokens(words)
    out = ""
    for k, w in enumerate(words):
        out += (" " if k and sps[k] else "") + w
    return out


def apply_clusters(clusters, log, unresolved, label, placed=None, flag_of=None,
                   sp_of=None):
    """placed: target index -> [note elements] that the review puts after
    that target word. flag_of(j) / sp_of(j): the review's italic flag and
    space-before for target word j. A token (or group) that takes review
    words keeps them (extra["reg_words"], ["reg_sp"], ["reg_inner"],
    ["tflags"]) so its <reg> can be rebuilt with spacing, italics and notes."""
    placed = placed or {}

    def mark(t, js):
        if flag_of is not None:
            t.extra["tflags"] = [(j, flag_of(j)) for j in js]
        t.extra["tidx"] = list(js)

    def keep(t, words, js, inner):
        t.extra["reg_words"] = list(words)
        t.extra["reg_sp"] = [sp_of(j) for j in js] if sp_of else None
        if inner:
            t.extra["reg_inner"] = inner

    def joined(words, js):
        return join_sp(words, [sp_of(j) for j in js] if sp_of else None)

    for ts, new, idxs in clusters:
        inner = {k: placed[j] for k, j in enumerate(idxs) if j in placed}
        if any(in_container(t, ("trailer",)) for t in ts):
            continue
        # roman list labels are handled as structure
        if len(ts) == 2 and not new and ts[0].kind == "word" and \
                ROMAN_RE.match(ts[0].expanded or "") and ts[1].orig == ".":
            continue
        parts = [SPLIT_RE.findall(t.reg if t.reg is not None else t.orig or "") for t in ts]
        if len(ts) == 1:
            apply_to_token(ts[0], joined(new, idxs), log, label)
            mark(ts[0], idxs)
            keep(ts[0], new, idxs, inner)
            continue
        if all(len(p) == 1 for p in parts) and len(new) == len(ts):
            for k, (t, n) in enumerate(zip(ts, new)):
                if [n] != SPLIT_RE.findall(t.reg or t.orig or ""):
                    apply_to_token(t, n, log, label)
                mark(t, [idxs[k]])
                if k in inner:
                    t.extra["notes_after"] = inner[k]
            continue
        # several source tokens -> one emendation spanning them
        par = ts[0].parent
        sibs = par.children if par is not None else None
        if sibs is None or any(t.parent is not par for t in ts):
            # the tokens sit in different elements (e.g. an italic name and
            # a roman 's): share the reviewed text out over them instead
            if distribute(ts, new, log, label, idxs, mark, joined(new, idxs)):
                continue
            unresolved.append((label, " ".join(t.reg or t.orig for t in ts), join_tokens(new)))
            continue
        i0, i1 = ts[0].idx, ts[-1].idx
        span = sibs[i0:i1 + 1]
        g = Tok("group")
        g.children = span
        g.reg = joined(new, idxs)
        mark(g, idxs)
        keep(g, new, idxs, inner)
        g.resp, g.rtype = "#editor", "emendation"
        g.parent = par
        g.orig = "".join(x.orig or "".join(p for p in x.pieces if isinstance(p, str))
                         for x in span)
        sibs[i0:i1 + 1] = [g]
        for k, x in enumerate(sibs):
            x.idx = k
        log.append((label, "emendation", " ".join(t.reg or t.orig for t in ts), g.reg))


def distribute(ts, new, log, label, idxs=None, mark=None, tgt=None):
    """Cut the reviewed text into one piece per source token, by aligning
    characters, and apply each piece to its token."""
    cur = [(t.reg if t.reg is not None else t.orig or "") for t in ts]
    src = "".join(cur)
    tgt = tgt if tgt is not None else join_tokens(new)
    tgt_ns = tgt.replace(" ", "")
    sm = difflib.SequenceMatcher(None, src.lower(), tgt_ns.lower(), autojunk=False)
    ops = sm.get_opcodes()

    def mp(i):
        for op, i1, i2, j1, j2 in ops:
            if i1 <= i <= i2:
                if op == "equal":
                    return j1 + (i - i1)
                return j2 if i == i2 else j1
        return len(tgt_ns)
    bounds, pos = [], 0
    for c in cur:
        pos += len(c)
        bounds.append(mp(pos))
    bounds[-1] = len(tgt_ns)
    # map no-space offsets back into tgt (with spaces)
    ns_to_full = [ci for ci, ch in enumerate(tgt) if ch != " "] + [len(tgt)]
    start = 0
    pieces = []
    for b in bounds:
        b = max(b, start)
        pieces.append(tgt[ns_to_full[start]:ns_to_full[b]].strip() if start < len(ns_to_full) else "")
        start = b
    for t, piece in zip(ts, pieces):
        if piece != (t.reg if t.reg is not None else t.orig or ""):
            apply_to_token(t, piece, log, label)
    if mark is not None and idxs:
        # each review word goes to the token whose piece holds its first letter
        starts, pos = [], 0
        for w in new:
            starts.append(pos)
            pos += len(w)
        owners = {}
        for w_i, st in enumerate(starts):
            k = next((n for n, b in enumerate(bounds) if st < b), len(ts) - 1)
            owners.setdefault(k, []).append(idxs[w_i])
        for k, t in enumerate(ts):
            mark(t, owners.get(k, []))
    return True


def fill_reg(r, t):
    """Put a token's regularized reading into <reg> r: plain text, or text
    with italics and notes/anchors where the review has them."""
    words = t.extra.get("reg_words")
    ital = t.extra.get("reg_italic")
    inner = t.extra.get("reg_inner")
    if not words or not (ital or inner):
        r.text = t.reg
        return
    sps = t.extra.get("reg_sp")
    lead, trail = t.extra.get("pad", ("", ""))
    b = Builder(r)
    b.text(lead)
    run = None                              # [italic, text]

    def flush():
        nonlocal run
        if run:
            if run[0]:
                h = etree.Element(T + "hi")
                h.text = run[1]
                b.elem(h)
            else:
                b.text(run[1])
        run = None

    for k, w in enumerate(words):
        if k:
            space = sps[k] if sps is not None else w[:1] not in NO_SPACE_BEFORE
        else:
            space = False
        it = bool(ital[k]) if ital and k < len(ital) else False
        if run is not None and run[0] == it:
            run[1] += (" " if space else "") + w
        else:
            flush()
            if space:
                b.text(" ")
            run = [it, w]
        for el in (inner or {}).get(k, []):
            flush()
            b.elem(copy.deepcopy(el) if el.getparent() is not None else el)
    flush()
    b.text(trail)


# ---------------------------------------------------------------------------
# Spacing: the review's spaces between words the edition keeps apart
# ---------------------------------------------------------------------------

def is_changed(t):
    return t.kind == "group" or (t.kind in ("word", "punct") and t.resp == "#editor")


def apply_spacing(root_tok, order, sp, log, label, skip_notes=True, owner=None):
    """order: target indices in reading order with their block number,
    [(j, block)]; sp[j]: space before target word j in the review.
    Compare every pair of neighbouring review words owned by different
    tokens with the space between those tokens in the source, and record
    each difference as a spacing decision."""
    leaves = []

    def walk(t):
        for c in t.children or []:
            if c.kind == "container":
                if skip_notes and local(c.el) == "note":
                    leaves.append(c)        # a note between words: not a space
                    continue
                walk(c)
            else:
                leaves.append(c)
    walk(root_tok)
    pos = {id(x): i for i, x in enumerate(leaves)}
    j2leaf = {}
    in_group = {id(c): x for x in leaves if x.kind == "group" for c in x.children}
    for j, tok in (owner or {}).items():
        leaf = tok if id(tok) in pos else in_group.get(id(tok))
        if leaf is not None:
            j2leaf[j] = leaf
    for x in leaves:
        if x.kind in ("word", "punct", "group"):
            js = x.extra.get("tidx")
            if js is None and x.kind == "group":
                js = [j for c in x.children for j in c.extra.get("tidx", [])]
            for j in js or []:
                j2leaf[j] = x
    for (j, blk), (j2, blk2) in zip(order, order[1:]):
        if blk != blk2:
            continue
        a, b = j2leaf.get(j), j2leaf.get(j2)
        if a is None or b is None or a is b or id(a) not in pos or id(b) not in pos:
            continue
        ia, ib = pos[id(a)], pos[id(b)]
        if ia >= ib:
            continue
        between = leaves[ia + 1:ib]
        spaces = [x for x in between if x.kind == "space"]
        want = sp[j2]
        if want == bool(spaces):
            continue
        if want:
            if is_changed(b) and b.extra.get("tidx", [None])[0] == j2:
                pad(b, lead=" ")
            elif is_changed(a) and (a.extra.get("tidx") or [None])[-1] == j:
                pad(a, trail=" ")
            else:
                s = Tok("spacing", [""])
                s.reg = " "
                par = a.parent
                k = next(i for i, c in enumerate(par.children) if contains(c, a))
                par.children.insert(k + 1, s)
                relink(par)
            log.append((label, "spacing", "(none)", "space"))
        else:
            for x in spaces:
                x.kind = "spacing"
                x.reg = ""
            log.append((label, "spacing", "space", "(none)"))


def pad(t, lead="", trail=""):
    l0, t0 = t.extra.get("pad", ("", ""))
    t.extra["pad"] = (l0 + lead, t0 + trail)
    t.reg = lead + (t.reg or "") + trail


# ---------------------------------------------------------------------------
# Notes: aligned apart from the body, matched, and placed where the review
# puts them
# ---------------------------------------------------------------------------

def split_notes(entries):
    """Body entries, and [(note Tok, its entries, anchor)] where anchor is
    the number of body entries before the note."""
    body, notes = [], []
    cur = None
    for e in entries:
        note = next((c for c in e[3] if local(c.el) == "note"), None)
        if note is None:
            body.append(e)
            cur = None
            continue
        if cur is None or cur[0] is not note:
            cur = (note, [], len(body))
            notes.append(cur)
        if e[1] == "w":
            cur[1].append(e)
    return body, notes


def position_map(a, b):
    """Map positions (0..len) in sequence a to positions in b."""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    ops = sm.get_opcodes()

    def f(i):
        for op, i1, i2, j1, j2 in ops:
            if i1 <= i < i2 or (i == i2 and op == ops[-1][0] and (i1, i2) == ops[-1][1:3]):
                if op == "equal":
                    return j1 + (i - i1)
                return j1 + round((i - i1) * (j2 - j1) / max(1, i2 - i1))
        return len(b)
    return f


def match_notes(src, tgt, s2t):
    """Monotonic matching of printed notes to review notes by position and
    text. src: [(anchor_in_src, text)], tgt: [(anchor_in_tgt, text)].
    Returns list of (i or None, j or None)."""
    n, m = len(src), len(tgt)
    SKIP = 1.0
    mapped = [s2t(a) for a, _ in src]

    def cost(i, j):
        d = min(abs(mapped[i] - tgt[j][0]), 400) / 100
        sim = difflib.SequenceMatcher(None, src[i][1].lower(), tgt[j][1].lower()).ratio()
        return d + (1 - sim)

    INF = float("inf")
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    P = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF:
                continue
            if i < n and D[i][j] + SKIP < D[i + 1][j]:
                D[i + 1][j], P[i + 1][j] = D[i][j] + SKIP, (i, j, "s")
            if j < m and D[i][j] + SKIP < D[i][j + 1]:
                D[i][j + 1], P[i][j + 1] = D[i][j] + SKIP, (i, j, "t")
            if i < n and j < m:
                c = D[i][j] + cost(i, j)
                if c < D[i + 1][j + 1]:
                    D[i + 1][j + 1], P[i + 1][j + 1] = c, (i, j, "m")
    out, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj, k = P[i][j]
        out.append((pi if k in "ms" else None, pj if k in "mt" else None))
        i, j = pi, pj
    return out[::-1]


def insert_after(tok, el):
    """Put element `el` right after `tok` in the token tree (after the group
    that swallowed tok, if any)."""
    par = tok.parent
    kids = par.children
    k = next(i for i, c in enumerate(kids) if contains(c, tok))
    atom = Tok("atom", el=el)
    kids.insert(k + 1, atom)
    relink(par)


def insert_before(tok, el):
    par = tok.parent
    kids = par.children
    k = next(i for i, c in enumerate(kids) if contains(c, tok))
    kids.insert(k, Tok("atom", el=el))
    relink(par)


NOTE_SEQ = {"n": 0}


def division_trailers(div_el):
    """Trailers ("FINIS.") inside a division, or right after it."""
    out = [c for c in div_el if local(c) == "trailer"]
    sib = div_el.getnext()
    while sib is not None and local(sib) == "trailer":
        out.append(sib)
        sib = sib.getnext()
    return out


def keep_trailers(d, review, f, log):
    """A trailer is left out of the edition unless the review ends with it;
    then it is marked ana="#in-edition" (and, if it sits outside the
    division, taken out of the review so the rest aligns cleanly)."""
    for tr in division_trailers(d.el):
        words = [w.lower() for w in SPLIT_RE.findall(
            " ".join("".join(tr.itertext()).split()).replace("ſ", "s"))]
        k = max((i for i, e in enumerate(review.body) if e[1] == "m"), default=None)
        if k is None:
            continue
        tail = [e[0].lower() for e in review.body[k + 1:]]
        if tail != words:
            continue
        tr.set("ana", "#in-edition")
        tr.set("change", "#review")
        log.append((f, "trailer", " ".join(words), "kept in the edition"))
        if tr.getparent() is not d.el:
            del review.body[k:]


def review_division(d, review, f, log, unresolved):
    """Align one division with its review: body and notes separately."""
    entries = stream(d.children)
    body, notes = split_notes(entries)
    tgt = [(t, k) for t, k, _ in review.body]
    owner = {}
    cl, st = align(body, tgt, [], f, owner)
    tflags = {}            # id(tok) -> [(target index, italic flag)]
    for j, tok in owner.items():
        tflags.setdefault(id(tok), []).append((j, review.body[j][2]))
    s2t = position_map([e[0] for e in body], [t for t, _ in tgt])
    t2s = position_map([t for t, _ in tgt], [e[0] for e in body])

    src = [(a, " ".join(e[0] for e in es)) for _, es, a in notes]
    tn = [(n["anchor"], " ".join(t for t, _ in n["toks"])) for n in review.notes]
    pairs = match_notes(src, tn, s2t)

    note_spacing = []      # (note Tok, review note, owner) for the spacing pass
    placed = {}            # target index -> [elements to put after that word]
    after_tok = []         # (tok, element): anchors after unchanged words
    before_first = []      # elements before the first word of the division

    def prev_word(j):
        k = j - 1
        while k >= 0 and tgt[k][1] != "w":
            k -= 1
        return k

    for i, j in pairs:
        if i is None:                      # a note the editor added
            nt = review.notes[j]
            el = etree.Element(T + "note")
            el.set("ana", "#edition-only")
            el.set("resp", "#editor")
            el.set("change", "#review")
            el.text = join_tokens([t for t, _ in nt["toks"]])
            k = prev_word(nt["anchor"])
            (placed.setdefault(k, []) if k >= 0 else before_first).append(el)
            log.append((f, "note", "(none)", el.text))
            continue
        note_tok, es, a = notes[i]
        if j is None:                      # a printed note the editor dropped
            note_tok.el.set("ana", "#print-only")
            note_tok.el.set("change", "#review")
            log.append((f, "note", " ".join(e[0] for e in es), "(dropped)"))
            continue
        nt = review.notes[j]
        nowner = {}
        ncl, _ = align(es, [(t, "w") for t, _ in nt["toks"]], [], f + " note", nowner)
        for jj, tok in nowner.items():
            tflags.setdefault(id(tok), []).append((jj, nt["toks"][jj][1]))
        apply_clusters(ncl, log, unresolved, f + " note", None,
                       lambda jj, nt=nt: nt["toks"][jj][1], lambda jj, nt=nt: nt["sp"][jj])
        note_spacing.append((note_tok, nt, nowner))
        # does the review keep the note where it was printed?
        k = prev_word(nt["anchor"])
        src_prev = next((e for e in reversed(body[:a]) if e[1] == "w"), None)
        if k < 0 or src_prev is None:
            if k < 0 and src_prev is None:
                continue
        elif owner.get(k) is src_prev[2] and \
                max(x for x, o in owner.items() if o is src_prev[2]) == k:
            continue
        NOTE_SEQ["n"] += 1
        aid = f"rn{NOTE_SEQ['n']}"
        anchor = etree.Element(T + "anchor")
        anchor.set("{%s}id" % XML_NS, aid)
        anchor.set("change", "#review")
        note_tok.el.set("target", "#" + aid)
        note_tok.el.set("change", "#review")
        (placed.setdefault(k, []) if k >= 0 else before_first).append(anchor)
        log.append((f, "note moved", " ".join(e[0] for e in es)[:40],
                    "after '" + (tgt[k][0] if k >= 0 else "(start)") + "'"))

    apply_clusters(cl, log, unresolved, f, placed, lambda j: review.body[j][2],
                   lambda j: review.body_sp[j])
    # words the review left alone but put a note after
    in_cluster = {j for _ts, _n, idxs in cl for j in idxs}
    for k, els in placed.items():
        if k in in_cluster:
            continue
        tok = owner.get(k)
        if tok is None:
            unresolved.append((f, "note position", tgt[k][0]))
            continue
        for el in reversed(els):
            insert_after(tok, el)
    first = next((e for e in body if e[1] == "w"), None)
    for el in before_first:
        insert_before(first[2], el)
    apply_emphasis(d, tflags, log, f)
    order, blk = [], 0
    for j, (t, k, _) in enumerate(review.body):
        if k == "m":
            blk += 1
        else:
            order.append((j, blk))
    apply_spacing(d, order, review.body_sp, log, f, owner=owner)
    for note_tok, nt, nowner in note_spacing:
        apply_spacing(note_tok, [(jj, 0) for jj in range(len(nt["toks"]))], nt["sp"],
                      log, f + " note", skip_notes=False, owner=nowner)
    return st, body


# ---------------------------------------------------------------------------
# Emphasis: italics the review removed or added
# ---------------------------------------------------------------------------

INLINE = {"hi", "seg", "q", "foreign", "name", "bibl", "term", "ref", "label"}


def is_emph(t):
    return t.kind == "container" and local(t.el) == "hi" and t.el.get("rend") != "sup"


def apply_emphasis(d, tflags, log, f):
    """Compare italics with the review. A printed italic run (<hi>) with any
    word set roman in the review becomes ana="#print-only"; words italic in
    the review but roman in the edition are wrapped in <hi ana=
    "#edition-only">; a reading that is partly italic gets <hi> in its reg."""

    def want(t):
        """'i' italic, 'r' roman, 'x' no opinion, '' no target words;
        or 'm' for a reading whose words differ."""
        if t.kind not in ("word", "punct", "group"):
            return ""
        if "tflags" in t.extra:
            fl = t.extra["tflags"]
        elif t.kind == "group":
            fl = [x for c in t.children for x in sorted(tflags.get(id(c), []))]
        else:
            fl = sorted(tflags.get(id(t), []))
        vals = {("x" if not isinstance(v, bool) else "i" if v else "r") for _, v in fl}
        vals.discard("x")
        if not vals:
            return "x" if fl else ""
        if len(vals) == 1:
            return vals.pop()
        t.extra["reg_italic"] = [v is True for _, v in fl]
        return "m"

    def leaves(t, skip_notes=True):
        for c in t.children or []:
            if c.kind == "container":
                if skip_notes and local(c.el) == "note":
                    continue
                yield from leaves(c, skip_notes)
            elif c.kind in ("word", "punct", "group"):
                yield c

    # 1. printed italics the review set (partly) roman
    def walk_hi(t):
        for c in t.children or []:
            if c.kind != "container":
                continue
            if is_emph(c) and not c.el.get("ana"):
                ws = [want(x) for x in leaves(c)]
                if any(w in ("r", "m") for w in ws):
                    c.el.set("ana", "#print-only")
                    c.el.set("change", "#review")
                    log.append((f, "italic", "printed italic", "set roman"))
            walk_hi(c)
    walk_hi(d)

    # 2. italics the edition adds
    def walk_add(t, italic):
        kids = t.children or []
        need = []
        for c in kids:
            if c.kind == "container":
                if local(c.el) == "note":
                    need.append("break")
                    continue
                inner = [want(x) for x in leaves(c)]
                c_it = italic or (is_emph(c) and c.el.get("ana") != "#print-only")
                inline = local(c.el) in INLINE and not (
                    local(c.el) == "q" and local(c.el.getparent()) == "div")
                if inline and not c_it and inner and \
                        all(w in ("i", "x", "") for w in inner) and "i" in inner:
                    need.append("wrap")
                else:
                    need.append("break" if inner else "neutral")
            elif c.kind in ("word", "punct", "group"):
                w = want(c)
                if w == "m" and italic:
                    need.append("break")
                elif w == "i" and not italic:
                    need.append("wrap")
                elif w in ("x", "") and not italic:
                    need.append("neutral")
                else:
                    need.append("break")
            elif c.kind in ("space", "noise"):
                need.append("neutral")
            else:
                need.append("break")                  # anchors, notes, pb ...
        runs, k = [], 0
        while k < len(kids):
            if need[k] != "wrap":
                k += 1
                continue
            e = k
            while e + 1 < len(kids) and need[e + 1] in ("wrap", "neutral"):
                e += 1
            while need[e] != "wrap":
                e -= 1
            runs.append((k, e))
            k = e + 1
        for a, b in reversed(runs):
            h = new_container("hi")
            h.el.set("ana", "#edition-only")
            h.el.set("change", "#review")
            h.children = kids[a:b + 1]
            relink(h)
            kids[a:b + 1] = [h]
            h.parent = t
            log.append((f, "italic", "roman in print", "set italic"))
        relink(t)
        for c in kids:
            if c.kind == "container":
                walk_add(c, italic or (is_emph(c) and c.el.get("ana") != "#print-only"))
    walk_add(d, False)


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
    """splits: list of (tok, kind, label_toks, order, file). kind '+', '¶'
    or '>' (split there), 'quote' (the block is a quotation), 'merge' (the
    block continues the previous one)."""
    later = [s for s in splits if s[1] in ("quote", "merge")]
    splits = [s for s in splits if s[1] not in ("quote", "merge")]
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
                if kind == ">":
                    p.el.set("rend", "quote")
                    p.el.set("change", "#review")
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
    for tok, kind, _l, _o, f in sorted(later, key=lambda s: s[3]):
        # the innermost paragraph (a <q> may itself hold paragraphs)
        b = next((a for a in ancestors(tok) if local(a.el) == "p"), None) or block_of(tok)
        if b is None or local(b.el) not in ("p", "q"):
            log.append((f, "skipped", f"{kind} at '{tok.orig}'", "not a paragraph"))
            continue
        if kind == "quote":
            b.el.set("rend", "quote")
            b.el.set("change", "#review")
            log.append((f, "quotation", tok.orig, "block set as a quotation"))
            continue
        # merge: this block continues the previous one in the edition; both
        # stay separate elements (as printed), linked by @prev/@next
        kids = b.parent.children
        k = kids.index(b)
        prev = next((c for c in reversed(kids[:k]) if c.kind == "container"), None)
        if prev is None or local(prev.el) not in ("p", "q"):
            log.append((f, "skipped", f"merge at '{tok.orig}'", "no paragraph before it"))
            continue
        for x in (prev, b):
            if not x.el.get("{%s}id" % XML_NS):
                NOTE_SEQ["b"] = NOTE_SEQ.get("b", 0) + 1
                x.el.set("{%s}id" % XML_NS, f"rb{NOTE_SEQ['b']}")
        prev.el.set("next", "#" + b.el.get("{%s}id" % XML_NS))
        b.el.set("prev", "#" + prev.el.get("{%s}id" % XML_NS))
        b.el.set("change", "#review")
        log.append((f, "merge", "paragraph", f"joined to the previous one at '{tok.orig}'"))


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
        elif s["tgt_marks"] == [">"] and not s["src_marks"]:
            splits.append((tok, ">", [], order, s["label"]))
        elif s["tgt_marks"] == [">"] and s["src_marks"] == ["¶"]:
            splits.append((tok, "quote", [], order, s["label"]))
        elif s["src_marks"] == ["¶"] and not s["tgt_marks"] and \
                in_container(tok, ("trailer",)):
            continue          # a trailer the review left out
        elif s["src_marks"] == ["¶"] and not s["tgt_marks"]:
            splits.append((tok, "merge", [], order, s["label"]))
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
    # encodings added for editions that rework the text more (moved notes,
    # italics, merges ...): documented only when the file uses them
    used = [(xp, txt) for xp, txt in (
        (".//t:note[@target]", "note/@target points at the anchor where this edition "
         "places the note; the note itself stays where it was printed."),
        (".//t:reg[@type='spacing']", "reg[@type='spacing']: a space this edition adds "
         "(empty orig) or removes (empty reg) between words."),
        (".//t:*[@prev]", "@prev/@next link blocks this edition runs together into one "
         "paragraph; they stay separate elements as printed."),
        (".//t:p[@rend='quote']", "p[@rend='quote']: a paragraph this edition sets as a "
         "quotation."),
        (".//t:head[@type='short']", "head[@type='short']: the short form of this "
         "edition's title, used in running heads."),
        (".//t:reg/t:hi", "hi inside reg: words of this edition's reading set in italic."),
    ) if root.find(xp, {"t": NS}) is not None]
    paras += [txt for _, txt in used]
    cats = [(c, d) for c, d in (
        ("print-only", "in the printed text but not in this edition (italics set "
         "roman, a note dropped)"),
        ("edition-only", "added by this edition (italics, a note)"),
        ("in-edition", "a printed trailer this edition keeps (trailers are otherwise "
         "left out)"),
    ) if root.find(f".//*[@ana='#{c}']") is not None]
    for ptxt in paras:
        p = etree.SubElement(decl, T + "p")
        p.text = ptxt
    if cats:
        cd = etree.SubElement(ed, T + "classDecl")
        tx = etree.SubElement(cd, T + "taxonomy")
        tx.set("{%s}id" % XML_NS, "edition-layers")
        for c, d in cats:
            cat = etree.SubElement(tx, T + "category")
            cat.set("{%s}id" % XML_NS, c)
            cd_ = etree.SubElement(cat, T + "catDesc")
            cd_.text = d
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
# --list: the occurrences editorial.py is keyed on
# ---------------------------------------------------------------------------

def list_editorial(toks, width=6):
    """Print each macron abbreviation and non-duplicate gap in document order,
    numbered exactly as MACRON_M and GAP_FIXES index them, with the printed
    page (pb/@n, pb/@facs for the page image) and the words around it."""
    words, page = [], ("?", "")
    for kind, t in iter_stream(toks):
        if kind != "tok":
            continue
        if t.kind == "atom" and t.el is not None and local(t.el) == "pb":
            page = (t.el.get("n") or "?", t.el.get("facs") or "")
        if t.kind == "word":
            words.append((t, page))
    for i, (t, (pn, facs)) in enumerate(words):
        if not (t.macrons or t.gaps):
            continue
        before = " ".join(w.expanded for w, _ in words[max(0, i - width):i])
        after = " ".join(w.expanded for w, _ in words[i + 1:i + 1 + width])
        where = f"p.{pn} {facs}".strip() + (" note" if t.in_note else "")
        for idx, _ in t.macrons:
            m = "m" if idx in MACRON_M else "n"
            print(f"macron {idx:4d}  [{m}]  {t.expanded!r:18}  {where}\n"
                  f"        ... {before} [{t.expanded}] {after} ...")
        for idx, g in t.gaps:
            desc = g.find(T + "desc")
            shown = desc.text if desc is not None and desc.text else "•"
            fix = GAP_FIXES.get(idx)
            state = f"fixed {fix[0]!r} ({fix[1]}: {fix[2]})" if fix else f"OPEN {shown!r}"
            print(f"gap    {idx:4d}  {state}  {where}\n"
                  f"        ... {before} [{t.expanded}] {after} ...")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--list", action="store_true",
                    help="list every macron abbreviation and illegible gap with its "
                    "index, page and context (for filling in editorial.py), then stop")
    ap.add_argument("--review", help="folder with dedication.typ, chapter-NN.typ")
    ap.add_argument("--report", help="write a Markdown report of review decisions")
    ap.add_argument("--editor", default="Courtney Allen Hicks")
    ap.add_argument("--tables", help="book's editorial.py (default: editorial.py "
                    "next to SOURCE, if there is one)")
    args = ap.parse_args()
    if not args.list and not args.out:
        ap.error("OUT is required unless --list is given")
    tables = Path(args.tables) if args.tables else Path(args.source).parent / "editorial.py"
    if tables.exists():
        load_tables(tables)
    elif args.tables:
        ap.error(f"no such file: {tables}")

    src = etree.parse(args.source)
    tree = copy.deepcopy(src)
    root = tree.getroot()
    text = root.find(".//" + T + "text")
    toks = tokenize(text, {"macron": 0, "gap": 0})
    compute_auto(toks)
    if args.list:
        list_editorial(toks)
        return

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
        files = [("dedication.typ" if d.el.get("type") == "dedication"
                  else f"chapter-{int(d.el.get('n')):02d}.typ") for d in divs]
        order = 0
        for d, f in zip(divs, files):
            review = reviewparse.parse_review((R / f).read_text())
            heads = review.headings
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
            elif heads and (d.el.get("type") == "dedication" or not sub):
                d.extra["edition_head"] = heads[0]
            if review.short and review.short[0]:
                d.extra["short_head"] = review.short[0]
            keep_trailers(d, review, f, log)
            st, s = review_division(d, review, f, log, unresolved)
            index = {}
            for k, e in enumerate(s):
                index.setdefault(id(e[2]), order + k)
            order += len(s)
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
            if d.extra.get("short_head"):
                sh = etree.Element(T + "head")
                sh.set("type", "short")
                sh.set("change", "#review")
                sh.text = d.extra["short_head"]
                sh.tail = h.tail
                d.el.insert(idx + 1, sh)
    add_header(root, args.editor)
    tree.write(args.out, xml_declaration=True, encoding="UTF-8")

    if args.report:
        write_report(args.report, log, unresolved)
    print(f"wrote {args.out}: {len(log)} review decisions, "
          f"{len(unresolved)} unresolved")





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
