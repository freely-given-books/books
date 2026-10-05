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
from spelling import (modernize_word_lower, apply_case_pattern, AMBIGUOUS_NAMES,  # noqa: E402
                      GRAMMAR_EXCEPTIONS)
import reviewparse  # noqa: E402
import layout  # noqa: E402
import sources  # noqa: E402

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

# Margin notes modernized as well, keeping their capitals as printed (the
# default keeps notes in original spelling, abbreviations expanded).
MODERNIZE_NOTES = False

# Latin found per run of text (the words between two pieces of markup): a run
# of LATIN_MIN_WORDS or more that is mostly not English, even modernized, is
# left as printed. Without it only the words in spelling.LATIN_SKIP are safe.
LATIN_RUNS = False
LATIN_MIN_WORDS = 4

# Greek/Hebrew the transcribers could not key (<gap reason="foreign">): left
# out of the reading text, with the punctuation it leaves stranded (reg/@type
# "omission"; the orig layer keeps the placeholder).
DROP_FOREIGN_GAPS = False

# Text for the reading layer in place of a gap of another kind, by reason,
# e.g. {"missing": "[{extent} of the 1622 edition are wanting here.]"}.
GAP_NOTES = {}

# "&c." read as "etc." (reg/@type "abbreviation").
EXPAND_ETC = False

# The legacy sentence rule (Perkins, Simon Magus): an italic run never opens
# a sentence, even at the start of a paragraph or after a full stop.
# "after-stop" (Gouge): an italic boundary right after . ! ? cancels the new
# sentence, but a paragraph that opens in italics still starts one.
# False: italics are ignored when deciding where a sentence starts.
ITALIC_SENTENCE_QUIRK = True

# A decorated initial printed with its word in capitals ("AS there are"):
# set the word in ordinary case at the start of the paragraph.
DROP_CAP_CASE = False

# The early-modern machine pass (spelling engine, sentence case, common-noun
# lowercasing). A book from a modern source (CCEL) turns it off: its words
# stay as given, and only TYPOGRAPHY and the review change them.
MODERNIZE = True

# Straight quotes curled the way Typst curls them (after a letter, digit or
# closing punctuation a quote closes, otherwise it opens) and "--" set as an
# em dash, recorded as #auto punctuation readings. For sources keyed in
# ASCII (CCEL); a TCP transcription already has its printed marks.
TYPOGRAPHY = False
DASH = "\u2014"          # what "--" becomes; " \u2014 " for a spaced dash

# The edition's attribution, when it differs from the TCP header's (a work
# printed under another's name): (author as in titleStmt, note giving the
# grounds). The printed/catalogue attribution stays in sourceDesc.
AUTHOR = None

# What the source is ("tcp" or "thml"), for the header; set by main().
SOURCE_KIND = "tcp"


def load_tables(path):
    """Replace the tables above with those defined in a book's editorial.py."""
    import runpy
    ns = runpy.run_path(str(path))
    g = globals()
    for name in ("MACRON_M", "GAP_FIXES", "LOWERCASE_COMMON_NOUNS", "REPORT_NOTES",
                 "MODERNIZE_NOTES", "LATIN_RUNS", "DROP_FOREIGN_GAPS", "GAP_NOTES",
                 "EXPAND_ETC", "ITALIC_SENTENCE_QUIRK", "DROP_CAP_CASE",
                 "MODERNIZE", "TYPOGRAPHY", "DASH", "AUTHOR"):
        if name in ns:
            g[name] = ns[name]
    # the book's own spellings, over the shared table (e.g. Gouge keeps
    # "domestical" where the shared table has "domestic")
    import spelling
    for k, v in ns.get("SPELLING", {}).items():
        spelling.MANUAL[k] = v
        spelling.NAMES.pop(k, None)

NUMERAL_RE = re.compile(r"\d{1,2}|(?=[IVXLC]+$)[IVXLC]+", re.I)
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
    # a W printed as two Vs (VVorshipfull, Vvisdome) is a letter form too
    w = re.sub(r"^V[Vv](?=[a-z])", "W", re.sub(r"^VV(?=[A-Z])", "W", w))
    if any(not isinstance(p, (str, tuple)) and local(p) == "hi" for p in tok.pieces):
        return w                     # y^e -> the (already expanded)
    if not re.fullmatch(r"[A-Za-z']+", w):
        return w
    if not MODERNIZE:
        return w
    low = w.lower()
    if ROMAN_RE.match(w) and w.isupper():
        return w                     # list labels I. II. III.
    # decorated initial artifact: CHristian -> Christian
    if len(w) > 2 and w[0].isupper() and w[1].isupper() and w[2:].islower():
        w = w[0] + w[1:].lower()
    elif DROP_CAP_CASE and len(w) > 1 and w.isupper() and any(
            not isinstance(p, (str, tuple)) and local(p) == "seg" and
            p.get("rend") == "decorInit" for p in tok.pieces):
        w = w[0] + w[1:].lower()      # AS there are -> As there are
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
    if w[:1].isupper() and low in AMBIGUOUS_NAMES:
        return AMBIGUOUS_NAMES[low]  # "Mary" mid-sentence is the name, not "marry"
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
        letters, cert, note, *who = GAP_FIXES[idx]
        resp = who[0] if who else "#auto"
    s = etree.Element(T + "supplied")
    s.set("reason", gap.get("reason", "illegible"))
    s.set("cert", cert)
    s.set("resp", resp)
    s.text = letters
    # keep the original <gap> inside for full provenance
    g = copy.deepcopy(gap)
    g.tail = None
    # XML comments may not hold "--" or end in "-"
    s.append(etree.Comment(" " + re.sub(r"-{2,}", "\u2013", note).rstrip("-") + " "))
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
        r.set("resp", t.resp or "#editor")
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
BLOCK_MARK = {"p": "¶", "item": "-", "signed": "¶", "trailer": "¶", "sp": "¶"}
# Layout mode (a book with LAYOUT in editorial.py): division heads are text
# of the file, marked "H" (a heading line) or "¶" (a run-in heading, for the
# div types in RUN_IN_DIVS). None: heads are skipped, the classic behaviour.
HEAD_MODE = {"on": False, "run_in": set()}
SUBTITLES = set()       # layout subtitles: printed heads set as a centred line
# CLOSER_PLAIN: openers and closers are set as plain paragraphs (a salute,
# a signature), which the review may run on into the text or split
SETTINGS = {"closer_plain": False}


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
    latin = latin_tokens(toks) if LATIN_RUNS else set()

    def walk(ts, in_note, in_head):
        for t in ts:
            if t.kind == "container":
                n = local(t.el)
                if n in ("p", "item", "signed", "trailer") or n == "head":
                    state["start"], state["by"] = True, "block"
                # legacy quirk kept for continuity: an italic boundary right
                # after a full stop did not start a new sentence
                is_emph = n == "hi" and t.el.get("rend") != "sup" and ITALIC_SENTENCE_QUIRK

                def emph_boundary():
                    if ITALIC_SENTENCE_QUIRK != "after-stop" or state.get("by") == "punct":
                        state["start"] = False
                if is_emph:
                    emph_boundary()
                saved = state["start"]
                is_div_head = n == "head" and t.el.getparent() is not None \
                    and local(t.el.getparent()) == "div"
                # a table set as a list: its cells keep the printed capitals
                plain_cell = n == "cell" and table_mode(t.el) != "inline"
                walk(t.children, in_note or n == "note", in_head or is_div_head or plain_cell)
                if n == "note":
                    state["start"] = saved
                if is_emph:
                    emph_boundary()
            elif t.kind == "word":
                word_strings(t)
                t.resp, t.rtype = "#auto", "spelling"
                if id(t) in latin:
                    t.reg = t.expanded.replace("ſ", "s").replace("Ʋ", "U")
                    if not in_note:
                        state["start"] = False
                    continue
                if in_note:
                    t.reg = auto_reg(t, False, heading=True) if MODERNIZE_NOTES \
                        else t.expanded.replace("ſ", "s")
                    continue
                if in_head:
                    t.reg = auto_reg(t, False, heading=True)
                else:
                    t.sent_start = state["start"]
                    t.reg = auto_reg(t, state["start"])
                    if re.search(r"[A-Za-z]", t.expanded):
                        state["start"], state["by"] = False, None
                    state["num"] = bool(re.fullmatch(r"\d+", t.expanded))
            elif t.kind == "punct":
                p = t.pieces[0]
                t.orig = p if isinstance(p, str) else (p.text or "")
                t.reg = t.orig
                if not in_note and not in_head:
                    # "1." opening a paragraph is its numeral, not a sentence
                    numeral = state.get("num") and state["start"] and \
                        state.get("by") == "block" and t.orig == "."
                    state["start"] = t.orig in ".!?"
                    if not numeral:
                        state["by"] = "punct" if state["start"] else None
                    state["num"] = False
    walk(toks, False, False)
    if DROP_FOREIGN_GAPS or GAP_NOTES:
        gap_readings(toks)
    if EXPAND_ETC:
        expand_etc(toks)
    table_readings(toks)
    page_break_spaces(toks)
    if TYPOGRAPHY:
        typography(toks)


