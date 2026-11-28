// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as the-crook-in-the-lot.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [The Crook in the Lot],
  subtitle: [Or, The Sovereignty and Wisdom of God Displayed in the Afflictions of Men, together with a Christian Deportment under Them \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Thomas Boston",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    The text is that of Samuel M’Millan’s edition of Boston’s Whole Works (Aberdeen, 1848), transcribed from the printed page. The titles of the three parts are this edition’s.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Consider the work of God: who can make straight what He has made crooked?_

        — Ecclesiastes 7:13
      ]
      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks every plural “you” (the older “ye”); a plain “you” is singular or general.]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

#include "chapters/modern/to-the-reader.typ"

// page fit: the chapter would end on a few lines alone; its letter spacing set so it falls well (page-fit skill)
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/part-1.typ"
]

#include "chapters/modern/part-2.typ"

#include "chapters/modern/part-3.typ"
