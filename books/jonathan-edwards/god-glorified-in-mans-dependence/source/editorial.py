# Editorial settings for Jonathan Edwards, God Glorified in the Work of Redemption, by the
# Greatness of Man's Dependance upon Him (Boston, 1731), his first published sermon, preached on
# the public lecture in Boston, July 8, 1731. Read by build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the only printing in Edwards's lifetime (Boston: S. Kneeland and T. Green, for
# D. Henchman, 1731; Evans 3415) as Evans-TCP N02859 keys it, kept untouched in N02859.tcp.xml
# (EDITION-RULES 1). No scan of the 1731 printing is free to use; CCEL's text (the Worcester line)
# is the witness. The TCP has no gaps.

import layout
import runpy as _runpy
from pathlib import Path

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True
SMALLCAPS = "smallcaps"
# the opening word in small capitals, numerals not
OPENING_SMALLCAPS = "words"
# a decorated initial and its word printed in capitals ("THERE is") set as a word (There)
DROP_CAP_CASE = True
# Religious Affections' list (Edwards's capitalized nouns, cased from CCEL)
LOWERCASE_COMMON_NOUNS = _runpy.run_path(str(Path(__file__).parent / "nouns.py"))["LOWERCASE_COMMON_NOUNS"]
# A quotation's first word (an italic run of 5 words or more) keeps its printed capital.
QUOTE_START_CASE = True
ITALIC_SENTENCE_QUIRK = False

# The half title and title page are the print's (EDITION-RULES 6).
SKIP_DIVISIONS = {"half_title", "title_page"}


def LAYOUT(root):
    """The ministers' preface, then the sermon in one file, its USE a heading of the file."""
    divs = {d.get("type"): d for d in root.iter(f"{T}div")}
    return [{"file": "to-the-reader.typ", "title": "To the Reader",
             "parts": layout.sections(divs["to_the_reader"])},
            {"file": "sermon.typ", "title": "God Glorified in Man's Dependence",
             "parts": layout.sections(divs["sermon"])}]


DIV_LEVELS = {"application": 2}
OUTLINE_MARKS = True

EPUB = {"title": "God Glorified in Man's Dependence", "author": "Jonathan Edwards",
        "file": "god-glorified-in-mans-dependence.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["god-glorified-in-mans-dependence.typ"]