def page_break_spaces(toks):
    """A page break keyed between two words with no space (A47561:
    "leaſt<pb n="14"/>to"): the word space the printed page break stands for,
    as an #auto spacing reading."""
    def walk(ts):
        for t in ts:
            if t.kind == "container":
                walk(t.children)
        for i in range(len(ts) - 2, 0, -1):
            a, pb, b = ts[i - 1], ts[i], ts[i + 1]
            if pb.kind == "atom" and pb.el is not None and local(pb.el) == "pb" \
                    and a.kind in ("word", "punct") and b.kind in ("word", "container") \
                    and not (b.kind == "container" and local(b.el) == "note"):
                s = Tok("spacing", [""])
                s.reg, s.resp, s.parent = " ", "#auto", pb.parent
                ts.insert(i + 1, s)
        for k, c in enumerate(ts):
            c.idx = k
    walk(toks)


TYPO_BLOCKS = {"p", "head", "item", "l", "note", "cell", "titlePart", "byline",
               "docAuthor", "signed", "trailer", "label"}
TYPO_CLOSERS = set(".,;:!?)]")


def typography(toks):
    """TYPOGRAPHY: curl straight quotes, set "--" as an em dash."""
    leaves = []

    def walk(ts):
        for t in ts:
            if t.kind == "container":
                if local(t.el) in TYPO_BLOCKS:
                    leaves.append(None)            # a block starts: nothing before
                walk(t.children)
            elif t.kind in ("word", "punct", "space", "noise"):
                leaves.append(t)
    walk(toks)
    prev = " "

    def curl(c, prev):
        closing = prev.isalnum() or prev in TYPO_CLOSERS
        if c == "'":
            return "\u2019" if closing else "\u2018"
        return "\u201d" if closing else "\u201c"

    for i, t in enumerate(leaves):
        if t is None:
            prev = " "
            continue
        if t.kind in ("space", "noise"):
            prev = " "
            continue
        cur = t.reg if t.reg is not None else t.orig
        if cur is None:
            continue
        if t.kind == "punct" and cur == "-":
            # "--", or "-" at a line end and "-" opening the next line (a
            # dash the keying split at the line break)
            j = i + 1
            if j < len(leaves) and leaves[j] is not None and \
                    leaves[j].kind in ("space", "noise") and "\n" in (leaves[j].pieces[0] or ""):
                j += 1
            nxt = leaves[j] if j < len(leaves) else None
            if nxt is not None and nxt.kind == "punct" and \
                    (nxt.reg if nxt.reg is not None else nxt.orig) == "-":
                t.reg, t.resp, t.rtype = DASH, "#auto", "punctuation"
                nxt.reg, nxt.resp, nxt.rtype = "", "#auto", "punctuation"
                prev = DASH[-1]
                continue
        if "'" in cur or '"' in cur:
            out = []
            for c in cur:
                if c in "'\"":
                    c = curl(c, prev)
                out.append(c)
                prev = c
            new = "".join(out)
            if new != cur:
                t.reg, t.resp = new, "#auto"
                if t.kind == "punct" or new.replace("\u2019", "'").replace("\u2018", "'") == \
                        (t.expanded if t.kind == "word" else cur):
                    t.rtype = "punctuation"
            continue
        if cur:
            prev = cur[-1]


def table_mode(cell_el):
    t = next((a for a in cell_el.iterancestors() if local(a) == "table"), None)
    return layout.table_reading(t)[0] if t is not None else None


def cell_leaves(ct):
    """Word and punctuation tokens of a cell, notes left out."""
    out = []

    def walk(ts):
        for t in ts:
            if t.kind == "container":
                if local(t.el) != "note":
                    walk(t.children)
            elif t.kind in ("word", "punct"):
                out.append(t)
    walk(ct.children)
    return out


def table_readings(toks):
    """A table set as a list (layout.table_reading) gets the tidying a list
    needs, as machine readings: a brace's items lose their printed number and
    trailing comma, open with a capital and, in the last column, end with a
    full stop; a label loses its trailing comma; a row-wise table's number
    cells are left out; a table read inline into its sentence has its cells
    joined with commas."""
    def cells_of(t):
        out = {}

        def walk(ts):
            for c in ts:
                if c.kind == "container":
                    if local(c.el) == "cell":
                        out[c.el] = c
                    else:
                        walk(c.children)
        walk(t.children)
        return out

    def omit(x, typ="omission"):
        x.reg, x.rtype, x.resp = "", typ, "#auto"

    def reading(x):
        return x.reg if x.reg is not None else (x.orig or "")

    def strip_comma(ls):
        if ls and ls[-1].kind == "punct" and ls[-1].orig == ",":
            omit(ls[-1], "punctuation")
            return True
        return False

    def visit(ts):
        for t in ts:
            if t.kind != "container":
                continue
            if local(t.el) != "table":
                visit(t.children)
                continue
            mode, blocks = layout.table_reading(t.el)
            cells = cells_of(t)
            if mode == "inline":
                cs = [cells[c] for _m, cl in blocks for c in cl if c in cells]
                for k, ct in enumerate(cs):
                    ls = [x for x in cell_leaves(ct) if reading(x)]
                    if not ls:
                        continue
                    if k == len(cs) - 1:
                        strip_comma(ls)
                    elif not (ls[-1].kind == "punct" and ls[-1].orig == ","):
                        last = ls[-1]
                        last.reg = reading(last) + ","
                        last.rtype, last.resp = "punctuation", "#auto"
                continue
            last_col = max((i for i, (m, _c) in enumerate(blocks) if m == "¶"), default=-1)
            for i, (marker, cl) in enumerate(blocks):
                cts = [cells[c] for c in cl if c in cells]
                if mode == "rows":
                    if marker == "+" and len(cts) > 1 and \
                            re.fullmatch(layout.NUMBER_CELL, " ".join(
                                "".join(cts[0].el.itertext()).split())):
                        for x in cell_leaves(cts[0]):
                            omit(x)
                    continue
                for ct in cts:
                    ls = cell_leaves(ct)
                    if marker == "¶":
                        strip_comma(ls)
                        continue
                    # an item: printed number, trailing comma, capital, stop
                    if len(ls) >= 2 and ls[0].kind == "word" and \
                            re.fullmatch(r"\d{1,2}", reading(ls[0])) and \
                            ls[1].kind == "punct" and ls[1].orig in ".)":
                        omit(ls[0])
                        omit(ls[1])
                    live = [x for x in ls if reading(x)]
                    stripped = strip_comma(live)
                    live = [x for x in live if reading(x)]
                    first = next((x for x in live if x.kind == "word"), None)
                    if first is not None and reading(first)[:1].islower():
                        first.reg = reading(first)[:1].upper() + reading(first)[1:]
                        first.rtype, first.resp = "case", "#auto"
                    final = i > last_col
                    if final and live and not re.search(
                            r"[.!?:;][\s)\]]*$", "".join(reading(x) for x in live)):
                        last = live[-1]
                        last.reg = reading(last) + "."
                        last.rtype, last.resp = "punctuation", "#auto"
    visit(toks)


def expand_etc(toks):
    """&c. -> etc.: the ampersand reads "etc", the c nothing."""
    def walk(ts):
        kids = [c for c in ts if c.kind != "noise"]
        for a, b in zip(kids, kids[1:]):
            if a.kind == "punct" and a.orig == "&" and b.kind == "word" and \
                    (b.expanded or "").lower() == "c":
                a.reg, a.rtype, a.resp = ("Etc" if b.expanded == "C" else "etc"), \
                    "abbreviation", "#auto"
                b.reg, b.rtype = "", "abbreviation"
                after = kids[kids.index(b) + 1] if kids.index(b) + 1 < len(kids) else None
                if not (after is not None and after.kind == "punct" and after.orig == "."):
                    a.reg += "."                  # "&c" printed without its stop
        for c in ts:
            if c.kind == "container":
                walk(c.children)
    walk(toks)


def gap_only(t):
    """The <gap> elements of a word token made of nothing but gaps."""
    els = [p for p in t.pieces if not isinstance(p, (str, tuple))]
    if not els or any(local(p) != "gap" for p in els):
        return []
    if any(isinstance(p, str) and p.strip() for p in t.pieces):
        return []
    return els


def gap_readings(toks):
    """DROP_FOREIGN_GAPS and GAP_NOTES: readings for words that are only a gap."""
    def walk(ts, in_note):
        kids = [c for c in ts if c.kind != "noise"]
        for i, t in enumerate(kids):
            if t.kind == "container":
                walk(t.children, in_note or local(t.el) == "note")
                continue
            if t.kind != "word":
                continue
            gaps = gap_only(t)
            if not gaps:
                continue
            reason = gaps[0].get("reason")
            if all(i in GAP_FIXES for i, _g in t.gaps):
                continue                        # filled in: <supplied>
            if reason in GAP_NOTES:
                t.reg = GAP_NOTES[reason].format(
                    extent=(gaps[0].get("extent") or "").capitalize())
                t.rtype = "editorial"
            elif reason == "foreign" and DROP_FOREIGN_GAPS:
                t.reg, t.rtype = "", "omission"
                prev = kids[i - 1] if i else None
                nxt = kids[i + 1] if i + 1 < len(kids) else None
                # punctuation left stranded after it: at the start of a note
                # or block it goes; mid-sentence the space before the gap goes
                first = all(k.kind in ("space", "atom") or
                            (k.kind == "word" and k.reg == "") for k in kids[:i])
                if nxt is not None and nxt.kind == "punct" and nxt.orig in ".,;:":
                    if first:
                        nxt.reg, nxt.rtype, nxt.resp = "", "omission", "#auto"
                        after = kids[i + 2] if i + 2 < len(kids) else None
                        if after is not None and after.kind == "space":
                            after.kind, after.reg, after.resp = "spacing", "", "#auto"
                    elif prev is not None and prev.kind == "space":
                        prev.kind, prev.reg, prev.resp = "spacing", "", "#auto"
                elif nxt is not None and nxt.kind == "space" and \
                        (first or (prev is not None and prev.kind == "space")):
                    nxt.kind, nxt.reg, nxt.resp = "spacing", "", "#auto"
    walk(toks, False)


