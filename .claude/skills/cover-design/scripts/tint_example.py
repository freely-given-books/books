# Example: how the Pilgrim's Progress plate was hand-tinted (see the
# cover-design skill). The washes are drawn in Pilgrim's coordinates; copy
# this and redraw them for another plate. Usage: python3 tint_example.py IN OUT

"""Hand-tint an engraving: loose watercolour washes under the line, the line
multiplied over them, as a Victorian colourist would lay them."""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageOps

src, out = sys.argv[1], sys.argv[2]
ink = (30, 44, 31)                       # the book's deep green, for the line
line = Image.open(src).convert("L")
W, H = line.size
k = W / 1024                             # drawn in the source's 1024-wide coordinates
hz = int(718 * k)                        # the horizon

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

# sky, cool above, warming toward the horizon; the field, pale gold-green
paper = Image.new("RGB", (W, H))
paper.paste(vgrad(W, hz, (192, 208, 202), (244, 231, 192)), (0, 0))
paper.paste(vgrad(W, H - hz, (232, 228, 188), (190, 200, 152)), (0, hz))

# the light at the gate, spreading through the sky and along the horizon
gx, gy = 762, 716
glow = Image.radial_gradient("L").resize((int(900 * k), int(900 * k)))
glow = ImageOps.invert(glow).point(lambda v: int(max(0, v - 60) * 1.35))
gm = Image.new("L", (W, H), 0)
gm.paste(glow, (int(gx * k - 450 * k), int(gy * k - 450 * k)))
paper = wash(paper, (247, 214, 128), gm, 0.85)

# where the engraver drew densely: the figure, not the lightly hatched field
# behind it, so a wash laid there keeps inside the drawing as a colourist's would
dense = ImageOps.invert(line).filter(ImageFilter.GaussianBlur(5 * k)).point(
    lambda v: 0 if v < 70 else 255 if v > 120 else int((v - 70) * 5.1))

def in_drawing(mask):
    return ImageChops.multiply(mask, dense)

# the hedge on the horizon and the trees by the house, green
paper = wash(paper, (150, 168, 118), in_drawing(poly_mask([(140, 700), (1024, 700), (1024, 750), (140, 750)], 3)), 0.6)
paper = wash(paper, (148, 170, 120), in_drawing(poly_mask([(0, 690), (180, 690), (300, 860), (300, 1000), (0, 1000)], 4)), 0.5)
# the thatch on the cottages
for pts in ([(0, 812), (70, 800), (122, 880), (0, 885)],
            [(110, 862), (205, 860), (215, 895), (112, 900)],
            [(225, 888), (275, 888), (280, 915), (228, 918)]):
    paper = wash(paper, (214, 184, 120), in_drawing(poly_mask(pts, 4)), 0.6)
# the near ground, a little warmer and earthier
paper = wash(paper, (206, 196, 150), poly_mask([(0, 1260), (1024, 1260), (1024, 1536), (0, 1536)], 40), 0.35)

# Christian: a russet coat, the burden a dull ochre, the book's pages left white
coat = [(450, 905), (500, 902), (522, 948), (560, 980), (556, 1012), (520, 1032),
        (512, 1180), (498, 1288), (470, 1298), (446, 1240), (422, 1290), (380, 1298),
        (370, 1190), (356, 1120), (342, 1080), (346, 1040), (372, 1030)]
paper = wash(paper, (170, 120, 86), in_drawing(poly_mask(coat, 1.5)), 0.55)
paper = wash(paper, (196, 160, 104), in_drawing(ellipse_mask(412, 968, 95, 88, 1.5)), 0.6)
paper = wash(paper, (222, 186, 152), in_drawing(ellipse_mask(486, 888, 18, 22, 1.5)), 0.35)

# the line over all of it
lines = ImageOps.colorize(line, black=ink, white=(255, 255, 255))
ImageChops.multiply(paper, lines).save(out)
