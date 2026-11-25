# Calvin, Institutes, vol. 6 (Book IV, chapters 14–20): Classic re-checked against the 1845 printing (Kraken OCR)

Base: `chapters/typ/vol-6/*.typ` in the `wt-institutes` worktree (book-4-chapter-14 … book-4-chapter-20; read only;
HEAD c1b462e7). Witness: Calvin Translation Society, Edinburgh 1845, our own scans, Kraken OCR with ALTO beside it, page images
`pages/p-NNNN.png`. Book IV ch. 14–20 lie wholly in **1845 vol. 3, pp. 299–554** (`work/institutes/vol3/kraken/`, image =
printed page + 4, images 303–558): ch. 14 begins p. 299 (image 303), ch. 15 p. 327, ch. 16 p. 349, ch. 17 p. 386, ch. 18
p. 457, ch. 19 p. 479, ch. 20 p. 518 (image 522), and Book IV ends on p. 554 (image 558) with “END OF THE INSTITUTES.”; the One
Hundred Aphorisms from image 559 on are not part of this volume and were not compared. In the **p.** column **III.n** is a page
of 1845 vol. 3.
Method (as vol. 5, same scripts adapted): every .typ file was aligned word by word with the Kraken text (difflib; main text
first, then the footnotes against the OCR words the main text left over; running heads dropped; line-end hyphens joined).
Differences were filtered for reference style (Roman → Arabic compared as numbers), American spelling and OCR noise; then
every remaining candidate (116 word and 40 reference rows, 20 capital-letter rows, 17 long runs) was read, and every one
that was not plain OCR noise was checked on the page image (line crops from the ALTO boxes: `w1.png`, `w2.png`, `z.png`,
`z2.png`, `r1.png`, `r2.png`, `cs1.png`, `gk.png` (the Greek), single crops in `crops/`). Two checks were added this time:
`doubles.py` compares the aligned words again with doubled letters kept (the aligner's fold collapses them, so a slip like
“suppresing” is invisible to it), and `bookcheck.py` lists reference rows whose numbers agree but whose book names differ
(the filter drops those). Every reference left unmatched in the OCR was checked against the CCEL text of its own chapter
(`refcheck.py`), every OCR run of two or more words left unmatched was read, and the footnotes were counted chapter by
chapter (`notecount.py`) and page by page (`notepages.py`) against CCEL's; every difference in the counts was traced. Only
what the image confirms is listed.
Scripts and raw candidates: `work/institutes/latin/vol6/recheck/` (`align.py`, `filter.py`, `refcheck.py`, `notepages.py`,
`notecount.py`, `doubles.py`, `bookcheck.py`, `crop.py`, `mkbatch.py`, `batch.sh`, `cand.json`, `cand.tsv`, `cand2.tsv`,
`cases.tsv`, `doubles.tsv`, `residual.txt`, `notepages.txt`, `build_report.py`, `apply-input.jsonl`, `manual-edits.json`,
`apply_recheck.py` (now with `VOLDIR`), `dryrun.txt`).

**Rule applied (editor, 2026-11-23):** the Classic follows the 1845 print wherever CCEL's wording departs from it, including
CCEL's modernised grammar (kind **d/grammar**) and CCEL additions (kind **c**). Not listed: Arabic reference style, American
spelling (1845 forms here: honour, favour, recognising, catechising, practised, despatch, sepulchre, grey, phrenzy, stye,
counsellor, fulfil/fulfilment, worshipper, quarrelling, enrol, carcases…), CCEL's punctuation around references, CCEL's word
joins (1845 “any thing”, “every thing”, “every where”, “good-will”, “judgment-seat”), Greek accents. The `proposed` column holds
only the replacement words; explanations are in the anchor and kind columns; an empty `proposed` means no change to the text
(misprint-1845). Where a row needs more than one word changed, or words added, `proposed` holds the whole replacement snippet
and the change is in `manual-edits.json`.

**Kinds:** b (1845 words missing in CCEL), c (CCEL words absent from 1845), d (a different word), d/grammar (CCEL's
modernised verb form), d/case (capital letter differs from the print), n (notes), misprint-1845 (the 1845 print is wrong;
CCEL corrects it).

**Counts:** d 7, d/case 19, d/grammar 1, misprint-1845 8 (total 35); no rows of kind b, c or n.