def latin_tokens(toks):
    """ids of the word tokens in Latin runs (see LATIN_RUNS): a run is the
    words of one container between two child containers (italics, notes)."""
    from spelling import _SPELL

    def english(w):
        low = w.lower()
        return low in _SPELL or modernize_word_lower(low) in _SPELL

    out = set()

    def judge(run):
        words = [t for t in run if re.search(r"[A-Za-z]", t.expanded or "")]
        if len(words) < LATIN_MIN_WORDS:
            return
        texts = [t.expanded.replace("ſ", "s") for t in words]
        eng = sum(english(re.sub(r"[^A-Za-z']", "", w)) for w in texts)
        if eng * 2 < len(words):
            out.update(id(t) for t in words)

    def walk(ts):
        run = []
        for t in ts:
            if t.kind == "container":
                judge(run)
                run = []
                walk(t.children)
            elif t.kind == "word":
                word_strings(t)
                run.append(t)
        judge(run)
    walk(toks)
    return out


def stream(toks, skip_heads=True):
    """Flatten tokens to [(text, kind, tok, container_path)]; kind 'w' or 'm'."""
    out = []

    def has_words(t):
        if t.kind in ("word", "punct"):
            return bool(t.reg if t.reg is not None else t.orig)
        return t.kind == "container" and local(t.el) != "note" and \
            any(has_words(c) for c in t.children or [])

    def walk(ts, path, pending=False):
        # a paragraph split around a block list or table goes on as a new
        # paragraph after it (layout.p_blocks)
        par = path[-1].el if path and path[-1].el is not None else None
        split = layout.p_blocks(par) if par is not None and local(par) == "p" else []
        for t in ts:
            if t.kind == "container" and t.el in split:
                pending = True          # a new paragraph after the block ...
            elif pending and has_words(t):
                out.append(("¶", "m", t, path))   # ... if text follows it
                pending = False
            if t.kind == "container" and local(t.el) == "table":
                table(t, path)
                continue
            if t.kind == "container":
                n = local(t.el)
                if n == "head" and t.el in SUBTITLES:
                    out.append(("¶", "m", t, path))      # a block of its own
                    walk(t.children, path + (t,))
                    continue
                if skip_heads and n == "head" and local(t.el.getparent()) == "div":
                    if not HEAD_MODE["on"]:
                        continue
                    run_in = t.el.getparent().get("type") in HEAD_MODE["run_in"]
                    out.append(("¶" if run_in else "H", "m", t, path))
                    walk(t.children, path + (t,))
                    continue
                if n == "closer" and layout.closer_lines(t.el) is not None:
                    # signatories one to a line, then place and date
                    toks_of = {}

                    def index(ts_):
                        for c in ts_:
                            if c.kind == "container":
                                toks_of[c.el] = c
                                index(c.children)
                    index(t.children)
                    for el in layout.closer_lines(t.el):
                        out.append(("¶", "m", toks_of[el], path))
                        walk(toks_of[el].children, path + (t, toks_of[el]))
                    continue
                if HEAD_MODE["on"] and n == "epigraph":
                    out.append(("¶", "m", t, path))
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
                in_epigraph = HEAD_MODE["on"] and any(
                    local(a.el) == "epigraph" for a in path if a.el is not None)
                if n == "p" and layout.p_blocks(t.el):
                    # opened only if text comes before its first block
                    walk(t.children, path + (t,), pending=True)
                    continue
                # a quotation block of the source (CCEL blockquote, verse) is
                # the review's #quote[...]; its paragraphs open no block
                if n == "quote":
                    # (a stanza of a section made of verse is a plain block)
                    out.append(("¶" if layout.verse_division(t.el) else ">", "m", t, path))
                    walk(t.children, path + (t,))
                    continue
                in_quote = n == "p" and t.el.getparent() is not None and \
                    local(t.el.getparent()) == "quote"
                # a speech opens a block with its speaker ("Christian: ..."),
                # which its first paragraph continues
                speech = n == "p" and t.el.getparent() is not None and \
                    local(t.el.getparent()) == "sp" and \
                    t.el.getprevious() is not None and local(t.el.getprevious()) == "speaker"
                if (n in BLOCK_MARK or block_q) and not list_only and not in_epigraph \
                        and not in_quote and not speech:
                    out.append((BLOCK_MARK.get(n, "¶"), "m", t, path))
                walk(t.children, path + (t,))
            elif t.kind in ("word", "punct"):
                txt = t.reg if t.reg is not None else t.orig
                for s in SPLIT_RE.findall(txt or ""):
                    out.append((s, "w", t, path))

    def table(t, path):
        """A table in the edition's reading order (layout.table_reading)."""
        cells = {}

        def find(ts):
            for c in ts:
                if c.kind == "container":
                    if local(c.el) == "cell":
                        cells[c.el] = c
                    else:
                        find(c.children)
        find(t.children)
        _mode, blocks = layout.table_reading(t.el)
        for marker, cl in blocks:
            if marker:
                out.append((marker, "m", t, path))
            for c in cl:
                if c in cells:
                    walk(cells[c].children, path + (t, cells[c]))
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


def run_cut_ops(mw, ow, run_lens):
    """Opcodes matching the words of several runs (mw, run after run) with
    one run (ow). When the same word could match in two runs ("in" in a
    deleted epigraph and "IN" opening the paragraph after it), take the
    reading that matches more words at the start of a run; on a tie, the
    first (difflib's own)."""
    starts, k = set(), 0
    for n in run_lens:
        starts.add(k)
        k += n

    def ops_for(a, b):
        return difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()

    def score(ops):
        eq = sum(i2 - i1 for op, i1, i2, _j1, _j2 in ops if op == "equal")
        st = sum(1 for op, i1, _i2, j1, _j2 in ops if op == "equal" and i1 in starts and j1 == 0)
        return eq, st
    fwd = ops_for(mw, ow)
    rev = ops_for(mw[::-1], ow[::-1])
    n, m = len(mw), len(ow)
    rev = [(op, n - i2, n - i1, m - j2, m - j1) for op, i1, i2, j1, j2 in reversed(rev)]
    return rev if score(rev) > score(fwd) else fwd


def split_marks(ops, src, tgt):
    """A changed stretch with block marks on both sides, more on one side
    (a paragraph the review deletes, then a printed "2." it makes an item):
    the surplus marks and what comes before them are a stretch of their
    own, so the rest pairs mark with mark."""
    out = []
    for op, i1, i2, j1, j2 in ops:
        sm_ = [k for k in range(i1, i2) if src[k][1] == "m"]
        rm_ = [k for k in range(j1, j2) if tgt[k][1] == "m"]
        if op == "equal" or not sm_ or not rm_ or len(sm_) == len(rm_):
            out.append((op, i1, i2, j1, j2))
            continue
        if len(sm_) > len(rm_):
            si, ri = sm_[len(sm_) - len(rm_)], rm_[0]
        else:
            si, ri = sm_[0], rm_[len(rm_) - len(sm_)]
        out += [("replace", i1, si, j1, ri), ("replace", si, i2, ri, j2)]
    return out


def numeral_stops(ops, src, tgt):
    """A stop the review adds before a printed numeral it makes a "+" item
    ("husband VIII. The" -> "husband.\n+ The"): difflib pairs the review's
    stop with the numeral's and deletes the numeral. Pair the numeral and
    its stop with the item mark instead (the label), and the review's stop
    is an insertion after the word before."""
    out, k = [], 0
    while k < len(ops):
        if k + 2 < len(ops):
            (o1, a1, a2, b1, b2), (o2, c1, c2, d1, d2), (o3, e1, e2, f1, f2) = ops[k:k + 3]
            if o1 == "delete" and a2 - a1 == 1 and src[a1][1] == "w" and \
                    NUMERAL_RE.fullmatch(src[a1][0]) and \
                    o2 == "equal" and c2 - c1 == 1 and src[c1][0] in ".)" and \
                    o3 == "insert" and tgt[f1][1] == "m" and tgt[f1][0] == "+":
                out += [("insert", a1, a1, d1, d2), ("replace", a1, c2, f1, f2)]
                k += 3
                continue
        out.append(ops[k])
        k += 1
    return out


