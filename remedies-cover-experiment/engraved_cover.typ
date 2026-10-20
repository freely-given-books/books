// Full-wrap cover in the engraved design: an experiment (Precious Remedies,
// 2026-10-19) for a catalogue of hundreds of books that still read as one
// house.
//
// The system, roughly three parts fixed to one part variable:
//
//   fixed, every book   the paper ground, the double gold frame, the type
//                       (Cinzel capitals, EB Garamond text), the diamond
//                       rules, the spine's layout, and the imprint's mark and
//                       name at the foot of front, spine and back
//   per author          the emblem at the spine's head, under the surname
//                       (one device, the same on every book by that author)
//                       and a restrained accent, the colour of the title
//   per book            the title, the front engraving, the spine's art
//                       under the title (Precious Remedies: the sword), the
//                       back's passages, a volume number
//
// So a shelf is told apart by emblem first and accent second, never by a
// ground colour of its own: the ground stays the house's.
//
//   #import "engraved_cover.typ": *
//   #engraved-cover(
//     author: [Thomas Brooks], spine-author: [Brooks],
//     title: [Precious \ Remedies], title-rest: [Against \ Satan's Devices],
//     author-emblem: image(...), spine-art: image("art/sword.png"),
//     engraving: image("art/vignette.png"),
//     pages: 354,
//   )
//
// Print rules are panel_cover.typ's: Lulu's spine, `pages / 444 + 0.06in`,
// from the page count and trim ./fgb build passes (--input pages=N
// trim-width=W trim-height=H), a 0.125in bleed, type 0.5in inside the trim.
// `--input front-only=true` gives the ebook front alone.
//
// Fonts: Cinzel and EB Garamond (both OFL) are not system fonts; compile with
// `--font-path fonts` (or TYPST_FONT_PATHS).

#import "@preview/droplet:0.3.1"

#let BLEED = 0.125in
#let SAFETY = 0.5in
// The frame sits outside the type's safety line but well inside the trim: a
// cut that drifts the 1/16in Lulu allows moves the frame against the edge
// without reaching it.
#let FRAME_INSET = 0.3in

// The spine: the author's emblem at the head, under the surname, and the
// book's art below the title, pinned: its height, and where its foot stands
// above the trim, the same on every spine so a shelf lines up.
#let EMBLEM_HEIGHT = 0.3in
#let SPINE_ART_HEIGHT = 1.05in
#let SPINE_ART_FOOT = 1.75in

#let HOUSE = (
  ground: rgb("#EEE5D0"),      // the paper, the whole wrap
  ink:    rgb("#2B2118"),      // text and engraving: a warm black
  gold:   rgb("#A9843F"),      // rules, frame, diamonds
  muted:  rgb("#5A4D3E"),      // small capitals, credits
)

#let DISPLAY = ("Cinzel", "Libertinus Serif")
#let TEXT = ("EB Garamond", "Libertinus Serif")

#let lulu-spine(pages) = (pages / 444.0 + 0.06) * 1in

// a gold rule broken by a diamond: the house's divider
#let diamond-rule(width: 1.7in, gold: HOUSE.gold) = box(width: width, {
  set align(center + horizon)
  grid(columns: (1fr, auto, 1fr), column-gutter: 0.09in, align: horizon,
    line(length: 100%, stroke: 0.6pt + gold),
    text(size: 7pt, fill: gold, sym.diamond.filled),
    line(length: 100%, stroke: 0.6pt + gold))
})

