#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in Owen's slate. The back carries the book's
// thesis, from chapter III.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and the spine is Lulu's formula (scripts/panel_cover.typ); `pages` here is
// only for compiling the cover by itself.
#panel-cover(
  title: [Of Temptation],
  subtitle: [
    The Nature and Power of It; the Danger of \
    Entering into It; and the Means of Preventing That Danger
  ],
  author: [John Owen],
  pages: 140,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "slate",
  spine-style: "ruled",
  epigraph: [
    It is the great duty of all believers to use all diligence in the ways
    of Christ's appointment, that they fall not into temptation.
  ],
  epigraph-source: [— From Chapter III],
)
