#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in Boston's heather. The back carries the book's
// first doctrine, from Part I.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and the spine is Lulu's formula (scripts/panel_cover.typ); `pages` here is
// only for compiling the cover by itself.
#panel-cover(
  title: [The Crook in the Lot],
  subtitle: [
    The Sovereignty and Wisdom of God \
    Displayed in the Afflictions of Men
  ],
  author: [Thomas Boston],
  pages: 160,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "heather",
  spine-style: "ruled",
  epigraph: [
    Whatsoever crook is in one's lot, it is of God's making.
  ],
  epigraph-source: [— From Part I],
)
