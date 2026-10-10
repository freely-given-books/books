// Full-wrap cover for the imprint's single-volume books.
//
// The design is the one The Secret Key of Heaven and The Glorious Feast of the
// Gospel were printed with, and it is what tells those books apart from the
// John Gill commentary (scripts/cover.typ, a dark ground, for a numbered set
// meant to be read as one shelf).  Here every book is its own: a warm ground
// across the whole wrap, a single panel of colour on the front carrying the
// title, and a cream spine.  What distinguishes one author from the next is
// that panel colour, so a palette is the first thing to choose.
//
//   #import "panel_cover.typ": *
//   #panel-cover(
//     title: [Christian Economy],
//     subtitle: [Or, A Short Survey ...],
//     author: [William Perkins],
//     pages: 130,
//     palette: "mulberry",
//     epigraph: [...],
//     epigraph-source: [Joshua 24:15],
//   )
//
// A cover has no running text, so panel-cover() is called rather than shown.
//
// The ebook cover is the front panel alone, at the trim size: compile with
// `--input front-only=true` (./fgb build does, rendering it to an image), or
// pass `front-only: true`.
//
// PRINT SPECIFICATIONS  ------------------------------------------------------
//
// Perfect binding, following Lulu's formulas.  Printer specs change, so
// download the live template for the trim and paper you are buying and check
// the wrap against it before ordering.
//
//   document = bleed + trim + spine + trim + bleed  by  bleed + trim + bleed
//   spine    = pages / 444 + 0.06in   (Lulu's published paperback formula)
//
// Everything here is computed from `pages` and the trim, and ./fgb build
// passes both from the compiled interior (--input pages=N, trim-width=W,
// trim-height=H, in inches), so a cover cannot fall out of step with its
// book. The `pages` and trim given in a cover file are only for compiling
// it by itself.

// Paper calipers, in inches per page (one leaf is two pages).
#let CALIPER = (
  "cream-60": 0.0025,          // Lulu 60# cream -- the usual choice for these
  "white-60": 0.002252,
  "white-80-coated": 0.0032,
)

#let BLEED = 0.125in           // trimmed off all four sides
#let SAFETY = 0.5in            // keep type this far inside the trim
#let PANEL_INSET = 0.3in       // the ground showing as a border around the panel

// One palette per author, so a shelf of these reads as a set of individuals
// rather than a series.  `ground` is the colour of the whole wrap, `panel` the
// block of colour on the front, `ink` the type on it and on the spine, `rule`
// the thin decorative lines, and `subtitle` the near-black used for the one
// line set against the ink.
//
// Both the ground and the panel want to be kept apart from the books already
// in print, and apart in hue rather than only in value: near-white creams and
// muted panels all read as the same book from across a room.
#let PALETTES = (
  // Thomas Brooks, The Secret Key of Heaven.
  sage: (
    ground:   rgb("#F5F3EC"),
    panel:    rgb("#C5CEBC"),
    ink:      rgb("#3C5A44"),
    rule:     rgb("#C8982A"),
    subtitle: rgb("#2A2A2A"),
  ),
  // Richard Sibbes, The Glorious Feast of the Gospel.
  sky: (
    ground:   rgb("#F5F5DC"),
    panel:    rgb("#B5D8E8"),
    ink:      rgb("#3A6A8A"),
    rule:     rgb("#3A6A8A"),
    subtitle: rgb("#2A2A2A"),
  ),
  // William Perkins, Christian Economy.  A sand ground rather than the pale
  // creams above -- the ground is most of the wrap, so it is what tells this
  // book from those at a glance.
  //
  // Two panels were cut for it and either works over that ground: mulberry,
  // below, and hearth brick, panel #BE7264 with rule #8A4438.
  mulberry: (
    ground:   rgb("#EADFC8"),
    // Halfway between the first cut of this panel, #A2707F, and #B68A97: the
    // lighter one gave the umber title 4.7:1 to work against but read pink,
    // so this sits between them at about 4:1, with a shade less red to keep
    // it mauve.  Lightening much past #B68A97 also starts closing the panel
    // on the sand ground.
    panel:    rgb("#A97D8A"),
    ink:      rgb("#40261A"),
    rule:     rgb("#6E4250"),
    subtitle: rgb("#2A2A2A"),
  ),
  // William Gouge, Of Domestical Duties.  The hearth brick that was cut as
  // the alternative panel for Perkins and not used: a household book earns
  // it, and it is the one warm red on a shelf whose other panels are a green,
  // a blue and a mauve.  The ground is a paler, greyer cream than Perkins's
  // sand so the two warm books do not read as a pair.
  hearth: (
    ground:   rgb("#F2EDE3"),
    panel:    rgb("#BE7264"),
    ink:      rgb("#33211C"),
    rule:     rgb("#8A4438"),
    subtitle: rgb("#2A2A2A"),
  ),
  // John Bunyan, The Pilgrim's Progress.  Ochre gold, after the gold type of
  // the book's first cover, and the one yellow on a shelf of green, blue,
  // mauve and red; the ground is a cool stone so it does not warm into the
  // creams and sands of the others.
  ochre: (
    ground:   rgb("#E9E8E2"),
    panel:    rgb("#C9A24E"),
    ink:      rgb("#2E2618"),
    rule:     rgb("#7A5A1E"),
    subtitle: rgb("#2A2A2A"),
  ),
  // Benjamin Keach, The Gospel Minister's Maintenance Vindicated.  The one
  // dark book on the shelf: every other wrap is a pale ground, so a midnight
  // navy ground tells this one apart at any distance, face out or end-on.
  // The type turns light to match -- cream on the panel and spine, gold rules
  // -- and the panel is a lifted navy, enough to read as a block on the
  // ground without going pale like Sibbes's sky.
  midnight: (
    ground:   rgb("#18213A"),
    panel:    rgb("#2D3D66"),
    ink:      rgb("#F3EBD3"),
    rule:     rgb("#C9A24E"),
    subtitle: rgb("#DCD4BE"),
  ),
  // John Owen, The Mortification of Sin.  Slate: the one grey on a shelf of
  // green, blue, mauve, red, gold and navy -- a cool blue-grey panel on a
  // warm paper ground, with ink near black-blue, plain as the book is.
  slate: (
    ground:   rgb("#F1EEE6"),
    panel:    rgb("#97A1AB"),
    ink:      rgb("#1F2A35"),
    rule:     rgb("#4A5866"),
    subtitle: rgb("#2A2A2A"),
  ),
)

