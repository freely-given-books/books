// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as the-surest-way-of-thriving.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.15.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [The Surest and Safest Way of Thriving],
  subtitle: [A Conviction of That Grand Mistake in Many, That What Is Given to the Poor Is a Loss to Their Estate \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Thomas Gouge",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Kindness to the poor is a loan to the LORD, and He will repay the lender._

        — Proverbs 19:17
      ]
      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks a plural “you” (the older “ye”), once in a sentence; a plain “you” is singular or general.]
    ]
  ],
  page-margin: (top: 0.9in, bottom: 0.6in, outside: 0.6in, inside: 0.625in),   // Lulu: 61-150 pages
)

// the outline: every level full width, each numbered point marked by its level
#show: outline-marks

// a touch looser or closer where a chapter would end with its last two to four lines alone on a
// page (./fgb pdf page checks)

#include "chapters/modern/ch01-the-text-opened.typ"
#include "chapters/modern/ch02-the-least-of-his-saints.typ"
#[
  #set text(tracking: 0.015em)
  #include "chapters/modern/ch03-the-main-point.typ"
]
#[
  #set text(tracking: 0.01em)
  #include "chapters/modern/ch04-proofs-from-scripture.typ"
]
#include "chapters/modern/ch05-testimonies.typ"
#include "chapters/modern/ch06-examples.typ"
#include "chapters/modern/ch07-examples-of-our-time.typ"
#include "chapters/modern/ch08-the-reasons.typ"
#include "chapters/modern/ch09-reproof.typ"
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/ch10-exhortation.typ"
]
#include "chapters/modern/ch11-directions.typ"
#include "chapters/modern/ch12-means.typ"
#include "chapters/modern/ch13-ministers.typ"
#include "chapters/modern/ch14-application.typ"
