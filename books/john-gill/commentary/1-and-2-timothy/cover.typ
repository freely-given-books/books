// Full-wrap cover for the John Gill commentary set.
//
// The volumes are meant to be seen together on a shelf, so the ground, the
// gold rules and the spine layout are identical in every one; what changes is
// the book's name, a small band of colour marking which division of Scripture
// it belongs to, and -- if the set has been numbered -- a volume numeral.  Read across a shelf those bands
// group the set into Law, History, Poetry, Prophets, Gospels and Epistles.
//
//   #import "cover.typ": *
//   #cover(
//     book: [1 & 2 Timothy],
//     subtitle: [The Epistles of Paul the Apostle to Timothy],
//     volume: 11,           // omit for an unnumbered volume
//     pages: 216,
//     division: "epistles",
//     binding: "paperback",     // or "hardcover"
//     isbn: "978-1-234567-89-0",   // omit until the book has one
//   )
//
// A cover has no running text, so cover() is called rather than shown.
//
// PRINT SPECIFICATIONS  ------------------------------------------------------
//
// The measurements below follow Lulu's published formulas.  Printer specs
// change, so before ordering, download the live template for the trim, paper
// and binding you are buying and check the spine width and wrap against it.
//
//   Paperback (perfect bound)
//     document = bleed + trim + spine + trim + bleed  by  bleed + trim + bleed
//     spine    = pages x paper caliper
//
//   Hardcover (case wrap)
//     the boards stand proud of the text block, and the printed sheet wraps
//     around them and is turned in, so the sheet is much larger than the trim
//     document = wrap + board + spine + board + wrap
//     board    = trim + 0.125in on the fore edge, trim + 0.25in tall
//     spine    = pages x caliper + 0.25in for the two boards
//
// Perfect binding needs roughly 32 pages.  The spine is trimmed to within
// 0.125in either way, so 0.25in of every spine is at risk: everything printed
// on the spine is set inside what is left, and a spine under about 0.41in is
// left blank because too little of it is guaranteed to survive the cut.
// gill_build_volume.py warns about both.

// Paper calipers, in inches per page (one leaf is two pages).
#let CALIPER = (
  "cream-60": 0.0025,          // Lulu 60# cream -- the usual choice for these
  "white-60": 0.002252,
  "white-80-coated": 0.0032,
)

#let BLEED = 0.125in           // paperback bleed on all four sides
#let WRAP = 0.75in             // hardcover turn-in on all four sides
#let BOARD_FORE = 0.125in      // board overhang at the fore edge
#let BOARD_HEAD = 0.125in      // board overhang at head and foot, each
#let BOARD_SPINE = 0.25in      // the two boards' thickness, added to the spine
#let SAFETY = 0.5in            // keep type this far inside the trim
// Lulu trims the spine to within 0.125in either way, so the fold can land that
// far onto the front or the back cover.  Type has to stay inside the spine by
// this much.  Nothing is run past it instead: the wrap is a single flat colour,
// so a drifting cut has nothing to reveal.
#let SPINE_TRIM = 0.125in
#let HINGE = 0.375in           // hardcover: keep type this far off the spine

// The set's palette.  The gold and cream are the imprint's, already used on
// the other Freely Given books; the dark ground is what sets the commentary
// apart from them on the shelf.
// One flat ground across the whole wrap, spine included.  A spine printed in
// its own shade spills onto the covers whenever a book is bound slightly
// crooked; keeping it identical makes that drift invisible.
#let ground = rgb("#3A1B22")        // deep oxblood
#let gold = rgb("#C8982A")
#let gold-pale = rgb("#E0C26A")
#let cream = rgb("#F5F3EC")
#let cream-dim = rgb("#CFC7BC")

// One colour per division of Scripture, for the bar on the spine.
#let DIVISIONS = (
  law:      (tint: rgb("#9A7433")),
  history:  (tint: rgb("#7C7A3C")),
  poetry:   (tint: rgb("#4F7B60")),
  prophets: (tint: rgb("#3F6E86")),
  gospels:  (tint: rgb("#A65437")),
  epistles: (tint: rgb("#7A5391")),
)

#let roman(n) = numbering("I", n)

#let ornament(width: 1.6in, fill: gold) = {
  set align(center)
  stack(
    dir: ltr,
    spacing: 0.5em,
    align(horizon, line(length: width / 2 - 0.5em, stroke: 0.6pt + fill)),
    text(7pt, fill: fill)[#sym.diamond.filled],
    align(horizon, line(length: width / 2 - 0.5em, stroke: 0.6pt + fill)),
  )
}

