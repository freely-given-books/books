// The Modern English edition of volume 1 (MODERN-ENGLISH-RULES.md): the same book as
// domestical-duties-vol-1.typ, its text from chapters/modern/vol-1, paragraph for paragraph
// with chapters/typ/vol-1. Terms as source/modern-glossary.md.
#import "@local/fgbooks:0.15.0": *
#import "stray-notes.typ": keep-notes, keep-text

// Edited by hand (first written by the earlier converter): a chapter added
// or renamed in source/edition.json needs its #include and <short> lines here.
//
// The imprint's 5.5x8.5 trim (the template's), at 10.5pt: at 290,000 words
// the whole work is four times the length of anything else in the imprint,
// and the smaller type keeps each volume a comfortable thickness.  The
// inside margin follows Lulu's recommendation for a block this thick.

#show outline: set text(9.5pt)

#show: book.with(
  title: [Of Domestical Duties],
  subtitle: [Volume I — The First Treatise: An Exposition of That Part of Scripture Out of Which Domestical Duties Are Raised \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "William Gouge",
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.0in),
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    The Modern English edition of William Gouge's _Of Domesticall Dvties_ (London, printed by John Haviland for William Bladen, 1622): his words in modern English, paragraph for paragraph with the Classic edition, nothing left out. The text is the Text Creation Partnership transcription of the first edition (EEBO-TCP A68107).

    This is volume 1 of four. The complete work is in eight treatises: I, an exposition of Ephesians 5:21–6:9; II, of husband and wife; III, of wives; IV, of husbands; V, of children; VI, of parents; VII, of servants; VIII, of masters.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Submit to one another in the fear of God._

        — Ephesians 5:21
      ]
      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks every plural “you” (the older “ye”); a plain “you” is singular or general.]
    ]
  ]
)

#set text(font: "Libertinus Serif", size: 10.5pt)
// Orphans allowed (a paragraph's first line alone at a page's foot): with
// orphan control Typst can push a marker's line onto the next page after
// setting its footnote, so note and marker part. Widows are still avoided.
#set text(costs: (orphan: 0%))
// A note is kept whole on its page, never broken over to the next (a note's
// last words alone at the top of the next page's notes read as a stray).
#show footnote.entry: it => block(breakable: false, it)
// Notes kept on their marker's page (stray-notes.typ; print_check.py), keyed by the Modern's own note numbers
#show: keep-notes.with(("220": "w", "308": "w", "473": "w", "596": "w", "621": "w", "812": "w", "865": "w", "974": "w",))
// Lists 1622 prints without numbers (a brace's unnumbered branches, "- "
// lines) are set as it prints them: no bullet, set in past a paragraph's
// first-line indent, where the brace puts them.
#set list(marker: [], indent: 2em)

#metadata[The Epistle Dedicatory] <short>
#include "chapters/modern/vol-1/dedication.typ"

#metadata[Serving Each Other in the Fear of the Lord] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 1–6])) <kicker>
#include "chapters/modern/vol-1/01-serving-each-other-in-the-fear-of-the-lord.typ"

#metadata[Particular Callings and the Wife’s Submission] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 7–13])) <kicker>
#include "chapters/modern/vol-1/02-particular-callings-and-the-wifes-submission.typ"

#metadata[Headship in Marriage and the Church] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 14–25])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/vol-1/03-headship-in-marriage-and-the-church.typ"
]

#metadata[Husbands and the Love of Christ] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 26–33])) <kicker>
#include "chapters/modern/vol-1/04-husbands-and-the-love-of-christ.typ"

#metadata[Love That Purifies the Unclean] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 34–47])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.005em)
  #include "chapters/modern/vol-1/05-love-that-purifies-the-unclean.typ"
]

#metadata[Redeemed for Glory] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 48–52])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.005em)
  #include "chapters/modern/vol-1/06-redeemed-for-glory.typ"
]

#metadata[Marital Love and Self-Love] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 53–67])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.005em)
  #include "chapters/modern/vol-1/07-marital-love-and-self-love.typ"
]

#metadata[Christ’s Union with His Beloved Body] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 68–78])) <kicker>
#include "chapters/modern/vol-1/08-christs-union-with-his-beloved-body.typ"

#metadata[The Ancient Law and Unique Bond of Marriage] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 79–89])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.015em)
  #include "chapters/modern/vol-1/09-the-ancient-law-and-unique-bond-of-marriage.typ"
]

#metadata[The Mystery and Practice of Marriage] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 90–95])) <kicker>
#include "chapters/modern/vol-1/10-the-mystery-and-practice-of-marriage.typ"

#metadata[The Child’s Duties to His Parents] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 96–114])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: 0.005em)
  #include "chapters/modern/vol-1/11-the-childs-duties-to-his-parents.typ"
]

#metadata[The Parents’ Duty towards Their Children] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 115–122])) <kicker>
#include "chapters/modern/vol-1/12-the-parents-duty-towards-their-children.typ"
