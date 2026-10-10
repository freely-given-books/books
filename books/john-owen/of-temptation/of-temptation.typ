#import "@local/fgbooks:0.5.5": *

#show: book.with(
  title: [Of Temptation],
  subtitle: [The Nature and Power of It; the Danger of Entering into It; and the Means of Preventing That Danger: with a Resolution of Sundry Cases Thereunto Belonging],
  author: "John Owen",
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
  ],
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Watch and pray, that ye enter not into temptation: the spirit indeed is willing, but the flesh is weak._

        — Matthew 26:41
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

#include "chapters/typ/to-the-reader.typ"

#include "chapters/typ/chapter-01.typ"

#include "chapters/typ/chapter-02.typ"

#include "chapters/typ/chapter-03.typ"

#include "chapters/typ/chapter-04.typ"

#include "chapters/typ/chapter-05.typ"

#include "chapters/typ/chapter-06.typ"

#include "chapters/typ/chapter-07.typ"

#include "chapters/typ/chapter-08.typ"

#include "chapters/typ/chapter-09.typ"
