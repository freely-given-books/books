"""
Editorial tables for The Gospel Minister's Maintenance Vindicated (London:
John Harris, 1689; Wing K711A; EEBO-TCP A47561, untouched in
A47561.tcp.xml). Read by build_tei.py, tei_extract.py, tcp_structure.py and
./fgb.

Catalogued (Wing, TCP) under Hanserd Knollys, whose name heads the eleven
elders signing the recommendation; the treatise is Benjamin Keach's, and
this edition gives it to him (the foreword says why). Page images: the
same microfilm on archive.org,
bim_early-english-books-1641-1700_the-gospel-ministers-ma_knollys-hanserd_1689
(scan index = printed page + 13).
"""

import runpy
from pathlib import Path

import layout

T = "{http://www.tei-c.org/ns/1.0}"

AUTHOR = ("Keach, Benjamin, 1640-1704.",
          "This edition attributes the treatise to Benjamin Keach. Wing and "
          "EEBO-TCP catalogue it under Hanserd Knollys, the first of the eleven "
          "elders who signed its recommendation (Keach among them).")

FILES = [("chapter-01.typ", "A Regular Ministry in the Church Asserted"),
         ("chapter-02.typ", "The Gospel Minister’s Maintenance Vindicated"),
         ("chapter-03.typ", "Motives to Press the Duty of the Minister’s Maintenance, "
                            "with an Answer to Other Objections"),
         ("chapter-04.typ", "The Great and Weighty Work of a True Gospel Minister Opened")]
SHORT = [None, "The Minister’s Maintenance Vindicated", "Motives to Press the Duty",
         "The Work of a Gospel Minister"]


def LAYOUT(root):
    """The elders' recommendation (its printed address and greeting set under
    the title), then the four sections of the treatise, one file each."""
    by = {}
    for d in layout.top_divs(root):
        by.setdefault(d.get("type"), []).append(d)
    rec = by["to_the_reader"][0]
    files = [{"file": "recommendation.typ", "title": "Recommendation",
              "subtitle": rec.find(f"{T}head"), "parts": layout.sections(rec)}]
    for (f, t), s, d in zip(FILES, SHORT, by["section"]):
        parts = [x for x in layout.sections(d) if x not in _duplicates(root)]
        files.append({"file": f, "title": t, "short": s, "parts": parts})
    return files


def _duplicates(root):
    return root.findall(f".//{T}body//{T}gap[@reason='duplicate']")


def SKIP_BLOCKS(root):
    """Pages 110-111 were photographed twice on the microfilm; the TCP marks
    the second copy as a gap. Nothing is missing."""
    return _duplicates(root)


# The title page, the errata (applied in the text as editor emendations), the
# printed contents (1689 page numbers) and the Advertisement on the 38th
# Article are not part of this edition; they stay in the TEI as printed.
SKIP_DIVISIONS = {"title_page", "errata", "table_of_contents", "notice"}

# Illegible print: every gap in the edition's text filled (see gap_fixes.py).
GAP_FIXES = runpy.run_path(str(Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

TYPST_ENUM = None

REPORT_NOTES = [
    "The recommendation is dated 'July, 30. 1681.' as printed, eight years "
    "before the book (1689); left as printed.",
]

# ./fgb epub / pdf / page (paths from the book folder)
EPUB = {"title": "The Gospel Minister’s Maintenance Vindicated", "author": "Benjamin Keach",
        "file": "the-gospel-ministers-maintenance-vindicated.epub",
        "front": "ebook-front.html", "cover": "cover.typ",
        "before": ["chapters/typ/foreword.typ"],
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-gospel-ministers-maintenance-vindicated.typ"]
COVERS = ["cover.typ"]
SIDE_BY_SIDE = {"before": ["chapters/typ/foreword.typ"]}
QUOTE_BLOCK = True


# "WE have read" under a decorated initial is set "We have read".
DROP_CAP_CASE = True
