#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.2": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). No picture of the fire itself: the pit's glow
// rising from the foot with a few sparks, and a single thread let down from
// the head with the spider small at its end, as the sermon has it ("much as
// one holds a spider ... over the fire"; the back gives the sentence). The
// spider is vector (art/spider.svg, made with the cover art's script,
// common-weal-press/sources/vector-art). The fire runs round the whole wrap.
//
// At about 40 pages the spine is too thin for anything on it.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#F6E3CF")

#plate-cover(
  ground: ((rgb("#1E0B09"), 0%), (rgb("#2A100D"), 48%), (rgb("#6B1C0E"), 72%),
           (rgb("#B8441C"), 89%), (rgb("#E9923A"), 100%)),
  art: box(width: 5.5in, height: 8.5in, {
    // sparks going up, a few, at no regular place
    for i in range(46) {
      let x = calc.rem(i * 1.37 + calc.sin(i * 12.9898) * 3.1 + 7, 5.5) * 1in
      let t = calc.rem(calc.abs(calc.sin(i * 78.233)) * 43758.5453, 1.0)
      let y = 8.5in - t * t * 3.6in
      let r = (0.6 + 1.4 * (1 - t)) * 1pt
      place(dx: x, dy: y, circle(radius: r, fill: rgb("#F2B25C").transparentize(25% + 60% * t)))
    }
    // the thread, from above the trim, and the spider small at its end
    let tx = 4.25in
    place(dx: tx, dy: -0.125in, line(start: (0pt, 0pt), end: (0pt, 4.955in),
      stroke: 0.45pt + ink.transparentize(45%)))
    place(dx: tx - 0.3in, dy: 4.82in, image("art/spider.svg", width: 0.6in))
  }),
  title-y: 1.0in,
  title-align: left,
  title-width: 3.5in,
  seal: press-seal,
  title: [Sinners],
  tail: [in the Hands \ of an Angry God],
  subtitle: [A Sermon Preached at Enfield, July 8th, 1741],
  author: [Jonathan Edwards],
  spine-author: [Edwards],
  title-size: 40pt,
  pages: 40,
  ink: ink,
  accent: rgb("#E98A3A"),
  label: rgb("#1C0907"),
  paper: ink,
  epigraph: [
    The God that holds you over the pit of hell, much as one holds a spider,
    or some loathsome insect over the fire, abhors you, and is dreadfully
    provoked … and yet it is nothing but his hand that holds you from falling
    into the fire every moment.
  ],
  epigraph-source: [Sinners in the Hands of an Angry God],
  // isbn: "978-0-000000-00-0",
)
