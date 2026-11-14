#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.14.0": press-seal

// Full-wrap paperback cover of Owen on Sin, the print volume of Of Temptation and The
// Mortification of Sin, in the design of Owen's sin books (no picture, the verses the
// books open as the image; plate_cover.typ). The editor asked for both books' colours:
// Of Temptation's slate blue above with its verse (Matthew 26:41), Mortification's
// oxblood below with its own (Romans 8:13), in the books' order, the blue deepening into
// the oxblood down the whole wrap (the editor's choice over a hard split at a gold rule).
// The back: Owen's most quoted line, from Mortification chapter II.
//
// `pages` here is only for compiling the cover by itself; ./fgb build gives it the
// interior's page count.
#let ink = rgb("#ECEEF0")
#let gold = rgb("#D6A55A")
#let blue = rgb("#1D2838")       // Of Temptation
#let oxblood = rgb("#3A1E1E")    // The Mortification of Sin
#let ground = ((blue, 0%), (blue, 30%), (oxblood, 72%), (oxblood, 100%))
// opaque: the ink mixed with the ground it sits on, not transparent (Lulu flattens at its height
// transparency into image tiles: scripts/plate_cover.typ)
#let behind = gradient.linear(..ground).sample(45%)

#plate-cover(
  ground: ground,
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 13pt, tracking: 0.12em,
      fill: color.mix((ink, 65%), (behind, 35%)), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 18pt,
      tracking: 0.14em, fill: gold, body)
    let verse(dy, body, source) = place(dx: 0.5in, dy: dy, box(width: 4.5in, {
      set align(center)
      set par(leading: 0.55em, spacing: 0pt)
      body
      v(0.16in)
      caps(source, 8pt, color.mix((gold, 80%), (behind, 20%)), tracking: 0.25em)
    }))
    verse(3.05in, {
      gilt[Watch and pray,]
      v(0.06in)
      [#plain[that ye enter not] \
       #plain[into]#h(0.1in)#gilt[temptation.]]
    }, [Matthew xxvi. 41])
    verse(5.0in, {
      [#plain[If ye through the Spirit] \
       #plain[do]#h(0.1in)#gilt[mortify] \
       #plain[the deeds of the body,]]
      v(0.06in)
      gilt[ye shall live.]
    }, [Romans viii. 13])
  }),
  title-y: 0.85in,
  seal: press-seal,
  title: [Owen on Sin],
  // the two books' titles: a size above the house's 11pt subtitle, as they name the volume's contents
  subtitle: text(size: 13pt)[Of Temptation \ The Mortification of Sin],
  author: [John Owen],
  spine-title: [Owen on Sin],
  spine-author: [Owen],
  pages: 262,
  ink: ink,
  accent: gold,
  // as the two books: the seal and name plate in gold, the fountain and lettering cut
  // in the ground's dark (the oxblood's, at the foot)
  label: gold,
  paper: rgb("#241212"),
  epigraph: [
    Do you mortify; do you make it your daily work; be always at it whilst you live;
    cease not a day from this work; be killing sin or it will be killing you.
  ],
  epigraph-source: [The Mortification of Sin, Chapter II],
)
