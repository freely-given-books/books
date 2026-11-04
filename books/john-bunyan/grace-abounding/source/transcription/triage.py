# the wording differences (wording.py) scored by the other texts: which side does each of the 1692
# copy, the 1666 first edition and the 1905 RTS text support, on the words with one neighbour each side
#   triage.py -> triage.json, triage.txt
import json, re, sys
from difflib import SequenceMatcher
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import wording as Wd
from gutter import witnesses, key

W = Path(__file__).parent


def main():
    wit = witnesses()
    new = Wd.tei_div_words()
    rows = []
    for f, nw in zip(Wd.FILES, new):
        ew = Wd.ed_words(f)
        nk, ek = [key(w) for w in nw], [key(w) for w in ew]
        sm = SequenceMatcher(None, nk, ek, autojunk=False)
        for op, a, b, c, d in sm.get_opcodes():
            if op == "equal": continue
            na, ea = nk[a:b], ek[c:d]
            if "".join(na) == "".join(ea): continue
            if all(x in Wd.BOOKS or x.isdigit() for x in na + ea): continue
            if (" ".join(na), " ".join(ea)) in Wd.MODERN: continue
            if [x for x in na if x not in Wd.BOOKS] == [x for x in ea if x not in Wd.BOOKS]: continue
            L, R = nk[max(0, a - 1):a], nk[b:b + 1]
            side_new = " " + " ".join(L + na + R) + " "
            side_ed = " " + " ".join(L + ea + R) + " "
            sup = {k: ("1688" if side_new in v else "") + ("ed" if side_ed in v else "") for k, v in wit.items()}
            n88 = sum("1688" in v for v in sup.values()); ned = sum("ed" in v for v in sup.values())
            cls = "ours-wrong?" if ned and not n88 else "1688-real" if n88 and not ned else "split" if n88 and ned else "unknown"
            rows.append({"file": f, "a": a, "b": b, "c": c, "d": d, "new": " ".join(nw[a:b]), "ed": " ".join(ew[c:d]), "cls": cls, "sup": sup,
                         "ctx": " ".join(nw[max(0, a - 6):a]) + " [" + " ".join(nw[a:b]) + " | " + " ".join(ew[c:d]) + "] " + " ".join(nw[b:b + 6])})
    (W / "triage.json").write_text(json.dumps(rows, indent=1))
    from collections import Counter
    print(Counter(r["cls"] for r in rows))
    with open(W / "triage.txt", "w") as fh:
        for cls in ("ours-wrong?", "1688-real", "split", "unknown"):
            fh.write(f"\n## {cls}\n")
            for r in rows:
                if r["cls"] == cls:
                    fh.write(f"{r['file'][:4]} {''.join(k[0] + (':' + v if v else '') + ' ' for k, v in r['sup'].items())}| {r['ctx']}\n")


main()
