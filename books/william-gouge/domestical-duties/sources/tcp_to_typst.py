#!/usr/bin/env python3
"""
tcp_to_typst.py
================

Convert an EEBO-TCP (Text Creation Partnership) TEI-XML transcription into
Typst (.typ), either preserving the original early-modern spelling exactly
or modernizing it (--modernize, via spelling.py).

This is a rewrite of the two-script version used for Perkins' *Christian
Oeconomie* (tcp_to_typst.py + modernize_render.py), which kept two nearly
identical renderers in step by hand and drifted.  Here there is ONE renderer
and modernization is a flag, so the old-spelling and modern-spelling renders
can never disagree about structure.

    python3 tcp_to_typst.py A68107.xml --list
    python3 tcp_to_typst.py A68107.xml --outdir out/
    python3 tcp_to_typst.py A68107.xml --outdir out/ --modernize
    python3 tcp_to_typst.py A68107.xml --sections 5 --gap-report gaps.tsv

The "1:N" numbering in a quod.lib.umich.edu URL
(.../A68107.0001.001/1:5?rgn=div1;view=fulltext) is the index into the
flattened list of direct <div> children of <front>, <body> and <back>;
--list prints that mapping.  Every EEBO-TCP text has a plain TEI-XML file at
https://github.com/textcreationpartnership/<ID> -- the site itself blocks
programmatic access, the GitHub mirror does not.

WHAT GETS RENDERED
------------------
- <hi> -> #emph[...]        (rend="sup" -> #super[...])
- <note> -> #footnote[...] spliced back in at its exact anchor point
- <table>/<row>/<cell> -> #table(...)
- <epigraph> (<bibl> + <q>) -> a centred scripture epigraph block
- <list>/<item> -> nested Typst bullet lists (nesting is carried by
  two-space indents, so never run a whitespace-collapsing pass on the output)
- <g ref="char:EOLhyphen"/> dropped so the two halves of the word rejoin
- <g ref="char:cmbAbbrStroke"/> (the macron abbreviation, "whe~" for "when")
  expanded via MACRON_M_OVERRIDE
- <gap reason="illegible"> reconstructed where possible (see gap_resolver.py),
  otherwise left as TCP's bullet placeholder
- <gap reason="foreign"> (Greek/Hebrew the transcribers could not key)
  dropped, along with the punctuation left dangling in front of it
- long s (U+017F) folded to plain "s" everywhere

DIV TYPE -> HEADING LEVEL
-------------------------
Configured by DIV_LEVELS / RUN_IN_DIVS at the top of the file.  For this book
a treatise is a chapter (level 2 in the fgbooks template: centred, opens on a
recto), a section is a run-in subheading (level 3), and a "question" div's
head is set as a bold run-in paragraph rather than a heading -- there are 242
of them and they are two words long ("Quest.", "Answ.").
"""

import argparse
import copy
import re
import sys
from pathlib import Path

from lxml import etree

import gap_resolver

NS = {"t": "http://www.tei-c.org/ns/1.0"}
WS_RE = re.compile(r"\s+")
ESCAPE_RE = re.compile(r"([\\#\$\*_`<>@\[\]])")

# Divs whose <head> becomes a real Typst heading, and at what level relative
# to the top-level div being rendered (which is itself level BASE_LEVEL).
BASE_LEVEL = 2
DIV_LEVELS = {"section": 3}
# Divs whose <head> is set as a bold run-in paragraph instead of a heading.
RUN_IN_DIVS = {"question"}


def local(tag):
    return etree.QName(tag).localname


# ---------------------------------------------------------------------------
# Source-text normalization
# ---------------------------------------------------------------------------

# The long s is a typographic variant of "s", not a different letter, and
# EEBO-TCP keys it literally (45,352 of them in this book).  Folding it here,
# at the point text is pulled out of the XML, means nothing downstream --
# spelling rules, the gap resolver, the word-frequency list -- ever has to
# know about it.  "VV" is likewise the compositor's W (only two here, both in
# the dedication's opening address).
def normalize_source(s):
    s = s.replace("ſ", "s")
    s = s.replace(" ", " ")
    s = re.sub(r"VV(?=[a-zſ])", "W", s)
    return s


def collapse(s):
    if s is None:
        return ""
    return WS_RE.sub(" ", normalize_source(s))


def esc(s):
    return ESCAPE_RE.sub(r"\\\1", s)


# ---------------------------------------------------------------------------
# The combining-macron abbreviation
# ---------------------------------------------------------------------------
# <g ref="char:cmbAbbrStroke"/> is a suppression mark over a vowel standing
# for a following nasal -- usually "n", sometimes "m", and the glyph itself
# does not say which.  There are 41 in this book; each was read in context and
# the "m" ones listed here by their 0-based document order.  These indices are
# specific to this text; rebuild the table for another one.
MACRON_M_OVERRIDE = set()
_macron_counter = {"i": -1}


def next_macron_letter():
    _macron_counter["i"] += 1
    return "m" if _macron_counter["i"] in MACRON_M_OVERRIDE else "n"


