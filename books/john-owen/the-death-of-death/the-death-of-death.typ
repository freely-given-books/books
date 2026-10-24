#import "@local/fgbooks:0.13.1": *

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

#include "chapters/typ/epistle-dedicatory.typ"

#include "chapters/typ/attestations.typ"

#include "chapters/typ/to-the-reader.typ"

= Book I

#metadata[Book I, Chapter I] <short>
#include "chapters/typ/book-1/chapter-01.typ"

#metadata[Book I, Chapter II] <short>
#include "chapters/typ/book-1/chapter-02.typ"

#metadata[Book I, Chapter III] <short>
#include "chapters/typ/book-1/chapter-03.typ"

#metadata[Book I, Chapter IV] <short>
#include "chapters/typ/book-1/chapter-04.typ"

#metadata[Book I, Chapter V] <short>
#include "chapters/typ/book-1/chapter-05.typ"

#metadata[Book I, Chapter VI] <short>
#include "chapters/typ/book-1/chapter-06.typ"

#metadata[Book I, Chapter VII] <short>
#include "chapters/typ/book-1/chapter-07.typ"

#metadata[Book I, Chapter VIII] <short>
#include "chapters/typ/book-1/chapter-08.typ"

= Book II

#metadata[Book II, Chapter I] <short>
#include "chapters/typ/book-2/chapter-01.typ"

#metadata[Book II, Chapter II] <short>
#include "chapters/typ/book-2/chapter-02.typ"

#metadata[Book II, Chapter III] <short>
#include "chapters/typ/book-2/chapter-03.typ"

#metadata[Book II, Chapter IV] <short>
#include "chapters/typ/book-2/chapter-04.typ"

#metadata[Book II, Chapter V] <short>
#include "chapters/typ/book-2/chapter-05.typ"

= Book III

#metadata[Book III, Chapter I] <short>
#include "chapters/typ/book-3/chapter-01.typ"

#metadata[Book III, Chapter II] <short>
#include "chapters/typ/book-3/chapter-02.typ"

#metadata[Book III, Chapter III] <short>
#include "chapters/typ/book-3/chapter-03.typ"

#metadata[Book III, Chapter IV] <short>
#include "chapters/typ/book-3/chapter-04.typ"

#metadata[Book III, Chapter V] <short>
#include "chapters/typ/book-3/chapter-05.typ"

#metadata[Book III, Chapter VI] <short>
#include "chapters/typ/book-3/chapter-06.typ"

#metadata[Book III, Chapter VII] <short>
#include "chapters/typ/book-3/chapter-07.typ"

#metadata[Book III, Chapter VIII] <short>
#include "chapters/typ/book-3/chapter-08.typ"

#metadata[Book III, Chapter IX] <short>
#include "chapters/typ/book-3/chapter-09.typ"

#metadata[Book III, Chapter X] <short>
#include "chapters/typ/book-3/chapter-10.typ"

#metadata[Book III, Chapter XI] <short>
#include "chapters/typ/book-3/chapter-11.typ"

= Book IV

#metadata[Book IV, Chapter I] <short>
#include "chapters/typ/book-4/chapter-01.typ"

#metadata[Book IV, Chapter II] <short>
#include "chapters/typ/book-4/chapter-02.typ"

#metadata[Book IV, Chapter III] <short>
#include "chapters/typ/book-4/chapter-03.typ"

#metadata[Book IV, Chapter IV] <short>
#include "chapters/typ/book-4/chapter-04.typ"

#metadata[Book IV, Chapter V] <short>
#include "chapters/typ/book-4/chapter-05.typ"

#metadata[Book IV, Chapter VI] <short>
#include "chapters/typ/book-4/chapter-06.typ"

#metadata[Book IV, Chapter VII] <short>
#include "chapters/typ/book-4/chapter-07.typ"

= Appendices

#metadata[Testimonies of the Ancients] <short>
#include "chapters/typ/appendix-1-testimonies.typ"

#metadata[Appendix on Mr Sprigge] <short>
#include "chapters/typ/appendix-2-sprigge.typ"
