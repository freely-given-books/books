#import "@local/fgbooks:0.14.0": *

// One volume, 484 pages at 10.5pt (the editor's decision, 2026-10-23: Book IV
// answers Books I-III point by point, so the book is not split).

#show: book.with(
  title: [The Death of Death in the Death of Christ],
  subtitle: [A Treatise of the Redemption and Reconciliation That Is in the Blood of Christ, with the Merit Thereof, and the Satisfaction Wrought Thereby],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.125in),   // Lulu: 401-600 pages
)

#set text(font: "Libertinus Serif", size: 10.5pt)

// Owen's title for each chapter, the line under "Chapter I" (the TEI's
// <argument>, the book's only inset paragraph): set as the chapter's title,
// centred and larger, not as a paragraph. The running head and the contents
// take the short name in the <short> metadata before each chapter.
#show block: it => if it.inset == (left: 1em, right: 1em) {
  set par(justify: false, first-line-indent: 0pt)
  align(center, block(width: 88%, above: 0pt, below: 2.2em,
    text(13pt, style: "italic", hyphenate: false, it.body)))
} else { it }

#metadata[The Epistle Dedicatory] <short>
#include "chapters/typ/epistle-dedicatory.typ"

#metadata[Two Attestations] <short>
#include "chapters/typ/attestations.typ"

#metadata[To the Reader] <short>
#include "chapters/typ/to-the-reader.typ"

= Book I

#metadata[The End of the Death of Christ] <short>
#include "chapters/typ/book-1/chapter-01.typ"

#metadata[The Nature of an End] <short>
#include "chapters/typ/book-1/chapter-02.typ"

#metadata[The Work of the Father] <short>
#include "chapters/typ/book-1/chapter-03.typ"

#metadata[The Work of the Son] <short>
#include "chapters/typ/book-1/chapter-04.typ"

#metadata[The Work of the Holy Spirit] <short>
#include "chapters/typ/book-1/chapter-05.typ"

#metadata[The Means of This Work] <short>
#include "chapters/typ/book-1/chapter-06.typ"

#metadata[Oblation and Intercession One] <short>
#include "chapters/typ/book-1/chapter-07.typ"

#metadata[Objections Answered] <short>
#include "chapters/typ/book-1/chapter-08.typ"

= Book II

#metadata[Previous Considerations] <short>
#include "chapters/typ/book-2/chapter-01.typ"

#metadata[False Ends Removed] <short>
#include "chapters/typ/book-2/chapter-02.typ"

#metadata[The Immediate End of Christ’s Death] <short>
#include "chapters/typ/book-2/chapter-03.typ"

#metadata[Impetration and Application Distinguished] <short>
#include "chapters/typ/book-2/chapter-04.typ"

#metadata[Application and Impetration] <short>
#include "chapters/typ/book-2/chapter-05.typ"

= Book III

#metadata[Arguments from the New Covenant] <short>
#include "chapters/typ/book-3/chapter-01.typ"

#metadata[Three Other Arguments] <short>
#include "chapters/typ/book-3/chapter-02.typ"

#metadata[From the Person Christ Sustained] <short>
#include "chapters/typ/book-3/chapter-03.typ"

#metadata[Sanctification and Faith] <short>
#include "chapters/typ/book-3/chapter-04.typ"

#metadata[Redemption] <short>
#include "chapters/typ/book-3/chapter-05.typ"

#metadata[Reconciliation] <short>
#include "chapters/typ/book-3/chapter-06.typ"

#metadata[The Satisfaction of Christ] <short>
#include "chapters/typ/book-3/chapter-07.typ"

#metadata[A Digression on Satisfaction] <short>
#include "chapters/typ/book-3/chapter-08.typ"

#metadata[Arguments for Christ’s Satisfaction] <short>
#include "chapters/typ/book-3/chapter-09.typ"

#metadata[The Merit of Christ] <short>
#include "chapters/typ/book-3/chapter-10.typ"

#metadata[The Last General Argument] <short>
#include "chapters/typ/book-3/chapter-11.typ"

= Book IV

#metadata[Things to Be Considered First] <short>
#include "chapters/typ/book-4/chapter-01.typ"

#metadata[Particular Arguments Entered Upon] <short>
#include "chapters/typ/book-4/chapter-02.typ"

#metadata[The Remaining Texts Unfolded] <short>
#include "chapters/typ/book-4/chapter-03.typ"

#metadata[The Second General Argument Answered] <short>
#include "chapters/typ/book-4/chapter-04.typ"

#metadata[The Last Argument from Scripture] <short>
#include "chapters/typ/book-4/chapter-05.typ"

#metadata[“The Universality of God’s Free Grace”] <short>
#include "chapters/typ/book-4/chapter-06.typ"

#metadata[Remaining Objections Removed] <short>
#include "chapters/typ/book-4/chapter-07.typ"

= Appendices

#metadata[Testimonies of the Ancients] <short>
#include "chapters/typ/appendix-1-testimonies.typ"

#metadata[Appendix on Mr Sprigge] <short>
#include "chapters/typ/appendix-2-sprigge.typ"
