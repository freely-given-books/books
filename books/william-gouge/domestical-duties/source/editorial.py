"""Editorial tables for William Gouge, Of Domesticall Duties (1622),
EEBO-TCP A68107. Read by scripts/tei/build_tei.py, tei_extract.py and the
other TEI tools (see the eebo-tcp-book skill)."""

import json
import re
from pathlib import Path

import layout

# Printed divisions the edition leaves out: the title page, and the table
# of contents, which indexes the 1622 pagination this edition does not share.
SKIP_DIVISIONS = {"title_page", "table_of_contents"}

# Gouge writes in numbered sections (heading level 3 under the edition's
# chapters); a question or objection inside a section has a run-in head.
DIV_LEVELS = {"section": 3, "dedication": 2, "errata": 2}
RUN_IN_DIVS = {"question", "dedication"}   # the dedication's address, in bold

EDITION = json.loads((Path(__file__).parent / "edition.json").read_text(encoding="utf-8"))


def slugify(title):
    s = title.lower().replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def LAYOUT(root):
    """edition.json: four volumes of chapters, each chapter a run of one
    treatise's sections cut by ordinal position (Gouge's own numbering
    repeats), plus the front and back matter each volume claims."""
    divs = layout.top_divs(root)
    files = []
    for vol in EDITION["volumes"]:
        d = f"vol-{vol['number']}"

        def matter(name):
            spec = EDITION["front"][name]
            files.append({"file": f"{d}/{name}.typ", "title": spec.get("title"),
                          "parts": [divs[spec["div"] - 1]]})
        for name in vol.get("front", []):
            matter(name)
        for i, ch in enumerate(vol["chapters"], start=1):
            first, last = ch["sections"]
            files.append({"file": f"{d}/{i:02d}-{slugify(ch['title'])}.typ",
                          "title": ch["title"],
                          "parts": layout.sections(divs[ch["div"] - 1], first, last)})
        for name in vol.get("back", []):
            matter(name)
    return files

# Margin notes are modernized too: Gouge's margins carry a running summary in
# English beside the citations, and leaving it in 1622 spelling next to
# modern text reads as an accident. Latin (in notes and text) is found per
# run of text and left as printed.
MODERNIZE_NOTES = True
LATIN_RUNS = True

# Common nouns this book capitalizes by convention rather than by meaning;
# only words that are never a title or proper name here ("Church", "Word",
# "Sabbath", "Minister" keep their capitals).
LOWERCASE_COMMON_NOUNS = {
    "husband", "husbands", "wife", "wives", "wiues", "child", "children",
    "childe", "parent", "parents", "father", "fathers", "mother", "mothers",
    "son", "sonne", "sonnes", "sons", "daughter", "daughters",
    "servant", "servants", "seruant", "seruants", "master", "masters",
    "mistress", "mistresse", "mistresses", "family", "familie", "families",
    "house", "household", "households", "houshold", "marriage", "mariage",
    "marriages", "contract", "contracts", "duty", "dutie", "duties",
    "subjection", "subiection", "authority", "authoritie", "obedience",
    "reverence", "reuerence", "honour", "honor", "love", "loue",
    "nature", "reason", "argument", "arguments", "rule", "rules",
    "case", "cases", "example", "examples", "note", "notes",
    "estate", "state", "states", "person", "persons", "place", "places",
    "point", "points", "thing", "things", "time", "times", "way", "ways",
    "wayes", "word", "words", "work", "works", "worke", "workes",
    "man", "men", "woman", "women", "brother", "brethren", "sister",
    "sisters", "widow", "widdow", "widows", "widdowes", "bride",
    "bridegroom", "bridegroome", "kindred", "sex", "society", "societie",
    "commonwealth", "common", "general", "generall", "particular", "proper",
}

# This edition's own spellings, over the shared table in spelling.py (what
# the Gouge edition printed before it moved to the TEI pipeline).
SPELLING = {
    "domesticall": "domestical",
    "vaile": "veil", "vailes": "veils",
    "iudgement": "judgment", "iudgements": "judgments",
    "judgement": "judgment", "judgements": "judgments",
}
# the 1622 spellings the review fixed by hand, found in every place they
# occur (possessives without the apostrophe, as printed: "Abrahams")
import runpy as _runpy
SPELLING.update(_runpy.run_path(str(Path(__file__).parent / "spelling_1622.py"))["SPELLING_1622"])

# "thorow" (9 times) is left as printed by the machine: it is "through" in
# some places ("strike thorow the very heart") and "thorough" in others ("a
# thorow dislike"); the old converter made them all "thorough". Each one is
# an editor decision in the review (4 thorough, 5 through, 2026-10-01).
REPORT_NOTES = []

# Illegible gaps: 477 of 478 filled (189 by hand, 288 from the book's own
# vocabulary), carried over from the earlier converter; see gap_fixes.py.
import runpy as _runpy
GAP_FIXES = _runpy.run_path(str(Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

# Greek and Hebrew the transcribers could not key (240, nearly all in margin
# citations) are read from the 1622 page images and filled in gap_fixes.py;
# this only matters for any left open.
DROP_FOREIGN_GAPS = True

# Pages 191-196, missing from the copy the TCP was made from, come from
# another 1622 copy (A68107.supplied.xml); the one illegible word is read
# there too, so no gap needs a note.
GAP_NOTES = {}

EXPAND_ETC = True

# An italic doctrine opening a paragraph ("Parents ought to...") starts a
# sentence, but an italic right after a full stop ("viz. to") does not; and
# "AS there are" under a decorated initial is set "As there are".
ITALIC_SENTENCE_QUIRK = "after-stop"
DROP_CAP_CASE = True

# Lists the review numbers ("+" items) keep Typst's 1. 2. 3., not I. II.
TYPST_ENUM = None

# A paragraph that opens with its number ("3. It is a means...") is set as a
# numbered item, as the printed volumes have always had it.
TYPST_NUMBERED_PARAGRAPHS = "enum"

# ./fgb epub / pdf / page (paths from the book folder)
EPUB = {"title": "Of Domestical Duties", "author": "William Gouge",
        "file": "domestical-duties.epub", "cover": "cover-ebook.typ",
        "front": "ebook-front.html",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"],
        "toc_depth": 4,
        # one ebook per volume, as printed
        "volumes": [
        {"files": ["vol-1/"], "title": "Of Domestical Duties, Volume I",
         "file": "domestical-duties-vol-1.epub", "cover": "cover-vol-1.typ",
         "front": "ebook-front-vol-1.html"},
        {"files": ["vol-2/"], "title": "Of Domestical Duties, Volume II",
         "file": "domestical-duties-vol-2.epub", "cover": "cover-vol-2.typ",
         "front": "ebook-front-vol-2.html"},
        {"files": ["vol-3/"], "title": "Of Domestical Duties, Volume III",
         "file": "domestical-duties-vol-3.epub", "cover": "cover-vol-3.typ",
         "front": "ebook-front-vol-3.html"},
        {"files": ["vol-4/"], "title": "Of Domestical Duties, Volume IV",
         "file": "domestical-duties-vol-4.epub", "cover": "cover-vol-4.typ",
         "front": "ebook-front-vol-4.html"}]}
PRINT = [f"domestical-duties-vol-{n}.typ" for n in range(1, 5)]
SIDE_BY_SIDE = {"split": ["vol-1/", "vol-2/", "vol-3/", "vol-4/"]}
