"""Negated Classic sentences whose best-matching Modern sentence (and its neighbours) carries no
negation: the likely lost negations. python3 audit-negflag.py PAIRS.jsonl"""
import json, re, sys
NEG = re.compile(r"\b(not|no|never|nor|neither|none|nothing|nobody|without|unless|cannot|scarce|scarcely|hardly|lest|nay|un\w+|in\w+able)\b|n['’]t\b", re.I)
sent = lambda s: re.split(r"(?<=[.?!;:])\s+", re.sub(r"\s+", " ", s))
W = lambda s: set(re.findall(r"[a-z]{4,}", s.lower()))
for l in open(sys.argv[1]):
    r = json.loads(l)
    ms = sent(r["modern"])
    for s in sent(r["classic"]):
        if not re.search(r"\b(not|no|never|nor|neither|none|nothing|without|unless|cannot)\b", s, re.I): continue
        if len(W(s)) < 4: continue
        i = max(range(len(ms)), key=lambda k: len(W(ms[k]) & W(s)))
        if len(W(ms[i]) & W(s)) < 3: continue
        near = " ".join(ms[max(0, i - 1): i + 2])
        if not NEG.search(near):
            print(f"{r['file']} ¶{r['n']}\n C: {s[:260]}\n M: {ms[i][:260]}")
