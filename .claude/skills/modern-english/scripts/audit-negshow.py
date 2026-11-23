import json, re, sys, ast
rows = {(r["file"], r["n"]): r for r in map(json.loads, open(sys.argv[1]))}
sent = lambda s: re.split(r"(?<=[.?!;:])\s+", re.sub(r"\s+", " ", s))
for line in open(sys.argv[2]):
    kind, f, n, sa, sb, lost, gained = line.rstrip("\n").split("\t")
    if kind != sys.argv[3]: continue
    r = rows[(f, int(n))]
    print(f"=== {f} ¶{n}  lost {lost}  gained {gained}")
    for side, d in (("C", ast.literal_eval(lost)), ("M", ast.literal_eval(gained))):
        if not d: continue
        pat = re.compile(r"\b(" + "|".join(d) + r")\b|n['’]t\b", re.I)
        for s in sent(r["classic" if side == "C" else "modern"]):
            if pat.search(s): print(f"  {side}: {s[:260]}")
