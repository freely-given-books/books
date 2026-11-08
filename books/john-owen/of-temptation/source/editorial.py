# Editorial settings for John Owen, Of Temptation: the Nature and Power of It, from the first
# edition (Oxford: Leon. Lichfield for Tho. Robinson, 1658), EEBO-TCP A90277, kept untouched in
# A90277.tcp.xml. Read by build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the 1658 print as the TCP keys it; no 1658 page images are free to read,
# so the TCP stands as our witness of the print (the editor, 2026-11-05). Witnesses: the 1721
# printing (archive.org bim_eighteenth-century_of-temptation-the-natur_owen-john_1721, Kraken
# and Tesseract, work/of-temptation/ocr-1721); Goold's text (The Works of John Owen, vol. 6,
# 1850-53), CCEL's ThML in temptation.ccel.witness.xml, the previous edition's source; and
# Monergism's modernized ebook (not kept here). Goold's wording, already brought close to
# Owen's, is the modernization layer: the review (chapters/typ).

import layout

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks
SMALLCAPS = "smallcaps"
OPENING_SMALLCAPS = True  # "HAving shewed": the chapter's first word in small capitals, as Goold
# A chapter opening the 1658 print sets without a drop capital, in small capitals as Goold. (His
# small-capital LORD and GOD, three times, are plain "Lord", "God" in the 1658 print: kept so.)
SMALLCAPS_PHRASES = ("^[The] Directions",)

# The title page is the print's, not the edition's; the errata are the printer's corrections,
# carried into the reading text as emendations (source/errata.md), not printed.
SKIP_DIVISIONS = {"title_page", "errata"}

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


def LAYOUT(root):
    """Owen's preface to the reader, then the nine chapters, one file each, each chapter's
    printed summary (head[@type="sub"]) set off under its title, indented both sides."""
    divs = layout.top_divs(root)
    files = [{"file": "to-the-reader.typ", "title": "To the Reader",
              "parts": layout.sections(next(d for d in divs if d.get("type") == "dedication"))}]
    chapters = [d for d in divs if d.get("type") == "chapter"]
    assert [d.get("n") for d in chapters] == [str(k) for k in range(1, 10)]
    for k, div in enumerate(chapters, 1):
        sub = next(h for h in div.findall(f"{T}head") if h.get("type") == "sub")
        files.append({"file": f"chapter-{k:02d}.typ", "title": f"Chapter {ROMAN[k - 1]}",
                      "subtitle": sub, "subtitle_rend": "inset", "parts": layout.sections(div)})
    return files


# Macron abbreviations default to a suppressed "n"; these document-order indices expand to "m"
# (te̅ptations, the̅, diste̅per, the̅selves: Goold and 1721 read temptations, them, distemper,
# themselves).
MACRON_M = {1, 3, 4, 5, 9}

# Gaps (build_tei.py --list): (letters, certainty, evidence). The Greek the TCP could not key
# is Goold's, and προσέχειν was read on the 1721 page (frame 11); gap 9 (Greek after "lead us
# not into temptation", p. 34) is in neither 1721 nor Goold and was read on the 1658 page (the
# user's scan); the reading text drops it. Gaps 1-5 are in the errata, which the edition does
# not print.
GAP_FIXES = {
    0: ("ly", "medium", "seen dayly: Goold and 1721 'daily'", "#editor"),
    6: ("Cor", "high", "margin Heb. 2. 9. Gal. 3. 13. 2 Cor. 5. 21. (Goold, 1721)", "#editor"),
    7: ("ἐμπίπτειν", "high", "Goold; 1 Tim. 6:9", "#editor"),
    8: ("προσέχειν", "high", "1721 page (frame 11), Goold", "#editor"),
    9: ("ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ", "high",
        "1658 (user's scan, pdf page 22 = pp. 34-35): ἀλλα ῥῦσαι ἡμᾶς ἀπο | τοῦ πονηροῦ, "
        "τοῦ and final -οῦ as ligatures, π as ϖ; Matt. 6:13; accents normalized", "#editor"),
    10: ("ἐκ τοῦ πονηροῦ", "high", "Goold", "#editor"),
    11: ("φρουρήσει τὰς καρδίας", "high", "Goold; Phil. 4:7", "#editor"),
    12: ("Φρουρά", "high", "Goold", "#editor"),
    13: ("φρουρήσει", "high", "Goold", "#editor"),
    14: ("Τὴν καλὴν παρακαταθήκην", "high", "Goold; 2 Tim. 1:14", "#editor"),
}

# The headings below each chapter title are this edition's own (Owen and Goold have none): the
# three parts of the text's opening, the doctrine, and the two inquiries with their parts, so a
# reader can see where he is in Owen's outline. label[@type="head"] in the TEI, not printed text.
EDITION_HEADINGS = True

# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "Of Temptation", "author": "John Owen",
        "file": "of-temptation.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "toc_depth": 4,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["of-temptation.typ"]
