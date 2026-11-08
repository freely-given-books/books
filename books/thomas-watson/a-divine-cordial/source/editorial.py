# Editorial settings for Thomas Watson, A Divine Cordial, from the first edition (London: for
# Thomas Parkhurst, 1663), EEBO-TCP A65292, kept untouched in A65292.tcp.xml. Read by
# build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the 1663 print as the TCP keys it, corrected where the page shows a keying
# slip. Witnesses: the 1663 scan the TCP was keyed from (archive.org
# bim_early-english-books-1641-1700_a-divine-cordial-_watson-thomas_1663, Kraken and Tesseract,
# work/a-divine-cordial/ocr-1663), the 1678 edition and the 1815 Philadelphia reprint (A Pious
# Selection) for letters the 1663 film lost; CCEL's text (cordial.ccel.witness.xml), a
# reworded 20th-century modernization, only as a check.

import layout

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True
SMALLCAPS = "smallcaps"
OPENING_SMALLCAPS = True
DROP_CAP_CASE = True
EXPAND_ETC = True

# The title page is the print's, not the edition's; the contents index the 1663 pages and the
# edition's own contents replace it.
SKIP_DIVISIONS = {"title_page", "table_of_contents"}

# Watson's sections (chapters 4 and 11) under their chapter.
DIV_LEVELS = {"section": 3}

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV", "XV", "XVI"]

# The book prints four parts, each opening with its title over its first chapter.
PARTS = {1: "A Divine Cordial", 7: "The Breathings of Love", 11: "Effectual Calling",
         15: "God’s Eternal Purpose"}


def LAYOUT(root):
    """Watson's epistle to the reader, then the sixteen chapters, one file each, the printed
    chapter head ("CHAP. III. Shewing that ...") set under the edition's title."""
    divs = layout.top_divs(root)
    files = [{"file": "to-the-reader.typ", "title": "To the Reader",
              "parts": layout.sections(next(d for d in divs if d.get("type") == "to_the_reader"))}]
    chapters = [d for d in divs if d.get("type") == "chapter"]
    assert [d.get("n") for d in chapters] == [str(k) for k in range(1, 17)]
    for k, div in enumerate(chapters, 1):
        sub = div.findall(f"{T}head")[-1]
        files.append({"file": f"chapter-{k:02d}.typ", "title": f"Chapter {ROMAN[k - 1]}",
                      "subtitle": sub, "part": PARTS.get(k),
                      "parts": layout.sections(div)})
    return files


# Macron abbreviations default to a suppressed "n"; these document-order indices expand to "m"
# ("bonū hominem", a Latin note). Index 1, "free-gracē" (p. 153), is no abbreviation: the 1663
# page (scan 161) has "free-grace:", the colon's upper dot set high; the reading text has "grace".
MACRON_M = {0}

# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "A Divine Cordial", "author": "Thomas Watson",
        "file": "a-divine-cordial.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "toc_depth": 3,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["a-divine-cordial.typ"]
