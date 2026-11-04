# words in foundation.json that neither a word list (cracklib-small) nor CCEL's text knows:
# OCR joins ("itis" = "it is"), splits ("pierce d"), misreadings, and the print's own misprints
import json, re, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import foundation as F
vocab = set(w.strip().lower() for w in open("/usr/share/dict/cracklib-small"))
vocab |= set(w.lower() for w in re.findall(r"[^\W\d_]+", Path(F.CCEL).read_text()))
known = lambda w: (w in vocab or re.sub(r"(s|es|ed|d|ing|ly|eth|est|th|'s)$", "", w) in vocab)
T = json.loads((F.W / "foundation.json").read_text())
out = []
for i, t in enumerate(T):
    w = t["t"].replace("­", "").replace("’", "'")
    if not w[0].isalpha(): continue
    lw = w.lower()
    if known(lw) or all(known(p) for p in re.split(r"[-']", lw) if p): continue
    ctx = " ".join(x["t"] for x in T[max(0, i - 5):i + 5])
    split = next((lw[:k] + " " + lw[k:] for k in range(1, len(lw)) if known(lw[:k]) and known(lw[k:]) and len(lw[:k]) > 1 and len(lw[k:]) > 1), None)
    nxt = T[i + 1]["t"].lower() if i + 1 < len(T) else ""
    joined = lw + nxt if known(lw + nxt) and not known(nxt) else None
    out.append((t["p"], t["l"], w, split, joined, ctx))
for p, l, w, s, j, c in out:
    print(f"p{p}:{l}\t{w}\tsplit={s}\tjoin={j}\t| {c}")
