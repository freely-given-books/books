#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.14.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The plate is the book's own figure: a cordial,
// which Watson prescribes to the drooping saint, "I would prescribe them to
// take now & then a little of this Cordial" (To the Reader): an apothecary's
// bottle, its cork tied over with paper, half full. An engraving made for
// this edition (art/cordial-original.png), hand-tinted by art/tint.py: amber
// cordial, faintly green glass, cream paper cap, on a soft teal ground. The back carries the
// epistle's promise.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
//
// the spine and back: the plate's own teal ground, deepening toward the foot (the
// editor chose it over sage, 2026-11-08: the amber cordial glows against it)
#let ground = ((rgb("#CFE0DC"), 0%), (rgb("#B9CFCA"), 100%))

// edition: the Modern English edition's label (cover-modern.typ)
#let cover(edition: none) = plate-cover(
  edition: edition,
  plate: read("art/plate.jpg", encoding: none),
  // enlarged past the bleed (the plate is mostly paper), the bottle below the title and
  // the table's edge above the seal
  plate-at: (dx: -0.85in, dy: -2in, width: 7.2in, height: 10.8in),
  ground: ground,
  front-ground: rgb("#B9CFCA"),
  seal: press-seal,
  title: [A Divine],
  tail: [Cordial],
  subtitle: [The Transcendent Privilege of Those \ That Love God and Are Savingly Called],
  author: [Thomas Watson],
  spine-title: [A Divine Cordial],
  spine-author: [Watson],
  title-size: 34pt,
  pages: 153,
  ink: rgb("#22302A"),
  accent: rgb("#9A5A26"),
  label: rgb("#26332C"),
  paper: rgb("#F3ECDD"),
  epigraph: [
    To be assured that all things which fall out, shall co-operate for
    their good, that their crosses shall be turned into blessings, the
    bloody showers of affliction shall water the withering root of their
    Grace, and make it flourish more; here is that may fill their hearts
    with joy till they run over.
  ],
  epigraph-source: [From the Epistle to the Reader],
)

#cover()
