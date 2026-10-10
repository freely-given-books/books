# Editorial settings for John Owen, Of Temptation: the Nature and Power of It,
# from CCEL (https://www.ccel.org/ccel/o/owen/temptation.xml), kept untouched in
# temptation.thml.xml. Read by build_tei.py, tei_extract.py and ./fgb.
#
# CCEL's text is Goold's (The Works of John Owen, vol. 6, 1850-53), with its
# page breaks. Witnesses: the 1658 first edition, EEBO-TCP A90277
# (A90277.witness.xml, untouched); Goold's printing (vol. 6, 1850) and its
# American reprint (Philadelphia, n.d.), archive.org scans; and Monergism's
# modernized ebook (not kept here: it is not ours to publish). drift.py
# compares them
# (source/witness-report.md).

import layout

# A modern text: the early-modern spelling and case rules stay off.
MODERNIZE = False
TYPOGRAPHY = True
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks

# CCEL's title page and indexes are its own apparatus.
SKIP_DIVISIONS = {"contents", "index", "titlePage"}

T = "{http://www.tei-c.org/ns/1.0}"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII"]


def _by_id(root):
    return {d.get(XML_ID): d for d in layout.top_divs(root)}


def LAYOUT(root):
    """Owen's preface to the reader, then the nine chapters, one file each.
    CCEL's ids: i.iii is the preface, i.iv chapter I ... i.xii IX."""
    by_id = _by_id(root)
    files = [{"file": "to-the-reader.typ", "title": "To the Reader",
              "parts": layout.sections(by_id["ccel-i.iii"])}]
    for k in range(1, 10):
        div = by_id[f"ccel-i.{ROMAN[k + 2].lower()}"]
        files.append({"file": f"chapter-{k:02d}.typ", "title": f"Chapter {ROMAN[k - 1]}",
                      "parts": layout.sections(div)})
    return files


def SKIP_BLOCKS(root):
    """Goold's prefatory note (1850s), not Owen's."""
    return [_by_id(root)["ccel-i.ii"]]


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "Of Temptation", "author": "John Owen",
        "file": "of-temptation.epub", "front": "ebook-front.html",
        "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["of-temptation.typ"]
