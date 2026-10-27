#import "@local/fgbooks:0.13.3": *

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.7in, inside: 1in),   // Lulu: 151-400 pages; outside 0.7in keeps the
  // signatures of To the Reader on the page with its last paragraph
  title: [The Glorious Feast of the Gospel],
  author: "Richard Sibbes",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page()
)

#include "chapters/typ/tothereader.typ"

#include "chapters/typ/chapter1.typ"

#include "chapters/typ/chapter2.typ"

#include "chapters/typ/chapter3.typ"

#include "chapters/typ/chapter4.typ"

#include "chapters/typ/chapter5.typ"

#include "chapters/typ/chapter6.typ"

#include "chapters/typ/chapter7.typ"

#include "chapters/typ/chapter8.typ"

#include "chapters/typ/chapter9.typ"