# ---------------------------------------------------------------------------
# Linearization
# ---------------------------------------------------------------------------
# A word is frequently split across inline markup -- justified line-wrapping
# means "ci<g ref="char:EOLhyphen"/>uill" is one word in two fragments, and an
# illegible letter in the middle of a word splits it again.  Transforming text
# fragment-by-fragment while walking the tree therefore processes each half of
# a split word independently and gets it wrong.  So: linearize a whole
# paragraph into ONE string first, with footnotes and inline markup held as
# placeholder tokens, do all text transformation in a single pass over that
# string, then splice the real markup back in.
#
# Placeholders are deliberately un-English and wrapped in NULs where they sit
# between words, so the word tokenizer can never fuse them with a real word or
# mistake "emph" for a word to capitalize.  Gap placeholders are the exception:
# they sit *inside* a word and must not be separated from it.

EM_START = "\x00ZZEMSTARTZZ\x00"
EM_END = "\x00ZZEMENDZZ\x00"
SU_START = "\x00ZZSUSTARTZZ\x00"
SU_END = "\x00ZZSUENDZZ\x00"


class Ctx:
    """Per-render mutable state: the footnote bodies collected so far and the
    gaps seen so far (both spliced back after text transformation)."""

    def __init__(self, resolver=None, inline_tables=False):
        self.footnotes = []
        self.gaps = []
        self.resolver = resolver
        # Set for a paragraph whose table interrupts a sentence, so the table
        # is flattened back into the running text instead of breaking it.
        self.inline_tables = inline_tables


def _leading_text_is_joinable_whitespace(el):
    """True if el.text is pure whitespace containing a newline -- i.e. just
    XML pretty-print indentation -- AND el's first child is a glyph-splice
    <g> or an illegible-text <gap>.  That "whitespace" is not a space in the
    source, it is noise before a mid-word continuation."""
    if not el.text or el.text.strip() or "\n" not in el.text:
        return False
    if len(el) == 0:
        return False
    return local(el[0].tag) in ("g", "gap")


def _tail_is_joinable_whitespace(child, tag):
    """Same trap on the other side: whitespace-only, newline-containing tail
    between two adjacent <g>/<gap> siblings.  Collapsing it to " " splits a
    word ("co" + macron + indent + "sent" must be "consent", not "con sent")."""
    next_el = child.getnext()
    joinable = ("g", "gap")
    return (tag in joinable and next_el is not None
            and local(next_el.tag) in joinable
            and not child.tail.strip() and "\n" in child.tail)


def linearize(el, ctx, in_note=False):
    parts = []
    if el.text and not _leading_text_is_joinable_whitespace(el):
        parts.append(esc(collapse(el.text)))
    for child in el:
        tag = local(child.tag)
        if tag == "hi":
            inner = linearize(child, ctx, in_note)
            if child.get("rend") == "sup":
                parts.append(f"{SU_START}{inner}{SU_END}")
            else:
                parts.append(f"{EM_START}{inner}{EM_END}")
        elif tag == "g":
            ref = child.get("ref", "")
            if ref == "char:cmbAbbrStroke":
                parts.append(next_macron_letter())
            elif ref in ("char:EOLhyphen", "char:EOLunhyphen"):
                pass  # soft line break: drop so the word rejoins
            elif child.text:
                parts.append(esc(normalize_source(child.text)))
        elif tag == "note":
            # A note's body is rendered immediately and in full (it is never
            # modernized -- see render_note), then held by an index token.
            body = render_note(child, ctx)
            if body:
                parts.append(ctx_note_token(ctx, body))
        elif tag == "gap":
            parts.append(render_gap(child, ctx))
        elif tag == "expan":
            # <expan><am><g ref="char:abque"/></am><ex>que</ex></expan>:
            # the abbreviation mark plus its editorial expansion.  Use the
            # expansion; the mark itself has no modern equivalent.
            ex = child.find(".//t:ex", namespaces=NS)
            if ex is not None and ex.text:
                parts.append(esc(collapse(ex.text)))
        elif tag in ("pb", "fw", "milestone"):
            pass
        elif tag == "table" and ctx.inline_tables:
            parts.append(linearize_table(child, ctx, in_note))
        else:
            # seg, bibl, q, abbr, corr, sic, unclear, term, and anything
            # unforeseen: recurse, so text is never silently dropped.
            parts.append(linearize(child, ctx, in_note))
            if tag == "seg" and child.get("rend") == "decorInit":
                parts.append(DECOR_INIT)
        if child.tail and not _tail_is_joinable_whitespace(child, tag):
            parts.append(esc(collapse(child.tail)))
    return "".join(parts)


def ctx_note_token(ctx, body):
    idx = len(ctx.footnotes)
    ctx.footnotes.append(body)
    return f"\x00ZZFN{idx:04d}ZZ\x00"


# What an unrecoverable gap looks like in the finished text.  TCP's own
# placeholders (a bullet per illegible letter, "<*>" for an illegible word)
# are markup for a transcriber, not something a reader should meet mid-word.
UNRECOVERED = "…"

# Whole leaves the microfilm did not capture.  This book has one: six pages
# between p. 190 and p. 197, in the middle of Treatise II part 2 on how a
# marriage contract is made.  Nothing in the TCP text can fill it, so say so
# where it happens rather than closing the sentence over the hole.
MISSING_NOTE = ("\\[{extent} of the 1622 edition are wanting here: they were "
                "not captured in the microfilm from which this text was "
                "transcribed.\\]")


