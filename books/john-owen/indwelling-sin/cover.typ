#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.14.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), Mortification's design for Owen's sin books: no
// picture, the book's text is the image. The whole book opens Romans 7:21,
// "I find then a law", so the verse is set in the title's type with "a law"
// and "evil is present with me" in gold, on a deep green (Mortification is
// oxblood, Of Temptation slate blue). The back carries the law's dwelling,
// from chapter II.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#ECEFEA")
#let gold = rgb("#D6A55A")

// edition: the Modern English edition's label (cover-modern.typ)
#let cover(edition: none) = plate-cover(
  edition: edition,
  ground: rgb("#1C2B22"),
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 15pt, tracking: 0.12em,
      fill: ink.transparentize(35%), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 22pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.5in, dy: 3.35in, box(width: 4.5in, {
      set align(center)
      set par(leading: 0.55em, spacing: 0pt)
      [#plain[I find then]#h(0.12in)#gilt[a law,]]
      v(0.08in)
      plain[that, when I would do good,]
      v(0.1in)
      gilt[evil is present]
      v(0.1in)
      gilt[with me.]
      v(0.2in)
      caps([Romans vii. 21], 9pt, gold.transparentize(20%), tracking: 0.25em)
    }))
  }),
  title-y: 0.85in,
  seal: press-seal,
  title: [Indwelling Sin],
  subtitle: [
    The Nature, Power, Deceit, and Prevalency \
    of the Remainders of Indwelling Sin in Believers
  ],
  author: [John Owen],
  spine-title: [Indwelling Sin],
  spine-author: [Owen],
  pages: 292,
  ink: ink,
  accent: gold,
  // as Mortification: the seal and name plate in gold, the fountain and
  // lettering cut in the ground's dark
  label: gold,
  paper: rgb("#121D17"),
  epigraph: [
    The soul is its home, there it dwells, and is no wanderer. Wherever you
    are, whatever you are about, this law of sin is always in you.
  ],
  epigraph-source: [From Chapter II],
)

#cover()
