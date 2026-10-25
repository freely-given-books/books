#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.1": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The image is the verse on the 1609 title page,
// Proverbs 24:3-4, under a house drawn in gold line: the book is "a short
// survey of the right manner of erecting and ordering a family", and the
// verse is its motto. Perkins's mulberry, taken deep for the plate design,
// with gold. The back keeps the book's Joshua 24:15.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#F1E9E2")
#let gold = rgb("#D4A95C")
#let ground = rgb("#4A2433")

// A plain gabled house, a door and two windows, in gold line.
#let house(w) = {
  let s = w / 100
  let st = (paint: gold, thickness: 1.4pt, join: "miter")
  box(width: w, height: 86 * s, {
    // roof and walls
    place(polygon(stroke: st, fill: none, (6 * s, 34 * s), (50 * s, 2 * s), (94 * s, 34 * s)))
    place(dx: 14 * s, dy: 34 * s, rect(stroke: st, width: 72 * s, height: 50 * s))
    // chimney
    place(polygon(stroke: st, (68 * s, 18.9 * s), (68 * s, 8 * s), (76 * s, 8 * s), (76 * s, 24.8 * s)))
    // door, arched
    place(dx: 43 * s, dy: 56 * s, rect(stroke: st, width: 14 * s, height: 28 * s, radius: (top: 7 * s)))
    // windows, each with its cross
    for x in (22, 64) {
      place(dx: x * s, dy: 44 * s, rect(stroke: st, width: 14 * s, height: 14 * s))
      place(line(stroke: st, start: ((x + 7) * s, 44 * s), end: ((x + 7) * s, 58 * s)))
      place(line(stroke: st, start: (x * s, 51 * s), end: ((x + 14) * s, 51 * s)))
    }
    // the ground line
    place(line(stroke: st, start: (0pt, 84 * s), end: (100 * s, 84 * s)))
  })
}

#plate-cover(
  ground: ground,
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 12pt, tracking: 0.12em,
      fill: ink.transparentize(30%), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 17pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.5in, dy: 3.05in, box(width: 4.5in, {
      set align(center)
      house(1.35in)
      v(0.3in)
      set par(leading: 0.62em, spacing: 0pt)
      [#plain[Through wisdom is] \
       #gilt[an house built,] \
       #plain[and by understanding] \
       #plain[it is established.]]
      v(0.2in)
      caps([Proverbs xxiv. 3], 9pt, gold.transparentize(20%), tracking: 0.25em)
    }))
  }),
  title-y: 0.85in,
  title-size: 32pt,
  seal: press-seal,
  title: [Christian Economy],
  subtitle: [
    Or, A Short Survey of the Right Manner of Erecting \
    and Ordering a Family, According to the Scriptures
  ],
  author: [William Perkins],
  spine-title: [Christian Economy],
  spine-author: [Perkins],
  pages: 126,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#2E1520"),
  epigraph: [
    And if it seem evil unto you to serve the LORD, choose you this day whom
    ye will serve… but as for me and my house, we will serve the LORD.
  ],
  epigraph-source: [Joshua 24:15],
)
