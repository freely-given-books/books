#!/usr/bin/env python3
"""
modernize.py
============

The prose layer of the modernized render: sentence-aware capitalization on
top of the word-level spelling rules in spelling.py.

tcp_to_typst.py hands this module one whole linearized paragraph at a time --
already de-hyphenated, with gaps filled, and with footnotes and inline markup
held as ZZ... placeholder tokens.  Everything here works on that flat string,
which is the whole point: a word split across markup in the source has already
been put back together, so word rules see real words.

What changes:
  - old spelling -> modern spelling, word by word (spelling.py)
  - a short, explicit list of unambiguous common nouns is lowercased when not
    sentence-initial, undoing the Early Modern habit of capitalizing them

What deliberately does not change:
  - which word is used.  "hath", "doth", "thou", "ye", "shalt" are different
    grammatical forms, not alternate spellings, and stay as they are
  - marginal-note content, which never reaches this module: notes are almost
    entirely Latin and bibliographic abbreviation, and the risk of mangling a
    citation outweighs the benefit
  - proper names, titles, and religious terms (God, Lord, Church, King,
    Bishop, Scripture...).  Guessing word-by-word which capital is a title and
    which is Early Modern noun-capitalization goes wrong more often than it
    goes right, so only the explicit list below is touched
"""

import re

from spelling import (AMBIGUOUS_NAMES, GRAMMAR_EXCEPTIONS, _SPELL,
                      apply_case_pattern, modernize_word_lower)

# Common nouns this book capitalizes by convention rather than by meaning.
# Only words that are never a title or a proper name in this text belong
# here -- "Church", "Word", "Sabbath", "Minister" and the like are left
# capitalized because in a Puritan treatise the capital is often meant.
LOWERCASE_COMMON_NOUNS = {
    "husband", "husbands", "wife", "wives", "wiues", "child", "children",
    "childe", "parent", "parents", "father", "fathers", "mother", "mothers",
    "son", "sonne", "sonnes", "sons", "daughter", "daughters",
    "servant", "servants", "seruant", "seruants", "master", "masters",
    "mistress", "mistresse", "mistresses", "family", "familie", "families",
    "house", "household", "households", "houshold", "marriage", "mariage",
    "marriages", "contract", "contracts", "duty", "dutie", "duties",
    "subjection", "subiection", "authority", "authoritie", "obedience",
    "reverence", "reuerence", "honour", "honor", "love", "loue",
    "nature", "reason", "argument", "arguments", "rule", "rules",
    "case", "cases", "example", "examples", "note", "notes",
    "estate", "state", "states", "person", "persons", "place", "places",
    "point", "points", "thing", "things", "time", "times", "way", "ways",
    "wayes", "word", "words", "work", "works", "worke", "workes",
    "man", "men", "woman", "women", "brother", "brethren", "sister",
    "sisters", "widow", "widdow", "widows", "widdowes", "bride",
    "bridegroom", "bridegroome", "kindred", "sex", "society", "societie",
    "commonwealth", "common", "general", "generall", "particular", "proper",
}

SENTENCE_END_RE = re.compile(r"[.!?]\s*$")
WORD_TOKEN_RE = re.compile(r"[A-Za-z']+|[^A-Za-z']+")

# ---------------------------------------------------------------------------
# Latin
# ---------------------------------------------------------------------------
# Gouge quotes the Fathers and the civilians constantly, in the margins and in
# the running text.  The spelling rules must not touch that: the silent-e and
# -es/-s rules are exactly wrong for Latin, and they fire, because the modern
# English word they produce is real -- "lege" becomes "leg", "ille" becomes
# "ill", "disces" becomes "discs", "posse" becomes "poss".  Blocklisting the
# vocabulary does not scale; there is a whole patristic library in these
# margins.
#
# Instead, decide per RUN.  A run is a stretch of text between two pieces of
# inline markup, which in this source is a good proxy for a quotation, since
# Latin is nearly always set in italic.  If most of its words are not English
# even after modernization, the run is Latin and is passed through untouched.
# Short runs are never judged: "Ibid." and "Aug. Epist. 121." look like Latin
# by any measure and there is nothing in them to modernize anyway.
LATIN_MIN_WORDS = 4
RUN_SPLIT_RE = re.compile(r"\x00")