// The double frame.  At each corner the inner rule bends inward and ends in
// a scroll, with a fleur-de-lis pointing into the corner in the space that
// leaves (art/corner.svg, drawn for the top left and mirrored for the
// others); the straight inner rules stop where the ornament takes over.  An
// SVG stays vector through to the PDF.
#let CORNER = read("art/corner.svg", encoding: none)
#let frame(w, h, gold: HOUSE.gold, ornament: 0.55in) = {
  let gap = 0.07in                 // outer rule to inner rule
  let u = ornament / 100           // one unit of the SVG's 100
  let inner = 0.6pt
  place(rect(width: w, height: h, stroke: 1.2pt + gold))
  // the inner rule's straight runs, between the ornaments (overlapping
  // their ends a little, so the joins do not show)
  let (x0, y0, x1, y1) = (gap, gap, w - gap, h - gap)
  let reach = 96 * u
  let s = inner + gold
  place(line(start: (x0 + reach, y0), end: (x1 - reach, y0), stroke: s))
  place(line(start: (x0 + reach, y1), end: (x1 - reach, y1), stroke: s))
  place(line(start: (x0, y0 + reach), end: (x0, y1 - reach), stroke: s))
  place(line(start: (x1, y0 + reach), end: (x1, y1 - reach), stroke: s))
  // the SVG's 0,0 is the inner corner, 2 units in from its own corner
  let o = 2 * u
  for (x, y, sx, sy) in ((x0 - o, y0 - o, 1, 1), (x1 + o - ornament, y0 - o, -1, 1),
                         (x0 - o, y1 + o - ornament, 1, -1), (x1 + o - ornament, y1 + o - ornament, -1, -1)) {
    place(dx: x, dy: y, scale(x: sx * 100%, y: sy * 100%,
      image(CORNER, format: "svg", width: ornament)))
  }
}

// Spaced capitals in the display face.
#let caps(body, size, tracking: 0.2em, fill: HOUSE.ink) = {
  text(font: DISPLAY, size: size, tracking: tracking, fill: fill, upper(body))
}

// Where an author's emblem goes until there is one: a cluster of four gold
// diamonds, the ornament of the mock-up's spine, at the emblem's size.
#let emblem-placeholder(size) = box(width: size, height: size, {
  let d = size * 0.36
  for (x, y) in ((0.5, 0.15), (0.15, 0.5), (0.85, 0.5), (0.5, 0.85)) {
    place(dx: size * x - d / 2, dy: size * y - d / 2,
      rotate(45deg, rect(width: d * 0.72, height: d * 0.72, fill: HOUSE.gold)))
  }
})

// Where the imprint's mark goes until it has one: a dotted roundel the size
// the mark will be printed, so the layout is drawn around the real thing.
#let imprint-placeholder(size) = box(width: size, height: size, radius: 50%,
  stroke: (paint: HOUSE.gold, thickness: 0.6pt, dash: "dotted"),
  align(center + horizon, text(font: DISPLAY, size: size * 0.16, fill: HOUSE.gold, tracking: 0.08em)[MARK]))

