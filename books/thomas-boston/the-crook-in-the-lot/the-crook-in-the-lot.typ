#import "@local/fgbooks:0.13.3": *

#show: book.with(
  title: [The Crook in the Lot],
  subtitle: [Or, The Sovereignty and Wisdom of God Displayed in the Afflictions of Men, together with a Christian Deportment under Them],
  author: "Thomas Boston",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    The text is that of Samuel M’Millan’s edition of Boston’s Whole Works (Aberdeen, 1848), transcribed from the printed page. The titles of the three parts are this edition’s.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Consider the work of God: for who can make that straight, which he hath made crooked?_

        — Ecclesiastes 7:13
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

#include "chapters/typ/to-the-reader.typ"

#include "chapters/typ/part-1.typ"

#include "chapters/typ/part-2.typ"

#include "chapters/typ/part-3.typ"
