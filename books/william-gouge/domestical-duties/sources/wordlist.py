#!/usr/bin/env python3
"""
wordlist.py
===========

Tooling for tuning spelling.py to a new book.  Reads the ORIGINAL-spelling
render, throws away Typst markup and footnote bodies (notes are not
modernized, so their Latin must not drive the dictionary), and reports:

    --unchanged   words the rules leave alone that a modern spellchecker does
                  not recognise -- i.e. old spellings still to be handled.
                  This is the list you work down when building MANUAL.
    --changed     what the rules currently do, so a bad rule shows up as a
                  column of nonsense rather than hiding in 300,000 words.
    --check WORD  what the pipeline does to one word, and why.

Expected noise in --unchanged, none of which is a bug:
  * archaic verb forms whose root is already modern (giueth -> giveth): the
    -eth/-est ending is kept on purpose, so the spellchecker rejects the word
  * proper names (Iaakob, Bathsheba, Elkanah) and Latin from quoted maxims
  * closed-class archaisms listed in GRAMMAR_EXCEPTIONS

Usage:
    python3 wordlist.py out/*.typ --unchanged | head -200
    python3 wordlist.py out/*.typ --changed | grep -v '^ok'
    python3 wordlist.py out/*.typ --check seruant
"""

import argparse
import re
import sys
from collections import Counter

from spelling import GRAMMAR_EXCEPTIONS, _SPELL, modernize_word_lower

WORD_RE = re.compile(r"[A-Za-z']+")


def strip_calls(text, name):
    """Remove `#name[...]` and its body, honouring nested brackets."""
    out = []
    i = 0
    needle = "#" + name + "["
    while True:
        j = text.find(needle, i)
        if j < 0:
            out.append(text[i:])
            return "".join(out)
        out.append(text[i:j])
        depth, k = 1, j + len(needle)
        while k < len(text) and depth:
            if text[k] == "[":
                depth += 1
            elif text[k] == "]":
                depth -= 1
            k += 1
        i = k


def collect_calls(text, name):
    """The inverse of strip_calls: return just the bodies of `#name[...]`."""
    out = []
    needle = "#" + name + "["
    i = 0
    while True:
        j = text.find(needle, i)
        if j < 0:
            return "\n".join(out)
        depth, k = 1, j + len(needle)
        while k < len(text) and depth:
            if text[k] == "[":
                depth += 1
            elif text[k] == "]":
                depth -= 1
            k += 1
        out.append(text[j + len(needle):k - 1])
        i = k


def body_text(paths, notes_only=False):
    chunks = []
    for path in paths:
        text = open(path, encoding="utf-8").read()
        text = (collect_calls(text, "footnote") if notes_only
                else strip_calls(text, "footnote"))
        text = re.sub(r"^#(set|show|import|include).*$", "", text, flags=re.M)
        text = re.sub(r"#(emph|super|strong|text|align|block|v|table|quote)\b", " ", text)
        text = re.sub(r"\\(.)", r"\1", text)
        chunks.append(text)
    return "\n".join(chunks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--unchanged", action="store_true")
    ap.add_argument("--changed", action="store_true")
    ap.add_argument("--check")
    ap.add_argument("--min", type=int, default=1, help="minimum frequency to report")
    ap.add_argument("--notes", action="store_true",
                    help="Look at marginal-note bodies instead of the running text")
    args = ap.parse_args()

    if args.check:
        w = args.check.lower()
        print(f"{args.check!r}: grammar-exception={w in GRAMMAR_EXCEPTIONS} "
              f"known-modern={w in _SPELL} -> {modernize_word_lower(w)!r}")
        return

    counts = Counter(w.lower()
                     for w in WORD_RE.findall(body_text(args.files, args.notes)))
    print(f"{sum(counts.values())} words, {len(counts)} distinct", file=sys.stderr)

    rows = []
    for word, n in counts.items():
        if n < args.min or word in GRAMMAR_EXCEPTIONS:
            continue
        modern = modernize_word_lower(word)
        if args.changed and modern != word:
            rows.append((n, f"{word} -> {modern}"))
        elif args.unchanged and modern == word and word not in _SPELL:
            rows.append((n, word))
    for n, row in sorted(rows, reverse=True):
        print(f"{n:6d}  {row}")


if __name__ == "__main__":
    main()
