"""Modern (or --classic) paragraph text around a phrase: PAIRS=pairs.jsonl audit-grep.py CHAPTER PATTERN [WIDTH]"""
import json, re, sys
args = [a for a in sys.argv[1:] if a != "--classic"]
side = "classic" if "--classic" in sys.argv else "modern"
ch, pat = args[0], args[1]; w = int(args[2]) if len(args) > 2 else 120
for l in open(__import__("os").environ["PAIRS"]):
    r = json.loads(l)
    if r["file"] != ch: continue
    for m in re.finditer(pat, r[side], re.I):
        print(f"{ch} ¶{r['n']}: …{r[side][max(0,m.start()-w):m.end()+w]}…")
