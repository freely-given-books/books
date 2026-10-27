#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.2": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ), on a wine ground that warms behind the art: the
// cup of the marriage feast in a wreath of vine and grapes. Drawn as vector
// (art/chalice.svg, made with the cover art's script,
// common-weal-press/sources/vector-art), so it prints sharp. The back keeps
// Wisdom's feast, Proverbs 9.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#plate-cover(
  ground: ((rgb("#6A2140"), 0%), (rgb("#4A142C"), 100%)),
  front-ground: gradient.radial(center: (50%, 30%), radius: 70%,
    rgb("#8A2F55"), rgb("#6A2140"), rgb("#4A142C")),
  art: box(width: 5.5in, height: 8.5in,
    place(center + top, dy: 0.72in, image("art/chalice.svg", width: 3.35in))),
  title-y: 4.55in,
  seal: press-seal,
  title: [The Glorious],
  tail: [Feast of the Gospel],
  subtitle: [The Marriage Feast Between Christ and His Church],
  author: [Richard Sibbes],
  spine-title: [The Glorious Feast of the Gospel],
  spine-author: [Sibbes],
  title-size: 26pt,
  pages: 166,
  ink: rgb("#F8E6EC"),
  accent: rgb("#E7AFC2"),
  label: rgb("#4A142C"),
  paper: rgb("#F8E6EC"),
  epigraph: [
    Wisdom has built her house; she has carved out her seven pillars. She has
    prepared her meat and mixed her wine; she has also set her table. She has
    sent out her maidservants; she calls out from the heights of the city.
    “Whoever is simple, let him turn in here!” she says to him who lacks
    judgment. “Come, eat my bread and drink the wine I have mixed.”
  ],
  epigraph-source: [Proverbs 9:1–5],
  // isbn: "978-0-000000-00-0",
)