#let spine-width(pages, binding: "paperback", paper: "cream-60") = {
  let leaves = pages * CALIPER.at(paper) * 1in
  if binding == "hardcover" { leaves + BOARD_SPINE } else { leaves }
}

#let cover(
  book: [Book],
  subtitle: none,
  volume: none,
  pages: 200,
  division: "epistles",
  binding: "paperback",
  paper: "cream-60",
  trim-width: 6in,
  trim-height: 9in,
  series: [An Exposition of the Old and New Testament],
  author: [John Gill],
  contents: none,
  epigraph: none,
  epigraph-source: none,
  // Given an ISBN, the back cover carries a white barcode field for the
  // printer.  Without one it carries nothing there.
  isbn: none,
) = {
  let band = DIVISIONS.at(division)
  let spine = spine-width(pages, binding: binding, paper: paper)

  // Geometry.  Both bindings are laid out as: an outer margin the trimmer or
  // the turn-in eats, then back cover, spine, front cover.
  let hardcover = binding == "hardcover"
  let margin = if hardcover { WRAP } else { BLEED }
  let panel-width = trim-width + if hardcover { BOARD_FORE } else { 0in }
  let panel-height = trim-height + if hardcover { 2 * BOARD_HEAD } else { 0in }

  let page-width = 2 * margin + 2 * panel-width + spine
  let page-height = 2 * margin + panel-height

  let back-x = margin
  let spine-x = margin + panel-width
  let front-x = spine-x + spine

  // Type stays clear of the trim, and on a hardcover also of the hinge crease
  // where the board folds.
  let inset = SAFETY + if hardcover { BOARD_FORE } else { 0in }
  let spine-clear = if hardcover { HINGE } else { 0in }

  set page(width: page-width, height: page-height, margin: 0pt)
  set text(font: ("Libertinus Serif", "Liberation Serif"), fill: cream,
           hyphenate: false)

  // Ground, across the whole sheet so the bleed and turn-in are covered.  The
  // spine is not distinguished: see the note on `ground` above.
  place(top + left, rect(width: 100%, height: 100%, fill: ground))

  // --- Front cover ---------------------------------------------------------
  place(top + left, dx: front-x + spine-clear, dy: margin,
    box(width: panel-width - spine-clear, height: panel-height)[
      #set align(center)
      // A double rule frame, the set's most visible signature.
      #place(top + left, dx: inset - 0.22in, dy: inset - 0.22in,
        rect(width: panel-width - spine-clear - 2 * inset + 0.44in,
             height: panel-height - 2 * inset + 0.44in,
             stroke: 1.4pt + gold))
      #place(top + left, dx: inset - 0.16in, dy: inset - 0.16in,
        rect(width: panel-width - spine-clear - 2 * inset + 0.32in,
             height: panel-height - 2 * inset + 0.32in,
             stroke: 0.5pt + gold))

      #place(top + left, dx: inset, dy: inset,
        box(width: panel-width - spine-clear - 2 * inset,
            height: panel-height - 2 * inset)[
        #set align(center)
        #text(8.5pt, tracking: 0.22em, fill: gold-pale, upper(series))
        #v(0.42in)
        #ornament(width: 1.5in)
        #v(1fr)
        #text(34pt, weight: 600, fill: cream, hyphenate: false, book)
        #v(0.3in)
        #if subtitle != none {
          block(width: 88%, text(10.5pt, style: "italic", fill: cream-dim, subtitle))
        }
        #v(1.25fr)
        #ornament(width: 1.5in)
        #v(0.35in)
        #text(15pt, tracking: 0.2em, fill: gold, upper(author))
        #v(0.28in)
        // The division mark, the one element that differs across the shelf.
        // It stands on its own when the volume is unnumbered.
        #rect(width: 0.9in, height: 2.5pt, fill: band.tint, stroke: none)
        #if volume != none {
          v(0.12in)
          text(8pt, tracking: 0.24em, fill: gold-pale)[VOLUME #roman(volume)]
        }
      ])
    ])

  // --- Spine ---------------------------------------------------------------
  // Rotated to read top to bottom, as a book laid face up on a table reads.
  // Everything set on the spine is sized against `safe` rather than the spine
  // itself: that is the strip guaranteed to survive the worst trim.
  let clamp(value, low, high) = calc.max(low, calc.min(value, high))
  let safe = spine - 2 * SPINE_TRIM
  if safe >= 0.16in {
    let safe-pt = safe / 1in * 72pt
    // The furniture is proportioned to the spine, so a thin volume and a thick
    // one look like the same design rather than the same design shrunk, and
    // held to a narrow range so a shelf still lines up.
    let rule = clamp(safe * 0.65, 0.14in, 0.55in)
    let title-size = clamp(safe-pt * 0.62, 8pt, 22pt)
    let author-size = clamp(title-size * 0.6, 6.5pt, 12pt)
    place(top + left, dx: spine-x, dy: margin,
      box(width: spine, height: panel-height)[
        #set align(center + horizon)
        #place(top + center, dy: 0.42in, rect(width: rule, height: 1.6pt, fill: gold))
        #place(top + center, dy: 0.47in, rect(width: rule, height: 0.6pt, fill: gold))
        #place(bottom + center, dy: -0.42in, rect(width: rule, height: 1.6pt, fill: gold))
        #place(bottom + center, dy: -0.47in, rect(width: rule, height: 0.6pt, fill: gold))
        // The division band crosses the foot of every spine in the set, at the
        // same height whatever the volume's bulk, so a shelf reads as a row.
        // It is a stripe rather than a panel: it has to look deliberate on the
        // many volumes that carry no numeral.
        // Held inside the safe strip rather than run to the fold: it is the
        // one coloured element on the spine, and reaching the edge is what
        // lets colour spill onto a cover when the cut drifts.  Kept low so it
        // reads as a bar even on a thin spine, where the safe strip is narrow
        // enough that anything taller would come out square.
        #place(bottom + center, dy: -0.66in,
          rect(width: safe - 0.06in, height: 0.12in,
               fill: band.tint, stroke: none))
        #if volume != none {
          // Upright, so it reads head-on when the book is shelved.
          place(bottom + center, dy: -0.84in,
            text(clamp(safe-pt * 0.42, 6pt, 9.5pt), tracking: 0.06em,
                 fill: gold, weight: 600, roman(volume)))
        }
        #rotate(90deg, reflow: false,
          box(width: panel-height - 2.6in, height: safe)[
            #set align(center + horizon)
            #stack(
              dir: ltr,
              spacing: 0.9em,
              align(horizon, text(title-size, weight: 600, fill: cream,
                                  hyphenate: false, book)),
              align(horizon, text(author-size * 0.7, fill: gold)[#sym.diamond.filled]),
              align(horizon, text(author-size, tracking: 0.18em, fill: gold,
                                  upper(author))),
            )
          ])
      ])
  }

  // --- Back cover ----------------------------------------------------------
  place(top + left, dx: back-x, dy: margin,
    box(width: panel-width - spine-clear, height: panel-height)[
      #place(top + left, dx: inset - 0.22in, dy: inset - 0.22in,
        rect(width: panel-width - spine-clear - 2 * inset + 0.44in,
             height: panel-height - 2 * inset + 0.44in,
             stroke: 0.5pt + gold))

      #place(top + left, dx: inset, dy: inset,
        box(width: panel-width - spine-clear - 2 * inset,
            height: panel-height - 2 * inset,
            inset: (x: 0.1in))[
        #set align(center)
        // The back carries a verse and the imprint, nothing else, so the two
        // float against each other rather than stacking from the top.
        #v(1.05fr)
        #if epigraph != none {
          block(width: 88%)[
            #set par(justify: false, leading: 0.8em)
            #text(13pt, style: "italic", fill: cream, epigraph)
            #if epigraph-source != none {
              v(0.22in)
              text(9.5pt, fill: gold)[#sym.dash.em #epigraph-source]
            }
          ]
          v(0.34in)
          ornament(width: 1.2in)
        }
        #v(1.35fr)
        #if contents != none {
          text(8.5pt, tracking: 0.14em, fill: gold-pale, upper(contents))
          v(0.28in)
        }
        #rect(width: 0.6in, height: 2pt, fill: band.tint, stroke: none)
        #v(0.16in)
        #text(8pt, fill: cream-dim)[
          Public domain. Freely you have received; freely give.
        ]
        #v(0.08in)
        #text(8.5pt, tracking: 0.08em, fill: gold)[books.freely.giving]
        // A printer needs a clear white field to drop the barcode into, but
        // only once the book has an ISBN; before that it is just a white hole.
        #if isbn != none {
          v(0.22in)
          box(fill: white, width: 2in, height: 1.2in)
          v(0.1in)
          text(7.5pt, tracking: 0.05em, fill: cream-dim)[ISBN #isbn]
        }
      ])
    ])
}
