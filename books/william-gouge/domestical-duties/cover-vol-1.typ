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
// edition: the Modern English edition's label (cover-vol-1-modern.typ)
#let cover(edition: none,
  epigraph: [Submitting your selves one to another in the fear of God.],
  epigraph-source: [Ephesians v. 21],
  psalm: [Thy children like olive plants round about thy table.],
  psalm-source: [Psalm cxxviii. 3]) = table-cover(
  edition: edition,
  seal: press-seal,
  cloth: rgb("#B4C77E"),
  // this volume's step from ivory (I) to parchment (IV)
  paper-tint: 6%,
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
  current: (0,),
  volume: [Volume I],
  volume-number: [I],
  // volume IV's spine (179 pages): the set's thinnest
  spine-fit: 0.21in,
  pages: 235,
  back-lead: [The first of Gouge's eight treatises: a verse-by-verse exposition of Ephesians 5:21-6:4, the passage the whole work is raised out of. Wives and husbands, children and parents, and above them the marriage of Christ and His church.],
  epigraph: epigraph,
  epigraph-source: epigraph-source,
  psalm: psalm,
  psalm-source: psalm-source,
  // isbn: "978-0-000000-00-0",
)

#cover()
