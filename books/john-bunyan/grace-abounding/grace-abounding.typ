#import "@local/fgbooks:0.5.4": *

#show: book.with(
  title: [Grace Abounding to the Chief of Sinners],
  subtitle: [Or, a Brief Relation of the Exceeding Mercy of God in Christ, to His Poor Servant John Bunyan],
  author: "John Bunyan",
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
        _Come and hear, all ye that fear God, and I will declare what he hath done for my soul._

        — Psalm 66:16
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

#metadata[A Preface] <short>
#include "chapters/typ/preface.typ"

#include "chapters/typ/relation.typ"

#metadata[The Author’s Call to the Ministry] <short>
#include "chapters/typ/call-to-the-ministry.typ"

#metadata[The Author’s Imprisonment] <short>
#include "chapters/typ/imprisonment.typ"

#include "chapters/typ/conclusion.typ"
