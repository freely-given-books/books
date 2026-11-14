// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as a-divine-cordial.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *
#import "../../../scripts/outline_marks.typ": outline-marks
#import "stray-notes.typ": keep-text

#show: book.with(
  title: [A Divine Cordial],
  subtitle: [Or, the Transcendent Privilege of Those That Love God and Are Savingly Called \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Thomas Watson",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _As for you, what you#super[+] intended against me for evil, God intended for good._

        — Genesis 50:20
      ]
      #v(2em)
      #text(size: 9pt)[In this edition “you#super[+]” marks a plural “you” (the older “ye”); \ a plain “you” is singular or general. \ Capitals for God in quotations (He, His) follow the Berean Standard Bible.]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
)

// the outline: every level full width, each numbered point marked by its level and given
// a little space (scripts/outline_marks.typ; the editor's choice, 2026-11-09)
#show: outline-marks


#include "chapters/modern/to-the-reader.typ"

#include "chapters/modern/chapter-01.typ"

// its letter spacing a little tighter keeps its notes on their markers' pages and its last lines
// off a page of their own (print_check)
#[
  #set text(tracking: -0.02em)
  #include "chapters/modern/chapter-02.typ"
]
// (its note 12, long, is set on the page after its marker at any spacing: accepted)

// its letter spacing a little tighter keeps its notes on their markers' pages and its last lines
// off a page of their own (print_check)
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/chapter-03.typ"
]

#include "chapters/modern/chapter-04.typ"

#include "chapters/modern/chapter-05.typ"

#include "chapters/modern/chapter-06.typ"

#include "chapters/modern/chapter-07.typ"

#include "chapters/modern/chapter-08.typ"

#include "chapters/modern/chapter-09.typ"

#include "chapters/modern/chapter-10.typ"

#include "chapters/modern/chapter-11.typ"

#include "chapters/modern/chapter-12.typ"

#include "chapters/modern/chapter-13.typ"

#include "chapters/modern/chapter-14.typ"

#include "chapters/modern/chapter-15.typ"

#include "chapters/modern/chapter-16.typ"
