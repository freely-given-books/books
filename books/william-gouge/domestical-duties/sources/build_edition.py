#!/usr/bin/env python3
"""
build_edition.py
================

Since the book moved to the TEI pipeline (2026-09-30) the chapters come from
the TEI (source/domestical-duties.tei.xml, via ./fgb sync or tei_extract.py),
cut by the same map, ../source/edition.json. This script now writes only what
follows from the chapters:

    domestical-duties-vol-N.typ       the print edition of each volume
    cover-vol-N.typ                   its wrap cover (--covers)
    ebook-domestical-duties.typ       the old one-file ebook source (the EPUB is
                                      now built by ./fgb epub gouge)

Usage:
    python3 build_edition.py                 # volumes, old ebook source
    python3 build_edition.py --covers        # rewrite the covers from the
                                             #    compiled page counts
    python3 build_edition.py --old-chapters  # the earlier converter's chapters
                                             #    (overwrites chapters/typ!)
    python3 build_edition.py --original      # old-spelling render as well

The covers need a page count, and the page count needs a compiled interior, so
that is a second pass: build, `typst compile` each volume, then `--covers`.
It reads the count out of the PDF rather than taking it on trust, because a
stale `pages:` is a wrong spine and a wrong spine is a wrecked print run.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from lxml import etree

import gap_resolver
import tcp_to_typst as T

HERE = Path(__file__).resolve().parent
BOOK = HERE.parent
XML = HERE / "A68107.xml"
EDITION = BOOK / "source" / "edition.json"   # one map, shared with the TEI layout

# The imprint's boilerplate, shared by the print and ebook editions.  Kept here
# rather than in each volume file so the four covers, four title pages and one
# ebook cannot drift apart.
LICENCE = """This copy is provided to you free of charge under the Creative Commons CC0 1.0 Universal license.

    https://creativecommons.org/publicdomain/zero/1.0/

    #image("lcc_standard_pd.png", width: 50%)

    Freely you have received; freely give. - Matthew 10:8b

    To get more free ebooks or at-cost printed copies, visit:

    https://books.freely.giving

    Printed books are at the cost of the printing, no revenue or
    royalty is made from printings so you can get ahold of
    physical prints at the lowest cost possible.

    Set from William Gouge's _Of Domesticall Dvties_ (London, printed by John
    Haviland for William Bladen, 1622), with the spelling modernized. The text
    is the Text Creation Partnership transcription of the first edition
    (EEBO-TCP A68107).

    Book formatted by Courtney Allen Hicks

    #link("mailto:books@lyndnex.com")

    ebook and PDF also available."""

EPIGRAPH = "Submitting your selves one to another in the fear of God."
EPIGRAPH_SOURCE = "Ephesians 5:21"

TRIM_W, TRIM_H = 6, 9
BLEED = 0.125


def slugify(title):
    s = title.lower().replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def load():
    edition = json.loads(EDITION.read_text(encoding="utf-8"))
    root = etree.parse(str(XML)).getroot()
    divs = T.get_top_divs(root)
    T.GAP_RESOLVER["r"] = gap_resolver.GapResolver(root, T.normalize_source)
    return edition, divs


# ---------------------------------------------------------------------------
# Chapters
# ---------------------------------------------------------------------------

def write_chapters(edition, divs, outdir, modernize):
    """One .typ per chapter, plus the front/back matter divisions each volume
    claims.  Returns {volume number: [(slug, title, path), ...]}."""
    T.MODERNIZE["on"] = modernize
    if modernize:
        T._load_modernizer()

    front = {}
    for name, spec in edition["front"].items():
        front[name] = spec

    built = {}
    for vol in edition["volumes"]:
        vdir = outdir / f"vol-{vol['number']}"
        vdir.mkdir(parents=True, exist_ok=True)
        items = []

        def matter(name):
            spec = front[name]
            div = divs[spec["div"] - 1]
            text = T.render_top_div(div, standalone=False)
            if spec.get("title"):
                # A division the original gives no heading of its own.
                text = f"{'=' * T.BASE_LEVEL} {spec['title']}\n\n" + text
            path = vdir / f"{name}.typ"
            path.write_text(text, encoding="utf-8")
            return (name, spec.get("title") or first_heading(text), path, False)

        items.extend(matter(name) for name in vol.get("front", []))

        for i, ch in enumerate(vol["chapters"], start=1):
            div = divs[ch["div"] - 1]
            first, last = ch["sections"]
            total = len(T.section_divs(div))
            if not (1 <= first <= last <= total):
                sys.exit(f"vol {vol['number']} ch {i}: sections {first}-{last} "
                         f"outside 1:{ch['div']} which has {total}")
            text = T.render_chapter(div, first, last, ch["title"])
            path = vdir / f"{i:02d}-{slugify(ch['title'])}.typ"
            path.write_text(text, encoding="utf-8")
            items.append((path.stem, ch["title"], path, False))

        # Back matter after the chapters, where the original prints it: the
        # errata leaf is the last thing in the 1622 book.
        items.extend(matter(name) for name in vol.get("back", []))

        built[vol["number"]] = items
    return built


def chapter_index(edition):
    """What write_chapters returns, for the chapters already in chapters/typ
    (written from the TEI): {volume: [(slug, title, path, False), ...]}."""
    built = {}
    for vol in edition["volumes"]:
        vdir = BOOK / "chapters" / "typ" / f"vol-{vol['number']}"
        items = []

        def matter(name):
            path = vdir / f"{name}.typ"
            spec = edition["front"][name]
            return (name, spec.get("title") or
                    first_heading(path.read_text(encoding="utf-8")), path, False)
        items += [matter(n) for n in vol.get("front", [])]
        for i, ch in enumerate(vol["chapters"], start=1):
            path = vdir / f"{i:02d}-{slugify(ch['title'])}.typ"
            if not path.exists():
                sys.exit(f"missing {path.relative_to(BOOK)}: run ./fgb sync gouge")
            items.append((path.stem, ch["title"], path, False))
        items += [matter(n) for n in vol.get("back", [])]
        built[vol["number"]] = items
    return built


def first_heading(text):
    m = re.search(r"^={1,3} (.+)$", text, re.M)
    return T.unwrap_emph(m.group(1)) if m else "Front matter"


def short_title(title):
    """What goes in the <short> metadata the fgbooks template reads.

    It is used for BOTH the running head and the table of contents, so it must
    not be an abbreviation: truncating to fit the header gives a contents page
    full of "A Master's Care for His Servants'...".  The longest title here is
    54 characters, which at 0.9em smallcaps is about 3.1in in a header column
    roughly 4.25in wide, so the full title fits.  Kept as a function because
    the next book's titles may not."""
    return title


