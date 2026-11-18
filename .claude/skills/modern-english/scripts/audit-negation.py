"""Negation/direction check: per paragraph pair, counts of polarity and limiting words that differ.
python3 audit-negation.py PAIRS.jsonl
NEG: any difference. LIM: a difference of 2+, or of 1 in a strong limiter (only, alone, all, nothing, none,
always, never, no more, every): one lost "only" can reverse an argument (2026-11-17)."""
import json, re, sys
from collections import Counter
NEG = r"not|no|never|nor|neither|none|nothing|nobody|without|unless|cannot|can't|don't|doesn't|isn't|won't|hardly|scarce|scarcely"
LIM = r"only|alone|all|always|every|some|any|more|less|most|least|until|till|except|but"
def counts(s, pat):
    s = re.sub(r"#[a-z]+(\.[a-z]+)*|\(\w+ \d+:[\d–,\s;]+\)", " ", s.lower())
    s = re.sub(r"n['’]t\b", " not", s)
    return Counter(re.findall(r"\b(" + pat + r")\b", s))
out = []
for l in open(sys.argv[1]):
    r = json.loads(l)
    for kind, pat in (("NEG", NEG), ("LIM", LIM)):
        a, b = counts(r["classic"], pat), counts(r["modern"], pat)
        sa, sb = sum(a.values()), sum(b.values())
        strong = {"only", "alone", "all", "always", "every"} & set((a - b) | (b - a))
        if kind == "NEG" and sa != sb or kind == "LIM" and (abs(sa - sb) >= 2 or strong):
            out.append((kind, r["file"], r["n"], sa, sb, dict(a - b), dict(b - a)))
for o in out:
    print(*o, sep="\t")
print(len(out), "pairs to read", file=sys.stderr)