def punct_after_deletion(ops, src):
    """A deletion that starts with the same mark as the text after it
    ("well . [deleted margin matter] . ¶ Under"): difflib keeps the later
    stop; keep the one after the word before instead, so the stop stays in
    its sentence and the deleted run takes the other."""
    out = list(ops)
    for k in range(1, len(out) - 1):
        p_op, d_op, n_op = out[k - 1], out[k], out[k + 1]
        if p_op[0] != "equal" or d_op[0] != "delete" or n_op[0] != "equal":
            continue
        a1, a2 = d_op[1], d_op[2]
        c1, c2, e1, e2 = n_op[1], n_op[2], n_op[3], n_op[4]
        if src[a1][1] != "w" or re.match(r"\w", src[a1][0]) or src[a1][0] != src[c1][0]:
            continue
        out[k - 1] = ("equal", p_op[1], p_op[2] + 1, p_op[3], p_op[4] + 1)
        out[k] = ("delete", a1 + 1, c1 + 1, e1 + 1, e1 + 1)
        out[k + 1] = ("equal", c1 + 1, c2, e1 + 1, e2) if c2 > c1 + 1 else None
    return [o for o in out if o is not None]


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

    for op, i1, i2, j1, j2 in split_marks(punct_after_deletion(numeral_stops(sm.get_opcodes(), src, tgt), src), src, tgt):
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
                wops = run_cut_ops(mw, ow, [len(run) for run in many])

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
                    # a printed numeral ("1." "II.") the review dropped when
                    # it made the block a "+" item is the item's label, not
                    # a deleted word
                    if n and n - 1 < len(Rm) and Rm[n - 1] == "+" and len(sr) >= 2 and \
                            NUMERAL_RE.fullmatch(sr[0][0][0]) and sr[1][0][0] in ".)" and \
                            not (rr and rr[0][0][0] == sr[0][0][0]):
                        for e, _ in sr[:2]:
                            add_tgt(e[2], [e[0]], [])
                        sr = sr[2:]
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
            # pure insertion: attach to the previous source word token, or,
            # right after a block opens on both sides ("¶ Obs. 2. Again"),
            # to the block's first word, so it opens that block
            prev = next((s for s in reversed(src[:i1]) if s[1] == "w"), None)
            if i1 and src[i1 - 1][1] == "m" and j1 and tgt[j1 - 1][1] == "m":
                prev = next((s for s in src[i2:] if s[1] == "w"), None) or prev
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


# Grammatical archaisms: modernizing them (thou -> you, hath -> has) is a
# change of word, not of spelling, but common enough to get its own type so
# that real rewordings stay easy to find.
ARCHAIC = {"thou", "thee", "thy", "thine", "ye", "hath", "doth", "hast", "dost",
           "art", "shalt", "wilt", "saith", "unto", "wast", "wert"}
ARCHAIC_ENDING = re.compile(r"(eth|est|'st)$")
# Pairs rather than words: "be" -> "bee" is a spelling fix (Bee-hive).
ARCHAIC_PAIRS = {("be", "is"), ("be", "are"), ("be", "am"), ("an", "a")}


def classify(old, new):
    """reg/@type of a single-token editor change: case, spelling (the same
    word spelled differently), grammar (an archaic form modernized) or
    emendation (another word, a word removed or added, a changed number)."""
    if old.lower() == new.lower():
        return "case"
    if " " in new or " " in old or not old.strip() or not new.strip():
        return "emendation"
    a, b = old.lower(), new.lower()
    if re.sub(r"\D", "", a) != re.sub(r"\D", "", b):
        return "emendation"                    # citation numbers
    if a in ARCHAIC or (a, b) in ARCHAIC_PAIRS or (ARCHAIC_ENDING.search(a) and
                        difflib.SequenceMatcher(None, a, b).ratio() >= 0.5):
        return "grammar"
    if difflib.SequenceMatcher(None, a, b).ratio() < 0.6:
        return "emendation"
    return "spelling"


def ancestors(tok):
    """Container tokens above tok (the element-less root is left out)."""
    a = []
    p = tok.parent
    while p is not None:
        if p.el is not None:
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


def space_between(a, b, limit=60):
    """Whether a space token stands between word tokens a and b (b after a in
    document order), looking at most `limit` tokens ahead."""
    t = a
    for _ in range(limit):
        while t.parent is not None and t.idx is not None and \
                t.idx == len(t.parent.children) - 1:
            t = t.parent
        if t.parent is None or t.idx is None:
            return False
        t = t.parent.children[t.idx + 1]
        while t.kind in ("container", "group") and t.children:
            if contains(t, b) and t.kind == "group":
                return False
            t = t.children[0]
        if t is b:
            return False
        if t.kind == "space":
            return True
    return False


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
    # a cut just after a word's leading punctuation ("'I", "(of") moves to
    # before it: the mark opens the next token's word, and the space printed
    # between the two tokens stays in front of it
    for k in range(len(bounds) - 1):
        b = bounds[k]
        w = ns_to_full[b] if b < len(ns_to_full) else len(tgt)
        a = w
        while a > 0 and tgt[a - 1] != " " and not tgt[a - 1].isalnum():
            a -= 1
        if a < w and (a == 0 or tgt[a - 1] == " ") and w < len(tgt) and tgt[w].isalnum():
            bounds[k] = max(ns_to_full.index(a), bounds[k - 1] if k else 0)
    # a cut inside a word, between tokens printed with a space between them,
    # moves to the nearer end of that word (else the space splits the word:
    # "Revela t ion")
    for k in range(len(bounds) - 1):
        w = ns_to_full[bounds[k]] if bounds[k] < len(ns_to_full) else len(tgt)
        if not (0 < w < len(tgt) and tgt[w - 1] != " " and tgt[w] != " ") or \
                not space_between(ts[k], ts[k + 1]):
            continue
        a, z = w, w
        while a > 0 and tgt[a - 1] != " ":
            a -= 1
        while z < len(tgt) and tgt[z] != " ":
            z += 1
        to = a if w - a <= z - w else z
        b = len(tgt[:to].replace(" ", ""))       # as an offset without spaces
        bounds[k] = max(b, bounds[k - 1] if k else 0)
    for k in range(1, len(bounds)):
        bounds[k] = max(bounds[k], bounds[k - 1])
    start = 0
    pieces = []
    for b in bounds:
        b = max(b, start)
        pieces.append(tgt[ns_to_full[start]:ns_to_full[b]].strip() if start < len(ns_to_full) else "")
        start = b
    for k, (t, piece) in enumerate(zip(ts, pieces)):
        if piece != (t.reg if t.reg is not None else t.orig or ""):
            apply_to_token(t, piece, log, label)
        # a piece that begins inside a review word: no space goes before it
        w = ns_to_full[bounds[k - 1]] if k and bounds[k - 1] < len(ns_to_full) else None
        if w is not None and 0 < w < len(tgt) and tgt[w - 1] != " " and tgt[w] != " ":
            t.extra["midword"] = True
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


def between_blocks(x):
    """Whitespace between two blocks (in a division, list ...), not inside
    one: a run-on join there is the block's @rend, not a spacing choice."""
    par = x.parent
    return isinstance(par, View) or par is None or par.el is None or \
        local(par.el) in ("div", "list", "body", "front", "back", "text", "group",
                          "lg", "sp", "closer", "opener", "epigraph")


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
        # indentation between two words' elements renders as a space too
        spaces = [x for x in between if x.kind == "space" or
                  (x.kind == "noise" and "".join(p for p in x.pieces if isinstance(p, str)).strip() == "")
                  or (x.kind == "spacing" and x.reg == " ")]     # the machine's (page_break_spaces)
        want = sp[j2]
        if not want:
            # whitespace between two blocks is not removed here: a block run
            # on without a space says so itself (@rend="run-on")
            if spaces and all(between_blocks(x) for x in spaces):
                continue
            spaces = [x for x in spaces if not between_blocks(x)]
        # a reading may carry its own space (a spaced dash, DASH = " — ")
        padded = (a.kind in ("word", "punct") and (a.reg or "").endswith(" ")) or \
            (b.kind in ("word", "punct") and (b.reg or "").startswith(" "))
        if want == (bool(spaces) or padded):
            continue
        if want and b.extra.get("midword"):
            continue            # b's reading starts inside a word; its space is in it
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
                x.reg, x.resp = "", "#editor"
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
    body, notes, rec = [], [], {}
    for e in entries:
        # the innermost note: a note printed inside a note is a note of its own
        note = next((c for c in reversed(e[3]) if local(c.el) == "note"), None)
        if note is None:
            body.append(e)
            continue
        if id(note) not in rec:
            rec[id(note)] = (note, [], len(body))
            notes.append(rec[id(note)])
        if e[1] == "w":
            rec[id(note)][1].append(e)
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
    for tr in (division_trailers(d.el) if d.el is not None else []):
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


class View:
    """A run of TEI parts (divisions and loose blocks) aligned as one unit
    with one reviewed file: the layout-mode stand-in for a division."""
    kind = "container"

    def __init__(self, children, el):
        self.children = children
        self.el = el
        self.extra = {}
        self.parent = None


