"""
Editorial tables for Thomas Brooks, Precious Remedies against Satans Devices
(London: M. Simmons for John Hancock, 1653, "The Second Edition Corrected
and Enlarged"; Wing B4954; EEBO-TCP A77614, untouched in A77614.tcp.xml;
the TCP header's edition date, 1658, is not the imprint's). Read by
build_tei.py, tei_extract.py, tcp_structure.py and ./fgb.

Witness: Monergism's PDF (from Grosart's Works of Thomas Brooks, vol. 1;
a check only, its text is not used).
"""

import layout

T = "{http://www.tei-c.org/ns/1.0}"

SIN = ["Presenting the Bait and Hiding the Hook",
       "Painting Sin with Virtue’s Colours",
       "Lessening Sin",
       "The Best Men’s Sins",
       "God as All Mercy",
       "Repentance Made Easy",
       "The Occasions of Sin",
       "The Outward Mercies of Vain Men",
       "The Crosses of the Saints",
       "Comparing Ourselves with Worse Men",
       "Error in the Judgment",
       "Wicked Company"]
DUTIES = ["The World in Its Best Dress",
          "The Dangers of Duty",
          "The Difficulty of Duty",
          "False Inferences from Christ’s Work",
          "The Fewness and Poverty of the Godly",
          "The Example of the World",
          "Vain Thoughts in Duty",
          "Resting in Performances"]
DOUBTING = ["Poring on Sin More than on the Saviour",
            "False Definitions of Grace",
            "Cross Providences",
            "Counterfeit Graces",
            "Conflict as in Hypocrites",
            "Lost Joy",
            "Relapses",
            "Temptations"]
RANKS = ["The Great: Self-Seeking",
         "The Great: Against the Saints",
         "The Learned and the Wise",
         "The Saints: Division",
         "The Ignorant"]
APPENDIX = ["The Greatness of Sin",
            "Unworthiness",
            "Want of Preparation",
            "Christ’s Unwillingness",
            "God’s Secret Decrees"]
PARTS = ["Part I. Devices to Draw the Soul into Sin",
         "Part II. Devices to Keep Souls from Holy Duties",
         "Part III. Devices to Keep Souls Doubting",
         "Part IV. Devices to Destroy All Ranks of Men",
         "Appendix. Five More Devices to Keep Souls from Christ"]


def _printed(el):
    """The printed text of an element: readings of the edition and margin
    notes left out."""
    out = [el.text or ""]
    for c in el:
        if isinstance(c.tag, str) and layout.local(c) not in ("reg", "expan", "note"):
            out.append(_printed(c))
        out.append(c.tail or "")
    return "".join(out)


def _text(el):
    """Printed text, long s as s and lower case, for matching."""
    return " ".join(_printed(el).replace("ſ", "s").split()).lower()


def _flat(div):
    """A division's blocks in reading order, its sub-divisions opened: each
    sub-division's printed head (a part of its own) and then its blocks.
    The division's own head is left to the caller."""
    out = []
    for c in div:
        if not isinstance(c.tag, str) or layout.local(c) in ("pb", "milestone"):
            continue
        if layout.local(c) == "head":
            continue
        if layout.local(c) == "div":
            out += c.findall(T + "head") + _flat(c)
        else:
            out.append(c)
    return out


def _cuts(blocks, starts):
    """Cut `blocks` before the first block (after the previous cut) whose
    printed text starts with each of `starts`: [before, file 1, file 2, ...]
    (cut by text, not position)."""
    out, k = [], 0
    for s in starts:
        j = next(i for i in range(k, len(blocks)) if _text(blocks[i]).startswith(s.lower()))
        out.append(blocks[k:j])
        k = j
    out.append(blocks[k:])
    return out


ORD = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
       "eighth"]


