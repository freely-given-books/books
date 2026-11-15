# How art/plate.jpg is made: the apple bough ("Religious Affections (blossom
# bough)" in fgbooks-generated-art) hand-tinted, after Crook in the Lot's
# art/tint.py. Washes are drawn in the source's 1024x1536 coordinates.
# Usage: python3 tint.py IN-2x.png OUT.jpg

"""Hand-tint the bough: blossoms white flushed with pink, young green
leaves, brown wood, the setting fruit green with a first blush, on a warm
paper; the line multiplied over all of it."""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageOps

src, out = sys.argv[1], sys.argv[2]
ink = (52, 40, 38)                       # a warm brown-black, for the line
line = Image.open(src).convert("L")
# the generated paper is not quite white: make it white, so the plate's paper is
# exactly the cover's ground and no seam shows where the plate ends
line = line.point(lambda v: 255 if v > 232 else v)
W, H = line.size
k = W / 1024
PAPER = (246, 241, 230)


def wash(base, colour, mask, strength):
    m = mask.point(lambda v: int(v * strength))
    return Image.composite(Image.new("RGB", base.size, colour), base, m)


def ellipses(spots, blur):
    m = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(m)
    for cx, cy, r in spots:
        d.ellipse([(cx - r) * k, (cy - r) * k, (cx + r) * k, (cy + r) * k], fill=255)
    return m.filter(ImageFilter.GaussianBlur(blur * k))


def stroke(pts, width, blur):
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).line([(x * k, y * k) for x, y in pts], fill=255, width=int(width * k), joint="curve")
    return m.filter(ImageFilter.GaussianBlur(blur * k))


# where the engraver drew densely (the leaves, the wood), so washes keep in the drawing
dense = ImageOps.invert(line).filter(ImageFilter.GaussianBlur(4 * k)).point(
    lambda v: 0 if v < 30 else 255 if v > 90 else int((v - 30) * 4.25))

# anywhere the engraver drew at all (the petals' fine lines too), a little spread
drawn = ImageOps.invert(line).filter(ImageFilter.GaussianBlur(9 * k)).point(
    lambda v: 0 if v < 6 else 255 if v > 30 else int((v - 6) * 10.6))

BLOSSOMS = [(390, 800, 85), (520, 860, 85), (645, 620, 90), (770, 700, 85), (355, 670, 65),
            (630, 920, 60), (150, 940, 60), (235, 905, 50), (195, 1015, 40), (100, 780, 40),
            (260, 655, 40), (840, 465, 50), (770, 480, 35), (85, 1005, 35), (870, 480, 30)]
FRUIT = [(505, 655, 34), (617, 782, 34), (348, 968, 30)]
BRANCH = [(120, 860), (240, 915), (330, 880), (450, 860), (640, 820), (830, 755), (1024, 675)]

paper = Image.new("RGB", (W, H), PAPER)
blossom = ImageChops.multiply(ellipses(BLOSSOMS, 10), drawn)
fruit = ellipses(FRUIT, 3)
wood = ImageChops.multiply(stroke(BRANCH, 30, 4), dense)
keep_out = ImageChops.lighter(ImageChops.lighter(blossom, fruit), wood)

# the leaves: young green, wherever the drawing is dense outside the flowers and wood
leaves = ImageChops.subtract(dense, keep_out)
paper = wash(paper, (150, 178, 108), leaves, 0.6)
# the wood, a soft grey-brown
paper = wash(paper, (150, 118, 92), wood, 0.55)
# the blossoms: white with a flush of pink, deeper toward the buds
paper = wash(paper, (246, 214, 214), blossom, 0.7)
paper = wash(paper, (226, 160, 168), ImageChops.multiply(drawn, ellipses([(100, 780, 30), (260, 655, 30),
             (840, 465, 38), (770, 480, 26), (85, 1005, 26), (870, 480, 22)], 6)), 0.5)
# the setting fruit: green with a first red blush on the sunward side
paper = wash(paper, (160, 186, 104), fruit, 0.75)
paper = wash(paper, (206, 120, 96), ellipses([(x + 10, y - 8, r * 0.55) for x, y, r in FRUIT], 6), 0.45)
# the falling petals
paper = wash(paper, (244, 214, 214), ImageChops.multiply(drawn, ellipses([(505, 1075, 26), (408, 1158, 30),
                                                                         (485, 1240, 26)], 6)), 0.7)

lines = ImageOps.colorize(line, black=ink, white=(255, 255, 255))
ImageChops.multiply(paper, lines).save(out, quality=93, subsampling=0)
