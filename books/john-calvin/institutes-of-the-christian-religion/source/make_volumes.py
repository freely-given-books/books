"""Write the six volumes' book files from editorial.py's LAYOUT: the print
book (institutes-vol-N.typ), its cover (cover-vol-N.typ) and its ebook front
page (ebook-front-vol-N.html), and for each volume in MODERN_VOLUMES its Modern
English edition's (institutes-vol-N-modern.typ, cover-vol-N-modern.typ,
ebook-front-vol-N-modern.html). Run it after changing the layout:

    colophon/.venv/bin/python books/john-calvin/institutes-of-the-christian-religion/source/make_volumes.py
"""

import re
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).parent
BOOK = HERE.parent
sys.path.insert(0, str(BOOK.parents[2] / "colophon"))
import sources  # noqa: E402

ED = runpy.run_path(str(HERE / "editorial.py"))
ROMAN = ["I", "II", "III", "IV", "V", "VI"]
# the template version the volume files import now (./fgb pins every book to
# the same one; a bump edits them all), so regenerating does not undo it
_m = re.search(r'#import "(@local/fgbooks:[\d.]+)"',
               (BOOK / "institutes-vol-1.typ").read_text(encoding="utf-8"))
TEMPLATE = _m.group(1) if _m else "@local/fgbooks:0.12.0"

SUBTITLES = [
    "Book First: Of the Knowledge of God the Creator",
    "Book Second: Of the Knowledge of God the Redeemer, in Christ",
    "Book Third, Chapters 1–10: The Mode of Obtaining the Grace of Christ",
    "Book Third, Chapters 11–25: Justification, Liberty, Prayer, Election",
    "Book Fourth, Chapters 1–13: Of the Holy Catholic Church",
    "Book Fourth, Chapters 14–20: The Sacraments and Civil Government",
]
BACK = [
    "Calvin's prefaces, among them the great address to King Francis, and the first book: how God is known as Creator, in his works and in Scripture; the Trinity; creation, man as first made, and providence.",
    "The second book: the fall and the bondage of the will; the law, given to lead to Christ; the Old Testament and the New; and Christ the Mediator, his person, his three offices, and the redemption he obtained.",
    "The third book begins: how the grace of Christ comes to us by the secret work of the Spirit; faith; regeneration and repentance; and the life of a Christian, self-denial, bearing the cross, and the use of this present life.",
    "The third book concluded: justification by faith; Christian liberty; prayer, with an exposition of the Lord's Prayer; eternal election; and the final resurrection.",
    "The fourth book begins: the true church and the false; its ministers and their office; the primitive church and the papacy; councils, laws, discipline, and vows.",
    "The fourth book concluded: the sacraments; baptism and the baptism of infants; the Lord's Supper and the mass; the five sacraments falsely so called; and civil government.",
]
EPIGRAPH = ("Our wisdom, in so far as it ought to be deemed true and solid wisdom, "
            "consists almost entirely of two parts: the knowledge of God and of ourselves.")
EPIGRAPH_SOURCE = "Institutes, I. i. 1"
SOURCE_NOTE = "Henry Beveridge's translation (Edinburgh, 1845), checked against the 1845 printing, with American spelling and printers' slips corrected."

# The Modern English edition (MODERN-ENGLISH-RULES.md): the same lines in its
# own words (the epigraph and back passage from chapters/modern), its note on
# Scripture and the plural "you", and its source paragraph
MODERN_EPIGRAPH = ("Our wisdom, insofar as it ought to be counted true and solid wisdom, "
                   "consists almost entirely of two parts: the knowledge of God and of ourselves.")
MODERN_SOURCE_NOTE = ("Henry Beveridge's translation (Edinburgh, 1845) in modern English, "
                      "checked against Calvin's Latin of 1559.")
MODERN_NOTE = ("Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own "
               "Bible where his argument rests on its wording; capitals for God in quotations "
               "(He, His) follow the BSB. “You{plus}” marks every plural “you” (the older “ye”); "
               "a plain “you” is singular or general.")
MODERN_BACK_WORDS = ("For just as the old, or those whose sight is weak, when any book, however "
                     "fine, is set before them, can see that something is written but can scarcely "
                     "make out two words together, yet with the help of glasses begin to read "
                     "distinctly, so Scripture gathers together the impressions of Deity that till "
                     "then lay confused in our minds, scatters the darkness, and shows us the true "
                     "God clearly.")