**Systematic check.** As in vol. 5 the verb forms agree: the OCR of pp. 299–554 and the seven .typ files alike give has
220, hath 17, does 75, Does 2, doth 3, saith 4, says 130, cometh 3, maketh 1, makes 43 (comes 8 against 7 is the print's
line-end “be-comes”). The one CCEL verb change is **sprung for “sprang”** (III.435, kind d/grammar). There is no “an” before
u- or h- that CCEL has made “a” (the print's an high ×2, an honest, an ubiquity, an un- ×10 all stand in CCEL). The word rows
are single CCEL slips: embued for *imbued*, amidst for *amid*, confectioneries for the print's (and the Authorised Version's)
*confectionaries*, and two French notes, “institutée” for *instituée* (III.350) and “effrontées” for *effrontés* (III.467).
Two Scripture references in the main text are wrong in CCEL and right in the print: Matt 9:19 for **4:19** (“fishers of men”,
III.381) and 1 Sam 24:9–11 for **26:9–11** (“Who can stretch forth his hand against the Lord's anointed, and be guiltless?”,
III.550). The capital comparison gives 20 rows: 19 are listed, one (III.386, “The knowledge of the sacrament”) is an OCR
misreading. CCEL adds nothing to the text that the print lacks (no kind c), and leaves out nothing (no kind b). Eight 1845
misprints are listed so that nobody “restores” them; four are footnote or text references the print gets wrong (1 John iv. 23,
Matth. vii. 33, Acts vii. 21, Prov. xvii. 14). This volume had already been checked against 1845 once (`bca6e3c6`, 134 findings;
`a2b5470c`, 8 references; and the typesetting sweep `06d783b4`), which is why so little is left.

**Also seen, not listed:** reference style (“Chap. xiv.” / “Chapter 14”, “Book III. Chap. xix.” / “Book 3 Chapter 19”,
“2 John ver. 7” / “2 John 7”, “Lib. iii.” / “Lib. 3”); CCEL's punctuation in the Father references (“&c.;” / “&c.,” at III.394,
“Art. 4” / “Art 4”, “Ad Concil.” / “Ad. Concil.” at III.375, “Dist. 5.” / “Dist. 5,” at III.489); “coeur” / “cœur” in the
French note at III.351 (a ligature); Greek accents; the other
“the divine liberality and kindness” (III.311, lower-case in the print too); spellings in the rule above.

**Structural:** no Beveridge footnote is missing in vol. 6 and none is added: CCEL has 67 notes (ch. 14–20: 5, 5, 3, 15, 11,
17, 11) and the print has the same. Chapters 14, 15 and 18 gave the same count at once; the differences in ch. 16, 17, 19
and 20 were signatures (“2A”, “2B”, “2D”–“2F”, “2H”, “2K”–“2M”) the counter took for notes, the note at III.457 that sits
on the page where ch. 18 begins, and notes whose first line the counter missed (“1 John ii. 18…”, III.477; “du temps de
Sainct Augustin”, III.488; “On conte trois especes de regime civil”, III.527; the two notes at III.532); each was found on its
page, and the note texts agree (the references in the notes were read on the image, `r1.png`, `r2.png`). Every OCR run left
unmatched after both passes is a reference present in CCEL in Arabic form (`refcheck.py` flags only OCR misreadings and the
listed rows), a running head or a signature (“VOL. III.”, “2A”…); no CCEL word is left without an OCR partner except a note
bracket and a section number. No CCEL line is absent from 1845 and no 1845 line from CCEL; the chapter titles, arguments and
Sections lists agree (capitals apart, listed).


## Book IV, chapter 14 — `book-4-chapter-14.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §17 give a ratification of the gifts which the Divine liberality has bestowed | the divine liberality has | the Divine liberality has | Divine | III.316 | d/case | high |

## Book IV, chapter 15 — `book-4-chapter-15.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §19 nothing which is appropriate would be omitted [keep CCEL (1845 “which i appropriate”)] | which is appropriate | which i appropriate |  | III.344 | misprint-1845 | - |

## Book IV, chapter 16 — `book-4-chapter-16.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 note (French): si elle n’avoit point eté instituée de Dieu | eté institutée de | eté instituée de | instituée | III.350 | d | high |
| §26 youth who, after being imbued duly and properly with the rudiments of piety | being embued duly | being imbued duly | imbued | III.375 | d | high |
| §31 all kinds of fishes? (1845 “Matth. iv. 19”, “fishers of men”; CCEL 9:19) | (Matt 9:19; 13:47) | (Matth. iv. 19; xiii. 47.) | (Matt 4:19; 13:47) | III.381 | d | high |

