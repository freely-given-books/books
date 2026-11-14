#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.15.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), as Owen's sin books and Religious Affections: no
// picture, the sermon's text is the image. Edwards preaches on 1 Cor 1:29-31, so its
// close is set in the title's type with "glory in the Lord" in gold. The back gives
// the doctrine in his words. The ground's colour is a placeholder until the editor
// chooses one (EDITION-RULES 7). At about 40 pages the spine carries nothing.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#EEEBE3")
#let gold = rgb("#D6A55A")
#let ground = rgb("#23332E")

// opaque: the ink mixed with the ground it sits on, not transparent (Lulu flattens
// transparency into image tiles: scripts/plate_cover.typ)
#plate-cover(
  ground: ground,
  art: box(width: 4.25in, height: 6.875in, {
    let plain(body) = text(font: DISPLAY, size: 11pt, tracking: 0.12em,
      fill: color.mix((ink, 65%), (ground, 35%)), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 16pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.4in, dy: 3.0in, box(width: 3.45in, {
      set align(center)
      set par(leading: 0.55em, spacing: 0pt)
      plain[He that glorieth,]
      v(0.08in)
      plain[let him]
      v(0.1in)
      gilt[glory in the Lord.]
      v(0.18in)
      caps([1 Corinthians i. 31], 7.5pt, color.mix((gold, 80%), (ground, 20%)), tracking: 0.25em)
    }))
  }),
  title-y: 0.75in,
  seal: press-seal,
  title: [God Glorified],
  tail: [in Man's Dependence],
  subtitle: [A Sermon Preached in Boston, July 8, 1731],
  author: [Jonathan Edwards],
  spine-author: [Edwards],
  title-size: 30pt,
  pages: 40,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#17221F"),
  epigraph: [
    God is glorified in the work of redemption in this, that there appears in it
    so absolute and universal a dependence of the redeemed on him.
  ],
  epigraph-source: [God Glorified in Man's Dependence],
)
