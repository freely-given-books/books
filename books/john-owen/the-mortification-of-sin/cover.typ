#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in Owen's slate. The back carries the book's
// best-known sentence, from chapter II.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and the spine is Lulu's formula (scripts/panel_cover.typ); `pages` here is
// only for compiling the cover by itself.
#panel-cover(
  title: [The Mortification of Sin],
  subtitle: [
    Of the Mortification of Sin in Believers: \
    the Necessity, Nature, and Means of It
  ],
  author: [John Owen],
  pages: 140,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "slate",
  spine-style: "ruled",
  epigraph: [
    Do you mortify; do you make it your daily work; be always at it whilst
    you live; cease not a day from this work; be killing sin or it will be
    killing you.
  ],
  epigraph-source: [— From Chapter II],
)