def render_gap(gap_el, ctx):
    """Emit a placeholder for one <gap>.

    Illegible gaps get an index token the resolver fills in later -- it needs
    the letters on both sides, which are not known until the whole paragraph
    has been linearized.

    Foreign-script gaps -- Greek and Hebrew the transcribers could not key,
    240 of them, nearly all a single word in a marginal citation -- are
    dropped.  There is no page image here to read them from, and TCP's
    "< in non-Latin alphabet >" is noise in a reading edition.

    Duplicate-page gaps carry no text at all.  Missing-page gaps carry a
    great deal, and get an editorial note in its place."""
    reason = gap_el.get("reason")
    if reason in ("duplicate", "foreign"):
        return ""
    extent = gap_el.get("extent") or ""
    doc_idx = int(gap_el.get(gap_resolver.INDEX_ATTR, "-1"))
    if reason == "missing":
        placeholder = (EM_START + MISSING_NOTE.format(extent=extent.capitalize())
                       + EM_END)
        entry = (doc_idx, extent, placeholder, True)
    else:
        entry = (doc_idx, extent, UNRECOVERED, False)
    slot = len(ctx.gaps)
    ctx.gaps.append(entry)
    return f"ZZGAP{slot:04d}ZZ"


def render_note(note_el, ctx):
    """Render a marginal note.

    Perkins' *Christian Oeconomie* left note bodies in original spelling on
    the grounds that they were all Latin and bibliographic abbreviation.  That
    is not true here: alongside 2,000-odd citations, Gouge's margins carry a
    running analytical summary in English ("Inferiours duties first deliuered,
    to teach them how to winne their gouernours fauour"), and leaving those in
    1622 spelling beside modernized text reads as an accident.

    So notes ARE modernized -- but in "plain" mode, which fixes spelling and
    touches nothing else.  Latin survives it: the letterform oracle only
    changes a word when the result is a word an ENGLISH dictionary knows, and
    "iustum", "seruum", "Arist." are not, so they come through untouched (and
    "vt" -> "ut", "vxor" -> "uxor" are what a modern Latin text prints anyway).
    Sentence-capitalization is deliberately NOT applied: a note is a fragment,
    and capitalizing after every "l." and "cap." would wreck the citations.

    Notes cannot nest, so this uses its own Ctx and resolves its own gaps."""
    sub = Ctx(ctx.resolver)
    raw = linearize(note_el, sub, in_note=True).strip()
    raw = resolve_gaps(raw, sub)
    raw = strip_dropped_foreign(raw)
    raw = apply_text_fixes(re.sub(r" +", " ", raw).strip())
    if not raw:
        return ""
    if MODERNIZE["on"]:
        raw = modernize_abbreviations(_prose["plain"](raw))
    body = splice_footnotes(raw, sub)
    return escape_leading_marker(finalize_markup(body).strip())


# ---------------------------------------------------------------------------
# Post-linearization repairs on the flat string
# ---------------------------------------------------------------------------

GAP_TOKEN_RE = re.compile(r"ZZGAP(\d{4})ZZ")


def resolve_gaps(text, ctx):
    """Replace each gap token with a reconstruction, or with TCP's original
    bullet placeholder if the resolver cannot settle it.

    Left to right, one at a time, because the resolver matches on the letters
    on either side of the gap: a gap already resolved supplies real letters to
    the next one, while gaps still ahead are masked so their token text
    ("ZZGAP0007ZZ" -- all letters!) is never mistaken for context."""
    while True:
        m = GAP_TOKEN_RE.search(text)
        if not m:
            return text
        doc_idx, extent, default, raw = ctx.gaps[int(m.group(1))]
        fill = None
        if ctx.resolver is not None:
            fill = ctx.resolver.resolve(
                doc_idx, text[:m.start()],
                GAP_TOKEN_RE.sub("\x01", text[m.end():]), extent, default)
        if fill is None:
            fill = default if raw else esc(default)
        text = text[:m.start()] + fill + text[m.end():]


# Dropping a foreign-script gap can leave the punctuation that followed it
# stranded at the start of a note ("<Greek>. Arist. Eth." -> ". Arist. Eth.")
# or a doubled space mid-sentence.
def strip_dropped_foreign(text):
    text = re.sub(r"^\s*[.,;:]\s*", "", text)
    text = re.sub(r"\s+([.,;:])", r"\1", text)
    return text


# Repairs to the flat text, applied after gaps are filled.  Two things
# produce a word that no per-word rule can reach:
#
#  * TCP sometimes swallows a word space into an illegible span, so filling
#    the gap correctly still yields two words run together ("semel est" keyed
#    as "sem<gap/>lest").  Conversely a spurious space can survive inside a
#    word.  Splicing letters at the gap cannot add or remove a space, so the
#    repair belongs here.
#  * A letter misread by the transcriber before the illegible span, so the
#    join is right but the surrounding letters are not ("C•raelius" for
#    Cornelius, identified by the Acts 10 citation in its own margin).
#
# Every entry is checked against context or against the work being cited.
# Keys are matched literally, so keep them long enough to be unambiguous.
TEXT_FIXES = {
    "before thetime of": "before the time of",
    "Quo semelest imbuta": "Quo semel est imbuta",
    "addictorum construx it": "addictorum construxit",
    "children: solikewise": "children: so likewise",
    "man and wife ouaght": "man and wife ought",
    "Abraham: ne que quicquam": "Abraham: neque quicquam",
    "Ministers are bourd to teach": "Ministers are bound to teach",
    "Craelius": "Cornelius",
    "his mastersmeanes": "his masters meanes",
    "Ex opere operato, B em.": "Ex opere operato, Bellarm.",
}


