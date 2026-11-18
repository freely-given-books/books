"""For given paragraphs, each Classic sentence matching PATTERN with its best Modern match."""
import json, re, sys
rows = {(r["file"], r["n"]): r for r in map(json.loads, open(sys.argv[1]))}
pat = re.compile(sys.argv[2], re.I)
sent = lambda s: re.split(r"(?<=[.?!;:])\s+", re.sub(r"\s+", " ", s))
W = lambda s: set(re.findall(r"[a-z]{4,}", s.lower()))
for spec in sys.argv[3:]:
    f, n = spec.split(":"); r = rows[(f if f.startswith(("chap","pref")) else f"chapter-{int(f):02d}", int(n))]
    ms = sent(r["modern"])
    for s in sent(r["classic"]):
        if pat.search(s):
            best = max(ms, key=lambda m: len(W(m) & W(s)))
            print(f"--- {spec}\n C: {s[:240]}\n M: {best[:240]}")
