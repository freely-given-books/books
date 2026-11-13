#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.14.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), Mortification's design for Owen's sin books: no
// picture, the book's text is the image. The whole book opens Matthew 26:41,
// Christ waking the disciples in Gethsemane, so the verse is set in the
// title's type with "Watch and pray" and "temptation" in gold, on the slate
// blue of a night garden (Mortification is oxblood). The back carries the
// book's doctrine, from chapter III.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#ECEEF0")
#let gold = rgb("#D6A55A")

// opaque: the ink mixed with the ground it sits on, not transparent (Lulu flattens
// transparency into image tiles: scripts/plate_cover.typ)
#plate-cover(
  ground: rgb("#1D2838"),
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 15pt, tracking: 0.12em,
      fill: color.mix((ink, 65%), (rgb("#1D2838"), 35%)), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 22pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.5in, dy: 3.45in, box(width: 4.5in, {
      set align(center)
      set par(leading: 0.55em, spacing: 0pt)
      gilt[Watch and pray,]
      v(0.08in)
      [#plain[that ye enter not] \
       #plain[into]#h(0.12in)#gilt[temptation.]]
      v(0.2in)
      caps([Matthew xxvi. 41], 9pt, color.mix((gold, 80%), (rgb("#1D2838"), 20%)), tracking: 0.25em)
    }))
  }),
  title-y: 0.85in,
  seal: press-seal,
  title: [Of Temptation],
  subtitle: [
    The Nature and Power of It; the Danger of Entering \
    into It; and the Means of Preventing That Danger
  ],
  author: [John Owen],
  spine-title: [Of Temptation],
  spine-author: [Owen],
  pages: 104,
  ink: ink,
  accent: gold,
  // as Mortification: the seal and name plate in gold, the fountain and
  // lettering cut in the ground's dark
  label: gold,
  paper: rgb("#141C28"),
  epigraph: [
    It is the great duty of all believers to use all diligence in the ways
    of Christ's appointment, that they fall not into temptation.
  ],
  epigraph-source: [From Chapter III],
)
