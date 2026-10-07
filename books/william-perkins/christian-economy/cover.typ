#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design: a warm
// ground, a panel of colour on the front, a cream spine.  The Secret Key of
// Heaven and The Glorious Feast of the Gospel are the same design in sage and
// in sky blue; the sand ground and mulberry panel are Perkins's, and so is
// the ruled spine -- the other two set their titles plain.  The spine itself
// is left the colour of the wrap on purpose: a fold that comes off the press
// crooked would otherwise carry a stripe of spine colour onto a cover.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and the spine is Lulu's formula (scripts/panel_cover.typ); `pages` here is
// only for compiling the cover by itself.  Everything else on the wrap
// follows from them.
#panel-cover(
  title: [Christian Economy],
  subtitle: [
    Or, A Short Survey of the Right Manner of Erecting
    and Ordering a Family, According to the Scriptures
  ],
  author: [William Perkins],
  pages: 124,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "mulberry",
  spine-style: "ruled",
  epigraph: [
    "And if it seem evil unto you to serve the LORD, choose you this day whom
    ye will serve… but as for me and my house, we will serve the LORD."
  ],
  epigraph-source: [— Joshua 24:15],
  // Uncomment once the book has an ISBN; this puts the white field the printer
  // drops the barcode into on the back cover.
  // isbn: "978-0-000000-00-0",
)
