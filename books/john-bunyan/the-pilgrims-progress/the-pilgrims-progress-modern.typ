// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as the-pilgrims-progress.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *



#show: book.with(
  title: [The Pilgrim's Progress],
  subtitle: [#text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "John Bunyan",
  // the Common Weal Press publisher's page, from the template
  // the publisher's page carries the Modern English front note (the Classic has no epigraph page to put it on)
  publishing-info: publisher-page(note: [Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks a plural “you” (the older “ye”), once in a sentence; a plain “you” is singular or general.]),
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
#include "chapters/modern/apology.typ"

= PART ONE

#include "chapters/modern/part-1/stage-01.typ"

#include "chapters/modern/part-1/stage-02.typ"

#include "chapters/modern/part-1/stage-03.typ"

#include "chapters/modern/part-1/stage-04.typ"

#include "chapters/modern/part-1/stage-05.typ"

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/part-1/stage-06.typ"
]

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/part-1/stage-07.typ"
]

#include "chapters/modern/part-1/stage-08.typ"

#include "chapters/modern/part-1/stage-09.typ"

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/part-1/stage-10.typ"
]

#include "chapters/modern/part-1/conclusion.typ"

= PART TWO

// Part Two's title page, set as Part One's preface page is
#page(header: none)[#align(center + horizon)[#include "chapters/modern/part-2/title.typ"]]

#include "chapters/modern/part-2/authors-way.typ"

#include "chapters/modern/part-2/to-the-reader.typ"

#include "chapters/modern/part-2/stage-01.typ"

#include "chapters/modern/part-2/stage-02.typ"

#include "chapters/modern/part-2/stage-03.typ"

// the virginals footnote would fall on the page before its marker: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.015em)
  #include "chapters/modern/part-2/stage-04.typ"
]

#include "chapters/modern/part-2/stage-05.typ"

#include "chapters/modern/part-2/stage-06.typ"

#include "chapters/modern/part-2/stage-07.typ"

#include "chapters/modern/part-2/stage-08.typ"