def LAYOUT(root):
    """The epistle dedicatory; To the Reader; the text opened and the point
    proved; the devices of the four parts and of the appendix, one file each
    (the device as printed, then its remedies); the propositions, the reasons
    and the use. In Part I each device is printed at the end of the division
    before it, so files are cut by printed text, the printed heads of the
    divisions ("Now the Remedies against this Device ...") kept as parts."""
    by = {}
    for d in layout.top_divs(root):
        by.setdefault(d.get("type"), []).append(d)
    p1, p2, p3, p4 = by["part"]
    app = by["appendix"][0]
    files = [{"file": "dedication.typ", "title": "The Epistle Dedicatory",
              "parts": layout.sections(by["dedication"][0])},
             {"file": "to-the-reader.typ", "title": "A Word to the Reader",
              "parts": layout.sections(by["to_the_reader"][0])}]

    # Part I: the text opened, then "Now the second thing ... his several
    # Devices"; each device opens "His first Device", "The second Device ...".
    b1 = _flat(p1)
    intro, *rest = _cuts(b1, ["Now the second thing that I am to shew you"])
    files.append({"file": "introduction.typ",
                  "title": "The Text Opened and the Point Proved",
                  "subtitle": p1.find(T + "head"), "parts": intro})
    lead, *sin = _cuts(rest[0], ["His first Device", "The second Device", "The third Device",
                                 "The fourth Device", "The fifth Device", "The sixt Device",
                                 "Now the seventh Device", "The eight Device",
                                 "The ninth Device", "The tenth Device",
                                 "The eleventh Device", "The twel"])
    sin[0] = lead + sin[0]
    for i, parts in enumerate(sin):
        files.append({"file": f"sin-{i + 1:02d}.typ", "title": f"{i + 1}. {SIN[i]}",
                      "parts": parts, "part": PARTS[0] if i == 0 else None})

    def part(div, names, stem, k, starts, subtitle=True):
        lead, *fs = _cuts(_flat(div), starts)
        fs[0] = lead + fs[0]
        out = []
        for i, parts in enumerate(fs):
            out.append({"file": f"{stem}-{i + 1:02d}.typ", "title": f"{i + 1}. {names[i]}",
                        "subtitle": div.find(T + "head") if i == 0 and subtitle else None,
                        "parts": parts, "part": PARTS[k] if i == 0 else None})
        return out

    files += part(p2, DUTIES, "duties", 1,
                  [f"The {ORD[i]} Device" for i in range(8)])
    files += part(p3, DOUBTING, "doubting", 2,
                  [f"The {ORD[i]} Device" for i in range(8)])
    b4 = _flat(p4)
    ranks, closing = _cuts(b4, ["And now to prevent Objections"])
    lead, *rk = _cuts(ranks, ["His first Device", "The second Device", "Secondly, Satan",
                              "Thirdly, Satan", "Lastly, as Satan"])
    rk[0] = lead + rk[0]
    for i, parts in enumerate(rk):
        files.append({"file": f"ranks-{i + 1:02d}.typ", "title": f"{i + 1}. {RANKS[i]}",
                      "subtitle": p4.find(T + "head") if i == 0 else None,
                      "parts": parts, "part": PARTS[3] if i == 0 else None})
    props, reasons, use = _cuts(closing, ["Now I shall come to the Reasons",
                                          "The use of the Point"])
    files += [{"file": "propositions.typ", "title": "Six Propositions Concerning Satan",
               "parts": props},
              {"file": "reasons.typ", "title": "The Reasons of the Point", "parts": reasons},
              {"file": "use.typ", "title": "The Use: Ten Helps Against All His Devices",
               "parts": use}]
    files += part(app, APPENDIX, "appendix", 4,
                  ["Now the first Device"] + [f"The {ORD[i]} Device" for i in range(1, 5)])
    return files


# Not part of this edition (kept in the TEI as printed): the title page, the
# printed table of contents (1653 page numbers), Caryll's imprimatur, the
# bookseller's catalogue and the errata.
SKIP_DIVISIONS = {"title_page", "table_of_contents", "imprimatur",
                  "publishers_advertisement", "errata"}

# A device or remedy head ("Now the Remedies against this Device of Satan
# are these.") is set as a bold paragraph, not a heading.
RUN_IN_DIVS = {"subpart"}

TYPST_ENUM = None

REPORT_NOTES = [
    "The title page, the printed table of contents, the imprimatur, the "
    "bookseller's catalogue and the errata are in the TEI as printed but not "
    "in this edition.",
]

# "IN the fifth Verse" under a decorated initial is set "In the fifth Verse".
DROP_CAP_CASE = True
# "&c." is written "etc.", as on the rest of the shelf.
EXPAND_ETC = True
# A sentence that opens after an italic quotation is capitalized.
ITALIC_SENTENCE_QUIRK = False

# ./fgb epub / pdf / page (paths from the book folder)
EPUB = {"title": "Precious Remedies Against Satan’s Devices", "author": "Thomas Brooks",
        "file": "precious-remedies-against-satans-devices.epub",
        "front": "ebook-front.html", "cover": "cover.typ", "toc_depth": 3,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["precious-remedies-against-satans-devices.typ"]
QUOTE_BLOCK = True

# Salutations and signatures are plain paragraphs, as in The Secret Key of
# Heaven.
CLOSER_PLAIN = True
