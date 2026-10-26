#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.1": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The plate is Bunyan's own vision (§53-55): the
// poor people of Bedford on the sunny side of a high mountain, a wall about
// it, and one narrow gap, "like a little doorway in the wall", which "was
// Jesus Christ, who is the way to God the Father"; we stand where he stood,
// in the frost and snow. An engraving made for this edition; its colour
// painted by ChatGPT on a copy and laid under the approved engraving's own
// lines (art/transfer.py), so no line, face or hand changed: art/plate.jpg.
// The back carries Bunyan's own reading of the vision (§55).
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
// The spine and back: the plate's own colours, blue sky warming
// toward the mountain, then cold snow below.
#let ground = ((rgb("#C3E3FC"), 0%), (rgb("#C8E5FA"), 20%), (rgb("#F2EED8"), 34%), (rgb("#E6ECF2"), 66%), (rgb("#ECF4FC"), 100%))

#plate-cover(
  plate: read("art/plate.jpg", encoding: none),
  // the scene lowered 0.8in under extended sky (tint.py), its top band clear
  // for the title; the foot of plain snow runs into the bleed
  plate-at: (dx: -0.125in, dy: -0.72in, width: 5.75in, height: 10.02in),
  ground: ground,
  // under the plate's foot, its own snow colour, so no seam shows
  front-ground: rgb("#EFF6FC"),
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
  // §55: Bunyan's own reading of the front's picture (quoted exactly from
  // chapters/typ; "etc.," and the references after "Father" left out)
  epigraph: [
    Now, this mountain and wall … was thus made out to me — the mountain
    signified the church of the living God; the sun that shone thereon, the
    comfortable shining of His merciful face on them that were therein; the
    wall, I thought, was the Word, that did make separation between the
    Christians and the world; and the gap which was in this wall, I thought,
    was Jesus Christ, who is the way to God the Father.
  ],
  epigraph-source: [Grace Abounding, §55],
)
