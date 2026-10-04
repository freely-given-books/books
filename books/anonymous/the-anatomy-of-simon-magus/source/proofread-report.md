# The Anatomy of Simon Magus: proofreading report

I read all of `chapters/typ` for sense: the foreword, chapters 1–8 and the
abbreviations guide. I checked it against the 1700 printing, which is the TEI's
printed layer, and against the KJV.

There is no modern witness. The old `.html` and `.xhtml` files in the book folder
are the user's own earlier copy of this same edition, so `slips.py` was not run.

This edition was modernized heavily on purpose (hath → has, thou → you, Holy
Ghost → Holy Spirit, thereof → of that, translations of the Latin added). I kept
all of that.

## Needs your decision

**Decided 2026-10-03 and applied** (synced, check OK 8/8, rebuilt: 124 pages,
epubcheck clean): 1–9 as recommended (both "Holy Ghost" → Holy Spirit; the
README notes the Jehu/Apollos corrections and the restored end of ch. 6);
10: the 46 there-/where- compounds an earlier editor replaced in chapters 1–2
(thereof, therein, whereby, wherein, hereunto, … and "Wherefore") are restored;
the 14 "unto" an earlier editor made "to" in chapters 1–3 (none changed the
meaning) are restored too, so all eight chapters match; 11 "satire"; 12 foreword kept as is; 13 Athalaric /
Pope John II entry corrected, Durandus added and the "Lib. 4. Dist. qu." form
moved to him.

1. **The end of chapter 6 is missing.** The chapter stops mid-sentence: "For
   whatsoever discouragement the sense of his own insufficiency." The 1700 printing
   goes on: "…insufficiency may breed in him, yet the Sincerity of his Intentions,
   and the Evidences of a Call from God, may give him confidence to rely upon his
   Grace, as sufficient for him, whose Strength is made perfect in Weakness."
   *Recommend:* restore it in the edition's style: "For whatsoever discouragement
   the sense of his own insufficiency may breed in him, yet the sincerity of his
   intentions, and the evidences of a call from God, may give him confidence to
   rely upon his grace, as sufficient for him, whose strength is made perfect in
   weakness."
2. **The Hebrew in chapter 2 is typed backwards.** The passage is "(or as it is
   according to the original, יָדמָלֵא, ad Implendum, to fill his hand,)" at
   2 Chron 13:9. The TCP has a gap there, and the editor filled it from the page
   image. But the two words were copied in the order they appear left to right on
   the page, with no space between them, so the edition reads "yad male", "hand
   full". *Recommend:* "מָלֵא יָד" ("fill the hand"), using the same letters and
   points, in logical order with a space. Please check this against the page image
   if you can.
3. **"John the Seer" (chapter 2).** The text reads "as John the Seer said to
   Jehoshaphat, for assisting Ahab, Should you help the ungodly?" The printing
   also says "John", but the seer in 2 Chron 19:2 is Jehu, son of Hanani.
   *Recommend:* "Jehu the seer", and say in the README that this is the author's
   slip, corrected.
4. **"Apollo" (chapter 2).** The text reads "The brethren at Ephesus did recommend
   Apollo by letters", and the printing has "Apollo" too. The KJV has Apollos
   (Acts 18:24-27). *Recommend:* "Apollos".
5. **British spellings in chapters 6–8 only.** Chapters 1–5 use American forms
   (honor, labor, Savior, favor, endeavor, fervor: about 60 words). Chapters 6–8
   use British forms (honour, labour(er)s, Saviour, favour, endeavour(s), fervour,
   humours, harboured, counsellors: about 35 words). *Recommend:* American
   throughout, since it is the majority and the edition's style.
6. **pedler / pedlers / pedlars.** Chapter 3 has "pedler", chapter 4 "pedlers" and
   chapter 8 "pedlars". The printing has "Pedler(s)" everywhere. *Recommend:*
   "peddler(s)", or "pedlar(s)" if you prefer British spelling.
7. **Simoniacs / simoniack / simoniacks.** Chapter 1 has "Simoniacs", chapter 3
   "simoniack", and chapters 4–5 "simoniacks". *Recommend:* "simoniac(s)" in
   lowercase.
