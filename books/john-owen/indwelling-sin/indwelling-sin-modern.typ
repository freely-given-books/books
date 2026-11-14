// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as indwelling-sin.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [Indwelling Sin],
  subtitle: [The Nature, Power, Deceit, and Prevalency of the Remainders of Indwelling Sin in Believers \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _What a wretched man I am! Who will rescue me from this body of death? Thanks be to God, through Jesus Christ our Lord!_

        — Romans 7:24-25
      ]
      #v(2em)
      #text(size: 9pt)[In this edition “you#super[+]” marks a plural “you” (the older “ye”); \ a plain “you” is singular or general. \ Capitals for God in quotations (He, His) follow the Berean Standard Bible.]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
)

// Owen's summary under each chapter's title (the TEI's <argument>, the book's only
// inset block): a line's space before the chapter's first paragraph.
#show block: it => if it.inset == (left: 1em, right: 1em) { block(below: 1.6em, it) } else { it }

// the outline: every level full width, each numbered point marked by its level
// (scripts/outline_marks.typ: 1. (1.) [1.] before Owen's First, Secondly)
#show: outline-marks

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.015em)
  #include "chapters/modern/preface.typ"
]

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/chapter-01.typ"
]

#include "chapters/modern/chapter-02.typ"

#include "chapters/modern/chapter-03.typ"

#include "chapters/modern/chapter-04.typ"

#include "chapters/modern/chapter-05.typ"

#include "chapters/modern/chapter-06.typ"

#include "chapters/modern/chapter-07.typ"

#include "chapters/modern/chapter-08.typ"

#include "chapters/modern/chapter-09.typ"

#include "chapters/modern/chapter-10.typ"

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.015em)
  #include "chapters/modern/chapter-11.typ"
]

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/chapter-12.typ"
]

#include "chapters/modern/chapter-13.typ"

#include "chapters/modern/chapter-14.typ"

#include "chapters/modern/chapter-15.typ"

#include "chapters/modern/chapter-16.typ"

#include "chapters/modern/chapter-17.typ"
