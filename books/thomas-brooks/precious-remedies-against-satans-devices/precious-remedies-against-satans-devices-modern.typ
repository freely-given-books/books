// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as precious-remedies-against-satans-devices.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *

#show outline: set text(10pt)

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
  title: [Precious Remedies Against Satan’s Devices],
  subtitle: [Or, salve for believers’ and unbelievers’ sores \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Thomas Brooks",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    Set from Thomas Brooks’s _Precious Remedies against Satans Devices_ (second edition, 1653), in modern English.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Put on the full armor of God, so that you#super[+] can stand against the wiles of the devil._

        — Ephesians 6:11
      ]
      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks a plural “you” (the older “ye”), once in a sentence; a plain “you” is singular or general.]
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

#include "chapters/modern/dedication.typ"

// its closing (salutation and name) would stand alone on the next page: its letter spacing a little tighter brings it back (print_check's page warning)
#[
  #set text(tracking: -0.02em)
  #include "chapters/modern/to-the-reader.typ"
]

#include "chapters/modern/introduction.typ"

= Part I. Devices to Draw the Soul into Sin

#include "chapters/modern/sin-01.typ"

#include "chapters/modern/sin-02.typ"

#include "chapters/modern/sin-03.typ"

#include "chapters/modern/sin-04.typ"

#include "chapters/modern/sin-05.typ"

#include "chapters/modern/sin-06.typ"

#include "chapters/modern/sin-07.typ"

#include "chapters/modern/sin-08.typ"

#include "chapters/modern/sin-09.typ"

#include "chapters/modern/sin-10.typ"

#include "chapters/modern/sin-11.typ"

#include "chapters/modern/sin-12.typ"

= Part II. Devices to Keep Souls from Holy Duties

#include "chapters/modern/duties-01.typ"

#include "chapters/modern/duties-02.typ"

#include "chapters/modern/duties-03.typ"

#include "chapters/modern/duties-04.typ"

#include "chapters/modern/duties-05.typ"

#include "chapters/modern/duties-06.typ"

#include "chapters/modern/duties-07.typ"

#include "chapters/modern/duties-08.typ"

= Part III. Devices to Keep Souls Doubting

#include "chapters/modern/doubting-01.typ"

#include "chapters/modern/doubting-02.typ"

#include "chapters/modern/doubting-03.typ"

#include "chapters/modern/doubting-04.typ"

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/doubting-05.typ"
]

#include "chapters/modern/doubting-06.typ"

#include "chapters/modern/doubting-07.typ"

#include "chapters/modern/doubting-08.typ"

= Part IV. Devices to Destroy All Ranks of Men

#include "chapters/modern/ranks-01.typ"

#include "chapters/modern/ranks-02.typ"

#include "chapters/modern/ranks-03.typ"

#include "chapters/modern/ranks-04.typ"

#include "chapters/modern/ranks-05.typ"

#include "chapters/modern/propositions.typ"

#include "chapters/modern/reasons.typ"

#include "chapters/modern/use.typ"

= Appendix. Five More Devices to Keep Souls from Christ

#include "chapters/modern/appendix-01.typ"

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/appendix-02.typ"
]

#include "chapters/modern/appendix-03.typ"

#include "chapters/modern/appendix-04.typ"

#include "chapters/modern/appendix-05.typ"
