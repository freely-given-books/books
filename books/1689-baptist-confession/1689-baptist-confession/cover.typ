// Cover for The 1689 Baptist Confession of Faith, with Catechisms: the full
// wrap for Lulu, or with `--input front-only=true` the front alone (the
// ebook cover).
//
// The book's own navy and gold, dressed in the engraved design's frame
// (wip/engraved-cover): a double gold rule with scrolled corners and a
// fleur-de-lis (art/corner.svg, recoloured), diamond rules, and the press's
// mark and name at the foot of front, spine and back.
//
// ./fgb build passes the interior's page count and trim (--input pages=N
// trim-width=W trim-height=H), so the spine is always Lulu's
// `pages / 444 + 0.06in`. Compiled on its own: typst compile cover.typ cover.pdf

#let pages = int(sys.inputs.at("pages", default: "210"))
#let trim-width = float(sys.inputs.at("trim-width", default: "5.5")) * 1in
#let trim-height = float(sys.inputs.at("trim-height", default: "8.5")) * 1in
#let front-only = sys.inputs.at("front-only", default: "false") == "true"

#let BLEED = 0.125in
#let SAFETY = 0.5in
#let FRAME_INSET = 0.3in
#let spine = (pages / 444.0 + 0.06) * 1in

#let navy = rgb("#1a2744")
#let gold = rgb("#c9a227")
#let cream = rgb("#f4e9d6")
#let soft = cream.transparentize(25%)

#let SERIF = "Libertinus Serif"
#let DISPLAY = ("Libertinus Serif Display", "Libertinus Serif")
#set text(font: SERIF, fill: cream, kerning: true, hyphenate: false)

// The press's mark, white line work, for a dark ground (from
// common-weal-press/mark-white.svg).
#let MARK = "art/mark-white.svg"
#let mark(size) = image(MARK, width: size)

// art/corner.svg is drawn in the engraved design's gold; this book's is warmer.
#let CORNER = bytes(read("art/corner.svg").replace("#A9843F", gold.to-hex()))

// A gold rule broken by a diamond.
#let diamond-rule(width: 1.7in) = box(width: width, grid(
  columns: (1fr, auto, 1fr), column-gutter: 0.09in, align: horizon,
  line(length: 100%, stroke: 0.6pt + gold),
  text(size: 7pt, fill: gold, sym.diamond.filled),
  line(length: 100%, stroke: 0.6pt + gold)))

// Spaced small capitals.
#let caps(body, size, tracking: 0.18em, fill: cream) = text(
  size: size, tracking: tracking, fill: fill, smallcaps(all: true, body))

// The double frame: at each corner the inner rule bends in and ends in a
// scroll, a fleur-de-lis pointing into the corner (corner.svg is the top
// left, mirrored for the others); the straight inner rules stop where the
// ornament takes over.
#let frame(w, h, ornament: 0.55in) = {
  let gap = 0.07in
  let u = ornament / 100
  place(rect(width: w, height: h, stroke: 1.2pt + gold))
  let (x0, y0, x1, y1) = (gap, gap, w - gap, h - gap)
  let reach = 96 * u
  let s = 0.6pt + gold
  place(line(start: (x0 + reach, y0), end: (x1 - reach, y0), stroke: s))
  place(line(start: (x0 + reach, y1), end: (x1 - reach, y1), stroke: s))
  place(line(start: (x0, y0 + reach), end: (x0, y1 - reach), stroke: s))
  place(line(start: (x1, y0 + reach), end: (x1, y1 - reach), stroke: s))
  let o = 2 * u
  for (x, y, sx, sy) in (
    (x0 - o, y0 - o, 1, 1), (x1 + o - ornament, y0 - o, -1, 1),
    (x0 - o, y1 + o - ornament, 1, -1), (x1 + o - ornament, y1 + o - ornament, -1, -1),
  ) {
    place(dx: x, dy: y, scale(x: sx * 100%, y: sy * 100%,
      image(CORNER, format: "svg", width: ornament)))
  }
}

