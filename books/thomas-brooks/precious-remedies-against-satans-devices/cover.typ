#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.3": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The plate is Brooks's remedy: "the shield of
// faith, whereby you shall be able to quench all the fiery darts of the
// devil" (Propositions): the shield standing alone, a dart quenched in it,
// its smoke rising. An engraving made for this edition, printed in the book's
// deep teal (art/plate.png, the paper cut away so the ground shows through).
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ground = ((rgb("#C5DAD4"), 0%), (rgb("#E3EEEA"), 45%), (rgb("#D2E3DD"), 80%), (rgb("#BDD3CC"), 100%))

#plate-cover(
  plate: read("art/plate.png", encoding: none),
  // a little under page size, so the shield stands clear of the press's seal
  plate-at: (dx: 0.635in, dy: 1.24in, width: 4.29in, height: 6.435in),
  ground: ground,
  seal: press-seal,
  title: [Precious Remedies],
  tail: [Against Satan’s Devices],
  subtitle: [Or, Salve for Believers’ and Unbelievers’ Sores],
  author: [Thomas Brooks],
  spine-title: [Precious Remedies Against Satan’s Devices],
  spine-author: [Brooks],
  title-size: 30pt,
  pages: 354,
  ink: rgb("#0F3133"),
  accent: rgb("#7A5C22"),
  label: rgb("#13393B"),
  paper: rgb("#F1E6CF"),
  epigraph: [
    “Put on the whole armour of God, that ye may be able to stand against
    the wiles of the devil.”
  ],
  epigraph-source: [Ephesians 6:11],
  // Uncomment once the book has an ISBN; this puts the white field the printer
  // drops the barcode into on the back cover.
  // isbn: "978-0-000000-00-0",
)
