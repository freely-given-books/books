# Editorial settings for John Owen, Of the Mortification of Sin in Believers. Read by
# build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the 1668 second edition (London: for Nathanael Ponder) as EEBO-TCP A53715
# keys it, kept untouched in A53715.tcp.xml: Owen's own revision in his lifetime, and the
# printing the TCP was keyed from, so the base (the editor, 2026-11-14: "I want the classic to
# stick close to the original"). The 1656 first edition is not transcribed or scanned anywhere
# we could find. Witnesses: the 1668 scan, archive.org
# bim_early-english-books-1641-1700_of-the-mortification-of-_owen-john-dd_1668, read with Kraken
# and Tesseract (work/mortification-1668/ocr-1668); Goold's text (The Works of John Owen, vol. 6,
# 1850-53), CCEL's ThML in mort.ccel.witness.xml, the edition's base until 2026-11-14.

import layout
import runpy as _runpy
from pathlib import Path

T = "{http://www.tei-c.org/ns/1.0}"

# Gaps (build_tei.py --list): every illegible letter and word, the Greek the TCP could not key,
# read from the 1668 page images (work/mortification-1668/gaps); the Greek as the 1668 prints it,
# Goold's the check. See gap_fixes.py.
GAP_FIXES = _runpy.run_path(str(Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

QUOTE_BLOCK = True
SMALLCAPS = "smallcaps"
OPENING_SMALLCAPS = True

# The headings below each chapter title are this edition's own (Owen and Goold have none): the
# three parts of chapter V's answer, the two general rules and the nine directions, so a reader
# can see where he is in Owen's outline. label[@type="head"] in the TEI, not printed text.
EDITION_HEADINGS = True

# The title page is the print's; the bookseller's catalogue at the end is Ponder's, not Owen's.
SKIP_DIVISIONS = {"title_page", "catalogue"}

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV"]


def LAYOUT(root):
    """Owen's letter to the Christian reader (TCP: a floatingText inside the front matter's
    division), then the fourteen chapters, one file each, each chapter's printed argument set
    off under its title, indented both sides."""
    divs = layout.top_divs(root)
    letter = next(d for d in divs if d.get("type") == "to_the_Christian_reader")
    body = letter.find(f"{T}floatingText/{T}body")
    files = [{"file": "preface.typ", "title": "Preface", "parts": layout.sections(body)}]
    chapters = [d for d in divs if d.get("type") == "chapter"]
    assert [d.get("n") for d in chapters] == [str(k) for k in range(1, 15)]
    for k, div in enumerate(chapters, 1):
        arg = div.find(f"{T}argument")
        files.append({"file": f"chapter-{k:02d}.typ", "title": f"Chapter {ROMAN[k - 1]}",
                      "subtitle": arg, "subtitle_rend": "inset",
                      "parts": [p for p in layout.sections(div) if p is not arg]})
    return files


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "The Mortification of Sin", "author": "John Owen",
        "file": "the-mortification-of-sin.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "toc_depth": 4,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"],
        # the Modern English edition (MODERN-ENGLISH-RULES.md)
        "modern": {"chapters": "chapters/modern", "file": "the-mortification-of-sin-modern.epub",
                   "title": "The Mortification of Sin (Modern English)",
                   "cover": "cover-modern.typ", "front": "ebook-front-modern.html"}}
PRINT = ["the-mortification-of-sin.typ", "the-mortification-of-sin-modern.typ"]


# The outline set full width, each numbered point marked by its level (1. (1.) [1.]) with a
# little space before it: the editor's choice of 2026-11-09. Print: scripts/outline_marks.typ.
OUTLINE_MARKS = True