def _is_english(word):
    lower = word.lower()
    return lower in _SPELL or modernize_word_lower(lower) in _SPELL


def _looks_latin(run):
    words = WORD_RE_ALPHA.findall(run)
    if len(words) < LATIN_MIN_WORDS:
        return False
    return sum(_is_english(w) for w in words) * 2 < len(words)


WORD_RE_ALPHA = re.compile(r"[A-Za-z']+")


def latin_spans(text):
    """Character ranges of `text` that should be left exactly as they are."""
    spans, pos = [], 0
    for run in RUN_SPLIT_RE.split(text):
        end = pos + len(run)
        if run.strip() and not run.upper().startswith("ZZ") and _looks_latin(run):
            spans.append((pos, end))
        pos = end + 1          # the \x00 that split() consumed
    return spans


def _in_spans(spans, i):
    return any(a <= i < b for a, b in spans)


class ProseState:
    """Whether the next word starts a sentence.  Carried across tokens so a
    word can be capitalized because of where it sits, not just what it is."""

    def __init__(self):
        self.sentence_start = True


def _is_marker(tok):
    # Placeholder tokens (ZZEMSTARTZZ, ZZFN0007ZZ, ZZGAP0007ZZ) must survive
    # untouched and must not count as words -- capitalizing "ZZEMSTARTZZ" or
    # letting it end a sentence would corrupt the markup spliced back in.
    return tok.upper().startswith("ZZ")


def modernize_prose_text(text, state):
    """Running prose: modernize spelling, capitalize sentence-initially, and
    lowercase the listed common nouns elsewhere."""
    out = []
    spans = latin_spans(text)
    for m in WORD_TOKEN_RE.finditer(text):
        tok = m.group(0)
        if not tok:
            continue
        if not tok[0].isalpha():
            out.append(tok)
            if SENTENCE_END_RE.search(tok):
                state.sentence_start = True
            continue
        if _is_marker(tok):
            # Markup, not a word: it must not clear sentence_start, or a
            # paragraph or table cell opening with #emph[...] loses its
            # initial capital.
            out.append(tok)
            continue
        if _in_spans(spans, m.start()):
            out.append(tok)
            state.sentence_start = False
            continue
        lower = tok.lower()
        if (tok[:1].isupper() and not state.sentence_start
                and lower in AMBIGUOUS_NAMES):
            # A capital mid-sentence is the proper name, not the verb that
            # happens to share its spelling.
            new_word = AMBIGUOUS_NAMES[lower]
        elif lower in GRAMMAR_EXCEPTIONS:
            new_word = tok
        else:
            modern = modernize_word_lower(lower)
            if state.sentence_start:
                # Capitalize, but keep an existing capital pattern: forcing
                # Titlecase here turns "III." into "Iii." and "GOD" into "God".
                cased = apply_case_pattern(tok, modern)
                new_word = (cased if cased[:1].isupper()
                            else cased[:1].upper() + cased[1:])
            elif tok[:1].isupper() and modern in LOWERCASE_COMMON_NOUNS:
                new_word = modern
            else:
                new_word = apply_case_pattern(tok, modern)
        out.append(new_word)
        state.sentence_start = False
    return "".join(out)


def modernize_plain(text):
    """Headings, table cells and scripture references: modernize spelling but
    leave the capitalization pattern exactly as the source set it."""
    out = []
    spans = latin_spans(text)
    for m in WORD_TOKEN_RE.finditer(text):
        tok = m.group(0)
        if (tok and tok[0].isalpha() and not _is_marker(tok)
                and not _in_spans(spans, m.start())):
            lower = tok.lower()
            if lower in GRAMMAR_EXCEPTIONS:
                out.append(tok)
            else:
                out.append(apply_case_pattern(tok, modernize_word_lower(lower)))
        else:
            out.append(tok)
    return "".join(out)
