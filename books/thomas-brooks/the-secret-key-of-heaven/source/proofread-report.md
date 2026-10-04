# The Secret Key of Heaven: proofreading report

A full read of `chapters/typ`: the epistle, the three opening chapters,
Arguments 1–20 and Applications 1–5, about 120,000 words. Each file was
checked against the 1665 printing (TCP `A29703`) and the KJV. The copy was
made from the Chapel Library edition (`Private Key to Heaven, The.epub`),
so most of its slips are Chapel Library's own and the witness agrees with
them. That is why a word-by-word comparison with 1665, not `slips.py`,
found them.

## Needs your decision

Answer like "1 yes, 2 no, 3 as recommended".

1. **Latin, Greek and Hebrew that are still cut.** Commit 555ca78 restored
   eleven phrases beside their English. These are still cut, or are given
   only in English: *poenae gravitas / personae dignitas*, *bene fecisti*,
   *bombarda christianorum*, *ultimum vitae / optimum gloria*, *invocare /
   advocare*, and the Hebrew *robets, tolagnath, gnarach, tsaphah*
   (app-03); *in nihil agendo*, *pulvinar diaboli*, *Carnifex* (now
   "executioner"), *totus oculus*, *munito corde / occlusa corde* (app-04);
   *meditatio nutrix orationis*, *aeternitati pingo*, *unum perpetuum
   hodie* (app-05); *lasuach* (arg-01); *porta coeli clavis paradisi*,
   *vicimus vicimus* (arg-08); *iste liber* (arg-06); *segullah* (arg-20);
   and the gloss "what extraordinary thing do you" (app-02, Mat 5:47).
   **Recommend:** restore the Latin beside the English, as 555ca78 did,
   and the Hebrew transliterations as printed. The Greek is lost in the
   TCP transcription ("non-Latin alphabet") and can only come from the
   page image.
2. **"Sirs!" where 1665 has "O Sirs"** (9 places: app-02 ×2, app-03 ×5,
   app-04, app-05). Chapel Library dropped the "O" here but kept "O sirs"
   27 times. **Recommend:** restore "O sirs!" so the book is consistent.
3. **Words Chapel Library lost.** app-04: "nor punishable by the hands of
   men", where 1665 has "by the Laws or hands of men". app-01 (end): "this
   may serve to exhort us", where 1665 has "But secondly, this may serve".
   **Recommend:** restore both.
4. **Ausonius / Ausanius** (app-04, the story of Parthenius). Chapel
   Library "corrected" the name to Ausonius, but 1665 and Gregory of Tours
   (*Hist.* III.36) both have Ausanius. **Recommend:** Ausanius.
5. **Harcatus / Hyrcanus.** 1665 has "Harcatus" and Chapel Library has
   "Hyrcanus". **Recommend:** keep Hyrcanus unless you prefer the printed
   form.
6. **"one perpetual day, which shall never see light"** (app-05). 1665
   reads the same, but the sense needs "night" (*unum perpetuum hodie*, a
   day with no night). **Recommend:** emend to "night" as an editor's
   correction.
7. **Song 8:11-12 after Bernard's "into the fields"** (app-05). Chapel
   Library added this reference; it is not in 1665, and 8:11-12 is about
   Solomon's vineyard. **Recommend:** drop it, or use Song 7:11 ("let us
   go forth into the field").
8. **Isa 54:13** (app-02, "the Spirit teaches"). Chapel Library expanded
   the reference into a quotation, so "In these words" now points at
   Isaiah instead of Brooks's own text. **Recommend:** return to the bare
   reference, as in 1665.
9. **"[Queen Elizabeth]"** (app-02) is Chapel Library's bracketed note
   beside "a great lady". **Recommend:** remove it, or make it a
   footnote.
10. **"yearnings"** (×4: arg-15, arg-19, app-03 ×2). This is 1665's
    "earnings", meaning longings, not wages. **Recommend:** keep it.
11. **"eminent danger"** (arg-13). This is the period spelling of
    "imminent". **Recommend:** modernize to "imminent".
12. **recompence (×2) / recompense.** **Recommend:** use "recompense"
    throughout.
13. **1Sa 1:11.** This is Brooks's reference; the verse he means is 1:13.
    **Recommend:** keep his reference.
14. **"as is evident by the scriptures in the margin"** (app-04 ×2; also
    elsewhere). The edition does not print the 1665 margin. **Recommend:**
    supply the margin's references in brackets, or change the wording to
    "in the scriptures".
15. **Earlier editor's wording, kept as is.** These are listed only in case
    you want them undone: "unskilful idiot" became "uneducated person"
    (arg-12), "victuals" became "food", "without all peradventure" became
    "without any doubt" (ch-03), every 'tis became "it is", 1665 "turtle"
    became "turtle dove", "homicide" became "murderer", and "Zeuxis …
    curious" became "cautious". **Recommend:** keep them.

