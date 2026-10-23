#import "../../../scripts/set_cover.typ": *
#import "@local/fgbooks:0.13.1": press-seal

// Full-wrap paperback cover in the Common Weal Press set design (see
// scripts/set_cover.typ), lettered after the 1622 title page: the whole
// work's eight treatises, this volume's picked out, its number in a roundel.
// Olive, for the household psalm: "thy children like olive plants round
// about thy table" (Psalm 128:3).
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#set-cover(
  seal: press-seal,
  title: [Of Domestical Duties],
  title-display: [
    #lettered([Of], 12pt, tracking: 0.5em)

    #lettered([Domestical], 29pt, tracking: 0.04em, weight: "bold")

    #lettered([Duties], 18pt, tracking: 0.42em)
  ],
  kicker: [Eight Treatises],
  imprint: [London, 1622],
  author: [William Gouge],
  spine-author: [Gouge],
  contents: (
    ([I.], [An Exposition of That Part of Scripture out of Which Domestical Duties Are Raised]),
    ([II.], [Of a Right Conjunction of Man and Wife, and Their Common-Mutual Duties]),
    ([III.], [Particular Duties of Wives]),
    ([IV.], [Particular Duties of Husbands]),
    ([V.], [Duties of Children]),
    ([VI.], [Duties of Parents]),
    ([VII.], [Duties of Servants]),
    ([VIII.], [Duties of Masters]),
  ),
  current: (6, 7),
  volume: [Volume IV],
  volume-number: [IV],
  // volume IV's spine (179 pages): the set's thinnest
  spine-fit: 0.21in,
  pages: 179,
  back-lead: [The last of the eight treatises, with the exposition of Ephesians 6:5-9 they are raised out of: what a servant owes his master in reverence, obedience and faithfulness, and what a master owes his servants in authority, provision, employment and wages — under the Master they both have in heaven.],
  epigraph: [Submitting your selves one to another in the fear of God.],
  epigraph-source: [Ephesians v. 21],
  // isbn: "978-0-000000-00-0",
)
