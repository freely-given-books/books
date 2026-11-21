#import "@local/fgbooks:0.14.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

// Owen on Sin in Modern English: the same print volume as owen-on-sin.typ (Of Temptation,
// then The Mortification of Sin, each after a part page), its text the two books' Modern
// English editions (chapters/modern), unchanged here (MODERN-ENGLISH-RULES.md).
#show: book.with(
  title: [Owen on Sin],
  subtitle: [Of Temptation \ The Mortification of Sin \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Watch and pray so that you#super[+] will not enter into temptation. For the spirit is willing, but the body is weak._

        — Matthew 26:41

        #v(2em)

        _For if you#super[+] live according to the flesh, you#super[+] will die; but if by the Spirit you#super[+] put to death the deeds of the body, you#super[+] will live._

        — Romans 8:13
      ]
      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks every plural “you” (the older “ye”); a plain “you” is singular or general.]
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
  #include "../of-temptation/chapters/modern/to-the-reader.typ"
]
#include "../of-temptation/chapters/modern/chapter-01.typ"
#include "../of-temptation/chapters/modern/chapter-02.typ"
#include "../of-temptation/chapters/modern/chapter-03.typ"
#include "../of-temptation/chapters/modern/chapter-04.typ"
// its last lines would stand alone on the next page: its letter spacing a little
// tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.005em)
  #include "../of-temptation/chapters/modern/chapter-05.typ"
]
#include "../of-temptation/chapters/modern/chapter-06.typ"
#include "../of-temptation/chapters/modern/chapter-07.typ"
#include "../of-temptation/chapters/modern/chapter-08.typ"
#include "../of-temptation/chapters/modern/chapter-09.typ"

= The Mortification of Sin

#include "../the-mortification-of-sin/chapters/modern/preface.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-01.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-02.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-03.typ"
// its last lines would stand alone on the next page: its letter spacing a little
// tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.015em)
  #include "../the-mortification-of-sin/chapters/modern/chapter-04.typ"
]
// its last lines would stand alone on the next page: its letter spacing a little
// tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "../the-mortification-of-sin/chapters/modern/chapter-05.typ"
]
#include "../the-mortification-of-sin/chapters/modern/chapter-06.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-07.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-08.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-09.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-10.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-11.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-12.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-13.typ"
#include "../the-mortification-of-sin/chapters/modern/chapter-14.typ"
