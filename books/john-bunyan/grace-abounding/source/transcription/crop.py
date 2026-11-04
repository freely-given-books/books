# Grace Abounding 1688 (EEBO microfilm): cut each frame down to its page, leaving out the film's
# black border and the sliver of the facing page beyond the gutter's dark line, which Kraken
# otherwise reads as letters glued to the line ends.
#   crop.py IN.jp2|png OUT.png [--debug]
import sys
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def runs(mask):
    """[(start, end)] of True runs"""
    out, st = [], None
    for i, v in enumerate(mask):
        if v and st is None: st = i
        if not v and st is not None: out.append((st, i)); st = None
    if st is not None: out.append((st, len(mask)))
    return out


def page_box(a):
    h, w = a.shape
    dark = a < 110
    mid = dark[int(h * 0.2):int(h * 0.8)]
    col = mid.mean(axis=0)                       # text columns ~0.1-0.35; rules, gutter, film > 0.6
    light = col < 0.55
    best = max(runs(light), key=lambda r: (r[1] - r[0]) * (1 if r[0] < w / 2 < r[1] else 0.3))
    x0, x1 = best
    rows = dark[:, x0:x1].mean(axis=1) < 0.55
    big = [r for r in runs(rows) if r[1] - r[0] > 0.04 * h]       # a smudge across the page splits the light rows:
    y0, y1 = big[0][0], big[-1][1]                                # from the first band to the last
    return x0, y0, x1, y1


def longest_vertical_run(dark):
    """per column, the longest unbroken run of dark pixels: a rule or the gutter's edge runs down
    the page, a letter's stroke is never taller than a line of type"""
    best = np.zeros(dark.shape[1], int); cur = np.zeros(dark.shape[1], int)
    for row in dark:
        cur = np.where(row, cur + 1, 0); best = np.maximum(best, cur)
    return best


def inner_rules(a, x0, x1):
    """move the side edges in past any rule within the outer 12% of the page (a sliver of the
    facing page lies beyond it)"""
    h = a.shape[0]
    run = longest_vertical_run(a[:, x0:x1] < 110)
    rule = run > 0.15 * h
    w = x1 - x0
    left = [i for i in np.where(rule)[0] if i < 0.12 * w]
    right = [i for i in np.where(rule)[0] if i > 0.88 * w]
    return x0 + (max(left) + 1 if left else 0), x0 + (min(right) if right else w)


def main(src, out, debug=False):
    im = Image.open(src).convert("L")
    a = np.asarray(im)
    x0, y0, x1, y1 = page_box(a)
    x0, x1 = inner_rules(a[y0:y1], x0, x1)
    pad = 4
    box = (x0 + pad, y0 + pad, x1 - pad, y1 - pad)
    im.crop(box).save(out)
    if debug: print(src, im.size, box)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], "--debug" in sys.argv)
