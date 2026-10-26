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

# the paper: a pale warm sky, the snow below the wall a cold blue-grey
WALL = int(540 * k)
paper = Image.new("RGB", (W, H))
paper.paste(vgrad(W, WALL, (238, 234, 222), (246, 236, 212)), (0, 0))
paper.paste(vgrad(W, H - WALL, (222, 228, 236), (232, 236, 240)), (0, WALL))

# the sun on the mountain and the women: a warm glow within the wall
glow = Image.radial_gradient("L").resize((int(900 * k), int(700 * k)))
glow = ImageOps.invert(glow).point(lambda v: int(max(0, v - 40) * 1.25))
gm = Image.new("L", (W, H), 0)
gm.paste(glow, (int(420 * k - 450 * k), int(380 * k - 350 * k)))
gm = ImageChops.multiply(gm, poly_mask([(0, 0), (700, 0), (700, 545), (0, 545)], 6))
paper = wash(paper, (248, 214, 140), gm, 0.75)

# where the engraver drew densely, so washes keep inside the drawing
dense = ImageOps.invert(line).filter(ImageFilter.GaussianBlur(4 * k)).point(
    lambda v: 0 if v < 35 else 255 if v > 95 else int((v - 35) * 4.25))

def in_drawing(mask):
    return ImageChops.multiply(mask, dense)

# the dark cloud at the far left, cold slate
paper = wash(paper, (150, 158, 178), in_drawing(poly_mask([(0, 215), (220, 230), (230, 330), (0, 365)], 10)), 0.6)
# the far hills at the left, cool and pale
paper = wash(paper, (176, 186, 200), in_drawing(poly_mask([(0, 350), (150, 365), (120, 420), (0, 425)], 10)), 0.5)
# the mountainside in the sun: warm ochre high up, grass green lower down
paper = wash(paper, (214, 182, 120), in_drawing(poly_mask([(130, 380), (420, 220), (560, 165), (700, 160), (700, 330), (150, 440)], 14)), 0.55)
paper = wash(paper, (168, 172, 112), in_drawing(poly_mask([(0, 440), (330, 360), (700, 300), (700, 545), (0, 545)], 14)), 0.55)
# the women: shawls a muted madder and brown, dresses warm grey; caps left paper
paper = wash(paper, (150, 92, 78), in_drawing(poly_mask([(190, 405), (565, 400), (565, 470), (190, 480)], 4)), 0.45)
paper = wash(paper, (140, 120, 98), in_drawing(poly_mask([(185, 470), (570, 460), (575, 530), (185, 530)], 4)), 0.45)
# the wall, cold grey stone under its snow
paper = wash(paper, (150, 156, 166), in_drawing(poly_mask([(0, 535), (700, 535), (700, 705), (0, 705)], 6)), 0.6)
# the snow and our side of the wall in shadow, cold blue
paper = wash(paper, (176, 190, 214), poly_mask([(0, 690), (700, 690), (700, 1050), (0, 1050)], 30), 0.35)
# frost-bitten grass and the thorn bush, a cold brown
paper = wash(paper, (128, 108, 92), in_drawing(poly_mask([(530, 640), (700, 640), (700, 880), (530, 880)], 6)), 0.5)
paper = wash(paper, (128, 108, 92), in_drawing(poly_mask([(0, 730), (260, 730), (260, 900), (0, 900)], 6)), 0.4)

# the line over all of it
lines = ImageOps.colorize(line, black=ink, white=(255, 255, 255))
plate = ImageChops.multiply(paper, lines)

# the foot fades into plain snow (the cover's front-ground below it), so the
# plate's edge never shows
FOOT = (228, 233, 239)
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
