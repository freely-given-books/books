#import "@local/fgbooks:0.5.3": *

#show outline: set text(9.5pt)

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
  title: [Christian Economy],
  subtitle: [Or, a short survey of the right manner of erecting and ordering a family, according to the Scriptures],
  author: "William Perkins",
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

    Set from William Perkins’s _Christian Oeconomie_ (1609), translated out of
    the Latin by Thomas Pickering, with the spelling modernized.

    Book formatted by Courtney Allen Hicks

    #link("mailto:books@lyndnex.com")

    ebook and PDF also available.

  ],
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _And if it seem evil unto you to serve the LORD, choose you this day whom ye will serve… but as for me and my house, we will serve the LORD._

        — Joshua 24:15
      ]
    ]
  ]
)

#set text(font: "Liberation Serif", size: 11pt)

#include "chapters/typ/dedication.typ"

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
