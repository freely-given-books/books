#!/usr/bin/env python3
"""
sweep.py: odd things in a book's chapters/typ that a reader would trip on.

  python3 sweep.py BOOK_DIR [--early]

Reads every chapters/typ/*.typ (Typst markup lines skipped) and lists, file
by file:

  spacing      a space before , ; : ! ? or a lone ".", "“ word", "word ”"
  punctuation  ",." ".;" ",," "....." and the like
  quotes       a quotation opened with “ and closed with ’’ ; a straight " or '
               left where the book otherwise curls its quotes
  semicolon    #emph[..]; — Typst ends the call at the ";" and drops it
               (write \\;)
  apostrophe   a straight ' inside a word, in a book quoting with single
               quotes: Typst closes the open quotation there (write ’)
  doubled      a word written twice ("the the")
  glued        "word,word" or "word.Word"
  words        (--early) words in neither the spelling dictionary nor the
               early printing (source/*.tcp.xml or *.witness.xml): typos

Nothing is changed. Every hit is a candidate: read it in context, and fix in
chapters/typ only what is clearly wrong ("etc.," and "130th" are fine).
"""

import argparse
import re
import sys
from pathlib import Path

CHECKS = [
    ("spacing", r"\w \s*[,;:!?](?=\s|$)|\w \.(?=\s|$)|“ (?=\w)|(?<=\w) ”"),
    ("punctuation", r"[,;:][,;:.](?!\d)|(?<!etc)\.[,;:](?!\d)|\.{4,}"),
    ("quotes", r"“[^”‘’]{0,400}?’’"),
    ("semicolon", r"#(?:emph|strong|super|smallcaps|footnote)\[[^\]\n]*\];"),
    ("doubled", r"\b(\w+) \1\b"),
    ("glued", r"[a-z][,;:][A-Za-z]|[a-z]\.[A-Z][a-z]"),
]
FINE_DOUBLED = {"that", "had", "is", "do", "very"}


def prose(text):
    """Chapter text without lines that are only Typst markup."""
    keep = [l for l in text.split("\n")
            if not re.match(r"\s*(#set|#import|#\[|\]|//|=)", l)]
    return re.sub(r"\s+", " ", " ".join(keep))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book")
    ap.add_argument("--early", action="store_true",
                    help="also list words in neither the dictionary nor the early printing")
    a = ap.parse_args()
    book = Path(a.book)
    files = sorted((book / "chapters" / "typ").rglob("*.typ"))
    texts = {f: f.read_text(encoding="utf-8") for f in files}
    every = " ".join(texts.values())
    single = every.count("‘") + every.count("’") > every.count("“") + every.count("”")
    straight_q = every.count('"') < (every.count("“") + every.count("”")) / 10
    hits = 0

    def show(f, kind, flat, m):
        nonlocal hits
        hits += 1
        print(f"{f.relative_to(book)}\t{kind:11}\t…{flat[max(0, m.start() - 40):m.end() + 25]}…")

    early = None
    if a.early:
        try:
            from spellchecker import SpellChecker
        except ImportError:
            sys.exit("--early needs pyspellchecker (use the fgb-tei venv)")
        sp = SpellChecker()
        src = [p for p in (book / "source").glob("*.xml")
               if p.name.endswith((".tcp.xml", ".witness.xml"))]
        early = set(w.lower().replace("ſ", "s") for p in src
                    for w in re.findall(r"[A-Za-zſ]+", p.read_text(encoding="utf-8")))
    for f, text in texts.items():
        flat = prose(text)
        for kind, pat in CHECKS:
            for m in re.finditer(pat, flat):
                if kind == "doubled" and m.group(1).lower() in FINE_DOUBLED:
                    continue
                show(f, kind, flat, m)
        if straight_q:
            for m in re.finditer(r'"', flat):
                show(f, "quotes", flat, m)
        if single:
            for m in re.finditer(r"(?<=[A-Za-z])'(?=[A-Za-z])", flat):
                show(f, "apostrophe", flat, m)
        if early is not None:
            # blank out markup calls at the same length, so offsets match flat
            for m in re.finditer(r"[A-Za-z]+", re.sub(r"#\w+", lambda c: " " * len(c.group()), flat)):
                w = m.group(0).lower()
                if len(w) > 2 and w not in early and not sp.known([w]):
                    show(f, f"words {m.group(0)}", flat, m)
    print(f"{hits} candidates", file=sys.stderr)


if __name__ == "__main__":
    main()
