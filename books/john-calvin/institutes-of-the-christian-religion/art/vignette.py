"""Make the covers' vignette, art/vignette.png, from the generated engraving
(spectacles on an open book, Institutes I.vi.1: "when aided by glasses,
begin to read distinctly"; kept in Nextcloud as fgbooks-generated-art/
"Antique Open Book with Round Spectacles.png").

The pages and glass are filled in paper colour inside the book's outline, the
lines printed in ink, and everything outside the outline transparent, so the
book sits on each volume's ground as a small printed picture.

    uv run --no-project --with numpy --with pillow python art/vignette.py IN.png
"""

import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image

INK = "#1C2433"
PAPER = "#F4EEDF"
OUT = Path(__file__).parent / "vignette.png"


def magick(*args):
    subprocess.run(["magick", *map(str, args)], check=True)


def main(src):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        gray, shape, ink, colour = (tmp / f for f in ("gray.png", "shape.png", "ink.png", "colour.png"))
        # the drawing alone, trimmed, a little white round it
        magick(src, "-colorspace", "gray", "-fuzz", "6%", "-trim", "+repage",
               "-bordercolor", "white", "-border", "20", gray)
        # the book's outline: fill the white from the corner (lines thickened
        # first so the fill cannot slip through them), the rest is the book
        magick(gray, "-threshold", "75%", "-morphology", "Erode", "Disk:2",
               "-fill", "red", "-fuzz", "5%", "-draw", "color 0,0 floodfill",
               "-fill", "white", "+opaque", "red", "-fill", "black", "-opaque", "red",
               "-morphology", "Erode", "Disk:1", shape)
        g = np.asarray(Image.open(gray).convert("L")).astype(int)
        s = np.asarray(Image.open(shape).convert("L")).copy()
        # the fill cannot get between the fine shadow lines under the book;
        # cut it at the cover's bottom edge (the lowest thick line in each
        # column of the bottom fifth), so the shadow stays lines only
        h = g.shape[0]
        dark = g < 110
        for x in range(g.shape[1]):
            run, low = 0, None
            for y in range(h):
                run = run + 1 if dark[y, x] else 0
                if run >= 5 and y > h * 0.8:
                    low = y
            if low is not None:
                s[low + 1:, x] = 0
        Image.fromarray(s).save(shape)
        # opaque inside the outline, and wherever there is ink outside it
        magick(gray, "-negate", "-level", "4%,85%", ink)
        magick(shape, ink, "-compose", "Lighten", "-composite", shape)
        magick(gray, "+level-colors", f"{INK},{PAPER}", colour)
        magick(colour, shape, "-alpha", "off", "-compose", "CopyOpacity", "-composite", OUT)
    print(OUT)


if __name__ == "__main__":
    main(sys.argv[1])
