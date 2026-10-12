#import "@local/fgbooks:0.6.1": *

#show: book.with(
  title: [The Crook in the Lot],
  subtitle: [Or, The Sovereignty and Wisdom of God Displayed in the Afflictions of Men, together with a Christian Deportment under Them],
  author: "Thomas Boston",
  publishing-info: [
    This copy is provided to you free of charge under the Creative Commons CC0 1.0 Universal license.

    https://creativecommons.org/publicdomain/zero/1.0/

    #image("lcc_standard_pd.png", width: 50%)

    Freely you have received; freely give. - Matthew 10:8b

    To get more free ebooks or at-cost printed copies, visit:

    https://books.freely.giving

    Printed books are at the cost of the printing, no revenue or
    royalty is made from printings so you can get ahold of
    physical prints at the lowest cost possible.

    Book formatted by Courtney Allen Hicks

    #link("mailto:books@lyndnex.com")

    ebook and PDF also available.

    The text is that of Samuel M’Millan’s edition of Boston’s Whole Works (Aberdeen, 1848), transcribed from the printed page. The titles of the three parts are this edition’s.
  ],
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Consider the work of God: for who can make that straight, which he hath made crooked?_

        — Ecclesiastes 7:13
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
)

#include "chapters/typ/to-the-reader.typ"

#include "chapters/typ/part-1.typ"

#include "chapters/typ/part-2.typ"

#include "chapters/typ/part-3.typ"
