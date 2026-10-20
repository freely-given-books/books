# Cut engraved art off a dark ground and re-ink it for a cream cover.
#   extract.py SRC OUT x0 y0 x1 y1 [ink=#2B2118]
# The art is light objects with dark hatching on a black ground with a soft
# glow. Ink is the darkness of each pixel; the mask keeps only textured
# (engraved) areas, so the smooth black ground and its glow drop out.
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as nd

src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
ink = sys.argv[7] if len(sys.argv) > 7 else "#2B2118"
ink = tuple(int(ink[i:i + 2], 16) for i in (1, 3, 5))

im = np.asarray(Image.open(src).convert("L"), dtype=np.float32)[y0:y1, x0:x1] / 255

# texture: local standard deviation; engraving is busy, the ground is smooth
m = nd.uniform_filter(im, 5)
sd = np.sqrt(np.clip(nd.uniform_filter(im * im, 5) - m * m, 0, None))
tex = nd.gaussian_filter(sd, 6)
mask = (tex > float(sys.argv[8]) if len(sys.argv) > 8 else tex > 0.045) & (nd.gaussian_filter(im, 6) > 0.12)
mask = nd.binary_closing(mask, iterations=6)
mask = nd.binary_fill_holes(mask)
lab, n = nd.label(mask)
if n:
    sizes = nd.sum(mask, lab, range(1, n + 1))
    mask = np.isin(lab, 1 + np.flatnonzero(sizes > 0.02 * sizes.max()))
mask = nd.binary_erosion(mask, iterations=3)
soft = np.clip(nd.gaussian_filter(mask.astype(np.float32), 3), 0, 1)

# tone: each pixel against its own surroundings, not against white.  A grey
# closing (a local maximum, smoothed) is the light level the lines are cut
# into -- the lit object, or the glow behind the foliage -- so a smooth glow
# comes out as paper and only the engraved lines darker than it as ink.
local = nd.gaussian_filter(nd.grey_closing(im, size=(9, 9)), 3)
dark = np.clip(1 - im / np.maximum(local, 0.08), 0, 1)
dark = np.clip(dark / 0.75, 0, 1) ** 0.85
# the ground showing between leaves: near black and smooth at a small scale
bg = (nd.gaussian_filter(im, 2) < float(sys.argv[9]) if len(sys.argv) > 9 else nd.gaussian_filter(im, 2) < 0.16) \
     & (nd.gaussian_filter(sd, 2) < 0.05)
bg = nd.gaussian_filter(nd.binary_opening(bg, iterations=1).astype(np.float32), 1.5)
alpha = (dark * soft * (1 - bg) * 255).astype(np.uint8)

rgba = np.zeros((*im.shape, 4), np.uint8)
rgba[..., :3] = ink
rgba[..., 3] = alpha
ys, xs = np.nonzero(alpha > 8)
rgba = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
Image.fromarray(rgba, "RGBA").save(out, dpi=(300, 300))
print(out, rgba.shape[1], "x", rgba.shape[0])
