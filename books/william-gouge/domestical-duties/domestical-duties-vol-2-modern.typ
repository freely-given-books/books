// The Modern English edition of volume 2 (MODERN-ENGLISH-RULES.md): the same book as
// domestical-duties-vol-2.typ, its text from chapters/modern/vol-2, paragraph for paragraph
// with chapters/typ/vol-2. Terms as source/modern-glossary.md.
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
  subtitle: [Volume II — The Second, Third and Fourth Treatises: Of Husband and Wife \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "William Gouge",
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.0in),
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    The Modern English edition of William Gouge's _Of Domesticall Dvties_ (London, printed by John Haviland for William Bladen, 1622): his words in modern English, paragraph for paragraph with the Classic edition, nothing left out. The text is the Text Creation Partnership transcription of the first edition (EEBO-TCP A68107).

    This is volume 2 of four. The complete work is in eight treatises: I, an exposition of Ephesians 5:21–6:9; II, of husband and wife; III, of wives; IV, of husbands; V, of children; VI, of parents; VII, of servants; VIII, of masters.
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

#metadata[Seeking Marriage] <short>
#metadata((part: [The Second Treatise, Part I: Of Husband and Wife], sections: [§§. 1–13])) <kicker>
#include "chapters/modern/vol-2/01-seeking-marriage.typ"

#metadata[Getting Married] <short>
#metadata((part: [The Second Treatise, Part I: Of Husband and Wife], sections: [§§. 14–28])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: 0.005em)
  #include "chapters/modern/vol-2/02-getting-married.typ"
]

#metadata[Marital Unity and Sexual Faithfulness] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 1–9])) <kicker>
#include "chapters/modern/vol-2/03-marital-unity-and-sexual-faithfulness.typ"

#metadata[Living Together in Love] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 10–17])) <kicker>
#include "chapters/modern/vol-2/04-living-together-in-love.typ"

#metadata[Caring for Each Other’s Souls] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 18–28])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/vol-2/05-caring-for-each-others-souls.typ"
]

#metadata[Guarding Each Other’s Health, Reputation, and Property] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 29–39])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.015em)
  #include "chapters/modern/vol-2/06-guarding-each-others-health-reputation-and-property.typ"
]

#metadata[Serving Together in Family Ministry] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 40–45])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: 0.0025em)
  #include "chapters/modern/vol-2/07-serving-together-in-family-ministry.typ"
]

#metadata[A Wife’s Respect for Her Husband] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 1–16])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: 0.0025em)
  #include "chapters/modern/vol-2/08-a-wifes-respect-for-her-husband.typ"
]

#metadata[A Wife’s Not Going Against Her Husband’s Will (I)] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 17–32])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/vol-2/09-a-wifes-not-going-against-her-husbands-will-i.typ"
]

#metadata[A Wife’s Not Going Against Her Husband’s Will (II)] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 33–42])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: 0.0025em)
  #include "chapters/modern/vol-2/10-a-wifes-not-going-against-her-husbands-will-ii.typ"
]

#metadata[A Wife’s Active Obedience to Her Husband] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 43–50])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/vol-2/11-a-wifes-active-obedience-to-her-husband.typ"
]

#metadata[A Wife’s Submission to Christ First] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 51–74])) <kicker>
#include "chapters/modern/vol-2/12-a-wifes-submission-to-christ-first.typ"

#metadata[A Husband’s Affectionate Authority over His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 1–12])) <kicker>
#include "chapters/modern/vol-2/13-a-husbands-affectionate-authority-over-his-wife.typ"

#metadata[A Husband’s Humble Gentleness to His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 13–23])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.005em)
  #include "chapters/modern/vol-2/14-a-husbands-humble-gentleness-to-his-wife.typ"
]

#metadata[A Husband’s Patient Correcting of His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 24–39])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.0125em)
  #include "chapters/modern/vol-2/15-a-husbands-patient-correcting-of-his-wife.typ"
]

#metadata[A Husband’s Kind Conduct toward His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 40–46])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/vol-2/16-a-husbands-kind-conduct-toward-his-wife.typ"
]

#metadata[A Husband’s Providing for His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 46–60])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.02em)
  #include "chapters/modern/vol-2/17-a-husbands-providing-for-his-wife.typ"
]

#metadata[A Husband’s Sincere and Steady Love for His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 61–76])) <kicker>
// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.005em)
  #include "chapters/modern/vol-2/18-a-husbands-sincere-and-steady-love-for-his-wife.typ"
]
