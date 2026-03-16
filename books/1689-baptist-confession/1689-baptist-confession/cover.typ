// Cover for The 1689 Baptist Confession of Faith
// Lulu Print Template Specifications:
// - Total document size (with bleed): 11.774" × 8.75"
// - Book trim size: 5.5" × 8.5"
// - Spine width: 0.524"
// - Bleed: 0.125"
// - Safety margin: 0.5" from trim

#set page(
  width: 11.774in,
  height: 8.75in,
  margin: 0pt,
)

#set text(font: "Liberation Serif", fill: rgb("#f4e9d6"))

// Colors - classic Reformed aesthetic
#let deep-navy = rgb("#1a2744")
#let gold-accent = rgb("#c9a227")
#let cream = rgb("#f4e9d6")

// Measurements
#let bleed = 0.125in
#let spine-width = 0.524in
#let trim-width = 5.5in
#let trim-height = 8.5in
#let safety = 0.5in

// Calculated positions
#let back-cover-start = bleed
#let back-cover-end = bleed + trim-width
#let spine-start = back-cover-end
#let spine-end = spine-start + spine-width
#let front-cover-start = spine-end
#let front-cover-end = front-cover-start + trim-width

// Full bleed background
#place(top + left, rect(width: 100%, height: 100%, fill: deep-navy))

// Spine - slightly darker
#place(
  top + left,
  dx: spine-start,
  rect(width: spine-width, height: 100%, fill: deep-navy.darken(15%))
)

// Spine text (rotated) - reads from bottom to top
#place(
  top + left,
  dx: spine-start,
  dy: bleed,
  box(
    width: spine-width,
    height: trim-height,
  )[
    #set align(center + horizon)
    #rotate(90deg)[
      #box(width: 6in)[
        #set align(center)
        #set text(size: 10pt, tracking: 0.08em, weight: "bold")
        THE 1689 LONDON BAPTIST CONFESSION OF FAITH
        #h(0.8em)
        #text(fill: gold-accent)[|]
        #h(0.8em)
        #text(size: 9pt, weight: "regular")[With Catechisms]
      ]
    ]
  ]
)

// Decorative line on spine edges
#place(top + left, dx: spine-start, rect(width: 0.5pt, height: 100%, fill: gold-accent.transparentize(50%)))
#place(top + left, dx: spine-end, rect(width: 0.5pt, height: 100%, fill: gold-accent.transparentize(50%)))

// === FRONT COVER ===
#place(
  top + left,
  dx: front-cover-start + safety,
  dy: bleed + safety,
  box(
    width: trim-width - 2 * safety,
    height: trim-height - 2 * safety,
  )[
    #set align(center)

    // Top decorative element
    #v(0.35in)
    #line(length: 2in, stroke: 0.5pt + gold-accent)

    #v(0.2in)

    // Year - prominent
    #text(size: 42pt, tracking: 0.1em, fill: gold-accent, weight: "bold")[1689]


    // Main title
    #text(size: 14pt, tracking: 0.2em)[THE]
    #v(0.03in)
    #text(size: 20pt, tracking: 0.12em)[LONDON]
    #v(0.03in)
    #text(size: 38pt, weight: "bold", tracking: 0.05em)[BAPTIST]
    #v(0.03in)
    #text(size: 24pt, tracking: 0.1em)[CONFESSION]
    #v(0.03in)
    #text(size: 14pt, tracking: 0.2em)[OF FAITH]

    #v(0.2in)

    // Subtitle
    #text(size: 14pt, style: "italic")[With Catechisms]

    #v(0.12in)

    // Catechism names
    #text(size: 10pt, tracking: 0.1em)[
      THE BAPTIST CATECHISM (1695)\
      AN ORTHODOX CATECHISM (1680)
    ]

    #v(0.15in)
    #v(1fr)

    // Bottom decorative element
    #line(length: 1.5in, stroke: 0.5pt + gold-accent)
    #v(0.12in)
    #text(size: 9pt, tracking: 0.15em, fill: gold-accent)[SOLA SCRIPTURA]
    #v(0.2in)
  ]
)

// === BACK COVER ===
#place(
  top + left,
  dx: back-cover-start + bleed + safety,
  dy: bleed + safety,
  box(
    width: trim-width - 2 * safety,
    height: trim-height - 2 * safety,
  )[
    #set align(center)
    #set text(size: 11pt, fill: cream)
    #set par(justify: true, leading: 0.8em)

    #v(1fr)

    #pad(x: 0.3in)[
      _We shall conclude with our earnest prayer, that the God of all
      grace, will pour out those measures of his holy Spirit upon us, that
      the profession of truth may be accompanied with the sound belief,
      and diligent practice of it by us; that his name may in all things be
      glorified, through Jesus Christ our Lord. Amen._
    ]

    #v(1fr)

    // Leave space for barcode area
    #v(1.5in)
  ]
)
