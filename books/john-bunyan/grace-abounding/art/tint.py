# How art/plate.jpg is made: the engraving of Bunyan's vision (§53-55),
# hand-tinted after the cover-design skill's tint_example.py and Crook's
# tint.py. Washes are drawn in a 700x1050 preview's coordinates.
# Usage: python3 tint.py IN-2x.png OUT.jpg

"""Hand-tint an engraving: loose watercolour washes under the line, the line
multiplied over them. The sun within the wall is warm; our side is cold."""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageOps

src, out = sys.argv[1], sys.argv[2]
ink = (38, 36, 52)                        # a cold slate for the line
line = Image.open(src).convert("L")
W, H = line.size
k = W / 700

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

# the paper: a soft blue sky warming toward the mountain; the snow below the
# wall a cold blue
WALL = int(540 * k)
paper = Image.new("RGB", (W, H))
paper.paste(vgrad(W, WALL, (206, 222, 238), (250, 236, 206)), (0, 0))
paper.paste(vgrad(W, H - WALL, (206, 218, 236), (226, 233, 242)), (0, WALL))

# the sun on the mountain and the women: a warm glow within the wall
glow = Image.radial_gradient("L").resize((int(900 * k), int(700 * k)))
glow = ImageOps.invert(glow).point(lambda v: int(max(0, v - 40) * 1.25))
gm = Image.new("L", (W, H), 0)
gm.paste(glow, (int(420 * k - 450 * k), int(400 * k - 350 * k)))
gm = ImageChops.multiply(gm, poly_mask([(0, 120), (700, 120), (700, 545), (0, 545)], 40))
paper = wash(paper, (250, 206, 120), gm, 0.8)

# where the engraver drew densely, so washes keep inside the drawing
dense = ImageOps.invert(line).filter(ImageFilter.GaussianBlur(4 * k)).point(
    lambda v: 0 if v < 35 else 255 if v > 95 else int((v - 35) * 4.25))

def in_drawing(mask):
    return ImageChops.multiply(mask, dense)

# heavy hatching: the women's clothes and the outlines round them; the land's
# washes keep off it, the shawls keep to it
cloth = ImageOps.invert(line).filter(ImageFilter.GaussianBlur(2 * k)).point(
    lambda v: 0 if v < 90 else 255 if v > 150 else int((v - 90) * 4.25))
not_cloth = ImageOps.invert(cloth.filter(ImageFilter.MaxFilter(17)).filter(ImageFilter.GaussianBlur(3 * k)))

def on_land(mask):
    return ImageChops.multiply(in_drawing(mask), not_cloth)

# the dark cloud at the far left, cold slate blue
paper = wash(paper, (112, 128, 162), in_drawing(poly_mask([(0, 215), (220, 230), (230, 330), (0, 365)], 10)), 0.75)
# the far hills at the left, cool blue
paper = wash(paper, (150, 170, 200), in_drawing(poly_mask([(0, 350), (150, 365), (120, 420), (0, 425)], 10)), 0.65)
# the mountainside in the sun: gold high up, grass green lower down, the
# trees a deeper green, the rocks warm grey
paper = wash(paper, (222, 170, 82), on_land(poly_mask([(130, 380), (420, 220), (560, 165), (700, 160), (700, 330), (150, 440)], 14)), 0.75)
paper = wash(paper, (140, 168, 72), on_land(poly_mask([(0, 440), (330, 360), (700, 300), (700, 545), (0, 545)], 14)), 0.7)
paper = wash(paper, (84, 120, 60), in_drawing(poly_mask([(500, 280), (700, 280), (700, 360), (500, 370)], 8)), 0.6)
paper = wash(paper, (84, 120, 60), in_drawing(poly_mask([(0, 440), (180, 420), (180, 500), (0, 505)], 8)), 0.55)
# the women, each her own shawl, over warm grey-brown skirts: washed only
# where the engraver hatched heavily (the cloth, not the grass round it), and
# below the faces; then the faces and the raised hand in a light flesh tone
FACES = [(243, 422), (352, 432), (438, 432), (503, 446)]
for (x0, x1), (fx, fy), colour in [((190, 268), FACES[0], (150, 54, 46)),    # madder red
                                   ((282, 386), FACES[1], (52, 70, 128)),    # indigo
                                   ((392, 468), FACES[2], (78, 108, 62)),    # moss green
                                   ((462, 560), FACES[3], (150, 86, 44))]:   # russet
    m = poly_mask([(x0, fy + 14), (x1, fy + 14), (x1, 478), (x0, 482)], 2)
    paper = wash(paper, colour, ImageChops.multiply(m, cloth), 0.75)
paper = wash(paper, (128, 104, 82), ImageChops.multiply(poly_mask([(188, 478), (568, 470), (570, 530), (188, 530)], 2), cloth), 0.6)
for fx, fy in FACES:
    paper = wash(paper, (238, 208, 182), ellipse_mask(fx, fy, 11, 13, 2), 0.9)
paper = wash(paper, (238, 208, 182), ellipse_mask(380, 456, 10, 7, 2), 0.9)

# the wall, grey stone warmed a little, under its snow
paper = wash(paper, (128, 126, 128), in_drawing(poly_mask([(0, 535), (700, 535), (700, 705), (0, 705)], 6)), 0.7)
# the snow and our side of the wall in shadow, cold blue
paper = wash(paper, (150, 172, 214), poly_mask([(0, 690), (700, 690), (700, 1050), (0, 1050)], 30), 0.45)
# frost-bitten grass and the thorn bush, a cold brown
paper = wash(paper, (120, 92, 70), in_drawing(poly_mask([(530, 640), (700, 640), (700, 880), (530, 880)], 6)), 0.6)
paper = wash(paper, (120, 92, 70), in_drawing(poly_mask([(0, 730), (260, 730), (260, 900), (0, 900)], 6)), 0.5)

# the line over all of it
lines = ImageOps.colorize(line, black=ink, white=(255, 255, 255))
plate = ImageChops.multiply(paper, lines)

# the foot fades into plain snow (the cover's front-ground below it), so the
# plate's edge never shows
FOOT = (222, 230, 242)
fade = Image.new("L", (W, H), 0)
fade.paste(Image.linear_gradient("L").resize((W, int(100 * k))), (0, H - int(100 * k)))
plate = Image.composite(Image.new("RGB", (W, H), FOOT), plate, fade)

# more sky above the scene, so the title block stands on open sky, clear of
# the mountain's ridge: the top row's own colour, carried up
PAD = int(170 * k)
top = plate.crop((0, 0, W, 8)).resize((1, 1)).getpixel((0, 0))
tall = Image.new("RGB", (W, H + PAD), top)
tall.paste(plate, (0, PAD))
blend = Image.linear_gradient("L").resize((W, int(30 * k)))
seam = Image.composite(plate.crop((0, 0, W, int(30 * k))), Image.new("RGB", (W, int(30 * k)), top), blend)
tall.paste(seam, (0, PAD))
tall.save(out, quality=93, subsampling=0)
