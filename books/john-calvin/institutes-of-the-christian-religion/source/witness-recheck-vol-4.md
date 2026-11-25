# Calvin, Institutes, vol. 4 (Book III, chapters 11–25): Classic re-checked against the 1845 printing (Kraken OCR)

Base: `chapters/typ/vol-4/*.typ` in the `wt-institutes` worktree (book-3-chapter-11 … book-3-chapter-25; read only).
Witness: Calvin Translation Society, Edinburgh 1845, our own scans, Kraken OCR with ALTO beside it, page images `pages/p-NNNN.png`.
Book III ch. 11–25 lies wholly in **1845 vol. 2, pp. 300–630** (`work/institutes/vol2/kraken/`, image = printed page + 10,
images 310–640): ch. 11 begins p. 300 (image 310), ch. 25 begins p. 606 and ends p. 630 (image 640, “…to press onward until
he himself shall be all in all.”), where 1845 prints “END OF VOLUME SECOND.” and the printer's imprint; images 641–655 hold no
text of Book III. In the **p.** column **II.n** is a page of 1845 vol. 2 (as in the vol. 2 and vol. 3 reports).
Method (as vols 1–3): every .typ file was aligned word by word with the Kraken text (difflib; main text first, then the
footnotes against the OCR words the main text left over; running heads dropped; line-end hyphens joined). Differences were
filtered for reference style (Roman → Arabic compared as numbers), American spelling and OCR noise; then every remaining
candidate (385 word and 92 reference rows, 32 capital-letter rows, 24 long runs) was read on the page image (line crops from the
ALTO boxes, contact sheets `gr1.png`–`gr6.png` (the 128 grammar rows), `w1.png`, `r1.png`, `r2.png`, `cs1.png`–`cs3.png`, and single crops in
`crops/`). Every reference left unmatched in the OCR was checked against the CCEL text of its own chapter (`refcheck.py`, made
stricter than vol. 3's whole-volume check), and the footnotes were counted page by page against CCEL's (`notepages.py`, ALTO
note zone vs CCEL notes placed through the alignment); every page where the counts differed was read. Only what the image
confirms is listed.
Scripts and raw candidates: `work/institutes/latin/vol4/recheck/` (`align.py`, `filter.py`, `refcheck.py`, `notepages.py`,
`notecount.py`, `crop.py`, `mkbatch.py`, `batch.sh`, `cand.json`, `cand.tsv`, `cand2.tsv`, `cases.tsv`, `residual.txt`,
`grammar_rows.tsv`, `build_report.py`, `apply-input.jsonl`, `manual-edits.json`, `apply_recheck.py`).

**Rule applied (editor, 2026-11-23):** the Classic follows the 1845 print wherever CCEL's wording departs from it, including
CCEL's modernised grammar in Scripture quotations (kind **d/grammar**). Not listed: Arabic reference style, American spelling
(1845 forms: stedfastness, practised, recognising, cognisance, stupify/stupified, sepulchre, meagre, fervour, favour,
hinderance, dependant, unblameable, immoveable, gainsayed, imposters, accepter (of persons)…), CCEL's punctuation around
references, CCEL's word joins, Greek accents. The `proposed` column holds only the replacement words; explanations are in the
anchor and kind columns; an empty `proposed` means no change to the text (misprint-1845). Where a row needs more than one word
changed, or words added or taken out, `proposed` holds the whole replacement snippet and the change is in `manual-edits.json`.

**Kinds:** b (1845 words missing in CCEL), c (CCEL words absent from 1845, as in vol. 2), d (a different word), d/grammar
(CCEL's modernised verb form), d/case (capital letter differs from the print), n (notes), misprint-1845 (the 1845 print is
wrong; CCEL corrects or shares it).

**Counts:** b 2, c 4, d 7, d/case 24, d/grammar 128, misprint-1845 17, n 2 (total 184).

**Systematic check.** No mid-sentence capital like vol-1's “Judgment”: the capital comparison (every aligned word whose
first letter differs in case) gives 32 rows, all single places (25 listed, in 24 rows; the rest are four lib./Lib., one small-capital opening and two
running-head artefacts). The one repeated pattern is again
CCEL's modern verb for the print's -th form, in Scripture quotations, the Fathers quoted (Augustine) and Calvin's own sentences:
128 places (has → hath 107 and one Has → Hath, does → doeth 6 / doth 4, comes → cometh 5, goes → goeth 3, sees → seeth 1,
believes → believeth 1). The print is not uniform: it keeps “has” in places CCEL also has “has” (II.576
“from him who has”), and both “doth” and “doeth” occur, so each row is listed separately. No keying slip recurs; the word
slips are all single (satisfied for *satisfies*, a iota for *an iota*, Rabbis for *Rabbins*, vehemence for *vehemency*, hands
for *hand*, inextinguishable for *unextinguishable*, a dropped “We” and a dropped verse “1”; in the notes arbre for *l’arbre*,
delaisse for *delaissez*). CCEL also adds four things the print does not have: three Scripture references ((Ps 36:9),
(2 Cor 1:20), and (Isa 42:10) inside a quotation) and the gloss “(Eligius)” after Eloy (kind c); and it fills out “(Ps. cvii.)”
as (Ps 107:6, 13, 19) (kind d). Seventeen 1845 misprints (mostly reference numbers) are listed so that nobody “restores” them.

**Also seen, not listed:** CCEL “lib.” for 1845 “Lib.” in Augustine/Ambrose references (II.331, II.337, II.412, II.554);
1845 small capitals at section openings (“I TRUST”); Psalm verses counted from the Hebrew title in 1845 where CCEL gives the
English verse (II.455 Ps. lxii. 9 = Ps 62:8; II.514 Ps. iv. 8 = Ps 4:7); CCEL “Chap 14 s18; Chapter 20 s10” (1845 “Chapter
xiv. s. 18; chap. xx. s. 10”: reference style); ligatures (1845 “œuvres”, “Perseverantiæ”; CCEL “oeuvres”, “Perseverantiae”);
small punctuation (1845 “and, secondly, that”, CCEL “And, secondly that”; 1845 “Calv. Com.)”, CCEL “Calv. Com)”; 1845 “viz.,”
for CCEL “—viz.”); the closing line, 1845 “END OF VOLUME SECOND.” (the end of the 1845 volume) where ours has “END OF BOOK
THREE.” (right for our volume); spellings in the rule above.

**Structural:** no Beveridge footnote is missing in vol. 4 and none is added: the page-by-page note count (`notepages.py`)
matched every 1845 note to a CCEL note (the differing pages were section openings taken for note lines, or note zones the
script could not find; each was read), and the note texts agree apart from the two French rows (n). Every OCR run left
unmatched after both passes was checked: all are references present in CCEL in Arabic form (`refcheck.py`; the ones it
flags are the listed misprints, the Hebrew verse numbers above and OCR misreadings), running heads, signatures and the
imprint. No CCEL line is absent from 1845 and no 1845 line from CCEL; the chapter titles and the Sections lists agree
(capitals apart, listed).


