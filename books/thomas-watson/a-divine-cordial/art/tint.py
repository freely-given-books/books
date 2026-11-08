# How art/plate.jpg is made: the cordial bottle engraving (art/cordial-original.png,
# ChatGPT, 2026-11-08) hand-tinted, after the cover-design skill's tint_example.py.
# The washes follow the bottle's own outline, read from the line row by row; the
# rows are in the source's 1024x1536 coordinates.
# Usage: python3 tint.py art/cordial-original.png art/plate.jpg "#CFE0DC" "#B9CFCA"
# The two colours are the ground behind the bottle, head and foot (the cover's teal;
# left out, a warm paper).

"""Hand-tint the cordial bottle: a warm amber cordial, faintly green glass, a
cream paper cap tied with brown string, the line multiplied over the washes."""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageOps

src, out = sys.argv[1], sys.argv[2]
line = Image.open(src).convert("L")
line = line.resize((line.width * 2, line.height * 2), Image.LANCZOS)
W, H = line.size
k = W / 1024
ink = (34, 40, 32)                           # a green-black, for the line

CAP_END = 888        # the paper cap and its flaps end here
SURFACE = 1063       # the cordial's level in the bottle
BASE = 1222          # the foot of the bottle

def wash(base, colour, mask, strength):
    m = mask.point(lambda v: int(v * strength))
    return Image.composite(Image.new("RGB", base.size, colour), base, m)

# the bottle's outline, row by row: the outermost lines in each row
src_px = Image.open(src).convert("L").load()
rows = {}
for y in range(765, BASE + 1):
    xs = [x for x in range(300, 720) if src_px[x, y] < 160]
    if xs:
        rows[y] = (min(xs), max(xs))

def region(y0, y1, blur=2.5):
    m = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(m)
    for y in range(y0, y1):
        if y in rows:
            a, b = rows[y]
            d.rectangle([a * k, y * k, b * k, (y + 1) * k], fill=255)
    return m.filter(ImageFilter.GaussianBlur(blur * k))

def ellipse(cx, cy, rx, ry, blur):
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([(cx - rx) * k, (cy - ry) * k, (cx + rx) * k, (cy + ry) * k], fill=255)
    return m.filter(ImageFilter.GaussianBlur(blur * k))

# the ground, a little deeper toward the foot
def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

TOP, FOOT = (hexrgb(a) for a in sys.argv[3:5]) if len(sys.argv) > 4 else ((245, 239, 225), (238, 229, 210))
paper = Image.new("RGB", (W, H), TOP)
g = Image.linear_gradient("L").resize((W, H))
paper = Image.composite(Image.new("RGB", (W, H), FOOT), paper, g)

# the table's shadow under the bottle
paper = wash(paper, (150, 130, 100), ellipse(506, 1218, 175, 14, 10), 0.35)

# the glass: neck and the empty upper body, a faint sea-green
paper = wash(paper, (198, 222, 208), region(CAP_END, SURFACE), 0.55)
# the cordial: amber, deeper at the bottom of the bowl
cordial = region(SURFACE, BASE)
paper = wash(paper, (226, 160, 72), cordial, 0.75)
deep = ImageChops.multiply(cordial, ellipse(506, 1170, 150, 70, 40))
paper = wash(paper, (176, 92, 40), deep, 0.45)
# the glow of light through the cordial, upper left of the bowl
paper = wash(paper, (252, 214, 140), ImageChops.multiply(cordial, ellipse(445, 1110, 55, 30, 18)), 0.6)
# the paper cap, cream, and its string, brown
cap = region(765, CAP_END, blur=1.5)
paper = wash(paper, (232, 214, 172), cap, 0.7)
paper = wash(paper, (126, 84, 52), ImageChops.multiply(cap, ellipse(506, 820, 82, 9, 2)), 0.45)

# the line over all of it
lines = ImageOps.colorize(line, black=ink, white=(255, 255, 255))
plate = ImageChops.multiply(paper, lines)
plate.save(out, quality=93, subsampling=0)
print(out, plate.size)
