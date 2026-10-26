#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.1": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The plate is Bunyan's own vision (§53-55): the
// poor people of Bedford on the sunny side of a high mountain, a wall about
// it, and one narrow gap, "like a little doorway in the wall", which "was
// Jesus Christ, who is the way to God the Father"; we stand where he stood,
// in the frost and snow. An engraving made for this edition, hand-tinted
// (art/tint.py): art/plate.jpg. The back carries Bunyan's word, from his
// preface, on how he wrote the book.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
// The spine and back: the plate's own colours down its edge, warm sky
// above to cold snow below.
#let ground = ((rgb("#ECE8DC"), 0%), (rgb("#EFE6CF"), 35%), (rgb("#DCE0E6"), 65%), (rgb("#E4E9EF"), 100%))

#plate-cover(
  plate: read("art/plate.jpg", encoding: none),
  // the scene lowered 0.8in under extended sky (tint.py), its top band clear
  // for the title; the foot of plain snow runs into the bleed
  plate-at: (dx: -0.125in, dy: -0.72in, width: 5.75in, height: 10.02in),
  ground: ground,
  // under the plate's foot, its own snow colour, so no seam shows
  front-ground: rgb("#E4E9EF"),
  seal: press-seal,
  title: [Grace Abounding],
  tail: [to the Chief of Sinners],
  subtitle: [Or, a Brief Relation of the Exceeding Mercy of God in Christ, \ to His Poor Servant John Bunyan],
  author: [John Bunyan],
  spine-title: [Grace Abounding],
  spine-author: [Bunyan],
  pages: 122,
  // a cold slate for the type, the sun's ochre for the author and rules
  ink: rgb("#262838"),
  accent: rgb("#8A6A1E"),
  label: rgb("#262838"),
  paper: rgb("#F2EBD8"),
  epigraph: [
    I could also have stepped into a style much higher than this in which I
    have here discoursed, and could have adorned all things more than here I
    have seemed to do, but I dare not. God did not play in convincing of me,
    the devil did not play in tempting of me, neither did I play when I sunk
    as into a bottomless pit, when the pangs of hell caught hold upon me;
    wherefore I may not play in relating of them, but be plain and simple,
    and lay down the thing as it was.
  ],
  epigraph-source: [The Preface],
)
