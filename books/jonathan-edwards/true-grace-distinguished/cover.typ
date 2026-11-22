#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.15.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The picture is the sermon's last image: "'Tis the
// day-star risen in the heart, that is a sure forerunner of that sun's rising,
// which will bring on an everlasting day." The night sky, the morning star
// alone over dark hills, the first light low behind them. Vector, drawn here in
// Typst (Sinners' way): a sky of gradient stops, the star a four-pointed figure
// in rings of its own colour mixed with the sky behind it (no transparency: Lulu
// flattens it into image tiles), the hills two filled curves.
//
// At about 80 pages the spine (under 0.25in) carries nothing.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#F1EAD8")
#let gold = rgb("#E3B865")
#let tw = float(sys.inputs.at("trim-width", default: "4.25")) * 1in
#let th = float(sys.inputs.at("trim-height", default: "6.875")) * 1in
// the sky, head to foot (the bleed included): night, the dawn low down, and on the spine and
// back the hills' dark below it, so the foot is one colour round the wrap
#let stops = ((rgb("#0D1526"), 0%), (rgb("#13203A"), 42%), (rgb("#2B3557"), 58%),
              (rgb("#6A4C66"), 66%), (rgb("#C27F5C"), 72%), (rgb("#E4AE72"), 77%), (rgb("#9A6A5E"), 82%),
              (rgb("#3A2F45"), 86%), (rgb("#1A1626"), 91%), (rgb("#1A1626"), 100%))
#let sky(y) = gradient.linear(..stops, angle: 90deg).sample((y + 0.125in) / (th + 0.25in) * 100%)

// a four-pointed star of radius r, its waist w
#let star(r, w, fill) = {
  let pts = ()
  for i in range(8) {
    let a = i * 45deg - 90deg
    let rr = if calc.rem(i, 2) == 0 { r } else { w }
    pts.push((rr * calc.cos(a) + r, rr * calc.sin(a) + r))
  }
  polygon(fill: fill, ..pts)
}

#let art = box(width: tw, height: th, {
  // a few faint stars, high up, at no regular place
  for i in range(34) {
    let x = calc.rem(calc.abs(calc.sin(i * 12.9898)) * 43758.5453, 1.0) * tw
    let t = calc.rem(calc.abs(calc.sin(i * 78.233)) * 24634.6345, 1.0)
    let y = 2.45in + t * 1.7in
    let a = 30% + 50% * (1 - t)
    place(dx: x, dy: y, circle(radius: 0.45pt + 0.5pt * (1 - t), fill: color.mix((ink, a), (sky(y), 100% - a))))
  }
  // the day-star: its glow in rings, then its rays and heart
  let sx = tw * 0.5
  let sy = th * 0.52
  for (r, a) in ((0.66in, 3%), (0.56in, 5%), (0.46in, 7%), (0.37in, 10%), (0.28in, 14%), (0.2in, 20%), (0.13in, 30%)) {
    place(dx: sx - r, dy: sy - r, circle(radius: r, fill: color.mix((gold, a), (sky(sy), 100% - a))))
  }
  let R = 0.62in
  place(dx: sx - R, dy: sy - R, star(R, 0.07in, color.mix((gold, 85%), (sky(sy), 15%))))
  let r2 = 0.3in
  place(dx: sx - r2, dy: sy - r2, rotate(45deg, star(r2, 0.05in, color.mix((gold, 70%), (sky(sy), 30%)))))
  place(dx: sx - 0.05in, dy: sy - 0.05in, circle(radius: 0.05in, fill: rgb("#FFF6DE")))
  // the hills: a far ridge, then the near one, dark against the first light
  place(dx: -0.125in, dy: 0in, curve(
    fill: rgb("#3A2F45"),
    curve.move((0in, th - 1.55in)),
    curve.cubic((1.1in, th - 1.95in), (1.9in, th - 1.4in), (2.8in, th - 1.7in)),
    curve.cubic((3.4in, th - 1.9in), (4.0in, th - 1.75in), (tw + 0.25in, th - 1.85in)),
    curve.line((tw + 0.25in, th + 0.125in)),
    curve.line((0in, th + 0.125in)),
    curve.close(),
  ))
  place(dx: -0.125in, dy: 0in, curve(
    fill: rgb("#1A1626"),
    curve.move((0in, th - 1.2in)),
    curve.cubic((0.9in, th - 1.05in), (1.6in, th - 1.45in), (2.6in, th - 1.25in)),
    curve.cubic((3.3in, th - 1.1in), (3.9in, th - 1.3in), (tw + 0.25in, th - 1.15in)),
    curve.line((tw + 0.25in, th + 0.125in)),
    curve.line((0in, th + 0.125in)),
    curve.close(),
  ))
})

#let cover(edition: none) = plate-cover(
  edition: edition,
  trim-width: tw,
  trim-height: th,
  ground: stops,
  art: art,
  title-y: 0.62in,
  seal: press-seal,
  title: [True Grace],
  tail: [Distinguished from the \ Experience of Devils],
  subtitle: [A Sermon Preached before the Synod of New York, 1752],
  author: [Jonathan Edwards],
  spine-author: [Edwards],
  title-size: 25pt,
  pages: 80,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#111A2E"),
  epigraph: [
    ’Tis the dawning of the light of glory. ’Tis the day-star risen in the
    heart, that is a sure forerunner of that sun’s rising, which will bring on
    an everlasting day.
  ],
  epigraph-source: [True Grace, Distinguished from the Experience of Devils],
)

#cover()
