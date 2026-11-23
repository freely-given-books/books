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
// edition: the Modern English edition's label (cover-vol-3-modern.typ)
#let cover(edition: none,
  epigraph: [Submitting your selves one to another in the fear of God.],
  epigraph-source: [Ephesians v. 21],
  psalm: [Thy children like olive plants round about thy table.],
  psalm-source: [Psalm cxxviii. 3]) = table-cover(
  edition: edition,
  seal: press-seal,
  cloth: rgb("#8AA45A"),
  // this volume's step from ivory (I) to parchment (IV)
  paper-tint: 34%,
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
  current: (4, 5),
  volume: [Volume III],
  volume-number: [III],
  // volume IV's spine (179 pages): the set's thinnest
  spine-fit: 0.21in,
  pages: 232,
  back-lead: [The duties children owe their parents — reverence, consent, obedience, and the recompense owed to age — and then the parents' own: love and prayer, nursing and nurture, teaching and correction, and the settling of a child in a calling and a marriage.],
  epigraph: epigraph,
  epigraph-source: epigraph-source,
  psalm: psalm,
  psalm-source: psalm-source,
  // isbn: "978-0-000000-00-0",
)

#cover()
