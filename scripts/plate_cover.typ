// Full-wrap cover for the Common Weal Press "plate" design: the front is an
// engraved plate (a black-ink engraving, cut out and printed in the book's
// own colours, or hand-tinted) run to the bleed, with the house's title block
// over it and the press's seal at the foot. The spine and back are the
// plate's own ground, so the book reads as one picture wrapped round it.
//
// What every plate cover shares (the house): Cinzel over EB Garamond; the
// title block (author, rule, title, subtitle); the seal and name plate at the
// foot of the front, the spine and the back. What each book brings: its plate,
// where the plate sits, its three colours, its back-cover words.
//
//   #import "../../../scripts/plate_cover.typ": *
//   #import "@local/fgbooks:0.14.0": press-seal
//   #plate-cover(
//     plate: read("art/plate.jpg", encoding: none),
//     plate-at: (dx: -0.85in, dy: -0.9in, width: 6.35in, height: 9.525in),
//     seal: press-seal,
//     title: [The Pilgrim’s], tail: [Progress], ...
//   )
//
// ./fgb build passes the interior's page count and trim (--input pages=N
// trim-width=W trim-height=H), so the spine is always Lulu's
// `pages / 444 + 0.06in`; with --input front-only=true the front alone is
// the ebook cover. The fonts come from the repository's fonts/ (./fgb sets
// TYPST_FONT_PATHS).
//
// PRINT: bleed 0.125in on every side; type at least 0.5in inside the trim;
// on the spine, inside 0.125in of each fold (Lulu trims to within that).
// The spine shares the back's ground, which is the plate's own colours, so a
// fold that drifts has no stripe to show.

#let BLEED = 0.125in
#let SAFETY = 0.5in
#let SPINE_TRIM = 0.125in
#let DISPLAY = "Cinzel"
#let SERIF = "EB Garamond"

#let caps(body, size, fill, tracking: 0.3em) = text(font: SERIF, size: size,
  tracking: tracking, fill: fill, upper(body))

#let diamond-rule(colour, width: 1.1in) = box(width: width, grid(
  columns: (1fr, auto, 1fr), column-gutter: 0.08in, align: horizon,
  line(length: 100%, stroke: 0.6pt + colour),
  text(size: 7pt, fill: colour, sym.diamond.filled),
  line(length: 100%, stroke: 0.6pt + colour)))

