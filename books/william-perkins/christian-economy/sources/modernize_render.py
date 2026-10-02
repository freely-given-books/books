#!/usr/bin/env python3
"""
Render dedication + treatise divs from A09377.xml into MODERNIZED-spelling
Typst files (dedication_modern.typ, treatise_modern.typ), while leaving the
original old-spelling .typ files completely untouched.

Key design point: a word can be split across inline markup in the source
(most commonly a line-break hyphen, <g ref="char:EOLhyphen"/>, e.g.
"ci<EOLhyphen/>uill" for "ciuill"). Modernizing each side of such a split
independently breaks word-level rules. So for each paragraph/heading/list
item/signature we first LINEARIZE the whole thing into one plain string
(with footnotes pulled out into placeholders, since their content must NOT
be modernized), modernize that single string in one pass, then splice the
footnotes back in.

What this changes:
 - Old spelling -> modern spelling, word-by-word (never changing which word
   is used -- see spelling.py for the exact rules/exceptions).
 - The "combining macron" abbreviation (e.g. "whe" for "when") is expanded
   to full modern spelling.
 - A small, explicit list of unambiguous common nouns (family, marriage,
   contract, husband, master, ...) gets lowercased when NOT at the start of
   a sentence, fixing the Early-Modern convention of capitalizing common
   nouns. Titles/religious terms (God, Lord, Church, King, Bishop, ...) are
   deliberately left alone rather than guessed at.
 - The "drop-cap" artifact where the first two letters of a paragraph's
   first word both ended up capitalized (e.g. "CHristian") is fixed.

What this does NOT change:
 - Footnote/marginal-note content (citations, Latin, abbreviations) --
   left exactly as in the original-spelling version.
 - Heading text capitalization pattern (spelling is still modernized).
 - Any actual wording -- "hath", "doth", "thou" etc. are untouched.
"""

import re
from lxml import etree
from spelling import modernize_word_lower, apply_case_pattern, GRAMMAR_EXCEPTIONS

NS = {"t": "http://www.tei-c.org/ns/1.0"}
WS_RE = re.compile(r"\s+")
ESCAPE_RE = re.compile(r"([\\#\$\*_`<>@\[\]])")


def local(tag):
    return etree.QName(tag).localname


def collapse(s):
    if s is None:
        return ""
    return WS_RE.sub(" ", s)


def esc(s):
    return ESCAPE_RE.sub(r"\\\1", s)


MACRON_M_OVERRIDE = {
    4, 29, 31, 35, 51, 53, 62, 72, 75, 78, 79, 81, 87, 88, 93,
    109, 113, 115, 132, 141, 144, 146, 151,
}
_macron_counter = {"i": -1}


def next_macron_letter():
    _macron_counter["i"] += 1
    return "m" if _macron_counter["i"] in MACRON_M_OVERRIDE else "n"


