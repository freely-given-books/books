# Editorial settings for John Calvin, Institutes of the Christian Religion,
# Henry Beveridge's translation (Calvin Translation Society, Edinburgh,
# 1845), from CCEL (https://www.ccel.org/ccel/c/calvin/institutes.xml),
# kept untouched in institutes.thml.xml. CCEL keyed it from Eerdmans' 1953
# reprint. Read by build_tei.py, tei_extract.py and ./fgb.
#
# Six volumes: Books I and II one each, Book III and Book IV two each.
# The edition keeps Calvin's own prefaces and leaves out the rest of the
# reprint's apparatus (the editor's call, 2026-10-11): John Murray's
# introduction (1953, still in copyright), Norton's 1581 prefaces, the
# tables and indexes keyed to the 1953 pages, Olevian's "Method and
# Arrangement", the general index of chapters, and the hundred Aphorisms.

import layout

# A modern text: the early-modern spelling and case rules stay off.
MODERNIZE = False
TYPOGRAPHY = True
QUOTE_BLOCK = True       # the fgbooks template sets #quote as a block, no marks
SMALLCAPS = "smallcaps"

T = "{http://www.tei-c.org/ns/1.0}"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"
ROMAN = ["I", "II", "III", "IV"]

# CCEL's ids: ii is the prefatory material, iii-vi Books I-IV (in each the
# first section is the Argument, then the chapters), vii the Aphorisms,
# viii the indexes.
PREFACES = [("ccel-ii.viii", "prefatory-address", "Prefatory Address to King Francis"),
            ("ccel-ii.ix", "epistle-1539", "Epistle to the Reader (1539)"),
            ("ccel-ii.x", "subject-1545", "Subject of the Present Work (1545)"),
            ("ccel-ii.xi", "epistle-1559", "Epistle to the Reader (1559)")]
BOOKS = ["ccel-iii", "ccel-iv", "ccel-v", "ccel-vi"]
BOOK_TITLES = ["Book First: Of the Knowledge of God the Creator",
               "Book Second: Of the Knowledge of God the Redeemer, in Christ",
               "Book Third: The Mode of Obtaining the Grace of Christ",
               "Book Fourth: Of the Holy Catholic Church"]
# (book, first chapter, last chapter) per volume; chapter 0 is the Argument
VOLUMES = [(1, 0, 18), (2, 0, 17), (3, 0, 10), (3, 11, 25), (4, 0, 13), (4, 14, 20)]

SKIP_DIVISIONS = {"contents", "index", "titlePage"}


def _ids(root):
    return {d.get(XML_ID): d for d in root.iter(T + "div")}


def _chapter_title(div):
    """The chapter's printed title: its second head, under "CHAPTER 2."
    ("WHAT IT IS TO KNOW GOD,—TENDENCY OF THIS KNOWLEDGE.")."""
    heads = [c for c in div if c.tag == T + "head"]
    # CCEL left Book I chapter 7 unmarked: its title is a plain paragraph
    return heads[1] if len(heads) > 1 else next(c for c in div if c.tag == T + "p")


SMALL = {"a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "into",
         "nor", "of", "on", "or", "the", "to", "with", "which", "who", "that"}
# The edition's short titles (contents and running heads), by (book, chapter),
# where the first clause of the printed title is too long for a running head;
# each in Beveridge's own words.
SHORT = {
    (1, 4): "The Knowledge of God Stifled or Corrupted",
    (1, 5): "The Knowledge of God Conspicuous in the Creation",
    (1, 6): "The Need of Scripture as a Guide and Teacher",
    (1, 7): "The Testimony of the Spirit Necessary to Scripture",
    (1, 8): "The Credibility of Scripture Sufficiently Proved",
    (1, 9): "Fanatics Who Substitute Revelations for Scripture",
    (1, 10): "The True God Opposed to the Gods of the Heathen",
    (1, 12): "God Distinguished from Idols",
    (1, 13): "The Unity of the Divine Essence in Three Persons",
    (1, 14): "The True God Distinguished in the Creation",
    (1, 16): "The World Still Cherished and Protected by God",
    (1, 18): "The Instrumentality of the Wicked Employed by God",
    (2, 1): "The Fall and Revolt of Adam",
    (2, 3): "Every Thing from the Corrupt Nature of Man Damnable",
    (2, 5): "The Arguments for Free Will Refuted",
    (2, 7): "The Law Given to Keep Alive the Hope of Salvation",
    (2, 9): "Christ Known Under the Law, Manifested Under the Gospel",
    (2, 12): "Christ Behoved to Become Man",
    (2, 16): "How Christ Performed the Office of Redeemer",
    (2, 17): "Christ Rightly Said to Have Merited Grace for Us",
    (3, 1): "The Benefits of Christ by the Secret Operation of the Spirit",
    (3, 4): "Penitence as Explained by the Schoolmen",
    (3, 12): "Contemplating the Judgment-Seat of God",
    (3, 15): "The Boasted Merit of Works",
    (3, 16): "Calumnies Against This Doctrine Refuted",
    (3, 21): "Of the Eternal Election",
    (3, 23): "Calumnies Against Election Refuted",
    (4, 4): "Of the State of the Primitive Church",
    (4, 5): "The Ancient Government Corrupted by the Papacy",
    (4, 7): "The Beginning and Rise of the Romish Papacy",
    (4, 11): "Of the Jurisdiction of the Church",
    (4, 12): "Of the Discipline of the Church",
}