## Fixed (62 edits, all synced; the evidence is 1665 unless marked)

### Wrong words (mostly Chapel Library slips)

- arg-08: "by might and flight" is now "might and sleight" (1665 "slight"; the next sentence has "sleights").
- arg-12: "His greatest and our choicest secrets" is now "His choicest".
- app-02: "Sirs, I, as you, love" is now "O sirs, as you love"; "enjoin our affections" is now "conjoin"; "so forwardly" is now "frowardly"; "husbandmen until their fields" is now "till"; "Thou sayest thou cannot pray" is now "canst not".
- app-04: "held the eye and ear of God" is now "care"; "The very thought of sin, if but thought on" is now "if not".
- app-05: "who is steadfastly resolved" is now "who is **not** steadfastly" (Chapel Library had reversed the sense); "If they were condemned … they gave him" is now "If any"; "would but spare one quarter of an hour" is now "spend".
- ch-01: "dear friend" is now "dear friends".
- Names: "Eropas" is now "Eropus" (1665 "Ero••s"); "Sirtorius" is now "Sertorius"; "brevis doemon" is now "daemon".

### Divine pronouns and case

About a dozen places were brought into line with the book's style. In arg-08, "God sends forth his mandamus" now has "His", and Augustine's "dost thou hear" now has "Thou". The same fix was made in arg-12, arg-14, app-02 ("until he entered", "some of his people") and app-03 ×4. "as a man would speak to His friend" is now "his". "Pharisees" is capitalized.

### Quotation marks and punctuation

- arg-01: "saying. “Well" is now "saying, “Well".
- arg-02: "bloody sweat; so John" is now "… sweat. So John".
- app-02: "the holy”." is now "holy.”"; ‘My sister …” now opens with “; "the “the soul’s beast" has lost its doubled "the".
- app-04: "city”, that is" is now "city,” that is".
- app-05: the stray “ before "Meditation is the nurse of prayer" now has its closing mark.
- app-02: "Tenthly and lastly. When" is now ", when"; the "authentic. / And, for ensuring." paragraph is merged as in 1665.
- app-03: "(1Sa 5). That closet duties" is now "5), that"; "it was" at the start of a sentence is now capitalized.

### References and numbers

- "the 16 argument" is now "16th"; "the 25 Psalm" is now "25th"; "the 15 verse" is now "15th".
- app-03: 2Ti 4:2 is now 1Ti 4:2 (the seared conscience); 1Sa 18:23 is now 2Sa 18:23 (Ahimaaz); and in the Hebrew, ה is now ת for *tau*.
- "(Heb 2:17; John 17)" is now "Joh 17", in the book's style. Zech is now Zec (×2), and "Song 2:16; 3-6" is now "2:16, 3-6".

### Spacing and joined words

- "forpublic" is now "for public".
- "water pot", "still born" and "love tokens" are now hyphenated or joined, as in both 1665 and Chapel Library.
- "sweet meats" is now "sweetmeats", and "resting place" is now "resting-place" (the book's form).
- "Dr Sibbes" is now "Dr. Sibbes".

## Checked and kept

- **1Ki 19:8** beside "subject to like passions" (app-02): the reference is Brooks's own margin and goes with "Enoch-like, he walked with God" (forty days in the strength of that meat).
- **Chapel Library's KJV wording** inside quotations, where 1665 paraphrases (for example "An idle soul shall suffer hunger" for 1665 "idle person"). This is kept because the edition quotes the KJV.
- "Nehemiah … rebuilt the temple" (app-05) is Brooks's slip (it was the wall), as printed.
- "Secret hatred often issues in open murder": 1665 has "upon", a misprint, and Chapel Library's "open" is right.
- `sweep.py`: 137 hits. All are period forms, names, or the book's abbreviated references (Joh, Jdg, Amo); `forpublic` was fixed.
- `refs.py`: 778 references, none missing. The five weak matches are chains of verses or Brooks's own references (Song 8:11-12 is in question 7).

## Shelf-ready checklist

- [x] Whole text read for sense (all 28 files).
- [x] `sweep.py` hits fixed or explained.
- [x] `slips.py` (3 hits) resolved.
- [x] `refs.py`: no missing verses; weak matches read.
- [x] `./fgb check brooks` OK. In step [2], 17 files differ from the extraction only by layout lines and a blank line after the heading; this was true before the branch.
- [x] `./fgb build brooks`: 293 pages; inside margin 1.0in (Lulu 1.0in); nothing within 0.5in of the trim; the spine (0.73in) matches 293 pages; epubcheck reports 0 errors and 0 warnings.
- [x] The PDF text has no wrongly curled quotes and no stray markup.
- [ ] Questions 1–14 are open. Questions 1–4 and 6 change the text, so the book should wait for them before printing.
