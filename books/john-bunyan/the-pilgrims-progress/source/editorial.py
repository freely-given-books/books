# Editorial settings for John Bunyan, The Pilgrim's Progress, Parts I and II,
# from CCEL (https://www.ccel.org/ccel/b/bunyan/pilgrim.xml; Logos's text of
# the 1853 Auburn edition), kept untouched in pilgrim.thml.xml. Read by
# build_tei.py, tei_extract.py and ./fgb.
#
# Witness: the 1678 first edition of Part I, EEBO-TCP A30170
# (A30170.witness.xml, untouched). It is not the master: CCEL's text carries
# Bunyan's later additions, which the first edition lacks. drift.py compares
# the two (source/witness-report.md). No TCP transcription of Part II exists.

import layout

# A modern text: the early-modern spelling and case rules stay off.
MODERNIZE = False
TYPOGRAPHY = True

# CCEL's contents page, index of scripture references and title page are its
# own apparatus, not the book's.
SKIP_DIVISIONS = {"contents", "index", "titlePage"}

# Verse is set line by line ("line \" in Typst, <br/> in the ebook), and
# CCEL's own line breaks are kept (the Author's Way signature): verse as an
# indented #quote block in the narrative, as plain stanzas in the sections
# that are all verse (the Apology, the Conclusion, the Author's Way).
VERSE_LINEBREAKS = True
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks

# CCEL's small capitals (the Author's Way's "Objection"/"answer" labels, Part
# Two's subtitle) are set bold: Liberation Serif has no small capitals, and
# Typst does not make them up.
SMALLCAPS = "strong"

STAGES = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH",
          "EIGHTH", "NINTH", "TENTH"]


def LAYOUT(root):
    """The Apology; Part One in ten stages and the Conclusion; Part Two's
    title, the Author's Way, To the Reader and eight stages. The PART ONE /
    PART TWO headings belong to the-pilgrims-progress.typ."""
    divs = layout.top_divs(root)
    by_id = {d.get("{http://www.w3.org/XML/1998/namespace}id"): d for d in divs}
    apology, part1, part2 = by_id["ccel-iii"], by_id["ccel-iv"], by_id["ccel-v"]
    files = [{"file": "apology.typ", "title": "The Author’s Apology For His Book",
              "parts": layout.sections(apology)}]
    subs = [c for c in part1 if layout.local(c) == "div"]
    for i, d in enumerate(subs[:10]):
        files.append({"file": f"part-1/stage-{i + 1:02d}.typ",
                      "title": f"THE {STAGES[i]} STAGE", "parts": layout.sections(d)})
    files.append({"file": "part-1/conclusion.typ", "title": "CONCLUSION",
                  "parts": layout.sections(subs[10])})
    subs = [c for c in part2 if layout.local(c) == "div"]
    files.append({"file": "part-2/title.typ", "title": None,
                  "parts": layout.sections(part2, 1, 0)})
    files.append({"file": "part-2/authors-way.typ", "title": "THE AUTHOR’S WAY",
                  "parts": layout.sections(subs[0])})
    files.append({"file": "part-2/to-the-reader.typ", "title": "TO THE READER",
                  "parts": layout.sections(subs[1])})
    for i, d in enumerate(subs[2:]):
        files.append({"file": f"part-2/stage-{i + 1:02d}.typ",
                      "title": f"THE {STAGES[i]} STAGE", "parts": layout.sections(d)})
    return files


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "The Pilgrim's Progress", "author": "John Bunyan",
        "file": "the-pilgrims-progress.epub", "front": "ebook-front.html",
        "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-pilgrims-progress.typ"]