def _short(book, n, head):
    """The first clause of a printed chapter title, in title case:
    "THE KNOWLEDGE OF GOD AND OF OURSELVES MUTUALLY CONNECTED. —NATURE..."
    -> "The Knowledge of God and of Ourselves Mutually Connected"."""
    if (book, n) in SHORT:
        return SHORT[(book, n)]
    import re
    import copy
    head = copy.deepcopy(head)
    for note in list(head.iter(T + "note")):    # a footnote is not the title
        note.getparent().remove(note)
    for ch in list(head.iter(T + "choice")):    # the edition's reading, not both
        reg = ch.find(T + "reg")                # (the editor's comes first)
        keep = "".join(reg.itertext()) if reg is not None else "".join(ch.itertext())
        for k in list(ch):
            ch.remove(k)
        ch.text = keep
    text = re.split(r"\s*(?:—|\.\s|\.$|;)", " ".join("".join(head.itertext()).split()))[0]
    text = text.rstrip(".")
    words = text.lower().split()
    return " ".join(w if i and w in SMALL else w[:1].upper() + w[1:]
                    for i, w in enumerate(words)).rstrip(",")


def LAYOUT(root):
    """Calvin's prefaces at the head of volume 1, then each Book's Argument
    and chapters, one file each, in six volume folders."""
    ids = _ids(root)
    files = []
    for v, (b, first, last) in enumerate(VOLUMES, start=1):
        d = f"vol-{v}"
        if v == 1:
            for i, (cid, name, title) in enumerate(PREFACES, start=1):
                files.append({"file": f"{d}/0{i}-{name}.typ", "title": title,
                              "parts": layout.sections(ids[cid])})
        chapters = [c for c in ids[BOOKS[b - 1]] if c.tag == T + "div"]
        for n in range(first, last + 1):
            div = chapters[n]
            book = f"Book {ROMAN[b - 1]}"
            if n == 0:
                f = {"file": f"{d}/book-{b}-argument.typ", "title": "Argument",
                     "short": "Argument", "parts": layout.sections(div)}
            else:
                head = _chapter_title(div)
                f = {"file": f"{d}/book-{b}-chapter-{n:02d}.typ", "title": f"Chapter {n}",
                     "short": f"Chapter {n}: {_short(b, n, head)}", "subtitle": head,
                     "parts": [p for p in layout.sections(div) if p is not head]}
            if n == first:
                f["part"] = BOOK_TITLES[b - 1] + ("" if first == 0 else " (continued)")
            files.append(f)
    return files


def SKIP_BLOCKS(root):
    """The reprint's apparatus this edition leaves out (above), with the
    1561 title page reprinted at the head of it."""
    ids = _ids(root)
    keep = {cid for cid, _, _ in PREFACES}
    pre = [d for d in ids["ccel-ii"] if d.tag == T + "div" and d.get(XML_ID) not in keep]
    # its heads and loose lines (the 1561 title page Norton's edition carried)
    loose = [c for c in ids["ccel-ii"] if isinstance(c.tag, str) and c.tag != T + "div"]
    return pre + loose + [ids["ccel-vii"]]

# ./fgb epub / pdf / page / build (paths from the book folder); one ebook
# per volume, as printed. The book files are written by make_volumes.py.
EPUB = {"title": "Institutes of the Christian Religion", "author": "John Calvin",
        "file": "institutes.epub", "cover": "cover-vol-1.typ",
        "front": "ebook-front-vol-1.html",
        "css": ["../../resources/css/ebook.css", "ebook-override.css"],
        "toc_depth": 3,
        "volumes": [
            {"files": [f"vol-{n}/"],
             "title": f"Institutes of the Christian Religion, Volume {r}",
             "file": f"institutes-vol-{n}.epub", "cover": f"cover-vol-{n}.typ",
             "front": f"ebook-front-vol-{n}.html"}
            for n, r in enumerate(["I", "II", "III", "IV", "V", "VI"], start=1)]}
PRINT = [f"institutes-vol-{n}.typ" for n in range(1, 7)]
SIDE_BY_SIDE = {"split": [f"vol-{n}/" for n in range(1, 7)]}