def review_division(d, review, f, log, unresolved):
    """Align one division with its review: body and notes separately."""
    entries = stream(d.children)
    body, notes = split_notes(entries)
    tgt = [(t, k) for t, k, _ in review.body]
    owner = {}
    cl, st = align(body, tgt, [], f, owner)
    for j0 in getattr(review, "epigraphs", ()):
        # a printed paragraph the review sets as a scripture epigraph
        jw = next((j for j in range(j0 + 1, len(tgt)) if j in owner), None)
        if jw is None:
            continue
        anc = ancestors(owner[jw])
        p = next((a for a in anc if local(a.el) in ("p", "epigraph")), None)
        if p is not None and local(p.el) == "p" and p.el.get("rend") != "epigraph" and \
                not any(local(a.el) == "epigraph" for a in anc):
            p.el.set("rend", "epigraph")
            p.el.set("change", "#review")
            log.append((f, "epigraph", owner[jw].orig, "set as a scripture epigraph"))
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
            words = [t for t, _ in nt["toks"]]
            sps = nt.get("sp")
            el.text = join_sp(words, sps if sps and len(sps) == len(words) else None)
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
    # the edition's own headings, placed before the block they stand over
    for pos, level, text in getattr(review, "edition_heads", []):
        jw = next((x for x in range(pos, len(tgt)) if tgt[x][1] == "w"), None)
        tok = owner.get(jw) if jw is not None else None
        if tok is None:
            unresolved.append((f, "edition heading", text))
        else:
            EDITION_HEADS.append((tok, level, text, f))
    # list items and the blocks set inside them (reviewparse list_info),
    # placed after restructure() has made the review's lists
    for j, info in sorted(getattr(review, "list_info", {}).items()):
        jw = next((x for x in range(j + 1, len(tgt)) if tgt[x][1] == "w"), None)
        tok = owner.get(jw) if jw is not None else None
        if tok is not None:
            LIST_SHAPE.append((tok, info, f))
        elif info["depth"] or info.get("numbering") or info.get("start"):
            unresolved.append((f, "list shape", tgt[jw][0] if jw is not None else "(end)"))
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
    # a block the review runs on without a space ("Psalm 37:" + "6. And ...")
    first_j = {}
    for j, tok in sorted(owner.items()):
        first_j.setdefault(id(tok), j)
    where = {id(e[2]): k for k, e in reversed(list(enumerate(body)))}
    for x in st:
        if x["at"] is not None and x["src_marks"] and not x["tgt_marks"]:
            # the first word of the joined block that the review keeps
            j = None
            for e in body[where.get(id(x["at"][2]), len(body)):]:
                if e[1] == "m":
                    break
                j = first_j.get(id(e[2]))
                if j is not None:
                    break
            if j is not None and not review.body_sp[j]:
                NO_SPACE_RUN_ON.add(id(x["at"][2]))
    return st, body


NO_SPACE_RUN_ON = set()     # id(tok): a merge at tok joins without a space


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

    def plain_leaves(t):
        for c in t.children or []:
            if c.kind == "container":
                if local(c.el) == "note":
                    continue
                if is_emph(c) and c.el.get("ana") != "#print-only":
                    continue
                yield from plain_leaves(c)
            elif c.kind in ("word", "punct", "group"):
                yield c

    # 2. italics the edition adds
    def walk_add(t, italic):
        kids = t.children or []
        need = []
        for c in kids:
            if c.kind == "container":
                if local(c.el) == "note":
                    need.append("break")
                    continue
                # words already under a printed italic inside c need nothing
                inner = [want(x) for x in plain_leaves(c)]
                if not inner and any(True for _ in leaves(c)):
                    need.append("neutral")
                    continue
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
            if k != "{%s}id" % XML_NS:      # the split-off part is a new element
                el.set(k, v)
    t = Tok("container", el=el)
    t.children = []
    return t


def relink(ct):
    if isinstance(ct, View):
        return          # a layout file's parts keep their own divisions as parents
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
    """The block a token stands in: a child of its division, or a paragraph
    of a speech (sp)."""
    a = tok.parent
    while a is not None and not (a.el.getparent() is not None and
                                 (local(a.el.getparent()) == "div" or
                                  (local(a.el.getparent()) == "sp" and
                                   local(a.el) != "speaker"))):
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


MADE_LISTS = []


def merge_lists(log):
    """Lists the review made from neighbouring paragraphs ("1. ..." and
    "2. ..." each a <p>) are one list: join a new list to the one before it
    when nothing but space lies between."""
    for lst in MADE_LISTS:
        par = lst.parent
        if par is None or lst not in par.children:
            continue
        k = par.children.index(lst)
        j = k - 1
        while j >= 0 and par.children[j].kind in ("space", "noise"):
            j -= 1
        prev = par.children[j] if j >= 0 else None
        if prev is not None and prev.kind == "container" and local(prev.el) == "list" \
                and prev.el.get("change") == "#review" and prev in MADE_LISTS \
                and prev.el.get("type") == lst.el.get("type"):
            prev.children += [Tok("space", ["\n"])] + [c for c in lst.children]
            relink(prev)
            del par.children[j + 1:k + 1]
            relink(par)


LIST_SHAPE = []         # (tok, list_info entry, file), in reading order
EDITION_HEADS = []      # (tok, level, text, file): headings the edition adds


def apply_edition_heads(log):
    """Each heading the edition adds becomes label[@type="head"] (its level
    in @n, ana="#edition-only") before the block whose first word it stands
    over; printed text is not touched."""
    for tok, level, text, f in EDITION_HEADS:
        path = path_to(ROOT["toks"], tok) or []
        conts = [c for c in path if c.kind == "container"]
        k = next((i for i in range(len(conts) - 1, 0, -1)
                  if local(conts[i - 1].el) in ("div", "item")), None)
        if k is None:
            log.append((f, "skipped", f"heading '{text}'", "no block for it"))
            continue
        blk, par = conts[k], conts[k - 1]
        if local(blk.el) == "list":     # over an item: before that item
            item = next((c for c in conts[k + 1:] if local(c.el) == "item"), None)
            items = [c for c in blk.children if c.kind == "container" and local(c.el) == "item"]
            if item is not None and items and item is not items[0]:
                blk, par = item, blk
        el = etree.Element(T + "label")
        el.set("type", "head")
        el.set("n", str(level))
        el.set("ana", "#edition-only")
        el.set("change", "#review")
        el.text = text
        i = next(j for j, c in enumerate(par.children) if c is blk)
        par.children[i:i] = [Tok("atom", el=el), Tok("space", ["\n"])]
        relink(par)
        log.append((f, "heading", "(none)", text))
ROOT = {"toks": []}


def path_to(ts, tok, trail=()):
    """The containers (and groups) from the top down to tok, or None."""
    for c in ts:
        if c is tok:
            return list(trail)
        if c.kind in ("container", "group") and c.children:
            r = path_to(c.children, tok, trail + (c,))
            if r is not None:
                return r
    return None


def detach(blk, parent):
    k = next(i for i, c in enumerate(parent.children) if c is blk)
    j = k - 1 if k and parent.children[k - 1].kind in ("space", "noise") else k
    del parent.children[j:k + 1]
    relink(parent)


def append_block(parent, blk):
    parent.children += [Tok("space", ["\n"]), blk]
    relink(parent)


def nested_under(item, path):
    """Whether the containers in path put a block inside item: in it, or in
    an item that only wraps a nested list and follows it (the TCP's way of
    nesting a list under an item, which the Typst lists render as inside)."""
    if item in path:
        return True
    lst = item.parent
    if lst is None:
        return False
    sibs = [c for c in lst.children if c.kind == "container"]
    k = next((i for i, c in enumerate(sibs) if c is item), None)
    while k is not None and k + 1 < len(sibs):
        nxt = sibs[k + 1]
        inner = [c for c in nxt.children if c.kind == "container" or has_words(c)]
        if local(nxt.el) != "item" or not inner or \
                any(c.kind != "container" or local(c.el) != "list" for c in inner):
            return False
        if nxt in path:
            return True
        k += 1
    return False


def apply_list_shape(log):
    """The review's list layout: an item it indents under another goes into
    a list inside that item, a paragraph it indents under an item goes
    into the item, and a list it numbers in its own way (#[ #set enum(
    numbering: "a)", start: 2) ... ]) gets list/@rend (the numbering) and
    item/@n on its first item (the start). Printed text is not moved
    across other text: only the nesting changes."""
    last, cur = {}, None             # depth -> the latest item at that depth
    for tok, info, f in LIST_SHAPE:
        if f != cur:
            last, cur = {}, f
        path = path_to(ROOT["toks"], tok)
        conts = [c for c in path or [] if c.kind == "container"]
        d = info["depth"]
        if info["kind"] in ("+", "-"):
            k = next((i for i in range(len(conts) - 1, 0, -1)
                      if local(conts[i].el) == "item"), None)
            cell = next((c for c in reversed(conts) if local(c.el) == "cell"), None)
            if k is None and cell is not None and d == 1 and info["kind"] == "+" and \
                    not info.get("numbering") and not info.get("start"):
                # a branch of a brace the review sets under the branch before
                if cell.el.get("rend") != "nested":
                    cell.el.set("rend", "nested")
                    cell.el.set("change", "#review")
                    log.append((f, "list", f"table cell at '{tok.orig}'",
                                "nested under the branch before"))
                continue
            if k is None:
                if d or info.get("numbering") or info.get("start"):
                    log.append((f, "skipped", f"list item at '{tok.orig}'", "not an item"))
                continue
            item, lst = conts[k], conts[k - 1]
            parent = last.get(d - 1) if d else None
            if parent is not None and not nested_under(parent, path):
                blocks = [c for c in parent.children if c.kind == "container"]
                sub = blocks[-1] if blocks and local(blocks[-1].el) == "list" else None
                if sub is None:
                    sub = new_container("list", like=lst.el)
                    sub.el.attrib.pop("rend", None)
                    sub.el.set("change", "#review")
                    append_block(parent, sub)
                detach(item, lst)
                if not any(c.kind == "container" and local(c.el) == "item"
                           for c in lst.children):
                    detach(lst, conts[k - 2])
                sub.children += ([Tok("space", ["\n"])] if sub.children else []) + [item]
                relink(sub)
                lst = sub
                log.append((f, "list", f"item at '{tok.orig}'", "set inside the item before"))
            num = info.get("numbering")
            if num and lst.el.get("rend") != num:
                lst.el.set("rend", num)
                lst.el.set("change", "#review")
                log.append((f, "list", f"numbering at '{tok.orig}'", num))
            if info.get("start"):
                first = next(c for c in lst.children
                             if c.kind == "container" and local(c.el) == "item")
                if first is item:
                    item.el.set("n", str(info["start"]))
                    log.append((f, "list", f"numbering at '{tok.orig}'",
                                f"starts at {info['start']}"))
                else:
                    log.append((f, "skipped", f"list start at '{tok.orig}'",
                                "not the first item of its list"))
            last[d] = item
            for x in [x for x in last if x > d]:
                del last[x]
        else:
            parent = last.get(d - 1)
            k = next((i for i in range(len(conts) - 1, 0, -1)
                      if local(conts[i].el) in ("p", "q")), None)
            if parent is None or k is None:
                log.append((f, "skipped", f"paragraph at '{tok.orig}'",
                            "set inside a list item, but no item before it"))
                continue
            if nested_under(parent, path):
                continue
            blk = conts[k]
            detach(blk, conts[k - 1])
            append_block(parent, blk)
            log.append((f, "list", f"paragraph at '{tok.orig}'", "set inside the item before"))
    merge_lists(log)            # the lists a paragraph stood between


