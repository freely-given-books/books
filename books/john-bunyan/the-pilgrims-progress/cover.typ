#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ): a stone ground, an ochre panel, a cream spine.
// The back carries the close of the Author's Apology, Bunyan's own
// invitation to the reader.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and the spine is Lulu's formula (scripts/panel_cover.typ); `pages` here is
// only for compiling the cover by itself.
#panel-cover(
  title: [The Pilgrim's Progress],
  subtitle: [
    From This World to That Which is to Come; \
    Delivered under the Similitude of a Dream
  ],
  author: [John Bunyan],
  pages: 404,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "ochre",
  spine-style: "ruled",
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
  epigraph-source: [— The Author's Apology for his Book],
  // Uncomment once the book has an ISBN; this puts the white field the printer
  // drops the barcode into on the back cover.
  // isbn: "978-0-000000-00-0",
)
