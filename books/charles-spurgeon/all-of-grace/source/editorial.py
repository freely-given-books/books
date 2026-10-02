# Editorial settings for Charles Spurgeon, All of Grace (1886), from CCEL
# (https://www.ccel.org/ccel/s/spurgeon/grace.xml), kept untouched in
# grace.thml.xml. Read by build_tei.py, tei_extract.py and ./fgb.
# Second witness for readings: Monergism's 2015 PDF (CCEL's text with three
# typos corrected; see README.md).

# A modern text: the early-modern spelling and case rules stay off; CCEL's
# ASCII quotes and "--" are set as the print edition sets them.
MODERNIZE = False
TYPOGRAPHY = True
DASH = " \u2014 "           # the edition spaces its dashes

REPORT_NOTES = [
    "chapter-20.typ: the three centred appeals (#align(center)[#text(11pt)...]) are "
    "layout, not text, so they are not stored in the TEI; keep them in chapters/typ.",
]

# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "All of Grace", "author": "Charles Spurgeon",
        "file": "all-of-grace.epub", "front": "ebook-front.html", "cover": "cover_front.jpg",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["all-of-grace.typ"]
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks
