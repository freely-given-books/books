# Editorial settings for Charles Spurgeon, All of Grace (1886), from our own
# transcription of the 1886 New York printing (Robert Carter & Brothers,
# archive.org allofgraceearnes00spur), kept as ThML in grace.thml.xml so the
# pipeline reads it as it reads a CCEL text. Read by build_tei.py,
# tei_extract.py and ./fgb.
#
# The transcription is Kraken's OCR of every page (CATMuS-Print model),
# corrected where GLM-OCR, Tesseract, archive.org's OCR and CCEL's text
# outvote it and read on the page image where they split; paragraphs, verse,
# italics and small capitals follow the print. CCEL's text
# (grace.ccel.witness.xml, untouched), which rewords and drops passages, is a
# witness only. How it was made: SOURCES.md.

# A modern text: the early-modern spelling and case rules stay off; the
# transcription's straight quotes and dashes are set as the print edition sets them.
MODERNIZE = False
TYPOGRAPHY = True
DASH = " \u2014 "           # the edition spaces its dashes

REPORT_NOTES = [
    "chapter-20.typ: the three centred appeals are centred in the print "
    "(p[@rend='center']), so the TEI sets them centred in print and ebook.",
]

# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "All of Grace", "author": "Charles Spurgeon",
        "file": "all-of-grace.epub", "front": "ebook-front.html", "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["all-of-grace.typ"]
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks
# Verse is set line by line, as the print breaks it ("line \\" in Typst, <br/>
# in the ebook): the hymns quoted in #quote blocks.
VERSE_LINEBREAKS = True

# Small capitals as the 1886 print sets them (each chapter's opening words, a
# few emphasized lines), marked in the transcription (span.sc).
SMALLCAPS = "smallcaps"
