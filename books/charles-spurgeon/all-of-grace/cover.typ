#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.1": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The plate is the book's own opening picture: "A
// certain man placed a fountain by the wayside, and he hung up a cup near to
// it by a little chain" (chapter 1), an engraving made for this edition,
// printed in the book's deep blue (art/plate.png, the paper cut away so the
// ground shows through). The back is Spurgeon's own word on it.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#let sky = ((rgb("#A6C9E0"), 0%), (rgb("#D9E9F3"), 38%), (rgb("#C3DAEA"), 70%), (rgb("#A9C9DF"), 100%))

#plate-cover(
  plate: read("art/plate.png", encoding: none),
  plate-at: (dx: -0.165in, dy: -0.125in, width: 5.83in, height: 8.75in),
  ground: sky,
  seal: press-seal,
  title: [All of Grace],
  subtitle: [An Earnest Word with Those Who Are Seeking Salvation \ by the Lord Jesus Christ],
  author: [C. H. Spurgeon],
  spine-title: [All of Grace],
  spine-author: [Spurgeon],
  title-size: 36pt,
  pages: 140,
  ink: rgb("#123049"),
  accent: rgb("#24557C"),
  label: rgb("#E7F0F6"),
  paper: rgb("#173A57"),
  epigraph: [
    Here is my fountain, and here is my cup: find fault if you please; but do
    drink of the water of life. I only care for this.
  ],
  epigraph-source: [All of Grace, chapter 1],
  // Uncomment once the book has an ISBN; this puts the white field the printer
  // drops the barcode into on the back cover.
  // isbn: "978-0-000000-00-0",
)
