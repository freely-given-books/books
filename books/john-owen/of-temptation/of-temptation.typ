#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [Of Temptation],
  subtitle: [The Nature and Power of It; the Danger of Entering into It; and the Means of Preventing That Danger: with a Resolution of Sundry Cases Thereunto Belonging],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    The text is that of William H. Goold’s edition of Owen’s Works (1850), checked against the first edition of 1658. The summaries at the head of each chapter are Goold’s; Owen’s first edition has none.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Watch and pray, that ye enter not into temptation: the spirit indeed is willing, but the flesh is weak._

        — Matthew 26:41
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

#include "chapters/typ/to-the-reader.typ"

#include "chapters/typ/chapter-01.typ"

#include "chapters/typ/chapter-02.typ"

#include "chapters/typ/chapter-03.typ"

#include "chapters/typ/chapter-04.typ"

#include "chapters/typ/chapter-05.typ"

#include "chapters/typ/chapter-06.typ"

#include "chapters/typ/chapter-07.typ"

#include "chapters/typ/chapter-08.typ"

#include "chapters/typ/chapter-09.typ"
