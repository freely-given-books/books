// Full-wrap cover for Gouge's Of Domestical Duties (the editor's choice, 2026-11-21):
// "thy children like olive plants round about thy table" (Psalm 128:3). The work's
// eight treatises are places at one household table, seen from above: the exposition
// at the head, man and wife at the foot, and down the sides the pairs Gouge treats
// facing each other (wives and husbands, children and parents, servants and masters).
// The table is spread with a cloth in the volume's green, olive plants round about it,
// and this volume's places are laid with gold plates.
//
// A cream sheet the whole way round, with a band of the volume's green across head and
// foot (front, spine and back alike, so the set's greens show on the shelf); the
// spine is cream, so a fold a little off true shows no stripe. The type is dark ink
// throughout, which reads on cream and on every green of the set. Cinzel over EB
// Garamond, the seal and name plate at the foot of the front, the surname on the
// spine and the seal at its foot (plate_cover.typ's house parts). Nothing is drawn
// semi-transparent (Lulu flattens transparency into image tiles).
//
//   #import "../../../scripts/table_cover.typ": table-cover
//   #table-cover(seal: press-seal, cloth: rgb("#8AA45A"), places: (...), current: (4, 5), ...)
//
// ./fgb build passes the interior's page count and trim (--input pages=N
// trim-width=W trim-height=H), so the spine is always Lulu's `pages / 444 +
// 0.06in`; with --input front-only=true the front alone is the ebook cover.

#import "plate_cover.typ": BLEED, SAFETY, SPINE_TRIM, DISPLAY, SERIF, caps

#let CREAM = rgb("#F6F1E1")
#let INK = rgb("#1E2913")
#let HONEY = rgb("#DCA53A")
// olive leaves: dark, mid and light, the same on every volume
#let LEAVES = (rgb("#5F7A3E"), rgb("#76914B"), rgb("#93AB62"))
#let OLIVE = rgb("#3B4724")

#let lettered(body, size, tracking: 0.03em, weight: "regular", fill: INK) = text(
  font: DISPLAY, size: size, tracking: tracking, weight: weight, fill: fill, upper(body))

// An olive sprig, a stem with leaves in pairs and an olive, laid from (x, y) at
// an angle.
#let sprig(x, y, angle, len: 0.7in) = place(dx: x, dy: y, rotate(angle, origin: top + left,
  box(width: 0pt, height: 0pt, {
    place(line(start: (0in, 0in), end: (len, 0in), stroke: 1.2pt + LEAVES.at(0)))
    for i in range(5) {
      let p = 0.12in + i * (len - 0.16in) / 4.5
      let s = if calc.even(i) { 1 } else { -1 }
      let l = 0.34in - i * 0.03in
      place(dx: p, dy: 0in, rotate(s * 35deg, origin: left + horizon,
        place(dy: -0.045in, ellipse(width: l, height: 0.09in, fill: LEAVES.at(calc.rem(i, 3))))))
    }
    place(dx: len - 0.02in, dy: -0.045in, ellipse(width: 0.3in, height: 0.09in, fill: LEAVES.at(1)))
    place(dx: len * 0.45, dy: 0.06in, ellipse(width: 0.11in, height: 0.14in, fill: OLIVE))
  })))

// A place at the table: laid (a gold plate with a dark rim, its numeral bold) or
// not (a cream plate, a quiet outline).
#let place-plate(n, laid, x, y, d: 0.46in) = {
  let size = if n == [VIII] { 8pt } else { 10pt }
  if laid {
    place(dx: x - d / 2 - 0.04in, dy: y - d / 2 - 0.04in, circle(radius: d / 2 + 0.04in, fill: INK))
    place(dx: x - d / 2, dy: y - d / 2, circle(radius: d / 2, fill: HONEY))
    place(dx: x - d / 2 + 0.06in, dy: y - d / 2 + 0.06in, circle(radius: d / 2 - 0.06in,
      stroke: 0.6pt + HONEY.darken(28%),
      align(center + horizon, text(font: DISPLAY, weight: "bold", size: size, fill: INK, n))))
  } else {
    place(dx: x - d / 2, dy: y - d / 2, circle(radius: d / 2, fill: CREAM,
      stroke: 0.6pt + color.mix((INK, 45%), (CREAM, 55%)),
      align(center + horizon, text(font: DISPLAY, size: size,
        fill: color.mix((INK, 62%), (CREAM, 38%)), n))))
  }
}

