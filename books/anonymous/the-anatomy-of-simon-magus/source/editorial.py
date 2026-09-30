"""
Editorial tables for The Anatomy of Simon Magus (EEBO-TCP A25330), loaded
by scripts/tei/build_tei.py and scripts/tei/tei_extract.py (both look for
editorial.py next to the TCP/TEI file). Every name is optional.

The edition (chapters/typ) was finished before the TEI existed; the TEI was
then built from it with --review, so every change it makes to the 1700 text
(modernized grammar, translations of the Latin, notes rewritten and moved,
italics, paragraphing) is recorded as an #editor decision.
"""

# No macron abbreviations in this printing, so no MACRON_M.

# Chapter files open with the book's own heading macro (common.typ), which
# takes the long title and the short one used in the running heads.
TYPST_PREAMBLE = '#import "../../common.typ": chapter'
TYPST_HEADING = "#chapter[{title}][{short}]"

# Printed divisions this edition leaves out (kept in the TEI as printed).
SKIP_DIVISIONS = {"table_of_contents", "publishers_advertisement"}

# Shown under "Please check" at the top of review-report.md.
REPORT_NOTES = [
    "chapters/typ also holds foreword.typ and abbreviations.typ: modern "
    "matter that is not in the 1700 text, so it is not in the TEI.",
    "The table of contents and the publisher's advertisement are in the TEI "
    "(as printed) but are not part of this edition.",
]
