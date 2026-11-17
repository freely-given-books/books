"""Prove a reader read everything: each reader returns one verdict line per paragraph of its assignment
(file, n, verdict ok|finding, ...); this lists paragraphs with no verdict, and timing if given.
python3 coverage.py PAIRS.jsonl ASSIGNMENT READER.tsv [MINUTES]
ASSIGNMENT: an assign.py .ids file (file<TAB>n per paragraph), or a list of pairs files / chapter names. MINUTES: wall time of the run;
under ~10 minutes per 10,000 Classic words is rejected as skimming (2026-11-17: assessment readers took 4-6
minutes for 20-27k words while each brief said "do not sample")."""
import json, sys, re
pairs = [json.loads(l) for l in open(sys.argv[1])]
lines = [w.rstrip("\n") for w in open(sys.argv[2]) if w.strip()]
if all("\t" in w for w in lines):
    rows = {(f, int(n)) for f, n in (w.split("\t")[:2] for w in lines)}
else:
    want = {re.sub(r"^pairs-|\.md$", "", w.strip()) for w in lines}
    rows = {(r["file"], r["n"]) for r in pairs if r["file"] in want}
words = sum(len(r["classic"].split()) for r in pairs if (r["file"], r["n"]) in rows)
seen = set()
for l in open(sys.argv[3]):
    f = l.rstrip("\n").split("\t")
    if len(f) >= 2 and f[1].lstrip("¶").isdigit(): seen.add((f[0].removesuffix(".typ"), int(f[1].lstrip("¶"))))
miss = sorted(rows - seen)
print(f"{len(rows)} paragraphs, {words} Classic words; verdicts for {len(rows & seen)}; missing {len(miss)}")
for f, n in miss[:200]: print(f"  missing {f} ¶{n}")
ok = not miss
if len(sys.argv) > 4:
    rate = float(sys.argv[4]) / (words / 10000)
    print(f"{rate:.1f} minutes per 10k words" + ("  TOO FAST: redo" if rate < 10 else ""))
    ok = ok and rate >= 10
sys.exit(0 if ok else 1)
