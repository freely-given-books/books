#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.1": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The plate is Boston's lot as the Ettrick hills:
// "the mountains and the valleys ... the heights and depths, the prosperity
// and adversity in the lot" (Part I), the valley still in shadow and the sun
// rising over the far hills, "as the morning follows the night" (Part III),
// the flock on its track, and a shepherd's crook standing in the near hill.
// An engraving made for this edition, printed in Boston's heather
// (art/plate.png, the paper cut away so the ground shows through).
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ground = ((rgb("#E4DFEC"), 0%), (rgb("#EFE9EC"), 40%), (rgb("#F4EDE6"), 52%), (rgb("#E6E1EC"), 100%))

#plate-cover(
  plate: read("art/plate.png", encoding: none),
  // full width to the bleed, raised so the near hill's grass ends above the
  // press's seal
  plate-at: (dx: -0.125in, dy: -0.45in, width: 5.75in, height: 8.625in),
  ground: ground,
  seal: press-seal,
  title: [The Crook],
  tail: [in the Lot],
  subtitle: [The Sovereignty and Wisdom of God \ Displayed in the Afflictions of Men],
  author: [Thomas Boston],
  spine-title: [The Crook in the Lot],
  spine-author: [Boston],
  title-size: 34pt,
  pages: 135,
  ink: rgb("#261F36"),
  accent: rgb("#5C4F7A"),
  label: rgb("#2A2340"),
  paper: rgb("#F1ECE6"),
  // the back's words as the book has had them: Boston's first doctrine
  epigraph: [Whatsoever crook is in one’s lot, it is of God’s making.],
  epigraph-source: [Part I],
  // Uncomment once the book has an ISBN; this puts the white field the printer
  // drops the barcode into on the back cover.
  // isbn: "978-0-000000-00-0",
)
