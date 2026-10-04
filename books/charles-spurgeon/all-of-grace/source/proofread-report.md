# All of Grace: proofreading report

A full read of `chapters/typ`. All twenty chapters were read for sense, start
to finish. The base text is CCEL's ThML (`grace.thml.xml`). The second
witness is Monergism's 2015 PDF, which follows CCEL's text. It was compared
from a copy kept outside the repository, never committed. Scripture was
checked against the KJV. CCEL has no page images, so where CCEL and
Monergism agree on an error, a fix rests on sense (marked *sense*).

## Needs your decision

**Decided 2026-10-03 and applied** (synced, check OK, rebuilt: 135 pages, epubcheck
clean): 1–4 as recommended ("I tell you, you cannot go to hell"; "think of it
as if"; "made a sin-offering"; "thy cause to plead, / Nor doubt"); 5 kept as
printed; 6 marks dropped in the four block quotations; 7 "plow"; 8 left as CCEL
has it; 9 set as an ordinary paragraph.

1. **Chapter 5, a word an earlier editor dropped.** The edition reads "If you
   believe on Him, I tell you cannot go to hell". CCEL and Monergism both
   read "I tell you you cannot go to hell". The old copy dropped the second
   "you", probably as a doubled word, and that is recorded as an `#editor`
   emendation. Without it the sentence does not parse.
   *Recommend:* restore it with a comma: "I tell you, you cannot go to hell".
2. **Chapter 7, a missing "it".** "Never make a Christ out of your faith, nor
   think of as if it were the independent source of your salvation." CCEL
   and Monergism read the same. The sentence needs an object.
   *Recommend:* "nor think of it as if it were" (*sense*).
3. **Chapter 8, "being made of a sin-offering".** "The Scriptures speak of
   Jesus Christ … as being made of a sin-offering on our behalf". CCEL and
   Monergism read the same. The phrase echoes 2 Cor. 5:21 ("made him to be
   sin for us").
   *Recommend:* "as being made a sin-offering" (*sense*). Keeping it as
   printed is also defensible.
4. **Chapter 14, the hymn "He ever lives to intercede".** CCEL and Monergism
   read "Give Him, my soul, Thy cause to plead, / No doubt the Father's
   grace." In Wesley's stanza the line is addressed to the soul: "Give Him,
   my soul, thy cause to plead, / Nor doubt the Father's grace."
   *Recommend:* "thy" (lowercase) and "Nor doubt".
5. **Chapter 18, "the life implanted as the new birth".** "the life
   implanted as the new birth comes of a living and incorruptible seed".
   CCEL and Monergism read the same.
   *Recommend:* keep it. "at the new birth" may be what was meant, but the
   printed words can be read as they stand.
6. **Quotation marks inside block quotations.** The template sets `#quote`
   as an indented block with no marks, and 21 of the 25 block quotations
   have none. Four keep CCEL's marks: chapter 5 (Rom. 3:21-26), chapter 7
   ("By grace are ye saved, through faith"), chapter 16 (Acts 5:31) and
   chapter 19 ("Who shall separate us…").
   *Recommend:* drop the marks in those four, so every block looks the same.
7. **"plough" in an American-spelling edition.** The edition already
   Americanizes Saviour, offence, endeavour, marvellous, axe, counsellor
   and fulfilment. Chapter 15 still has "two handles of the same plough".
   *Recommend:* "plow", to match. "Good-by" (chapter 9) is the period
   American form and can stay.
8. **Capitals and other variants that CCEL itself mixes.** These were left
   as CCEL has them. Normalize only if you want to:
   - heaven 11 / Heaven 17
   - hell 8 / Hell 3
   - devil 6 / Devil 2
   - for ever 5 / forever 5 (the KJV quotations use "for ever")
   - every one 2 / everyone 2
   - fountain-head / fountainhead (both in chapter 7)
   - evangelists / Evangelists
   - covenant head / Covenant Head
   - he, him and his for God and Christ: mostly capitalized, but lowercase
     in many places, e.g. "he justifieth the ungodly" (ch. 3), "If he does
     not confirm us" (ch. 17), "Has he called us?" (ch. 19)

   *Recommend:* leave pronouns and the KJV's "for ever" alone. If you want
   tidiness, make Heaven and Hell uppercase only where they are named as
   places in Spurgeon's own sentences.
9. **Chapter 9, a sentence set as a block quotation.** "The faith which saves
   has its analogies in the human frame." CCEL opens a `<blockquote>` with
   it and runs the next paragraph on inside, and the edition kept it as a
   `#quote`. It reads as Spurgeon's own topic sentence, not a quotation.
   *Recommend:* set it as an ordinary paragraph. Keeping CCEL's layout is
   harmless.

## Fixed

All of these are in CCEL, and Monergism agrees with CCEL unless stated.

### Misprints and letter slips

| ch. | was | now | evidence |
| --- | --- | --- | --- |
| 1 | the critic himself might fill the cup, and *he* refreshed | *be* refreshed | Monergism (the README said this was fixed already; it was not) |
| 11 | how to perform that which *l* would I find not | *I* | Rom. 7:18 |
| 9 | TO MAKE THE MATTER *Of* faith | *of* | the opening capitals ran one word too far |
| 12 | "Well, *Sir*," replied the foreman | *sir* | case |

### Quotation marks

- Chapter 8: "The water that I shall give him … springing up into everlasting
  life, it must be true" had no closing mark. It is now closed after "life,".
- Chapter 13: the chapter opened `YE MUST BE BORN AGAIN.”` with no opening
  mark. It now has one.
- Chapter 18: "that we may be preserved, blameless unto the day of our Lord
  Jesus Christ.”" had a closing mark only. It now opens before "blameless",
  the word the next sentence discusses ("The revised version has
  'unreproveable,' instead of 'blameless.'").
- Chapter 11: "‘Twas for the sinful Thou didst die" had its apostrophe curled
  the wrong way. It is now "’Twas".
- Chapters 15 and 19: there was a stray space after the opening mark in
  “ BY GRACE ARE YE SAVED.” and “ ALL OF GRACE.” (an earlier spacing
  decision). It is removed.

### Punctuation

- Chapter 11: "in this case, The witness of God must be true" is now "in
  this case. The witness".
- Chapter 11: "Oh, sir my want of strength" is now "Oh, sir, my want",
  matching "Oh, sir, my weakness" later in the chapter.
- Chapter 9: "Will not my reader put his trust in God in Christ Jesus." now
  ends with "?".
- Chapter 6: "and will give an heart of flesh. (Ezekiel 11:19)." is now
  "flesh (Ezekiel 11:19).", like every other reference in the book.
- Chapter 16 (Hone's verses): "Is quell’d my Lord, by Thee" is now "Is
  quell’d, my Lord, by Thee", with the comma before the address.
- Chapter 3: "Come for this great mercy of God is meant for such as you are"
  is now "Come, for this great mercy…". Without the comma the sentence
  first reads as "come for this mercy".

## Checked and kept

- The earlier editor's corrections of CCEL were checked and kept:
  "everlasting" (ch. 8), "worldly" (ch. 11), "nutrition" (ch. 13), "it
  would forgive" (ch. 6) and "God in human flesh" (ch. 8, CCEL "is").
  Monergism still has "wordly", "mutrition" and "is" (so does the PDF text
  `slips.py` read), so the README overstates what Monergism corrects.
- Spurgeon's free quotations of scripture and hymns are kept as printed. For
  example, "None of the men of strength have found their hands" (Ps. 76:5,
  KJV "might"), "principalities and power", the Ezekiel 11:19 wording, and
  "Bold shall I stand" printed slightly differently in chapters 4 and 18.
- Hymns run together in one block, as the README describes. The verses with
  line breaks in chapters 14, 15 and 16 render the same way, because Typst
  joins the lines.
- "Our Lord Jesus Christ, who shall also confirm you" (ch. 17) quotes from
  the end of 1 Cor. 1:7 into 1:8–9. "His Son" (ch. 19) against "his Son"
  (ch. 17) is CCEL's own.
- Period words and usages are kept: justifieth, doth, hath, "a deal more",
  deshabille, Koh-i-noors, "Good-by", "the Negro", "the African", Hottentot,
  "Plastic Pliable", "Hell Gate and Heaven Gate".
- "Romans 8:33" under the chapter 4 heading is CCEL's text line.
- The centred appeals in chapter 20 (`#align(center)`) are layout and are
  not in the TEI. This is a known difference in `./fgb check`.

## Checklist

- [x] `sweep.py`: 2 hits (stray spaces after an opening quote). Both fixed;
  it now finds none.
- [x] `slips.py` against Monergism: 44 places. 41 are the edition's recorded
  American spellings and emendations. The other three are "be"/"he"
  (fixed) and the chapter 5 "you" (question 1).
- [x] `refs.py --quotes`: 12 references, 0 missing, 0 weak quote matches.
  References use the full book name, chapter:verse, in parentheses
  throughout.
- [x] `./fgb check`: OK. The rebuild matches, the reg extraction matches 19/20
  (chapter 20 differs only by the `#align` layout), the TEI is valid and the
  book compiles.
- [x] `./fgb build`: 135 pages, Lulu margins OK, epubcheck 0 errors and 0
  warnings.
- [x] PDF text: no wrongly curled quotes, no stray markup, no doubled words.
- [ ] Shelf ready once questions 1–4 are answered. 1 and 2 leave sentences
  that do not parse, and 4 is a misquoted hymn. 5–9 are optional.
