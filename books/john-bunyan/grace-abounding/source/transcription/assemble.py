# Grace Abounding 1688: foundation.json tokens -> lines with their ALTO boxes -> paragraphs.
# A paragraph opens on a line indented past the page's text margin (the numbered sections).
#   assemble.py -> paras.json [{"frame", "line", "indent", "text"}], prints the section check
import json, re, statistics, sys
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from alto import lines as alto_lines

W = Path(__file__).parent
NOSPACE_BEFORE = set(".,;:!?)]’”­")
NOSPACE_AFTER = set("([“‘")


def join(toks):
    out = ""
    for t in toks:
        if out and not (t[0] in NOSPACE_BEFORE or out[-1] in NOSPACE_AFTER or out.endswith("­")):
            out += " "
        out += t
    return out


@lru_cache(maxsize=None)
def line_fix():
    """foundation.py numbers a page's lines from the first kept line when the kept lines are one
    run of Kraken's; where the running head was dropped from the middle (Kraken read it out of
    order) there is no run and it numbered from 1: the true line numbers of those frames"""
    import foundation as F
    raw = F.frames(lambda n: F.kraken_lines("kf1688", n))
    pages = F.stripped(raw)
    fix = {}
    for n in sorted(pages):
        kept = pages[n]
        if any(raw[n][i:i + len(kept)] == kept for i in range(len(raw[n]))):
            continue
        j, m = 0, {}
        for k, ln in enumerate(kept):
            while raw[n][j] != ln: j += 1
            m[k + 1] = j + 1; j += 1
        fix[n] = m
    return fix


RESP = {"1692": "#p1692", "1666": "#e1666", "RTS": "#rts"}

# Transcription errors found against the current edition and read on the page (2026-11-01):
# (frame of the first token, tokens as transcribed, tokens as printed). Signature marks read into
# the text; "I" lost or read as "l"/"1"; a catchword kept beside the next page's first word.
FIXES = [
    (49, ["C"], []), (153, ["G"], []),
    (129, ["Intercession", ",", "I", "being"], ["Intercession", ",", "being"]),       # signature F
    (55, ["1", "began"], ["I", "began"]), (167, ["1"], ["I"]),
    (109, ["1", "lif\xadted"], ["I", "lif\xadted"]),
    (166, ["catcht", "them", ",", "have"], ["catcht", "them", ",", "I", "have"]),
    (17, ["time", "fell"], ["time", "I", "fell"]),
    (76, ["here", ",", "intend"], ["here", ",", "I", "intend"]),
    (83, ["what", "is", "was"], ["what", "it", "was"]),
    (94, ["l", "am"], ["I", "am"]), (102, ["Wherefore", "l"], ["Wherefore", "I"]),
    (168, ["male", "may"], ["make", "way"]),
    (61, ["sometimes", "times"], ["sometimes"]),
    (113, ["their", "their"], ["their"]),
    (59, ["yet", "I", "as", "bound"], ["yet", "I", "was", "as", "bound"]),
    (10, ["Psal", ".", "77"], ["Psal", ".", "73"]),
    (136, ["253", ".", "“", "Twas"], ["233", ".", "’Twas"]),     # middle digit damaged; 232 and 234 round it                 # as printed; Ps 77 is meant
]


def apply_fixes(toks):
    for frame, old, new in FIXES:
        hit = next((i for i in range(len(toks) - len(old) + 1) if toks[i]["p"] == frame and
                    [t["t"] for t in toks[i:i + len(old)]] == old), None)
        assert hit is not None, (frame, old)
        rep, k = [], 0
        for w in new:                              # keep each kept token (its frame, line, vote)
            j = next((j for j in range(k, len(old)) if old[j] == w), None)
            if j is not None:
                rep.append(toks[hit + j]); k = j + 1
            else:
                near = toks[hit + min(k, len(old) - 1)]
                rep.append({"t": w, "p": near["p"], "l": near["l"], "voted": "post"})
        toks[hit:hit + len(old)] = rep
    return toks


def gutter_fill(toks):
    """the words and letters the film lost in the gutter, from gutter.json (gutter.py)"""
    g = W / "gutter.json"
    if not g.exists(): return toks
    rows = [r for r in json.load(open(g)) if r["t"] not in ("Cor",)
            and (r["p"], r["l"]) != (167, 29)]          # printed, read as "1": a FIXES case
    before, after = defaultdict(list), defaultdict(list)
    first, last = {}, {}
    for i, t in enumerate(toks):
        first.setdefault((t["p"], t["l"]), i); last[(t["p"], t["l"])] = i
    for r in rows:
        if "after" in r:                     # after the line's last token (its punctuation)
            r["after"] = last[(r["p"], r["l"])]
        elif "before" in r:
            r["before"] = first[(r["p"], r["l"])] if r["before"] == first[(r["p"], r["l"])] or \
                all(not toks[k]["t"][0].isalnum() for k in range(first[(r["p"], r["l"])], r["before"])) else r["before"]
        resp = RESP[r["by"][0]]
        if r["kind"] == "word":
            t = {"t": r["t"], "p": r["p"], "l": r["l"], "voted": "gutter", "resp": resp}
            (before[r["before"]] if "before" in r else after[r["after"]]).append(t)
        else:
            t = toks[r["at"]]
            t.update({"t": r["word"], "voted": "gutter-" + r["kind"], "sup": r["t"], "resp": resp})
    out = []
    for i, t in enumerate(toks):
        out += before.get(i, []); out.append(t); out += after.get(i, [])
    return out


def page_lines():
    toks = json.load(open(W / "foundation.json"))
    fix = line_fix()
    for t in toks:
        if t["p"] in fix:
            t["l"] = fix[t["p"]][t["l"]]
    toks = apply_fixes(gutter_fill(toks))
    by = defaultdict(list)
    for t in toks:
        by[(t["p"], t["l"])].append(t)
    pages = defaultdict(list)
    for (p, l), ts in sorted(by.items()):
        box = alto_lines(p)[l - 1][1]
        pages[p].append({"frame": p, "line": l, "box": box, "toks": ts})
    for p, ls in pages.items():
        lefts = sorted(x["box"][0] for x in ls)
        margin = statistics.median(lefts[:max(3, len(lefts) // 2)])
        hs = [x["box"][3] - x["box"][1] for x in ls]
        em = statistics.median(hs)
        for x in ls:
            x["indent"] = round((x["box"][0] - margin) / em, 2)
            x["right"] = round((max(y["box"][2] for y in ls) - x["box"][2]) / em, 2)
    return pages


if __name__ == "__main__":
    pages = page_lines()
    rows = []
    for p in sorted(pages):
        for x in pages[p]:
            rows.append({"frame": p, "line": x["line"], "indent": x["indent"], "right": x["right"],
                         "text": join([t["t"] for t in x["toks"]])})
    (W / "lines.json").write_text(json.dumps(rows, indent=0))
    # section numbers at indented line starts
    nums = []
    for r in rows:
        m = re.match(r"(\d+)\s*\.", r["text"])
        if m and r["indent"] > 0.5:
            nums.append((int(m[1]), r["frame"], r["indent"]))
    prev = 0
    for n, f, ind in nums:
        if n != prev + 1:
            print("jump", prev, "->", n, "frame", f, ind)
        prev = n
    print(len(nums), "numbered starts")
    import collections
    print(collections.Counter(round(r["indent"]) for r in rows))