def first_words(ct, n):
    """The first n word/punct tokens inside a container, in order."""
    out = []

    def walk(ts):
        for t in ts:
            if len(out) >= n:
                return
            if t.kind in ("word", "punct"):
                out.append(t)
            elif t.kind == "container" and local(t.el) != "note":
                walk(t.children or [])
    walk(ct.children)
    return out


def has_words(t):
    """Whether a token (or anything in a container) has text."""
    if t.kind in ("word", "punct"):
        return bool(t.reg if t.reg is not None else t.orig)
    return t.kind in ("container", "group") and any(has_words(c) for c in t.children or [])


def leading(ct, tok):
    """The tokens of ct before tok, at every level down to it."""
    out = []
    for c in ct.children:
        if contains(c, tok):
            if c is not tok and c.kind == "container":
                out += leading(c, tok)
            return out
        out.append(c)
    return out


def lines_as_p(lg):
    """Verse lines the review sets as prose: one paragraph of their words
    (the line's id kept when there is one line)."""
    p = new_container("p")
    p.el.set("change", "#review")
    lines = [c for c in lg.children if c.kind == "container" and local(c.el) == "l"]
    kids = []
    for ln in lines:
        if kids:
            kids.append(Tok("space", [" "]))
        kids += ln.children
    if len(lines) == 1 and lines[0].el.get("{%s}id" % XML_NS):
        p.el.set("{%s}id" % XML_NS, lines[0].el.get("{%s}id" % XML_NS))
    p.children = kids
    relink(p)
    return p


def split_quote(q, pts, log):
    """A source quotation the review breaks up (CCEL puts prose and verse in
    one blockquote): split it at each point; a part after a new paragraph
    mark leaves the quotation (its paragraphs become the edition's own), a
    part after a new quote mark is a quotation of its own."""
    div = q.parent
    parts, cur = [(q, None)], q
    for tok, kind, _labels, _o, _f in pts:
        if kind == "unquote" and parts[-1][1] is None and \
                not any(has_content([c]) for c in leading(cur, tok)):
            parts[-1] = (cur, "unquote")        # from its first word on
            continue
        _left, right = split_container(cur, tok)
        parts.append((right, kind))
        cur = right
    out = []
    for ct, kind in parts:
        if kind is None:
            if has_content(ct.children):
                out.append(ct)
        elif kind == ">":
            ct.el.set("change", "#review")
            out.append(ct)
        else:
            for c in ct.children:
                if c.kind == "container" and local(c.el) == "lg":
                    out.append(lines_as_p(c))
                elif c.kind == "container":
                    c.el.set("change", "#review")
                    out.append(c)
    i = div.children.index(q)
    repl = []
    for k, t in enumerate(out):
        if k:
            repl.append(Tok("space", ["\n"]))
        repl.append(t)
    div.children[i:i + 1] = repl
    relink(div)
    log.append((pts[0][4], "split", "quotation",
                f"{len(parts) - 1} split(s) at " + ", ".join(s[0].orig or "" for s in pts)))


