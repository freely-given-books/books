# Editorial settings for John Bunyan, Grace Abounding to the Chief of Sinners,
# from CCEL (https://www.ccel.org/ccel/b/bunyan/grace.xml), kept untouched in
# grace.thml.xml. Read by build_tei.py, tei_extract.py and ./fgb.
#
# CCEL's text is Bunyan's enlarged text (the later editions, to 1688). Witness:
# the 1666 first edition, EEBO-TCP A30143 (A30143.witness.xml, untouched),
# about 7,000 words shorter. drift.py compares the two
# (source/witness-report.md).

import layout

# A modern text: the early-modern spelling and case rules stay off.
MODERNIZE = False
TYPOGRAPHY = True
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks

# CCEL's title page, contents and scripture index are its own apparatus.
SKIP_DIVISIONS = {"contents", "index", "titlePage"}

FILES = [("ccel-iii", "preface.typ", "A Preface, or Brief Account of the Publishing of This Work"),
         ("ccel-iv", "relation.typ", "Grace Abounding to the Chief of Sinners"),
         ("ccel-v", "call-to-the-ministry.typ",
          "A Brief Account of the Author’s Call to the Work of the Ministry"),
         ("ccel-vi", "imprisonment.typ", "A Brief Account of the Author’s Imprisonment"),
         ("ccel-vii", "conclusion.typ", "The Conclusion")]


T = "{http://www.tei-c.org/ns/1.0}"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"


def _by_id(root):
    return {d.get(XML_ID): d for d in layout.top_divs(root)}


def LAYOUT(root):
    """Bunyan's preface, the relation itself, his call to the ministry, his
    imprisonment and the conclusion, one file each."""
    by_id = _by_id(root)
    files = [{"file": f, "title": t, "parts": layout.sections(by_id[i])} for i, f, t in FILES]
    # the preface's dedication, a printed head, set under its title
    files[0]["subtitle"] = next(h for h in by_id["ccel-iii"].iter(f"{T}head")
                                if h.get(XML_ID) == "ccel-iii-p0.3")
    return files


def SKIP_BLOCKS(root):
    """CCEL's "Publisher's Foreword": a modern biography of Bunyan, not his."""
    return [_by_id(root)["ccel-ii"]]


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "Grace Abounding to the Chief of Sinners", "author": "John Bunyan",
        "file": "grace-abounding.epub", "front": "ebook-front.html",
        "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["grace-abounding.typ"]
