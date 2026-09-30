#import "helpers.typ": *

#show align: it => html.elem("div", attrs: (style: "text-align: " + repr(it.alignment)))[#it.body]
#show pagebreak: it => context if target() == "html" { } else { it }
#set enum(numbering: n => text(weight: "bold")[#n.])
#set par(first-line-indent: 0pt)

#text(size: 24pt, weight: "bold")[The 1689 Baptist Confession of Faith]

With Catechisms

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

= The Baptist Confession

#include "chapters/typ/preface.typ"

#lbcf-all-chapters()

#include "chapters/typ/ending_statement_and_signatories.typ"

= The Baptist Catechism

#bc1695-all-questions()

= An Orthodox Catechism

#include "chapters/typ/aoc_preface.typ"

#aoc1680-all-questions()
