# Editorial settings for The 1689 Baptist Confession of Faith, with the
# Baptist Catechism (1695) and An Orthodox Catechism (1680). Read by
# build_tei.py, tei_extract.py and ./fgb.
#
# The text is SVRBC's symbolics-data, laid out as ThML by make_thml.py
# (lbcf1689.thml.xml), so the pipeline reads it as it reads a CCEL text. It is
# the text this edition prints, on its own: no other copy is compared with it.
# The confession's preface and closing statement are our own transcription
# (transcription/).
#
# Each confession paragraph and each catechism question and answer is a
# speech: "Paragraph 1:", "Question 1:", "Answer:" (SPEECH_BLOCKS), and each
# Scripture proof a note after the words it proves. The book's proofs.typ
# sets them as the book always has: the label in bold, the proofs as a
# numbered list after the paragraph or answer.

import layout

# A modern text: the early-modern spelling and case rules stay off.
MODERNIZE = False
TYPOGRAPHY = True

SMALLCAPS = "smallcaps"
SPEECH_BLOCKS = True
# every chapter file is two folders down (chapters/typ/<part>/<file>.typ)
TYPST_PREAMBLE = '#import "../../../proofs.typ": speech, footnote'

XML_ID = "{http://www.w3.org/XML/1998/namespace}id"


def LAYOUT(root):
    """The confession (its preface, 32 chapters, the closing statement), the
    Baptist Catechism in one file, An Orthodox Catechism (its preface and six
    sections). File titles are the data's; print sets the part headings."""
    by_id = {d.get(XML_ID): d for d in layout.top_divs(root)}

    def f(file, key, title, part=None):
        return {"file": file, "title": title, "part": part,
                "parts": layout.sections(by_id[f"ccel-{key}"])}

    def head(key):
        return "".join(by_id[f"ccel-{key}"].find(f"{layout.T}head").itertext())

    files = [f("confession/00-preface.typ", "lbcf-preface", "The Preface",
               part="The Baptist Confession")]
    files += [f(f"confession/chapter-{n:02}.typ", f"lbcf-{n:02}", head(f"lbcf-{n:02}"))
              for n in range(1, 33)]
    files.append(f("confession/33-closing.typ", "lbcf-closing",
                   "Ending Statement and Signatories"))
    files.append(f("baptist-catechism/questions.typ", "bc1695", None,
                   part="The Baptist Catechism"))
    files.append(f("orthodox-catechism/00-preface.typ", "aoc-preface", "The Preface",
                   part="An Orthodox Catechism"))
    files += [f(f"orthodox-catechism/section-{n}.typ", f"aoc-{n:02}", head(f"aoc-{n:02}"))
              for n in range(1, 7)]
    return files


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "The 1689 Baptist Confession of Faith: With Catechisms",
        "author": "Particular Baptist Churches",
        "file": "1689-baptist-confession.epub", "front": "ebook-front.html",
        "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["1689-baptist-confession.typ"]