# ---------------------------------------------------------------------------
# The print volumes
# ---------------------------------------------------------------------------

VOLUME_TEMPLATE = '''#import "@local/fgbooks:0.5.2": *

// GENERATED BY sources/build_edition.py -- edit edition.json, not this file.
//
// 6x9 rather than the template's 5.5x8.5, and 10.5pt: at 290,000 words the
// whole work is four times the length of anything else in the imprint, and
// the larger trim is what keeps each volume inside a binder's page limit
// while still reading as one column.  The inside margin follows Lulu's
// recommendation for a block this thick.

#show outline: set text(9.5pt)

#show: book.with(
  title: [Of Domestical Duties],
  subtitle: [Volume {roman} — {subtitle}],
  author: "William Gouge",
  page-width: 6in,
  page-height: 9in,
  page-margin: (bottom: 0.75in, top: 0.75in, outside: 0.75in, inside: 1.0in),
  publishing-info: [
    {licence}

    This is volume {number} of four. The complete work is in eight treatises:
    I, an exposition of Ephesians 5:21–6:9; II, of husband and wife; III, of
    wives; IV, of husbands; V, of children; VI, of parents; VII, of servants;
    VIII, of masters.

  ],
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _{epigraph}_

        — {epigraph_source}
      ]
    ]
  ]
)

#set text(font: "Liberation Serif", size: 10.5pt)

{includes}
'''