def volumes():
    # the TEI, so headings carry the edition's corrections (CHIEFLY, not
    # CCEL's BRIEFLY), as the chapters do
    root = sources.load(str(HERE / "institutes-of-the-christian-religion.tei.xml")).getroot()
    files = ED["LAYOUT"](root)
    out = [[] for _ in ED["VOLUMES"]]
    for f in files:
        out[int(f["file"].split("/")[0].split("-")[1]) - 1].append(f)
    return out


# Page fit (print_check's page warnings: a chapter ending on 1-4 lines, a note
# set off its marker's page): letter spacing a little tighter or looser on a
# file, per print book, (volume, modern) -> {file: tracking}, found by trying
PAGEFIT = {
    (1, False): {"01-prefatory-address.typ": "-0.01em", "book-1-chapter-12.typ": "-0.005em",
                 "book-1-chapter-17.typ": "0.005em"},
    (1, True): {"book-1-chapter-05.typ": "-0.005em", "book-1-chapter-09.typ": "-0.01em",
                "book-1-chapter-11.typ": "0.005em", "book-1-chapter-12.typ": "-0.005em"},
    (2, False): {"book-2-argument.typ": "-0.01em", "book-2-chapter-04.typ": "-0.01em", "book-2-chapter-05.typ": "-0.01em",
                 "book-2-chapter-06.typ": "-0.01em", "book-2-chapter-10.typ": "-0.01em", "book-2-chapter-16.typ": "0.005em"},
    (4, False): {"book-3-chapter-11.typ": "-0.01em", "book-3-chapter-20.typ": "-0.005em"},
    (5, False): {"book-4-chapter-12.typ": "-0.01em"},
    (6, False): {"book-4-chapter-20.typ": "-0.005em"},
}


def print_book(n, files, modern=False):
    fit = PAGEFIT.get((n, modern), {})
    head = ([f"// The Modern English edition of volume {n} (MODERN-ENGLISH-RULES.md): the same book as",
             f"// institutes-vol-{n}.typ, its text from chapters/modern/vol-{n}, paragraph for paragraph",
             f"// with chapters/typ/vol-{n}. Terms as source/modern-glossary.md."] if modern else [])
    edition = r" \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]" if modern else ""
    epigraph = MODERN_EPIGRAPH if modern else EPIGRAPH
    note = ["      #v(2em)",
            "      #text(size: 9pt)[" + MODERN_NOTE.format(plus="#super[+]") + "]"] if modern else []
    lines = head + [f'#import "{TEMPLATE}": *', "",
             "// GENERATED BY source/make_volumes.py -- edit that and editorial.py, not this file.",
             "//",
             "// 6x9 at 10.5pt, the trim for a large set (the editor, 2026-11-23): at 700,000",
             "// words the Institutes is six volumes of 220-350 pages.", "",
             "#show outline: set text(9.5pt)", "",
             "#show: book.with(",
             "  title: [Institutes of the Christian Religion],",
             f"  subtitle: [Volume {ROMAN[n - 1]} — {SUBTITLES[n - 1]}{edition}],",
             '  author: "John Calvin",',
             "  page-width: 6in, page-height: 9in,",
             "  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.0in),",
             "  // the Common Weal Press publisher's page, from the template",
             "  publishing-info: publisher-page(note: [",
             "    " + (MODERN_SOURCE_NOTE if modern else SOURCE_NOTE), "",
             f"    Volume {n} of six.",
             "  ]),",
             "  preface: [",
             "    #align(center + horizon)[",
             "      #text(size: 12pt)[",
             f"        _{epigraph}_", "",
             f"        — {EPIGRAPH_SOURCE}",
             "      ]", *note, "    ]", "  ]", ")", "",
             '#set text(font: "Libertinus Serif", size: 10.5pt)', ""]
    for f in files:
        if f.get("part"):
            lines += [f"= {f['part']}", ""]
        inc = f'#include "chapters/{"modern" if modern else "typ"}/{f["file"]}"'
        if f["file"].split("/", 1)[1] in fit:
            inc = ("// page fit (print_check's page warning): letter spacing adjusted\n"
                   f"#[\n  #set text(tracking: {fit[f['file'].split('/', 1)[1]]})\n  {inc}\n]")
        lines += [f"#metadata[{f.get('short') or f['title']}] <short>", inc, ""]
    (BOOK / f"institutes-vol-{n}{'-modern' if modern else ''}.typ").write_text("\n".join(lines))


