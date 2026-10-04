# Christian Economy: proofreading report

I read all of `chapters/typ` for sense: Pickering's epistle dedicatory and
chapters 1–18. I checked each suspect place against the 1609 printing (TCP
A09377, the TEI's printed layer) and quotations against the KJV. The book has
no modern witness, so `slips.py` was not run. As this book does by design, the
footnotes stay in original spelling.

## Needs your decision

**Decided 2026-10-03 and applied:** 1–4 as recommended (Coloss. 3. 11; "cometh";
KJV names: Hannah, Tamar, Reuben, Vashti, Iscah, Ahasuerus, Ham, Adonijah,
Jezreelitess; honor and labour); 5–9 kept as printed (Perkins's own words);
10 "Bring forth fruit and multiply"; 11 "In fauorem Matrimonij"; 12 "1. King.
1. 5. 6."; 13 done: `build_tei.py` now carries a bullet item the review indents
under another (Laban set under Bethuel, as the 1609 page 29 shows) and a stop
added before a printed numeral that becomes an item (item VII now ends with a
full stop, VIII keeps its label); 14 checked against the 1609 page image
(archive.org `bim_early-english-books-1475-1640_christian-oeconomie-or-_perkins-william_1609_0`,
p. 43): the TCP diagram is right — Isaac's children Esau, Jacob and Joseph,
Jacob's son Joseph joined by a marriage line to Maria, the daughter of Eli
among Samuel's children Aaron, Eli and Levi — and the edition already sets it
so; no change.

1. **Ch. 16, a reference to a chapter that does not exist.** The passage reads:
   "But Christ hath purchased liberty to believers, *Coloss. 5. 11.*" The 1609
   printing has the same reference, but Colossians has only four chapters. The
   next sentence quotes "neither … bond nor free" (Col. 3:11; Gal. 3:28).
   Gal. 5:1, "the liberty wherewith Christ hath made us free", is also
   possible. *Recommend:* **Coloss. 3. 11.**
2. **"commeth" ×3 (ch. 4, ch. 5, ch. 17) against "cometh" ×1 (ch. 9).** The
   machine wrote "cometh". The earlier review changed it back to the old
   spelling "commeth", and the review report records that as a grammar choice.
   *Recommend:* **"cometh"** throughout. It is the KJV form and the spelling
   this book uses everywhere else.
3. **Biblical names not yet in KJV form.** The machine put most names in KJV
   form (Thare → Terah, Nachor → Nahor, Isaak → Isaac, Rahel → Rachel). These
   are still as printed:
   - Anna ×3 (Hannah). Ch. 2 already has "Hannah".
   - Thamar ×2 (Tamar)
   - Ruben (Reuben)
   - Queen Vashi (Vashti)
   - Iischa (Iscah)
   - Ahashuerosh (Ahasuerus)
   - Cham ×2 (Ham)
   - Adoniah (Adonijah)
   - "Ahinoam the Izreelite" (Jezreelitess)

   *Recommend:* **KJV forms**, to match the rest of the book.
4. **honor/honour and labor/labour are mixed.** The book has honor 16 times
   and honour/Honour 4 times (in the dedication, including "Honourable"). It
   has labour 10 times and labor once. *Recommend:* **honor and labour**, the
   majority form of each. The other option is British forms throughout:
   honour, labour, favour and Saviour, which are already the majority for the
   last two.
5. **Ch. 5:** "Kindred in consanguinity, are those which issue from *out*, &
   the same common blood or stock." The 1609 printing has the same words. The
   sense needs "one". *Recommend:* **"from one & the same"**.
6. **Ch. 5:** "Again whole sisters by the same father *or* mother, or half
   sisters by one of them and not by both." The 1609 printing has "or". The
   whole brothers just before are "by the same father and mother", and the
   half sisters are set against these. *Recommend:* **"and"**.
7. **Ch. 7:** a leper is "commanded to lead his life, where he may
   conveniently *from company*". The 1609 printing has the same words, and a
   word seems lost. *Recommend:* **"where he may conveniently be from
   company"**, or leave it as printed.
8. **Ch. 8:** "Those that are at liberty, are tied necessarily to subjection
   in respect of marriage; but the other being still of the family … are bound
   to be ordered, by their parents". The 1609 printing has the same words. The
   "but" contrast, and the whole argument, need a "not". *Recommend:* **"are
   not tied necessarily"**. This would be a real change of wording, so leaving
   it as printed is also defensible.
9. **Ch. 15:** the master is to "yield them sometimes intercession & rest".
   The 1609 printing has the same words. *Recommend:* **"intermission"**,
   meaning a break from work.
10. **Ch. 3, Gen. 1:28:** "Bring forth fruit multiply, fill the earth". The
    1609 printing reads "Bringforth fruit multiply". The Geneva Bible reads
    "Bring forth fruit and multiply". *Recommend:* **add "and"**.
11. **Ch. 4 footnote:** "Jn sauorem Matrimony." The TCP transcribers probably
    misread "In fauorem Matrimonij". *Recommend:* **"In fauorem
    Matrimonij."** The footnote stays in original spelling.
12. **Dedication footnote:** "1. King. 5. 6." is printed against Absalom and
    Adoniah. Adonijah's story is 1 Kings 1:5–6, and "1. King. 1." follows two
    notes later. *Recommend:* **"1. King. 1. 5. 6."**, or keep it as printed.
13. **Ch. 5, two corrections the pipeline cannot store.** Both were tried in
    `chapters/typ`, then undone, because the TEI cannot carry them yet:
    - In the "For example" tree under Terah, Laban is set beside Bethuel. The
      text says Laban is three degrees from Terah, so he belongs one level
      down, under Bethuel. The TEI does not record list nesting, so the sync
      dropped the change.
    - Item VII of the affinity list ends "… or of the woman by another
      husband" with no full stop, as printed. Adding the stop made the aligner
      read it as deleting the next item's numeral "VIII".

    *Recommend:* teach `build_tei.py` both cases, then apply them. Until then
    they stay as printed.
14. **Ch. 5, the second affinity tree (Isaac … Joseph— / Samuel … Maria,
    Levi).** The TCP encoding of the diagram is garbled. It lists a second
    "Joseph" and a "Levi", and the text never mentions either. Fixing it needs
    the page image (`tcp:2719`, around printed p. 38). *Recommend:* look at the
    page image, or leave it as transcribed.

## Fixed

There are about 60 edits in `chapters/typ`, all synced into the TEI.

### Misprints in the 1609 printing (the sense is clear)

| ch. | was | now |
| --- | --- | --- |
| 2 | now the time *or* rest draweth on | *of* |
| 3 | some are general, some are proper general gifts are such | proper*.* General |
| 4 | require mature deliberation*,* Secondly | *.* |
| 5 | termed his daughter Now howsoever | daughter*.* Now |
| 5 | Or at least it *way* be said | *may* |
| 5 | restraineth himself … from *he* occasions | *the* |
| 5 | with the fathers *brother* wife | *brothers* |
| 5 | And contrariwise for example. | contrariwise*.* For example. |
| 8 | in his Tragedy called Andromacha, wherein *in* when | wherein when |
| 8 | the holy hand of *Thesphylus* | *Theophilus* (Nicephorus 14.55) |
| 10 | The Ark, and Israel … dwell *intents* | *in tents* |
| 10 | I will marry *the* unto me in righteousness | *thee* |
| 10 | thy love is better *them* wine | *then* (the book's form of "than") |
| 11 | Shall I follow after this company*,?* | company*?* |
| 13 | the Priest *of* Prince of Midian | *or* |
| 16 | in case of offence, *them* master hath authority | *the* |
| 16 | he that is *bough* with money | *bought* |
| 8 | Gen. 2. 24*,* (end of paragraph) | *.* |

### Errors from the machine pass

- Ch. 2: "On the other*side*" had become "On the *otherwise*". It is now "On the other side".
- Ch. 2: "go finely and *faire* daintily" had become "fair". It is now "fare" (compare Luke 16:19, "fared deliciously").
- Ch. 12: "*bitternes*" had become "bitterns". It is now "bitterness".
- Ch. 14: "thy brethren shall *prayse* thee" had become "prays". It is now "praise".
- Wrong capitals after "&c." mid-sentence: "&c. And not", "By this form", "With intention", "Should be joined", "Yet this is not" and "Resteth" are now lowercase, as in 1609.
- Wrong capitals after references mid-sentence: "chap. 16. Saith", "chap. 9. Requires", "Matth. 19. Speaketh", "Rom. 8. 8. Affirming", "Gen. 2. 22. And 1. 27", "60. Years" and "1000. Shekels".
- Lowercased sentence starts are capitalized again, as in 1609: "Proper gifts", "Marriage is honorable" (twice), "Honor thy father", "Wives submit" (twice) and "Parents provoke". After a footnote, "the master of the sentences" is now "The master of the Sentences", as in ch. 3.

### An earlier review slip

- Ch. 9: Ambrose's "the party that is *for shaken* for Gods cause" is now "forsaken". The 1609 printing has "for saken", broken across the line.

### Spelling (the machine missed these)

- cal → call, an heard → an herd, bruit beasts → brute beasts (×2)
- Cananites → Canaanites (×2), commiteth → committeth (×5), marieth → marrieth
- "in advise" → "in advice", "Sea of Rome" → "See of Rome"

### Scripture references

- Esay 62. 7 → 62. 5 (the quotation is Isa. 62:5).
- Ephes. 6. 3 → 6. 4 ("provoke not your children").
- Jerem. 26. 6 → 29. 6 (as ch. 8 cites the same verse).
- Mat. 24. 25 → 24. 45 ("Who then is a faithful servant…").
- Ruth "chap. I. vers. II." → "chap. 1. vers. 11." The TCP had read the numerals as Roman.
- "v. II." → "v. 11." (2 Sam. 11:11).
- "Luk 10. 39." → "Luk. 10. 39.".

### Layout and spacing

- Ch. 17: the paragraph that broke in the middle of Prov. 27:26–27 ("… v. 27. ¶ And let the milk of thy goats …") is joined again.
- Dash spacing: "understanding —For" and "wonderfully— for" are closed up.

## Checked and kept

- **Ch. 13, Exod. 2:19 "delivered us from the Philistines":** the 1609 printing has "Philistims". It is Perkins' (or Pickering's) slip for "shepherds", and it is kept as the author's text.
- **Reference styles are kept as printed:** Mat./Matth., Psal./Psalm./Psa., Exod./Exo., "1 Cor. 7. 9" next to "1. Cor.", and Ans./Answ. They are the 1609 printer's, and the earlier review kept them.
- **Period words and forms are kept:** -eth and -est verbs, "moe", "hath perished it", "indued", "to morrow", "to day", "a far off", "shamefastness", "aequipollent", "otherwhiles", "thrust him thorough". "then" for "than" is kept throughout.
- **Lombard's "now since the fall it is also remedy" is kept** (*etiam in remedium*). It is as printed.
- **The footnotes stay in original spelling**, as this edition decided (for example "Leuit.", "vxorem", "diuortijs").

## Checklist

- [x] `sweep.py --early`: all 186 hits read. They are -eth verbs, Latin in the notes, period words, and "great great grand-fathers" in the kinship lists. The only slip, "commiteth", is fixed.
- [x] `refs.py --quotes`: 209 references and 0 weak quote matches. The 1 missing verse is Coloss. 5. 11, printed that way in 1609 (question 1). Four wrong but existing verse numbers were found by reading and are fixed.
- [n/a] `slips.py`: the book has no modern witness.
- [x] `./fgb check`: OK. The rebuild matches, the TEI is valid, the orig layer matches the TCP and the book compiles. chapter-05 differs from the extraction only by the known layout `#linebreak()`.
- [x] `./fgb build`: 124 pages, within Lulu's margins (inside 0.625in), and no footnote warnings. epubcheck reports 0 errors and 0 warnings.
- [x] PDF text: no quotes curled the wrong way and no stray markup.
- [ ] **Shelf ready once the questions above are answered.** Questions 1, 5, 8 and 9 touch the sense of the text.