# ---------------------------------------------------------------------------
# Illegible-text <gap> reconstruction. Keyed by 0-indexed document order of
# non-duplicate <gap> elements (dedication's 3 gaps come first, then the
# treatise's 36). Resolved by context: biblical citations, known Latin
# legal/canon-law maxims, and surrounding English gloss; the eight that
# context could not settle -- the wholly lost marginal notes and the
# Greek/Hebrew ones -- were read off the 1609 folio instead. All 39 are now
# filled; a gap not listed here would fall back to the original
# bracket/bullet placeholder.
# The 1609 folio (_The Workes ... of M. W. Perkins_, vol. 3, sig. Rrrr ff.,
# archive.org bim_early-english-books-1475-1640_the-workes-of-that-famou_
# perkins-william_1609_3) reprints this whole text from the same setting of
# copy with the margins reset and legible; where a note is cited below as
# "folio", it was read off that scan. See CLAUDE.md, "A second witness".
GAP_FIXES = {
    0: "Aristot. Politic. 1.",   # folio leaf n1021 margin: "Ariſtot.Poli-|tic.1."
    1: "Xenoph. in Oeconom.",    # folio, same margin, next note down
    2: "\u1f00\u03c0\u03bf\u03b9\u03ba\u03af\u03b6\u03b5\u03b9",
                                  # apoikizei, "sends out a colony" -- folio
                                  # leaf n1021, glossing "remoueth some of them
                                  # to other places of abode"
    3: "eu",              # pray [eu]ery where (1 Tim. 2:8) -- matches this
                           # document's consistent "eu" spelling of "every"
    4: "w",               # without [w]rath or doubting
    5: "st",              # cu[st]ome
    6: "ti",              # in their [ti]mes
    7: "t",               # that [t]hey keepe
    8: "t",               # righ[t]eousnesse
    9: "G",               # [G]en. 18. 19
    10: "\u03c0\u03c1\u03bf\u03c3\u03ba\u03bf\u03bb\u03bb\u03b7\u03b8\u03ae\u03c3\u03b5\u03c4\u03b1\u03b9",
                           # proskollethesetai (Eph. 5. 31 "shall cleaue vnto
                           # his wife") -- folio leaf n1029 margin
    11: "i",              # it [i]s, by the expresse commandment
    12: "e",              # s[e]mel (Diu deliberandum quod semel statuendum)
    13: "t",              # sta[t]uendum
    14: "b",              # ver[b]is (In verbis de praesenti)
    15: "praesenti",      # de [praesenti]
    16: "i",              # de [i]ure (glossed "in regard of right")
    17: "u",              # lawf[u]ll
    18: "\u05e9\u05b0\u05c1\u05d0\u05b5\u05e8 \u05d1\u05b0\u05bc\u05e9\u05c2\u05b8\u05e8\u05d5\u05b9",
                           # she'er besaro, Leuit. 18. 6 "the kindred of his
                           # flesh" -- the folio (leaf n1031) sets this note as
                           # the transliteration "Ebr. Sheer Besaro."
    19: "5",              # lib. 1[5]. ca. 16 -- confirmed against the folio
                           # (leaf n1033: "De ciuit. Dei. lib. 15. cap. 16.")
    20: "a",              # in ste[a]d
    21: "o",              # blo[o]d
    22: "o",              # Epist[o]l.
    23: "8. epist.",      # Ambrose to Paternus -- folio leaf n1034 margin:
                           # "Epiſtol.lib.|8.epiſt.66."
    24: "e",              # cousin-g[e]rman
    25: "it",             # [it] forbiddeth matching
    26: "en",             # childr[en]
    27: "e",              # th[e] mother
    28: "i",              # Mar[i]e
    29: "i",              # nuptias in[i]re (inire -- "to enter into marriage")
    30: "g",              # coniu[g]is
    31: "r",              # forme[r]ly made
    32: "nta",            # mai[nta]ining
    33: "6",              # cap. 1[6] -- folio leaf n1045: "Lib.de Fide|&
                           # oper.c.16." (Augustine, De fide et operibus)
    34: "r",              # ma[r]iage vndertaken -- single r, matching this
                           # document's consistent old spelling of "mariage"
    35: "L. Consensu. C. de diuortijs.",
                           # Cod. Iust. 5. 17 -- the civil law forbidding a
                           # husband to strike his wife; folio leaf n1050
    36: "su",             # ages [su]cceeding
    37: "r",              # seue[r]itie
    38: "8",              # Mat. 1[8] (Matthew 18, on rebuking one's brother)
}
_gap_counter = {"i": -1}


def next_gap_text(default_desc):
    _gap_counter["i"] += 1
    return GAP_FIXES.get(_gap_counter["i"], default_desc)


# ---------------------------------------------------------------------------
# Marginal-note repairs. An end-of-line hyphen in the source joins two halves
# of a word (see linearize()), but where the compositor abbreviated the first
# half with a suspension mark the transcription did not record, that join
# produces a non-word. Keyed by the rendered (post-join) note text; each entry
# is a citation checked against the work being cited, not a guess.
NOTE_TEXT_FIXES = {
    # Beza, Tractatio de repudiis et divortiis. The section heading is
    # "de sponsalibus absque consensu PARENTUM factis" -- the source has
    # "par<EOLhyphen/>factis", losing the abbreviated "-entum".
    "consensu parfactis": "consensu parentum factis",
}


