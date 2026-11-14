# Editorial settings for Thomas Gouge, The Surest & Safest Way of Thriving (London: for William
# Rawlins, 1673). Read by build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the 1673 printing as EEBO-TCP A41657 keys it, kept untouched in
# A41657.tcp.xml. A 1676 printing (archive.org, work/surest-way/scan-1676) is the witness for the
# gaps and for any revision of Gouge's own (EDITION-RULES 1.3); the Works (1706; the 1815 reprint,
# work/thomas-gouge/sources/scan-1815) a later witness.
#
# The 1673 issue has a gathering of examples inserted after p. 24 (pp. 25-32 numbered twice): p. 24
# breaks off in the Reasons ("Men may be forward"), the inserted pages end by setting the Reasons
# again in full, and the original p. 25 goes on ("in promising"). The reading text gives the
# Reasons once, after the examples (the review removes p. 24's broken-off run); the orig layer
# keeps both, as printed.

import layout
import runpy as _runpy
from pathlib import Path

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True
SMALLCAPS = "smallcaps"
OPENING_SMALLCAPS = True
DROP_CAP_CASE = True
# an italic run ending in a full stop ends the sentence: the next word keeps its capital
ITALIC_SENTENCE_QUIRK = False
EXPAND_ETC = True
TYPST_ENUM = None
OUTLINE_MARKS = True

SKIP_DIVISIONS = {"title_page"}
LOWERCASE_COMMON_NOUNS = _runpy.run_path(str(Path(__file__).parent / "nouns.py"))["LOWERCASE_COMMON_NOUNS"]
GAP_FIXES = _runpy.run_path(str(Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

# Each file: its title, in Gouge's words where he gives a head, and the printed opening it starts at.
FILES = [
    ("01-the-text-opened.typ", "The Text Opened", None),
    ("02-the-least-of-his-saints.typ", "God Takes Notice of the Least of His Saints",
     "The words thus explained, afford unto us two"),
    ("03-the-main-point.typ", "The Least Kindness Shall Not Lose Its Reward",
     "And thus I come to the Second and main point"),
    ("04-proofs-from-scripture.typ", "Proofs from Scripture", "1. For Scripture proofes"),
    ("05-testimonies.typ", "The Testimonies of Divines", "Though these proofes of Scripture are sufficient"),
    ("06-examples.typ", "Examples out of Scripture and History", "These two Cautions premised"),
    ("07-examples-of-our-time.typ", "Examples of Our Own Time", "Daniel Waldow Esquire"),
    ("08-the-reasons.typ", "The Reasons", "The Point being thus proved by Scriptures and Examples, Come we now"),
    ("09-reproof.typ", "A Use of Reproof", "1. Vse of Reproof"),
    ("10-exhortation.typ", "A Use of Exhortation", "2. Use of Exhortation"),
    ("11-directions.typ", "Directions for Giving", "I told you before that I am willing"),
    ("12-means.typ", "Means for the Better Managing of It", "2. For the Means tending"),
    ("13-ministers.typ", "A Word for the Ministers", "A word or two for my Brethrens sake"),
]


def _first_reasons(root):
    """p. 24's run of the Reasons, broken off at "Men may be forward" where the inserted examples
    begin: its three paragraphs, the first of the two runs printed (the second, complete, is kept)."""
    ps = [p for p in root.iter(f"{T}p")]
    k = next(i for i, p in enumerate(ps) if _text(p).startswith("The point being thus proved by Scriptures"))
    assert _text(ps[k + 2]).startswith("2. Reason") and _text(ps[k + 3]).startswith("Daniel Waldow")
    return ps[k:k + 3]


def SKIP_BLOCKS(root):
    return _first_reasons(root)


def _text(el):
    return " ".join(layout.printed_text(el).split())


def LAYOUT(root):
    """The treatise cut into files at the printed openings above; the Application (a printed
    part) its own file. The text (Matt 10:41-42) is the first file's epigraph."""
    treatise = next(d for d in root.iter(f"{T}div") if d.get("type") == "treatise")
    skip = set(_first_reasons(root))
    blocks = [b for b in layout.sections(treatise)
              if b not in skip and not (layout.local(b) == "div" and b.get("type") == "part")]
    part = next(d for d in treatise.iter(f"{T}div") if d.get("type") == "part")
    at = [0]
    for _, _, opening in FILES[1:]:
        # the last match: the Reasons are printed twice, the full run after the inserted examples
        hits = [i for i, b in enumerate(blocks) if i > at[-1] and _text(b).startswith(opening)]
        assert hits, opening
        at.append(hits[-1] if opening.startswith("The Point being") else hits[0])
    files = []
    for k, (name, title, _) in enumerate(FILES):
        files.append({"file": name, "title": title,
                      "parts": blocks[at[k]:at[k + 1] if k + 1 < len(at) else len(blocks)]})
    files.append({"file": "14-application.typ", "title": "The Application", "parts": layout.sections(part)})
    return files


EPUB = {"title": "The Surest and Safest Way of Thriving", "author": "Thomas Gouge",
        "file": "the-surest-way-of-thriving.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-surest-way-of-thriving.typ"]