## Book IV, chapter 17 — `book-4-chapter-17.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §25 On hearing the words of Christ, This is my body | Christ, this is my | Christ, This is my | This | III.419 | d/case | high |
| §32 “Every spirit that confesseth not …” (1 John 4:3) [keep CCEL (1845 “1 John iv. 23”; the chapter has 21 verses)] | (1 John 4:3; 2 John 7) | (1 John iv. 23; 2 John ver. 7.) |  | III.432 | misprint-1845 | - |
| §33 neglecting and almost suppressing them [keep CCEL (1845 “suppresing”)] | almost suppressing them | almost suppresing them |  | III.432 | misprint-1845 | - |
| §33 the seed which fell among thorns sprang up (1845 “sprang”) | thorns sprung up | thorns sprang up | sprang | III.435 | d/grammar | high |

## Book IV, chapter 18 — `book-4-chapter-18.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 14. Those who mutter over the Mass cannot be called priests | mutter over the mass | mutter over the Mass | Mass | III.458 | d/case | high |
| Sections 19. the views which ought to be held concerning Baptism and the Lord’s Supper | concerning baptism and | concerning Baptism and | Baptism | III.458 | d/case | high |
| §1 the way in which the sounder schoolmen at first received | sounder Schoolmen at | sounder schoolmen at | schoolmen | III.458 | d/case | high |
| §7 While the Supper itself is a gift of God | While the supper itself | While the Supper itself | Supper | III.465 | d/case | high |
| §9 note (French): ceux qui sont les plus effrontés entre les Papistes | plus effrontées entre | plus effrontés entre | effrontés | III.467 | d | high |
| §14 But what else is done in the Mass than | done in the mass | done in the Mass | Mass | III.472 | d/case | high |

## Book IV, chapter 19 — `book-4-chapter-19.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Argument: Impiety of the Popish teachers in attributing more | the popish teachers | the Popish teachers | Popish | III.479 | d/case | high |
| §23 note: John 2:15; 10:7; Luke 4:17; Mark 7:33 [keep CCEL (1845 “Matth. vii. 33”; Matthew 7 has 29 verses, the spittle and the tongue are Mark 7:33)] | Mark 7:33; | Matth. vii. 33; |  | III.503 | misprint-1845 | - |
| §24 and shut the doors of churches? | doors of Churches? | doors of churches? | churches | III.504 | d/case | high |
| §34 The last of all is Marriage, which | is marriage, which | is Marriage, which | Marriage | III.513 | d/case | high |
| §34 “I am the true vine, and my Father is the husbandman” | my father is | my Father is | Father | III.514 | d/case | high |

## Book IV, chapter 20 — `book-4-chapter-20.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Argument: Next, the three forms of civil government are added | three Forms of | three forms of | forms | III.518 | d/case | high |
| Sections 12. Objection, that the lawfulness of War is not taught in Scripture | lawfulness of war is | lawfulness of War is | War | III.519 | d/case | high |
| Sections 16. All laws should be just | All Laws should | All laws should | laws | III.519 | d/case | high |
| Sections 16. Civil law of Moses; how far in force | Civil Law of Moses | Civil law of Moses | law | III.519 | d/case | high |
| §4 Augustine: “If Scripture called them gods, to whom the word of God came” | called them Gods, | called them gods, | gods | III.523 | d/case | high |
| §7 “The kings of the Gentiles exercise lordship over them” | of the gentiles | of the Gentiles | Gentiles | III.526 | d/case | high |
| §9 defending the honor of Him whose vicegerents they are | honor of him whose | honor of Him whose | Him | III.529 | d/case | high |
| §10 note: Exod 2:12; Acts 7:24 [keep CCEL (1845 “Acts vii. 21”; Moses strikes the Egyptian in 7:24)] | Exod 2:12; Acts 7:24; | Exod. ii. 12; Acts vii. 21; |  | III.532 | misprint-1845 | - |
| §10 note: Prov … 17:15; 17:11; 24:24 [keep CCEL (1845 “xvii. 14”; the text quotes 17:11, “An evil man seeketh only rebellion”, III.533)] | 17:15; 17:11; 24:24.] | xvii. 15; xvii. 14; xxiv. 24. |  | III.532 | misprint-1845 | - |
| §16 Yet we see that amid this diversity they all tend | amidst this diversity | amid this diversity | amid | III.539 | d | high |
| §19 from the governor to Cæsar’s judgment seat [keep CCEL (1845 “Cesar’s” here; vol. 5 has “Cæsars”, III.149)] | governor to Cæsar’s | governor to Cesar’s |  | III.541 | misprint-1845 | medium |
| §21 the passion for litigation prevailed in the church of Corinth | in the Church of Corinth | in the church of Corinth | church | III.543 | d/case | high |
| §25 raised up by him to punish the people for their iniquity [keep CCEL (1845 “so punish”)] | by him to punish | by him so punish |  | III.546 | misprint-1845 | - |
| §26 he will take your daughters to be confectionaries (1 Sam 8:13; 1845 “confectionaries”, the women who make them) | be confectioneries, | be confectionaries, | confectionaries | III.548 | d | high |
| §28 “Who can stretch forth his hand against the Lord’s anointed” (1845 “1 Sam. xxvi. 9-11”; CCEL 24:9–11) | (1 Sam 24:9–11) | (1 Sam. xxvi. 9-11.) | (1 Sam 26:9–11) | III.550 | d | high |