#let plate-cover(
  // the plate (bytes: read("art/plate.jpg", encoding: none)), and where it
  // sits relative to the front's trim box (it may run past it: it is cut at
  // the bleed and at the spine fold)
  plate: none,
  // or, in place of a plate image, art drawn in Typst: content laid on the
  // front, its origin the front's top-left trim corner (it may run into the
  // bleed). Drawn after the plate, before the title.
  art: none,
  // the front's own ground when it differs from the spine and back's (a
  // radial glow behind a vignette): a fill; none uses `ground`
  front-ground: none,
  // where the title block sits: its top, measured from the trim, and its
  // alignment (center, or left for a title set at the left margin)
  title-y: 0.6in,
  title-align: center,
  title-width: none,
  plate-at: (dx: 0in, dy: 0in, width: 5.5in, height: 8.5in),
  // the ground of the spine and back: gradient stops from head to foot,
  // matched to the plate's colours down its edge
  ground: ((rgb("#C0D0CA"), 0%), (rgb("#F4E7C0"), 42%), (rgb("#E8E4BC"), 52%), (rgb("#BEC898"), 100%)),
  // the press's seal (fgbooks' press-seal), so the cover need not reach
  // the template itself
  seal: none,
  title: [Title],
  tail: none,
  subtitle: none,
  author: [Author],
  spine-title: none,
  spine-author: none,
  title-size: 32pt,
  // ink: the title; accent: author, rules; label: the name plate and seal
  ink: rgb("#1E3524"),
  accent: rgb("#7E6220"),
  label: rgb("#1E3524"),
  paper: rgb("#F0E6CC"),
  // the back: a passage and its source
  epigraph: none,
  epigraph-source: none,
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

  set text(font: SERIF, fill: ink)
  set page(width: page-width, height: page-height, margin: 0pt) if not front-only
  set page(width: trim-width, height: trim-height, margin: 0pt) if front-only

  // The press tab: the seal over a name plate, at one height on every front.
  let press-tab(at-y, size: 0.74in) = {
    if seal != none {
      place(center + top, dy: at-y, seal(width: size, roundel: label, fountain: paper))
    }
    place(center + top, dy: at-y + size + 0.1in, box(fill: label, inset: (x: 0.13in, y: 0.065in),
      caps([Common Weal Press], 6.5pt, paper)))
  }

  let wrap(body) = if front-only {
    place(top + left, dx: -front-x, dy: -BLEED, box(width: page-width, height: page-height, body))
  } else { body }

  wrap({
    // --- spine and back: the plate's ground ----------------------------------
    // `ground` is gradient stops (head to foot) or any fill
    let ground-fill = if type(ground) == array { gradient.linear(dir: ttb, ..ground) } else { ground }
    place(top + left, rect(width: front-x, height: page-height, fill: ground-fill))

    // --- front: the plate, cut at the fold and the bleed ----------------------
    place(top + left, dx: front-x, box(width: trim-width + BLEED, height: page-height, clip: true, {
      place(rect(width: 100%, height: 100%,
        fill: if front-ground != none { front-ground } else { ground-fill }))
      if plate != none {
        place(dx: plate-at.dx, dy: BLEED + plate-at.dy,
          box(width: plate-at.width, height: plate-at.height,
            image(plate, width: 100%, height: 100%)))
      }
      if art != none { place(dy: BLEED, art) }
    }))

    // the title block, the house's order: author, rule, title, subtitle
    place(top + left, dx: front-x + SAFETY, dy: BLEED + title-y,
      box(width: if title-width != none { title-width } else { trim-width - 2 * SAFETY }, {
        set align(title-align)
        set par(spacing: 0pt, leading: 0.3em, justify: false)
        caps(author, 10pt, accent)
        v(0.16in)
        if title-align == left { line(length: 0.9in, stroke: 1.3pt + accent) } else { diamond-rule(accent) }
        v(0.2in)
        text(font: DISPLAY, weight: "bold", size: title-size, fill: ink, title)
        if tail != none {
          linebreak()
          v(0.04in)
          text(font: DISPLAY, size: title-size * 0.66, fill: ink, tail)
        }
        if subtitle != none {
          v(0.22in)
          block(width: 100%, {
            set par(leading: 0.5em)
            text(style: "italic", size: 11pt, fill: ink.transparentize(15%), subtitle)
          })
        }
      }))
    place(top + left, dx: front-x, dy: BLEED, box(width: trim-width, height: trim-height,
      press-tab(trim-height - SAFETY - 1.18in)))

    // --- spine ------------------------------------------------------------------
    // Rules across head and foot, the seal at the foot. The author's surname
    // has a fixed place under the head rules, at the same height on every
    // book, so a shelf of these reads as a row of names: across the spine
    // when it is wide enough for the name at a readable size, otherwise
    // running down it from that same point. The title runs down the rest.
    // Everything inside what survives the trim.
    let safe = spine - 2 * SPINE_TRIM
    let spine-name = if spine-author != none { spine-author } else { author }
    let spine-title = if spine-title != none { spine-title } else { title }
    if safe > 0.2in {
      place(top + left, dx: spine-x, dy: BLEED, box(width: spine, height: trim-height, {
        set align(center)
        for (edge, sign) in ((top, 1.0), (bottom, -1.0)) {
          place(edge + center, dy: sign * 0.42in, rect(width: safe, height: 1.2pt, fill: accent))
          place(edge + center, dy: sign * 0.48in, rect(width: safe, height: 0.5pt, fill: accent))
        }
        let s = calc.min(safe, 0.5in)
        if seal != none {
          place(bottom + center, dy: -0.62in, seal(width: s, roundel: label, fountain: paper))
        }
        // where the name begins, and where the title must end (above the seal)
        let name-y = 0.66in
        let foot = trim-height - 0.62in - s - 0.16in
        let title-size = calc.min(14pt, safe / 1in * 72pt * 0.42)
        let name-text(size) = text(font: SERIF, weight: "medium", size: size, tracking: 0.1em,
          fill: accent, upper(spine-name))
        context {
          // the name across the spine, as large as fits, up to 10.5pt
          let w = measure(name-text(10pt)).width
          let across = calc.min(10.5pt, 10pt * ((safe * 0.94) / w))
          if across >= 7pt {
            place(top + center, dy: name-y, name-text(across))
            place(top + center, dy: name-y + across * 1.25 + 0.06in,
              text(size: 6pt, fill: accent, sym.diamond.filled))
            let top-y = name-y + across * 1.25 + 0.28in
            place(top + center, dy: top-y, rotate(90deg, reflow: true,
              box(width: foot - top-y, height: safe, align(center + horizon,
                text(font: DISPLAY, weight: "bold", size: title-size, fill: ink, spine-title)))))
          } else {
            // a thin spine: the name runs down it from the same place, then the title
            place(top + center, dy: name-y, rotate(90deg, reflow: true,
              box(width: foot - name-y, height: safe, align(left + horizon, {
                name-text(calc.min(10.5pt, safe / 1in * 72pt * 0.55))
                h(0.12in)
                text(size: 6pt, fill: accent, sym.diamond.filled)
                h(0.12in)
                text(font: DISPLAY, weight: "bold", size: title-size, fill: ink, spine-title)
              }))))
          }
        }
      }))
    } else if spine >= 0.25in {
      // A thin spine (about 80 to 170 pages): too narrow for the full
      // allowance, so the name and title run down it on one line from the
      // same head position, held 1/16in off each fold, with a single rule
      // across head and foot and the seal, as wide as the spine allows, at
      // the foot (it still reads as a fountain at a fifth of an inch).
      let w = spine - 0.125in
      let s = calc.min(w, 0.5in)
      place(top + left, dx: spine-x, dy: BLEED, box(width: spine, height: trim-height, {
        set align(center)
        for (edge, sign) in ((top, 1.0), (bottom, -1.0)) {
          place(edge + center, dy: sign * 0.42in, rect(width: w, height: 0.8pt, fill: accent))
        }
        if seal != none {
          place(bottom + center, dy: -0.58in, seal(width: s, roundel: label, fountain: paper))
        }
        let size = calc.min(10pt, w / 1in * 72pt * 0.62)
        place(top + center, dy: 0.66in, rotate(90deg, reflow: true,
          box(width: trim-height - 1.32in - s - 0.3in, height: w, align(left + horizon, {
            text(font: SERIF, weight: "medium", size: size * 0.9, tracking: 0.1em, fill: accent,
              upper(spine-name))
            h(0.1in)
            text(size: 5pt, fill: accent, sym.diamond.filled)
            h(0.1in)
            text(font: DISPLAY, weight: "bold", size: size, fill: ink, spine-title)
          }))))
      }))
    }

    // --- back ---------------------------------------------------------------------
    place(top + left, dx: back-x + SAFETY, dy: BLEED + SAFETY,
      box(width: trim-width - 2 * SAFETY, height: trim-height - 2 * SAFETY, {
        set align(center)
        v(0.55in)
        if epigraph != none {
          diamond-rule(accent, width: 1.2in)
          v(0.3in)
          block(width: 100%, inset: (x: 0.1in), {
            set par(justify: false, leading: 0.7em)
            text(size: 11.5pt, style: "italic", fill: ink, epigraph)
          })
          if epigraph-source != none {
            v(0.2in)
            caps(epigraph-source, 8.5pt, accent, tracking: 0.16em)
          }
          v(0.3in)
          diamond-rule(accent, width: 1.2in)
        }
        v(1fr)
        // the press at the foot, left; the lower right kept clear for a
        // barcode (2in x 1.2in) once the book has an ISBN
        grid(columns: (1fr, auto), align: (left + bottom, right + bottom),
          grid(columns: 2, column-gutter: 0.12in, align: left + horizon,
            if seal != none { seal(width: 0.46in, roundel: label, fountain: paper) },
            caps([Common Weal Press], 7pt, accent, tracking: 0.2em)),
          if isbn != none {
            stack(box(fill: white, width: 2in, height: 1.2in), v(0.06in),
              text(size: 7.5pt)[ISBN #isbn])
          } else { box(width: 2in, height: 1.2in) })
      }))
  })
}