def apply_text_fixes(text):
    for wrong, right in TEXT_FIXES.items():
        text = text.replace(wrong, right)
    return text


# Typographic abbreviations the 1622 compositor used and a modern reader does
# not.  Unlike TEXT_FIXES, which repair transcription damage and belong in
# both renders, these are modernization and run only under --modernize.  They
# apply inside Latin quotations too: "&c." is et cetera in either language,
# which is why this is not part of the word-level spelling rules.
ABBREVIATIONS = (
    (re.compile(r"&c\.?"), "etc."),
)


def modernize_abbreviations(text):
    for pattern, repl in ABBREVIATIONS:
        text = pattern.sub(repl, text)
    return text


DECOR_INIT = "\x02"


def fix_decorinit(text):
    """A decorated initial capital is followed in the source by a letter the
    original typesetting also set capital -- <seg rend="decorInit">A</seg>S
    there are... is the word "As", and CHristian is "Christian".  linearize()
    marks the join; lowercase the letter after it.

    Matching on "two capitals then a lowercase" instead would miss "AS there"
    (a space, not a lowercase letter, follows) and would fire on any genuine
    two-capital opening, so the marker is worth carrying."""
    def repl(m):
        return m.group(1).lower()

    return re.sub(DECOR_INIT + r"([A-Z])", repl, text).replace(DECOR_INIT, "")


def splice_footnotes(text, ctx):
    def repl(m):
        return f"#footnote[{ctx.footnotes[int(m.group(1))]}]"

    return re.sub(r"\x00ZZFN(\d{4})ZZ\x00", repl, text)


def finalize_markup(text):
    text = text.replace(EM_START, "#emph[").replace(EM_END, "]")
    text = text.replace(SU_START, "#super[").replace(SU_END, "]")
    return text.replace("\x00", "")


# A Typst content block re-parses its body as markup, so a footnote or list
# item whose text opens with "1. " (very common -- "1. Cor. 7.") or with "- "
# becomes a list *inside* the block, swallowing what follows.  Escape the
# marker so it stays literal.
def escape_leading_marker(text):
    m = re.match(r"(\s*\d+)([.)])(\s)", text)
    if m:
        return text[:m.end(1)] + "\\" + text[m.start(2):]
    m = re.match(r"(\s*)([-+/])(\s)", text)
    if m:
        return text[:m.end(1)] + "\\" + text[m.start(2):]
    return text


# ---------------------------------------------------------------------------
# The one place text transformation happens
# ---------------------------------------------------------------------------

MODERNIZE = {"on": False}
_prose = {"fn": None, "plain": None}


def _load_modernizer():
    from modernize import modernize_prose_text, modernize_plain, ProseState
    _prose["fn"] = lambda t: modernize_prose_text(t, ProseState())
    _prose["plain"] = modernize_plain


def render_text_block(el, ctx, mode="prose"):
    """Linearize `el`, repair it, optionally modernize it, and splice the
    real markup back in.  This is the only path from XML to output text, so
    the old-spelling and modern-spelling renders differ in exactly one step."""
    raw = linearize(el, ctx).strip()
    raw = resolve_gaps(raw, ctx)
    raw = strip_dropped_foreign(raw)
    raw = apply_text_fixes(re.sub(r" +", " ", raw).strip())
    if mode == "prose":
        raw = fix_decorinit(raw)
    if MODERNIZE["on"] and raw:
        raw = _prose["fn"](raw) if mode == "prose" else _prose["plain"](raw)
        # After the modernizer, never before: "etc." ends in a period, and
        # feeding that to sentence-aware capitalization turns the next word
        # into a sentence opening -- and "&c." itself into "Etc.".
        raw = modernize_abbreviations(raw)
    return finalize_markup(splice_footnotes(raw, ctx)).strip()


def render_paragraph_like(el, mode="prose", inline_tables=False):
    ctx = Ctx(GAP_RESOLVER["r"], inline_tables=inline_tables)
    return render_text_block(el, ctx, mode)


GAP_RESOLVER = {"r": None}


# ---------------------------------------------------------------------------
# Block-level rendering
# ---------------------------------------------------------------------------

def render_list(list_el, depth=0):
    lines = []
    indent = "  " * depth
    head = list_el.find("t:head", namespaces=NS)
    if head is not None:
        text = render_paragraph_like(head).strip()
        if text:
            lines += [f"{indent}#strong[{text}]", ""]
    for item in list_el.findall("t:item", namespaces=NS):
        sub_lists = item.findall("t:list", namespaces=NS)
        # Render the item's own text without its nested sub-lists, which are
        # rendered separately one level deeper.  Copy rather than mutate: the
        # tree is walked again by the other render mode.
        stripped = copy.deepcopy(item)
        stripped.tail = None
        for child in stripped.findall("t:list", namespaces=NS):
            # lxml drops an element's tail along with the element, and that
            # tail is the item's own text resuming after the sub-list.
            prev, tail = child.getprevious(), child.tail
            if tail:
                if prev is not None:
                    prev.tail = (prev.tail or "") + tail
                else:
                    stripped.text = (stripped.text or "") + tail
            stripped.remove(child)
        text = escape_leading_marker(render_paragraph_like(stripped).strip())
        if text:
            lines.append(f"{indent}- {text}")
        for sub in sub_lists:
            lines.extend(render_list(sub, depth + 1))
    return lines


