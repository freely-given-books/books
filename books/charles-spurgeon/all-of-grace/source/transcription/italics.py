# italic words in the 1886 print: each Tesseract word box is sheared through a range of
# slants; the slant that makes its strokes most upright (sharpest column profile) is its
# slant. Roman type stands near 0, this italic near 0.2 (12 degrees).
#   italics.py -> italics.json {"page:line": [[word, slant], ...]} (line = assemble.tess_lines order)
import csv, json, re, sys
from pathlib import Path
import numpy as np
from PIL import Image
sys.path.insert(0, str(Path(__file__).parent))
from assemble import X, W, tess_lines

SHEARS = np.linspace(-0.1, 0.4, 26)


def slant(ink):
    h, w = ink.shape
    ys, xs = np.nonzero(ink)
    if len(xs) < 30: return None
    best, bs = -1, 0
    for s in SHEARS:
        x2 = np.round(xs + s * (ys - h)).astype(int)
        x2 -= x2.min()
        prof = np.bincount(x2)
        score = float((prof.astype(float) ** 2).sum())
        if score > best: best, bs = score, s
    return round(float(bs), 3)


def words(page):
    f = X / f"tesseract/pages/{page:06d}.tsv"
    rows = [r for r in csv.DictReader(open(f), delimiter="\t", quoting=csv.QUOTE_NONE)
            if r["level"] == "5" and (r.get("text") or "").strip()]
    return rows


out = {}
for page in range(9, 135):
    im = np.asarray(Image.open(W / f"pages/p-{page:03d}.png").convert("L"))
    thr = im.mean() - 2 * im.std() * 0.5
    lines = tess_lines(page)
    tops = {(l["top"], l["left"]): n for n, l in enumerate(lines)}
    by = {}
    for r in words(page):
        by.setdefault((r["block_num"], r["par_num"], r["line_num"]), []).append(r)
    for ws in by.values():
        top = min(int(w["top"]) for w in ws); left = min(int(w["left"]) for w in ws)
        n = tops.get((top, left))
        res = []
        for w in ws:
            x, y, ww, hh = (int(w[k]) for k in ("left", "top", "width", "height"))
            crop = im[y:y + hh, x:x + ww] < thr
            res.append([w["text"], slant(crop)])
        out[f"{page}:{n}"] = res
(W / "italics.json").write_text(json.dumps(out))
vals = [s for v in out.values() for _, s in v if s is not None]
print(len(vals), "words; histogram:", np.histogram(vals, bins=[-0.11, 0.05, 0.1, 0.15, 0.41])[0])