# The covers: one set on scripts/set_cover.typ (its spine and back), with a
# front of their own: the title, the spectacles on an open book (art/
# vignette.png; Book I. vi. 1, Scripture as the glasses by which we read God
# clearly), this volume's line, the seal. The grounds step from sea-green to
# indigo through the six volumes, so the set shelves as one band of colour.
GROUNDS = ["#3E6E5C", "#336A6E", "#2D5B77", "#2E4C79", "#353F75", "#3A3363"]
# the seal's fountain and the name plate's lettering: each ground, darker
PAPERS = ["#22392F", "#1B3739", "#172F3D", "#18283F", "#1C213D", "#1E1A33"]
FRONTS = [
    ("One", "Of the Knowledge of God the Creator"),
    ("Two", "Of the Knowledge of God the Redeemer, in Christ"),
    ("Three", "The Mode of Obtaining the Grace of Christ, chapters 1–10"),
    ("Three", "Justification, Liberty, Prayer, Election, chapters 11–25"),
    ("Four", "Of the Holy Catholic Church, chapters 1–13"),
    ("Four", "The Sacraments and Civil Government, chapters 14–20"),
]
BACK_WORDS = ("For as the aged, or those whose sight is defective, when any book, "
              "however fair, is set before them, though they perceive that there is "
              "something written are scarcely able to make out two consecutive words, "
              "but, when aided by glasses, begin to read distinctly, so Scripture, "
              "gathering together the impressions of Deity, which, till then, lay "
              "confused in our minds, dissipates the darkness, and shows us the true "
              "God clearly.")
BACK_SOURCE = "Institutes, I. vi. 1"
# volume III's spine (the thinnest) less 1/8in each side: every spine's type
# and marks are sized to it
SPINE_FIT = "0.38in"


def cover(n, modern=False):
    if modern:
        # the Classic cover (cover-vol-N.typ) with the edition's label, a spine
        # mark and the back passage in its own words
        (BOOK / f"cover-vol-{n}-modern.typ").write_text(f'''// GENERATED BY source/make_volumes.py -- edit that, not this file.
// The Modern English edition of volume {n}'s cover: the Classic cover (cover-vol-{n}.typ),
// labelled (MODERN-ENGLISH-RULES.md: same art and colours, a small label and a spine mark).
#import "cover-vol-{n}.typ": cover
#cover(edition: [Modern English],
  epigraph: [{MODERN_BACK_WORDS}])
''')
        return
    # the page count the cover file has (set from the built interior), so
    # regenerating does not put the placeholder back
    old = BOOK / f"cover-vol-{n}.typ"
    m = re.search(r"pages: (\d+)", old.read_text(encoding="utf-8")) if old.exists() else None
    pages = m.group(1) if m else "400"
    book, subject = FRONTS[n - 1]
    (BOOK / f"cover-vol-{n}.typ").write_text(f'''#import "../../../scripts/set_cover.typ": *
#import "@local/fgbooks:0.14.0": press-seal

// GENERATED BY source/make_volumes.py -- edit that, not this file.
// The set's cover (scripts/set_cover.typ: its spine and back, the seal and
// name plate) with a front of its own: the title, the spectacles on an open
// book (art/vignette.png, made by art/vignette.py), this volume's line.
// ./fgb build gives the cover its compiled interior's page count and trim;
// `pages` is only for compiling the cover by itself.
// edition: the Modern English edition's label (cover-vol-{n}-modern.typ), set
// under this volume's line, clear of the vignette
#let ink = rgb("#F4EEDF")
#let gold = rgb("#E2C383")

#let cover(edition: none, epigraph: [{BACK_WORDS}]) = set-cover(
  // the books' 6x9 trim, for the front image the EPUB renders on its own
  trim-width: 6in, trim-height: 9in,
  edition: edition,
  ground: rgb("{GROUNDS[n - 1]}"),
  seal: press-seal,
  front: {{
    set align(center)
    set par(spacing: 0pt, leading: 0.4em, justify: false)
    place(center + top, dy: 0.95in, box(width: 4.5in, {{
      caps([John Calvin], 10pt, gold)
      v(0.14in)
      diamond-rule(gold)
      v(0.2in)
      text(font: DISPLAY, weight: "bold", size: 36pt, tracking: 0.04em, fill: ink)[INSTITUTES]
      v(0.1in)
      text(font: DISPLAY, size: 13pt, tracking: 0.28em, fill: ink)[OF THE CHRISTIAN RELIGION]
    }}))
    place(center + top, dy: 3.2in, image("art/vignette.png", width: 2.5in))
    place(center + top, dy: 5.05in, box(width: 4.5in, {{
      caps([Volume {ROMAN[n - 1]} · Book {book}], 8.5pt, gold, tracking: 0.3em)
      v(0.1in)
      text(size: 11pt, style: "italic", fill: ink)[{subject}]
      if edition != none {{
        v(0.2in)
        box(stroke: (top: 0.6pt + gold, bottom: 0.6pt + gold), inset: (x: 0.04in, y: 0.07in),
          caps(edition, 8pt, gold))
      }}
    }}))
  }},
  title: [Institutes of the Christian Religion],
  author: [John Calvin],
  spine-author: [Calvin],
  volume-number: [{ROMAN[n - 1]}],
  spine-fit: {SPINE_FIT},
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("{PAPERS[n - 1]}"),
  pages: {pages},
  back-lead: [{BACK[n - 1]}],
  epigraph: epigraph,
  epigraph-source: [{BACK_SOURCE}],
  // isbn: "978-0-000000-00-0",
)

#cover()
''')


