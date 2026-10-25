#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in Owen's slate. The back carries Owen's
// dilemma to the Universalists, from Book I, chapter III.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and the spine is Lulu's formula (scripts/panel_cover.typ); `pages` here is
// only for compiling the cover by itself.
#panel-cover(
  title: [The Death of Death \ in the Death of Christ],
  subtitle: [
    A Treatise of the Redemption and Reconciliation \
    That Is in the Blood of Christ
  ],
  author: [John Owen],
  pages: 484,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "slate",
  spine-style: "ruled",
  epigraph: [
    God imposed his wrath due unto, and Christ underwent the pains of hell
    for, either all the sins of all men, or all the sins of some men, or some
    sins of all men.
  ],
  epigraph-source: [— From Book I, Chapter III],
)
