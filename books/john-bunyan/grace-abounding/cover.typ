#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in Bunyan's ochre. The back carries Bunyan's own
// word on how he wrote the book, from his preface.
//
// ./fgb build gives the cover its compiled interior's page count and trim,
// and the spine is Lulu's formula (scripts/panel_cover.typ); `pages` here is
// only for compiling the cover by itself.
#panel-cover(
  title: [Grace Abounding to the Chief of Sinners],
  subtitle: [
    Or, a Brief Relation of the Exceeding Mercy of God in Christ, \
    to His Poor Servant John Bunyan
  ],
  author: [John Bunyan],
  pages: 144,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "ochre",
  spine-style: "ruled",
  epigraph: [
    I could also have stepped into a style much higher than this in which I
    have here discoursed, and could have adorned all things more than here I
    have seemed to do, but I dare not. God did not play in convincing of me,
    the devil did not play in tempting of me, neither did I play when I sunk
    as into a bottomless pit, when the pangs of hell caught hold upon me;
    wherefore I may not play in my relating of them, but be plain and simple,
    and lay down the thing as it was.
  ],
  epigraph-source: [— From the Preface],
)
