# Of Domestical Duties: proofreading report

A full read of `chapters/typ`, all four volumes (the dedication, the
parallel of duties, and the eight treatises, about 400,000 words), checked
against the 1622 printing (TCP `A68107`, the TEI's printed layer) and the
KJV. There is no modern witness. Most errors were print or transcription
slips the machine pass carried through. The rest were 1622 spellings the
machine did not modernize.

The work was done by four volume reviews (2026-10-02/03), merged into one
branch and finished on 2026-10-03. About 3,950 word-level edits, all synced
into the TEI:

| Volume | Edits |
| --- | --- |
| 1 | 861 |
| 2 | 1,580 |
| 3 | 998 |
| 4 | 514 |

## Decided 2026-10-04 and applied

Every recommendation below was accepted ("go for all of it") and applied
in `chapters/typ`, with these notes:

- **30 ("then"/"than"):** the premise was wrong. The 1622 printing itself
  has "than" in all 16 places the edition prints it, so they are kept as
  printed. Nothing was changed.
- **8, 12, 18, 36:** kept as printed, as recommended.
- **25 (epigraphs):** both are set as epigraphs (new encoding
  `p[@rend="epigraph"]`).
- **26 (lists):** done with new encodings:
  - §56: `cell[@rend="nested"]`, a brace branch set under the branch before it.
  - vol 2, 17 §47: `table[@rend="inline"]`, the brace read as one sentence:
    "we will consider the extent and continuance thereof".
  - vol 2, 10: `head[@next]`, "Object." run into its paragraph.
- **35 (spellings):** 503 words of the 1622 spelling map are in
  `source/spelling_1622.py`, merged into `SPELLING`. The machine is now
  credited with about 640 decisions (editor spelling decisions went from
  1,264 to 622), and the text is unchanged.
  - Left out: misprints (beter, thogh…), words read by context
    (course/coarse, staid, steed…), and words used in another sense
    elsewhere (aduise as both advice and advise, bee, paine).
- **Also fixed:** a footnote in vol 3, 06 cited "Reu. 16. 15", which is now "Rev. 16. 15" (the thief verse).

**Proofed to print so far: volume 1** (PDF and Lulu checks, below).
Volumes 2–4 carry the same decisions but have not been proofread in the
built PDF since.

### The 1622 errata (the printer's own corrections, never applied)

The errata leaf at the end of the 1622 book lists these. Each one was
checked against the text.

1. **p. 218, vol 2 (adultery and repentance):** "(for we have direct and strict warrant for it)". The erratum reads "we have **no** direct". This reverses the sense. **Recommend: apply.**
2. **p. 215, vol 2:** "such dissolution" should be "such **a** dissolution". **Recommend: apply.**
3. **p. 268, vol 2, Treat. 3 §2:** "honour which is required in the first commandment" should be "**fifth** commandment". **Recommend: apply.**
4. **p. 297, vol 2, Treat. 3 §27:** "A fit reason may be taken from the mischiefs" should be "A **fifth** reason" (it follows the fourth). **Recommend: apply.**
5. **p. 412, vol 2, §60/61:** "both by their wives … but also by their children" should be "**and** also". **Recommend: apply.**
6. **p. 606, vol 4, ch 3 §11:** "a point of justice and unlawful" should be "a point of **injustice**". **Recommend: apply.**
7. **p. 629, vol 4, ch 4 §31:** "Example and advice of ones equal" should be "of **one** equal". **Recommend: apply.**
8. **p. 218, margin:** the erratum for "viro" (Chrysostom's "Vir post fornicationem non est vir") could not be placed. **Recommend:** leave it.

### Readings where the print is wrong but the fix is a real change of words

9. **Vol 1, 02 §13:** "Thus the Apostle himself expoundeth this phrase, chap. 5. vers. 5, 6." Eph 6:5-6 ("as unto Christ") is the passage that expounds it. **Recommend: chap. 6.**
10. **Vol 2, ch 3 §9:** "(Eccles. 20. 7.)" is given for abstinence. The verse meant is Ezek 18:6. **Recommend: Ezek. 18. 6.**
11. **Vol 2, ch 6 §31:** Prov 22:1, "to be chosen #emph[love great riches]" (print "loue"). **Recommend: "above great riches".**
12. **Vol 2, ch 12 §60:** "a curst cow, which having given a fair soap of milk". The print has "soape", probably meaning "sup" (a quantity of milk). **Recommend:** leave it as printed.
13. **Vol 3, 01 §6:** "when children pout, lour, swell, and give to answer at all". The print is the same; a word is lost. **Recommend: "give no answer at all".**
14. **Vol 3, 01 §5:** "making known to them me needful matter". **Recommend: "some needful matter".**
15. **Vol 3, 02 §14:** the one illegible word ("4. For the loving of father and mother more then Christ, ⟨…⟩ It doth not") is almost certainly the number "1.", because "2. If they be forsaken" follows. **Recommend: "1."**
16. **Vol 3, 02 §12:** "Num. 30. 17" points at a verse that does not exist; KJV 30:16 is the verse meant. **Recommend: 30. 16.**
17. **Vol 3, 02 §14:** "Levies speech" (×2) is Levi's. **Recommend: "Levis"**, the book's possessive style without an apostrophe (see 27).
18. **Vol 3, 04 §45:** "the duty of children to bring the bodies of their parents deceased". **Recommend:** keep it ("bring" = carry to the grave); "bury" is possible.
19. **Vol 4, ch 7 §17:** "the phrase with the Apostle useth". **Recommend: "which the Apostle useth".**
20. **Vol 4, ch 9 §36:** "foking". **Recommend:** check the page image; perhaps "soaking".
21. **Vol 4, ch 10:** "As God is the masters of servants" (printed so). **Recommend: "master".**

### Layout and structure (needs a pipeline change or a careful edit)

22. **Vol 3, 06 §23:** margin notes run into the text: "till it be fit to be placed forth: even so Many distinguish the whole course of a mans life into four parts. 1. Childhood … Long as ordinarily it liveth under the parents government". The age list, "Children must be well + Fed + Taught" and "Feed them in discipline, saith the Apostle" are run in the same way. **Recommend:** rejoin "even so long as ordinarily it liveth under the parents government" and set the margin matter as footnotes.
23. **Vol 4, ch 6 (Treat. 8 §4):** the TCP turned a sentence into a false section heading ("=== §. 4. Some of the reasons…"). **Recommend:** make it a paragraph again.
24. **Vol 4, ch 8 §25:** "The Hebrew word is oft used for scarlet…" is a margin note set as body text. **Recommend:** make it a footnote.
25. **Epigraphs set as plain paragraphs:** vol 1, 11 (EPHES. 6. 1) and vol 4, ch 1 §126 (verse 7), unlike the other epigraphs. **Recommend:** set them as epigraphs.
26. **Lists the pipeline cannot store:**
    - vol 1, 07 §56 sets "Nourisheth" and "Cherisheth" as items 3–4, when they are the two branches of item 2;
    - vol 2, 17 §47, where the machine read a brace as a list ("+ In this provident care … of / + His wife, we will consider the / + Extent / + Continuance");
    - vol 2, 10, where a run-in "#strong[Object.]" head cannot be merged into its paragraph.

    **Recommend:** teach `build_tei.py` these, as was done for Perkins and Bunyan.

### Spellings and forms across the book

27. **Possessives:** names from the shared spelling table get an apostrophe (Adam's, David's, Abraham's, Jacob's, Solomon's: 74 places), while the book writes "Aarons, Sauls, Josephs", sometimes side by side ("The issue of Adam's, Aarons, Sauls"). **Recommend:** drop the apostrophe from the table names in this book, to match the book.
28. **humane (20) / human (1):** "humane nature", "humane laws". **Recommend: "human"** where it means human.
29. **in deed (6) / indeed (43):** three in vol 1, 03 mean "indeed". **Recommend:** join those three.
30. **"then" for "than":** "more then" appears 97 times against "more than" 6. **Recommend:** keep "then" (the book's form) and change the 6 to match.
31. **Holy Ghost (23) / holy Ghost (27).** **Recommend: "Holy Ghost".**
32. **ourselves (2), yourselves (1), herself (2), himself (391):** against "our selves" 57, "your selves" 17, "her self" 109. **Recommend:** keep the separated forms but join "him self" (×1), and make the few joined "our/your/her" forms match the majority.
33. **Duplicate section numbers, as printed:**
    - vol 2, 14 has §. 15 twice;
    - vol 2, 16 has §. 43 twice;
    - vol 2, 17 has §. 57 after 55 and §. 58 twice;
    - vol 1, 06 has §. 44 between 48 and 50 (that one is surely 49).

    **Recommend:** §. 49 in vol 1; elsewhere keep Gouge's numbers.
34. **Heading, vol 1, 03 §16:** "Of the resemblance betwixt The Church to Christ. A wife to her husband." (a brace in the print). **Recommend:** "Of the resemblance betwixt the Church to Christ, and a wife to her husband."
35. **The 1622 spellings fixed by hand:** about 300 words the machine missed (cleering, aduiseth, inioyneth, borne for born…) were fixed in `chapters/typ` across all volumes. **Recommend:** move this word map into `editorial.py` `SPELLING`, so the machine credits them. The text would not change.
36. **Latin misprints left as printed** (impiun, seruorun, seruabaxtur, Conslit, di'igat, sea quo. libet, fine causa, revs, Deil.), per the README. **Recommend:** keep them, or correct them as was done for the clear ones (see below).

## Fixed

### Misprints in the 1622 printing (the sense is clear; print reading shown)

- **Vol 1:**
  - EPHES. 6. 29 is now 5. 29 (the epigraph).
  - "evidences of Gods Jove" is now "love".
  - "What now if all the world have us?" is now "hate us?".
  - "members of Christ body" is now "Christs body".
  - "the line of our reason" (print "last").
  - "is no rust excuse" is now "just".
  - "Psalm 28" is now "128".
  - 1 King. 13. 14 is now 13. 24; Isa. 17. 1 is now 57. 1; Judg. 9. 5 6 is now 9. 56.
  - "Iob." is now "Joh." where John is cited (×4).
  - The §31 heading "value of the prince of our redemption" is now "price" (vol 1, 04; a misprint in Gouge's own head).
- **Vol 2:**
  - "slut, drab, quean" (print "stut, drab, queant").
  - "above all others" (print "about").
  - "his joy and delight" (print "by").
  - "if before them" (print "of").
  - "if it be kept".
  - "the good we aim at" (print "time at").
  - "the good of her soul" (print "rule").
  - "I will most gladly bestow, and be bestowed for your souls" (print "bestowed", the words "bestow, and be" lost; 2 Cor 12:15 Geneva).
  - "by just consequence" (print "must").
  - "their pleasure" (print "measure").
  - "at noon day" (print "soon").
  - "If thou be righteous" (print "be est", Job 35:7).
  - Mic. 4. 9 (print "49").
  - "a slavish fear" (print "feat").
- **Vol 3:**
  - "tendeth" (print "condeth").
  - "covet earnestly" (print "ccuet").
  - "with ease" (print "case").
  - "teach children" (print "each").
  - "When scholars" (print "Then").
  - "that may" ×2 (print "at").
  - "oft he repeateth" (print "of the").
  - "at first".
  - "a very wise man".
  - "it is then safest" (print lacks "is").
  - "seek" (print "leek").
  - "the main ends" (print "rhaine").
  - "reckoning: if the Guardian … he careth" (print "of … the caueth").
  - "after a sort" (print "for").
  - "like unto leaven" (print "heauen", Mat 13:33).
  - Jer. 30. 11 for "God correcteth in measure" (print 10. 11).
  - 1 Sam. 16. 11 for Jesse's son keeping sheep (print 16. 7).
- **Vol 4:**
  - "lest" for "left".
  - "Onesimus" (print "One simus").
  - "fences and gates" (print "sences and gats").
  - "set on fire".
  - "Jesse" (machine error "Jess").
  - "infect" (print "insect"), and many more.
  - The margin note in ch 7 §16 that had run into the text is now a footnote.

### Machine-pass errors and missed spellings

- **born / borne:** "borne" is now "born" wherever it means birth (62 places). It is kept where it means carried or endured ("to be borne withal").
- **Missed 1622 spellings, book-wide:** about 300 words, among them aduiseth, inioyneth, pitty, mony, Angell, hiderance, Counseller, commiteth, and infereth, indeavour, wearisomness, privatly, jaylor, revenewes.
- **Slips:** wordlings → worldlings, conpany, mafested, fron, beevishness → peevishness, blewness → blueness (Prov 20:30), corasive → corrosive, cunny → coney.
- **Lost capitals:** "Children obey", "Honour", "Mothers in law", "Love covereth", and capitals after Object./Answ.
- **Latin the machine had modernized, restored:** "parentes" (×2), "partes", "Senecae", "vocatione".
- **Abbreviations:** Reu. → Rev., Leu. → Lev., Iam. → Jam., Uers. → Vers., the last old I/J and u/v forms in the references.

### Names in KJV form (as the volume reviews had begun)

- Adonijah, Jesse (Ishai), Ahasuerus (×13, from Ahash-verosh, Ahashuerosh and other forms), Eli, Elijah, Jehoshaphat, Bathsheba, Michal, Reuben, Hiram, Naomi, Phinehas.
- Shunammite, Amalekites, Hittites, Ezekiel, Zechariah (the prophet; Luke's Zachary is kept).
- Isaiah where it was English "Isay"; "in Isay" in Latin is kept.

### References and punctuation

- **Doubled full stops:** "3. 7..", "5. 14.." and others, throughout.
- **Missing stops:** "Gen. 3 10", "21. 3 #emph[Jer.]", "§ 33", "Treat 3." and others.
- **Item labels:** "1\." where "1" was meant, and the reverse.
- **Stray print marks:** asterisks, the "a"/"b" footnote letters, "Tract▪".

### Latin misprints (clear ones)

- filios, castigandum, si nulla, adunci sunt, iam, adultam, matrimonio, iuventutis, fornicandi, eorum, Leonidis, adhuc, ab ipsis … consecretur, potestatem, accusamur, praeesse, annitendum, tanquam … afficere, domum sponsi, spiritaliter, Verendum, Vatabl.
- The volume reviews corrected dozens more (cum, dum, autem, inauditum…).

### Epigraphs

- Italics nested inside the italic epigraph blocks printed upright; they are removed in ten epigraphs across the volumes (among them Eph 6:3, with "mayest").

## Restored from the 1622 page images (2026-10-06)

The page images of the copy the TCP was made from are on archive.org
(`bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622`,
scan index = 2 x TCP image - 3 or - 2), and a second 1622 copy
(`..._of-domesticall-duties_gouge-william_1622`). Read from them:

- **Greek and Hebrew, 240 places** the TCP left as "in non-Latin alphabet":
  all restored as printed (230 high certainty, 10 medium), as `#editor` fills
  in `gap_fixes.py` with the scan and evidence for each. With the words back,
  61 stops the review had deleted (left hanging when the Greek was dropped:
  "1 Tim. 5. 14. .") are printed again.
  - Kept as printed: ψίλος (Eph 5:27, for σπίλος), ῥύτις, σώζειν, οἱ γόνεις,
    ἴδιοι, צבח (Job 7:1 has צבא), and Gouge's own εὖ in 1 Tim 3:4.
  - Medium: 80, 93 (יארכון), 94, 232, 250, 708, 710 (אף ab אנף), 712, and
    the unclear accents noted in each entry.
- **Pages 191–196**, missing from the filmed copy, transcribed from the
  second copy (`source/A68107.supplied.xml`): the end of §10 and §§11–13 of the
  second treatise. "Seeking Marriage" now holds §§1–13 and "Getting Married"
  §§14–28 (`edition.json`). The text joins exactly at both ends (catchwords
  "maids." and "parties"). Editorial fixes in it, as in the rest of the book:
  servingmen, capable, leaven, females, yoked, exemplary, Nazarite, Rebekah,
  "Luk." with its stop, "Isaac." for the printed comma, and 1 Cor. 7. 16
  (printed "1. 16").
- **The one illegible word** (vol 3, 02): "1.", as the edition had it; the
  second copy and the 1634 edition print it.
- **"foking"** (vol 4, 09) is "ſoking" with a long s: "soaking" is right.
- **Medium-certainty fills, 177:** 144 confirmed, 32 corrected, 1 still
  unreadable (260, a figure in "Coke Rep. 4."). Corrections that change the
  text: man's or woman's **lust** (not sacrifice), an angry King over a
  **subject** (not object), a **mocker** to his father (not cocker),
  **urge** matters (not use), relinquish **the** place (not their),
  **Rhem.** loc. citat. (the Rhemists, cited earlier in the section; not
  Bellarm.), committit, alijque, Dominus, ad Cler.; the rest confirm readings
  the review had already made by sense (aim, pleasure, noon, sine, just,
  teach, very, no, so, tell, she, ought, if).
- Also fixed: "di'igat" is "diligat" (vol 4, 10).

## Checked and kept

- **Period English:** -eth forms, "then" for "than", "it self / any thing / our selves" written apart, "betwixt", "too too", "Pigsny", "gripulous", "venter", "slaken", "nousled", "bezel".
- **British spellings:** honour, labour, favour, Saviour, consistent throughout.
- **`refs.py`:** 2,361 references, 8 reported as missing.
  - Four are Latin titles ("Aug. de Unit. Eccl.").
  - "Philem. v. 2" is verse 2.
  - "I John 4. 34" is "that is, I [John 4:34] prefer it".
  - Two are questions 10 and 16.
- **`sweep.py`:** the hits are Latin, period forms, the possessive question (27), "Coke Rep. 4. 3 3." (a law report, printed so) and "too too".

## Shelf-ready checklist

- [x] Whole text read for sense (53 files, all four volumes).
- [x] `sweep.py` and `refs.py` hits fixed or explained.
- [x] `./fgb check gouge`: OK.
  - In step [2], 10 files differ from the extraction only in where an italic run or a footnote marker falls, or by known layout lines.
- [x] `./fgb build gouge`: the four volumes are 195, 295, 194 and 153 pages, unchanged and matching the covers.
  - Inside margins are 1.0in, and nothing is within 0.5in of the trim.
  - epubcheck reports 0 errors and 0 warnings.
- [x] 47 warnings that a footnote is set on another page than its marker (Typst's widow control).
  - The build from `main` gives 48, so they predate this review; none are new.
- [x] The PDF text has no wrongly curled quotes and no stray markup.
- [x] Questions 1–36 decided and applied (2026-10-04).
- [x] Volume 1 rebuilt after the decisions: 195 pages, Lulu margins OK.
  - It has 9 footnote warnings, the same as `main`.
  - The epigraph and the §56 branches checked in the PDF text; no stray markup.
  - The EPUB (all four volumes) passes epubcheck with 0 errors and 0 warnings.
- [ ] Volumes 2–4: rebuild and proof the PDFs (left for later).
