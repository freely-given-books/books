// Full-wrap cover for a Common Weal Press set of several volumes, lettered
// after the work's printed title page (Gouge's Of Domestical Duties, after
// 1622): a double-ruled frame, the title in spaced capitals, the whole work's
// contents with this volume's entries picked out, and the volume's number in
// a roundel. The house parts are plate_cover.typ's: Cinzel over EB Garamond,
// the author over a diamond rule at the head, the seal and name plate at the
// foot of the front, the surname under the spine's head rules, the seal at
// the foot of the spine and the back, one ground round the whole wrap.
//
//   #import "../../../scripts/set_cover.typ": *
//   #import "@local/fgbooks:0.14.0": press-seal
//   #set-cover(
//     seal: press-seal,
//     title-display: [...],      // lettered() lines
//     contents: ((label, entry), ...), current: (0,),
//     volume-number: [I], ...
//   )
//
// ./fgb build passes the interior's page count and trim (--input pages=N
// trim-width=W trim-height=H), so the spine is always Lulu's
// `pages / 444 + 0.06in`; with --input front-only=true the front alone is
// the ebook cover.

#import "plate_cover.typ": BLEED, SAFETY, SPINE_TRIM, DISPLAY, SERIF, caps, diamond-rule

// Spaced capitals in the display face, for lettering after a title page.
#let lettered(body, size, tracking: 0.18em, weight: "regular") = text(font: DISPLAY,
  size: size, tracking: tracking, weight: weight, upper(body))

// A volume number in a double-ruled roundel.
#let roundel(n, colour, ink, size: 0.72in, type-size: 17pt) = box(
  width: size, height: size, radius: 50%, stroke: 1pt + colour,
  align(center + horizon, box(width: size - 0.1in, height: size - 0.1in,
    radius: 50%, stroke: 0.4pt + colour,
    align(center + horizon, text(font: DISPLAY, size: type-size, fill: ink, n)))))

