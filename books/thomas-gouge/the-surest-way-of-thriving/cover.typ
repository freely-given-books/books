#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.15.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), type only, as Owen's and Edwards's: the 1673 title page's
// own verse, Prov 19:17, with "lendeth unto the Lord" in gold. The back gives Gouge's
// paradox in his words (chapter 3). The ground's colour is a placeholder until the
// editor chooses one (EDITION-RULES 7); dark olive, after his father's Domestical Duties.
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
  art: box(width: 5.5in, height: 8.5in, {
    let plain(body) = text(font: DISPLAY, size: 15pt, tracking: 0.12em,
      fill: color.mix((ink, 65%), (ground, 35%)), body)
    let gilt(body) = text(font: DISPLAY, weight: "bold", size: 22pt,
      tracking: 0.14em, fill: gold, body)
    place(dx: 0.5in, dy: 3.4in, box(width: 4.5in, {
      set align(center)
      set par(leading: 0.55em, spacing: 0pt)
      plain[He that hath pity]
      v(0.08in)
      plain[on the poor]
      v(0.1in)
      gilt[lendeth unto the Lord.]
      v(0.2in)
      caps([Proverbs xix. 17], 9pt, color.mix((gold, 80%), (ground, 20%)), tracking: 0.25em)
    }))
  }),
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