// One panel (front or back): the frame, and the content inside the safety line.
#let panel(body) = box(width: trim-width, height: trim-height, {
  place(dx: FRAME_INSET, dy: FRAME_INSET,
    frame(trim-width - 2 * FRAME_INSET, trim-height - 2 * FRAME_INSET))
  place(dx: SAFETY, dy: SAFETY,
    box(width: trim-width - 2 * SAFETY, height: trim-height - 2 * SAFETY, {
      set par(spacing: 0pt)
      body
    }))
})

#let front = panel({
  set align(center)
  v(0.42in)
  diamond-rule()
  v(1fr)
  text(font: DISPLAY, size: 70pt, fill: gold, tracking: 0.05em)[1689]
  v(0.34in)
  caps([The London], 12.5pt, tracking: 0.34em)
  v(0.24in)
  text(font: DISPLAY, size: 48pt, tracking: 0.05em)[BAPTIST]
  v(0.2in)
  text(font: DISPLAY, size: 25pt, tracking: 0.12em)[CONFESSION]
  v(0.22in)
  caps([of Faith], 12.5pt, tracking: 0.34em)
  v(0.42in)
  diamond-rule()
  v(0.34in)
  text(size: 15.5pt, style: "italic")[With Catechisms]
  v(0.16in)
  caps([The Baptist Catechism · 1695], 9.5pt, tracking: 0.14em, fill: soft)
  v(0.09in)
  caps([An Orthodox Catechism · 1680], 9.5pt, tracking: 0.14em, fill: soft)
  v(1.3fr)
  caps([Sola Scriptura], 9pt, tracking: 0.3em, fill: gold)
  v(0.24in)
  mark(0.6in)
  v(0.1in)
  caps([Common Weal Press], 8pt, tracking: 0.24em, fill: soft)
})

#let back = panel({
  set align(center)
  // the back cover's words as the book has always had them: the closing
  // prayer of the confession's preface, alone
  v(1fr)
  diamond-rule(width: 1.3in)
  v(0.32in)
  pad(x: 0.15in, {
    set par(justify: true, leading: 0.8em)
    text(size: 11pt, style: "italic")[We shall conclude with our earnest
      prayer, that the God of all grace, will pour out those measures of his
      holy Spirit upon us, that the profession of truth may be accompanied
      with the sound belief, and diligent practice of it by us; that his name
      may in all things be glorified, through Jesus Christ our Lord. Amen.]
  })
  v(0.32in)
  diamond-rule(width: 1.3in)
  v(1fr)
  // the imprint at the foot, left of centre; the lower right is kept clear
  // for a barcode (2in x 1.2in) once the book has an ISBN
  pad(left: 0.42in, bottom: 0.2in, align(left, stack(dir: ltr, spacing: 0.12in,
    mark(0.46in),
    align(horizon, caps([Common Weal Press], 7.5pt, tracking: 0.2em, fill: soft)))))
})

// The spine (under 0.6in: title and author run along it, no art).
#let spine-panel = box(width: spine, height: trim-height, {
  let rules(y) = place(dx: 0.07in, dy: y, stack(spacing: 0.035in,
    line(length: spine - 0.14in, stroke: 0.9pt + gold),
    line(length: spine - 0.14in, stroke: 0.4pt + gold)))
  rules(0.42in)
  rules(trim-height - 0.47in)
  place(center + horizon, dy: -0.15in, rotate(90deg, reflow: true,
    box(width: trim-height - 2.2in, align(center + horizon, {
      text(font: DISPLAY, size: 11pt, fill: gold, tracking: 0.08em)[1689]
      h(0.12in)
      caps([The London Baptist Confession of Faith], 10pt, tracking: 0.12em)
      h(0.12in)
      text(size: 8pt, fill: gold, sym.diamond.filled)
      h(0.12in)
      text(size: 9pt, style: "italic", fill: soft)[With Catechisms]
    }))))
  place(center + bottom, dy: -0.66in, mark(spine - 0.14in))
})

#if front-only {
  set page(width: trim-width, height: trim-height, margin: 0pt, fill: navy)
  front
} else {
  set page(width: 2 * trim-width + spine + 2 * BLEED, height: trim-height + 2 * BLEED,
    margin: 0pt, fill: navy)
  place(dx: BLEED, dy: BLEED, back)
  place(dx: BLEED + trim-width, dy: BLEED, spine-panel)
  place(dx: BLEED + trim-width + spine, dy: BLEED, front)
}
