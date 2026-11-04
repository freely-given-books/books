# triage.json -> buckets.json: A 1688 backed by a period text (1692/1666) and the edition not;
# B the edition backed and 1688 not; C neither or both; K edition-only passages of 3+ words in 1666
import json, re
from difflib import SequenceMatcher
rows = json.load(open("triage.json"))


def spelling(r):
    a, b = r["new"].replace("\xad", ""), r["ed"]
    if " " in a.strip() or " " in b.strip() or not a or not b:
        return re.sub(r"[\s’']", "", a.lower()) == re.sub(r"[\s’']", "", b.lower())
    al, bl = a.lower(), b.lower()
    if al + "s" == bl or bl + "s" == al or al + "es" == bl or bl + "es" == al: return False
    return SequenceMatcher(None, al, bl).ratio() >= 0.7


# word pairs the similarity test took for spelling but which are different words (1688 | edition):
# bucket S, decided separately (2026-11-01, found by the before/after measure)
REAL = {("these", "those"), ("those", "these"), ("further", "farther"), ("amongst", "among"), ("among", "amongst"),
        ("remains", "remaineth"), ("about", "but"), ("once", "one"), ("presented", "represented"),
        ("parteth", "parted"), ("breathings", "breakings"), ("the", "these"), ("these", "the"), ("this", "his"),
        ("risings", "raisings"), ("fresh", "afresh"), ("speak", "spake"), ("know", "knew"), ("rent", "rend"),
        ("fail", "fall"), ("horridly", "horribly"), ("iniquity", "iniquities"), ("remembred", "remember"),
        ("nor", "or"), ("comes", "cometh"), ("furthest", "farthest"), ("searching", "scorching"),
        ("affected", "infected"), ("bear", "beat"), ("battel", "battles"), ("dram", "drachm"), ("fears", "tears"),
        ("whilst", "while"), ("jostle", "justle"), ("sprawl", "spraul"),
        ("awakened", "awaked"), ("awaked", "awakened")}
out = {"A": [], "B": [], "C": [], "K": [], "S": []}
for r in rows:
    if spelling(r) and (r["new"].lower().replace("\xad", ""), r["ed"].lower()) in REAL:
        r["tag"] = " ".join(f"{k}:{v}" for k, v in r["sup"].items() if v)
        out["S"].append(r); continue
    if spelling(r) or re.fullmatch(r"(amp c|amp|’|c|etc|)", r["new"] + r["ed"]) or re.fullmatch(r"(amp c|amp|c)", r["new"]):
        continue
    s = r["sup"]
    r["tag"] = " ".join(f"{k}:{v}" for k, v in s.items() if v)
    p88 = [k for k in ("1692", "1666") if "1688" in s[k]]; ped = [k for k in ("1692", "1666") if "ed" in s[k]]
    if not r["new"] and len(r["ed"].split()) >= 3 and "1666" in ped: out["K"].append(r)
    elif p88 and not ped: out["A"].append(r)
    elif ped and not p88: out["B"].append(r)
    else: out["C"].append(r)
json.dump(out, open("buckets.json", "w"), indent=1)
print({k: len(v) for k, v in out.items()})
