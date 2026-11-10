#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [Of Temptation],
  subtitle: [The Nature and Power of It; the Danger of Entering into It; and the Means of Preventing That Danger: with a Resolution of Sundry Cases Thereunto Belonging],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
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

// Owen's summary under each chapter's title (the TEI's <argument>, the book's only
// inset block): a line's space before the chapter's first paragraph.
#show block: it => if it.inset == (left: 1em, right: 1em) { block(below: 1.6em, it) } else { it }

#include "chapters/typ/to-the-reader.typ"

#include "chapters/typ/chapter-01.typ"

#include "chapters/typ/chapter-02.typ"

#include "chapters/typ/chapter-03.typ"

#include "chapters/typ/chapter-04.typ"

#include "chapters/typ/chapter-05.typ"

#include "chapters/typ/chapter-06.typ"

// chapter VII's last two lines would stand alone on p. 82: its letter spacing
// a little tighter brings them back to p. 81 (the next chapter opens on p. 83 either way)
#[
  #set text(tracking: -0.01em)
  #include "chapters/typ/chapter-07.typ"
]

#include "chapters/typ/chapter-08.typ"

#include "chapters/typ/chapter-09.typ"
