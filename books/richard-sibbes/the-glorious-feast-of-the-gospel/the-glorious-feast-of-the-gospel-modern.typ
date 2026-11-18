// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as the-glorious-feast-of-the-gospel.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.7in, inside: 1in),   // Lulu: 151-400 pages; outside 0.7in keeps the
  // signatures of To the Reader on the page with its last paragraph
  title: [The Glorious Feast of the Gospel],
  subtitle: [#text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Richard Sibbes",
  // the Common Weal Press publisher's page, from the template
  // the publisher's page carries the Modern English front note (the Classic has no epigraph page to put it on)
  publishing-info: publisher-page(note: [Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks a plural “you” (the older “ye”), once in a sentence; a plain “you” is singular or general.]),
)

// the signatures would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/tothereader.typ"
]

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/chapter1.typ"
]

#include "chapters/modern/chapter2.typ"

#include "chapters/modern/chapter3.typ"

#include "chapters/modern/chapter4.typ"

#include "chapters/modern/chapter5.typ"

// its last lines would stand alone on the next page: its letter spacing a little tighter brings them back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/chapter6.typ"
]

#include "chapters/modern/chapter7.typ"

#include "chapters/modern/chapter8.typ"

#include "chapters/modern/chapter9.typ"