## Findings (one JSON line each)

```
{"file": "book-4-chapter-14.typ", "anchor": "§17 give a ratification of the gifts which the Divine liberality has bestowed", "ccel": "the divine liberality has", "1845": "the Divine liberality has", "proposed": "Divine", "page": "III.316", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-15.typ", "anchor": "§19 nothing which is appropriate would be omitted [keep CCEL (1845 “which i appropriate”)]", "ccel": "which is appropriate", "1845": "which i appropriate", "proposed": "", "page": "III.344", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-16.typ", "anchor": "§1 note (French): si elle n’avoit point eté instituée de Dieu", "ccel": "eté institutée de", "1845": "eté instituée de", "proposed": "instituée", "page": "III.350", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§26 youth who, after being imbued duly and properly with the rudiments of piety", "ccel": "being embued duly", "1845": "being imbued duly", "proposed": "imbued", "page": "III.375", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§31 all kinds of fishes? (1845 “Matth. iv. 19”, “fishers of men”; CCEL 9:19)", "ccel": "(Matt 9:19; 13:47)", "1845": "(Matth. iv. 19; xiii. 47.)", "proposed": "(Matt 4:19; 13:47)", "page": "III.381", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§25 On hearing the words of Christ, This is my body", "ccel": "Christ, this is my", "1845": "Christ, This is my", "proposed": "This", "page": "III.419", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§32 “Every spirit that confesseth not …” (1 John 4:3) [keep CCEL (1845 “1 John iv. 23”; the chapter has 21 verses)]", "ccel": "(1 John 4:3; 2 John 7)", "1845": "(1 John iv. 23; 2 John ver. 7.)", "proposed": "", "page": "III.432", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-17.typ", "anchor": "§33 neglecting and almost suppressing them [keep CCEL (1845 “suppresing”)]", "ccel": "almost suppressing them", "1845": "almost suppresing them", "proposed": "", "page": "III.432", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-17.typ", "anchor": "§33 the seed which fell among thorns sprang up (1845 “sprang”)", "ccel": "thorns sprung up", "1845": "thorns sprang up", "proposed": "sprang", "page": "III.435", "kind": "d/grammar", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "Sections 14. Those who mutter over the Mass cannot be called priests", "ccel": "mutter over the mass", "1845": "mutter over the Mass", "proposed": "Mass", "page": "III.458", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "Sections 19. the views which ought to be held concerning Baptism and the Lord’s Supper", "ccel": "concerning baptism and", "1845": "concerning Baptism and", "proposed": "Baptism", "page": "III.458", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§1 the way in which the sounder schoolmen at first received", "ccel": "sounder Schoolmen at", "1845": "sounder schoolmen at", "proposed": "schoolmen", "page": "III.458", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§7 While the Supper itself is a gift of God", "ccel": "While the supper itself", "1845": "While the Supper itself", "proposed": "Supper", "page": "III.465", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§9 note (French): ceux qui sont les plus effrontés entre les Papistes", "ccel": "plus effrontées entre", "1845": "plus effrontés entre", "proposed": "effrontés", "page": "III.467", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§14 But what else is done in the Mass than", "ccel": "done in the mass", "1845": "done in the Mass", "proposed": "Mass", "page": "III.472", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "Argument: Impiety of the Popish teachers in attributing more", "ccel": "the popish teachers", "1845": "the Popish teachers", "proposed": "Popish", "page": "III.479", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§23 note: John 2:15; 10:7; Luke 4:17; Mark 7:33 [keep CCEL (1845 “Matth. vii. 33”; Matthew 7 has 29 verses, the spittle and the tongue are Mark 7:33)]", "ccel": "Mark 7:33;", "1845": "Matth. vii. 33;", "proposed": "", "page": "III.503", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-19.typ", "anchor": "§24 and shut the doors of churches?", "ccel": "doors of Churches?", "1845": "doors of churches?", "proposed": "churches", "page": "III.504", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§34 The last of all is Marriage, which", "ccel": "is marriage, which", "1845": "is Marriage, which", "proposed": "Marriage", "page": "III.513", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§34 “I am the true vine, and my Father is the husbandman”", "ccel": "my father is", "1845": "my Father is", "proposed": "Father", "page": "III.514", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "Argument: Next, the three forms of civil government are added", "ccel": "three Forms of", "1845": "three forms of", "proposed": "forms", "page": "III.518", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "Sections 12. Objection, that the lawfulness of War is not taught in Scripture", "ccel": "lawfulness of war is", "1845": "lawfulness of War is", "proposed": "War", "page": "III.519", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "Sections 16. All laws should be just", "ccel": "All Laws should", "1845": "All laws should", "proposed": "laws", "page": "III.519", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "Sections 16. Civil law of Moses; how far in force", "ccel": "Civil Law of Moses", "1845": "Civil law of Moses", "proposed": "law", "page": "III.519", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§4 Augustine: “If Scripture called them gods, to whom the word of God came”", "ccel": "called them Gods,", "1845": "called them gods,", "proposed": "gods", "page": "III.523", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§7 “The kings of the Gentiles exercise lordship over them”", "ccel": "of the gentiles", "1845": "of the Gentiles", "proposed": "Gentiles", "page": "III.526", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§9 defending the honor of Him whose vicegerents they are", "ccel": "honor of him whose", "1845": "honor of Him whose", "proposed": "Him", "page": "III.529", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§10 note: Exod 2:12; Acts 7:24 [keep CCEL (1845 “Acts vii. 21”; Moses strikes the Egyptian in 7:24)]", "ccel": "Exod 2:12; Acts 7:24;", "1845": "Exod. ii. 12; Acts vii. 21;", "proposed": "", "page": "III.532", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-20.typ", "anchor": "§10 note: Prov … 17:15; 17:11; 24:24 [keep CCEL (1845 “xvii. 14”; the text quotes 17:11, “An evil man seeketh only rebellion”, III.533)]", "ccel": "17:15; 17:11; 24:24.]", "1845": "xvii. 15; xvii. 14; xxiv. 24.", "proposed": "", "page": "III.532", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-20.typ", "anchor": "§16 Yet we see that amid this diversity they all tend", "ccel": "amidst this diversity", "1845": "amid this diversity", "proposed": "amid", "page": "III.539", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§19 from the governor to Cæsar’s judgment seat [keep CCEL (1845 “Cesar’s” here; vol. 5 has “Cæsars”, III.149)]", "ccel": "governor to Cæsar’s", "1845": "governor to Cesar’s", "proposed": "", "page": "III.541", "kind": "misprint-1845", "confidence": "medium"}
{"file": "book-4-chapter-20.typ", "anchor": "§21 the passion for litigation prevailed in the church of Corinth", "ccel": "in the Church of Corinth", "1845": "in the church of Corinth", "proposed": "church", "page": "III.543", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§25 raised up by him to punish the people for their iniquity [keep CCEL (1845 “so punish”)]", "ccel": "by him to punish", "1845": "by him so punish", "proposed": "", "page": "III.546", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-20.typ", "anchor": "§26 he will take your daughters to be confectionaries (1 Sam 8:13; 1845 “confectionaries”, the women who make them)", "ccel": "be confectioneries,", "1845": "be confectionaries,", "proposed": "confectionaries", "page": "III.548", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§28 “Who can stretch forth his hand against the Lord’s anointed” (1845 “1 Sam. xxvi. 9-11”; CCEL 24:9–11)", "ccel": "(1 Sam 24:9–11)", "1845": "(1 Sam. xxvi. 9-11.)", "proposed": "(1 Sam 26:9–11)", "page": "III.550", "kind": "d", "confidence": "high"}
```