#let engraved-cover(
  author: [Author],
  // the author as the spine's head gives it: the surname
  spine-author: none,
  // The title in its display lines (\ breaks), and the rest of it: Precious
  // Remedies / Against Satan's Devices.  `subtitle` is the printed "Or, ..."
  title: [Title],
  title-rest: none,
  subtitle: none,
  // the rest of the title as the spine's foot sets it, stacked, if it differs
  spine-rest: auto,
  volume: none,
  // The author's emblem (the spine's head), this book's art for the spine
  // (under the title) and its engraving for the front: images, art on a
  // transparent ground inked in HOUSE.ink.
  author-emblem: none,
  spine-art: none,
  engraving: none,
  engraving-height: 3.05in,
  // the author's accent: the colour of the title on front and spine
  accent: rgb("#1D2A3A"),
  title-size: 38pt,
  // The back: a heading, a passage from the book (its first letter dropped),
  // a second shorter one with its source, and a few lines about the book.
  back-heading: none,
  back-passage: none,
  back-quote: none,
  back-quote-source: none,
  back-about: none,
  // The imprint: its mark (an image, or content), its name.
  imprint-mark: none,
  imprint-name: [Freely Given Books],
  isbn: none,
  pages: 200,
  trim-width: 5.5in,
  trim-height: 8.5in,
  front-only: sys.inputs.at("front-only", default: "false") == "true",
) = {
  let pages = int(sys.inputs.at("pages", default: str(pages)))
  let trim-width = if "trim-width" in sys.inputs {
    float(sys.inputs.at("trim-width")) * 1in } else { trim-width }
  let trim-height = if "trim-height" in sys.inputs {
    float(sys.inputs.at("trim-height")) * 1in } else { trim-height }
  let spine = lulu-spine(pages)
  let page-width = 2 * BLEED + 2 * trim-width + spine
  let page-height = 2 * BLEED + trim-height
  let back-x = BLEED
  let spine-x = BLEED + trim-width
  let front-x = spine-x + spine
  let mark(size) = if imprint-mark == none { imprint-placeholder(size) }
    else { box(height: size, imprint-mark) }

  set page(width: page-width, height: page-height, margin: 0pt) if not front-only
  set page(width: trim-width, height: trim-height, margin: 0pt) if front-only
  set text(font: TEXT, fill: HOUSE.ink, number-type: "old-style")

  let wrap(body) = if front-only {
    place(top + left, dx: -front-x, dy: -BLEED, box(width: page-width, height: page-height, body))
  } else { body }

  wrap({
  place(rect(width: 100%, height: 100%, fill: HOUSE.ground))

  // the frames, front and back, inset from each trim
  for x in (back-x, front-x) {
    place(dx: x + FRAME_INSET, dy: BLEED + FRAME_INSET,
      frame(trim-width - 2 * FRAME_INSET, trim-height - 2 * FRAME_INSET))
  }

  // --- Front ---------------------------------------------------------------
  place(dx: front-x + SAFETY, dy: BLEED + SAFETY,
    box(width: trim-width - 2 * SAFETY, height: trim-height - 2 * SAFETY, {
      set align(center)
      set par(spacing: 0.1in)
      set block(spacing: 0.1in)
      v(0.1in)
      caps(author, 13pt, tracking: 0.28em)
      v(0.04in)
      diamond-rule()
      v(0.22in)
      {
        set par(leading: 0.22em)
        text(font: DISPLAY, size: title-size, weight: "bold", fill: accent, tracking: 0.02em, upper(title))
      }
      if volume != none {
        v(0.06in)
        caps(volume, 11pt, tracking: 0.3em, fill: HOUSE.muted)
      }
      v(0.12in)
      diamond-rule(width: 2.4in)
      if title-rest != none {
        v(0.06in)
        set par(leading: 0.42em)
        caps(title-rest, 14pt, tracking: 0.16em)
      }
      if subtitle != none {
        v(0.02in)
        text(size: 10.5pt, style: "italic", fill: HOUSE.muted, subtitle)
      }
      v(1fr)
      if engraving != none { box(height: engraving-height, engraving) }
      v(1fr)
      diamond-rule()
      v(0.08in)
      mark(0.42in)
      v(0.02in)
      caps(imprint-name, 8.5pt, tracking: 0.24em, fill: HOUSE.muted)
    }))

  // --- Spine ---------------------------------------------------------------
  // Head: the surname across the spine and the author's emblem under it.
  // Then the title, rotated to read top to bottom; the book's art, pinned;
  // the rest of the title across the spine under it; the imprint's mark at
  // the foot, at the same height on every book.  A spine too thin for type
  // across it (under about half an inch, ~200 pages) keeps only the rotated
  // title and author and the mark.
  let wide = spine >= 0.5in
  place(dx: spine-x, dy: BLEED, box(width: spine, height: trim-height, {
    set align(center)
    let rule-w = spine - 0.16in
    // rules across the spine at head and foot: caps on the lettering
    for (edge, sign) in ((top, 1.0), (bottom, -1.0)) {
      place(edge + center, dy: sign * 0.36in, rect(width: rule-w, height: 1pt, fill: HOUSE.gold))
      place(edge + center, dy: sign * 0.41in, rect(width: rule-w, height: 0.4pt, fill: HOUSE.gold))
    }
    if wide {
      let sa = if spine-author != none { spine-author } else { author }
      place(top + center, dy: 0.52in, caps(sa, 9pt, tracking: 0.12em))
      place(top + center, dy: 0.74in,
        if author-emblem != none { box(height: EMBLEM_HEIGHT, author-emblem) }
        else { emblem-placeholder(EMBLEM_HEIGHT) })
      let rest = if spine-rest == auto { title-rest } else { spine-rest }
      // The book's art is pinned (SPINE_ART_FOOT); the rest of the title
      // hangs under it, and the title fills the column above.
      let art-top = trim-height - SPINE_ART_FOOT - SPINE_ART_HEIGHT
      if spine-art != none {
        place(top + center, dy: art-top, box(height: SPINE_ART_HEIGHT, spine-art))
      }
      if rest != none {
        place(top + center, dy: trim-height - SPINE_ART_FOOT + 0.13in, {
          set par(leading: 0.75em)
          caps(rest, 7pt, tracking: 0.1em)
        })
      }
      let title-top = 0.74in + EMBLEM_HEIGHT + 0.2in
      place(top + center, dy: title-top,
        box(width: spine, height: art-top - title-top - 0.2in,
          align(center + horizon, rotate(90deg, reflow: true, {
            show linebreak: [ ]
            text(font: DISPLAY, size: 21pt, weight: "bold", fill: accent, tracking: 0.05em, upper(title))
            if volume != none { h(0.5em); caps(volume, 10pt) }
          }))))
    } else {
      place(center + horizon, dy: -0.2in, rotate(90deg, reflow: true, {
        show linebreak: [ ]
        text(font: DISPLAY, size: 10pt, weight: "bold", fill: accent, tracking: 0.08em, upper(title))
        h(0.8em); text(size: 5pt, fill: HOUSE.gold, sym.diamond.filled); h(0.8em)
        caps(author, 7.5pt, tracking: 0.1em)
      }))
    }
    place(bottom + center, dy: -0.5in, mark(calc.min(0.38in, spine - 0.12in)))
  }))

  // --- Back ----------------------------------------------------------------
  place(dx: back-x + SAFETY, dy: BLEED + SAFETY,
    box(width: trim-width - 2 * SAFETY, height: trim-height - 2 * SAFETY, {
      set align(center)
      set par(justify: false, spacing: 0.1in)
      set block(spacing: 0.1in)
      v(0.05in)
      if back-heading != none {
        caps(back-heading, 10.5pt, tracking: 0.26em)
        v(0.04in)
        diamond-rule()
        v(0.14in)
      }
      if back-passage != none {
        set align(left)
        set par(justify: true, leading: 0.55em)
        set text(size: 13pt)
        // the first letter dropped three lines, in the display face
        let (first, rest) = back-passage
        droplet.dropcap(height: 3, gap: 0.05in,
          transform: l => text(font: DISPLAY, weight: "bold", fill: accent, l),
          [#first#rest])
      }
      v(1fr)
      if back-quote != none {
        diamond-rule(width: 1.3in)
        v(0.1in)
        pad(x: 0.2in, {
          set par(leading: 0.5em)
          text(size: 13pt, style: "italic", back-quote)
          v(0.06in)
          caps(back-quote-source, 7.5pt, tracking: 0.18em, fill: HOUSE.muted)
        })
      }
      if back-about != none {
        v(1fr)
        diamond-rule(width: 1.3in)
        v(0.1in)
        pad(x: 0.15in, {
          set par(leading: 0.5em)
          text(size: 11.5pt, fill: HOUSE.muted, back-about)
        })
      }
      v(1fr)
      // the foot: the imprint at left, the barcode's field at right
      grid(columns: (1fr, 2in), align: (left + bottom, right + bottom),
        {
          set align(center)
          box(width: 1.5in, {
            mark(0.36in)
            v(0.01in)
            caps(imprint-name, 6.5pt, tracking: 0.2em, fill: HOUSE.muted)
          })
        },
        // Lulu drops the barcode into a white field once there is an ISBN
        if isbn != none { box(fill: white, width: 2in, height: 1.2in) } else { box(height: 1.2in) })
    }))
  })
}