def _cell_span(cell):
    def n(attr):
        try:
            return max(1, int(cell.get(attr, "1")))
        except ValueError:
            return 1
    return n("rows"), n("cols")


def table_layout(table_el):
    """Place every <cell> on a grid, honouring rowspan and colspan.

    Returns (placements, ncols, carried), where placements is
    [(cell_element, row, col, rowspan, colspan), ...] in document order and
    `carried` is the set of rows an earlier rowspan reaches into.
    Trailing empty unspanned cells are dropped -- the source uses them as
    spacers, and rendered they are a column of blanks.

    One geometry, two readings: `render_table` walks it row by row, and
    `linearize_table` walks it column by column (see there for why)."""
    placements = []
    occupied = {}                       # column -> rows still held above
    carried = set()                     # rows an earlier rowspan reaches into
    ncols = 0
    for row_i, row in enumerate(table_el.findall("t:row", namespaces=NS)):
        if any(n > 0 for n in occupied.values()):
            carried.add(row_i)
        # Empty unspanned cells are the compositor's spacers, and taking them
        # as real columns pushes everything after them out of line: Treatise
        # I's "was {Creator/Creature}, but here {Head/Body}" puts a blank
        # where "Body" belongs and strands "Body" two columns further on.
        # Dropping them puts each branch back under its own head.
        cells = [c for c in row.findall("t:cell", namespaces=NS)
                 if "".join(c.itertext()).strip() or _cell_span(c) != (1, 1)]
        col = 0
        for cell in cells:
            rowspan, colspan = _cell_span(cell)
            while occupied.get(col, 0) > 0:
                col += 1
            placements.append((cell, row_i, col, rowspan, colspan))
            for c in range(col, col + colspan):
                occupied[c] = rowspan
            col += colspan
        ncols = max(ncols, col)
        occupied = {c: n - 1 for c, n in occupied.items() if n > 1}
    return placements, ncols, carried


# A list item usually carries its own number ("1. Cheerfulnesse.") and often
# the comma that separated it from the next.  The enum marker supplies the
# number, so strip it; strip the comma too, and close the list with a full
# stop when nothing follows it.
# These run on finished markup, so the terminator to look behind is the "]"
# that closes an #emph[...], not the placeholder the linearizer used.
ITEM_NUMBER_RE = re.compile(r"^\d{1,2}[.)]\s+")
ITEM_COMMA_RE = re.compile(r",(\s*[\])]*)\s*$")
ENDS_SENTENCE_RE = re.compile(r"[.!?:;][\s)\]]*$")


# Skip past any markup a cell opens with, to find the first letter of the
# actual words: "#emph[husbands," has to be capitalized at the "h", not at
# the "e" of "emph".
LEAD_MARKUP_RE = re.compile(r"#[a-z]+\[|[\s(\[\"']")


def _capitalize_item(text):
    i = 0
    while i < len(text):
        m = LEAD_MARKUP_RE.match(text, i)
        if not m:
            break
        i = m.end()
    if i < len(text) and text[i].islower():
        return text[:i] + text[i].upper() + text[i + 1:]
    return text


def _list_item(text, final):
    """A branch of a brace, set as its own line: it opens with a capital and,
    if nothing follows the list, closes with a full stop.

    A brace's LABEL gets neither -- it continues the sentence running through
    the diagram ("of an husband.", "but here", "all which he"), so it keeps
    the case the compositor gave it."""
    text = ITEM_NUMBER_RE.sub("", text.strip())
    text = ITEM_COMMA_RE.sub(r"\1", text)
    if final and text and not ENDS_SENTENCE_RE.search(text):
        text += "."
    return escape_leading_marker(_capitalize_item(text))


def render_table(table_el):
    """Set a table as a lead-in and a list, never as a grid.

    The source's "tables" are not tabular data.  They are the brace diagrams a
    1622 compositor drew to show one thing dividing into several -- "Behold
    here the mutual relation betwixt {Christ, / The Church.}" -- plus a
    handful of genuine row-wise lists in the front matter.  Set as a grid they
    read as neither: the brace's label floats in a column of its own and the
    branches sit in a second column with nothing to align to.

    Two shapes, told apart by whether any cell spans rows:

    A BRACE (71 of the 76) is read COLUMN by column, because that is how a
    brace groups.  A column holding one cell is the brace's label and becomes
    a paragraph; a column holding several is its branches and becomes an
    enumerated list.  Labels can stand on either side, or on both -- "The
    effect is noted partly as a {Confirmation of the truth / Declaration of
    the measure} of Christs love" -- and column order keeps them in the order
    they are read.

    A ROW-WISE TABLE (the front matter's parallels of duties) is read row by
    row: each row is one entry, a row of a single full-width cell is a heading
    over what follows, and a short leading cell is the entry's number, which
    the enum marker replaces."""
    placements, ncols, _carried = table_layout(table_el)
    if not placements:
        return []
    if any(rowspan > 1 for _c, _r, _col, rowspan, _cs in placements):
        return _render_brace(placements, ncols)
    return _render_rows(placements, ncols)


