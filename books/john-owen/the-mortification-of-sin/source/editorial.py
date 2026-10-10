# Editorial settings for John Owen, Of the Mortification of Sin in Believers,
# from CCEL (https://www.ccel.org/ccel/o/owen/mort.xml), kept untouched in
# mort.thml.xml. Read by build_tei.py, tei_extract.py and ./fgb.
#
# CCEL's text is Goold's (The Works of John Owen, vol. 6, 1850-53), with its
# page breaks. Witnesses: the 1668 second edition, EEBO-TCP A53715
# (A53715.witness.xml, untouched); and Monergism's modernized ebook (not kept
# here: it is not ours to publish). drift.py compares them
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
    """Owen's preface to the reader, then the fourteen chapters, one file
    each. CCEL's ids: i.iii is the preface, i.iv chapter I ... i.xvii XIV."""
    by_id = _by_id(root)
    files = [{"file": "preface.typ", "title": "Preface",
              "parts": layout.sections(by_id["ccel-i.iii"])}]
    for k in range(1, 15):
        div = by_id[f"ccel-i.{ROMAN[k + 2].lower()}"]
        files.append({"file": f"chapter-{k:02d}.typ", "title": f"Chapter {ROMAN[k - 1]}",
                      "parts": layout.sections(div)})
    return files


def SKIP_BLOCKS(root):
    """Goold's prefatory note (1850s), not Owen's."""
    return [_by_id(root)["ccel-i.ii"]]


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "The Mortification of Sin", "author": "John Owen",
        "file": "the-mortification-of-sin.epub", "front": "ebook-front.html",
        "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-mortification-of-sin.typ"]