## Book III, chapter 11 — `book-3-chapter-11.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 6. Necessity of this refutation | necessity of this | Necessity of this | Necessity | II.301 | d/case | high |
| §2 the expressions, To be justified in the sight of God, To be justified by faith or by works (italic; two capitals) | God, to be Justified by | God, To be justified by | God, To be justified by | II.302 | d/case | high |
| §4 Eph 1:5, 6 | he has made | he hath made | hath | II.305 | d/grammar | high |
| §5 heaps together many passages of Scripture | of scripture showing | of Scripture showing | Scripture | II.306 | d/case | high |
| §7 by giving Christ; just as such a vessel | Christ; Just as | Christ; just as | just | II.310 | d/case | high |
| §8 the office of Mediator | office of mediator, | office of Mediator, | Mediator | II.311 | d/case | high |
| §9 | Christ, “He has | Christ, “He hath | hath | II.312 | d/grammar | high |
| §10 carnal eating in the supper; and, secondly | supper; And, secondly | supper; and, secondly | and | II.314 | d/case | high |
| §12 | who “has | who “hath | hath | II.319 | d/grammar | high |
| §12 John 17:19 | he has deposited | he hath deposited | hath | II.320 | d/grammar | high |
| §13 | he has whereof | he hath whereof | hath | II.321 | d/grammar | high |
| §15 Heb 11:6 | that comes | that cometh | cometh | II.323 | d/grammar | high |
| §17 Rom 10:5, 6 | which does | which doeth | doeth | II.325 | d/grammar | high |
| §17 Rom 10:5, 6 | God has raised | God hath raised | hath | II.325 | d/grammar | high |
| §18 Gal 3:11, 12 | but, The man that does | but, The man that doeth | doeth | II.325 | d/grammar | high |
| §19 Gal 3:12 | “The man that does | “The man that doeth | doeth | II.327 | d/grammar | high |
| §19 Gal 3:21, 22 | Scripture has | Scripture hath | hath | II.328 | d/grammar | high |
| §21 | Lord has | Lord hath | hath | II.330 | d/grammar | high |
| §22 | and has | and hath | hath | II.330 | d/grammar | high |
| §22 | embassy: “He has | embassy: “He hath | hath | II.330 | d/grammar | high |
| §22 “by him all that believe are justified” [keep CCEL (1845 Acts xii. here, xiii. at II.305)] | (Acts 13:38, 39). Thus | (Acts xii. 38, 39.) Thus |  | II.330 | misprint-1845 | - |

## Book III, chapter 12 — `book-3-chapter-12.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 4. Another engine overthrowing the righteousness of works, viz., a serious examination | A serious examination | a serious examination | a | II.333 | d/case | high |
| §5 “Who can bring a clean thing out of an unclean? not one” [keep CCEL (the verse is Job 14:4)] | (Job 14:4) | (Job xiv. 5.) |  | II.339 | misprint-1845 | - |
| §6 Isa 66:2 Again, “Thus saith the high and lofty One” | 66:2). again, | 66:2). Again, | Again | II.340 | d/case | high |

