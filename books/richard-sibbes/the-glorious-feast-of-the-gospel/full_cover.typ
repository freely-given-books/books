// Full cover for Lulu printing
// Template: w4ywv7q-cover-template.pdf
// Total document size (with bleed): 11.731" × 8.75" (297.97mm × 222.25mm)
// Book trim size: 5.5" × 8.5" (139.7mm × 215.9mm)
// Spine width: 0.481" (12.22mm)
// Bleed: 0.125" (3.17mm)
// Safety margin: 0.5" (12.7mm) from trim edge

#set page(
  width: 297.97mm,
  height: 222.25mm,
  margin: 0mm,
)

#set text(
  font: "Libertinus Serif",
  size: 11pt,
)

// Colors matching the theme
#let cream = rgb("#F5F5DC")
#let light-blue = rgb("#B5D8E8")
#let title-blue = rgb("#3A6A8A")  // deeper blue for better contrast
#let text-dark = rgb("#2A2A2A")

// Dimensions
#let bleed = 3.17mm
#let trim-width = 139.7mm
#let trim-height = 215.9mm
#let spine-width = 12.22mm
#let safety = 12.7mm

// Calculated positions
#let back-cover-start = bleed
#let back-cover-end = bleed + trim-width
#let spine-start = back-cover-end
#let spine-end = spine-start + spine-width
#let front-cover-start = spine-end
#let front-cover-end = front-cover-start + trim-width

// Full page cream background
#place(
  top + left,
  rect(
    width: 100%,
    height: 100%,
    fill: cream,
  )
)

// === BACK COVER ===
#place(
  top + left,
  dx: back-cover-start + safety,
  dy: bleed + safety,
  box(
    width: trim-width - 2 * safety,
    height: trim-height - 2 * safety,
    [
      #set text(fill: text-dark)

      #v(1fr)

      // Subtitle/description
      #align(center)[
        #set text(size: 11pt, style: "italic")
        Christ's gracious Invitation and royal Entertainment of Believers.

        Wherein amongst other things these comfortable doctrines are handled:
      ]

      #v(1.5em)

      // List of doctrines
      #set text(size: 10pt)
      #pad(left: 0.5em)[
        1. The Marriage Feast between Christ and the Church.\
        2. The veil of Ignorance and Unbelief removed.\
        3. Christ's Conquest over death.\
        4. The wiping away of tears from the faces of God's people.\
        5. The taking away of their Reproaches.\
        6. The precious Promises of God, and their certain performance.\
        7. The Divine Authority of the Holy Scriptures.\
        8. The Duty and comfort of waiting upon God.
      ]

      #v(1.5em)

      // Decorative separator - matching front cover style
      #align(center)[
        #box(width: 50%, line(length: 100%, stroke: 0.75pt + title-blue))
      ]

      #v(1.5em)

      // Scripture quote
      #set text(size: 9.5pt, style: "italic")
      #pad(x: 0.5em)[
        Wisdom has built her house; she has carved out her seven pillars.

        She has prepared her meat and mixed her wine; she has also set her table.

        She has sent out her maidservants; she calls out from the heights of the city.

        "Whoever is simple, let him turn in here!" she says to him who lacks judgment.

        "Come, eat my bread and drink the wine I have mixed."
      ]

      #v(0.5em)
      #align(right)[
        #set text(size: 9pt, style: "normal")
        — Proverbs 9:1–5
      ]

      #v(1fr)

      // Author credit - styled to match front
      #align(center)[
        #set text(size: 10pt, fill: title-blue, tracking: 1pt)
        RICHARD SIBBES
      ]

      #v(0.5fr)

      // Space reserved for ISBN barcode (92mm × 32mm, positioned bottom-left)
      // Barcode area: 3.622" × 1.26" with 0.5" margin from bleed edge
      #v(32mm)
    ]
  )
)

// === SPINE ===
// Spine background matches rest of cover (cream)
#place(
  top + left,
  dx: spine-start,
  dy: 0mm,
  rect(
    width: spine-width,
    height: 100%,
    fill: cream,
  )
)

// Spine text (rotated - reads bottom to top)
#place(
  top + left,
  dx: spine-start,
  dy: 0mm,
  box(
    width: spine-width,
    height: 100%,
    {
      set text(fill: title-blue)

      // Title on spine - rotated 90 degrees (read from bottom to top)
      place(
        center + horizon,
        dy: -20mm,
        rotate(
          90deg,
          box(
            width: 150mm,
            align(center)[
              #set text(size: 11pt, weight: "bold", tracking: 0.3pt)
              The Glorious Feast of the Gospel
            ]
          )
        )
      )

      // Author on spine - balanced with title
      place(
        center + horizon,
        dy: 50mm,
        rotate(
          90deg,
          box(
            width: 60mm,
            align(center)[
              #set text(size: 10pt, tracking: 0.3pt)
              Richard Sibbes
            ]
          )
        )
      )
    }
  )
)

// === FRONT COVER ===
// Light blue rectangle inset from edges (cream border visible on ALL sides)
#let front-inset = 8mm  // cream border width
#place(
  top + left,
  dx: front-cover-start + front-inset,
  dy: bleed + front-inset,
  rect(
    width: trim-width - 2 * front-inset,  // cream border on both left and right
    height: trim-height - 2 * front-inset,
    fill: light-blue,
  )
)

// Front cover content
#place(
  top + left,
  dx: front-cover-start + safety,
  dy: bleed + safety,
  box(
    width: trim-width - 2 * safety,
    height: trim-height - 2 * safety,
    [
      #set text(fill: title-blue)

      #v(1fr)

      // Main title - unified as single title
      #align(center)[
        #set text(size: 30pt, weight: "regular")
        The Glorious Feast

        of the Gospel
      ]

      #v(2em)

      // Decorative separator - centered line
      #align(center)[
        #box(width: 60%, line(length: 100%, stroke: 1pt + title-blue))
      ]

      #v(2em)

      // Historical subtitle - better line break
      #align(center)[
        #set text(size: 12pt, fill: text-dark, style: "italic")
        The Marriage Feast Between

        Christ and His Church
      ]

      #v(1fr)

      // Author - moved up, less dead space below
      #align(center)[
        #set text(size: 12pt, fill: text-dark, tracking: 2pt)
        RICHARD SIBBES
      ]

      #v(2em)
    ]
  )
)
