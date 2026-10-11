# Editorial settings for Thomas Boston, The Crook in the Lot (Edinburgh, 1737),
# from our own transcription of Samuel M'Millan's edition of Boston's Whole
# Works, vol. 3 (Aberdeen, 1848), pp. 495-590, kept as ThML in crook.thml.xml so
# the pipeline reads it as it reads a CCEL text. Read by build_tei.py,
# tei_extract.py and ./fgb.
#
# CCEL's text (crook.ccel.witness.xml, untouched) is a modernized revision with
# many spell-checker slips, so it is a witness only, as are the 1782, 1791 and
# 1811 printings on archive.org and Monergism's copy (not kept here). How the
# transcription was made is in SOURCES.md.

import layout

# A modern text: the early-modern spelling and case rules stay off.
MODERNIZE = False
TYPOGRAPHY = True
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks

# The title page is the transcription's own; the template sets the book's.
SKIP_DIVISIONS = {"titlePage"}

# Boston's doctrines, one heading level under the part.
DIV_LEVELS = {"section": 3}

XML_ID = "{http://www.w3.org/XML/1998/namespace}id"


def LAYOUT(root):
    """The publishers' preface, then Boston's three discourses, one file each;
    the doctrines are headings inside them. ThML ids: ii is To the Reader,
    iii-v the three parts."""
    by_id = {d.get(XML_ID): d for d in layout.top_divs(root)}
    return [
        {"file": "to-the-reader.typ", "title": "To the Reader",
         "parts": layout.sections(by_id["ccel-ii"])},
        {"file": "part-1.typ", "title": "Part I: The Crook in the Lot",
         "short": "The Crook in the Lot", "parts": layout.sections(by_id["ccel-iii"])},
        {"file": "part-2.typ", "title": "Part II: An Humble Spirit with the Lowly",
         "short": "An Humble Spirit", "parts": layout.sections(by_id["ccel-iv"])},
        {"file": "part-3.typ", "title": "Part III: Under the Mighty Hand of God",
         "short": "Under the Mighty Hand", "parts": layout.sections(by_id["ccel-v"])},
    ]


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "The Crook in the Lot", "author": "Thomas Boston",
        "file": "the-crook-in-the-lot.epub", "front": "ebook-front.html",
        "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-crook-in-the-lot.typ"]