8. **"Holy Ghost" is left in twice (chapter 5).** Everywhere else the edition has
   "Holy Spirit". One is in Matt 28:19, "…and of the Holy Ghost", and one is in
   the author's own prose, "for the power of the Holy Ghost to render it
   effectual". *Recommend:* change the prose one to Holy Spirit. Change Matt 28:19
   as well unless the baptismal formula was kept on purpose.
9. **Headings.**
   - Title case: chapter 2 "May be Incurred in the Entrance Upon" → "May Be
     Incurred in the Entrance upon"; chapter 3 "How Simony is Practiced" → "Is";
     chapter 5 "Are to be Reputed" → "to Be"; chapter 6 "Entry Upon" → "upon".
   - The chapter 6 title ends with a full stop and no other title does.
     *Recommend:* drop it.
   - Chapter 4's running head repeats the whole title, "Of the Heinousness of the
     Sin of Simony". The other running heads drop "Of" (chapter 1 is "The Nature
     of Simony"). *Recommend:* "The Heinousness of Simony".
10. **Uneven modernizing between chapters.** Chapter 1 turns thereof/therein into
    "of that" or "in that". The other chapters keep them (about 100 times). "unto"
    is gone from chapters 1–3 but stays in chapters 4–8 (34 times). "shall" stays
    in chapters 6–8 ("then you shall be speechless"). *Recommend:* leave it all, in
    line with the light-edition preference, and make no new grammar changes.
11. **"that old satyr" (chapter 4).** This introduces "Cuncta venalia nobis…"
    (Mantuan). "Satyr" is the old spelling of satire. *Recommend:* "satire".
12. **Foreword (modern matter, so the author's call).**
    - The first footnote reads "See especially 17-20. Also see William Downes
      Willis, Simony, 21-24." The "17-20" names no source.
    - The note marker comes before the full stop ("church office#footnote[…].");
      everywhere else it comes after.
    - The foreword text is in two places: `chapters/typ/foreword.typ` (used by the
      ebook) and the `foreword:` argument in `the-anatomy-of-simon-magus.typ`
      (used by the print book). Any change must be made in both.
    *Recommend:* ask Conley Owens for the source of "17-20".
13. **Abbreviations guide (modern matter).**
    - "Epist. ad Johan. 22." is glossed as a "Letter to Pope John XXII", a
      14th-century pope. The letter is King Athalaric's (d. 534), so the addressee
      is Pope John II (533). The letter is in Cassiodorus, *Variae* 9.15.
    - "Lib. 4. Dist. [N]. qu. [N]." is glossed as Peter Lombard. In chapter 2 it is
      Durandus's commentary on the Sentences ("Durandus is in the right… Lib. 4.
      Dist. 25. qu. 4."); Lombard's Sentences have no questions. Durandus is not
      in the guide.
    *Recommend:* correct both entries and add Durandus of Saint-Pourçain
    (c. 1275–1334), *Commentary on the Sentences*.

## Fixed (44 changes)

### Wording slips (printing or edition)
- Chapter 2: "Athalaricus… having… condemned simony. He also… condemn those" is now
  "…condemned simony, he also… condemns those". The editor had dropped "doth"
  ("He doth also… condemn") and left "condemn".
- Chapter 6: "when the Lord told Ananias that had he called Saul" is now "that he
  had called". This is a transposition in the printing.
- Chapter 8: Cyprian's "pertimiscamus" is now "pertimescamus" (a Latin misprint in
  the printing).
- Chapter 2: "munere á lingua" is now "munere à lingua", the same as "à manu, …
  à lingua" a page earlier.
- Chapter 3: "freely ye have received" is now "freely you have received". It was
  the only "ye" left; the edition writes "Freely you have received" elsewhere.

### Quotations whose capitals the edition had lowercased (restored from the print)
- Chapter 2: "saying, Lay hands suddenly".
- Chapter 6: "Whether you eat", "Who is sufficient", "Not that we are sufficient",
  "None of these things", "Who will go for us?".
- Chapter 7: "Give account of your stewardship", "We have sinned", "What is that
  to us?", "Your money perish with you".