def apply_note_text_fixes(text):
    for wrong, right in NOTE_TEXT_FIXES.items():
        text = text.replace(wrong, right)
    return text


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

SENTENCE_END_RE = re.compile(r"[.!?]\s*$")
WORD_TOKEN_RE = re.compile(r"[A-Za-z']+|[^A-Za-z']+")


class ProseState:
    def __init__(self):
        self.sentence_start = True


def modernize_prose_text(text, state):
    out = []
    for m in WORD_TOKEN_RE.finditer(text):
        tok = m.group(0)
        if not tok:
            continue
        if tok[0].isalpha():
            if tok.upper().startswith("ZZ"):
                out.append(tok)
                continue  # structural marker -- doesn't affect sentence state
            lower = tok.lower()
            if lower in GRAMMAR_EXCEPTIONS:
                new_word = tok
            else:
                modern_lower = modernize_word_lower(lower)
                if state.sentence_start:
                    new_word = modern_lower[:1].upper() + modern_lower[1:]
                elif tok[:1].isupper() and modern_lower in LOWERCASE_COMMON_NOUNS:
                    new_word = modern_lower
                else:
                    new_word = apply_case_pattern(tok, modern_lower)
            out.append(new_word)
            state.sentence_start = False
        else:
            out.append(tok)
            if SENTENCE_END_RE.search(tok):
                state.sentence_start = True
    return "".join(out)


def modernize_plain_word_by_word(text):
    out = []
    for m in WORD_TOKEN_RE.finditer(text):
        tok = m.group(0)
        if tok and tok[0].isalpha():
            if tok.upper().startswith("ZZ"):
                out.append(tok)
                continue
            lower = tok.lower()
            if lower in GRAMMAR_EXCEPTIONS:
                out.append(tok)
            else:
                modern_lower = modernize_word_lower(lower)
                out.append(apply_case_pattern(tok, modern_lower))
        else:
            out.append(tok)
    return "".join(out)


def _leading_text_is_joinable_whitespace(el):
    """True if el.text is pure whitespace containing a newline (i.e. just
    XML pretty-print indentation) AND el's first child is a glyph-splice
    <g> or a resolved <gap> -- meaning this "whitespace" isn't a real
    space, it's noise before a mid-word continuation."""
    if not el.text or el.text.strip() or "\n" not in el.text:
        return False
    if len(el) == 0:
        return False
    return local(el[0].tag) in ("g", "gap")


