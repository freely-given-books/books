#import "@local/fgbooks:0.13.1": *

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
  title: [All of Grace],
  author: "Charles Spurgeon",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 16pt)[“Where sin abounded, grace did much more abound.” - Romans 5:20]
    ]
  ]
)

#include "chapters/typ/chapter-01.typ"

#include "chapters/typ/chapter-02.typ"

#include "chapters/typ/chapter-03.typ"

#include "chapters/typ/chapter-04.typ"

#include "chapters/typ/chapter-05.typ"

#include "chapters/typ/chapter-06.typ"

#include "chapters/typ/chapter-07.typ"

#include "chapters/typ/chapter-08.typ"

#include "chapters/typ/chapter-09.typ"

#include "chapters/typ/chapter-10.typ"

#include "chapters/typ/chapter-11.typ"

#include "chapters/typ/chapter-12.typ"

#include "chapters/typ/chapter-13.typ"

#include "chapters/typ/chapter-14.typ"

#include "chapters/typ/chapter-15.typ"

#include "chapters/typ/chapter-16.typ"

#include "chapters/typ/chapter-17.typ"

#include "chapters/typ/chapter-18.typ"

#include "chapters/typ/chapter-19.typ"

#include "chapters/typ/chapter-20.typ"
