# Kraken's ALTO for the 1688 frames: per frame, the lines (in the order of the plain-text run) with
# each word's box. lines(frame) -> [(text, line_box, [(word, box)])]
import re
from functools import lru_cache
from pathlib import Path
from lxml import etree

W = Path(__file__).parent


def box(e):
    if e.get("HPOS") is None: return None
    x, y, w, h = (int(float(e.get(k))) for k in ("HPOS", "VPOS", "WIDTH", "HEIGHT"))
    return (x, y, x + w, y + h)


@lru_cache(maxsize=None)
def lines(frame):
    t = etree.parse(str(W / f"kalto/p-{frame:03d}.xml"))
    out = []
    for tl in t.iter("{*}TextLine"):
        lb = box(tl)
        words = [(s.get("CONTENT"), box(s) or lb) for s in tl.iter("{*}String")]
        out.append((" ".join(w for w, _ in words), lb, words))
    return out
