#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.2": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), with no picture: the whole book is an exposition
// of one verse, Romans 8:13, so the verse is the image, set in the title's
// type with "mortify" and "ye shall live" in gold. Oxblood and gold. The back
// carries the book's best-known sentence, from chapter II.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#F1ECE2")
#let gold = rgb("#D6A55A")

#plate-cover(
  ground: rgb("#3A1E1E"),
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 15pt, tracking: 0.12em,
      fill: ink.transparentize(35%), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 22pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.5in, dy: 3.45in, box(width: 4.5in, {
      set align(center)
      set par(leading: 0.55em, spacing: 0pt)
      [#plain[If ye through the Spirit] \
       #plain[do]#h(0.12in)#gilt[mortify] \
       #plain[the deeds of the body,]]
      v(0.08in)
      gilt[ye shall live.]
      v(0.2in)
      caps([Romans viii. 13], 9pt, gold.transparentize(20%), tracking: 0.25em)
    }))
  }),
  title-y: 0.85in,
  seal: press-seal,
  title: [The Mortification],
  tail: [of Sin],
  subtitle: [
    Of the Mortification of Sin in Believers: \
    the Necessity, Nature, and Means of It
  ],
  author: [John Owen],
  spine-title: [The Mortification of Sin],
  spine-author: [Owen],
  pages: 151,
  ink: ink,
  accent: gold,
  // the seal and name plate in gold, the fountain and lettering cut in the
  // ground's dark: dark-on-oxblood was lost against the ground
  label: gold,
  paper: rgb("#241212"),
  epigraph: [
    Do you mortify; do you make it your daily work; be always at it whilst
    you live; cease not a day from this work; be killing sin or it will be
    killing you.
  ],
  epigraph-source: [From Chapter II],
  // isbn: "978-0-000000-00-0",
)
