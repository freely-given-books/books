# Editorial settings for Charles Spurgeon, All of Grace (1886), from CCEL
# (https://www.ccel.org/ccel/s/spurgeon/grace.xml), kept untouched in
# grace.thml.xml. Read by build_tei.py, tei_extract.py and ./fgb.
# Second witness for readings: Monergism's 2015 PDF (CCEL's text with three
# typos corrected; see README.md).

# A modern text: the early-modern spelling and case rules stay off; CCEL's
# ASCII quotes and "--" are set as the print edition sets them.
MODERNIZE = False
TYPOGRAPHY = True
DASH = " \u2014 "           # the edition spaces its dashes

REPORT_NOTES = [
    "chapter-20.typ: the three centred appeals are centred in CCEL "
    "(p[@rend='center']), so the TEI sets them centred in print and ebook.",
]

# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "All of Grace", "author": "Charles Spurgeon",
        "file": "all-of-grace.epub", "front": "ebook-front.html", "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["all-of-grace.typ"]
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks
# Verse is set line by line, as CCEL breaks it ("line \\" in Typst, <br/> in
# the ebook): the hymns quoted in #quote blocks (2026-10-26; before, their
# lines ran together, "sacred thing; The Holy Ghost hath made him so").
VERSE_LINEBREAKS = True

# Small capitals (2026-10-26): the words CCEL has in capitals, each chapter's
# opening and a few emphasized lines, as the 1886 printing set them, and the
# lines the review emphasized the same way; before, they were set in full
# capitals. Printed words, with context; the bracketed words are in small
# capitals (colophon's SMALLCAPS_PHRASES).
SMALLCAPS = "smallcaps"
SMALLCAPS_PHRASES = [
    "[HE WHO SPOKE] and wrote",                               # ch. 1
    "[I HEARD A STORY]; I think",                             # 2
    "salvation is [all of grace], which",
    "[THIS MESSAGE] is for you",                              # 3
    "^[UNGODLY]$",
    "[A WONDERFUL THING] it is, this being",                  # 4
    "[I believe in the Forgiveness of Sins].",
    "Sins.\" [Do You]?",
    "[WE HAVE SEEN] the ungodly",                             # 5
    "[IN THIS PLACE] I would",                                # 6
    "[I THINK IT WELL] to turn",                              # 7
    "Think more of [Him] to whom",
    "[WHAT IS THIS FAITH] concerning",                        # 8
    "\"[He that believeth in Him hath everlasting life].\"",
    "[TO MAKE THE MATTER] of faith",                          # 9
    "[WHY IS FAITH SELECTED] as the channel",                 # 10
    "[AFTER THE ANXIOUS HEART] has",                          # 11
    "[HOW CAN WE OBTAIN] an increase",                        # 12
    "[YE MUST BE BORN AGAIN].\" This word",                  # 13
    "[CONTINUALLY] have I spoken",                            # 14
    "[IT IS CLEAR] from the text",                            # 15
    "^\"[BY GRACE ARE YE SAVED].\"$",
    "[TO RETURN] to the grand",                               # 16
    "^[Christ is all].$",
    "[A DARK FEAR] haunts",                                   # 17
    "[I WANT YOU TO NOTICE] the security",                    # 18
    "[THE HOPE] which filled",                                # 19
    "this little book, \"[all of grace]",
    "[IF MY READER] has not",                                 # 20
    "^[I beseech you],$",
    "^[Do not turn away from your Redeemer]!$",
    "[Reader, meet me in heaven]! Do not",
    "^[now or never]$",
    "Let it be [NOW];",
    "^[meet me in heaven].$",
]