## Book III, chapter 13 — `book-3-chapter-13.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 “the justifier of him which believeth in Jesus” [keep CCEL (the verse is Rom 3:26)] | Jesus,” (Rom 3:26). Observe, | Jesus,” (Rom. iii. 25.) Observe, |  | II.344 | misprint-1845 | - |
| §2 1 Pet 2:9 | who has | who hath | hath | II.346 | d/grammar | high |
| §3 (Calvin's sentence: no man ever fully satisfies it by works) | ever fully satisfied it | ever fully satisfies it | satisfies | II.347 | d | high |
| §4 1 Cor 2:16 | ‘Who has | ‘Who hath | hath | II.348 | d/grammar | high |
| §5 our souls cannot have peace | our Souls cannot | our souls cannot | souls | II.350 | d/case | high |

## Book III, chapter 14 — `book-3-chapter-14.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 | that does | that doeth | doeth | II.353 | d/grammar | high |
| §1 not an iota of good will be found | not a iota | not an iota | an | II.353 | d | high |
| §5 Eph 2:4 | sins, has | sins, hath | hath | II.356 | d/grammar | high |
| §5 Job 41:11 | “Who has prevented | “Who hath prevented | hath | II.356 | d/grammar | high |
| §5 Eph 2:10 | God has before | God hath before | hath | II.356 | d/grammar | high |
| §5 | God “has | God “hath | hath | II.356 | d/grammar | high |
| §8 the order which Scripture sets before us | which scripture sets | which Scripture sets | Scripture | II.360 | d/case | high |
| §15 Isa 1:12 | “Who has required | “Who hath required | hath | II.367 | d/grammar | high |
| §15 matter for these indolent Rabbins | indolent Rabbis to | indolent Rabbins to | Rabbins | II.367 | d | medium |
| §17 | God has set | God hath set | hath | II.369 | d/grammar | high |

## Book III, chapter 15 — `book-3-chapter-15.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §4 | that has shall | that hath shall | hath | II.379 | d/grammar | high |
| §4 Isa 55:1 | that has no money, | that hath no money, | hath | II.379 | d/grammar | high |
| §5 | God “has chosen | God “hath chosen | hath | II.379 | d/grammar | high |
| §6 1 John 5:12 | that has the | that hath the | hath | II.380 | d/grammar | high |
| §6 1 John 5:12 | Son has | Son hath | hath | II.380 | d/grammar | high |
| §6 1 John 5:12 | that has not | that hath not | hath | II.380 | d/grammar | high |
| §6 1 John 5:12 | God has not | God hath not | hath | II.380 | d/grammar | high |
| §6 | God “has raised | God “hath raised | hath | II.381 | d/grammar | high |
| §6 | “Who has | “Who hath | hath | II.381 | d/grammar | high |
| §6 | and has translated | and hath translated | hath | II.381 | d/grammar | high |
| §7 Eph 2:10 | God has before | God hath before | hath | II.382 | d/grammar | high |
| §8 | God does | God doth | doth | II.383 | d/grammar | high |

## Book III, chapter 16 — `book-3-chapter-16.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 | God has appeared | God hath appeared | hath | II.387 | d/grammar | high |
| §2 | God has not appointed | God hath not appointed | hath | II.388 | d/grammar | high |
| §2 | “God has | “God hath | hath | II.388 | d/grammar | high |
| §2 | whosoever does | whosoever doeth | doeth | II.388 | d/grammar | high |
| §2 | and has | and hath | hath | II.388 | d/grammar | high |
| §2 | that has | that hath | hath | II.388 | d/grammar | high |

## Book III, chapter 17 — `book-3-chapter-17.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 “which if a man do, he shall live in them” [keep CCEL (the verse is Ezek 20:11)] | (Lev 18:5; Ezek 20:11) | (Levit. xviii. 5; Ezek. xx. 10,) |  | II.395 | misprint-1845 | - |
| §5 | hands has he recompensed me,” | hands hath he recompensed me,” | hath | II.399 | d/grammar | high |
| §7 | sun goes | sun goeth | goeth | II.400 | d/grammar | high |
| §10 | that has | that hath | hath | II.405 | d/grammar | high |
| note (French): comme le fruict à l’arbre | le fruict à arbre.” | le fruict à l’arbre.” | l’arbre | II.405 | n | high |
| §11 Jas 2:14 | “What does | “What doth | doth | II.407 | d/grammar | high |
| §11 Jas 2:14 | he has faith, | he hath faith, | hath | II.407 | d/grammar | high |
| §14 | hands has he recompensed me. | hands hath he recompensed me. | hath | II.410 | d/grammar | high |
| §15 | that “has | that “hath | hath | II.411 | d/grammar | high |
| §15 Ezek 18:9, 21 | and has | and hath | hath | II.412 | d/grammar | high |

## Book III, chapter 18 — `book-3-chapter-18.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 | he has done, | he hath done, | hath | II.414 | d/grammar | high |
| §1 | that does | that doeth | doeth | II.414 | d/grammar | high |
| §1 | which has begun | which hath begun | hath | II.415 | d/grammar | high |
| §6 Prov 19:17 | that has | that hath | hath | II.421 | d/grammar | high |
| §7 | who has | who hath | hath | II.423 | d/grammar | high |
| §10 in the preaching of the Gospel. My readers | of the gospel. My | of the Gospel. My | Gospel | II.426 | d/case | high |

## Book III, chapter 19 — `book-3-chapter-19.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 1. … Necessity of vindicating it | liberty. necessity of | liberty. Necessity of | Necessity | II.429 | d/case | high |
| §3 | “Christ has | “Christ hath | hath | II.431 | d/grammar | high |
| §9 “are in their feasts” [keep CCEL (the words are Isa 5:12; CCEL also adds Amos 6:4, the ivory beds)] | (Amos 6:4, 6; Isa 5:8, 12) | (Amos vi. 6; Is. v. 8, 10.) |  | II.437 | misprint-1845 | medium |
| §11 Elsewhere he says, “Take heed lest by any means” | edification.” elsewhere he | edification.” Elsewhere he | Elsewhere | II.439 | d/case | high |
| §15 as being agreeable to the word of God | to the Word of God, and those | to the word of God, and those | word | II.443 | d/case | high |

## Book III, chapter 20 — `book-3-chapter-20.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 24. 4. Fourth papistical argument | Fourth Papistical argument | Fourth papistical argument | papistical | II.448 | d/case | high |
| §1 see light in his light. [CCEL adds the reference; 1845 has none] | light in his light (Ps 36:9). But | light in his light. But | light in his light. But | II.451 | c | medium |
| §6 less fervour and vehemency of desire | and vehemence of | and vehemency of | vehemency | II.458 | d | medium |
| §9 “to cleanse us from all unrighteousness” [keep CCEL (the verse is 1 John 1:9)] | (1 John 1:9) | (1 John i. 5.) |  | II.462 | misprint-1845 | - |
| §15 (Ps. cvii.): CCEL adds verse numbers the print does not give | faith (Ps 107:6, 13, 19). For | faith (Ps. cvii.) For | faith (Ps 107). For | II.473 | d | medium |
| §17 in him amen;” that is [CCEL adds the reference; 1845 has none] | amen;” (2 Cor 1:20), that is | amen;” that is | amen;” that is | II.478 | c | medium |
| §18 that we may be heard in his person; and, secondly | person; And secondly, | person; and, secondly, | and | II.478 | d/case | high |
| §20 “who also maketh intercession for us” [keep CCEL (the verse is Rom 8:34)] | (Rom 8:34) | (Rom. viii. 32.) |  | II.480 | misprint-1845 | - |
| §20 (August. in Ps. xciv.) We imagine not that he throws himself | in Ps 94) imagine | in Ps. xciv.) We imagine | in Ps 94) We imagine | II.481 | b | high |
| §22 calling upon Eloy or Medard [CCEL adds “(Eligius)”; 1845 has none] | Eloy (Eligius) or Medard | Eloy or Medard | Eloy or Medard | II.484 | c | high |
| §22 Sancte Petre, ora pro nobis [keep CCEL (Latin vocative Sancte; 1845 Sancti)] | #emph[Sancte Petre | Sancti Petre (italic) |  | II.484 | misprint-1845 | - |
| §25 “for David’s sake,” (Ps. cxxxii. 1, 10; see Calv. Com.) | (Ps 132:10; see | (Ps. cxxxii. 1, 10; see | (Ps 132:1, 10; see | II.489 | b | medium |
| §28 “Sing unto the Lord a new song.” [CCEL adds the reference inside the quotation; 1845 has none] | a new song (Isa 42:10).” In | a new song.” In | a new song.” In | II.493 | c | medium |
| §32 he commends spiritual songs | spiritual Songs, | spiritual songs, | songs | II.500 | d/case | high |
| §34 (Plato, Alcibiad. 2) [keep CCEL (the prayer is in the Second Alcibiades; 1845 “Alcibid. i.”)] | Alcibiad. 2) | Alcibid. i.) |  | II.503 | misprint-1845 | medium |
| §36 God surpasses all men in goodness and mercy [keep CCEL (the verse is Isa 63:16)] | mercy (Isa 63:16) | mercy, (Isaiah lxiii. 18.) |  | II.505 | misprint-1845 | - |
| §38 to stretch out our hand, and give assistance | out our hands and | out our hand, and | hand | II.506 | d | high |
| Sections 47. their confidence founded entirely on His nature | entirely on his nature. | entirely on His nature. | His | II.523 | d/case | high |

## Book III, chapter 21 — `book-3-chapter-21.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 John 10:26 | Father has taken | Father hath taken | hath | II.530 | d/grammar | high |
| §5 Ps 100:3 | that has | that hath | hath | II.536 | d/grammar | high |
| §5 Ps 33:12 | he has chosen | he hath chosen | hath | II.536 | d/grammar | high |
| §5 1 Sam 12:22 | it has pleased | it hath pleased | hath | II.536 | d/grammar | high |
| §6 Ps 147:20 | “He has | “He hath | hath | II.538 | d/grammar | high |
| §7 | Father has connected | Father hath connected | hath | II.538 | d/grammar | high |

## Book III, chapter 22 — `book-3-chapter-22.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 | he, “has | he, “hath | hath | II.544 | d/grammar | high |
| §3 2 Tim 1:9 | “Who has called | “Who hath called | hath | II.545 | d/grammar | high |
| §3 Eph 1:9 | he has purposed | he hath purposed | hath | II.545 | d/grammar | high |
| §3 “before the world began” [keep CCEL (the verse is 2 Tim 1:9)] | (2 Tim 1:9) | (1 Tim. ii. 9.) |  | II.545 | misprint-1845 | - |
| §3 Rom 11:35 | “Who has first | “Who hath first | hath | II.546 | d/grammar | high |
| §7 John 6:37, 39 | which has sent me, that of all which he has given me I should lose nothing,” | which hath sent me, that of all which he has given me I should lose nothing,” | hath | II.550 | d/grammar | high |
| §7 John 6:37, 39 | he has given me I should lose nothing,” | he hath given me I should lose nothing,” | hath | II.550 | d/grammar | high |
| §7 | which has sent me draw | which hath sent me draw | hath | II.551 | d/grammar | high |
| §7 John 6:44, 45 | that has | that hath | hath | II.551 | d/grammar | high |
| §7 John 6:44, 45 | Father comes | Father cometh | cometh | II.551 | d/grammar | high |
| §7 | he has chosen them, | he hath chosen them, | hath | II.551 | d/grammar | high |
| §10 In those again who display their petulance | those Again who | those again who | again | II.554 | d/case | high |
| §10 | Father “has | Father “hath | hath | II.556 | d/grammar | high |
| §10 Eph 1:3, 4 | he has chosen us | he hath chosen us | hath | II.556 | d/grammar | high |
| §10 John 6:46 | man has | man hath | hath | II.557 | d/grammar | high |
| §10 | which has sent me, that of all which he has given me I should lose nothing;” | which hath sent me, that of all which he has given me I should lose nothing;” | hath | II.557 | d/grammar | high |
| §10 | he has given me I should lose nothing;” | he hath given me I should lose nothing;” | hath | II.557 | d/grammar | high |
| §10 John 6:39, 40 | which sees | which seeth | seeth | II.557 | d/grammar | high |
| §10 John 6:39, 40 | and believes | and believeth | believeth | II.557 | d/grammar | high |
| §11 Rom 9:18 | God has mercy | God hath mercy | hath | II.558 | d/grammar | high |

## Book III, chapter 23 — `book-3-chapter-23.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Matt 15:13 | Father has not planted | Father hath not planted | hath | II.560 | d/grammar | high |
| note: This is taken from August. de Gen. cont. Manich. [keep CCEL (1845 “Auguste Dein Gen.”)] | August. de Gen. cont | Auguste Dein Gen. cont |  | II.562 | misprint-1845 | - |
| §2 held in detestation by us [keep CCEL (1845 “destesta-tion”)] | held in detestation by | held in destestation by |  | II.563 | misprint-1845 | - |
| §4 Rom 9:20, 21 | thus? Has | thus? Hath | Hath | II.564 | d/grammar | high |
| note (French): mais plustost delaissez | plustost delaisse;” | plustost delaissez;” | delaissez | II.565 | n | high |
| §6 Prov 16:4 | Lord has made | Lord hath made | hath | II.567 | d/grammar | high |
| §11 | “God has | “God hath | hath | II.573 | d/grammar | high |
| §11 Rom 11:32, 35 | “who has | “who hath | hath | II.573 | d/grammar | high |
| §13 | God has not | God hath not | hath | II.575 | d/grammar | high |
| §13 1 Thess 4:4, 7 | God has before | God hath before | hath | II.575 | d/grammar | high |
| §13 Matt 13:9 | “Who has | “Who hath | hath | II.575 | d/grammar | high |
| §13 | Who has known | Who hath known | hath | II.575 | d/grammar | high |
| §13 | whoso has | whoso hath | hath | II.576 | d/grammar | high |
| §13 | who has ears if | who hath ears if | hath | II.576 | d/grammar | high |
| §13 | he has not | he hath not | hath | II.576 | d/grammar | high |
| §13 | who has ears to | who hath ears to | hath | II.577 | d/grammar | high |
| §14 | (who has | (who hath | hath | II.577 | d/grammar | high |
| §14 | he has pleased | he hath pleased | hath | II.577 | d/grammar | high |
| §14 “Because we know not who belongs to the number” | omitted: “because we | omitted: “Because we | Because | II.577 | d/case | high |

## Book III, chapter 24 — `book-3-chapter-24.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 John 6:46 | man has | man hath | hath | II.581 | d/grammar | high |
| §1 John 6:46 | he has seen | he hath seen | hath | II.581 | d/grammar | high |
| §1 John 6:44 | which has sent | which hath sent | hath | II.581 | d/grammar | high |
| §1 | learned comes, | learned cometh, | cometh | II.581 | d/grammar | high |
| §1 | who has learned of | who hath learned of | hath | II.581 | d/grammar | high |
| §1 | that has heard | that hath heard | hath | II.581 | d/grammar | high |
| §1 | Father comes | Father cometh | cometh | II.581 | d/grammar | high |
| §2 1 John 3:24 | he has given us,” | he hath given us,” | hath | II.583 | d/grammar | high |
| §2 Abraham … to be his friend [keep CCEL (the verse is Isa 41:8)] | (Isa 41:8) | (Isaiah xxiv. 3;) |  | II.583 | misprint-1845 | - |
| §3 | Lord has | Lord hath | hath | II.584 | d/grammar | high |
| §6 John 6:37–39, 17 | he has delivered | he hath delivered | hath | II.588 | d/grammar | high |
| §6 | that comes | that cometh | cometh | II.589 | d/grammar | high |
| §6 John 6:37, 39 | he has given me | he hath given me | hath | II.589 | d/grammar | high |
| §6 Matt 15:13 | Father has not | Father hath not | hath | II.589 | d/grammar | high |
| §6 Phil 1:6 | who has begun | who hath begun | hath | II.589 | d/grammar | high |
| §7 | Father has given | Father hath given | hath | II.590 | d/grammar | high |
| §10 | “You has | “You hath | hath | II.594 | d/grammar | high |
| §13 | that has rebelled | that hath rebelled | hath | II.597 | d/grammar | high |
| §13 Ezek 2:3, 6 | which has eyes | which hath eyes | hath | II.597 | d/grammar | high |
| §14 John 12:37, 38 | who has believed | who hath believed | hath | II.599 | d/grammar | high |
| §15 Ezek 18:23 “Have I any pleasure at all” | is, “have I any | is, “Have I any | Have | II.600 | d/case | high |
| §16 Deut 4:7 | who has God | who hath God | hath | II.601 | d/grammar | high |
| §16 | words, “God has | words, “God hath | hath | II.602 | d/grammar | high |
| §16 Ps 115:3 | he has done | he hath done | hath | II.602 | d/grammar | high |
| §16 Ps 115:3 | he has pleased,” | he hath pleased,” | hath | II.602 | d/grammar | high |
| §16 (Ps 115:3). We must, therefore, expound | 115:3). we must, | 115:3). We must, | We | II.602 | d/case | high |
| §17 “unto a rebellious people” [keep CCEL (the verse is Isa 65:2)] | people,” (Isa 65:2) | people,” (Isa. lxv. 1,) |  | II.604 | misprint-1845 | - |
| §17 | passage, “God has | passage, “God hath | hath | II.605 | d/grammar | high |

## Book III, chapter 25 — `book-3-chapter-25.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 | gospel, has, | gospel, hath, | hath | II.607 | d/grammar | high |
| §5 | that goes upward, | that goeth upward, | goeth | II.614 | d/grammar | high |
| §5 | that goes downward | that goeth downward | goeth | II.614 | d/grammar | high |
| §6 the divinity is most refulgent | most Refulgent and | most refulgent, and | refulgent | II.617 | d/case | high |
| §7 2 Cor 5:10 | he has done, | he hath done, | hath | II.618 | d/grammar | high |
| §7 “every knee shall bow to me” [keep CCEL (the verse is Isa 45:23)] | Isa 45:23) | Isa. xix. 18;) |  | II.619 | misprint-1845 | - |
| §8 1 Cor 6:13, 14 | God has both | God hath both | hath | II.621 | d/grammar | high |
| §8 John 6:39 | which has | which hath | hath | II.623 | d/grammar | high |
| §8 John 6:39 | he has given | he hath given | hath | II.623 | d/grammar | high |
| §9 (John 11:25). Is it to revive the whole | 11:25). is it | 11:25). Is it | Is | II.624 | d/case | high |
| §10 1 John 3:2 | it does | it doth | doth | II.626 | d/grammar | high |
| §10 “Ye are our glory and our joy” [keep CCEL (the words are 1 Thess 2:20; 1845 “2 Thess. ii. 19”)] | (1 Thess 2:20) | (2 Thess. ii. 19,) |  | II.627 | misprint-1845 | - |
| §12 Isa 30:33 | he has made | he hath made | hath | II.629 | d/grammar | high |
| §12 Isa 30:33 | brimstone, does | brimstone, doth | doth | II.629 | d/grammar | high |
| §12 Matt 8:12 … inextinguishable fire (1845 unextinguishable) | teeth, inextinguishable fire | teeth, unextinguishable fire | unextinguishable | II.629 | d | high |

