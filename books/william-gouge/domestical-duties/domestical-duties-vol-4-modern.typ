// The Modern English edition of volume 4 (MODERN-ENGLISH-RULES.md): the same book as
// domestical-duties-vol-4.typ, its text from chapters/modern/vol-4, paragraph for paragraph
// with chapters/typ/vol-4. Terms as source/modern-glossary.md.
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
  subtitle: [Volume IV — The Seventh and Eighth Treatises: Of Servants and Masters \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "William Gouge",
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.0in),
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    The Modern English edition of William Gouge's _Of Domesticall Dvties_ (London, printed by John Haviland for William Bladen, 1622): his words in modern English, paragraph for paragraph with the Classic edition, nothing left out. The text is the Text Creation Partnership transcription of the first edition (EEBO-TCP A68107).

    This is volume 4 of four. The complete work is in eight treatises: I, an exposition of Ephesians 5:21–6:9; II, of husband and wife; III, of wives; IV, of husbands; V, of children; VI, of parents; VII, of servants; VIII, of masters.
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
// Lists 1622 prints without numbers (a brace's unnumbered branches, "- "
// lines) are set as it prints them: no bullet, set in past a paragraph's
// first-line indent, where the brace puts them.
#set list(marker: [], indent: 2em)
// Notes kept on their marker's page (stray-notes.typ; print_check.py), keyed by the Modern's own note numbers:
// none yet (set after the first build of the Modern)

#metadata[Servants and Masters in the Apostle’s Words] <short>
#metadata((part: [The First Treatise: On Ephesians 5:21–6:9], sections: [§§. 123–133])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.0025em)
  #include "chapters/modern/vol-4/01-servants-and-masters-in-the-apostles-words.typ"
]

#metadata[A Servant’s Reverence for His Master] <short>
#metadata((part: [The Seventh Treatise: Of Servants], sections: [§§. 1–9])) <kicker>
#include "chapters/modern/vol-4/02-a-servants-reverence-for-his-master.typ"

#metadata[A Servant’s Obedience to His Master] <short>
#metadata((part: [The Seventh Treatise: Of Servants], sections: [§§. 10–19])) <kicker>
#include "chapters/modern/vol-4/03-a-servants-obedience-to-his-master.typ"

#metadata[A Servant’s Faithful and Willing Service] <short>
#metadata((part: [The Seventh Treatise: Of Servants], sections: [§§. 20–34])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: 0.004em)
  #include "chapters/modern/vol-4/04-a-servants-faithful-and-willing-service.typ"
]

#metadata[A Servant’s Duty and Its Limits under God] <short>
#metadata((part: [The Seventh Treatise: Of Servants], sections: [§§. 35–43])) <kicker>
#include "chapters/modern/vol-4/05-a-servants-duty-and-its-limits-under-god.typ"

#metadata[A Master’s Authority Rightly Maintained] <short>
#metadata((part: [The Eighth Treatise: Of Masters], sections: [§§. 1–12])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: 0.005em)
  #include "chapters/modern/vol-4/06-a-masters-authority-rightly-maintained.typ"
]

#metadata[A Master’s Correcting and Governing of His Household] <short>
#metadata((part: [The Eighth Treatise: Of Masters], sections: [§§. 13–20])) <kicker>
#include "chapters/modern/vol-4/07-a-masters-correcting-and-governing-of-his-household.typ"

#metadata[A Master’s Care for His Servants’ Souls and Bodies] <short>
#metadata((part: [The Eighth Treatise: Of Masters], sections: [§§. 21–34])) <kicker>
#include "chapters/modern/vol-4/08-a-masters-care-for-his-servants-souls-and-bodies.typ"

#metadata[A Master’s Employing and Rewarding of His Servants] <short>
#metadata((part: [The Eighth Treatise: Of Masters], sections: [§§. 35–45])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.0025em)
  #include "chapters/modern/vol-4/09-a-masters-employing-and-rewarding-of-his-servants.typ"
]

#metadata[A Master’s Own Master in Heaven] <short>
#metadata((part: [The Eighth Treatise: Of Masters], sections: [§§. 46–49])) <kicker>
#include "chapters/modern/vol-4/10-a-masters-own-master-in-heaven.typ"

