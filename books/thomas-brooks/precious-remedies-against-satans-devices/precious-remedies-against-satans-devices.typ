#import "@local/fgbooks:0.13.1": *

#show outline: set text(10pt)

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
  title: [Precious Remedies Against Satan’s Devices],
  subtitle: [Or, salve for believers’ and unbelievers’ sores],
  author: "Thomas Brooks",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    Set from Thomas Brooks’s _Precious Remedies against Satans Devices_ (second edition, 1653), and lightly modernized.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Put on the whole armour of God, that ye may be able to stand against the wiles of the devil._

        — Ephesians 6:11
      ]
    ]
  ]
)

#set text(font: "Libertinus Serif", size: 11pt)
// Orphans allowed (a paragraph's first line alone at a page's foot): with
// orphan control Typst can push a marker's line onto the next page after
// setting its footnote, so note and marker part. Widows are still avoided.
#set text(costs: (orphan: 0%))
// A note is kept whole on its page, never broken over to the next (a note's
// last words alone at the top of the next page's notes read as a stray).
#show footnote.entry: it => block(breakable: false, it)

#include "chapters/typ/dedication.typ"

#include "chapters/typ/to-the-reader.typ"

#include "chapters/typ/introduction.typ"

= Part I. Devices to Draw the Soul into Sin

#include "chapters/typ/sin-01.typ"

#include "chapters/typ/sin-02.typ"

#include "chapters/typ/sin-03.typ"

#include "chapters/typ/sin-04.typ"

#include "chapters/typ/sin-05.typ"

#include "chapters/typ/sin-06.typ"

#include "chapters/typ/sin-07.typ"

#include "chapters/typ/sin-08.typ"

#include "chapters/typ/sin-09.typ"

#include "chapters/typ/sin-10.typ"

#include "chapters/typ/sin-11.typ"

#include "chapters/typ/sin-12.typ"

= Part II. Devices to Keep Souls from Holy Duties

#include "chapters/typ/duties-01.typ"

#include "chapters/typ/duties-02.typ"

#include "chapters/typ/duties-03.typ"

#include "chapters/typ/duties-04.typ"

#include "chapters/typ/duties-05.typ"

#include "chapters/typ/duties-06.typ"

#include "chapters/typ/duties-07.typ"

#include "chapters/typ/duties-08.typ"

= Part III. Devices to Keep Souls Doubting

#include "chapters/typ/doubting-01.typ"

#include "chapters/typ/doubting-02.typ"

#include "chapters/typ/doubting-03.typ"

#include "chapters/typ/doubting-04.typ"

#include "chapters/typ/doubting-05.typ"

#include "chapters/typ/doubting-06.typ"

#include "chapters/typ/doubting-07.typ"

#include "chapters/typ/doubting-08.typ"

= Part IV. Devices to Destroy All Ranks of Men

#include "chapters/typ/ranks-01.typ"

#include "chapters/typ/ranks-02.typ"

#include "chapters/typ/ranks-03.typ"

#include "chapters/typ/ranks-04.typ"

#include "chapters/typ/ranks-05.typ"

#include "chapters/typ/propositions.typ"

#include "chapters/typ/reasons.typ"

#include "chapters/typ/use.typ"

= Appendix. Five More Devices to Keep Souls from Christ

#include "chapters/typ/appendix-01.typ"

#include "chapters/typ/appendix-02.typ"

#include "chapters/typ/appendix-03.typ"

#include "chapters/typ/appendix-04.typ"

#include "chapters/typ/appendix-05.typ"
