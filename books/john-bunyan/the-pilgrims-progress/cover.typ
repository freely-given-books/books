#import "../../../scripts/plate_cover.typ": *
#import "@local/fgbooks:0.13.3": press-seal

// Full-wrap paperback cover in the Common Weal Press plate design (see
// scripts/plate_cover.typ). The plate is the book's opening: Christian in
// rags, a book in his hand and a great burden on his back, setting out across
// a wide field toward the wicket-gate and the shining light Evangelist points
// him to ("Keep that light in your eye"). An engraving made for this edition,
// hand-tinted: art/plate.jpg. The back carries the close of the Author's
// Apology, Bunyan's own invitation to the reader.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and with --input front-only=true renders the front alone (the ebook cover);
// `pages` here is only for compiling the cover by itself.
#plate-cover(
  plate: read("art/plate.jpg", encoding: none),
  // enlarged, some sky cut away and slid left, so Christian stands clear of
  // the press's seal and the path runs from his feet to the gate
  plate-at: (dx: -0.85in, dy: -0.9in, width: 6.35in, height: 9.525in),
  seal: press-seal,
  title: [The Pilgrim’s],
  tail: [Progress],
  subtitle: [From This World to That Which Is to Come; \ Delivered under the Similitude of a Dream],
  author: [John Bunyan],
  spine-title: [The Pilgrim’s Progress],
  spine-author: [Bunyan],
  pages: 357,
  ink: rgb("#1E3524"),
  accent: rgb("#7E6220"),
  label: rgb("#1E3524"),
  paper: rgb("#F0E6CC"),
  epigraph: [
    Would'st thou be in a dream, and yet not sleep? \
    Or would'st thou in a moment laugh and weep? \
    Would'st thou lose thyself and catch no harm, \
    And find thyself again without a charm? \
    Would'st read thyself, and read thou know'st not what, \
    And yet know whether thou art blest or not, \
    By reading the same lines? O then come hither, \
    And lay my book, thy head, and heart together.
  ],
  epigraph-source: [The Author’s Apology for his Book],
  // Uncomment once the book has an ISBN; this puts the white field the printer
  // drops the barcode into on the back cover.
  // isbn: "978-0-000000-00-0",
)
