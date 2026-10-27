#import "../../../scripts/set_cover.typ": *
#import "@local/fgbooks:0.13.2": press-seal

// Full-wrap paperback cover in the Common Weal Press set design (see
// scripts/set_cover.typ), lettered after the 1622 title page: the whole
// work's eight treatises, this volume's picked out, its number in a roundel.
// Olive in its dark, for the household psalm: "thy children like olive plants round
// about thy table" (Psalm 128:3).
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#set-cover(
  seal: press-seal,
  // the dark of the earlier covers round the frame and on spine and back;
  // inside the frame, olive with a soft light behind the title and contents
  ground: rgb("#1F2416"),
  panel: gradient.radial((rgb("#566038"), 0%), (rgb("#4A5230"), 45%),
    (rgb("#363D25"), 100%), center: (50%, 42%), radius: 75%),
  title: [Of Domestical Duties],
  title-display: [
    #lettered([Of], 13pt, tracking: 0.5em)

    #lettered([Domestical], 34pt, tracking: 0.04em, weight: "bold")

    #lettered([Duties], 21pt, tracking: 0.42em)
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
  current: (0,),
  volume: [Volume I],
  volume-number: [I],
  // volume IV's spine (179 pages): the set's thinnest
  spine-fit: 0.21in,
  pages: 235,
  back-lead: [The first of Gouge's eight treatises: a verse-by-verse exposition of Ephesians 5:21-6:4, the passage the whole work is raised out of. Wives and husbands, children and parents, and above them the marriage of Christ and His church.],
  epigraph: [Submitting your selves one to another in the fear of God.],
  epigraph-source: [Ephesians v. 21],
  // isbn: "978-0-000000-00-0",
)