def restructure(splits, log):
    """splits: list of (tok, kind, label_toks, order, file). kind '+', '¶'
    or '>' (split there), 'quote' (the block is a quotation), 'merge' (the
    block continues the previous one)."""
    LATER = ("quote", "merge", "renumber", "unlist", "inline", "headmerge")
    tables = {}
    for s in splits:
        if s[1] == "tableinline":
            tables.setdefault(id(s[0]), (s[0], []))[1].append(s)
    for tb, ss in tables.values():
        marks = [m for m, _c in layout.table_reading(tb.el)[1] if m]
        if len(ss) == len(marks):
            tb.el.set("rend", "inline")
            tb.el.set("change", "#review")
            log.append((ss[0][4], "list", "table", "run into its sentence"))
        else:
            log.append((ss[0][4], "unresolved", "table",
                        f"{len(ss)} of its {len(marks)} lines run on; kept as is"))
    splits = [s for s in splits if s[1] != "tableinline"]
    later = [s for s in splits if s[1] in LATER]
    splits = [s for s in splits if s[1] not in LATER]
    by_block = {}
    for s in splits:
        b = block_of(s[0])
        if b is not None and local(b.el) == "quote":
            by_block.setdefault(id(b), (b, []))[1].append(s)
            continue
        if b is not None and local(b.el) == "lg" and s[1] == "¶":
            # verse the edition sets a line to a paragraph
            if b.el.get("rend") != "paragraphs":
                b.el.set("rend", "paragraphs")
                b.el.set("change", "#review")
                log.append((s[4], "verse", "lines", "set as paragraphs"))
            continue
        sg = next((a for a in ancestors(s[0]) if local(a.el) == "signed"), None)
        if sg is not None and SETTINGS["closer_plain"] and s[1] == "¶":
            # a signature the edition sets on two lines
            par = sg.parent
            _l, right = split_container(sg, s[0])
            right.el.set("change", "#review")
            i = next(k for k, c in enumerate(par.children) if c is sg)
            par.children[i + 1:i + 1] = [Tok("space", ["\n"]), right]
            relink(par)
            log.append((s[4], "split", "signature", f"new line at '{s[0].orig}'"))
            continue
        if b is None or local(b.el) != "p":
            log.append((s[4], "skipped", f"new {s[1]} before '{s[0].orig}'",
                        "not a paragraph (e.g. a list heading); kept as is"))
            continue
        by_block.setdefault(id(b), (b, []))[1].append(s)
    for b, pts in by_block.values():
        pts.sort(key=lambda s: s[3])
        if local(b.el) == "quote":
            split_quote(b, pts, log)
            continue
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
            if kind in ("+", "-"):
                item = new_container("item")
                kids = ct.children
                if not labels:
                    # a printed numeral ("9.") the review took no words from:
                    # the item's label, not text
                    ws = first_words(ct, 2)
                    if len(ws) == 2 and NUMERAL_RE.fullmatch(ws[0].orig or "") and \
                            ws[1].orig in (".", ")") and not ws[0].extra.get("tidx") and \
                            not ws[1].extra.get("tidx") and ws[0].reg in (None, ws[0].orig):
                        labels = ws
                if labels:
                    wrap_label(labels)
                    kids = ct.children
                item.children = kids
                relink(item)
                if lst is not None and lst.el.get("type") != ("numbered" if kind == "+"
                                                             else "bulleted"):
                    lst = None
                if lst is None:
                    lst = new_container("list")
                    lst.el.set("type", "numbered" if kind == "+" else "bulleted")
                    lst.el.set("change", "#review")
                    out.append(lst)
                    MADE_LISTS.append(lst)
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
    merge_lists(log)
    for tok, kind, _l, _o, f in sorted(later, key=lambda s: s[3]):
        if kind == "headmerge":
            head = next((a for a in ancestors(tok) if local(a.el) == "head"), None)
            div = head.parent if head is not None else None
            prev = None
            if div is not None and div.parent is not None:
                sibs = [c for c in div.parent.children if c.kind == "container"]
                k = next(i for i, c in enumerate(sibs) if c is div)
                prev = sibs[k - 1] if k else None
                # the last paragraph of the division before
                while prev is not None and local(prev.el) == "div":
                    blocks = [c for c in prev.children if c.kind == "container"
                              and local(c.el) in ("p", "div")]
                    prev = blocks[-1] if blocks else None
            if prev is None or local(prev.el) != "p":
                log.append((f, "skipped", f"head at '{tok.orig}'", "no paragraph before it"))
                continue
            for x in (prev, head):
                if not x.el.get("{%s}id" % XML_NS):
                    NOTE_SEQ["b"] = NOTE_SEQ.get("b", 0) + 1
                    x.el.set("{%s}id" % XML_NS, f"rb{NOTE_SEQ['b']}")
            prev.el.set("next", "#" + head.el.get("{%s}id" % XML_NS))
            head.el.set("prev", "#" + prev.el.get("{%s}id" % XML_NS))
            head.el.set("change", "#review")
            log.append((f, "merge", "heading", f"run on into the paragraph before at '{tok.orig}'"))
            continue
        if kind in ("unlist", "inline"):
            anc = ancestors(tok)
            item = next((a for a in anc if local(a.el) == "item"), None)
            lst = next((a for a in anc if local(a.el) == "list"), None)
            if kind == "unlist" and item is not None:
                item.el.set("rend", "paragraph")       # set as a paragraph
                item.el.set("change", "#review")
                log.append((f, "list", f"item at '{tok.orig}'", "set as a paragraph"))
            elif kind == "inline" and lst is not None and lst.el.get("rend") != "inline":
                lst.el.set("rend", "inline")
                lst.el.set("change", "#review")
                log.append((f, "list", f"list at '{tok.orig}'", "run into its sentence"))
                if local(lst.el.getparent()) != "p":
                    # a list between paragraphs: it runs on from the one before
                    kids = lst.parent.children
                    k = next(i for i, c in enumerate(kids) if c is lst)
                    prev = next((c for c in reversed(kids[:k]) if c.kind == "container"), None)
                    if prev is not None and local(prev.el) in ("p", "q"):
                        for x in (prev, lst):
                            if not x.el.get("{%s}id" % XML_NS):
                                NOTE_SEQ["b"] = NOTE_SEQ.get("b", 0) + 1
                                x.el.set("{%s}id" % XML_NS, f"rb{NOTE_SEQ['b']}")
                        prev.el.set("next", "#" + lst.el.get("{%s}id" % XML_NS))
                        lst.el.set("prev", "#" + prev.el.get("{%s}id" % XML_NS))
            continue
        if kind == "renumber":
            # a printed bullet list the review numbers: its numerals become labels
            lst = next((a for a in ancestors(tok) if local(a.el) == "list"), None)
            if lst is None:
                log.append((f, "skipped", f"numbering at '{tok.orig}'", "not in a list"))
                continue
            if lst.el.get("type") != "numbered":
                lst.el.set("type", "numbered")
                lst.el.set("subtype", "printed")
                lst.el.set("change", "#review")
                log.append((f, "list", "printed list", "numbered"))
            if _l:
                wrap_label(_l)
            continue
        # the innermost paragraph (a <q> may itself hold paragraphs); a
        # scripture epigraph the review sets as a quotation is one block
        b = next((a for a in ancestors(tok) if local(a.el) == "p"), None) or block_of(tok)
        if SETTINGS["closer_plain"]:
            b = next((a for a in ancestors(tok) if local(a.el) in
                      ("salute", "signed", "dateline")), None) or b
        if kind == "merge" and b is not None and local(b.el) == "p" and \
                any(has_words(c) for c in leading(b, tok)):
            # text after a printed list inside the paragraph: the review
            # runs the list into the sentence
            for c in layout.p_blocks(b.el):
                if local(c) == "list" and c.get("rend") != "inline":
                    c.set("rend", "inline")
                    c.set("change", "#review")
                    log.append((f, "list", f"list before '{tok.orig}'", "run into its sentence"))
            continue
        ep = next((a for a in ancestors(tok) if local(a.el) == "epigraph"), None)
        if kind == "quote" and ep is not None:
            b = ep
        if b is None or local(b.el) not in ("p", "q", "epigraph", "salute", "signed",
                                            "dateline"):
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
        # the block before, passing over any the review emptied
        prev = next((c for c in reversed(kids[:k]) if c.kind == "container"
                     and (has_words(c) or local(c.el) not in ("p", "list"))), None)
        if prev is None and local(b.parent.el) in ("closer", "opener"):
            # a closer's first line runs on from the paragraph before it
            outer = b.parent.parent.children
            j = next(i for i, c in enumerate(outer) if c is b.parent)
            prev = next((c for c in reversed(outer[:j]) if c.kind == "container"), None)
        if prev is not None and local(prev.el) in ("opener", "sp"):
            # a speech's last paragraph (CCEL can end a speech mid-sentence
            # and carry the rest on in a plain paragraph after it)
            prev = next((c for c in reversed(prev.children) if c.kind == "container"
                         and (local(prev.el) != "sp" or local(c.el) == "p")), prev)
        into_item = False
        if prev is not None and local(prev.el) == "list" and prev.el.get("rend") != "inline":
            # runs on into the list's last item: it moves into that item,
            # after the item's own text (and before anything set in it later)
            items = [c for c in prev.children if c.kind == "container" and
                     local(c.el) == "item"]
            if items:
                prev, into_item = items[-1], True
        run_in_head = prev is not None and local(prev.el) == "head" and \
            prev.el.getparent().get("type") in HEAD_MODE["run_in"]
        if prev is None or local(prev.el) not in ("p", "q", "item", "salute", "signed",
                                                  "dateline", "list") and not run_in_head:
            # the last block of the division before
            before = None
            if prev is None and b.parent.parent is not None:
                sibs = [c for c in b.parent.parent.children if c.kind == "container"]
                i = next((n for n, c in enumerate(sibs) if c is b.parent), 0)
                ps = [c for c in sibs[i - 1].children if c.kind == "container"
                      and local(c.el) == "p"] if i else []
                before = ps[-1] if ps else None
            if before is not None and not has_words(before):
                # the paragraph the review took out (margin matter set as a
                # note) was aligned this side of the break: nothing runs on
                log.append((f, "list", "blocks", "emptied by the review"))
                continue
            log.append((f, "skipped", f"merge at '{tok.orig}'", "no paragraph before it"))
            continue
        if into_item:
            detach(b, b.parent)
            append_block(prev, b)
        for x in (prev, b):
            if not x.el.get("{%s}id" % XML_NS):
                NOTE_SEQ["b"] = NOTE_SEQ.get("b", 0) + 1
                x.el.set("{%s}id" % XML_NS, f"rb{NOTE_SEQ['b']}")
        prev.el.set("next", "#" + b.el.get("{%s}id" % XML_NS))
        b.el.set("prev", "#" + prev.el.get("{%s}id" % XML_NS))
        b.el.set("change", "#review")
        if id(tok) in NO_SPACE_RUN_ON:
            b.el.set("rend", "run-on")
        log.append((f, "merge", "paragraph", f"joined to the previous one at '{tok.orig}'"))
    merge_lists(log)            # lists that a run-on paragraph kept apart


