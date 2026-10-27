#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.2": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The plate is the verse on the 1609 title page,
// Proverbs 24:3, "Through wisdom is an house built": a timber-framed house of
// Perkins's day, an engraving made for this edition, printed in Perkins's deep
// mulberry (art/plate.png, the paper cut away so the ground shows through) on
// a pale mulberry-rose ground, the shelf's first light cover in that colour.
// The back keeps the book's Joshua 24:15, "as for me and my house".
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let rose = ((rgb("#E6D7DD"), 0%), (rgb("#F3EBEE"), 38%), (rgb("#EDE2E6"), 70%), (rgb("#E3D3DA"), 100%))

#plate-cover(
  plate: read("art/plate.png", encoding: none),
  // set half an inch low: the title and its two-line subtitle need the sky
  plate-at: (dx: -0.165in, dy: 0.42in, width: 5.83in, height: 8.75in),
  ground: rose,
  seal: press-seal,
  title: [Christian Economy],
  subtitle: [
    Or, A Short Survey of the Right Manner of Erecting \
    and Ordering a Family, According to the Scriptures
  ],
  author: [William Perkins],
  spine-title: [Christian Economy],
  spine-author: [Perkins],
  title-size: 34pt,
  pages: 126,
  ink: rgb("#3E1C2A"),
  accent: rgb("#7A4058"),
  label: rgb("#F3EAEE"),
  paper: rgb("#4A2433"),
  epigraph: [
    And if it seem evil unto you to serve the LORD, choose you this day whom
    ye will serve… but as for me and my house, we will serve the LORD.
  ],
  epigraph-source: [Joshua 24:15],
)
