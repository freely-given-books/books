#import "@local/fgbooks:0.5.4": *

#show: book.with(
  title: [The Gospel Minister’s Maintenance Vindicated],
  subtitle: [Wherein a Regular Ministry in the Churches Is First Asserted, and the Objections Against a Gospel Maintenance for Ministers Answered],
  author: "Benjamin Keach",
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
        _Even so hath the Lord ordained that they which preach the gospel should live of the gospel._

        — 1 Corinthians 9:14
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

#include "chapters/typ/foreword.typ"

#include "chapters/typ/recommendation.typ"

#include "chapters/typ/chapter-01.typ"

#metadata[The Minister’s Maintenance Vindicated] <short>
#include "chapters/typ/chapter-02.typ"

#metadata[Motives to Press the Duty] <short>
#include "chapters/typ/chapter-03.typ"

#metadata[The Work of a Gospel Minister] <short>
#include "chapters/typ/chapter-04.typ"
