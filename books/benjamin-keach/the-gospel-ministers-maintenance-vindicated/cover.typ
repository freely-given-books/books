#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in Keach's midnight navy. The back carries a passage
// from the last part of the treatise.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and the spine is Lulu's formula (scripts/panel_cover.typ); `pages` here is
// only for compiling the cover by itself.
#panel-cover(
  title: [The Gospel Minister’s Maintenance Vindicated],
  subtitle: [
    Wherein a Regular Ministry in the Churches Is First Asserted, \
    and the Objections Against a Gospel Maintenance for Ministers Answered
  ],
  author: [Benjamin Keach],
  pages: 86,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "midnight",
  spine-style: "ruled",
  epigraph: [
    If one soul be worth more than all the world, how great is the charge of
    Christ’s ministers, that have many souls committed to their care and trust?
  ],
  epigraph-source: [— The Great and Weighty Work of a True Gospel Minister],
)
