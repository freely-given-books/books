#import "../../../scripts/table_cover.typ": table-cover
#import "@local/fgbooks:0.14.0": press-seal

// Full-wrap paperback cover: the household table (scripts/table_cover.typ, the
// editor's choice of 2026-11-21). "Thy children like olive plants round about thy
// table" (Psalm 128:3): the eight treatises are places at one table, this volume's
// laid in gold, on a cloth in this volume's green; the set's greens step from a
// light spring green (volume I) to a mid olive (volume IV).
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
// edition: the Modern English edition's label (cover-vol-2-modern.typ)
#let cover(edition: none,
  epigraph: [Submitting your selves one to another in the fear of God.]) = table-cover(
  edition: edition,
  seal: press-seal,
  cloth: rgb("#9FB66B"),
  places: (
    ([I], [Exposition], [An Exposition of That Part of Scripture out of Which Domestical Duties Are Raised]),
    ([II], [Man and Wife], [Of a Right Conjunction of Man and Wife, and Their Common-Mutual Duties]),
    ([III], [Wives], [Particular Duties of Wives]),
    ([IV], [Husbands], [Particular Duties of Husbands]),
    ([V], [Children], [Duties of Children]),
    ([VI], [Parents], [Duties of Parents]),
    ([VII], [Servants], [Duties of Servants]),
    ([VIII], [Masters], [Duties of Masters]),
  ),
  current: (1, 2, 3),
  volume: [Volume II],
  volume-number: [II],
  // volume IV's spine (179 pages): the set's thinnest
  spine-fit: 0.21in,
  pages: 348,
  back-lead: [Who may marry and how a marriage is made; the duties husband and wife owe each other in common; and then, at length, the particular duties of wives and of husbands — each duty set against the fault that answers to it.],
  epigraph: epigraph,
  epigraph-source: [Ephesians v. 21],
  // isbn: "978-0-000000-00-0",
)

#cover()
