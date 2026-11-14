// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as of-temptation.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [Of Temptation],
  subtitle: [The Nature and Power of It; the Danger of Entering into It; and the Means of Preventing That Danger: with a Resolution of Sundry Cases Thereunto Belonging \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Watch and pray so that you#super[+] will not enter into temptation. For the spirit is willing, but the body is weak._

        — Matthew 26:41
      ]
      #v(2em)
      #text(size: 9pt)[In this edition “you#super[+]” marks a plural “you” (the older “ye”); \ a plain “you” is singular or general. \ Capitals for God in quotations (He, His) follow the Berean Standard Bible.]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

// the outline: every level full width, each numbered point marked by its level and given
// a little space (scripts/outline_marks.typ; the editor's choice, 2026-11-09)
#show: outline-marks

// Owen's summary under each chapter's title (the TEI's <argument>, the book's only
// inset block): a line's space before the chapter's first paragraph.
#show block: it => if it.inset == (left: 1em, right: 1em) { block(below: 1.6em, it) } else { it }

#include "chapters/modern/to-the-reader.typ"

// chapter I's last three lines would stand alone on p. 19: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/chapter-01.typ"
]

#include "chapters/modern/chapter-02.typ"

#include "chapters/modern/chapter-03.typ"

#include "chapters/modern/chapter-04.typ"

#include "chapters/modern/chapter-05.typ"

#include "chapters/modern/chapter-06.typ"

#include "chapters/modern/chapter-07.typ"

#include "chapters/modern/chapter-08.typ"

#include "chapters/modern/chapter-09.typ"
