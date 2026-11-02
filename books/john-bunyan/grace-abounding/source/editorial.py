# Editorial settings for John Bunyan, Grace Abounding to the Chief of Sinners, from our own
# transcription of the sixth edition (London: Nath. Ponder, 1688), the last printed in Bunyan's
# lifetime: grace-abounding-1688.tcp.xml (Kraken OCR of the British Library copy, every
# disagreement with the other witnesses read on the page image; the words the film lost in the
# gutter supplied from the 1692 copy, the 1666 first edition or the RTS text). Read by
# build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the 1688 print as printed (its spelling, its section numbers, its italics);
# the reading text keeps the editor's rule of 2026-10-26 (Bunyan's 1688 wording, modern
# spelling; the passages 1688 cut kept from 1666: source/witness-report.md) and the print's
# italics (the editor, 2026-11-01). Witnesses: CCEL's text (grace.ccel.witness.xml, the
# previous edition's source) and the 1666 first edition, EEBO-TCP A30143 (A30143.witness.xml).

import layout

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks
SMALLCAPS = "smallcaps"
DROP_CAP_CASE = True     # "IN this my relation", "AND now I am speaking": the print's drop capitals
EXPAND_ETC = True

# The title page is the print's, not the edition's.
SKIP_DIVISIONS = {"title_page"}

FILES = [("preface", "preface.typ", "A Preface, or Brief Account of the Publishing of This Work"),
         ("text", "relation.typ", "Grace Abounding to the Chief of Sinners"),
         ("part", "call-to-the-ministry.typ",
          "A Brief Account of the Author’s Call to the Work of the Ministry"),
         ("part", "imprisonment.typ", "A Brief Account of the Author’s Imprisonment"),
         ("conclusion", "conclusion.typ", "The Conclusion")]


def LAYOUT(root):
    """Bunyan's preface, the relation itself, his call to the ministry, his imprisonment and the
    conclusion, one file each; the preface's dedication, a printed head, set under its title."""
    divs = [d for d in layout.top_divs(root) if d.get("type") != "title_page"]
    files = []
    for d, (typ, f, t) in zip(divs, FILES):
        assert d.get("type") == typ, (d.get("type"), typ)
        files.append({"file": f, "title": t, "parts": layout.sections(d)})
    files[0]["subtitle"] = next(h for h in divs[0].iter(f"{T}head") if h.get("type") == "sub")
    return files


# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "Grace Abounding to the Chief of Sinners", "author": "John Bunyan",
        "file": "grace-abounding.epub", "front": "ebook-front.html",
        "cover": "cover.typ",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["grace-abounding.typ"]