def write_volumes(edition, built):
    for vol in edition["volumes"]:
        lines = []
        for slug, title, path, _is_back in built[vol["number"]]:
            rel = path.relative_to(BOOK).as_posix()
            lines.append(f"#metadata[{short_title(title)}] <short>")
            lines.append(f'#include "{rel}"')
            lines.append("")
        text = VOLUME_TEMPLATE.format(
            roman=vol["roman"], subtitle=vol["subtitle"], number=vol["number"],
            licence=LICENCE, epigraph=EPIGRAPH,
            epigraph_source=EPIGRAPH_SOURCE, includes="\n".join(lines).strip())
        (BOOK / f"domestical-duties-vol-{vol['number']}.typ").write_text(
            text, encoding="utf-8")


# ---------------------------------------------------------------------------
# The ebook -- one file for the whole work
# ---------------------------------------------------------------------------

EBOOK_HEAD = '''#show align: it => html.elem("div", attrs: (style: "text-align: " + repr(it.alignment)))[#it.body]
#show pagebreak: it => context if target() == "html" {{ }} else {{ it }}

// GENERATED BY sources/build_edition.py -- edit edition.json, not this file.
// The print edition is four volumes; the ebook is deliberately one file, so a
// reader searching for a duty is not searching four books.

#text(size: 24pt, weight: "bold")[Of Domestical Duties]

Eight treatises on the duties of husbands and wives, parents and children,
masters and servants.

{licence}

#text(size: 16pt)[_{epigraph}_ — {epigraph_source}]

'''


def write_ebook(edition, built):
    parts = [EBOOK_HEAD.format(licence=LICENCE.replace("    ", ""),
                               epigraph=EPIGRAPH,
                               epigraph_source=EPIGRAPH_SOURCE)]
    for vol in edition["volumes"]:
        parts.append(f"#text(size: 20pt, weight: \"bold\")"
                     f"[Volume {vol['roman']}: {vol['subtitle']}]\n")
        for slug, title, path, _ in built[vol["number"]]:
            parts.append(f'#include "{path.relative_to(BOOK).as_posix()}"\n')
    (BOOK / "ebook-domestical-duties.typ").write_text(
        "\n".join(parts), encoding="utf-8")


# ---------------------------------------------------------------------------
# Covers
# ---------------------------------------------------------------------------

COVER_TEMPLATE = '''#import "../../../scripts/panel_cover.typ": *

// GENERATED BY sources/build_edition.py --covers.  The page count is read
// from the compiled interior, so recompile domestical-duties-vol-{number}.pdf
// and re-run before ordering.
//
// The spine uses Lulu's own formula rather than page-count-times-caliper.
// The two agree under about 240 pages and drift apart above it; at 300 pages
// they differ by 0.06in, and the trim tolerance is 0.125in.  VERIFY against a
// downloaded live 6x9 perfect-bound template before ordering.
//
//   front-panel crop for the ebook cover, at 300 dpi:
//     magick -density 300 "cover-vol-{number}.pdf[0]" -background white \\
//       -alpha remove -crop 1800x2700+{crop_x}+38 +repage \\
//       -resize 900x1350 -quality 92 cover-vol-{number}-front.jpg
#panel-cover(
  title: [Of Domestical Duties],
  volume: [Volume {roman}],
  subtitle: [{subtitle}],
  author: [William Gouge],
  pages: {pages},
  spine: lulu-spine({pages}),
  paper: "cream-60",
  trim-width: 6in,
  trim-height: 9in,
  palette: "hearth",
  spine-style: "plain",
  title-size: 26pt,
  back-lead: [{back_lead}],
  epigraph: ["{epigraph}"],
  epigraph-source: [— {epigraph_source}],
  // Uncomment once the volume has an ISBN; this puts the white field the
  // printer drops the barcode into on the back cover.
  // isbn: "978-0-000000-00-0",
)
'''


