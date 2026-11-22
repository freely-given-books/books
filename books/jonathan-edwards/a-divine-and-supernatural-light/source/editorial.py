# Editorial settings for Jonathan Edwards, A Divine and Supernatural Light, Immediately Imparted
# to the Soul by the Spirit of God, Shown to be both a Scriptural, and Rational Doctrine (Boston,
# 1734), a sermon preached at Northampton on Matt 16:17, with his preface to the people of his
# church. Read by build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the only printing in Edwards's lifetime (Boston: S. Kneeland and T. Green,
# 1734; Evans 3768) as Evans-TCP N03122 keys it, kept untouched in N03122.tcp.xml (EDITION-RULES
# 1). No free scan of the 1734 printing was found (the Evans images are Readex's); the best early
# printing with a free scan is the posthumous Boston reprint by Manning & Loring [c.1795], which
# has the sermon but not the preface or the hymn. Its page images settle the sermon's gaps.

import layout
import runpy as _runpy
from pathlib import Path

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True
SMALLCAPS = "smallcaps"
# the opening word in small capitals, numerals not
OPENING_SMALLCAPS = "words"
# a decorated initial and its word printed in capitals ("CHRIST says") set as a word
DROP_CAP_CASE = True
# Edwards's capitalized nouns (Religious Affections' and God Glorified's list) and this sermon's own
LOWERCASE_COMMON_NOUNS = _runpy.run_path(str(Path(__file__).parent / "nouns.py"))["LOWERCASE_COMMON_NOUNS"]
# A quotation's first word (an italic run of 5 words or more) keeps its printed capital.
QUOTE_START_CASE = True
ITALIC_SENTENCE_QUIRK = False
# The title page is the print's (EDITION-RULES 6). The hymn on the last page ("Taken from the
# Excellent Dr. Watts's Hymns", Luke 10:21-22) is the printer's filler, Watts's not Edwards's, and
# no later printing carries it: left out of the draft, a question for the editor (Vikunja).
SKIP_DIVISIONS = {"title_page", "poem"}


def LAYOUT(root):
    """Edwards's preface, then the sermon in one file."""
    divs = {d.get("type"): d for d in root.iter(f"{T}div")}
    return [{"file": "preface.typ", "title": "The Preface",
             "parts": layout.sections(divs["preface"])},
            {"file": "sermon.typ", "title": "A Divine and Supernatural Light",
             "parts": layout.sections(divs["sermon"])}]


OUTLINE_MARKS = True