def linearize(el, footnotes):
    parts = []
    if el.text and not _leading_text_is_joinable_whitespace(el):
        parts.append(esc(collapse(el.text)))
    for child in el:
        tag = local(child.tag)
        if tag == "hi":
            inner = linearize(child, footnotes)
            if child.get("rend") == "sup":
                parts.append(f"\x00ZZSUSTARTZZ\x00{inner}\x00ZZSUENDZZ\x00")
            else:
                parts.append(f"\x00ZZEMSTARTZZ\x00{inner}\x00ZZEMENDZZ\x00")
        elif tag == "g":
            ref = child.get("ref", "")
            if ref == "char:cmbAbbrStroke":
                parts.append(next_macron_letter())
            elif child.text:
                parts.append(child.text)
        elif tag == "note":
            note_body = apply_note_text_fixes(render_footnote(child).strip())
            if note_body:
                idx = len(footnotes)
                footnotes.append(note_body)
                letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                token = "ZZFN" + letters[idx % 26] + letters[(idx // 26) % 26] + "ZZ"
                parts.append(token)
        elif tag == "gap":
            if child.get("reason") != "duplicate":
                desc = child.find(".//t:desc", namespaces=NS)
                default = desc.text if desc is not None and desc.text else ""
                fixed = next_gap_text(default)
                if fixed:
                    parts.append(esc(fixed))
        elif tag == "expan":
            ex = child.find(".//t:ex", namespaces=NS)
            if ex is not None and ex.text:
                parts.append(esc(ex.text))
        elif tag in ("seg", "bibl", "q", "abbr", "corr", "sic", "unclear", "term"):
            parts.append(linearize(child, footnotes))
        elif tag in ("pb", "fw", "milestone"):
            pass
        else:
            parts.append(linearize(child, footnotes))
        if child.tail:
            # Whitespace-only tail that's purely XML pretty-print
            # indentation (contains a newline) adjacent to a glyph-splice
            # <g> tag or a resolved mid-word <gap> is not a real space in
            # the source -- collapsing it to " " would wrongly split a
            # word (e.g. "co" + macron + <newline-indent> + "sent" ->
            # "consent", not "con sent"; same for "cu" + <EOLhyphen> +
            # <newline-indent> + gap-fix "st" + "ome" -> "custome").
            next_el = child.getnext()
            joinable = ("g", "gap")
            if (tag in joinable and next_el is not None and local(next_el.tag) in joinable
                    and not child.tail.strip() and "\n" in child.tail):
                pass
            else:
                parts.append(esc(collapse(child.tail)))
    return "".join(parts)


def render_footnote(note_el):
    parts = []
    if note_el.text and not _leading_text_is_joinable_whitespace(note_el):
        parts.append(esc(collapse(note_el.text)))
    for child in note_el:
        tag = local(child.tag)
        if tag == "hi":
            inner = render_footnote(child)
            parts.append(f"#super[{inner}]" if child.get("rend") == "sup" else f"#emph[{inner}]")
        elif tag == "g":
            if child.get("ref") == "char:cmbAbbrStroke":
                next_macron_letter()
                parts.append(child.text or "")
            elif child.text:
                parts.append(child.text)
        elif tag == "gap":
            if child.get("reason") != "duplicate":
                desc = child.find(".//t:desc", namespaces=NS)
                default = desc.text if desc is not None and desc.text else ""
                fixed = next_gap_text(default)
                if fixed:
                    parts.append(esc(fixed))
        elif tag == "expan":
            ex = child.find(".//t:ex", namespaces=NS)
            if ex is not None and ex.text:
                parts.append(esc(ex.text))
        else:
            parts.append(render_footnote(child))
        if child.tail:
            next_el = child.getnext()
            joinable = ("g", "gap")
            if (tag in joinable and next_el is not None and local(next_el.tag) in joinable
                    and not child.tail.strip() and "\n" in child.tail):
                pass
            else:
                parts.append(esc(collapse(child.tail)))
    return "".join(parts)


# A Typst content block re-parses its own body as markup, so a footnote whose
# text opens with "1. " (very common here -- "1. Cor. 7.") or with "- " becomes
# a list *inside* the note, swallowing the notes that follow it. Escape the
# marker so it stays literal. Same hazard for the text of a list <item>.
def escape_leading_marker(text):
    # "1. Cor." / "2) x"  -> escape the punctuation after the number
    m = re.match(r"(\s*\d+)([.)])(\s)", text)
    if m:
        return text[:m.end(1)] + "\\" + text[m.start(2):]
    # "- x" / "+ x" / "/ x" -> escape the marker itself
    m = re.match(r"(\s*)([-+/])(\s)", text)
    if m:
        return text[:m.end(1)] + "\\" + text[m.start(2):]
    return text

def splice_footnotes(text, footnotes):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def repl(m):
        token = m.group(0).upper()
        c1, c2 = token[4], token[5]
        idx = letters.index(c1) + letters.index(c2) * 26
        return f"#footnote[{escape_leading_marker(footnotes[idx])}]"

    return re.sub(r"ZZFN[A-Za-z]{2}ZZ", repl, text, flags=re.IGNORECASE)


def fix_decorinit_in_text(text):
    m = re.match(r"^([A-Z])([A-Z])([a-z])", text)
    if m:
        return text[0] + text[1].lower() + text[2:]
    return text


def finalize_markup(text):
    text = text.replace("\x00ZZEMSTARTZZ\x00", "#emph[")
    text = text.replace("\x00ZZEMENDZZ\x00", "]")
    text = text.replace("\x00ZZSUSTARTZZ\x00", "#super[")
    text = text.replace("\x00ZZSUENDZZ\x00", "]")
    text = text.replace("\x00", "")  # safety net for any unpaired stray marker
    return text


def render_paragraph_like(el, mode="prose"):
    footnotes = []
    raw = linearize(el, footnotes).strip()
    raw = re.sub(r" +", " ", raw)
    if mode == "prose":
        raw = fix_decorinit_in_text(raw)
        state = ProseState()
        modernized = modernize_prose_text(raw, state)
    else:
        modernized = modernize_plain_word_by_word(raw)
    spliced = splice_footnotes(modernized, footnotes)
    return finalize_markup(spliced)


def render_list(list_el, depth=0):
    lines = []
    indent = "  " * depth
    head = list_el.find("t:head", namespaces=NS)
    if head is not None:
        text = render_paragraph_like(head, "prose").strip()
        if text:
            lines.append(f"{indent}#strong[{text}]")
            lines.append("")
    for item in list_el.findall("t:item", namespaces=NS):
        sub_lists = item.findall("t:list", namespaces=NS)
        item_copy = etree.Element(item.tag)
        item_copy.text = item.text
        for child in item:
            if local(child.tag) != "list":
                item_copy.append(etree.fromstring(etree.tostring(child)))
        text = escape_leading_marker(render_paragraph_like(item_copy, "prose").strip())
        if text:
            lines.append(f"{indent}- {text}")
        for sub in sub_lists:
            lines.extend(render_list(sub, depth + 1))
    return lines


def render_closer(closer_el):
    signed = closer_el.find("t:signed", namespaces=NS)
    out = []
    if signed is not None:
        txt = render_paragraph_like(signed, "prose").strip()
        out.append("#align(right)[" + txt + "]")
        out.append("")
    return out


def render_block(el):
    tag = local(el.tag)
    if tag == "p":
        txt = render_paragraph_like(el, "prose")
        return [txt, ""] if txt else []
    if tag == "list":
        return render_list(el) + [""]
    if tag == "closer":
        return render_closer(el)
    if tag in ("pb", "head", "fw", "trailer"):
        return []
    txt = render_paragraph_like(el, "prose")
    return [txt, ""] if txt else []


def render_heads(div_el, level):
    out = []
    heads = div_el.findall("t:head", namespaces=NS)
    for i, head in enumerate(heads):
        text = render_paragraph_like(head, "heading").strip()
        if not text:
            continue
        if i == 0:
            out.append(f"{'=' * level} {text}")
        else:
            out.append(f"#emph[{text}]")
            out.append("")
    if len(heads) == 1:
        out.append("")
    return out


def render_div(div_el, level):
    out = []
    out.extend(render_heads(div_el, level))
    for child in div_el:
        tag = local(child.tag)
        if tag == "head":
            continue
        if tag == "div":
            out.extend(render_div(child, level + 1))
        else:
            out.extend(render_block(child))
    return out


PREAMBLE = '''#set page(width: 6in, height: 9in, margin: 1in)
#set par(justify: true)
#set text(font: "New Computer Modern", size: 11pt)

'''


def render_top_div(div_el):
    lines = [PREAMBLE.rstrip("\n"), ""]
    lines.extend(render_div(div_el, 1))
    return "\n".join(lines).rstrip() + "\n"


def main():
    tree = etree.parse("A09377.xml")
    root = tree.getroot()
    dedication = root.find(".//t:div[@type='dedication']", namespaces=NS)
    treatise = root.find(".//t:div[@type='treatise']", namespaces=NS)

    ded_out = render_top_div(dedication)
    treat_out = render_top_div(treatise)

    with open("dedication_modern.typ", "w", encoding="utf-8") as f:
        f.write(ded_out)
    with open("treatise_modern.typ", "w", encoding="utf-8") as f:
        f.write(treat_out)

    print("Dedication (modern) length:", len(ded_out))
    print("Treatise (modern) length:", len(treat_out))
    print("Macron occurrences processed:", _macron_counter["i"] + 1)


if __name__ == "__main__":
    main()