def pdf_pages(path):
    out = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True)
    for line in out.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    sys.exit(f"could not read a page count from {path} -- compile it first")


EBOOK_COVER_BACK_LEAD = (
    "London, 1622. Eight treatises preached to the parish of Blackfriars: an "
    "exposition of Ephesians 5:21-6:9, and then the duties of husband and "
    "wife, of wives, of husbands, of children, of parents, of servants, and "
    "of masters — each set against the faults that answer to it.")


def write_covers(edition):
    total = 0
    for vol in edition["volumes"]:
        n = vol["number"]
        pdf = BOOK / f"domestical-duties-vol-{n}.pdf"
        if not pdf.exists():
            sys.exit(f"{pdf.name} does not exist -- compile the volume first")
        pages = pdf_pages(pdf)
        total += pages
        spine = pages / 444.0 + 0.06
        crop_x = round((BLEED + TRIM_W + spine) * 300)
        (BOOK / f"cover-vol-{n}.typ").write_text(COVER_TEMPLATE.format(
            number=n, roman=vol["roman"], subtitle=vol["subtitle"],
            pages=pages, crop_x=crop_x, back_lead=vol["back-lead"],
            epigraph=EPIGRAPH, epigraph_source=EPIGRAPH_SOURCE),
            encoding="utf-8")
        print(f"cover-vol-{n}.typ: {pages} pages, spine {spine:.3f}in")

    # One more wrap with no volume line, for the ebook's cover image: the
    # ebook is the whole work, so a cover saying "Volume I" would be a lie.
    # Its spine is notional -- the four volumes together are past any
    # perfect-binding limit -- but the crop offset has to come from
    # somewhere, and the front panel is what gets used.
    spine = total / 444.0 + 0.06
    text = COVER_TEMPLATE.format(
        number="ebook", roman="", subtitle=(
            "Eight Treatises on the Duties of Husbands and Wives, "
            "Parents and Children, Masters and Servants"),
        pages=total, crop_x=round((BLEED + TRIM_W + spine) * 300),
        back_lead=EBOOK_COVER_BACK_LEAD,
        epigraph=EPIGRAPH, epigraph_source=EPIGRAPH_SOURCE)
    text = text.replace("  volume: [Volume ],\n", "")
    (BOOK / "cover-ebook.typ").write_text(text, encoding="utf-8")
    print(f"cover-ebook.typ: whole work, {total} pages across four volumes")


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--covers", action="store_true",
                    help="Rewrite the covers from the compiled page counts")
    ap.add_argument("--old-chapters", action="store_true",
                    help="Write the earlier converter's chapters over chapters/typ")
    ap.add_argument("--original", action="store_true",
                    help="Also write the original-spelling render")
    args = ap.parse_args()

    edition, divs = load()

    if args.covers:
        write_covers(edition)
        return

    if args.old_chapters:
        built = write_chapters(edition, divs, BOOK / "chapters" / "typ", True)
    else:
        built = chapter_index(edition)
    write_volumes(edition, built)
    write_ebook(edition, built)
    if args.old_chapters:
        T.GAP_RESOLVER["r"].summarize(sys.stderr)
    total = sum(len(v["chapters"]) for v in edition["volumes"])
    print(f"{len(edition['volumes'])} volumes, {total} chapters")

    if args.original:
        T.MODERNIZE["on"] = False
        _, divs = load()
        write_chapters(edition, divs, HERE / "original-spelling", False)
        print("original-spelling render written")


if __name__ == "__main__":
    main()
