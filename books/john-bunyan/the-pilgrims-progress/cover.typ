// Book cover for The Pilgrim's Progress
// Template: 12.22" × 8.75" total with bleed
// Trim: 5.5" × 8.5" per panel
// Spine: 0.97"
// Bleed: 0.125"

#set page(
  width: 12.22in,
  height: 8.75in,
  margin: 0pt,
)

#set text(font: "Liberation Serif")

// Colors - original scheme
#let cream = rgb("#FAF3E8")
#let panel-color = cream
#let text-color = rgb("#D4A017")
#let border-color = rgb("#5A8A9A")

// Dimensions
#let bleed = 0.125in
#let trim-width = 5.5in
#let trim-height = 8.5in
#let spine-width = 0.97in
#let safety = 0.5in
#let border-inset = 0.4in

// Calculate positions
#let back-cover-start = bleed
#let spine-start = bleed + trim-width
#let front-cover-start = bleed + trim-width + spine-width

// Full page cream background
#place(top + left, rect(width: 100%, height: 100%, fill: cream))

// Front cover border
#place(
  top + left,
  dx: front-cover-start + border-inset,
  dy: bleed + border-inset,
  rect(
    width: trim-width - 2 * border-inset,
    height: trim-height - 2 * border-inset,
    fill: none,
    stroke: 1.5pt + border-color,
  )
)

// Back cover border
#place(
  top + left,
  dx: back-cover-start + border-inset,
  dy: bleed + border-inset,
  rect(
    width: trim-width - 2 * border-inset,
    height: trim-height - 2 * border-inset,
    fill: none,
    stroke: 1.5pt + border-color,
  )
)

// === FRONT COVER ===
// Title
#place(
  top + left,
  dx: front-cover-start,
  dy: bleed + 2in,
  box(
    width: trim-width,
    align(center)[
      #text(size: 32pt, fill: text-color)[The Pilgrim's Progress]
    ]
  )
)

// Line separator under title
#place(
  top + left,
  dx: front-cover-start + 1.5in,
  dy: bleed + 2.8in,
  line(length: trim-width - 3in, stroke: 0.75pt + text-color)
)

// Subtitle on front cover
#place(
  top + left,
  dx: front-cover-start,
  dy: bleed + 3.1in,
  box(
    width: trim-width,
    align(center)[
      #text(size: 14pt, fill: text-color, style: "italic")[
        From This World to That Which is to Come
      ]
      #v(0.15in)
      #text(size: 14pt, fill: text-color, style: "italic")[
        Delivered under the Similitude of a Dream
      ]
    ]
  )
)

// Line separator above author
#place(
  top + left,
  dx: front-cover-start + 1.5in,
  dy: bleed + 4.1in,
  line(length: trim-width - 3in, stroke: 0.75pt + text-color)
)

// Author on front - small caps with tracking
#place(
  top + left,
  dx: front-cover-start,
  dy: bleed + trim-height - 1.5in,
  box(
    width: trim-width,
    align(center)[
      #text(size: 14pt, fill: text-color, tracking: 0.2em)[JOHN BUNYAN]
    ]
  )
)

// === SPINE ===
// Spine background
#place(
  top + left,
  dx: spine-start,
  dy: bleed,
  rect(
    width: spine-width,
    height: trim-height,
    fill: panel-color,
  )
)

// Title on spine (top)
#place(
  top + left,
  dx: spine-start,
  dy: bleed + 0.5in,
  box(
    width: spine-width,
    height: 4in,
    align(center + horizon)[
      #rotate(90deg, reflow: true)[
        #text(size: 14pt, fill: text-color)[The Pilgrim's Progress]
      ]
    ]
  )
)

// Author on spine (bottom)
#place(
  top + left,
  dx: spine-start,
  dy: bleed + trim-height - 2.5in,
  box(
    width: spine-width,
    height: 2in,
    align(center + horizon)[
      #rotate(90deg, reflow: true)[
        #text(size: 12pt, fill: text-color, tracking: 0.1em)[John Bunyan]
      ]
    ]
  )
)

// === BACK COVER ===
// Quote from Author's Apology
#place(
  top + left,
  dx: back-cover-start + safety,
  dy: bleed + 2.5in,
  box(
    width: trim-width - 2 * safety,
    align(center)[
      #text(size: 16pt, fill: text-color, style: "italic")[
        "O then come hither, \
        And lay my book, thy head, and heart together."
      ]
    ]
  )
)

// Author on back cover (above barcode area)
#place(
  top + left,
  dx: back-cover-start,
  dy: bleed + trim-height - 2.8in,
  box(
    width: trim-width,
    align(center)[
      #text(size: 14pt, fill: text-color, tracking: 0.2em)[JOHN BUNYAN]
    ]
  )
)