def collect_splits(struct, stream_index, log):
    splits = []
    for s in struct:
        at = s["at"]
        if at is None:
            continue
        tok = at[2]
        Sw = [x for x in s["S"] if x[1] == "w"]
        order = stream_index.get(id(tok), 0)
        tabs = [x[2] for x in s["S"] if x[1] == "m" and x[2].kind == "container"
                and local(x[2].el) == "table"]
        if tabs and len(tabs) == len(s["src_marks"]) and s["tgt_marks"] in ([], ["¶"]):
            # a table's reading the review runs into one sentence
            # (restructure checks that every one of its marks went)
            splits += [(tb, "tableinline", [], order, s["label"]) for tb in tabs]
            continue
        if s["tgt_marks"] == ["+"] and not s["src_marks"]:
            labels = []
            if len(Sw) >= 2 and (ROMAN_RE.match(Sw[0][0]) and Sw[1][0] == "." or
                                 NUMERAL_RE.fullmatch(Sw[0][0]) and Sw[1][0] in ".)"):
                labels = [Sw[0][2], Sw[1][2]]
            splits.append((labels[0] if labels else tok, "+", labels, order, s["label"]))
        elif s["tgt_marks"] == ["+"] and s["src_marks"] in (["¶"], ["-"]):
            labels = []
            if len(Sw) >= 2 and NUMERAL_RE.fullmatch(Sw[0][0]) and Sw[1][0] in ".)":
                labels = [Sw[0][2], Sw[1][2]]
            kind = "+" if s["src_marks"] == ["¶"] else "renumber"
            splits.append((labels[0] if labels else tok, kind, labels, order, s["label"]))
        elif s["tgt_marks"] == ["-"] and s["src_marks"] in ([], ["¶"]):
            splits.append((tok, "-", [], order, s["label"]))
        elif s["tgt_marks"] == ["¶"] and s["src_marks"] == ["-"]:
            splits.append((tok, "unlist", [], order, s["label"]))
        elif s["tgt_marks"] == ["¶"] and not s["src_marks"]:
            if in_container(tok, ("closer", "signed", "trailer")) and \
                    not (SETTINGS["closer_plain"] and in_container(tok, ("signed",))):
                continue
            splits.append((tok, "¶", [], order, s["label"]))
        elif s["tgt_marks"] == [">"] and not s["src_marks"]:
            splits.append((tok, ">", [], order, s["label"]))
        elif s["tgt_marks"] == [">"] and s["src_marks"] == ["¶"]:
            splits.append((tok, "quote", [], order, s["label"]))
        elif s["tgt_marks"] == ["¶"] and s["src_marks"] == [">"]:
            # the review takes a quotation's opening lines out of it (CCEL set
            # a line of prose as the first line of the verse)
            splits.append((tok, "unquote", [], order, s["label"]))
        elif s["src_marks"] == ["¶"] and not s["tgt_marks"] and \
                in_container(tok, ("trailer",)):
            continue          # a trailer the review left out
        elif s["src_marks"] == ["¶"] and not s["tgt_marks"]:
            splits.append((tok, "merge", [], order, s["label"]))
        elif len(s["src_marks"]) > 1 and not s["tgt_marks"] and \
                all(m in ("¶", "-", "+") for m in s["src_marks"]):
            # blocks the review deletes whole (margin matter moved into a
            # note): they stay, emptied; the block after them, if it keeps
            # any words, runs on into the text before them
            marks = [x for x in s["S"] if x[1] == "m"]
            blk = marks[-1][2]
            ws = first_words(blk, 1) if blk.kind == "container" else []
            if ws and has_words(blk):
                splits.append((ws[0], "merge", [], order, s["label"]))
            else:
                log.append((s["label"], "list", "blocks", "emptied by the review"))
        elif s["src_marks"] == ["H"] and not s["tgt_marks"]:
            # a printed division head the review runs on into the text
            # before it (the TCP made a sentence a heading)
            splits.append((tok, "headmerge", [], order, s["label"]))
        elif s["src_marks"] == ["-"] and not s["tgt_marks"]:
            # a printed list inside a paragraph that the review runs into
            # its sentence; else list nesting shown differently, kept as is
            lst = next((a for a in ancestors(tok) if local(a.el) == "list"), None)
            if lst is not None and lst.el.getparent() is not None and \
                    local(lst.el.getparent()) in ("p", "div"):
                splits.append((tok, "inline", [], order, s["label"]))
            continue
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
    if AUTHOR:
        name, why = AUTHOR
        for a in ts.findall(T + "author"):
            a.text = name
        ns_ = fd.find(T + "notesStmt")
        if ns_ is None:
            ns_ = etree.Element(T + "notesStmt")
            fd.insert(list(fd).index(fd.find(T + "sourceDesc")), ns_)
        etree.SubElement(ns_, T + "note", type="attribution").text = why
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
    ccel = SOURCE_KIND == "thml"
    paras = [
        ("This file is the CCEL text (converted from ThML) with editorial layers "
         "added inline; nothing of it has been removed." if ccel else
         "This file is the EEBO-TCP transcription with editorial layers added "
         "inline; nothing of the transcription has been removed."),
        "choice/orig holds the text as printed; choice/reg holds the modern "
        "reading. reg/@resp says who decided it (#auto = machine, #editor = "
        "reviewed by hand); reg/@type is spelling, case, punctuation, spacing, "
        "grammar (an archaic form modernized: thou, hath, -eth) or emendation "
        "(another word, or a word added or removed). "
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
    if ccel:
        # a modern source has no abbreviations, illegible print, period
        # spelling or transcription line breaks; say what it does have
        tcp_only = ("choice/abbr", "supplied:", "Spelling regularized", "Line breaks")
        paras = [x for x in paras if not x.startswith(tcp_only)]
        paras.append("The text is CCEL's, paragraph by paragraph; CCEL gives no page "
                     "or line information. quote: a block quotation or verse set off "
                     "in the source.")
        if TYPOGRAPHY:
            paras.append("reg[@type='punctuation'][@resp='#auto']: CCEL's straight "
                         "quotes curled and its -- set as an em dash.")
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
        (".//t:lg[@rend='paragraphs']", "lg[@rend='paragraphs']: verse this edition "
         "sets a line to a paragraph."),
        (".//t:item[@rend='paragraph']", "item[@rend='paragraph']: a printed list item "
         "this edition sets as a paragraph."),
        (".//t:list[@rend='inline']", "list[@rend='inline']: a printed list this "
         "edition runs into its sentence."),
        (".//t:label[@type='head']", "label[@type='head']: a heading this edition adds "
         "(its level in @n); it is not printed text."),
        (".//t:*[@rend='run-on']", "@rend='run-on': a block this edition runs on "
         "from the one before without a space between them."),
        (".//t:list[@rend]", "list/@rend: the numbering this edition gives a list "
         "(a Typst numbering pattern, e.g. 'a)'); item/@n on its first item: the "
         "number it starts from."),
        (".//t:epigraph[@rend='quote']", "epigraph[@rend='quote']: a scripture "
         "epigraph this edition sets as a quotation in the text."),
        (".//t:cell[@rend='nested']", "cell[@rend='nested']: a branch of a brace "
         "table this edition sets as an item under the branch before it."),
        (".//t:table[@rend='inline']", "table[@rend='inline']: a brace table this "
         "edition reads into one sentence, column by column."),
        (".//t:head[@next]", "head[@next]: a run-in head this edition sets as "
         "the opening words of its paragraph (p/@prev), not as a bold line."),
        (".//t:head[@prev]", "head[@prev]: a printed heading this edition runs on "
         "into the paragraph before it (a margin note or catchword set as a head)."),
        (".//t:p[@rend='epigraph']", "p[@rend='epigraph']: a paragraph holding a "
         "scripture text (reference and verse) this edition sets as an epigraph."),
        (".//t:head[@type='short']", "head[@type='short']: the short form of this "
         "edition's title, used in running heads."),
        (".//t:reg/t:hi", "hi inside reg: words of this edition's reading set in italic."),
        (".//t:list[@subtype='printed']", "list[@subtype='printed']: a list printed as "
         "one that this edition numbers; the printed numerals are kept in label."),
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
    ch.text = ("Enriched edition built from the CCEL text and the reviewed Typst chapters."
               if SOURCE_KIND == "thml" else
               "Enriched edition built from the TCP file and the reviewed Typst chapters.")
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
    cfg = {}
    if tables.exists():
        load_tables(tables)
        import runpy
        cfg = runpy.run_path(str(tables))
    elif args.tables:
        ap.error(f"no such file: {tables}")

    global SOURCE_KIND
    SOURCE_KIND = sources.kind(args.source)
    src = sources.load(args.source)
    tree = copy.deepcopy(src)
    root = tree.getroot()
    text = root.find(".//" + T + "text")
    toks = tokenize(text, {"macron": 0, "gap": 0})
    compute_auto(toks)
    if args.list:
        list_editorial(toks)
        return

    files = layout.book_layout(root, cfg)
    if files is not None:
        missing = layout.check(root, files, cfg)
        if missing:
            for el, n in missing[:20]:
                print(f"  not in any file: <{local(el)}> {n} words: "
                      f"{' '.join(''.join(el.itertext()).split())[:70]}", file=sys.stderr)
            sys.exit(f"LAYOUT leaves {len(missing)} text blocks out; add them to a "
                     "file or to SKIP_DIVISIONS")
        HEAD_MODE["on"] = True
        HEAD_MODE["run_in"] = set(cfg.get("RUN_IN_DIVS", ()))
        SETTINGS["closer_plain"] = bool(cfg.get("CLOSER_PLAIN"))
        if SETTINGS["closer_plain"]:
            BLOCK_MARK.update({"salute": "¶", "dateline": "¶"})
        return build_layout(args, tree, root, text, toks, files, cfg)

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
        ROOT["toks"] = toks
        apply_list_shape(log)

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





def build_layout(args, tree, root, text, toks, files, cfg=None):
    """main() for a book with a LAYOUT: each file is aligned as one unit with
    the parts the layout gives it; heads are part of its text."""
    by_el = {}

    def index(ts):
        for t in ts:
            if t.kind == "container":
                by_el[t.el] = t
                index(t.children)
    index(toks)
    log, unresolved, all_splits = [], [], []
    if args.review:
        R = Path(args.review)
        order = 0
        for f in files:
            fname = f["file"]
            path = R / fname
            if not path.exists():
                unresolved.append((fname, "file", "missing from the review"))
                continue
            review = reviewparse.parse_review(path.read_text(), inline_headings=True,
                                              titled=bool(f["title"]),
                                              edition_heads=bool((cfg or {}).get("EDITION_HEADINGS")))
            title = review.headings[0] if review.headings else None
            if f["title"] and title and " ".join(title.split()) != " ".join(f["title"].split()):
                unresolved.append((fname, "file title (change it in the LAYOUT)", title))
            sub = [f["subtitle"]] if f.get("subtitle") is not None else []
            SUBTITLES.update(sub)
            view = View([by_el[p] for p in sub + f["parts"]], None)
            st, s = review_division(view, review, fname, log, unresolved)
            index_ = {}
            for k, e in enumerate(s):
                index_.setdefault(id(e[2]), order + k)
            order += len(s)
            all_splits += collect_splits(st, index_, log)
        restructure(all_splits, log)
        ROOT["toks"] = toks
        apply_list_shape(log)
        apply_edition_heads(log)
    rebuild(text, toks)
    add_header(root, args.editor)
    tree.write(args.out, xml_declaration=True, encoding="UTF-8")
    if args.report:
        write_report(args.report, log, unresolved)
    print(f"wrote {args.out}: {len(files)} files, {len(log)} review decisions, "
          f"{len(unresolved)} unresolved")


def write_report(path, log, unresolved):
    from collections import Counter, defaultdict
    kinds = Counter(k for _, k, *_ in log)
    lines = ["# Review decisions carried into the enriched TEI", ""]
    if REPORT_NOTES:
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
              "emendation", "grammar", "punctuation", "case", "spelling"]:
        if k not in groups:
            continue
        lines.append(f"## {k}")
        lines.append("")
        if k in ("spelling", "case", "grammar"):
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
