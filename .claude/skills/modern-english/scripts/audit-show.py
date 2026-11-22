"""Show a term's Classic contexts and the closest Modern sentence: audit-show.py PAIRS TERMS.tsv TERM..."""
import json, re, sys
rows = {(r["file"], r["n"]): r for r in map(json.loads, open(sys.argv[1]))}
want = set(sys.argv[3:])
words = lambda s: set(re.findall(r"[a-z]{4,}", s.lower()))
seen = set()
for line in list(open(sys.argv[2]))[1:]:
    f, n, t, a, b = line.rstrip("\n").split("\t")
    if want and t not in want: continue
    r = rows[(f, int(n))]
    msents = re.split(r"(?<=[.?!;:])\s+", r["modern"])
    for m in re.finditer(r"\b" + t.replace(".", r"\W+"), r["classic"], re.I):
        ctx = r["classic"][max(0, m.start()-120):m.end()+80].replace("\n", " ")
        if (f, n, ctx[:40]) in seen: continue
        seen.add((f, n, ctx[:40]))
        best = max(msents, key=lambda s: len(words(s) & words(ctx)))
        print(f"=== {f} ¶{n} [{t}]\n  C: …{ctx}…\n  M: {best[:330]}")