#let set-cover(
  // the spine and back's fill, and the front's unless it has its own:
  // `front-ground` (any fill, a gradient laid over the front's trim and
  // bleed), or `panel`, a fill inside the frame with `ground` outside it
  ground: rgb("#4A5230"),
  front-ground: none,
  panel: none,
  // a front of the set's own design, in place of the frame, the lettering
  // and the contents: content laid on the front's trim box (the seal and
  // name plate are still set at the house's place, over it)
  front: none,
  seal: none,
  title: [Title],
  // the title as lettered() lines; none sets `title` plainly
  title-display: none,
  // a line under the title ("Eight Treatises") and a smaller one under it
  kicker: none,
  imprint: none,
  author: [Author],
  spine-title: none,
  spine-author: none,
  // (label, entry) pairs, and the indexes of this volume's entries
  contents: (),
  current: (),
  contents-height: 2.45in,
  volume: none,          // "Volume I", under the roundel
  volume-number: none,   // "I", in it
  // the spine's type, roundel and seal are sized to this width, the
  // thinnest volume's safe strip (spine less 1/8in each side), so every
  // volume of a set shelves alike; none sizes them to this volume's own
  spine-fit: none,
  // ink: type; accent: rules, author, frame; label and paper: the seal's
  // roundel and fountain, and the name plate
  ink: rgb("#F1EAD2"),
  accent: rgb("#C9A24E"),
  label: rgb("#C9A24E"),
  paper: rgb("#1F2416"),
  // the back: a paragraph on this volume, then a passage and its source
  back-lead: none,
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
  let dim = ink.transparentize(50%)

  set text(font: SERIF, fill: ink)
  set page(width: page-width, height: page-height, margin: 0pt) if not front-only
  set page(width: trim-width, height: trim-height, margin: 0pt) if front-only

  let wrap(body) = if front-only {
    place(top + left, dx: -front-x, dy: -BLEED, box(width: page-width, height: page-height, body))
  } else { body }

  wrap({
    place(top + left, rect(width: page-width, height: page-height, fill: ground))

    // --- front ------------------------------------------------------------------
    // the frame, 0.3in inside the trim; the seal and name plate sit inside
    // its foot at the house's height
    let frame = 0.3in
    if front-ground != none {
      place(top + left, dx: front-x, rect(width: trim-width + BLEED, height: page-height, fill: front-ground))
    }
    if panel != none and front == none {
      place(top + left, dx: front-x + frame, dy: BLEED + frame,
        rect(width: trim-width - 2 * frame, height: trim-height - 2 * frame, fill: panel))
    }
    let seal-y = trim-height - SAFETY - 1.18in
    if front != none {
      place(top + left, dx: front-x, dy: BLEED, box(width: trim-width, height: trim-height, front))
    } else {
    place(top + left, dx: front-x + frame, dy: BLEED + frame,
      box(width: trim-width - 2 * frame, height: trim-height - 2 * frame,
        stroke: 1.4pt + accent, inset: 3.5pt,
        box(width: 100%, height: 100%, stroke: 0.5pt + accent)))

    place(top + left, dx: front-x + SAFETY, dy: BLEED + SAFETY + 0.12in,
      box(width: trim-width - 2 * SAFETY, height: seal-y - SAFETY - 0.2in, {
        set align(center)
        set par(spacing: 0pt, leading: 0.3em, justify: false)
        caps(author, 10pt, accent)
        v(0.14in)
        diamond-rule(accent)
        v(0.2in)
        // the lettered lines are paragraphs: room between them
        if title-display != none { block({ set par(spacing: 0.16in); title-display }) } else {
          text(font: DISPLAY, weight: "bold", size: 30pt, title)
        }
        if kicker != none {
          v(0.18in)
          text(size: 14pt, style: "italic", kicker)
        }
        if imprint != none {
          v(0.07in)
          text(size: 9pt, style: "italic", fill: ink.transparentize(25%), imprint)
        }
        v(0.16in)
        line(length: 100%, stroke: 0.5pt + accent)
        if contents.len() > 0 {
          // a fixed height, so the roundel stands at one place on every
          // volume whichever entries wrap
          block(height: contents-height, width: 100%, align(horizon, {
            set text(size: 11pt)
            set par(leading: 0.42em)
            grid(columns: (2.4em, 1fr), column-gutter: 0.6em, row-gutter: 0.62em,
              align: (right + top, left + top),
              ..contents.enumerate().map(((i, entry)) => {
                let on = i in current
                let style = (fill: if on { ink } else { dim },
                             weight: if on { "medium" } else { "regular" })
                (text(..style, entry.at(0)), text(..style, style: "italic", entry.at(1)))
              }).flatten())
          }))
          line(length: 100%, stroke: 0.5pt + accent)
        }
        v(1fr)
        if volume-number != none { roundel(volume-number, accent, ink) }
        if volume != none {
          v(0.08in)
          caps(volume, 8.5pt, accent, tracking: 0.3em)
        }
        v(1fr)
      }))
    }
    if seal != none {
      place(top + left, dx: front-x, dy: BLEED, box(width: trim-width, height: trim-height, {
        place(center + top, dy: seal-y, seal(width: 0.74in, roundel: label, fountain: paper))
        place(center + top, dy: seal-y + 0.84in, box(fill: label, inset: (x: 0.13in, y: 0.065in),
          caps([Common Weal Press], 6.5pt, paper)))
      }))
    }

    // --- spine ------------------------------------------------------------------
    // The house's rules at head and foot, the surname at its fixed place under
    // the head rules, the seal at the foot; a set adds the volume's number in
    // a roundel above the seal, at one height on every volume. The surname
    // runs down the spine on every volume, so a set shelved together lines up
    // whatever each volume's thickness.
    let safe = spine - 2 * SPINE_TRIM
    let band = spine - 0.125in
    let fit = if spine-fit != none { calc.min(spine-fit, safe) } else { safe }
    let s = calc.min(fit, 0.5in)
    let name = if spine-author != none { spine-author } else { author }
    let stitle = if spine-title != none { spine-title } else { title }
    place(top + left, dx: spine-x, dy: BLEED, box(width: spine, height: trim-height, {
      set align(center)
      for (edge, sign) in ((top, 1.0), (bottom, -1.0)) {
        place(edge + center, dy: sign * 0.42in, rect(width: band, height: 1.2pt, fill: accent))
        place(edge + center, dy: sign * 0.48in, rect(width: band, height: 0.5pt, fill: accent))
      }
      if seal != none {
        place(bottom + center, dy: -0.62in, seal(width: s, roundel: label, fountain: paper))
      }
      let d = calc.min(0.36in, fit)
      let mark-y = 0.62in + s + 0.14in
      if volume-number != none {
        place(bottom + center, dy: -mark-y, box(width: d, height: d, radius: 50%,
          stroke: 0.8pt + accent, align(center + horizon,
            text(font: DISPLAY, size: 10pt * (d / 0.36in), fill: ink, volume-number))))
      }
      let size = calc.min(11pt, fit / 1in * 72pt * 0.5)
      let top-y = 0.66in
      place(top + center, dy: top-y, rotate(90deg, reflow: true,
        box(width: trim-height - top-y - mark-y - d - 0.16in, height: safe,
          align(left + horizon, {
            text(weight: "medium", size: size * 0.9, tracking: 0.1em, fill: accent, upper(name))
            h(0.14in)
            text(size: 6pt, fill: accent, sym.diamond.filled)
            h(0.14in)
            show linebreak: [ ]
            text(font: DISPLAY, size: size, tracking: 0.12em, fill: ink, upper(stitle))
          }))))
    }))

    // --- back -------------------------------------------------------------------
    place(top + left, dx: back-x + SAFETY, dy: BLEED + SAFETY,
      box(width: trim-width - 2 * SAFETY, height: trim-height - 2 * SAFETY, {
        set align(center)
        v(0.55in)
        if back-lead != none {
          block(width: 100%, inset: (x: 0.1in), {
            set par(justify: false, leading: 0.7em)
            text(size: 11pt, fill: ink.transparentize(10%), back-lead)
          })
          v(0.35in)
        }
        if epigraph != none {
          diamond-rule(accent, width: 1.2in)
          v(0.3in)
          block(width: 100%, inset: (x: 0.1in), {
            set par(justify: false, leading: 0.7em)
            text(size: 12.5pt, style: "italic", fill: ink, epigraph)
          })
          if epigraph-source != none {
            v(0.2in)
            caps(epigraph-source, 8.5pt, accent, tracking: 0.16em)
          }
          v(0.3in)
          diamond-rule(accent, width: 1.2in)
        }
        v(1fr)
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
