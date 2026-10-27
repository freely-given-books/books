#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.3": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), on a gold ground. The art is the book's title:
// the key of closet prayer, standing in the arched closet door ("go into your
// closet, shut your door, and pray to your Father", Matthew 6:6, the back's
// text). The key is drawn as vector (art/key.svg, made with the cover art's
// script, common-weal-press/sources/vector-art), so it prints sharp.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let rule-ink = rgb("#5E370B")

// a round-headed arch, ruled
#let arch(w, h, stroke) = curve(stroke: stroke,
  curve.move((0pt, h)), curve.line((0pt, w / 2)),
  curve.cubic((0pt, w / 2 * 0.4477), (w / 2 * 0.4477, 0pt), (w / 2, 0pt)),
  curve.cubic((w / 2 * 1.5523, 0pt), (w, w / 2 * 0.4477), (w, w / 2)),
  curve.line((w, h)), curve.close())

#plate-cover(
  ground: rgb("#C8922C"),
  art: box(width: 5.5in, height: 8.5in, {
    place(dx: 2.75in - 1.2in, dy: 0.5in, arch(2.4in, 4.05in, 1.2pt + rule-ink))
    place(dx: 2.75in - 1.1in, dy: 0.6in, arch(2.2in, 3.95in, 0.4pt + rule-ink))
    place(dx: 2.75in - 1.45in, dy: 4.55in, line(length: 2.9in, stroke: 1.2pt + rule-ink))
    place(center + top, dy: 0.95in, image("art/key.svg", height: 3.45in))
  }),
  title-y: 4.95in,
  seal: press-seal,
  title: [The Secret Key],
  tail: [of Heaven],
  subtitle: [Or, Twenty Arguments for Closet Prayer],
  author: [Thomas Brooks],
  spine-title: [The Secret Key of Heaven],
  spine-author: [Brooks],
  title-size: 27pt,
  pages: 301,
  ink: rgb("#2E1A06"),
  accent: rule-ink,
  label: rgb("#4A2C0C"),
  paper: rgb("#F6E7C4"),
  epigraph: [
    “But when you pray, go into your closet, shut your door, and pray to your
    Father, who is unseen. And your Father, who sees what is done in secret,
    will reward you.”
  ],
  epigraph-source: [Matthew 6:6],
  // isbn: "978-0-000000-00-0",
)
