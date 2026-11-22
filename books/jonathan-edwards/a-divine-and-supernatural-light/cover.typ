#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.15.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ): a small framed picture on a dark ground, as God
// Glorified (the editor's choice for a short book, 2026-11-15). The picture is
// the sermon's own: "There is a difference between having an opinion that God is
// holy and gracious, and having a sense of the loveliness and beauty of that
// holiness and grace. There is a difference between having a rational judgment
// that honey is sweet, and having a sense of its sweetness" (part I). A piece of
// honeycomb, its cells catching the light, one drop of honey falling: drawn in
// Typst (a simple emblem, cover-design rule 4), gold on a night-blue ground, the
// light in the dark of the sermon's "spiritual darkness and blindness".
// Opaque throughout: every tint is a colour mixed with the ground, never alpha.
//
// ./fgb build gives the cover its compiled interior's page count and trim, and
// with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#EFE9DA")
#let gold = rgb("#D9A84A")
#let ground = rgb("#1D2333")
#let panel = rgb("#141926")
#let honey = rgb("#C98A1E")
#let honey-light = rgb("#F0C35C")
#let wax = rgb("#E6CF8F")

// a pointy-topped hexagon of circumradius r, centred at (cx, cy)
#let hex(cx, cy, r, fill: none, stroke: none) = {
  let pts = range(6).map(i => {
    let a = (60 * i + 30) * 1deg
    (cx + r * calc.cos(a), cy + r * calc.sin(a))
  })
  place(top + left, polygon(fill: fill, stroke: stroke, ..pts))
}

// the comb: a few rows of cells, some full of honey, some empty wax, the
// cells nearest the light brightest
#let comb(w, h) = box(width: w, height: h, clip: true, {
  // the light falls from above: a soft radial glow on the panel (an opaque gradient)
  let lx = w * 0.5
  let ly = h * 0.05
  place(rect(width: w, height: h, fill: gradient.radial(rgb("#3A3A3C"), panel, center: (50%, 5%), radius: 95%)))
  let r = 0.17in
  let dx = calc.sqrt(3) * r
  let dy = 1.5 * r
  // which cells exist (rows from the top: first and last column, w = empty wax, h = honey)
  let rows = (
    (2, 6, "wwhhw"),
    (1, 6, "hhhhhw"),
    (1, 7, "whhhhhw"),
    (2, 6, "hhhhh"),
    (2, 5, "whhw"),
    (3, 5, "hhw"),
  )
  // centred: the widest row spans columns 1 to 7
  let x0 = w / 2 - 4 * dx
  let y0 = (h - (2 * r + 5 * dy + 0.55in)) / 2 + r
  for (j, row) in rows.enumerate() {
    let (first, last, kinds) = row
    for i in range(first, last + 1) {
      let kind = kinds.at(i - first, default: "w")
      let cx = x0 + i * dx + (if calc.rem(j, 2) == 1 { dx / 2 } else { 0in })
      let cy = y0 + j * dy
      // nearer the light, brighter
      let d = calc.sqrt(calc.pow((cx - lx) / 1in, 2) + calc.pow((cy - ly) / 1in, 2))
      let lit = calc.max(0, calc.min(1, 1.35 - d / 1.6))
      let wall = color.mix((wax, 45% + 50% * lit), (panel, 55% - 50% * lit))
      let fill = if kind == "h" {
        color.mix((honey-light, 20% + 70% * lit), (honey, 80% - 70% * lit))
      } else {
        color.mix((rgb("#3A3426"), 70%), (panel, 30%))
      }
      hex(cx, cy, r, fill: wall)
      hex(cx, cy, r * 0.8, fill: fill)
      if kind == "h" {
        // a glint on each full cell, toward the light
        place(dx: cx - r * 0.2, dy: cy - r * 0.45,
          ellipse(width: r * 0.4, height: r * 0.16,
            fill: color.mix((rgb("#FFF1C8"), 30% + 60% * lit), (honey-light, 70% - 60% * lit))))
      }
    }
  }
  // one drop of honey falling from a cell of the lowest row
  let bx = x0 + 4.5 * dx
  let by = y0 + 5 * dy + r * 0.85
  place(dx: bx - 0.016in, dy: by, rect(width: 0.032in, height: 0.24in, fill: honey))
  place(dx: bx - 0.045in, dy: by + 0.23in,
    polygon(fill: honey, (0in, 0.1in), (0.045in, 0in), (0.09in, 0.1in)))
  place(dx: bx - 0.07in, dy: by + 0.28in, circle(radius: 0.07in, fill: honey))
  place(dx: bx - 0.04in, dy: by + 0.31in, circle(radius: 0.02in, fill: honey-light))
})

// edition: a Modern English edition's label, if one is ever made
#let cover(edition: none) = plate-cover(
  edition: edition,
  ground: ground,
  // the picture in a frame of gold, between the title block and the seal
  art: box(width: 4.25in, height: 6.875in,
    place(dx: 0.55in, dy: 2.3in, block(width: 3.15in, height: 2.6in, clip: true,
      stroke: 0.6pt + gold, comb(3.15in, 2.6in)))),
  // the pocket trim as the default too (./fgb build passes it for the print
  // cover, but the ebook's front is rendered without it), as Sinners' cover does
  trim-width: 4.25in,
  trim-height: 6.875in,
  title-y: 0.62in,
  seal: press-seal,
  title: [A Divine and],
  tail: [Supernatural Light],
  subtitle: [A Sermon Preached at Northampton, 1734],
  author: [Jonathan Edwards],
  spine-author: [Edwards],
  title-size: 22pt,
  pages: 40,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#121722"),
  epigraph: [
    There is a difference between having a rational judgment that honey is sweet,
    and having a sense of its sweetness. A man may have the former, that knows not
    how honey tastes; but a man can't have the latter unless he has an idea of the
    taste of honey in his mind.
  ],
  epigraph-source: [A Divine and Supernatural Light],
)

#cover()