- Chapter 1: "My House… the House of Prayer… my Father's House" is now lowercase,
  because the edition lowercases the printed nouns everywhere else.

### Punctuation
- Chapter 1: "apostle's hands" (Peter and John) is now "apostles' hands", as in
  Acts 8:18. "saying; Give me" now has a comma.
- Fragments created when the edition turned a printed colon into a full stop:
  - Chapter 2: "bought and sold, therefore every gainful transaction…".
  - Chapter 5: "pleaded for re-ordination; and Leo…" (the "howsoever… yet"
    sentence).
  - Chapter 4: "the stones thereof, their houses, I'm sure…" ("if that flying
    roll…").
- Chapter 4: "while he tells him. Your heart" now has a comma, as in the print.
- Chapter 5: the two exclamations are back as printed: "reduced unto upon his
  account!" and "may not easily apprehend!".
- Commas:
  - Added: "if the person is worthy, then" and "acts of discipline, censures".
  - Removed: "would have sold the exercise", and "the resolution whereof depends"
    (the comma made it misread).
- Chapter 5: "forty days' penance" and "yourselves" (the printing has "your
  selves").

### Scripture and other references
- Chapter 5: "Matt. 19:16" is now "Matt. 16:19" (the keys of the kingdom). The
  printing has "Matth. 19.16", which is transposed.
- Chapter 6: "Acts 9:17" is now "Acts 9:15, 16" (the chosen vessel; "I will show
  him how great things he must suffer"). Verse 17 has neither.
- One style throughout: "Act."/"Acts." → "Acts" (5 places), "1 King." → "1 Kings".
  The full stop was added to "Matt. 21:13.", "John 2:16." and "Acts 8:19-23.".
- Patristic notes: "Bernard. Compost in Decret Greg." → "Compost. … Decret.";
  "Caus. 1 Qu. 1." → "Caus. 1. Qu. 1.".

## Checked and kept

- The edition's deliberate modernizations: has/does, you/your, Holy Spirit, "of
  that" for thereof in chapter 1, the bracketed translations of the Latin, notes
  rewritten in modern form, and the editor's one-word glosses in footnotes
  ("extreme poverty", "collusion").
- Period forms the printing has, kept: "in end", "of such one", "notwithstanding
  of", "how soon" (as soon as), "it is like", "of new again", "anti-date", "haply",
  "Whosesoever's sins", "a crime deserving, and laws… for inflicting the highest
  censures".
- "vaenalia" (Mantuan): an attested old spelling of venalia, as printed.
- "Council… holden in Trullus", "five hundred and forty years ago" (Lateran
  under Innocent II), and "about the year 531": the author's own statements.
- "Blessed Spirit" (3 times) and "blessed Spirit" (once): left as they are.
- "You will not muzzle the ox" and "My house will be called": the editor's
  shall → will.
- Sentences the printing also breaks with a full stop, kept: "…glory of God. Much
  more will he…" and "…unto the Lord. It can be no reproach…" (chapter 6).
- The Bonaventure and Gregory notes in chapter 1 are written out in full; the
  rest stay abbreviated, as the editor left them.
- The scripture quotations match the KJV, as modernized by the edition.

## Checklist

- [x] `sweep.py --early`: 163 candidates. All are Latin or period words, or the
  `/ term:` lines of the abbreviations guide. None is an error.
- [x] `slips.py`: not applicable, because there is no modern witness.
- [x] `refs.py --quotes`: 128 references, 0 missing, 0 weak matches.
- [x] `./fgb check`: OK. The rebuild matches, the extraction matches 8/8, the orig
  layer is exact, the TEI is valid and the book compiles.
- [x] `./fgb build`: 124 pages, still the cover's page count. The inside margin is
  0.625in, as Lulu requires, nothing is within 0.5in of the trim, and there were
  no footnote warnings.
- [x] epubcheck: 0 errors and 0 warnings.
- [x] PDF text: no wrongly curled quotes and no stray markup.
- [ ] Shelf ready: **not yet.** The lost end of chapter 6 (question 1) and the
  backwards Hebrew (question 2) need fixing before print. The other questions are
  consistency and accuracy.
