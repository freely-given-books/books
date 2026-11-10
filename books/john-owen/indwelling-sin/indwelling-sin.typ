#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [Indwelling Sin],
  subtitle: [The Nature, Power, Deceit, and Prevalency of the Remainders of Indwelling Sin in Believers],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _O wretched man that I am! who shall deliver me from the body of this death? I thank God through Jesus Christ our Lord._

        — Romans 7:24-25
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
)

// Owen's summary under each chapter's title (the TEI's <argument>, the book's only
// inset block): a line's space before the chapter's first paragraph.
#show block: it => if it.inset == (left: 1em, right: 1em) { block(below: 1.6em, it) } else { it }

#include "chapters/typ/preface.typ"

// chapter 1's last lines would stand alone on the next page: its letter spacing a
// little tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "chapters/typ/chapter-01.typ"
]

// chapter 2's last lines would stand alone on the next page: its letter spacing a
// little tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.02em)
  #include "chapters/typ/chapter-02.typ"
]

// chapter 3's last lines would stand alone on the next page: its letter spacing a
// little tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "chapters/typ/chapter-03.typ"
]

#include "chapters/typ/chapter-04.typ"

#include "chapters/typ/chapter-05.typ"

#include "chapters/typ/chapter-06.typ"

#include "chapters/typ/chapter-07.typ"

#include "chapters/typ/chapter-08.typ"

#include "chapters/typ/chapter-09.typ"

#include "chapters/typ/chapter-10.typ"

#include "chapters/typ/chapter-11.typ"

// chapter 12's last lines would stand alone on the next page: its letter spacing a
// little tighter brings them back (print_check's page warning)
#[
  #set text(tracking: -0.02em)
  #include "chapters/typ/chapter-12.typ"
]

#include "chapters/typ/chapter-13.typ"

#include "chapters/typ/chapter-14.typ"

#include "chapters/typ/chapter-15.typ"

#include "chapters/typ/chapter-16.typ"

#include "chapters/typ/chapter-17.typ"