def _render_brace(placements, ncols):
    columns = {}
    for cell, row, col, rowspan, colspan in placements:
        columns.setdefault(col, []).append((row, cell))

    rendered = []
    for col in sorted(columns):
        texts = []
        for _row, cell in sorted(columns[col]):
            text = render_paragraph_like(cell, "plain").strip()
            if text:
                texts.append(text)
        if texts:
            rendered.append(texts)

    out = []
    for i, texts in enumerate(rendered):
        final = i == len(rendered) - 1
        if len(texts) == 1:
            # The brace's label, on whichever side the compositor drew it.
            out += [ITEM_COMMA_RE.sub(r"\1", texts[0]), ""]
        else:
            out += [f"+ {_list_item(t, final)}" for t in texts] + [""]
    return out


def _render_rows(placements, ncols):
    rows = {}
    for cell, row, col, rowspan, colspan in placements:
        rows.setdefault(row, []).append((col, cell, colspan))

    out = []
    for row in sorted(rows):
        cells = sorted(rows[row])
        # A row of one cell is a heading over what follows ("TREAT. III.") or
        # the lead-in to it, not an entry with its columns missing.  Left as
        # the source set it: it italicizes what it means to.
        if len(cells) == 1:
            text = render_paragraph_like(cells[0][1], "plain").strip()
            if text:
                out += ["", text, ""]
            continue
        texts = [render_paragraph_like(c, "plain").strip() for _col, c, _cs in cells]
        # A short leading cell is the entry's own number; the enum supplies it.
        if len(texts) > 1 and re.fullmatch(r"\d{1,2}[.)]?", texts[0]):
            texts = texts[1:]
        text = " ".join(t for t in texts if t).strip()
        if text:
            out.append(f"+ {escape_leading_marker(text)}")
    return out + [""]


# A cell often carries the comma that separates it from the next, so joining
# with ", " would double it.  The comma sits inside the emphasis the source
# put round the word, so strip it from in front of any closing markers.
TRAILING_COMMA_RE = re.compile(
    r",(\s*(?:\x00ZZ(?:EM|SU)ENDZZ\x00)*)\s*$")


def linearize_table(table_el, ctx, in_note):
    """A brace diagram flattened back into the sentence it interrupts.

    Read COLUMN by column, because that is what the brace groups: the 1622
    compositor set "a family consisteth of these three orders" as two rows of
    three, and the three orders are the columns -- husbands over wives,
    parents over children, masters over servants. Read row by row it comes out
    as "Husbands, Parents, Masters, Wives, Children, Servants", which is not
    three orders of anything. A cell spanning the rows is the brace's own
    label and falls where its column does."""
    parts = []
    placements, _ncols, _carried = table_layout(table_el)
    for cell, row_i, col, _rowspan, _colspan in sorted(
            placements, key=lambda p: (p[2], p[1])):
        text = TRAILING_COMMA_RE.sub(r"\1", linearize(cell, ctx, in_note).strip())
        if text:
            parts.append(text)
    return ", ".join(parts)


# Block-level elements this text nests inside a <p>.  A paragraph containing
# one has to be split around it: linearizing a whole table into the running
# text turns the author's side-by-side parallel of husbands' and wives'
# duties into an unreadable ribbon of prose.
BLOCK_IN_P = ("table", "list")


def _text_follows(p, node):
    """True if anything but whitespace comes after `node` inside `p` -- i.e.
    the block is interrupting a sentence rather than standing between them."""
    seen = False
    for child in p:
        if child is node:
            seen = True
            continue
        if seen and ((child.tail or "").strip()
                     or "".join(child.itertext()).strip()):
            return True
    return bool((node.tail or "").strip())


def render_paragraph(el):
    blocks = [c for c in el if local(c.tag) in BLOCK_IN_P]
    if not blocks:
        txt = render_paragraph_like(el)
        return [txt, ""] if txt else []

    # A brace diagram set in the middle of a sentence -- "a family consisteth
    # of these three orders, {Husbands/Wives, Parents/Children,
    # Masters/Servants} all which he reckoneth up" -- must not break the
    # paragraph in three: the sentence would be cut in half and the resumption
    # capitalized as if it began one.  Flatten it back into the running text
    # and render the paragraph in a single pass.  Only one table in this book
    # sits that way; the other 76 stand on their own and stay tables.
    if any(local(b.tag) == "table" and _text_follows(el, b) for b in blocks):
        txt = render_paragraph_like(el, inline_tables=True)
        return [txt, ""] if txt else []

    src = copy.deepcopy(el)
    src.tail = None
    out = []
    run = etree.Element(src.tag)
    run.text = src.text
    for child in list(src):
        tag = local(child.tag)
        if tag not in BLOCK_IN_P:
            run.append(child)       # moves it, tail and all, out of src
            continue
        txt = render_paragraph_like(run)
        if txt:
            out += [txt, ""]
        tail, child.tail = child.tail, None
        out += render_table(child) if tag == "table" else render_list(child) + [""]
        run = etree.Element(src.tag)
        run.text = tail
    txt = render_paragraph_like(run)
    if txt:
        out += [txt, ""]
    return out


