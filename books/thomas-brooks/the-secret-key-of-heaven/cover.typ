// Cover for The Secret Key of Heaven — Thomas Brooks
// Lulu Print Template Specifications:
// - Total document size (with bleed): 11.975" × 8.75"
// - Book trim size: 5.5" × 8.5"
// - Spine width: 0.725" (290 pages × 0.0025" cream paper)
// - Bleed: 0.125"
// - Safety margin: 0.5" from trim

#set page(
  width: 11.975in,
  height: 8.75in,
  margin: 0pt,
)

#set text(font: "Liberation Serif")

// Colors
#let cream       = rgb("#F5F3EC")   // warm cream — overall background
#let sage-panel  = rgb("#C5CEBC")   // soft sage green — front cover panel
#let forest      = rgb("#3C5A44")   // deep forest green — title, author, rules
#let gold        = rgb("#C8982A")   // warm gold — decorative rules
#let text-dark   = rgb("#2A2A2A")   // near-black — subtitle

// Measurements
#let bleed       = 0.125in
#let spine-width = 0.725in  // 290 pages; follow a page-count change
#let trim-width  = 5.5in
#let trim-height = 8.5in
#let safety      = 0.5in
#let panel-inset = 0.3in           // sage panel margin from trim edge

// Calculated positions
#let back-start  = bleed
#let spine-start = bleed + trim-width
#let spine-end   = spine-start + spine-width
#let front-start = spine-end

// Full bleed cream background
#place(top + left, rect(width: 100%, height: 100%, fill: cream))

// === FRONT COVER — sage green panel ===
#place(
  top + left,
  dx: front-start + panel-inset,
  dy: bleed + panel-inset,
  rect(
    width: trim-width - 2 * panel-inset,
    height: trim-height - 2 * panel-inset,
    fill: sage-panel,
  )
)

// Front cover content
#place(
  top + left,
  dx: front-start + safety,
  dy: bleed + safety,
  box(
    width: trim-width - 2 * safety,
    height: trim-height - 2 * safety,
  )[
    #set align(center)
    #set text(fill: forest)

    #v(1.4in)

    // Title
    #text(size: 30pt)[The Secret Key \ of Heaven]

    #v(0.35in)

    // Gold rule
    #line(length: 2.2in, stroke: 0.75pt + gold)

    #v(0.25in)

    // Subtitle
    #text(size: 12pt, fill: text-dark, style: "italic")[
      Or, Twenty Arguments for Closet Prayer
    ]

    #v(0.25in)

    // Gold rule
    #line(length: 2.2in, stroke: 0.75pt + gold)

    #v(1fr)

    // Author
    #text(size: 12pt, tracking: 0.15em)[THOMAS BROOKS]

    #v(0.3in)
  ]
)

// === SPINE ===
// Spine uses cream background like both reference covers
#place(
  top + left,
  dx: spine-start,
  dy: 0in,
  rect(width: spine-width, height: 100%, fill: cream)
)

#place(
  top + left,
  dx: spine-start,
  dy: bleed,
  box(width: spine-width, height: trim-height)[
    #set align(center + horizon)
    #rotate(90deg)[
      #box(width: 7in)[
        #set align(center)
        #set text(fill: forest)
        #text(size: 11pt, weight: "bold", tracking: 0.05em)[
          The Secret Key of Heaven
        ]
        #h(1em)
        #text(fill: gold)[|]
        #h(1em)
        #text(size: 10pt)[Thomas Brooks]
      ]
    ]
  ]
)

// === BACK COVER ===
#place(
  top + left,
  dx: back-start + safety,
  dy: bleed + safety,
  box(
    width: trim-width - 2 * safety,
    height: trim-height - 2 * safety,
  )[
    #set align(center)
    #set par(leading: 0.9em)

    #v(1.8in)

    #pad(x: 0.2in)[
      // #text(size: 13pt, fill: forest, style: "italic")[
      //   "But thou, when thou prayest, enter into thy closet,
      //   and when thou hast shut thy door, pray to thy Father
      //   which is in secret; and thy Father which seeth in secret
      //   shall reward thee openly."
      // ]
      #text(size: 13pt, fill: forest, style: "italic")[
        "But when you pray, go into your closet,
        shut your door, and pray to your Father,
        who is unseen. And your Father, who sees what is done in secret,
        will reward you."
      ]


      #v(0.3in)

      #line(length: 1.5in, stroke: 0.75pt + gold)

      #v(0.2in)

      #text(size: 11pt, fill: text-dark)[— Matthew 6:6]
    ]

    #v(1fr)

    // Space for barcode
    #v(1.5in)
  ]
)
