#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.1": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), with no picture: the verse on Owen's 1648 title
// page, Matthew 20:28, is the image, set in the title's type with "to give
// his life" and "a ransom for many" in gold (the book's argument: a ransom
// paid for many, and so their certain deliverance). Slate and gold, apart
// from The Mortification of Sin's oxblood. The back carries Owen's dilemma
// to the Universalists, from Book I, chapter III.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#ECEEEA")
#let gold = rgb("#D2A859")

#plate-cover(
  ground: rgb("#1D2830"),
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 13pt, tracking: 0.12em,
      fill: ink.transparentize(35%), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 19pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.5in, dy: 3.35in, box(width: 4.5in, {
      set align(center)
      set par(leading: 0.6em, spacing: 0pt)
      [#plain[The Son of man came] \
       #plain[not to be ministered unto,] \
       #plain[but to minister, and] \
       #gilt[to give his life] \
       #gilt[a ransom for many.]]
      v(0.2in)
      caps([Matthew xx. 28], 9pt, gold.transparentize(20%), tracking: 0.25em)
    }))
  }),
  title-y: 0.85in,
  title-size: 27pt,
  seal: press-seal,
  title: [The Death of Death],
  tail: [in the Death of Christ],
  subtitle: [
    A Treatise of the Redemption and Reconciliation \
    That Is in the Blood of Christ
  ],
  author: [John Owen],
  spine-title: [The Death of Death],
  spine-author: [Owen],
  pages: 484,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#141C22"),
  epigraph: [
    God imposed his wrath due unto, and Christ underwent the pains of hell
    for, either all the sins of all men, or all the sins of some men, or some
    sins of all men.
  ],
  epigraph-source: [From Book I, Chapter III],
)