def render_epigraph(ep_el):
    """<epigraph><bibl>EPHES. 5. 21.</bibl><q>Submit your selues...</q></epigraph>
    -- the scripture text a treatise expounds.  Set centred and italic above
    the first section."""
    bibl = ep_el.find("t:bibl", namespaces=NS)
    quote = ep_el.find("t:q", namespaces=NS)
    ref = render_paragraph_like(bibl, "plain").strip() if bibl is not None else ""
    body = render_paragraph_like(quote).strip() if quote is not None else ""
    if not (ref or body):
        return []
    lines = ["#align(center)[", "  #block(width: 85%)[", "    #set par(justify: false)"]
    if ref:
        lines.append(f"    #text(size: 0.9em, weight: 600)[{ref}]")
        lines.append("")
    if body:
        lines.append(f"    #emph[{body}]")
    lines += ["  ]", "]", "", "#v(0.8em)", ""]
    return lines


def render_closer(closer_el):
    signed = closer_el.find("t:signed", namespaces=NS)
    if signed is None:
        return []
    txt = render_paragraph_like(signed).strip()
    return [f"#align(right)[{txt}]", ""] if txt else []


def render_block(el):
    tag = local(el.tag)
    if tag == "p":
        return render_paragraph(el)
    if tag == "list":
        return render_list(el) + [""]
    if tag == "table":
        return render_table(el)
    if tag == "epigraph":
        return render_epigraph(el)
    if tag == "closer":
        return render_closer(el)
    if tag == "q":
        txt = render_paragraph_like(el)
        return [f"#quote(block: true)[{txt}]", ""] if txt else []
    if tag in ("pb", "head", "fw", "trailer"):
        return []
    txt = render_paragraph_like(el)
    return [txt, ""] if txt else []


# A top-level head in this book is a title and a descriptive subtitle run
# together: "The first Treatise. AN EXPOSITION OF THAT PART OF SCRIPTURE out
# of which Domestical Duties are raised."  Set at chapter-opening size that is
# a wall of type, so split it at the first sentence break.
# The split point is the first sentence break, allowing for the closing
# bracket of an #emph[...] that the source's <hi> markup put around the title
# half ("#emph[The first Treatise.] AN EXPOSITION OF...").
HEAD_SPLIT_RE = re.compile(r"^(.{4,70}?[.:]\]?)\s+(\S.*)$", re.S)


# Repairs to a rendered top-level heading.  Treatise II is printed in two
# parts, each with its own title page reading "The second Treatise." above a
# separate "PART I." line -- which splits into two chapters both titled "The
# second Treatise", indistinguishable in the table of contents.  Fold the part
# number into the title instead.
HEAD_FIXES = [
    (re.compile(r"^(#emph\[The second Treatise)\.\]\s+PART\.?\s+(I+)\."),
     r"\1, Part \2.]"),
    # The dedication's head is the whole address to the parishioners of
    # Blackfriars, with no sentence break in it -- as a chapter title and a
    # line in the table of contents it is unusable.  Give it the name the
    # thing has always had and let the address become its subtitle.
    (re.compile(r"^(#emph\[TO THE RIGHT HONOURABLE,)"),
     r"The Epistle Dedicatory. \1"),
]


def apply_head_fixes(text):
    for pattern, repl in HEAD_FIXES:
        text = pattern.sub(repl, text)
    return text


def unwrap_emph(text):
    """Strip an #emph[...] that wraps the WHOLE string.  A heading is already
    styled and a subtitle block adds its own emphasis, so the markup would
    only nest.  Leaves "#emph[a] and #emph[b]" alone by checking that the
    bracket opened at the start is the one closed at the end."""
    while text.startswith("#emph[") and text.endswith("]"):
        depth = 0
        for i, ch in enumerate(text):
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    break
        if i != len(text) - 1:
            return text
        text = text[len("#emph["):-1].strip()
    return text


def subtitle_block(text):
    # The line break after the #set matters: Typst is still in code mode
    # until the statement ends, so a "#emph" on the same line is a syntax
    # error rather than markup.
    return ["#align(center)[#block(width: 80%)[",
            "  #set par(justify: false)",
            f"  #emph[{unwrap_emph(text)}]",
            "]]", "", "#v(1.2em)", ""]


def render_heads(div_el, level, run_in):
    """Render every direct <head> of a div.  The first is the heading proper;
    a second (a chapter number line and then its descriptive title) is set
    centred underneath it."""
    out = []
    heads = div_el.findall("t:head", namespaces=NS)
    for i, head in enumerate(heads):
        text = re.sub(r"\s+", " ", render_paragraph_like(head, "heading").strip())
        if not text:
            continue
        if run_in:
            out += [f"#strong[{text}]", ""]
        elif i == 0:
            subtitle = None
            if level == BASE_LEVEL:
                text = apply_head_fixes(text)
                m = HEAD_SPLIT_RE.match(text)
                if m:
                    text, subtitle = m.group(1), m.group(2)
                text = unwrap_emph(text).rstrip(".")
            out += [f"{'=' * level} {text}", ""]
            if subtitle:
                out += subtitle_block(subtitle)
        else:
            out += subtitle_block(text)
    return out


def render_div(div_el, level):
    dtype = div_el.get("type")
    run_in = dtype in RUN_IN_DIVS
    out = render_heads(div_el, level, run_in)
    for child in div_el:
        tag = local(child.tag)
        if tag == "head":
            continue
        if tag == "div":
            child_level = DIV_LEVELS.get(child.get("type"), level + 1)
            out.extend(render_div(child, child_level))
        else:
            out.extend(render_block(child))
    return out


