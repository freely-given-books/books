# How art/plate.jpg is made: Boston's engraving hand-tinted, after the
# cover-design skill's tint_example.py (Pilgrim's). Washes are drawn in the
# source's 1024x1536 coordinates. Usage: python3 tint.py IN-2x.png OUT.jpg

"""Hand-tint an engraving: loose watercolour washes under the line, the line
multiplied over them, as a Victorian colourist would lay them."""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageOps

src, out = sys.argv[1], sys.argv[2]
ink = (40, 33, 62)                       # Boston's heather, for the line
line = Image.open(src).convert("L")
W, H = line.size
k = W / 1024
hz = int(640 * k)                        # the far hills' line, where the sun rises

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

# the sky, cool heather above, warming to rose at the hills; the land below,
# a pale sage that the washes build on
SKY_TOP, SKY_LOW = (222, 218, 236), (246, 228, 214)
LAND_TOP, LAND_LOW = (232, 230, 214), (238, 234, 222)
paper = Image.new("RGB", (W, H))
paper.paste(vgrad(W, hz, SKY_TOP, SKY_LOW), (0, 0))
paper.paste(vgrad(W, H - hz, LAND_TOP, LAND_LOW), (0, hz))

# the dawn behind the far hills, spreading through the sky and down their slopes
gx, gy = 367, 625
glow = Image.radial_gradient("L").resize((int(820 * k), int(820 * k)))
glow = ImageOps.invert(glow).point(lambda v: int(max(0, v - 50) * 1.3))
gm = Image.new("L", (W, H), 0)
gm.paste(glow, (int(gx * k - 410 * k), int(gy * k - 410 * k)))
paper = wash(paper, (250, 218, 150), gm, 0.8)

# where the engraver drew densely, so washes keep inside the drawing
dense = ImageOps.invert(line).filter(ImageFilter.GaussianBlur(5 * k)).point(
    lambda v: 0 if v < 40 else 255 if v > 100 else int((v - 40) * 4.25))

def in_drawing(mask):
    return ImageChops.multiply(mask, dense)

# the far hills, heather in the dawn
paper = wash(paper, (198, 172, 206), in_drawing(poly_mask([(0, 610), (1024, 600), (1024, 720), (0, 730)], 12)), 0.55)
# the middle slopes on the right, sage green
paper = wash(paper, (170, 186, 146), in_drawing(poly_mask([(330, 790), (1024, 690), (1024, 900), (480, 960)], 14)), 0.55)
# the valley's sides, deep heather, still in shadow
paper = wash(paper, (140, 110, 156), in_drawing(poly_mask([(0, 710), (380, 780), (660, 950), (300, 1170), (0, 1170)], 14)), 0.6)
# the near hill, grass in the first light
paper = wash(paper, (176, 190, 138), in_drawing(poly_mask([(470, 960), (1024, 860), (1024, 1290), (0, 1290), (0, 1180)], 18)), 0.5)
paper = wash(paper, (236, 222, 176), poly_mask([(0, 1200), (1024, 1100), (1024, 1340), (0, 1340)], 50), 0.25)

# the crook, brown wood
staff = [(878, 900), (896, 900), (948, 530), (930, 528)]
paper = wash(paper, (150, 104, 70), in_drawing(poly_mask(staff, 1.5)), 0.7)
paper = wash(paper, (150, 104, 70), in_drawing(ellipse_mask(915, 545, 40, 32, 1.5)), 0.7)

# the line over all of it
lines = ImageOps.colorize(line, black=ink, white=(255, 255, 255))
plate = ImageChops.multiply(paper, lines)

# the foot fades into plain paper (the cover's front-ground below it), so the
# plate's edge never shows
FOOT = (236, 232, 220)
fade = Image.new("L", (W, H), 0)
fade.paste(Image.linear_gradient("L").resize((W, int(150 * k))), (0, H - int(150 * k)))
Image.composite(Image.new("RGB", (W, H), FOOT), plate, fade).save(out, quality=93, subsampling=0)