## Findings (one JSON line each)

```
{"file": "book-3-chapter-11.typ", "anchor": "Sections 6. Necessity of this refutation", "ccel": "necessity of this", "1845": "Necessity of this", "proposed": "Necessity", "page": "II.301", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§2 the expressions, To be justified in the sight of God, To be justified by faith or by works (italic; two capitals)", "ccel": "God, to be Justified by", "1845": "God, To be justified by", "proposed": "God, To be justified by", "page": "II.302", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§4 Eph 1:5, 6", "ccel": "he has made", "1845": "he hath made", "proposed": "hath", "page": "II.305", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§5 heaps together many passages of Scripture", "ccel": "of scripture showing", "1845": "of Scripture showing", "proposed": "Scripture", "page": "II.306", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§7 by giving Christ; just as such a vessel", "ccel": "Christ; Just as", "1845": "Christ; just as", "proposed": "just", "page": "II.310", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§8 the office of Mediator", "ccel": "office of mediator,", "1845": "office of Mediator,", "proposed": "Mediator", "page": "II.311", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§9", "ccel": "Christ, “He has", "1845": "Christ, “He hath", "proposed": "hath", "page": "II.312", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§10 carnal eating in the supper; and, secondly", "ccel": "supper; And, secondly", "1845": "supper; and, secondly", "proposed": "and", "page": "II.314", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§12", "ccel": "who “has", "1845": "who “hath", "proposed": "hath", "page": "II.319", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§12 John 17:19", "ccel": "he has deposited", "1845": "he hath deposited", "proposed": "hath", "page": "II.320", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§13", "ccel": "he has whereof", "1845": "he hath whereof", "proposed": "hath", "page": "II.321", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§15 Heb 11:6", "ccel": "that comes", "1845": "that cometh", "proposed": "cometh", "page": "II.323", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§17 Rom 10:5, 6", "ccel": "which does", "1845": "which doeth", "proposed": "doeth", "page": "II.325", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§17 Rom 10:5, 6", "ccel": "God has raised", "1845": "God hath raised", "proposed": "hath", "page": "II.325", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§18 Gal 3:11, 12", "ccel": "but, The man that does", "1845": "but, The man that doeth", "proposed": "doeth", "page": "II.325", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§19 Gal 3:12", "ccel": "“The man that does", "1845": "“The man that doeth", "proposed": "doeth", "page": "II.327", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§19 Gal 3:21, 22", "ccel": "Scripture has", "1845": "Scripture hath", "proposed": "hath", "page": "II.328", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§21", "ccel": "Lord has", "1845": "Lord hath", "proposed": "hath", "page": "II.330", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§22", "ccel": "and has", "1845": "and hath", "proposed": "hath", "page": "II.330", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§22", "ccel": "embassy: “He has", "1845": "embassy: “He hath", "proposed": "hath", "page": "II.330", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§22 “by him all that believe are justified” [keep CCEL (1845 Acts xii. here, xiii. at II.305)]", "ccel": "(Acts 13:38, 39). Thus", "1845": "(Acts xii. 38, 39.) Thus", "proposed": "", "page": "II.330", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-12.typ", "anchor": "Sections 4. Another engine overthrowing the righteousness of works, viz., a serious examination", "ccel": "A serious examination", "1845": "a serious examination", "proposed": "a", "page": "II.333", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-12.typ", "anchor": "§5 “Who can bring a clean thing out of an unclean? not one” [keep CCEL (the verse is Job 14:4)]", "ccel": "(Job 14:4)", "1845": "(Job xiv. 5.)", "proposed": "", "page": "II.339", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-12.typ", "anchor": "§6 Isa 66:2 Again, “Thus saith the high and lofty One”", "ccel": "66:2). again,", "1845": "66:2). Again,", "proposed": "Again", "page": "II.340", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§1 “the justifier of him which believeth in Jesus” [keep CCEL (the verse is Rom 3:26)]", "ccel": "Jesus,” (Rom 3:26). Observe,", "1845": "Jesus,” (Rom. iii. 25.) Observe,", "proposed": "", "page": "II.344", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-13.typ", "anchor": "§2 1 Pet 2:9", "ccel": "who has", "1845": "who hath", "proposed": "hath", "page": "II.346", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§3 (Calvin's sentence: no man ever fully satisfies it by works)", "ccel": "ever fully satisfied it", "1845": "ever fully satisfies it", "proposed": "satisfies", "page": "II.347", "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§4 1 Cor 2:16", "ccel": "‘Who has", "1845": "‘Who hath", "proposed": "hath", "page": "II.348", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§5 our souls cannot have peace", "ccel": "our Souls cannot", "1845": "our souls cannot", "proposed": "souls", "page": "II.350", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§1", "ccel": "that does", "1845": "that doeth", "proposed": "doeth", "page": "II.353", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§1 not an iota of good will be found", "ccel": "not a iota", "1845": "not an iota", "proposed": "an", "page": "II.353", "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§5 Eph 2:4", "ccel": "sins, has", "1845": "sins, hath", "proposed": "hath", "page": "II.356", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§5 Job 41:11", "ccel": "“Who has prevented", "1845": "“Who hath prevented", "proposed": "hath", "page": "II.356", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§5 Eph 2:10", "ccel": "God has before", "1845": "God hath before", "proposed": "hath", "page": "II.356", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§5", "ccel": "God “has", "1845": "God “hath", "proposed": "hath", "page": "II.356", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§8 the order which Scripture sets before us", "ccel": "which scripture sets", "1845": "which Scripture sets", "proposed": "Scripture", "page": "II.360", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§15 Isa 1:12", "ccel": "“Who has required", "1845": "“Who hath required", "proposed": "hath", "page": "II.367", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§15 matter for these indolent Rabbins", "ccel": "indolent Rabbis to", "1845": "indolent Rabbins to", "proposed": "Rabbins", "page": "II.367", "kind": "d", "confidence": "medium"}
{"file": "book-3-chapter-14.typ", "anchor": "§17", "ccel": "God has set", "1845": "God hath set", "proposed": "hath", "page": "II.369", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§4", "ccel": "that has shall", "1845": "that hath shall", "proposed": "hath", "page": "II.379", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§4 Isa 55:1", "ccel": "that has no money,", "1845": "that hath no money,", "proposed": "hath", "page": "II.379", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§5", "ccel": "God “has chosen", "1845": "God “hath chosen", "proposed": "hath", "page": "II.379", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6 1 John 5:12", "ccel": "that has the", "1845": "that hath the", "proposed": "hath", "page": "II.380", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6 1 John 5:12", "ccel": "Son has", "1845": "Son hath", "proposed": "hath", "page": "II.380", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6 1 John 5:12", "ccel": "that has not", "1845": "that hath not", "proposed": "hath", "page": "II.380", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6 1 John 5:12", "ccel": "God has not", "1845": "God hath not", "proposed": "hath", "page": "II.380", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6", "ccel": "God “has raised", "1845": "God “hath raised", "proposed": "hath", "page": "II.381", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6", "ccel": "“Who has", "1845": "“Who hath", "proposed": "hath", "page": "II.381", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6", "ccel": "and has translated", "1845": "and hath translated", "proposed": "hath", "page": "II.381", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§7 Eph 2:10", "ccel": "God has before", "1845": "God hath before", "proposed": "hath", "page": "II.382", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§8", "ccel": "God does", "1845": "God doth", "proposed": "doth", "page": "II.383", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§2", "ccel": "God has appeared", "1845": "God hath appeared", "proposed": "hath", "page": "II.387", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§2", "ccel": "God has not appointed", "1845": "God hath not appointed", "proposed": "hath", "page": "II.388", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§2", "ccel": "“God has", "1845": "“God hath", "proposed": "hath", "page": "II.388", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§2", "ccel": "whosoever does", "1845": "whosoever doeth", "proposed": "doeth", "page": "II.388", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§2", "ccel": "and has", "1845": "and hath", "proposed": "hath", "page": "II.388", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§2", "ccel": "that has", "1845": "that hath", "proposed": "hath", "page": "II.388", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§3 “which if a man do, he shall live in them” [keep CCEL (the verse is Ezek 20:11)]", "ccel": "(Lev 18:5; Ezek 20:11)", "1845": "(Levit. xviii. 5; Ezek. xx. 10,)", "proposed": "", "page": "II.395", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-17.typ", "anchor": "§5", "ccel": "hands has he recompensed me,”", "1845": "hands hath he recompensed me,”", "proposed": "hath", "page": "II.399", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§7", "ccel": "sun goes", "1845": "sun goeth", "proposed": "goeth", "page": "II.400", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§10", "ccel": "that has", "1845": "that hath", "proposed": "hath", "page": "II.405", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "note (French): comme le fruict à l’arbre", "ccel": "le fruict à arbre.”", "1845": "le fruict à l’arbre.”", "proposed": "l’arbre", "page": "II.405", "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§11 Jas 2:14", "ccel": "“What does", "1845": "“What doth", "proposed": "doth", "page": "II.407", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§11 Jas 2:14", "ccel": "he has faith,", "1845": "he hath faith,", "proposed": "hath", "page": "II.407", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§14", "ccel": "hands has he recompensed me.", "1845": "hands hath he recompensed me.", "proposed": "hath", "page": "II.410", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§15", "ccel": "that “has", "1845": "that “hath", "proposed": "hath", "page": "II.411", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§15 Ezek 18:9, 21", "ccel": "and has", "1845": "and hath", "proposed": "hath", "page": "II.412", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§1", "ccel": "he has done,", "1845": "he hath done,", "proposed": "hath", "page": "II.414", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§1", "ccel": "that does", "1845": "that doeth", "proposed": "doeth", "page": "II.414", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§1", "ccel": "which has begun", "1845": "which hath begun", "proposed": "hath", "page": "II.415", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§6 Prov 19:17", "ccel": "that has", "1845": "that hath", "proposed": "hath", "page": "II.421", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§7", "ccel": "who has", "1845": "who hath", "proposed": "hath", "page": "II.423", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§10 in the preaching of the Gospel. My readers", "ccel": "of the gospel. My", "1845": "of the Gospel. My", "proposed": "Gospel", "page": "II.426", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "Sections 1. … Necessity of vindicating it", "ccel": "liberty. necessity of", "1845": "liberty. Necessity of", "proposed": "Necessity", "page": "II.429", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§3", "ccel": "“Christ has", "1845": "“Christ hath", "proposed": "hath", "page": "II.431", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§9 “are in their feasts” [keep CCEL (the words are Isa 5:12; CCEL also adds Amos 6:4, the ivory beds)]", "ccel": "(Amos 6:4, 6; Isa 5:8, 12)", "1845": "(Amos vi. 6; Is. v. 8, 10.)", "proposed": "", "page": "II.437", "kind": "misprint-1845", "confidence": "medium"}
{"file": "book-3-chapter-19.typ", "anchor": "§11 Elsewhere he says, “Take heed lest by any means”", "ccel": "edification.” elsewhere he", "1845": "edification.” Elsewhere he", "proposed": "Elsewhere", "page": "II.439", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§15 as being agreeable to the word of God", "ccel": "to the Word of God, and those", "1845": "to the word of God, and those", "proposed": "word", "page": "II.443", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "Sections 24. 4. Fourth papistical argument", "ccel": "Fourth Papistical argument", "1845": "Fourth papistical argument", "proposed": "papistical", "page": "II.448", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§1 see light in his light. [CCEL adds the reference; 1845 has none]", "ccel": "light in his light (Ps 36:9). But", "1845": "light in his light. But", "proposed": "light in his light. But", "page": "II.451", "kind": "c", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§6 less fervour and vehemency of desire", "ccel": "and vehemence of", "1845": "and vehemency of", "proposed": "vehemency", "page": "II.458", "kind": "d", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§9 “to cleanse us from all unrighteousness” [keep CCEL (the verse is 1 John 1:9)]", "ccel": "(1 John 1:9)", "1845": "(1 John i. 5.)", "proposed": "", "page": "II.462", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-20.typ", "anchor": "§15 (Ps. cvii.): CCEL adds verse numbers the print does not give", "ccel": "faith (Ps 107:6, 13, 19). For", "1845": "faith (Ps. cvii.) For", "proposed": "faith (Ps 107). For", "page": "II.473", "kind": "d", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§17 in him amen;” that is [CCEL adds the reference; 1845 has none]", "ccel": "amen;” (2 Cor 1:20), that is", "1845": "amen;” that is", "proposed": "amen;” that is", "page": "II.478", "kind": "c", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§18 that we may be heard in his person; and, secondly", "ccel": "person; And secondly,", "1845": "person; and, secondly,", "proposed": "and", "page": "II.478", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§20 “who also maketh intercession for us” [keep CCEL (the verse is Rom 8:34)]", "ccel": "(Rom 8:34)", "1845": "(Rom. viii. 32.)", "proposed": "", "page": "II.480", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-20.typ", "anchor": "§20 (August. in Ps. xciv.) We imagine not that he throws himself", "ccel": "in Ps 94) imagine", "1845": "in Ps. xciv.) We imagine", "proposed": "in Ps 94) We imagine", "page": "II.481", "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§22 calling upon Eloy or Medard [CCEL adds “(Eligius)”; 1845 has none]", "ccel": "Eloy (Eligius) or Medard", "1845": "Eloy or Medard", "proposed": "Eloy or Medard", "page": "II.484", "kind": "c", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§22 Sancte Petre, ora pro nobis [keep CCEL (Latin vocative Sancte; 1845 Sancti)]", "ccel": "#emph[Sancte Petre", "1845": "Sancti Petre (italic)", "proposed": "", "page": "II.484", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-20.typ", "anchor": "§25 “for David’s sake,” (Ps. cxxxii. 1, 10; see Calv. Com.)", "ccel": "(Ps 132:10; see", "1845": "(Ps. cxxxii. 1, 10; see", "proposed": "(Ps 132:1, 10; see", "page": "II.489", "kind": "b", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§28 “Sing unto the Lord a new song.” [CCEL adds the reference inside the quotation; 1845 has none]", "ccel": "a new song (Isa 42:10).” In", "1845": "a new song.” In", "proposed": "a new song.” In", "page": "II.493", "kind": "c", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§32 he commends spiritual songs", "ccel": "spiritual Songs,", "1845": "spiritual songs,", "proposed": "songs", "page": "II.500", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§34 (Plato, Alcibiad. 2) [keep CCEL (the prayer is in the Second Alcibiades; 1845 “Alcibid. i.”)]", "ccel": "Alcibiad. 2)", "1845": "Alcibid. i.)", "proposed": "", "page": "II.503", "kind": "misprint-1845", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§36 God surpasses all men in goodness and mercy [keep CCEL (the verse is Isa 63:16)]", "ccel": "mercy (Isa 63:16)", "1845": "mercy, (Isaiah lxiii. 18.)", "proposed": "", "page": "II.505", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-20.typ", "anchor": "§38 to stretch out our hand, and give assistance", "ccel": "out our hands and", "1845": "out our hand, and", "proposed": "hand", "page": "II.506", "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "Sections 47. their confidence founded entirely on His nature", "ccel": "entirely on his nature.", "1845": "entirely on His nature.", "proposed": "His", "page": "II.523", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§1 John 10:26", "ccel": "Father has taken", "1845": "Father hath taken", "proposed": "hath", "page": "II.530", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§5 Ps 100:3", "ccel": "that has", "1845": "that hath", "proposed": "hath", "page": "II.536", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§5 Ps 33:12", "ccel": "he has chosen", "1845": "he hath chosen", "proposed": "hath", "page": "II.536", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§5 1 Sam 12:22", "ccel": "it has pleased", "1845": "it hath pleased", "proposed": "hath", "page": "II.536", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§6 Ps 147:20", "ccel": "“He has", "1845": "“He hath", "proposed": "hath", "page": "II.538", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§7", "ccel": "Father has connected", "1845": "Father hath connected", "proposed": "hath", "page": "II.538", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§1", "ccel": "he, “has", "1845": "he, “hath", "proposed": "hath", "page": "II.544", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§3 2 Tim 1:9", "ccel": "“Who has called", "1845": "“Who hath called", "proposed": "hath", "page": "II.545", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§3 Eph 1:9", "ccel": "he has purposed", "1845": "he hath purposed", "proposed": "hath", "page": "II.545", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§3 “before the world began” [keep CCEL (the verse is 2 Tim 1:9)]", "ccel": "(2 Tim 1:9)", "1845": "(1 Tim. ii. 9.)", "proposed": "", "page": "II.545", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-22.typ", "anchor": "§3 Rom 11:35", "ccel": "“Who has first", "1845": "“Who hath first", "proposed": "hath", "page": "II.546", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§7 John 6:37, 39", "ccel": "which has sent me, that of all which he has given me I should lose nothing,”", "1845": "which hath sent me, that of all which he has given me I should lose nothing,”", "proposed": "hath", "page": "II.550", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§7 John 6:37, 39", "ccel": "he has given me I should lose nothing,”", "1845": "he hath given me I should lose nothing,”", "proposed": "hath", "page": "II.550", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§7", "ccel": "which has sent me draw", "1845": "which hath sent me draw", "proposed": "hath", "page": "II.551", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§7 John 6:44, 45", "ccel": "that has", "1845": "that hath", "proposed": "hath", "page": "II.551", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§7 John 6:44, 45", "ccel": "Father comes", "1845": "Father cometh", "proposed": "cometh", "page": "II.551", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§7", "ccel": "he has chosen them,", "1845": "he hath chosen them,", "proposed": "hath", "page": "II.551", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 In those again who display their petulance", "ccel": "those Again who", "1845": "those again who", "proposed": "again", "page": "II.554", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10", "ccel": "Father “has", "1845": "Father “hath", "proposed": "hath", "page": "II.556", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 Eph 1:3, 4", "ccel": "he has chosen us", "1845": "he hath chosen us", "proposed": "hath", "page": "II.556", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 John 6:46", "ccel": "man has", "1845": "man hath", "proposed": "hath", "page": "II.557", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10", "ccel": "which has sent me, that of all which he has given me I should lose nothing;”", "1845": "which hath sent me, that of all which he has given me I should lose nothing;”", "proposed": "hath", "page": "II.557", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10", "ccel": "he has given me I should lose nothing;”", "1845": "he hath given me I should lose nothing;”", "proposed": "hath", "page": "II.557", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 John 6:39, 40", "ccel": "which sees", "1845": "which seeth", "proposed": "seeth", "page": "II.557", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 John 6:39, 40", "ccel": "and believes", "1845": "and believeth", "proposed": "believeth", "page": "II.557", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§11 Rom 9:18", "ccel": "God has mercy", "1845": "God hath mercy", "proposed": "hath", "page": "II.558", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§1 Matt 15:13", "ccel": "Father has not planted", "1845": "Father hath not planted", "proposed": "hath", "page": "II.560", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "note: This is taken from August. de Gen. cont. Manich. [keep CCEL (1845 “Auguste Dein Gen.”)]", "ccel": "August. de Gen. cont", "1845": "Auguste Dein Gen. cont", "proposed": "", "page": "II.562", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-23.typ", "anchor": "§2 held in detestation by us [keep CCEL (1845 “destesta-tion”)]", "ccel": "held in detestation by", "1845": "held in destestation by", "proposed": "", "page": "II.563", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-23.typ", "anchor": "§4 Rom 9:20, 21", "ccel": "thus? Has", "1845": "thus? Hath", "proposed": "Hath", "page": "II.564", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "note (French): mais plustost delaissez", "ccel": "plustost delaisse;”", "1845": "plustost delaissez;”", "proposed": "delaissez", "page": "II.565", "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§6 Prov 16:4", "ccel": "Lord has made", "1845": "Lord hath made", "proposed": "hath", "page": "II.567", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§11", "ccel": "“God has", "1845": "“God hath", "proposed": "hath", "page": "II.573", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§11 Rom 11:32, 35", "ccel": "“who has", "1845": "“who hath", "proposed": "hath", "page": "II.573", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13", "ccel": "God has not", "1845": "God hath not", "proposed": "hath", "page": "II.575", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13 1 Thess 4:4, 7", "ccel": "God has before", "1845": "God hath before", "proposed": "hath", "page": "II.575", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13 Matt 13:9", "ccel": "“Who has", "1845": "“Who hath", "proposed": "hath", "page": "II.575", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13", "ccel": "Who has known", "1845": "Who hath known", "proposed": "hath", "page": "II.575", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13", "ccel": "whoso has", "1845": "whoso hath", "proposed": "hath", "page": "II.576", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13", "ccel": "who has ears if", "1845": "who hath ears if", "proposed": "hath", "page": "II.576", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13", "ccel": "he has not", "1845": "he hath not", "proposed": "hath", "page": "II.576", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13", "ccel": "who has ears to", "1845": "who hath ears to", "proposed": "hath", "page": "II.577", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§14", "ccel": "(who has", "1845": "(who hath", "proposed": "hath", "page": "II.577", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§14", "ccel": "he has pleased", "1845": "he hath pleased", "proposed": "hath", "page": "II.577", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§14 “Because we know not who belongs to the number”", "ccel": "omitted: “because we", "1845": "omitted: “Because we", "proposed": "Because", "page": "II.577", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§1 John 6:46", "ccel": "man has", "1845": "man hath", "proposed": "hath", "page": "II.581", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§1 John 6:46", "ccel": "he has seen", "1845": "he hath seen", "proposed": "hath", "page": "II.581", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§1 John 6:44", "ccel": "which has sent", "1845": "which hath sent", "proposed": "hath", "page": "II.581", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§1", "ccel": "learned comes,", "1845": "learned cometh,", "proposed": "cometh", "page": "II.581", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§1", "ccel": "who has learned of", "1845": "who hath learned of", "proposed": "hath", "page": "II.581", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§1", "ccel": "that has heard", "1845": "that hath heard", "proposed": "hath", "page": "II.581", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§1", "ccel": "Father comes", "1845": "Father cometh", "proposed": "cometh", "page": "II.581", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§2 1 John 3:24", "ccel": "he has given us,”", "1845": "he hath given us,”", "proposed": "hath", "page": "II.583", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§2 Abraham … to be his friend [keep CCEL (the verse is Isa 41:8)]", "ccel": "(Isa 41:8)", "1845": "(Isaiah xxiv. 3;)", "proposed": "", "page": "II.583", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-24.typ", "anchor": "§3", "ccel": "Lord has", "1845": "Lord hath", "proposed": "hath", "page": "II.584", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§6 John 6:37–39, 17", "ccel": "he has delivered", "1845": "he hath delivered", "proposed": "hath", "page": "II.588", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§6", "ccel": "that comes", "1845": "that cometh", "proposed": "cometh", "page": "II.589", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§6 John 6:37, 39", "ccel": "he has given me", "1845": "he hath given me", "proposed": "hath", "page": "II.589", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§6 Matt 15:13", "ccel": "Father has not", "1845": "Father hath not", "proposed": "hath", "page": "II.589", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§6 Phil 1:6", "ccel": "who has begun", "1845": "who hath begun", "proposed": "hath", "page": "II.589", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§7", "ccel": "Father has given", "1845": "Father hath given", "proposed": "hath", "page": "II.590", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§10", "ccel": "“You has", "1845": "“You hath", "proposed": "hath", "page": "II.594", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§13", "ccel": "that has rebelled", "1845": "that hath rebelled", "proposed": "hath", "page": "II.597", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§13 Ezek 2:3, 6", "ccel": "which has eyes", "1845": "which hath eyes", "proposed": "hath", "page": "II.597", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§14 John 12:37, 38", "ccel": "who has believed", "1845": "who hath believed", "proposed": "hath", "page": "II.599", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§15 Ezek 18:23 “Have I any pleasure at all”", "ccel": "is, “have I any", "1845": "is, “Have I any", "proposed": "Have", "page": "II.600", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§16 Deut 4:7", "ccel": "who has God", "1845": "who hath God", "proposed": "hath", "page": "II.601", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§16", "ccel": "words, “God has", "1845": "words, “God hath", "proposed": "hath", "page": "II.602", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§16 Ps 115:3", "ccel": "he has done", "1845": "he hath done", "proposed": "hath", "page": "II.602", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§16 Ps 115:3", "ccel": "he has pleased,”", "1845": "he hath pleased,”", "proposed": "hath", "page": "II.602", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§16 (Ps 115:3). We must, therefore, expound", "ccel": "115:3). we must,", "1845": "115:3). We must,", "proposed": "We", "page": "II.602", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§17 “unto a rebellious people” [keep CCEL (the verse is Isa 65:2)]", "ccel": "people,” (Isa 65:2)", "1845": "people,” (Isa. lxv. 1,)", "proposed": "", "page": "II.604", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-24.typ", "anchor": "§17", "ccel": "passage, “God has", "1845": "passage, “God hath", "proposed": "hath", "page": "II.605", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§1", "ccel": "gospel, has,", "1845": "gospel, hath,", "proposed": "hath", "page": "II.607", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§5", "ccel": "that goes upward,", "1845": "that goeth upward,", "proposed": "goeth", "page": "II.614", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§5", "ccel": "that goes downward", "1845": "that goeth downward", "proposed": "goeth", "page": "II.614", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§6 the divinity is most refulgent", "ccel": "most Refulgent and", "1845": "most refulgent, and", "proposed": "refulgent", "page": "II.617", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§7 2 Cor 5:10", "ccel": "he has done,", "1845": "he hath done,", "proposed": "hath", "page": "II.618", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§7 “every knee shall bow to me” [keep CCEL (the verse is Isa 45:23)]", "ccel": "Isa 45:23)", "1845": "Isa. xix. 18;)", "proposed": "", "page": "II.619", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-25.typ", "anchor": "§8 1 Cor 6:13, 14", "ccel": "God has both", "1845": "God hath both", "proposed": "hath", "page": "II.621", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§8 John 6:39", "ccel": "which has", "1845": "which hath", "proposed": "hath", "page": "II.623", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§8 John 6:39", "ccel": "he has given", "1845": "he hath given", "proposed": "hath", "page": "II.623", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§9 (John 11:25). Is it to revive the whole", "ccel": "11:25). is it", "1845": "11:25). Is it", "proposed": "Is", "page": "II.624", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§10 1 John 3:2", "ccel": "it does", "1845": "it doth", "proposed": "doth", "page": "II.626", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§10 “Ye are our glory and our joy” [keep CCEL (the words are 1 Thess 2:20; 1845 “2 Thess. ii. 19”)]", "ccel": "(1 Thess 2:20)", "1845": "(2 Thess. ii. 19,)", "proposed": "", "page": "II.627", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-25.typ", "anchor": "§12 Isa 30:33", "ccel": "he has made", "1845": "he hath made", "proposed": "hath", "page": "II.629", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§12 Isa 30:33", "ccel": "brimstone, does", "1845": "brimstone, doth", "proposed": "doth", "page": "II.629", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§12 Matt 8:12 … inextinguishable fire (1845 unextinguishable)", "ccel": "teeth, inextinguishable fire", "1845": "teeth, unextinguishable fire", "proposed": "unextinguishable", "page": "II.629", "kind": "d", "confidence": "high"}
```

## Applied (2026-11-23)

All 167 rows (159 one-word rows and 8 hand edits) were applied with `apply_recheck.py`; the 17 misprint-1845 rows were left unchanged. The CCEL additions (kind c) were deleted to follow the print, under the editor's rule. The word-level diff was read: every change is a listed row.