def front(n, modern=False):
    note = SOURCE_NOTE.replace("_Institutio Christianae Religionis_",
                               "<em>Institutio Christianae Religionis</em>")
    if modern:
        note = re.sub(r"_([^_]+)_", r"<em>\1</em>", MODERN_SOURCE_NOTE).replace("'", "’")
    edition = '\n<p class="subtitle">Modern English</p>' if modern else ""
    epigraph = MODERN_EPIGRAPH if modern else EPIGRAPH
    after = ('\n<p class="note">' + MODERN_NOTE.format(plus="<sup>+</sup>") + "</p>") if modern else ""
    (BOOK / f"ebook-front-vol-{n}{'-modern' if modern else ''}.html").write_text(f'''<section id="front">
<p class="title">Institutes of the Christian Religion</p>
<p class="subtitle">Volume {ROMAN[n - 1]} — {SUBTITLES[n - 1]}</p>{edition}
<div class="imprint">
<img src="art/device-ebook.png" alt="The Common Weal Press device: a fountain in a town square, a cup hanging from it on a chain, with the words “Drink freely” and “Let the one who is thirsty come”, Revelation 22:17" class="device"/>
<p class="press">Common Weal Press</p>
<p class="motto"><em>Christian classics, freely given.</em></p>
<hr/>
<p>This edition is published by Common Weal Press and dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. You are free to copy, distribute, modify and use it for any purpose, without asking. <a href="https://creativecommons.org/publicdomain/zero/1.0/">creativecommons.org/publicdomain/zero/1.0</a></p>
<img src="lcc_standard_pd.png" alt="Public domain mark" class="licence"/>
<p><em>Freely you have received; freely give.</em> — Matthew 10:8</p>
<p>Printed copies are sold at the cost of printing: no revenue or royalty is made from them.</p>
<p>{note}</p>
<p>This is volume {n} of six: Book I is volume 1, Book II volume 2, Book III volumes 3 and 4, and Book IV volumes 5 and 6.</p>
<hr/>
<p>Free ebooks, PDFs and at-cost printed copies:</p>
<p class="site"><a href="https://commonwealpress.org">commonwealpress.org</a></p>
<p class="contact">Corrections and questions: <a href="mailto:books@commonwealpress.org">books@commonwealpress.org</a></p>
</div>
<p class="epigraph"><em>{epigraph}</em> — {EPIGRAPH_SOURCE}</p>{after}
</section>
''')


if __name__ == "__main__":
    for n, files in enumerate(volumes(), start=1):
        print_book(n, files)
        cover(n)
        front(n)
        if n in ED["MODERN_VOLUMES"]:
            print_book(n, files, modern=True)
            cover(n, modern=True)
            front(n, modern=True)
        print(f"volume {n}: {len(files)} files" + (" (and Modern English)" if n in ED["MODERN_VOLUMES"] else ""))
