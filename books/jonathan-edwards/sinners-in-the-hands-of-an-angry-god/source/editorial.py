"""
Editorial tables for Jonathan Edwards, Sinners in the Hands of an Angry God
(preached at Enfield, July 8, 1741). Source: EEBO-TCP's Evans text N05520,
untouched in N05520.tcp.xml: True Grace, Distinguished from the Experience
of Devils (New York, 1753) with, bound after it, the "second edition" of
Sinners (Boston printed, New York reprinted by James Parker), pages 43-62.
The first edition (Boston, 1741) has no TCP transcription. Read by
build_tei.py, tei_extract.py, tcp_structure.py and ./fgb.

The edition (chapters/typ) was finished before the TEI existed; the TEI is
built from it with --review, so every change it makes to the printed text
is an #editor decision.
"""

import layout

T = "{http://www.tei-c.org/ns/1.0}"


def _texts(root):
    """The two books in the TCP group: True Grace, then Sinners."""
    return root.findall(f".//{T}group/{T}text")


def LAYOUT(root):
    """Sinners as one file; the printed head is replaced by the edition's
    title, the APPLICATION part is a heading of the file."""
    sinners = _texts(root)[1].find(f"{T}body/{T}div")
    return [{"file": "sermon.typ", "title": "Sinners in the Hands of an Angry God",
             "parts": layout.sections(sinners)}]


DIV_LEVELS = {"part": 2}


def SKIP_BLOCKS(root):
    """True Grace (the first book of the volume) and Sinners' title page."""
    first, second = _texts(root)
    return list(first.iter(f"{T}div")) + [second.find(f"{T}front/{T}div")]


TYPST_ENUM = None

REPORT_NOTES = [
    "True Grace, Distinguished from the Experience of Devils (the first book "
    "of this TCP volume) and Sinners' title page are in the TEI as printed, "
    "but not in this edition.",
]

# ./fgb epub / pdf / page (paths from the book folder)
EPUB = {"title": "Sinners in the Hands of an Angry God", "author": "Jonathan Edwards",
        "file": "sinners-in-the-hands-of-an-angry-god.epub", "front": "ebook-front.html",
        "cover": "cover.jpg",
        "css": ["../../resources/css/ebook.css"]}
PRINT = ["sinners-in-the-hands-of-an-angry-god.typ"]
QUOTE_BLOCK = True
