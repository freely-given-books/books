"""
Editorial tables for Richard Sibbes, The Glorious Feast of the Gospel (London,
1650; EEBO-TCP A93248, untouched in A93248.tcp.xml). Read by build_tei.py,
tei_extract.py, tcp_structure.py and ./fgb.

The edition (chapters/typ) was finished before the TEI existed; the TEI is
built from it with --review, so every change it makes to the 1650 text
(modernized spelling and case, scripture references added, "Obs."/"Use"
labels, quotations set as blocks, lists) is an #editor decision.

Witness: Monergism's PDF (SDG reprint, (c) Monergism Books 2017; a check
only, its text is not used). drift.py compares it with the edition.
"""

import layout

ORDINALS = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh",
            "Eighth", "Ninth"]

# Not part of this edition (kept in the TEI as printed): the title page, the
# printed "Analyticall Table" of the sermons' contents and the alphabetical
# index, whose page numbers are the 1650 printing's.
SKIP_DIVISIONS = {"title_page", "table_of_contents", "index"}


def LAYOUT(root):
    """To the Reader, then one file per sermon (the printed heads are
    replaced by "The First Sermon" ...; the first is printed as "The
    Marriage Feast between Christ and his Church")."""
    divs = layout.top_divs(root)
    reader = next(d for d in divs if d.get("type") == "dedication")
    files = [{"file": "tothereader.typ", "title": "To The Reader",
              "parts": layout.sections(reader)}]
    for d in divs:
        if d.get("type") == "sermon":
            n = int(d.get("n"))
            files.append({"file": f"chapter{n}.typ",
                          "title": f"The {ORDINALS[n - 1]} Sermon",
                          "parts": layout.sections(d)})
    return files


# Illegible print, by gap index (build_tei.py --list): (letters, certainty,
# evidence). Monergism's reprint of this 1650 text is the second witness.
# Left open: the Greek (5-9; the edition's own readings stand in the text),
# a blotted marginal numeral (10) and "these have ha• day" (18; both the
# edition and Monergism read "have a day", which leaves the letters unknown).
GAP_FIXES = {
    1: ("ra", "high", "Pa[ra]dise: Rev. 2:7 'the midst of the paradise of God'; "
        "Monergism 'in the midst of the Paradise of God'"),
    2: ("e", "high", "happineſſ[e]: Monergism 'an excellent treatise of happiness'"),
    3: ("ing", "high", "the K[ing] answered him: 'presenting it unto a great King'; "
        "Monergism 'the King answered him'"),
    4: ("us", "medium", "doe not anſwer [us] I am not now at leiſure: Monergism "
        "'do not answer us, \"I am not now at leisure.\"'"),
    11: ("t", "high", "Aquavitae [t]o the ſoule: Monergism 'Aqua vita to the soul'"),
    12: ("ſ", "high", "The Apoſtle Peter [ſ]aith: Monergism 'The Apostle Peter saith'"),
    13: ("e", "high", "as they ar[e] (margin): the text beside it, 'Things shall be "
         "known to be as they are'"),
    14: ("r", "high", "the Chu[r]ch (margin)"),
    15: ("G", "high", "to be of [G]od (margin)"),
    17: ("ſ", "high", "Beg of God to [ſ]eale to our ſoules: Monergism 'Beg of God "
         "to seal to our souls'"),
}

# Lists keep Typst's own numbering ("1."); a list numbered otherwise (To the
# Reader's "I.", the "a)" list in the third sermon) carries it in the TEI.
TYPST_ENUM = None

# Shown under "Please check" at the top of review-report.md.
REPORT_NOTES = [
    "chapter3.typ: #par(first-line-indent: 0pt)[There be four things in sight:] "
    "is layout, not text, so it is not stored in the TEI; keep it in chapters/typ.",
    "The analytical table and the alphabetical index are in the TEI as printed, "
    "but not in this edition.",
]

# ./fgb epub / pdf / page (paths from the book folder)
EPUB = {"title": "The Glorious Feast of the Gospel", "author": "Richard Sibbes",
        "file": "the-glorious-feast-of-the-gospel.epub", "front": "ebook-front.html",
        "cover": "cover.jpg",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-glorious-feast-of-the-gospel.typ"]
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks
COVERS = ["full_cover.typ"]   # the Lulu wrap (its spine follows the page count)