#let spine-width(pages, paper: "cream-60") = pages * CALIPER.at(paper) * 1in

// Lulu publishes its own paperback spine formula, `pages / 444 + 0.06in`,
// which is not the same as page count times caliper.  The two agree to within
// a thousandth of an inch under about 240 pages and drift apart as a book
// grows: at 800 pages they differ by 0.14in, more than the 0.125in trim
// tolerance, which is enough to put the fold onto a cover.  Lulu's is the
// one every cover uses; spine-width() is kept for comparison.
#let lulu-spine(pages) = (pages / 444.0 + 0.06) * 1in

#let panel-cover(
  title: [Book],
  subtitle: none,
  author: [Author],
  // A volume label for a set ("Volume II"), set under the title on the front
  // and after the title on the spine.  Four volumes shelved together have to
  // be tellable apart end-on, so the spine carries it in either style.
  volume: none,
  pages: 200,
  // The paper caliper of spine-width(); unused now that the spine is Lulu's
  // formula, and kept so older cover files still compile.
  paper: "cream-60",
  trim-width: 5.5in,
  trim-height: 8.5in,
  // A name from PALETTES, or a dictionary of the same keys.  A dictionary is
  // merged over the palette named by `base`, so a book can take one of the
  // above and change a single colour of it.
  palette: "mulberry",
  base: "mulberry",
  // The back cover: a passage, its reference, and optionally something set
  // above them (a table of contents, a note on the text).
  epigraph: none,
  epigraph-source: none,
  back-lead: none,
  // How the spine is set.  "plain" is the title and author with a rule between
  // them, which is what the books already printed carry; "ruled" brackets them
  // with a pair of rules at head and foot and sets the title in tracked caps.
  // One per book, so a shelf of these is tellable apart end-on.
  //
  // The spine is never given a colour of its own, in any style.  A wrap folded
  // slightly off-centre puts part of the spine onto a cover, and a spine in
  // its own colour shows that as a stripe down the front; keeping it the same
  // as the ground makes a crooked fold invisible.
  spine-style: "plain",
  // Sizes worth reaching for when a title is long or a spine is thin.
  title-size: 32pt,
  subtitle-size: 11pt,
  spine-title-size: 11pt,
  // Lulu needs a clear white field to drop the barcode into, but only once the
  // book has an ISBN; before that the foot of the back cover is just left
  // empty for it.
  isbn: none,
  // An explicit spine width, overriding Lulu's formula (lulu-spine): only
  // for a printer whose template says otherwise.
  spine: none,
  font: ("Libertinus Serif", "Liberation Serif"),
  // Only the front cover, trimmed (no bleed, spine or back): the ebook cover.
  front-only: sys.inputs.at("front-only", default: "false") == "true",
) = {
  let pal = PALETTES.at(base) + (
    if type(palette) == str { PALETTES.at(palette) } else { palette }
  )
  // the interior's page count and trim, when ./fgb build passes them
  let pages = int(sys.inputs.at("pages", default: str(pages)))
  let trim-width = if "trim-width" in sys.inputs {
    float(sys.inputs.at("trim-width")) * 1in } else { trim-width }
  let trim-height = if "trim-height" in sys.inputs {
    float(sys.inputs.at("trim-height")) * 1in } else { trim-height }
  let spine = if spine != none { spine } else { lulu-spine(pages) }

  let page-width = 2 * BLEED + 2 * trim-width + spine
  let page-height = 2 * BLEED + trim-height

  let back-x = BLEED
  let spine-x = BLEED + trim-width
  let front-x = spine-x + spine

  set page(width: page-width, height: page-height, margin: 0pt) if not front-only
  set page(width: trim-width, height: trim-height, margin: 0pt) if front-only
  set text(font: font)

  // The whole wrap is laid out either way; for the front alone it is shifted
  // so the front's trim box is the page, and the rest falls outside it.
  let wrap(body) = if front-only {
    place(top + left, dx: -front-x, dy: -BLEED,
      box(width: page-width, height: page-height, body))
  } else { body }
  wrap({

  // The ground runs the whole sheet, so the bleed is covered on every side and
  // the spine is the same colour as the covers: a fold that drifts has nothing
  // to reveal.
  place(top + left, rect(width: 100%, height: 100%, fill: pal.ground))

  // --- Front cover ---------------------------------------------------------
  // The panel is inset from the trim rather than run to the bleed, so the
  // ground frames it on all four sides after the cut.
  place(top + left, dx: front-x + PANEL_INSET, dy: BLEED + PANEL_INSET,
    rect(width: trim-width - 2 * PANEL_INSET,
         height: trim-height - 2 * PANEL_INSET,
         fill: pal.panel))

  place(top + left, dx: front-x + SAFETY, dy: BLEED + SAFETY,
    box(width: trim-width - 2 * SAFETY, height: trim-height - 2 * SAFETY)[
      #set align(center)
      #set text(fill: pal.ink)

      #v(1.4in)
      #text(size: title-size, title)
      #if volume != none {
        v(0.18in)
        text(size: 13pt, tracking: 0.22em, upper(volume))
      }
      #v(0.35in)
      #line(length: 2.2in, stroke: 0.75pt + pal.rule)
      #if subtitle != none {
        v(0.25in)
        text(size: subtitle-size, fill: pal.subtitle, style: "italic", subtitle)
        v(0.25in)
        line(length: 2.2in, stroke: 0.75pt + pal.rule)
      }

      #v(1fr)
      #text(size: 12pt, tracking: 0.15em, upper(author))
      #v(0.3in)
    ])

  // --- Spine ---------------------------------------------------------------
  // Rotated to read top to bottom, as a book laid face up on a table reads.
  let ruled = spine-style == "ruled"

  place(top + left, dx: spine-x, dy: BLEED,
    box(width: spine, height: trim-height)[
      #set align(center + horizon)

      // The rules run across the spine rather than along it, so they read as
      // caps on the lettering when the book is shelved.  Held inside the spine
      // by a sixteenth of an inch, the same clearance the type gets.
      #if ruled {
        let rule-width = spine - 0.125in
        for edge in (top + center, bottom + center) {
          let sign = if edge == top + center { 1.0 } else { -1.0 }
          place(edge, dy: sign * 0.5in,
            rect(width: rule-width, height: 1.2pt, fill: pal.rule))
          place(edge, dy: sign * 0.56in,
            rect(width: rule-width, height: 0.5pt, fill: pal.rule))
        }
      }

      #rotate(90deg, box(width: trim-height - 1.5in)[
        #set align(center)
        #set text(fill: pal.ink)
        // a title set on two lines on the front runs on along the spine
        #show linebreak: [ ]
        #if ruled {
          text(size: spine-title-size - 1.5pt, tracking: 0.18em, upper(title))
          if volume != none {
            h(0.8em)
            text(size: spine-title-size - 2.5pt, tracking: 0.18em, upper(volume))
          }
          h(1.2em)
          text(size: (spine-title-size - 1.5pt) * 0.8,
               fill: pal.rule)[#sym.diamond.filled]
          h(1.2em)
          text(size: spine-title-size - 2.5pt, tracking: 0.12em, upper(author))
        } else {
          text(size: spine-title-size, weight: "bold", tracking: 0.05em, title)
          if volume != none {
            h(0.6em)
            text(size: spine-title-size - 1pt, weight: "bold", volume)
          }
          h(1em)
          text(fill: pal.rule)[|]
          h(1em)
          text(size: spine-title-size - 1pt, author)
        }
      ])
    ])

  // --- Back cover ----------------------------------------------------------
  place(top + left, dx: back-x + SAFETY, dy: BLEED + SAFETY,
    box(width: trim-width - 2 * SAFETY, height: trim-height - 2 * SAFETY)[
      #set align(center)
      #set par(leading: 0.9em)
      #set text(fill: pal.subtitle)

      #if back-lead != none {
        v(0.6in)
        back-lead
      }

      #if epigraph != none {
        v(if back-lead == none { 1.8in } else { 0.4in })
        pad(x: 0.2in)[
          #text(size: 13pt, fill: pal.ink, style: "italic", epigraph)
          #v(0.3in)
          #line(length: 1.5in, stroke: 0.75pt + pal.rule)
          #v(0.2in)
          #text(size: 11pt, epigraph-source)
        ]
      }

      #v(1fr)

      // The barcode field, or the space kept clear for one.
      #if isbn != none {
        box(fill: white, width: 2in, height: 1.2in)
        v(0.1in)
        text(size: 8pt)[ISBN #isbn]
      } else {
        v(1.5in)
      }
    ])
  })
}
