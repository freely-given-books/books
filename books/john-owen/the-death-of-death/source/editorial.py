# Editorial settings for John Owen, The Death of Death in the Death of
# Christ (Salus Electorum, Sanguis Jesu, 1648), from CCEL
# (https://www.ccel.org/ccel/o/owen/deathofdeath.xml), kept untouched in
# deathofdeath.thml.xml. Read by build_tei.py, tei_extract.py and ./fgb.
#
# CCEL's text is Goold's (The Works of John Owen, vol. 10, 1850-53), keyed
# from Banner's 1967 reprint, with Goold's page breaks. Goold is the base;
# Owen's 1648 wording is restored where Goold changed it (his Scripture
# quotations brought to the KJV, words in his prose), Goold's corrected
# classical quotations and light modernizing ("namely" for "viz.") stand.
# Witnesses (SOURCES.md): Goold's 1850 printing and the 1648 first edition,
# both scans on archive.org; Monergism and sermonindex, Goold's text again.

import layout

# A modern text: the early-modern spelling and case rules stay off.
MODERNIZE = False
TYPOGRAPHY = True
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks
SMALLCAPS = "smallcaps"  # Goold's small capitals; Libertinus has real ones

# CCEL's title page and indexes are its own apparatus.
SKIP_DIVISIONS = {"contents", "index", "titlePage"}

T = "{http://www.tei-c.org/ns/1.0}"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]

# CCEL's ids: i.iii the epistle dedicatory, i.iv the attestations, i.v To
# the Reader, i.vii-i.x Books I-IV, i.xi the appendices.
PREFACES = [("ccel-i.iii", "epistle-dedicatory", "The Epistle Dedicatory"),
            ("ccel-i.iv", "attestations", "Two Attestations"),
            ("ccel-i.v", "to-the-reader", "To the Reader")]
BOOKS = ["ccel-i.vii", "ccel-i.viii", "ccel-i.ix", "ccel-i.x"]
APPENDICES = [("ccel-i.xi.i", "appendix-1-testimonies", "Some Few Testimonies of the Ancients",
               "Testimonies of the Ancients"),
              ("ccel-i.xi.ii", "appendix-2-sprigge", "An Appendix upon Mr Sprigge's Book",
               "Appendix on Mr Sprigge")]


def _ids(root):
    return {d.get(XML_ID): d for d in root.iter(T + "div")}


def LAYOUT(root):
    """Owen's prefaces, the four Books a chapter to a file, the two
    appendices."""
    ids = _ids(root)
    files = [{"file": f"{name}.typ", "title": title, "parts": layout.sections(ids[cid])}
             for cid, name, title in PREFACES]
    for b, bid in enumerate(BOOKS, start=1):
        chapters = [c for c in ids[bid] if c.tag == T + "div"]
        for n, div in enumerate(chapters, start=1):
            f = {"file": f"book-{b}/chapter-{n:02d}.typ", "title": f"Chapter {ROMAN[n - 1]}",
                 "short": f"Book {ROMAN[b - 1]}, Chapter {ROMAN[n - 1]}",
                 "parts": layout.sections(div)}
            if n == 1:
                f["part"] = f"Book {ROMAN[b - 1]}"
            files.append(f)
    for k, (cid, name, title, short) in enumerate(APPENDICES):
        f = {"file": f"{name}.typ", "title": title, "short": short,
             "parts": layout.sections(ids[cid])}
        if k == 0:
            f["part"] = "Appendices"
        files.append(f)
    return files


def SKIP_BLOCKS(root):
    """Goold's prefatory note and Analysis (1850s, not Owen's), and CCEL's
    indexes (ccel-ii, titled "Indexes." so not taken for an index)."""
    ids = _ids(root)
    return [ids["ccel-i.ii"], ids["ccel-ii"]]


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "The Death of Death in the Death of Christ", "author": "John Owen",
        "file": "the-death-of-death.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "toc_depth": 3,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-death-of-death.typ"]

# Owen's antithesis at the end of Book IV (Goold p. 414: "Universalists" against
# "Scriptural Redemption", eight points each), set as two columns, point
# against point, as printed.
def PARALLEL_TABLES(root):
    ns = {"t": "http://www.tei-c.org/ns/1.0"}
    tables = root.xpath("//t:table", namespaces=ns)
    assert len(tables) == 2, len(tables)
    return [tables]
