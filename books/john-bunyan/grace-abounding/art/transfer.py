# How art/plate.jpg is made when the colour comes from a coloured copy of the
# engraving (ChatGPT): the copy's colour, lifted off its lines, is laid under
# the approved engraving's own lines, so no line, face or hand can change.
# Usage: python3 transfer.py LINE-2x.png COLOURED.png OUT.jpg [--pad SKY_ROWS]

"""Colour transfer: wash = the coloured copy with its dark lines closed over
(max filter) and softened; plate = wash x the original line. The copy is
first aligned to the line by phase correlation (a small shift)."""
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageChops, ImageOps

line_p, col_p, out = sys.argv[1:4]
line = Image.open(line_p).convert("L")
W, H = line.size
col = Image.open(col_p).convert("RGB").resize((W, H), Image.LANCZOS)

# align: the shift that best lays the copy's grey over the line
a = np.asarray(line.resize((W // 4, H // 4)), dtype=float)
b = np.asarray(col.convert("L").resize((W // 4, H // 4)), dtype=float)
F = np.fft.fft2(a - a.mean()) * np.conj(np.fft.fft2(b - b.mean()))
r = np.fft.ifft2(F / (np.abs(F) + 1e-9)).real
dy, dx = np.unravel_index(np.argmax(r), r.shape)
dy = dy - r.shape[0] if dy > r.shape[0] // 2 else dy
dx = dx - r.shape[1] if dx > r.shape[1] // 2 else dx
col = ImageChops.offset(col, dx * 4, dy * 4)
print(f"shift {dx * 4},{dy * 4} px")

# the wash: lines closed over, then softened as watercolour
wash = col.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(4))
ink = (38, 36, 52)
lines = ImageOps.colorize(line, black=ink, white=(255, 255, 255))
plate = ImageChops.multiply(wash, lines)

pad = int(sys.argv[sys.argv.index("--pad") + 1]) if "--pad" in sys.argv else 0
if pad:                                   # carry the sky up, as tint.py does
    top = plate.crop((0, 0, W, 8)).resize((1, 1)).getpixel((0, 0))
    tall = Image.new("RGB", (W, H + pad), top)
    tall.paste(plate, (0, pad))
    plate = tall
plate.save(out, quality=93, subsampling=0)
