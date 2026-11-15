#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.15.0": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The picture is Edwards' own figure for the whole
// treatise (Part II, xii): blossoms in the spring, many of which fall, and the
// fruit by which we must judge. ChatGPT engraving, its fruit redrawn as young apples
// (fgbooks-generated-art "Religious Affections (blossom bough, apples)"),
// hand-tinted by art/tint.py into art/plate.jpg (the editor, 2026-11-15). The bough
// stands 0.78in clear of the spine fold, so a cover trimmed a little crooked loses
// nothing (the editor); its branch runs off the outer edge, the petals fall clear
// of the seal.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let paper = rgb(245, 241, 230)              // the plate's own paper

#plate-cover(
  plate: read("art/plate.jpg", encoding: none),
  plate-at: (dx: 0.7in, dy: 0.42in, width: 5.5in, height: 8.25in),
  ground: paper,
  // the book's 6 x 9in trim as the default too (./fgb build passes it for the print
  // cover, but the ebook's front is rendered without it)
  trim-width: 6in,
  trim-height: 9in,
  title-y: 0.85in,
  seal: press-seal,
  title: [Religious Affections],
  subtitle: [A Treatise Concerning Religious Affections, in Three Parts],
  author: [Jonathan Edwards],
  spine-title: [Religious Affections],
  spine-author: [Edwards],
  pages: 426,
  ink: rgb("#3B3330"),
  accent: rgb("#9A5B54"),
  label: rgb("#4E5B3A"),
  paper: paper,
  epigraph: [
    ’Tis the mature fruit which comes afterwards, and not the beautiful colors
    and smell of the blossom, that we must judge by.
  ],
  epigraph-source: [Part II],
)
