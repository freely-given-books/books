#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.14.0": press-seal

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
// The pocket trim (4.25 x 6.875in, the interior's), which ./fgb build also passes;
// the front's art is laid out for it, scaled from the first 5.5 x 8.5in design (k).
#let tw = float(sys.inputs.at("trim-width", default: "4.25")) * 1in
#let th = float(sys.inputs.at("trim-height", default: "6.875")) * 1in
#let k = tw / 5.5in
#let stops = ((rgb("#1E0B09"), 0%), (rgb("#2A100D"), 48%), (rgb("#6B1C0E"), 72%),
              (rgb("#B8441C"), 89%), (rgb("#E9923A"), 100%))
// No transparency on a cover (Lulu flattens it into image tiles: plate_cover.typ):
// a faint spark is its colour mixed with the ground behind it, sampled at its height.
#let behind(y) = gradient.linear(..stops).sample((y + 0.125in) / (th + 0.25in) * 100%)

#plate-cover(
  trim-width: tw,
  trim-height: th,
  ground: stops,
  art: box(width: tw, height: th, {
    // sparks going up, a few, at no regular place
    for i in range(46) {
      let x = calc.rem(i * 1.37 + calc.sin(i * 12.9898) * 3.1 + 7, 5.5) * k * 1in
      let t = calc.rem(calc.abs(calc.sin(i * 78.233)) * 43758.5453, 1.0)
      let y = th - t * t * 3.6in * k
      let r = (0.6 + 1.4 * (1 - t)) * k * 1pt
      let a = 100% - (25% + 60% * t)
      place(dx: x, dy: y, circle(radius: r, fill: color.mix((rgb("#F2B25C"), a), (behind(y), 100% - a))))
    }
    // the thread, from above the trim, and the spider small at its end
    let tx = 4.25in * k
    let sy = 4.82in * k
    place(dx: tx, dy: -0.125in, line(start: (0pt, 0pt), end: (0pt, sy + 0.135in * k),
      stroke: 0.45pt + color.mix((ink, 55%), (behind(sy / 2), 45%))))
    place(dx: tx - 0.3in * k, dy: sy, image("art/spider.svg", width: 0.6in * k))
  }),
  title-y: 0.8in,
  title-align: left,
  title-width: tw - 1in,
  seal: press-seal,
  title: [Sinners],
  tail: [in the Hands \ of an Angry God],
  subtitle: [A Sermon Preached at Enfield, July 8th, 1741],
  author: [Jonathan Edwards],
  spine-author: [Edwards],
  title-size: 31pt,
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