// A place's name beside the table: right of `x` (side: left), left of it (right),
// or centred on it (top, bottom).
#let place-label(name, laid, x, y, side, w: 1.3in) = {
  let lab = text(font: SERIF, size: if laid { 9.5pt } else { 8.5pt }, tracking: 0.16em,
    fill: INK, weight: if laid { "bold" } else { "regular" }, upper(name))
  if side == left { place(dx: x - w, dy: y - 0.07in, box(width: w, align(right, lab))) }
  else if side == right { place(dx: x, dy: y - 0.07in, box(width: w, align(left, lab))) }
  else { place(dx: x - w, dy: y - 0.07in, box(width: 2 * w, align(center, lab))) }
}

#let table-cover(
  seal: none,
  // the volume's green: the table's cloth, and the bands at head and foot
  cloth: rgb("#8AA45A"),
  author: [William Gouge],
  spine-author: [Gouge],
  title: [Of Domestical Duties],
  imprint: [Eight treatises, London, 1622],
  volume: [Volume I],
  volume-number: [I],
  // the eight places: (numeral, name at the table, full title), in the work's order;
  // the first sits at the head, the second at the foot, then the pairs down the sides
  places: (),
  // the indexes of this volume's places
  current: (),
  // the edition, for a second edition of the same volume ([Modern English]): a
  // small ruled label under the imprint and a mark on the spine
  edition: none,
  // the spine's type and marks are sized to this width, the thinnest volume's
  // safe strip, so every volume of the set shelves alike
  spine-fit: none,
  back-lead: none,
  epigraph: none,
  epigraph-source: none,
  // the verse the front is drawn from, small above the seal on the back
  psalm: [Thy children like olive plants round about thy table.],
  isbn: none,
  pages: 200,
  trim-width: 5.5in,
  trim-height: 8.5in,
  front-only: sys.inputs.at("front-only", default: "false") == "true",
) = {
  let pages = int(sys.inputs.at("pages", default: str(pages)))
  let trim-width = if "trim-width" in sys.inputs { float(sys.inputs.at("trim-width")) * 1in } else { trim-width }
  let trim-height = if "trim-height" in sys.inputs { float(sys.inputs.at("trim-height")) * 1in } else { trim-height }
  let spine = (pages / 444.0 + 0.06) * 1in
  let page-width = 2 * BLEED + 2 * trim-width + spine
  let page-height = 2 * BLEED + trim-height
  let back-x = BLEED
  let spine-x = BLEED + trim-width
  let front-x = spine-x + spine
  // the bands' depth inside the trim
  let band = 0.24in

  set text(font: SERIF, fill: INK)
  set par(spacing: 0pt, leading: 0.35em, justify: false)
  set page(width: page-width, height: page-height, margin: 0pt) if not front-only
  set page(width: trim-width, height: trim-height, margin: 0pt) if front-only

  let wrap(body) = if front-only {
    place(top + left, dx: -front-x, dy: -BLEED, box(width: page-width, height: page-height, body))
  } else { body }

  wrap({
    place(top + left, rect(width: page-width, height: page-height, fill: CREAM))
    place(top + left, rect(width: page-width, height: BLEED + band, fill: cloth))
    place(bottom + left, rect(width: page-width, height: BLEED + band, fill: cloth))

    // --- front ------------------------------------------------------------------
    place(top + left, dx: front-x, dy: BLEED, box(width: trim-width, height: trim-height, {
      let W = trim-width
      let cx = W / 2
      // the title, centred
      place(dx: 0in, dy: SAFETY + 0.05in, box(width: W, {
        set align(center)
        caps(author, 9.5pt, LEAVES.at(0), tracking: 0.3em)
        v(0.18in)
        lettered([Of], 13pt, tracking: 0.4em)
        v(0.1in)
        lettered([Domestical], 32pt, weight: "bold", tracking: 0.02em)
        v(0.1in)
        lettered([Duties], 21pt, tracking: 0.36em)
        v(0.14in)
        text(size: 11.5pt, style: "italic", imprint + [ #h(0.3em)·#h(0.3em) ] + volume)
        if edition != none {
          v(0.1in)
          box(stroke: (top: 0.6pt + LEAVES.at(0), bottom: 0.6pt + LEAVES.at(0)),
            inset: (x: 0.04in, y: 0.07in), caps(edition, 8pt, LEAVES.at(0)))
        }
      }))
      // the table, its cloth, and the olive plants round about it
      let tw = 1.35in
      let th = 3.2in
      let tx = (W - tw) / 2
      let ty = if edition != none { 2.9in } else { 2.75in }
      sprig(tx - 0.3in, ty + 0.1in, 200deg)
      sprig(tx + tw + 0.3in, ty + 0.1in, -20deg)
      sprig(tx - 0.3in, ty + th - 0.1in, 160deg)
      sprig(tx + tw + 0.3in, ty + th - 0.1in, 20deg)
      place(dx: tx, dy: ty, rect(width: tw, height: th, radius: 0.1in, fill: cloth,
        stroke: 1pt + LEAVES.at(0)))
      place(dx: tx + 0.09in, dy: ty + 0.09in, rect(width: tw - 0.18in, height: th - 0.18in,
        radius: 0.06in, stroke: (paint: CREAM, thickness: 0.6pt, dash: "dotted")))
      let laid(i) = i in current
      place-plate(places.at(0).at(0), laid(0), cx, ty + 0.38in)
      place-plate(places.at(1).at(0), laid(1), cx, ty + th - 0.38in)
      place-label(places.at(0).at(1), laid(0), cx, ty - 0.3in, top)
      place-label(places.at(1).at(1), laid(1), cx, ty + th + 0.24in, bottom)
      for (k, (a, b)) in ((2, 3), (4, 5), (6, 7)).enumerate() {
        let y = ty + 0.92in + k * 0.68in
        place-plate(places.at(a).at(0), laid(a), tx + 0.32in, y)
        place-plate(places.at(b).at(0), laid(b), tx + tw - 0.32in, y)
        place-label(places.at(a).at(1), laid(a), tx - 0.18in, y, left)
        place-label(places.at(b).at(1), laid(b), tx + tw + 0.18in, y, right)
      }
      // this volume's treatises in full, under the table
      let seal-y = trim-height - SAFETY - 0.92in
      place(dx: SAFETY, dy: ty + th + 0.45in, box(width: W - 2 * SAFETY,
        height: seal-y - (ty + th + 0.45in) - 0.08in, align(center + horizon, {
          set par(leading: 0.4em)
          let n = current.len()
          for i in current {
            text(size: if n > 2 { 10.5pt } else { 11.5pt }, style: "italic", places.at(i).at(2))
            if i != current.last() { v(0.06in) }
          }
        })))
      if seal != none {
        place(center + top, dy: seal-y, seal(width: 0.6in, roundel: LEAVES.at(0), fountain: CREAM))
        place(center + top, dy: seal-y + 0.7in, box(fill: LEAVES.at(0), inset: (x: 0.12in, y: 0.06in),
          caps([Common Weal Press], 6pt, CREAM, tracking: 0.3em)))
      }
    }))

    // --- spine ------------------------------------------------------------------
    // cream between the bands; the surname and title run down it, the volume's
    // number on a gold plate and the seal at the foot, all inside 1/8in of each fold
    let safe = spine - 2 * SPINE_TRIM
    let fit = if spine-fit != none { calc.min(spine-fit, safe) } else { safe }
    let s = calc.min(fit, 0.5in)
    place(top + left, dx: spine-x, dy: BLEED, box(width: spine, height: trim-height, {
      set align(center)
      if seal != none {
        place(bottom + center, dy: -0.5in, seal(width: s, roundel: LEAVES.at(0), fountain: CREAM))
      }
      let d = calc.min(0.36in, fit)
      let mark-y = 0.5in + s + 0.14in
      place(bottom + center, dy: -mark-y, box(width: d, height: d, radius: 50%, fill: INK,
        inset: 0.03in * (d / 0.36in), box(width: 100%, height: 100%, radius: 50%, fill: HONEY,
          align(center + horizon, text(font: DISPLAY, weight: "bold", size: 9pt * (d / 0.36in),
            fill: INK, volume-number)))))
      let size = calc.min(11pt, fit / 1in * 72pt * 0.5)
      let top-y = 0.5in
      place(top + center, dy: top-y, rotate(90deg, reflow: true,
        box(width: trim-height - top-y - mark-y - d - 0.16in, height: safe,
          align(left + horizon, {
            text(weight: "medium", size: size * 0.9, tracking: 0.1em, fill: LEAVES.at(0), upper(spine-author))
            h(0.14in)
            text(size: 6pt, fill: LEAVES.at(0), sym.diamond.filled)
            h(0.14in)
            text(font: DISPLAY, size: size, tracking: 0.12em, weight: "bold", fill: INK, upper(title))
            if edition != none {
              h(0.1in); text(size: 6pt, fill: LEAVES.at(0), sym.diamond.filled); h(0.1in)
              text(weight: "medium", size: size * 0.6, tracking: 0.1em, fill: LEAVES.at(0), upper(edition))
            }
          }))))
    }))

    // --- back -------------------------------------------------------------------
    place(top + left, dx: back-x + SAFETY, dy: BLEED + SAFETY,
      box(width: trim-width - 2 * SAFETY, height: trim-height - 2 * SAFETY, {
        set align(center)
        v(0.45in)
        if back-lead != none {
          block(width: 100%, inset: (x: 0.1in), {
            set par(leading: 0.7em)
            text(size: 11pt, back-lead)
          })
          v(0.45in)
        }
        if epigraph != none {
          // a pair of sprigs, as round the table
          box(width: 1.6in, height: 0.3in, {
            sprig(0.62in, 0.15in, 180deg, len: 0.55in)
            sprig(0.98in, 0.15in, 0deg, len: 0.55in)
          })
          v(0.3in)
          block(width: 100%, inset: (x: 0.1in), {
            set par(leading: 0.7em)
            text(size: 12.5pt, style: "italic", epigraph)
          })
          if epigraph-source != none {
            v(0.2in)
            caps(epigraph-source, 8.5pt, LEAVES.at(0), tracking: 0.16em)
          }
        }
        v(1fr)
        // the verse the front is drawn from
        block(width: 100%, inset: (x: 0.3in), {
          set par(leading: 0.6em)
          text(size: 10pt, style: "italic", psalm)
          v(0.1in)
          caps([Psalm cxxviii. 3], 7.5pt, LEAVES.at(0), tracking: 0.16em)
        })
        v(0.45in)
        grid(columns: (1fr, auto), align: (left + bottom, right + bottom),
          grid(columns: 2, column-gutter: 0.12in, align: left + horizon,
            if seal != none { seal(width: 0.46in, roundel: LEAVES.at(0), fountain: CREAM) },
            caps([Common Weal Press], 7pt, LEAVES.at(0), tracking: 0.2em)),
          if isbn != none {
            stack(box(fill: white, width: 2in, height: 1.2in), v(0.06in),
              text(size: 7.5pt)[ISBN #isbn])
          } else { box(width: 2in, height: 1.2in) })
      }))
  })
}
