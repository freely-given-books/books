"""Prove a reader read everything: python3 coverage.py PAIRS.jsonl ASSIGNMENT READER.tsv LEDGER.tsv [MINUTES]

ASSIGNMENT: an assign.py .ids file (file<TAB>n per paragraph), or a list of pairs files / chapter names.
READER.tsv: one verdict row per paragraph (file, n, ok|finding, ...).
LEDGER.tsv: the reader's clause ledger, one row per Classic sentence or clause it compared:
    file<TAB>n<TAB>classic clause (its first words, copied)<TAB>modern words carrying it<TAB>= or ≠
Passes when every paragraph has a verdict AND ledger rows covering at least 80% of its Classic sentences, each
row's Classic words found in that paragraph (so the rows cannot be made up).

Why a ledger and not a clock (2026-11-17, the first four re-checks): a timing gate of 10 minutes per 10,000
words failed honest readers on every run (opus and sonnet read 2,000-3,500 words a minute) and passed small
runs only because of start-up overhead; readers asked to keep a clause ledger read clause by clause, and the
ledger is checkable. MINUTES, if given, is reported only."""
import json, re, sys
from collections import Counter

pairs = [json.loads(l) for l in open(sys.argv[1])]
lines = [w.rstrip("\n") for w in open(sys.argv[2]) if w.strip()]
if all("\t" in w for w in lines):
    rows = {(f, int(n)) for f, n in (w.split("\t")[:2] for w in lines)}
else:
    want = {re.sub(r"^pairs-|\.md$", "", w.strip()) for w in lines}
    rows = {(r["file"], r["n"]) for r in pairs if r["file"] in want}
by = {(r["file"], r["n"]): r for r in pairs}
words = sum(len(by[k]["classic"].split()) for k in rows)
key = lambda f, n: (f.removesuffix(".typ"), int(str(n).lstrip("¶")))
norm = lambda s: re.sub(r"[^a-z0-9 ]", "", re.sub(r"#[a-z]+(\.[a-z]+)*|[\[\]]", " ", s.lower()))

seen = set()
for l in open(sys.argv[3]):
    f = l.rstrip("\n").split("\t")
    if len(f) >= 2 and f[1].lstrip("¶").isdigit(): seen.add(key(f[0], f[1]))

led, bad = Counter(), 0
for l in open(sys.argv[4]):
    f = l.rstrip("\n").split("\t")
    if len(f) < 4 or not f[1].lstrip("¶").isdigit(): continue
    k = key(f[0], f[1])
    if k not in by: continue
    first = " ".join(norm(f[2]).split()[:3])
    if first and first in " ".join(norm(by[k]["classic"]).split()): led[k] += 1
    else: bad += 1

short = []
for k in sorted(rows):
    text = re.sub(r"\b(\d+)\s*([ls]d?)\.", r"\1\2", by[k]["classic"])  # money: 20 l. 5 s.
    s = len([x for x in re.split(r"(?<=[.?!])[”’)\]]?\s+(?=[“‘(]?[A-Z])", text) if len(x.split()) > 2]) or 1
    if led[k] < max(1, round(0.8 * s)): short.append((k, led[k], s))
miss = sorted(rows - seen)
print(f"{len(rows)} paragraphs, {words} Classic words; verdicts {len(rows & seen)}, missing {len(miss)}; "
      f"ledger short in {len(short)}; ledger rows not found in their paragraph: {bad}")
for (f, n) in miss[:100]: print(f"  no verdict {f} ¶{n}")
for (f, n), a, s in short[:100]: print(f"  ledger {f} ¶{n}: {a} rows for {s} sentences")
if len(sys.argv) > 5: print(f"{float(sys.argv[5]) / max(words / 10000, 1e-9):.1f} minutes per 10k words (for the record)")
sys.exit(0 if not miss and not short and bad <= len(rows) // 20 else 1)
