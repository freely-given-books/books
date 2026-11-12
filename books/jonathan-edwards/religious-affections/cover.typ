#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.15.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), as Owen's sin books: no picture, the book's text is
// the image. The treatise opens on 1 Peter 1:8, so the verse is set in the
// title's type with "joy unspeakable" and "full of glory" in gold. The ground's
// colour is a placeholder until the editor chooses one (EDITION-RULES 7).
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#ECEDF0")
#let gold = rgb("#D6A55A")

#plate-cover(
  ground: rgb("#1B2238"),
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 15pt, tracking: 0.12em,
      fill: ink.transparentize(35%), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 22pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.5in, dy: 3.35in, box(width: 4.5in, {
      set align(center)
      set par(leading: 0.55em, spacing: 0pt)
      plain[Whom having not seen, ye love;]
      v(0.08in)
      plain[yet believing, ye rejoice with]
      v(0.1in)
      gilt[joy unspeakable]
      v(0.1in)
      gilt[and full of glory.]
      v(0.2in)
      caps([1 Peter i. 8], 9pt, gold.transparentize(20%), tracking: 0.25em)
    }))
  }),
  title-y: 0.85in,
  seal: press-seal,
  title: [Religious Affections],
  subtitle: [A Treatise Concerning Religious Affections, in Three Parts],
  author: [Jonathan Edwards],
  spine-title: [Religious Affections],
  spine-author: [Edwards],
  pages: 500,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#11162A"),
  epigraph: [
    True religion, in great part, consists in holy affections.
  ],
  epigraph-source: [Part I],
)
