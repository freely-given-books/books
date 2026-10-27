#import "@local/fgbooks:0.13.2": *



#show: book.with(
  title: [The Pilgrim's Progress],
  author: "John Bunyan",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      From This World to That Which is to Come;
      
      Delivered under the Similitude of a Dream
      
      by John Bunyan
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),
)

#set text(font: "Libertinus Serif", size: 10.5pt)
#include "chapters/typ/apology.typ"

= PART ONE

#include "chapters/typ/part-1/stage-01.typ"

#include "chapters/typ/part-1/stage-02.typ"

#include "chapters/typ/part-1/stage-03.typ"

#include "chapters/typ/part-1/stage-04.typ"

#include "chapters/typ/part-1/stage-05.typ"

#include "chapters/typ/part-1/stage-06.typ"

#include "chapters/typ/part-1/stage-07.typ"

#include "chapters/typ/part-1/stage-08.typ"

#include "chapters/typ/part-1/stage-09.typ"

#include "chapters/typ/part-1/stage-10.typ"

#include "chapters/typ/part-1/conclusion.typ"

= PART TWO

// Part Two's title page, set as Part One's preface page is
#page(header: none)[#align(center + horizon)[#include "chapters/typ/part-2/title.typ"]]

#include "chapters/typ/part-2/authors-way.typ"

#include "chapters/typ/part-2/to-the-reader.typ"

#include "chapters/typ/part-2/stage-01.typ"

#include "chapters/typ/part-2/stage-02.typ"

#include "chapters/typ/part-2/stage-03.typ"

#include "chapters/typ/part-2/stage-04.typ"

#include "chapters/typ/part-2/stage-05.typ"

#include "chapters/typ/part-2/stage-06.typ"

#include "chapters/typ/part-2/stage-07.typ"

#include "chapters/typ/part-2/stage-08.typ"