EPUB = {"title": "A Divine and Supernatural Light", "author": "Jonathan Edwards",
        "file": "a-divine-and-supernatural-light.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["a-divine-and-supernatural-light.typ"]

# Every gap of the TCP, read from page images (EDITION-RULES 2). No free scan of the 1734
# printing exists, so the sermon's gaps (27-99) were read on the best early printing with a free
# scan, the Manning & Loring Boston reprint [c.1795] (work/divine-and-supernatural-light/scan-1795),
# by two independent full reads that agree on every gap. The preface (1-26) is not in that reprint
# nor in any later text found: its gaps are filled by sense, medium or low certainty, for the
# editor to check against a copy of the 1734 (Vikunja). Gap 0 is on the title page (not printed).
GAP_FIXES = {
    1: ('m', 'medium', 'I Am sensible (the decorated initial I, then A·m); preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    2: ('m', 'medium', 'my consenting; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    3: ('n', 'medium', 'consenting; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    4: ('nt', 'medium', 'consenting (the gap marks one letter; the word needs two); preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    5: ('', 'medium', 'fol-lowing: the mark is the line-end hyphen, no letter lost; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    6: ('mine should', 'medium', 'the following Discourse of mine should be published; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    7: ('n', 'medium', 'needs Excuse; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    8: ("I don't", 'medium', "but yet I don't think it worth the while ... much to excuse my self: he then does not plead his reluctance at length; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)", '#editor'),
    9: ('m', 'medium', 'for me; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    10: ('much', 'medium', 'for me, much to excuse my self; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    11: ('h', 'medium', 'how much I was urged; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    12: ('prevailed', 'medium', 'I was prevailed with to do it; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    13: ('with an aim', 'low', 'more to gratify others, and with an aim at promoting the Interest of Religion; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    14: ('n', 'medium', 'Religion; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    15: ('I believe', 'low', 'for such things, I believe, ordinarily make less Impression; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    16: ('R', 'medium', 'Readers; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    17: ('Design', 'medium', 'the Author, and his Design; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    18: ('s', 'medium', 'this Sermon is printed; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    19: ('t', 'medium', 'to read it; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    20: ('u', 'medium', 'upon; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    21: ('u', 'medium', 'Candour; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    22: ('l', 'medium', 'Flock; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    23: ('o', 'medium', 'out of Mode; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    24: ('t', 'medium', 'has cast my Lot; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    25: ('w', 'medium', "own'd; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)", '#editor'),
    26: ('t', 'medium', 'that I have had; preface, read by sense: no free scan of the 1734 preface (the c.1795 reprint omits it)', '#editor'),
    27: ('had', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-03); two independent reads agree', '#editor'),
    28: ('t', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-03); two independent reads agree', '#editor'),
    29: ('he', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-03); two independent reads agree', '#editor'),
    30: ('he', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-03); two independent reads agree', '#editor'),
    31: ('r', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-03); two independent reads agree', '#editor'),
    32: ('Simon', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-04); two independent reads agree', '#editor'),
    33: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-04); two independent reads agree', '#editor'),
    34: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-05); two independent reads agree', '#editor'),
    35: ('t', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-05); two independent reads agree', '#editor'),
    36: ('r', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    37: ('abit', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    38: ('xer', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    39: ('Principle', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    40: ('i', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    41: ('ples', 'high', "read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree; 'Principles' (3 marks, 4 letters)", '#editor'),
    42: ('assisted', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    43: ('and fully,', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    44: ('a', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    45: ('.', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    46: ('int', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-06); two independent reads agree', '#editor'),
    47: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    48: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    49: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    50: ('sense', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    51: ('Former', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    52: ('a', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    53: ('t', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    54: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    55: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-09); two independent reads agree', '#editor'),
    56: ('due', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    57: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    58: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    59: ('ri', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    60: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    61: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    62: ('th', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    63: ('c', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    64: ('d', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-10); two independent reads agree', '#editor'),
    65: ('t', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-12); two independent reads agree', '#editor'),
    66: ('a', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-13); two independent reads agree', '#editor'),
    67: ('e', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-13); two independent reads agree', '#editor'),
    68: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-13); two independent reads agree', '#editor'),
    69: ('e', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-13); two independent reads agree', '#editor'),
    70: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-14); two independent reads agree', '#editor'),
    71: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-14); two independent reads agree', '#editor'),
    72: ('d', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-14); two independent reads agree', '#editor'),
    73: ('H', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-14); two independent reads agree', '#editor'),
    74: ('I am come', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-14); two independent reads agree', '#editor'),
    75: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-14); two independent reads agree', '#editor'),
    76: ('could', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-15); two independent reads agree', '#editor'),
    77: ('es', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-15); two independent reads agree', '#editor'),
    78: ('adds', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-15); two independent reads agree', '#editor'),
    79: ('ye', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-15); two independent reads agree', '#editor'),
    80: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-15); two independent reads agree', '#editor'),
    81: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-15); two independent reads agree', '#editor'),
    82: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-15); two independent reads agree', '#editor'),
    83: ('i', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-15); two independent reads agree', '#editor'),
    84: ('Glory', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-16); two independent reads agree', '#editor'),
    85: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-17); two independent reads agree', '#editor'),
    86: ('ei', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-17); two independent reads agree', '#editor'),
    87: ('les', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-18); two independent reads agree', '#editor'),
    88: ('Gift', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-18); two independent reads agree', '#editor'),
    89: ('t', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-18); two independent reads agree', '#editor'),
    90: ('m', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-18); two independent reads agree', '#editor'),
    91: ('t', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-18); two independent reads agree', '#editor'),
    92: ('as', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-19); two independent reads agree', '#editor'),
    93: ('ned', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-19); two independent reads agree', '#editor'),
    94: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-19); two independent reads agree', '#editor'),
    95: ('I', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-19); two independent reads agree', '#editor'),
    96: ('r', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-20); two independent reads agree', '#editor'),
    97: ('ll', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-20); two independent reads agree', '#editor'),
    98: ('a', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-20); two independent reads agree', '#editor'),
    99: ('o', 'high', 'read on the Manning & Loring reprint [c.1795] (work scan-1795 s-20); two independent reads agree', '#editor'),
}
