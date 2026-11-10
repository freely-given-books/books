# Editorial settings for John Owen, The Nature, Power, Deceit, and Prevalency of the Remainders
# of Indwelling-Sin in Believers. Read by build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the 1675 printing (London: for Thomas Cockerill) as EEBO-TCP A53712 keys it,
# kept untouched in A53712.tcp.xml: Owen's lifetime printing and the TCP's, so the base (the
# editor, 2026-11-08). Witnesses: the 1675 scan the TCP was keyed from and the first edition
# (London: for Elizabeth Calvert, 1668), both archive.org
# bim_early-english-books-1641-1700_the-nature-power-decei_owen-john_1675 / _1668, read with
# Kraken and Tesseract (work/indwelling-sin/ocr-1675, ocr-1668); Goold's text (The Works of John
# Owen, vol. 6, 1850-53), CCEL's ThML in indwellingsin.ccel.witness.xml.

import layout
import runpy as _runpy
from pathlib import Path

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True
SMALLCAPS = "smallcaps"
OPENING_SMALLCAPS = True

# Headings this edition adds over the parts of its deepest chapters (7, 8, 9, 10, 13), in Owen's
# own words from the chapter's text or summary, so his outline needs at most three levels of
# indent (work/indwelling-sin/outline/headings.py; the levels: source/outline.json).
EDITION_HEADINGS = True

# Gaps (build_tei.py --list): every illegible letter and word, the Greek and Hebrew the TCP could
# not key, read from the 1675 page images, its Kraken and Tesseract readings and the 1668 first
# edition's (Kraken); Goold's Greek where the print agrees with it. See gap_fixes.py.
GAP_FIXES = _runpy.run_path(str(Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

# The frontispiece and title page are the print's, not the edition's.
SKIP_DIVISIONS = {"illustration", "title_page"}

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII"]


def LAYOUT(root):
    """Owen's preface, then the seventeen chapters, one file each, each chapter's printed
    argument set off under its title, indented both sides."""
    divs = layout.top_divs(root)
    files = [{"file": "preface.typ", "title": "The Preface",
              "parts": layout.sections(next(d for d in divs if d.get("type") == "preface"))}]
    chapters = [d for d in divs if d.get("type") == "chapter"]
    assert [d.get("n") for d in chapters] == [str(k) for k in range(1, 18)]
    for k, div in enumerate(chapters, 1):
        arg = div.find(f"{T}argument")
        files.append({"file": f"chapter-{k:02d}.typ", "title": f"Chapter {ROMAN[k - 1]}",
                      "subtitle": arg, "subtitle_rend": "inset",
                      "parts": [p for p in layout.sections(div) if p is not arg]})
    return files

# ./fgb epub / pdf / build (paths from the book folder)
# The outline set full width, each numbered point marked by its level (1. (1.) [1.] before
# Owen's First, Secondly): the editor's choice of 2026-11-09. Print: scripts/outline_marks.typ.
OUTLINE_MARKS = True

EPUB = {"title": "Indwelling Sin", "author": "John Owen",
        "file": "indwelling-sin.epub", "front": "ebook-front.html", "cover": "cover.typ", "toc_depth": 4,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["indwelling-sin.typ"]