def section_divs(div_el):
    """The direct <div> children of a top-level div, in order.  In this text
    they are all type="section", and they are what a chapter is built out of.

    Chapters are cut by ORDINAL POSITION, not by the printed section number.
    Gouge's numbering is not reliable: Treatise IV prints "s. 15", "s. 43",
    "s. 46" and "s. 58" twice each, Treatise VIII prints "s. 4" twice, and two
    sections (Treatise VII, 19th; Treatise VIII, 27th) have no heading at all.
    Position is unambiguous; the printed number is not."""
    return [c for c in div_el if local(c.tag) == "div"]


def render_chapter(div_el, first, last, title, subtitle=None):
    """Render sections `first`..`last` (1-based ordinals, inclusive) of a
    top-level div as one chapter under its own heading.

    A chapter starting at section 1 also picks up whatever stands before the
    first section -- for Treatise I that is the scripture epigraph the whole
    treatise expounds."""
    out = [f"{'=' * BASE_LEVEL} {title}", ""]
    if subtitle:
        out.extend(subtitle_block(subtitle))
    seen = 0
    for child in div_el:
        tag = local(child.tag)
        if tag == "head":
            continue
        if tag == "div":
            seen += 1
            if first <= seen <= last:
                level = DIV_LEVELS.get(child.get("type"), BASE_LEVEL + 1)
                out.extend(render_div(child, level))
        elif seen == 0:
            if first == 1:
                out.extend(render_block(child))
        elif first <= seen <= last:
            out.extend(render_block(child))
    return "\n".join(out).rstrip() + "\n"


PREAMBLE = """#set page(width: 6in, height: 9in, margin: 1in)
#set par(justify: true)
#set text(font: "New Computer Modern", size: 11pt)
"""


def render_top_div(div_el, standalone=True):
    lines = []
    if standalone:
        lines += [PREAMBLE, ""]
    lines.extend(render_div(div_el, BASE_LEVEL))
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Top-level division discovery (the quod.lib.umich.edu "1:N" numbering)
# ---------------------------------------------------------------------------

def get_top_divs(root):
    divs = []
    text_el = root.find(".//t:text", namespaces=NS)
    for section_name in ("front", "body", "back"):
        section = text_el.find(f"t:{section_name}", namespaces=NS)
        if section is not None:
            divs.extend(section.findall("t:div", namespaces=NS))
    return divs


def div_label(div_el, index):
    dtype = div_el.get("type") or f"section{index}"
    head = div_el.find("t:head", namespaces=NS)
    title = ""
    if head is not None:
        title = re.sub(r"\s+", " ", normalize_source("".join(head.itertext()))).strip()
    return dtype, title


def slugify(s):
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower() or "section"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="Path to a TEI XML file")
    ap.add_argument("--sections", nargs="*", type=int, default=None,
                    help="1-based indices of top-level divs (quod.lib's 1:N). Default: all.")
    ap.add_argument("--outdir", default="out")
    ap.add_argument("--list", action="store_true",
                    help="List the top-level divs (index, type, heading) and exit")
    ap.add_argument("--modernize", action="store_true",
                    help="Modernize spelling (see spelling.py); default is original spelling")
    ap.add_argument("--no-standalone", action="store_true",
                    help="Omit the page-setup preamble (for files meant to be #include-d)")
    ap.add_argument("--gap-report", metavar="TSV",
                    help="Write a report of every illegible gap and what was filled in")
    ap.add_argument("--no-gap-fill", action="store_true",
                    help="Leave every illegible gap as TCP's bullet placeholder")
    ap.add_argument("--names", nargs="*", default=[], metavar="N=SLUG",
                    help="Name the output file for div N (e.g. 5=treatise-1) "
                         "instead of the default <index>-<div type>")
    args = ap.parse_args()

    tree = etree.parse(args.source)
    root = tree.getroot()
    top_divs = get_top_divs(root)
    if not top_divs:
        sys.exit("No top-level <div> elements found under front/body/back.")

    if args.list:
        for i, div_el in enumerate(top_divs, start=1):
            dtype, title = div_label(div_el, i)
            print(f"1:{i}\t{dtype}\t{title[:70]}")
        return

    if args.modernize:
        MODERNIZE["on"] = True
        _load_modernizer()

    if not args.no_gap_fill:
        GAP_RESOLVER["r"] = gap_resolver.GapResolver(root, normalize_source)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    names = dict(pair.split("=", 1) for pair in args.names)
    wanted = (set(args.sections) if args.sections
              else set(int(k) for k in names) if names
              else set(range(1, len(top_divs) + 1)))

    for i, div_el in enumerate(top_divs, start=1):
        if i not in wanted:
            continue
        dtype, _ = div_label(div_el, i)
        out_path = outdir / f"{names.get(str(i), f'{i:02d}-{slugify(dtype)}')}.typ"
        out_path.write_text(render_top_div(div_el, not args.no_standalone),
                            encoding="utf-8")
        print(f"Wrote {out_path} (1:{i}, type={dtype})")

    print(f"Macron abbreviations expanded: {_macron_counter['i'] + 1}", file=sys.stderr)
    if GAP_RESOLVER["r"] is not None:
        GAP_RESOLVER["r"].summarize(sys.stderr)
        if args.gap_report:
            GAP_RESOLVER["r"].write_report(args.gap_report)
            print(f"Gap report: {args.gap_report}", file=sys.stderr)


if __name__ == "__main__":
    main()
