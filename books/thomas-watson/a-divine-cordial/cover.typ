#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.14.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), the first of Watson's books: no picture, the
// book's text is the image. The whole book opens Romans 8:28, so the verse is
// set in the title's type with "all things" and "for good" in gold, on a deep
// green, the colour of a cordial. The back carries the book's own promise,
// from the epistle to the reader. (A draft: the colour is the editor's to
// choose.)
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#EEF0EA")
#let gold = rgb("#D6A55A")

#plate-cover(
  ground: rgb("#1F3328"),
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 15pt, tracking: 0.12em,
      fill: ink.transparentize(35%), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 22pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.5in, dy: 3.45in, box(width: 4.5in, {
      set align(center)
      set par(leading: 0.55em, spacing: 0pt)
      [#plain[We know that]#h(0.12in)#gilt[all things]]
      v(0.08in)
      [#plain[work together]#h(0.12in)#gilt[for good] \
       #plain[to them that love God.]]
      v(0.2in)
      caps([Romans viii. 28], 9pt, gold.transparentize(20%), tracking: 0.25em)
    }))
  }),
  title-y: 0.85in,
  seal: press-seal,
  title: [A Divine Cordial],
  subtitle: [
    The Transcendent Privilege of Those \
    That Love God and Are Savingly Called
  ],
  author: [Thomas Watson],
  spine-title: [A Divine Cordial],
  spine-author: [Watson],
  pages: 180,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#16241C"),
  epigraph: [
    That all things which fall out shall co-operate for their good, that
    their crosses shall be turned into blessings, here is that which may
    fill their hearts with joy till they run over.
  ],
  epigraph-source: [From the Epistle to the Reader],
)
