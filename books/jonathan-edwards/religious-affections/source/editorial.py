# Editorial settings for Jonathan Edwards, A Treatise Concerning Religious Affections, in Three
# Parts. Read by build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the first edition (Boston: for S. Kneeland and T. Green, 1746; Evans 5767) as
# Evans-TCP N04635 keys it, kept untouched in N04635.tcp.xml. Edwards made no later revision, so
# it is the base (EDITION-RULES 1). Witnesses: the Princeton copy of 1746 (archive.org
# treatiseconcerni1746edwa) and the New York reprint of 1768 (treatiseconcerni00edwa), read with
# Kraken and Tesseract (work/religious-affections/ocr-1746, ocr-1768); CCEL's text and the
# Worcester and Leeds Works (work/religious-affections/sources/SOURCES-SURVEY.md).

import layout
import runpy as _runpy
from pathlib import Path

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True
# Edwards's notes are English: long quotations from Flavel, Shepard, Stoddard and others.
MODERNIZE_NOTES = "case"
SMALLCAPS = "smallcaps"
# the opening word in small capitals, a numeral opening a sign not
OPENING_SMALLCAPS = "words"
# a decorated initial and its word printed in capitals ("THERE is") set as a word (There)
DROP_CAP_CASE = True

LOWERCASE_COMMON_NOUNS = _runpy.run_path(str(Path(__file__).parent / "nouns.py"))["LOWERCASE_COMMON_NOUNS"]
# A quotation's first word (an italic run of 5 words or more) keeps its printed capital.
QUOTE_START_CASE = True
# an italic run opening a sentence (#emph[First,] at a paragraph's head) takes its capital
ITALIC_SENTENCE_QUIRK = False

