#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.15.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ): a small framed picture on the dark green ground, the
// editor's choice for a short book (2026-11-15). The picture is Edwards' own:
// "that River of water of life, that proceeds from the throne of God and the
// Lamb" (Rev 22:1), its source in the light beyond the hills. ChatGPT engraving
// (fgbooks-generated-art "God Glorified (river, light at source)"), hand-tinted
// by art/tint.py into art/plate.jpg. At about 40 pages the spine carries nothing.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#EEEBE3")
#let gold = rgb("#D6A55A")
#let ground = rgb("#23332E")

// opaque: the ink mixed with the ground it sits on, not transparent (Lulu flattens
// transparency into image tiles: scripts/plate_cover.typ)
#plate-cover(
  ground: ground,
  // the picture in a frame of gold, the river's source near its top third
  art: box(width: 4.25in, height: 6.875in, place(dx: 0.55in, dy: 2.2in,
    block(width: 3.15in, height: 2.65in, clip: true, stroke: 0.6pt + gold,
      place(top + left, dx: -0.35in, dy: -1.62in,
        image("art/plate.jpg", width: 3.85in, height: 5.775in))))),
  // the pocket trim as the default too (./fgb build passes it for the print cover,
  // but the ebook's front is rendered without it), as Sinners' cover does
  trim-width: 4.25in,
  trim-height: 6.875in,
  title-y: 0.62in,
  seal: press-seal,
  title: [God Glorified],
  tail: [in Man's Dependence],
  subtitle: [A Sermon Preached in Boston, July 8, 1731],
  author: [Jonathan Edwards],
  spine-author: [Edwards],
  title-size: 28pt,
  pages: 40,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#17221F"),
  epigraph: [
    The sum of the blessings, which the redeemed shall receive in heaven, is that
    River of water of life, that proceeds from the throne of God and the Lamb.
  ],
  epigraph-source: [God Glorified in Man's Dependence],
)
