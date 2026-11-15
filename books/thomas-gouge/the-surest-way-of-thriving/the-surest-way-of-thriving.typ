#import "@local/fgbooks:0.15.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [The Surest and Safest Way of Thriving],
  subtitle: [A Conviction of That Grand Mistake in Many, That What Is Given to the Poor Is a Loss to Their Estate],
  author: "Thomas Gouge",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _He that hath pity on the poor, lendeth unto the Lord; and that which he hath given will he pay him again._

        — Proverbs 19:17
      ]
    ]
  ],
  page-margin: (top: 0.9in, bottom: 0.6in, outside: 0.6in, inside: 0.625in),   // Lulu: 61-150 pages
)

// the outline: every level full width, each numbered point marked by its level
#show: outline-marks

// a touch looser or closer where a chapter would end with its last two to four lines alone on a
// page (./fgb pdf page checks)

#include "chapters/typ/ch01-the-text-opened.typ"
#include "chapters/typ/ch02-the-least-of-his-saints.typ"
#[
  #set text(tracking: 0.015em)
  #include "chapters/typ/ch03-the-main-point.typ"
]
#[
  #set text(tracking: 0.01em)
  #include "chapters/typ/ch04-proofs-from-scripture.typ"
]
#include "chapters/typ/ch05-testimonies.typ"
#include "chapters/typ/ch06-examples.typ"
#include "chapters/typ/ch07-examples-of-our-time.typ"
#include "chapters/typ/ch08-the-reasons.typ"
#include "chapters/typ/ch09-reproof.typ"
#[
  #set text(tracking: -0.01em)
  #include "chapters/typ/ch10-exhortation.typ"
]
#include "chapters/typ/ch11-directions.typ"
#include "chapters/typ/ch12-means.typ"
#include "chapters/typ/ch13-ministers.typ"
#include "chapters/typ/ch14-application.typ"
