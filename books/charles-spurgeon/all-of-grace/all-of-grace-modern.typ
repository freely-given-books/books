// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as all-of-grace.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
  title: [All of Grace],
  subtitle: [#text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Charles Spurgeon",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 16pt)[“Where sin increased, grace increased all the more.” - Romans 5:20]

      #v(2em)
      #text(size: 8pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own \ Bible where his argument rests on its wording; capitals for God in quotations \ (He, His) follow the BSB. “You#super[+]” marks a plural “you” (the older “ye”), \ once in a sentence; a plain “you” is singular or general.]
    ]
  ]
)

#include "chapters/modern/chapter-01.typ"

#include "chapters/modern/chapter-02.typ"

#include "chapters/modern/chapter-03.typ"

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

#include "chapters/modern/chapter-17.typ"

#include "chapters/modern/chapter-18.typ"

#include "chapters/modern/chapter-19.typ"

#include "chapters/modern/chapter-20.typ"