# Gaps (build_tei.py --list): every illegible letter and word the TCP could not key, read from the
# 1746 page images and their Kraken and Tesseract readings. See gap_fixes.py.
# the fills modernized like the words around them ("dead Frames;" -> "dead frames;")
MODERNIZE_FILLS = True
GAP_FIXES = _runpy.run_path(str(Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

# The title page and the print's own "Table of the Contents" are the print's, not the edition's
# (EDITION-RULES 6); the errata are applied in the reading text; the booksellers' notice is an
# advertisement.
SKIP_DIVISIONS = {"title_page", "index", "errata", "booksellers_notice"}

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]

# Each file's title, in Edwards's own words from the point it opens.
PART_1 = [
    ("01-the-text.typ", "The Text and the Doctrine", None),
    ("02-what-the-affections-are.typ", "What the Affections Are", "I. It may be enquired"),
    ("03-religion-in-the-affections.typ", "True Religion Lies Much in the Affections", "There are other mixt"),
    ("04-inferences.typ", "Inferences", "1. We may hence learn"),
]
# Each sign: the edition's title, in Edwards's own words, and the printed opening it starts at.
PART_2 = [("Affections Raised Very High", "I. 'Tis no Sign one Way"),
          ("Great Effects on the Body", "II. 'Tis no Sign that Affections have"),
          ("Fluent Talk of Religion", "III. 'Tis no Sign"),
          ("Affections Not Made by Ourselves", "IV. 'Tis no Sign"),
          ("Texts of Scripture Brought to Mind", "V. 'Tis no Sign"),
          ("An Appearance of Love", "VI. 'Tis no Evidence"),
          ("Affections of Many Kinds", "VII. Persons having"),
          ("Comforts Following Convictions in a Certain Order", "VIII. Nothing can"),
          ("Much Time in Religion", "IX. 'Tis no certain Sign"),
          ("Praising God with the Mouth", "X. Nothing can"),
          ("Confidence in a Good Estate", "XI. 'Tis no Sign"),
          ("Relations Pleasing to the Godly", "XII. Nothing can")]
PART_3 = [("Spiritual, Supernatural and Divine", "1. Affections that are truly spiritual"),
          ("The Excellent Nature of Divine Things", "II. The first objective Ground"),
          ("The Loveliness of Moral Excellency", "III. Those Affections"),
          ("The Mind Enlightened", "IV. Gracious Affections"),
          ("Conviction of the Reality of Divine Things", "V. Truly gracious"),
          ("Evangelical Humiliation", "VI. Gracious Affections"),
          ("A Change of Nature", "VII. Another Thing"),
          ("The Spirit of Jesus Christ", "VIII. Truly gracious"),
          ("Tenderness of Spirit", "IX. Gracious Affections"),
          ("Symmetry and Proportion", "X. Another Thing"),
          ("Longing After Spiritual Attainments", "XI. Another great"),
          ("Christian Practice", "XII. Gracious and holy")]


def _text(el):
    return " ".join(layout.printed_text(el).split())


def _blocks(div):
    """A part's blocks after its printed heads."""
    return [c for c in layout.sections(div)]


def _cut(blocks, starts):
    """blocks split before each of starts (a list of predicates, in order), each found once."""
    at, k = [0], 0
    for pred in starts:
        hits = [i for i in range(at[-1] + 1, len(blocks)) if pred(blocks[i])]
        assert hits, f"start {k} not found"
        at.append(hits[0])
        k += 1
    return [blocks[a:b] for a, b in zip(at, at[1:] + [len(blocks)])]


def _opens(prefix):
    return lambda el: layout.local(el) == "p" and _text(el).startswith(prefix)


def LAYOUT(root):
    """The preface; Part I in four files (the text and doctrine, its two heads, the inferences);
    Parts II and III one file for each numbered sign, Part III's preliminary remarks in a file of
    their own. The part's printed head is set over its first file."""
    divs = layout.top_divs(root)
    preface = next(d for d in divs if d.get("type") == "preface")
    parts = [d for d in root.iter(f"{T}div") if d.get("type") == "part"]
    assert [p.get("n") for p in parts] == ["1", "2", "3"]
    files = [{"file": "preface.typ", "title": "The Preface", "parts": layout.sections(preface)}]

    def part_title(div):
        heads = div.findall(f"{T}head")
        return heads[1] if len(heads) > 1 else None

    # Part I: the text, the doctrine and the method; I. the affections; II. their place; inferences
    # the text (1 Pet 1:8), printed as two heads under the part's title, is the first file's epigraph
    text = tuple(parts[0].findall(f"{T}head")[2:4])
    p1 = _blocks(parts[0])
    # "but I hasten to the / IId. Thing proposed": the second head opens in the sentence before it
    starts = [_opens(PART_1[1][2]), _opens(PART_1[2][2]), _opens(PART_1[3][2])]
    for k, ((name, title, _), chunk) in enumerate(zip(PART_1, _cut(p1, starts))):
        files.append({"file": f"part-1/{name}", "title": title,
                      "kicker": "Part I · The Nature and Importance of the Affections",
                      "part": "Part I" if k == 0 else None,
                      "subtitle": part_title(parts[0]) if k == 0 else None,
                      "epigraph": text if k == 0 else None, "parts": chunk})

    # Part II: the plan (I. no signs, II. distinguishing signs), then twelve signs that are no signs
    p2 = _blocks(parts[1])
    chunks = _cut(p2, [_opens(o) for _, o in PART_2])
    for n, (title, _) in enumerate(PART_2, 1):
        files.append({"file": f"part-2/sign-{n:02d}.typ", "title": title,
                      "kicker": f"Part II · No Certain Sign {ROMAN[n - 1]}",
                      "part": "Part II" if n == 1 else None,
                      "subtitle": part_title(parts[1]) if n == 1 else None,
                      "parts": (chunks[0] if n == 1 else []) + chunks[n]})

    # Part III: what may be observed of the signs, then the twelve distinguishing signs
    p3 = _blocks(parts[2])
    chunks = _cut(p3, [_opens(o) for _, o in PART_3])
    files.append({"file": "part-3/00-of-the-signs.typ", "title": "Concerning the Marks",
                  "kicker": "Part III · Distinguishing Signs", "part": "Part III",
                  "subtitle": part_title(parts[2]), "parts": chunks[0]})
    for n, (title, _) in enumerate(PART_3, 1):
        files.append({"file": f"part-3/sign-{n:02d}.typ", "title": title,
                      "kicker": f"Part III · Sign {ROMAN[n - 1]}", "parts": chunks[n]})
    return files


def SKIP_BLOCKS(root):
    """The printed "THE END." under the last part."""
    return list(root.iter(f"{T}trailer"))


# ./fgb epub / pdf / build (paths from the book folder)
OUTLINE_MARKS = True

EPUB = {"title": "Religious Affections", "author": "Jonathan Edwards",
        "file": "religious-affections.epub", "front": "ebook-front.html", "cover": "cover.typ",
        "toc_depth": 4, "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["religious-affections.typ"]
