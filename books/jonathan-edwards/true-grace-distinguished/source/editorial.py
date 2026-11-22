# Editorial settings for Jonathan Edwards, True Grace, Distinguished from the Experience of Devils,
# a sermon on James 2:19 preached before the Synod of New York, convened at Newark, New Jersey,
# September 28, 1752 (N.S.), and printed at the Synod's desire. Read by build_tei.py,
# tei_extract.py and ./fgb.
#
# The orig layer is the only printing in Edwards's lifetime (New York: James Parker, 1753; Evans
# 6996, ESTC W24052) as Evans-TCP N05520 keys it, kept untouched in N05520.tcp.xml (EDITION-RULES 1).
# The same TCP file carries, bound after it, the "second edition" of Sinners in the Hands of an
# Angry God (pp. 43-62), which is its own book here; this edition takes only True Grace's sermon.
# No free scan of the 1753 printing exists (the Evans images are Readex's); the page images read
# against are the earliest free ones, the Leeds Works (1806, vol. 8), with CCEL (Hickman) as the
# keyed witness: source/SOURCES.md.

import layout
import runpy as _runpy
from pathlib import Path

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True
SMALLCAPS = "smallcaps"
# the opening word in small capitals, numerals not
OPENING_SMALLCAPS = "words"
# a decorated initial and its word printed in capitals ("OBSERVE") set as a word (Observe)
DROP_CAP_CASE = True
# Religious Affections' list (Edwards's capitalized nouns, cased from CCEL)
LOWERCASE_COMMON_NOUNS = _runpy.run_path(str(Path(__file__).parent / "nouns.py"))["LOWERCASE_COMMON_NOUNS"]
# A quotation's first word (an italic run of 5 words or more) keeps its printed capital.
QUOTE_START_CASE = True
ITALIC_SENTENCE_QUIRK = False


def _texts(root):
    """The two books in the TCP group: True Grace, then Sinners."""
    return root.findall(f".//{T}group/{T}text")


def LAYOUT(root):
    """The sermon in one file, its IMPROVEMENT a heading of the file."""
    sermon = _texts(root)[0].find(f"{T}body/{T}div")
    return [{"file": "sermon.typ", "title": "True Grace, Distinguished from the Experience of Devils",
             "parts": layout.sections(sermon)}]


DIV_LEVELS = {"part": 2}
OUTLINE_MARKS = True


def SKIP_BLOCKS(root):
    """True Grace's title page and the Synod's minute (the print's front matter: EDITION-RULES 6;
    the minute's words are on the edition's own opening page), and Sinners, the second book
    of the volume (its own edition: sinners-in-the-hands-of-an-angry-god)."""
    first, second = _texts(root)
    front = list(first.find(f"{T}front"))
    return front + list(second.iter(f"{T}div")) + [e for e in second.iter() if e.tag == f"{T}trailer"]


EPUB = {"title": "True Grace, Distinguished from the Experience of Devils", "author": "Jonathan Edwards",
        "file": "true-grace-distinguished.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["true-grace-distinguished.typ"]

# The TCP's four illegible places in True Grace (gaps 4-10 are in Sinners, not this edition).
# No 1753 page image is free to use: each is read from the sense, the Leeds Works (1806, vol. 8,
# archive.org worksofpresident81edwa) and CCEL (Hickman), which agree.
GAP_FIXES = {
    0: ("b", "high", "p. 5 'cannot [b]e of the Nature of divine and holy Light'; Leeds 1806 p. 109 and CCEL 'cannot be'", "#editor"),
    1: ("reſtleſs", "high", "p. 12 'mighty Efforts, [restless] and indefatigable Operations'; Leeds 1806 p. 115 and CCEL 'restless'", "#editor"),
    2: ("l", "high", "p. 15 'awfu[l] Threatnings'; Leeds 1806 and CCEL 'awful threatenings'", "#editor"),
    3: ("n", "high", "p. 19 'as He will the[n]'; Leeds 1806 and CCEL 'as he will then'", "#editor"),
}

# The Improvement's three uses get the edition's headings, in Edwards's words (EDITION-RULES 4:
# the second use's outline runs three levels deep).
EDITION_HEADINGS = True
