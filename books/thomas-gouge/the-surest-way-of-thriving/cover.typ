#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.15.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ): a framed picture on the olive ground, as God Glorified's.
// The picture is the figure Gouge quotes, "money here like the widow's oil, the more
// 'tis poured out, the more it doth increase": the widow of 2 Kings 4 pouring, the
// door shut, her sons bringing the vessels, the full ones set aside. ChatGPT
// engraving (fgbooks-generated-art "Surest Way (widow's oil, door shut)"), coloured by
// ChatGPT and that colour laid under the approved lines by art/transfer.py into
// art/plate.jpg (the editor, 2026-11-15). The back keeps Gouge's own paradox.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let ink = rgb("#EEEBE0")
#let gold = rgb("#D6A55A")
#let ground = rgb("#2C311F")

// opaque: the ink mixed with the ground it sits on, not transparent (Lulu flattens
// transparency into image tiles: scripts/plate_cover.typ)
#plate-cover(
  ground: ground,
  // the picture in a frame of gold: the shut door, the sons, the widow pouring
  art: box(width: 5.5in, height: 8.5in, place(dx: 0.75in, dy: 2.6in,
    block(width: 4.0in, height: 3.85in, clip: true, stroke: 0.6pt + gold,
      place(top + left, dy: -0.958in,
        image("art/plate.jpg", width: 4.0in, height: 5.333in))))),
  title-y: 0.85in,
  seal: press-seal,
  title: [The Surest Way],
  tail: [of Thriving],
  subtitle: [That What Is Given to the Poor Is No Loss],
  author: [Thomas Gouge],
  spine-title: [The Surest Way of Thriving],
  spine-author: [Gouge],
  pages: 100,
  ink: ink,
  accent: gold,
  label: gold,
  paper: rgb("#1E2215"),
  epigraph: [
    This may seem a paradox to many uncharitable men, that giving should be the
    surest way of getting, and that the more liberal any man is, the more likely
    he is to thrive and prosper in the world.
  ],
  epigraph-source: [The Surest and Safest Way of Thriving],
)
