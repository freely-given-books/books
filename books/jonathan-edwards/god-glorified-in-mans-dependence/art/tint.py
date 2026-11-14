# How art/plate.jpg is made: the river engraving ("God Glorified (river, light
# at source)" in fgbooks-generated-art) hand-tinted lightly, after Crook in the
# Lot's art/tint.py. Washes are drawn in the source's 1024x1536 coordinates.
# Usage: python3 tint.py IN-2x.png OUT.jpg

"""Hand-tint the river: a pale sky warming to gold where the light rises
behind the far hills, the river taking the sky's colour, soft greens on the
banks and trees, the line multiplied over all of it."""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageOps

src, out = sys.argv[1], sys.argv[2]
ink = (34, 52, 44)                       # the cover's deep green, for the line
line = Image.open(src).convert("L")
W, H = line.size
k = W / 1024

# the rays ChatGPT drew are too faint to survive at cover size: darken them,
# in the sky above the hills only, the edge feathered so no box shows
rays = Image.new("L", (W, H), 0)
ImageDraw.Draw(rays).polygon([(x * k, y * k) for x, y in (
    (330, 540), (700, 540), (700, 655), (610, 682), (512, 700), (420, 684), (330, 655))], fill=255)
rays = rays.filter(ImageFilter.GaussianBlur(10 * k))
line = Image.composite(line.point(lambda v: 255 if v > 245 else int(v * 0.72)), line, rays)

hz = int(690 * k)                        # where the far hills meet the sky


def vgrad(w, h, top, bot):
    g = Image.linear_gradient("L").resize((w, h))
    return Image.composite(Image.new("RGB", (w, h), bot), Image.new("RGB", (w, h), top), g)


def wash(base, colour, mask, strength):
    m = mask.point(lambda v: int(v * strength))
    return Image.composite(Image.new("RGB", base.size, colour), base, m)


def poly_mask(pts, blur):
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon([(x * k, y * k) for x, y in pts], fill=255)
    return m.filter(ImageFilter.GaussianBlur(blur * k))


def ellipse_mask(cx, cy, rx, ry, blur):
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([(cx - rx) * k, (cy - ry) * k, (cx + rx) * k, (cy + ry) * k], fill=255)
    return m.filter(ImageFilter.GaussianBlur(blur * k))


# the sky, a clear pale blue warming toward the hills; below, the water
# repeats it, a little deeper
paper = Image.new("RGB", (W, H))
paper.paste(vgrad(W, hz, (214, 228, 238), (248, 240, 222)), (0, 0))
paper.paste(vgrad(W, H - hz, (236, 238, 230), (206, 222, 230)), (0, hz))

# the light at the river's source, spreading up the sky and onto the water
gx, gy = 510, 705
glow = Image.radial_gradient("L").resize((int(700 * k), int(700 * k)))
glow = ImageOps.invert(glow).point(lambda v: int(max(0, v - 60) * 1.35))
gm = Image.new("L", (W, H), 0)
gm.paste(glow, (int(gx * k - 350 * k), int(gy * k - 350 * k)))
paper = wash(paper, (250, 226, 160), gm, 0.75)
paper = wash(paper, (246, 232, 190), poly_mask([(440, 770), (580, 770), (640, 1000), (380, 1000)], 40), 0.35)

# where the engraver drew densely, so washes keep inside the drawing
dense = ImageOps.invert(line).filter(ImageFilter.GaussianBlur(5 * k)).point(
    lambda v: 0 if v < 40 else 255 if v > 100 else int((v - 40) * 4.25))


def in_drawing(mask):
    return ImageChops.multiply(mask, dense)


# the far hills, blue-green in the distance
paper = wash(paper, (176, 198, 190), in_drawing(poly_mask([(0, 640), (1024, 640), (1024, 790), (0, 790)], 14)), 0.5)
# the banks, meadow green, warmer toward the light
banks = [
    [(0, 700), (300, 760), (480, 870), (300, 920), (0, 975)],           # left bank
    [(470, 810), (700, 760), (1024, 720), (1024, 900), (620, 850)],     # far right bank
    [(510, 1010), (760, 930), (1024, 880), (1024, 1180), (800, 1110)],  # near right bank
    [(420, 1536), (1024, 1340), (1024, 1536)],                          # the foot's grass
]
for b in banks:
    paper = wash(paper, (176, 196, 138), in_drawing(poly_mask(b, 12)), 0.55)
# the trees, a deeper green
for cx, cy, rx, ry in ((180, 740, 85, 60), (655, 752, 38, 28), (880, 880, 130, 80)):
    paper = wash(paper, (128, 156, 104), in_drawing(ellipse_mask(cx, cy, rx, ry, 6)), 0.6)

# the line over all of it
lines = ImageOps.colorize(line, black=ink, white=(255, 255, 255))
ImageChops.multiply(paper, lines).save(out, quality=93, subsampling=0)
