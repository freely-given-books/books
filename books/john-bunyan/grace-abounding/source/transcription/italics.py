# italic words of the 1688 print: each Kraken (ALTO) word box is sheared through a range of
# slants; the slant that makes its strokes most upright (sharpest column profile) is its slant.
#   italics.py -> italics.json {"frame:line": [[word, slant, x0, x1], ...]} (line = ALTO line, 1-based)
import json, sys
from pathlib import Path
import numpy as np
from PIL import Image
sys.path.insert(0, str(Path(__file__).parent))
from alto import lines

W = Path(__file__).parent
SHEARS = np.round(np.arange(-8, 23) * 0.02, 3)   # -0.16 .. 0.44, through 0


def slant(ink):
    h, w = ink.shape
    ys, xs = np.nonzero(ink)
    if len(xs) < 40: return None
    best, bs, up = -1, 0, None
    for s in SHEARS:
        x2 = np.round(xs + s * (ys - h)).astype(int)
        x2 -= x2.min()
        score = float((np.bincount(x2).astype(float) ** 2).sum())
        if abs(s) < 1e-9: up = score
        if score > best: best, bs = score, s
    return round(float(bs), 3), round(best / up, 3)   # slant; its gain over upright


out = {}
for f in range(5, 194):
    p = W / f"f1688/p-{f:03d}.png"
    if not p.exists(): continue
    im = np.asarray(Image.open(p).convert("L"))
    thr = im.mean() - im.std()
    for n, (text, lb, words) in enumerate(lines(f), 1):
        res = []
        for w, (x0, y0, x1, y1) in words:
            # the word's x-height band only: ascenders/descenders of neighbours stay out
            yy0 = y0 + (y1 - y0) // 5; yy1 = y1 - (y1 - y0) // 5
            crop = im[yy0:yy1, x0:x1] < thr
            r = slant(crop)
            res.append([w, *(r if r else (None, None)), x0, x1])
        out[f"{f}:{n}"] = res
(W / "italics.json").write_text(json.dumps(out))
vals = [s for v in out.values() for _, s, *_ in v if s is not None]
print(len(vals), "words;", np.histogram(vals, bins=[-0.2, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.5]))
