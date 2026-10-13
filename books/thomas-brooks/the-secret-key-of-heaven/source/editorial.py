"""
Editorial tables for Thomas Brooks, The Privie Key of Heaven (London, 1665;
EEBO-TCP A29703, untouched in A29703.tcp.xml), published here as The Secret
Key of Heaven. Read by build_tei.py, tei_extract.py, tcp_structure.py and
./fgb.

The edition (chapters/typ) was finished before the TEI existed; the TEI is
built from it with --review, so every change it makes to the 1665 text is
an #editor decision. Its headings are its own.
"""

import layout

T = "{http://www.tei-c.org/ns/1.0}"

ARGUMENTS = [
    '1. The Most Eminent Saints in Private Prayer',
    '2. Christ Much Exercised Himself in Secret Prayer',
    '3. Secret Prayer Distinguishes You from Hypocrites',
    '4. In Secret We May Freely Unbosom Our Souls to God',
    '5. Secret Duties Shall Have Open Rewards',
    '6. God Lets Out Himself Most to His People in Secret',
    '7. This Life Is the Only Time for Private Prayer',
    '8. The Great Prevalency of Secret Prayer',
    '9. Secret Duties Are the Most Soul-Enriching',
    '10. All Christians Have Their Secret Sins',
    '11. Christ Delights in His People’s Secret Prayers',
    '12. God Hath Chosen You to Reveal His Secrets To',
    '13. Private Prayer in Times of Great Straits and Trials',
    '14. God Is Omnipresent',
    '15. He That Neglects the Closet Is Neglected in Public',
    '16. The Times Wherein We Live Call for Secret Prayer',
    '17. Your Relations to the Lord Call for Secret Prayer',
    '18. God’s Special Mark on Those That Pray in Secret',
    '19. Satan Is a Very Great Enemy to Secret Prayer',
    '20. You Are the Lord’s Secret Ones, His Hidden Ones',
]
APPLICATION = [
    '1. The Use and Application of All',
    '2. The Main Objections Against Closet Prayer Answered',
    '3. Advice and Counsel in Eleven Particulars',
    '4. Means, Rules, and Directions',
    '5. Other Things to Apply Yourselves To',
]


def _blocks(div):
    return [c for c in div if isinstance(c.tag, str) and layout.local(c) not in ("pb", "head")]


def _printed(el):
    """The printed text of an element: readings of the edition left out."""
    out = [el.text or ""]
    for c in el:
        if isinstance(c.tag, str) and layout.local(c) not in ("reg", "expan", "note"):
            out.append(_printed(c))
        out.append(c.tail or "")
    return "".join(out)


def _cut(blocks, text, last=False):
    """Index of the block whose printed text starts with `text` (cut by text,
    not position, so headings the edition inserts do not move it)."""
    hits = [i for i, b in enumerate(blocks)
            if layout.local(b) != "label" and " ".join(_printed(b).split()).startswith(text)]
    return hits[-1] if last else hits[0]


def _divs(root):
    d = layout.top_divs(root)
    by = {}
    for x in d:
        by.setdefault(x.get("type"), []).append(x)
    return by


def _preface(root):
    ded = _blocks(_divs(root)["dedication"][0])
    return ded, _cut(ded, "Dear Friends, the following")


def LAYOUT(root):
    """The end of the epistle dedicatory as the Preface; To the Reader; the
    discourse's opening (text and doctrine) as the Introduction; the twenty
    arguments; the application in five files (the printed section 1 ends
    with the first objection, which opens file 2; section 4 is cut at "And
    as you must take heed of these five things")."""
    by = _divs(root)
    ded, k = _preface(root)
    files = [{"file": "chapter-01.typ", "title": "Preface", "parts": ded[k:]},
             {"file": "chapter-02.typ", "title": "To the Reader",
              "parts": layout.sections(by["to_the_reader"][0])},
             {"file": "chapter-03.typ", "title": "Introduction",
              "parts": layout.sections(by["doctrine"][0], 1, 0)}]
    args = [d for d in by["doctrine"][0] if isinstance(d.tag, str) and d.get("type") == "argument"]
    for i, d in enumerate(args):
        files.append({"file": f"argument-{i + 1:02d}.typ", "title": ARGUMENTS[i],
                      "parts": layout.sections(d),
                      "part": "Twenty Arguments for Private Prayer" if i == 0 else None})
    s1, s2, s3, s4 = (_blocks(x) for x in by["section"])
    c1 = _cut(s1, "Objection", last=True)
    c4 = _cut(s4, "And as you mu")
    parts = [s1[:c1], s1[c1:] + s2, s3, s4[:c4], s4[c4:]]
    for i, p in enumerate(parts):
        files.append({"file": f"application-{i + 1:02d}.typ", "title": APPLICATION[i],
                      "parts": p, "part": "Application" if i == 0 else None})
    return files


def SKIP_BLOCKS(root):
    """The epistle dedicatory up to its last paragraph (the twenty lessons
    of the rod, i.e. the plague of 1665), left out of this edition."""
    ded, k = _preface(root)
    return ded[:k]


# The title page, the publisher's list of Brooks's books, the errata and the
# printed table of heads (page numbers of 1665) are not part of this edition.
SKIP_DIVISIONS = {"title_page", "publishers_advertisement", "errata", "index"}

TYPST_ENUM = None

REPORT_NOTES = [
    "chapter-03.typ: the introduction's text is an epigraph and its Doctrine an "
    "inset block (q[@rend='inset']), both in the TEI; headings are kept with "
    "their text by the template (fgbooks 0.5.4), not by page breaks.",
    "Most of the epistle dedicatory, the publisher's list, the errata and the "
    "printed table of heads are in the TEI as printed but not in this edition.",
]

# ./fgb epub / pdf / page (paths from the book folder)
EPUB = {"title": "The Secret Key of Heaven", "author": "Thomas Brooks",
        "file": "the-secret-key-of-heaven.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "toc_depth": 4,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-secret-key-of-heaven.typ"]
QUOTE_BLOCK = True

# The headings below each file title are this edition's own (the 1665 print
# has none): label[@type="head"] in the TEI, not printed text.
EDITION_HEADINGS = True

# Salutations and signatures are plain paragraphs, which the edition runs on
# into the text or sets on two lines.
CLOSER_PLAIN = True
