#import "@local/fgbooks:0.14.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

// Owen on Sin: a print volume of two of the books, Of Temptation (1658) and The
// Mortification of Sin (1656), as the 1855 Presbyterian Board reprint paired them
// (Temptation first, the editor's order). Each work is its own book, with its own
// TEI, ebook and sign-off; this file only sets their chapters in one paperback, each
// work after a part page. Indwelling Sin prints alone.
#show: book.with(
  title: [Owen on Sin],
  subtitle: [Of Temptation \ The Mortification of Sin],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Watch and pray, that ye enter not into temptation: the spirit indeed is willing, but the flesh is weak._

        — Matthew 26:41

        #v(2em)

        _For if ye live after the flesh, ye shall die: but if ye through the Spirit do mortify the deeds of the body, ye shall live._

        — Romans 8:13
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
)

// the outline: every level full width, each numbered point marked by its level and given
// a little space (scripts/outline_marks.typ; the editor's choice, 2026-11-09)
#show: outline-marks

// Owen's summary under each chapter's title (the TEI's <argument>, each book's only
// inset block): a line's space before the chapter's first paragraph.
#show block: it => if it.inset == (left: 1em, right: 1em) { block(below: 1.6em, it) } else { it }

= Of Temptation

// its last lines would stand alone on the next page: its letter spacing a little
// tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.02em)
  #include "../of-temptation/chapters/typ/to-the-reader.typ"
]
#include "../of-temptation/chapters/typ/chapter-01.typ"
#include "../of-temptation/chapters/typ/chapter-02.typ"
#include "../of-temptation/chapters/typ/chapter-03.typ"
#include "../of-temptation/chapters/typ/chapter-04.typ"
// its last lines would stand alone on the next page: its letter spacing a little
// tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.02em)
  #include "../of-temptation/chapters/typ/chapter-05.typ"
]
#include "../of-temptation/chapters/typ/chapter-06.typ"
#include "../of-temptation/chapters/typ/chapter-07.typ"
#include "../of-temptation/chapters/typ/chapter-08.typ"
#include "../of-temptation/chapters/typ/chapter-09.typ"

= The Mortification of Sin

#include "../the-mortification-of-sin/chapters/typ/preface.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-01.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-02.typ"
// its last lines would stand alone on the next page: its letter spacing a little
// tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "../the-mortification-of-sin/chapters/typ/chapter-03.typ"
]
#include "../the-mortification-of-sin/chapters/typ/chapter-04.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-05.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-06.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-07.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-08.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-09.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-10.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-11.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-12.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-13.typ"
#include "../the-mortification-of-sin/chapters/typ/chapter-14.typ"
