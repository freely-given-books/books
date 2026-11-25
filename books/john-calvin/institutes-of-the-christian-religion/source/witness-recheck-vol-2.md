# Calvin, Institutes, vol. 2 (Book II): Classic re-checked against the 1845 printing (Kraken OCR)

Base: `chapters/typ/vol-2/*.typ` in the `wt-institutes` worktree (book-2-argument + chapters 1–17; read only).
Witness: Calvin Translation Society, Edinburgh 1845, our own scans, Kraken OCR with ALTO beside it, page images `pages/p-NNNN.png`.
Book II runs over two 1845 volumes: **vol. 1 pp. 279–542** (Argument to ch. 11; `work/institutes/kraken/`, image = printed
page + 124, images 403–666) and **vol. 2 pp. 1–82** (ch. 12–17; `work/institutes/vol2/kraken/`, image = printed page + 10,
images 11–92; Book III begins at image 93). In the **p.** column a plain number is a page of 1845 vol. 1, **II.n** a page of
1845 vol. 2.
Method (as vol. 1): every .typ file was aligned word by word with the Kraken text (difflib; main text first, then the footnotes
against the OCR words the main text left over; running heads dropped; line-end hyphens joined). Differences were filtered for
reference style (Roman → Arabic compared as numbers), American spelling and OCR noise; then every remaining candidate (366
word and 83 reference rows, 58 capital-letter rows, 35 long runs) was read on the page image (line crops from the ALTO boxes,
contact sheets `b1.png`–`b11.png`). Only what the image confirms is listed.
Scripts and raw candidates: `work/institutes/latin/vol2/recheck/` (`align.py`, `filter.py`, `crop.py`, `mkbatch.py`,
`cand.json`, `cand2.tsv`, `cases.tsv`, `residual.txt`, `grammar_rows.tsv`, `build_report.py`).

**Rule applied (editor, 2026-11-23):** the Classic follows the 1845 print wherever CCEL's wording departs from it, including
CCEL's modernised grammar in Scripture quotations (kind **d/grammar**). Not listed: Arabic reference style, American spelling
(honor, Savior, sepulcher, apostasy, meager, steadfastness, honeyed, endeavor, stupefied, viciousness, engulfed, sty, by and
by…), CCEL's punctuation around references, CCEL's word joins, Greek accents. The `proposed` column holds only the replacement
words; explanations are in the anchor and kind columns; an empty `proposed` means no change to the text (misprint-1845) or a deletion (kind c).

**Kinds:** b (1845 words missing in CCEL), c (a CCEL line absent from 1845), d (a different word), d/grammar (CCEL's
modernised verb form), d/case (capital letter differs from the print), n (notes), misprint-1845 (the 1845 print is wrong;
CCEL corrects or shares it).

**Counts:** b 2, c 1, d 29, d/case 21, d/grammar 76, misprint-1845 7, n 8 (total 144).

**Systematic check.** Nothing like vol-1's “Judgment”: vol-2 has no capital *Judgment* at all, and a word-by-word
comparison of mid-sentence capitals against vols 3–6 turned up only *Moral Law*, *Table* (of the Law) and *Apostles* — all
three capitalised in 1845 too. The only repeated pattern is CCEL's has/does for hath/doth/doeth/doest/seeth/mayst in
Scripture quotations (76 places). Two CCEL keying slips recur across the volume: “untreated” for *uncreated* (twice, as in
vol-1) and “re-” for *be-* (rethinks, retaking).

**Also seen, not listed (as in vol. 1):** “Gospel” capitalised by 1845 where CCEL has “gospel” (p. 498 “preachers of the
Gospel”, p. 536 “fled for refuge to the Gospel”); 1845 lower case after “?” where CCEL starts a capital (II.64 “? and we
know”); CCEL “Lib.” → “lib.” in references (20 places); 1845 “the 1st and 2d sections” (ch. 9 heads; CCEL “2nd”);
small punctuation (ch. 1 Sections 7 “Another objection, viz.,”; CCEL drops the commas); “By and bye” (spelling).

**Structural:** no Beveridge footnote is missing: every OCR run left unmatched after both passes was checked, and all are
references (present in CCEL in Arabic form), running heads, signatures, the Book II / Book III title pages and the
“END OF THE FIRST VOLUME” imprint. One 1845 word is missing in CCEL (ch. 10 “contumely and reproach”), and the Book II title is cut short (first
row: 1845 adds “as first manifested to the Fathers, under the Law, and thereafter to us under the Gospel”; the volume's
`institutes-vol-2.typ` holds it, not a chapter file). 1845 heads Book II's opening summary “SUBJECT.” (Book I's
is “ARGUMENT.”); ours says “Argument” for both (listed). One CCEL line is
absent from 1845: the ch. 13 Sections list has a fourth entry, “4. Other three objections answered.”, which the print does
not have (its list stops at 3, though the chapter text runs to §4 and the chapter heads say “sec. 2-4”). The one long CCEL
run the OCR lacked (ch. 10 §4 “cannot be denied that the subject of that oath must ever”) is a line Kraken dropped; the
image has it.


## Book II title — `institutes-vol-2.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Book II title (heading in institutes-vol-2.typ; the subtitle on line 12 and the cover may follow) | = Book Second: Of the Knowledge of God the Redeemer, in Christ | BOOK SECOND. OF THE KNOWLEDGE OF GOD THE REDEEMER, IN CHRIST, AS FIRST MANIFESTED TO THE FATHERS, UNDER THE LAW, AND THEREAFTER TO US UNDER THE GOSPEL. | = Book Second: Of the Knowledge of God the Redeemer, in Christ, as First Manifested to the Fathers, under the Law, and Thereafter to Us under the Gospel | 279 | b | medium |

## book-2-argument — `book-2-argument.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| heading of the opening summary (Book I's 1845 heading is ARGUMENT., Book II's is SUBJECT.) | == Argument | SUBJECT. | == Subject | 280 | d | medium |

## Book II, chapter 01 — `book-2-chapter-01.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §6 “The Spirit is life because of righteousness” [keep CCEL (the words are Rom 8:10)] | righteousness,” (Rom 8:10) | righteousness,” (1 Cor. xv. 22.) |  | 290 | misprint-1845 | - |

## Book II, chapter 02 — `book-2-chapter-02.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| note: The French adds, “Pour en dire franchement | “pour en dire | “Pour en dire | Pour | 304 | n | low |
| note: Idem ad Bonifacium, Lib. 4 | ad Bonifacum, | ad Bonifacium, | Bonifacium | 310 | n | high |
| §14 the fact of an universal reason | fact of a universal | fact of an universal | an | 317 | d | medium |
| §20 Deut 29:2, 3, 4 | Lord has not | Lord hath not | hath | 322 | d/grammar | high |
| §20 John 6:44 | which has sent | which hath sent | hath | 323 | d/grammar | high |
| §20 is wise only in so far as He enlightens it | as he enlightens it | as He enlightens it | He | 323 | d/case | high |
| §20 1 Cor 2:9 | “Eye has | “Eye hath | hath | 324 | d/grammar | high |
| §20 1 Cor 2:9 | God has prepared | God hath prepared | hath | 324 | d/grammar | high |
| §20 | God has “made | God hath “made | hath | 324 | d/grammar | high |
| §24 when you hear of an universal judgment | hear of a universal | hear of an universal | an | 327 | d | medium |
| §25 sins proceed from preconceived pravity | preconceived gravity | preconceived pravity | pravity | 328 | d | high |

## Book II, chapter 03 — `book-2-chapter-03.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Rom 3:10–18 | that does good, | that doeth good, | doeth | 337 | d/grammar | high |
| §2 | that does good. | that doeth good. | doeth | 338 | d/grammar | high |
| §5 Jer 31:11 | Lord has redeemed | Lord hath redeemed | hath | 341 | d/grammar | high |
| §5 (August. lib. de Perf. Justit.) | Perf. Justin) | Perf. Justit.) | Justit. | 342 | d | high |
| note (French, “…peche franchement;”) which has been a deadly pest | franchement;” Which has | franchement;” which has | which | 343 | n | high |
| §6 Phil 1:6 | which has begun | which hath begun | hath | 344 | d/grammar | high |
| §6 Eph 2:10 | God has before | God hath before | hath | 345 | d/grammar | high |
| §6 | God has prepared; | God hath prepared; | hath | 345 | d/grammar | high |
| §6 | Lord “has | Lord “hath | hath | 345 | d/grammar | high |
| §7 John 6:45 | that has heard, | that hath heard, | hath | 347 | d/grammar | high |
| §7 John 6:45 | and has learned | and hath learned | hath | 347 | d/grammar | high |
| §9 Matt 15:13 | Father has | Father hath | hath | 349 | d/grammar | high |
| §10 John 6:45 | that has heard and | that hath heard and | hath | 351 | d/grammar | high |
| §10 | which has sent | which hath sent | hath | 352 | d/grammar | high |
| §10 1 John 3:9 | God does not commit | God doth not commit | doth | 352 | d/grammar | high |
| §11 | that has shall | that hath shall | hath | 353 | d/grammar | high |
| §12 Ps 59:10 | ‘the God of my | ‘The God of my | The | 354 | d/case | high |

## Book II, chapter 04 — `book-2-chapter-04.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 | world has | world hath | hath | 359 | d/grammar | high |
| §3 Moses relates that Sihon, king of the Amorites (Deut 2:30) | that Simon, king | that Sihon, king | Sihon | 362 | d | high |
| §7 peculiar grace in the use of them. When he says | use of them, when he says | use of them. When he says | them. When | 365 | d/case | high |
| note to §8 (French): il ne seroit pas moins libre [keep CCEL (pas)] | il ne seroit pas moins | il ne seroit par moins |  | 366 | misprint-1845 | - |

## Book II, chapter 05 — `book-2-chapter-05.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §4 John 15:5 [keep CCEL (the words are John 15:5)] | nothing,” (John 15:5) | nothing,” (John xx. 5.) |  | 372 | misprint-1845 | - |
| §10 Isa 1:19, 20 | Lord has | Lord hath | hath | 379 | d/grammar | high |
| §11 1 John 3:9 | God does not commit | God doth not commit | doth | 384 | d/grammar | high |
| §14 (Augustine) establishes and strengthens it | and establishes and | and stablishes and | stablishes | 388 | d | medium |
| §18 Ecclesiasticus 15:14-17 | He has | He hath | hath | 392 | d/grammar | high |
| §18 | “God has | “God hath | hath | 392 | d/grammar | high |
| §19 says not that the half dead are cured [keep CCEL (1845's “30” is garbled)] | (Eph 2:5, 6; 5:14) | (Eph. ii. 5, 30; v. 14,) |  | 393 | misprint-1845 | - |

## Book II, chapter 06 — `book-2-chapter-06.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 to return to that fountain; and, accordingly | fountain; And, accordingly | fountain; and, accordingly | and | 397 | d/case | high |
| §3 Isa 7:14 | his name Emmanuel; | his name Immanuel; | Immanuel | 400 | d | high |
| §3 Isa 7:14 | a virgin shall | a Virgin shall | Virgin | 400 | d/case | medium |
| §4 1 John 2:23 | same has | same hath | hath | 403 | d/grammar | high |
| §4 1 John 2:23 | “whosoever denieth | “Whosoever denieth | Whosoever | 403 | d/case | high |

## Book II, chapter 07 — `book-2-chapter-07.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Ps 110:4 | Lord has | Lord hath | hath | 408 | d/grammar | high |
| §8 | “God has | “God hath | hath | 414 | d/grammar | high |
| note: August. Ep. 89, Quaest. 2; Ad Assell. …; Ad Innocent. | ad Assell. Ep. 200; ad Innocent. | Ad Assell. Ep. 200; Ad Innocent. | Ad Assell. Ep. 200; Ad Innocent. | 415 | n | low |
| §14 Matt 5:18 | jot or little | jot or tittle | tittle | 420 | d | high |
| §17 Col 2:13, 14 | flesh, has | flesh, hath | hath | 422 | d/grammar | high |
| §16 Matt 27:51 the veil of the temple was rent in twain | rent in vain | rent in twain | twain | 422 | d | high |
| §16 the whole would have been elusory | been delusory | been elusory | elusory | 422 | d | medium |
| §17 Eph 2:14 | who has made | who hath made | hath | 423 | d/grammar | high |
| §17 Eph 2:14 | and has | and hath | hath | 423 | d/grammar | high |

## Book II, chapter 08 — `book-2-chapter-08.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections, 47: the Ninth Commandment | the ninth Commandment | the Ninth Commandment | Ninth | 428 | d/case | high |
| §3 he bethinks him of applying | he rethinks him | he bethinks him | bethinks | 432 | d | high |
| §5 | thou does | thou doest | doest | 433 | d/grammar | high |
| §5 | that has | that hath | hath | 433 | d/grammar | high |
| §7 Moses, the giver of an Evangelical | an evangelical, to | an Evangelical, to | Evangelical | 436 | d/case | high |
| §14 Matt 22:32 [keep CCEL (Matt 22 has 46 verses)] | (Matt 22:32) | (Matth. xxii. 52.) |  | 443 | misprint-1845 | - |
| §16 Invocation … the betaking of ourselves to his | the retaking of | the betaking of | betaking | 446 | d | high |
| §18 Second Commandment, Exod 20:6 | AND SHEWING MERCY | AND SHOWING MERCY | SHOWING | 448 | d | high |
| §18 | who has betrothed | who hath betrothed | hath | 449 | d/grammar | high |
| note to §18 (God as husband) [keep CCEL (Jeremiah has 52 chapters; the verse is Isa 62:5)] | Eph 5:30; Isa 62:5; | Eph. v. 30; Jer. lxii. 5; |  | 449 | misprint-1845 | - |
| §29 | that does | that doth | doth | 461 | d/grammar | high |
| §29 | whosoever does any work therein, | whosoever doeth any work therein, | doeth | 461 | d/grammar | high |
| §29 Exod 31:13–17 | whosoever does any work in | whosoever doeth any work in | doeth | 461 | d/grammar | high |
| §31 Col 2:16 | an holiday, | an holyday, | holyday | 463 | d | medium |
| §32 the hearing of the word | of the Word, the | of the word, the | word | 463 | d/case | high |
| §32 as the Apostle expresses it | the apostle expresses | the Apostle expresses | Apostle | 463 | d/case | high |
| §34 and public prayer: and, thirdly | prayer: And, thirdly | prayer: and, thirdly | and | 466 | d/case | high |
| note: As to this liberty, see Socrates | liberty, See Socrates | liberty, see Socrates | see | 466 | n | high |
| §37 | thou may | thou mayst | mayst | 468 | d/grammar | high |
| §37 a thing which not unfrequently happens | not infrequently happens | not unfrequently happens | unfrequently | 469 | d | medium |
| §39 vain pretexts, where either wrath | pretexts. Where either | pretexts, where either | pretexts, where | 471 | d/case | high |
| §46 embrace them with the lenity and indulgence | the levity and | the lenity and | lenity | 477 | d | high |
| §51 Deut 10:12, 13 | what does the | what doth the | doth | 483 | d/grammar | high |
| §53 Rom 13:8 | another has | another hath | hath | 485 | d/grammar | high |
| note: August. de Doctrina Christiana, Lib. 1 ch. 23, et seqq. | ch. 23 et seq.] | chap. 23, et seqq. | ch. 23 et seqq.] | 486 | n | low |

## Book II, chapter 09 — `book-2-chapter-09.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| chapter heads, III: between the Law and the Gospel | between the law and the Gospel | between the Law and the Gospel | Law | 492 | d/case | high |
| §1 John 1:18 | man has | man hath | hath | 493 | d/grammar | high |
| §1 John 1:18 | he has declared | he hath declared | hath | 493 | d/grammar | high |
| §1 Heb 1:1, 2 | prophets, has | prophets, hath | hath | 494 | d/grammar | high |
| §1 2 Cor 4:6 | darkness, has | darkness, hath | hath | 494 | d/grammar | high |
| §1 2 Cor 4:4 | world has | world hath | hath | 494 | d/grammar | high |
| §3 1 John 3:2 | “it does | “it doth | doth | 495 | d/grammar | high |
| §3 “We are saved by hope” [1845 and CCEL both; the words are Rom 8:24 if the editor fixes plain misprints] | hope,” (Rom 3:24) | hope,” (Rom. iii. 24.) |  | 495 | misprint-1845 | medium |
| §5 Matt 11:11 | there has | there hath | hath | 497 | d/grammar | high |

## Book II, chapter 10 — `book-2-chapter-10.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §8 Ps 144:15 | he has chosen | he hath chosen | hath | 507 | d/grammar | high |
| §12 Laban: assailed with contumely and reproach (Gen 31:20) | with contumely and (Gen 31:20) | with contumely and reproach, (Gen. xxxi. 20.) | contumely and reproach (Gen 31:20) | 512 | b | high |
| §13 | which has foundations, | which hath foundations, | hath | 514 | d/grammar | high |
| §13 Heb 11:9, 10, 13–16 | he has prepared | he hath prepared | hath | 514 | d/grammar | high |
| §17 | he sees that | he seeth that | seeth | 518 | d/grammar | high |
| §21 putrid carcases would be raised to life | putrid caresses | putrid carcases | carcases | 521 | d | high |
| §22 Isa 66:24 look upon the carcases | the caresses of | the carcases of | carcases | 522 | d | high |

## Book II, chapter 11 — `book-2-chapter-11.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Ps 133:3 | Lord has commanded | Lord hath commanded | hath | 529 | d/grammar | high |
| note: le vieil Testament est opposé au Nouveau | le viel Testament | le vieil Testament | vieil | 529 | n | high |
| §7 Jer 31:34 | saying, know the Lord | saying, Know the Lord | Know | 533 | d/case | high |
| §9 fear and trembling, the New inspires | trembling—The New | trembling, the New | trembling, the New | 536 | d/case | high |
| §12 Col 1:26 | which has | which hath | hath | 540 | d/grammar | high |
| §13 God who is always consistent with himself | consistent With himself | consistent with himself | with | 540 | d/case | high |

## Book II, chapter 12 — `book-2-chapter-12.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §4 Titus 2:11 | salvation has | salvation hath | hath | II.6 | d/grammar | high |
| §4 | “Therefore does | “Therefore doth | doth | II.6 | d/grammar | high |
| §5 Eph 1:4–7 | “He has | “He hath | hath | II.7 | d/grammar | high |
| §5 Eph 1:4–7 | he has made | he hath made | hath | II.7 | d/grammar | high |
| §5 wantonness and pruriency of the human mind | and prurience of | and pruriency of | pruriency | II.7 | d | medium |
| §7 the church would have been ἀκέφαλον | been akefalon | been ἀκέφαλον | ἀκέφαλον | II.11 | d | high |
| §7 to extract ridiculous paeans out of nothing | ridiculous plans | ridiculous pæans | paeans | II.12 | d | high |

## Book II, chapter 13 — `book-2-chapter-13.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections, 2: Impious objections of heretics farther discussed | heretics further discussed | heretics farther discussed | farther | II.13 | d | medium |
| Sections list: delete this line; 1845 lists sections 1-3 only (the chapter body does have §4) | #block(inset: (x: 1em))[4\. Other three objections answered.] | (no such line; the list ends “3. Other eight objections answered.”) |  | II.13 | c | medium |
| §2 | neither has | neither hath | hath | II.16 | d/grammar | high |

## Book II, chapter 14 — `book-2-chapter-14.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 John 3:13 | man has | man hath | hath | II.24 | d/grammar | high |
| §5 spirit, flesh, and three uncreated elements | three untreated elements. | three uncreated elements. | uncreated | II.27 | d | high |
| §8 compounds Christ of three uncreated elements | three untreated elements, | three uncreated elements, | uncreated | II.33 | d | high |
| §8 Nor does he acknowledge | God. nor does | God. Nor does | Nor | II.33 | d/case | high |

## Book II, chapter 15 — `book-2-chapter-15.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 | he “has | he “hath | hath | II.36 | d/grammar | high |
| §1 John 4:25 | that Messiah cometh | that Messias cometh | Messias | II.36 | d | high |
| note: the Angel or Interpreter of the great counsel | Angel or interpreter | Angel or Interpreter | Interpreter | II.36 | n | high |
| §2 Isa 61:1, 2 | Lord has | Lord hath | hath | II.37 | d/grammar | high |
| §2 Isa 61:1, 2 | he has sent | he hath sent | hath | II.37 | d/grammar | high |
| §2 under the Law, prophets as well as priests | under the law, prophets | under the Law, prophets | Law | II.37 | d/case | high |
| §5 | Father has given | Father hath given | hath | II.42 | d/grammar | high |
| §5 | God has | God hath | hath | II.42 | d/grammar | high |

## Book II, chapter 16 — `book-2-chapter-16.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §4 | God “has | God “hath | hath | II.51 | d/grammar | high |
| §4 Eph 1:3, 4 | he has chosen | he hath chosen | hath | II.51 | d/grammar | high |
| §5 Rom 3:25 | God has | God hath | hath | II.52 | d/grammar | high |
| §5 2 Cor 5:21 | “He has | “He hath | hath | II.52 | d/grammar | high |
| §6 Isa 53:6 | Lord has | Lord hath | hath | II.55 | d/grammar | high |
| §6 Gal 3:13, 14 | “Christ has | “Christ hath | hath | II.55 | d/grammar | high |
| §6 whenever Scripture explains the mode of redemption | whenever scripture explains | whenever Scripture explains | Scripture | II.56 | d/case | high |
| §7 he mortifies … and kills the old man | and kill the old man | and kills the old man | kills | II.57 | d | high |
| §8 the not unfrequent use of the term infernis | not infrequent use | not unfrequent use | unfrequent | II.58 | d | medium |
| §8 the term infernis for sepulcher | #emph[infernos] | infernis (italic) | infernis | II.58 | d | high |
| §15 | and has put | and hath put | hath | II.68 | d/grammar | high |
| §17 1 Thess 4:17 | meet the lord in | meet the Lord in | Lord | II.71 | d/case | high |

## Book II, chapter 17 — `book-2-chapter-17.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 than the Mediator himself | the mediator himself | the Mediator himself | Mediator | II.75 | d/case | high |
| §2 | “He has made us | “He hath made us | hath | II.76 | d/grammar | high |
| §2 2 Cor 5:21 | “He has made him | “He hath made him | hath | II.77 | d/grammar | high |
| §5 Rom 3:24, 25 | God has set | God hath set | hath | II.79 | d/grammar | high |
| §5 | Christ “has | Christ “hath | hath | II.80 | d/grammar | high |
| §5 John 6:57 | Father has | Father hath | hath | II.81 | d/grammar | high |
| §6 Phil 2:9 | God has highly | God hath highly | hath | II.81 | d/grammar | high |

## Findings (one JSON line each)

```
{"file": "/home/courtney/Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion/institutes-vol-2.typ", "anchor": "Book II title (heading in institutes-vol-2.typ; the subtitle on line 12 and the cover may follow)", "ccel": "= Book Second: Of the Knowledge of God the Redeemer, in Christ", "1845": "BOOK SECOND. OF THE KNOWLEDGE OF GOD THE REDEEMER, IN CHRIST, AS FIRST MANIFESTED TO THE FATHERS, UNDER THE LAW, AND THEREAFTER TO US UNDER THE GOSPEL.", "proposed": "= Book Second: Of the Knowledge of God the Redeemer, in Christ, as First Manifested to the Fathers, under the Law, and Thereafter to Us under the Gospel", "page": 279, "kind": "b", "confidence": "medium"}
{"file": "book-2-argument.typ", "anchor": "heading of the opening summary (Book I's 1845 heading is ARGUMENT., Book II's is SUBJECT.)", "ccel": "== Argument", "1845": "SUBJECT.", "proposed": "== Subject", "page": 280, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-01.typ", "anchor": "§6 “The Spirit is life because of righteousness” [keep CCEL (the words are Rom 8:10)]", "ccel": "righteousness,” (Rom 8:10)", "1845": "righteousness,” (1 Cor. xv. 22.)", "proposed": "", "page": 290, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-2-chapter-02.typ", "anchor": "note: The French adds, “Pour en dire franchement", "ccel": "“pour en dire", "1845": "“Pour en dire", "proposed": "Pour", "page": 304, "kind": "n", "confidence": "low"}
{"file": "book-2-chapter-02.typ", "anchor": "note: Idem ad Bonifacium, Lib. 4", "ccel": "ad Bonifacum,", "1845": "ad Bonifacium,", "proposed": "Bonifacium", "page": 310, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§14 the fact of an universal reason", "ccel": "fact of a universal", "1845": "fact of an universal", "proposed": "an", "page": 317, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-02.typ", "anchor": "§20 Deut 29:2, 3, 4", "ccel": "Lord has not", "1845": "Lord hath not", "proposed": "hath", "page": "322", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§20 John 6:44", "ccel": "which has sent", "1845": "which hath sent", "proposed": "hath", "page": "323", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§20 is wise only in so far as He enlightens it", "ccel": "as he enlightens it", "1845": "as He enlightens it", "proposed": "He", "page": 323, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§20 1 Cor 2:9", "ccel": "“Eye has", "1845": "“Eye hath", "proposed": "hath", "page": "324", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§20 1 Cor 2:9", "ccel": "God has prepared", "1845": "God hath prepared", "proposed": "hath", "page": "324", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§20", "ccel": "God has “made", "1845": "God hath “made", "proposed": "hath", "page": "324", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§24 when you hear of an universal judgment", "ccel": "hear of a universal", "1845": "hear of an universal", "proposed": "an", "page": 327, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-02.typ", "anchor": "§25 sins proceed from preconceived pravity", "ccel": "preconceived gravity", "1845": "preconceived pravity", "proposed": "pravity", "page": 328, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§2 Rom 3:10–18", "ccel": "that does good,", "1845": "that doeth good,", "proposed": "doeth", "page": "337", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§2", "ccel": "that does good.", "1845": "that doeth good.", "proposed": "doeth", "page": "338", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§5 Jer 31:11", "ccel": "Lord has redeemed", "1845": "Lord hath redeemed", "proposed": "hath", "page": "341", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§5 (August. lib. de Perf. Justit.)", "ccel": "Perf. Justin)", "1845": "Perf. Justit.)", "proposed": "Justit.", "page": 342, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "note (French, “…peche franchement;”) which has been a deadly pest", "ccel": "franchement;” Which has", "1845": "franchement;” which has", "proposed": "which", "page": 343, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§6 Phil 1:6", "ccel": "which has begun", "1845": "which hath begun", "proposed": "hath", "page": "344", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§6 Eph 2:10", "ccel": "God has before", "1845": "God hath before", "proposed": "hath", "page": "345", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§6", "ccel": "God has prepared;", "1845": "God hath prepared;", "proposed": "hath", "page": "345", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§6", "ccel": "Lord “has", "1845": "Lord “hath", "proposed": "hath", "page": "345", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§7 John 6:45", "ccel": "that has heard,", "1845": "that hath heard,", "proposed": "hath", "page": "347", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§7 John 6:45", "ccel": "and has learned", "1845": "and hath learned", "proposed": "hath", "page": "347", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§9 Matt 15:13", "ccel": "Father has", "1845": "Father hath", "proposed": "hath", "page": "349", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§10 John 6:45", "ccel": "that has heard and", "1845": "that hath heard and", "proposed": "hath", "page": "351", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§10", "ccel": "which has sent", "1845": "which hath sent", "proposed": "hath", "page": "352", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§10 1 John 3:9", "ccel": "God does not commit", "1845": "God doth not commit", "proposed": "doth", "page": "352", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§11", "ccel": "that has shall", "1845": "that hath shall", "proposed": "hath", "page": "353", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§12 Ps 59:10", "ccel": "‘the God of my", "1845": "‘The God of my", "proposed": "The", "page": 354, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§1", "ccel": "world has", "1845": "world hath", "proposed": "hath", "page": "359", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§3 Moses relates that Sihon, king of the Amorites (Deut 2:30)", "ccel": "that Simon, king", "1845": "that Sihon, king", "proposed": "Sihon", "page": 362, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§7 peculiar grace in the use of them. When he says", "ccel": "use of them, when he says", "1845": "use of them. When he says", "proposed": "them. When", "page": 365, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "note to §8 (French): il ne seroit pas moins libre [keep CCEL (pas)]", "ccel": "il ne seroit pas moins", "1845": "il ne seroit par moins", "proposed": "", "page": 366, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-2-chapter-05.typ", "anchor": "§4 John 15:5 [keep CCEL (the words are John 15:5)]", "ccel": "nothing,” (John 15:5)", "1845": "nothing,” (John xx. 5.)", "proposed": "", "page": 372, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-2-chapter-05.typ", "anchor": "§10 Isa 1:19, 20", "ccel": "Lord has", "1845": "Lord hath", "proposed": "hath", "page": "379", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§11 1 John 3:9", "ccel": "God does not commit", "1845": "God doth not commit", "proposed": "doth", "page": "384", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§14 (Augustine) establishes and strengthens it", "ccel": "and establishes and", "1845": "and stablishes and", "proposed": "stablishes", "page": 388, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-05.typ", "anchor": "§18 Ecclesiasticus 15:14-17", "ccel": "He has", "1845": "He hath", "proposed": "hath", "page": "392", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§18", "ccel": "“God has", "1845": "“God hath", "proposed": "hath", "page": "392", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§19 says not that the half dead are cured [keep CCEL (1845's “30” is garbled)]", "ccel": "(Eph 2:5, 6; 5:14)", "1845": "(Eph. ii. 5, 30; v. 14,)", "proposed": "", "page": 393, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-2-chapter-06.typ", "anchor": "§1 to return to that fountain; and, accordingly", "ccel": "fountain; And, accordingly", "1845": "fountain; and, accordingly", "proposed": "and", "page": 397, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-06.typ", "anchor": "§3 Isa 7:14", "ccel": "his name Emmanuel;", "1845": "his name Immanuel;", "proposed": "Immanuel", "page": 400, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-06.typ", "anchor": "§3 Isa 7:14", "ccel": "a virgin shall", "1845": "a Virgin shall", "proposed": "Virgin", "page": 400, "kind": "d/case", "confidence": "medium"}
{"file": "book-2-chapter-06.typ", "anchor": "§4 1 John 2:23", "ccel": "same has", "1845": "same hath", "proposed": "hath", "page": "403", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-06.typ", "anchor": "§4 1 John 2:23", "ccel": "“whosoever denieth", "1845": "“Whosoever denieth", "proposed": "Whosoever", "page": 403, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§2 Ps 110:4", "ccel": "Lord has", "1845": "Lord hath", "proposed": "hath", "page": "408", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§8", "ccel": "“God has", "1845": "“God hath", "proposed": "hath", "page": "414", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "note: August. Ep. 89, Quaest. 2; Ad Assell. …; Ad Innocent.", "ccel": "ad Assell. Ep. 200; ad Innocent.", "1845": "Ad Assell. Ep. 200; Ad Innocent.", "proposed": "Ad Assell. Ep. 200; Ad Innocent.", "page": 415, "kind": "n", "confidence": "low"}
{"file": "book-2-chapter-07.typ", "anchor": "§14 Matt 5:18", "ccel": "jot or little", "1845": "jot or tittle", "proposed": "tittle", "page": 420, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§17 Col 2:13, 14", "ccel": "flesh, has", "1845": "flesh, hath", "proposed": "hath", "page": "422", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§16 Matt 27:51 the veil of the temple was rent in twain", "ccel": "rent in vain", "1845": "rent in twain", "proposed": "twain", "page": 422, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§16 the whole would have been elusory", "ccel": "been delusory", "1845": "been elusory", "proposed": "elusory", "page": 422, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-07.typ", "anchor": "§17 Eph 2:14", "ccel": "who has made", "1845": "who hath made", "proposed": "hath", "page": "423", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§17 Eph 2:14", "ccel": "and has", "1845": "and hath", "proposed": "hath", "page": "423", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "Sections, 47: the Ninth Commandment", "ccel": "the ninth Commandment", "1845": "the Ninth Commandment", "proposed": "Ninth", "page": 428, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§3 he bethinks him of applying", "ccel": "he rethinks him", "1845": "he bethinks him", "proposed": "bethinks", "page": 432, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§5", "ccel": "thou does", "1845": "thou doest", "proposed": "doest", "page": "433", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§5", "ccel": "that has", "1845": "that hath", "proposed": "hath", "page": "433", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§7 Moses, the giver of an Evangelical", "ccel": "an evangelical, to", "1845": "an Evangelical, to", "proposed": "Evangelical", "page": 436, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§14 Matt 22:32 [keep CCEL (Matt 22 has 46 verses)]", "ccel": "(Matt 22:32)", "1845": "(Matth. xxii. 52.)", "proposed": "", "page": 443, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-2-chapter-08.typ", "anchor": "§16 Invocation … the betaking of ourselves to his", "ccel": "the retaking of", "1845": "the betaking of", "proposed": "betaking", "page": 446, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§18 Second Commandment, Exod 20:6", "ccel": "AND SHEWING MERCY", "1845": "AND SHOWING MERCY", "proposed": "SHOWING", "page": 448, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§18", "ccel": "who has betrothed", "1845": "who hath betrothed", "proposed": "hath", "page": "449", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note to §18 (God as husband) [keep CCEL (Jeremiah has 52 chapters; the verse is Isa 62:5)]", "ccel": "Eph 5:30; Isa 62:5;", "1845": "Eph. v. 30; Jer. lxii. 5;", "proposed": "", "page": 449, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-2-chapter-08.typ", "anchor": "§29", "ccel": "that does", "1845": "that doth", "proposed": "doth", "page": "461", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§29", "ccel": "whosoever does any work therein,", "1845": "whosoever doeth any work therein,", "proposed": "doeth", "page": "461", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§29 Exod 31:13–17", "ccel": "whosoever does any work in", "1845": "whosoever doeth any work in", "proposed": "doeth", "page": "461", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§31 Col 2:16", "ccel": "an holiday,", "1845": "an holyday,", "proposed": "holyday", "page": 463, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-08.typ", "anchor": "§32 the hearing of the word", "ccel": "of the Word, the", "1845": "of the word, the", "proposed": "word", "page": 463, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§32 as the Apostle expresses it", "ccel": "the apostle expresses", "1845": "the Apostle expresses", "proposed": "Apostle", "page": 463, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§34 and public prayer: and, thirdly", "ccel": "prayer: And, thirdly", "1845": "prayer: and, thirdly", "proposed": "and", "page": 466, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: As to this liberty, see Socrates", "ccel": "liberty, See Socrates", "1845": "liberty, see Socrates", "proposed": "see", "page": 466, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§37", "ccel": "thou may", "1845": "thou mayst", "proposed": "mayst", "page": "468", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§37 a thing which not unfrequently happens", "ccel": "not infrequently happens", "1845": "not unfrequently happens", "proposed": "unfrequently", "page": 469, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-08.typ", "anchor": "§39 vain pretexts, where either wrath", "ccel": "pretexts. Where either", "1845": "pretexts, where either", "proposed": "pretexts, where", "page": 471, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§46 embrace them with the lenity and indulgence", "ccel": "the levity and", "1845": "the lenity and", "proposed": "lenity", "page": 477, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§51 Deut 10:12, 13", "ccel": "what does the", "1845": "what doth the", "proposed": "doth", "page": "483", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§53 Rom 13:8", "ccel": "another has", "1845": "another hath", "proposed": "hath", "page": "485", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: August. de Doctrina Christiana, Lib. 1 ch. 23, et seqq.", "ccel": "ch. 23 et seq.]", "1845": "chap. 23, et seqq.", "proposed": "ch. 23 et seqq.]", "page": 486, "kind": "n", "confidence": "low"}
{"file": "book-2-chapter-09.typ", "anchor": "chapter heads, III: between the Law and the Gospel", "ccel": "between the law and the Gospel", "1845": "between the Law and the Gospel", "proposed": "Law", "page": 492, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§1 John 1:18", "ccel": "man has", "1845": "man hath", "proposed": "hath", "page": "493", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§1 John 1:18", "ccel": "he has declared", "1845": "he hath declared", "proposed": "hath", "page": "493", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§1 Heb 1:1, 2", "ccel": "prophets, has", "1845": "prophets, hath", "proposed": "hath", "page": "494", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§1 2 Cor 4:6", "ccel": "darkness, has", "1845": "darkness, hath", "proposed": "hath", "page": "494", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§1 2 Cor 4:4", "ccel": "world has", "1845": "world hath", "proposed": "hath", "page": "494", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§3 1 John 3:2", "ccel": "“it does", "1845": "“it doth", "proposed": "doth", "page": "495", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§3 “We are saved by hope” [1845 and CCEL both; the words are Rom 8:24 if the editor fixes plain misprints]", "ccel": "hope,” (Rom 3:24)", "1845": "hope,” (Rom. iii. 24.)", "proposed": "", "page": 495, "kind": "misprint-1845", "confidence": "medium"}
{"file": "book-2-chapter-09.typ", "anchor": "§5 Matt 11:11", "ccel": "there has", "1845": "there hath", "proposed": "hath", "page": "497", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§8 Ps 144:15", "ccel": "he has chosen", "1845": "he hath chosen", "proposed": "hath", "page": "507", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§12 Laban: assailed with contumely and reproach (Gen 31:20)", "ccel": "with contumely and (Gen 31:20)", "1845": "with contumely and reproach, (Gen. xxxi. 20.)", "proposed": "contumely and reproach (Gen 31:20)", "page": 512, "kind": "b", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§13", "ccel": "which has foundations,", "1845": "which hath foundations,", "proposed": "hath", "page": "514", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§13 Heb 11:9, 10, 13–16", "ccel": "he has prepared", "1845": "he hath prepared", "proposed": "hath", "page": "514", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§17", "ccel": "he sees that", "1845": "he seeth that", "proposed": "seeth", "page": "518", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§21 putrid carcases would be raised to life", "ccel": "putrid caresses", "1845": "putrid carcases", "proposed": "carcases", "page": 521, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§22 Isa 66:24 look upon the carcases", "ccel": "the caresses of", "1845": "the carcases of", "proposed": "carcases", "page": 522, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§2 Ps 133:3", "ccel": "Lord has commanded", "1845": "Lord hath commanded", "proposed": "hath", "page": "529", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "note: le vieil Testament est opposé au Nouveau", "ccel": "le viel Testament", "1845": "le vieil Testament", "proposed": "vieil", "page": 529, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§7 Jer 31:34", "ccel": "saying, know the Lord", "1845": "saying, Know the Lord", "proposed": "Know", "page": 533, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§9 fear and trembling, the New inspires", "ccel": "trembling—The New", "1845": "trembling, the New", "proposed": "trembling, the New", "page": 536, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§12 Col 1:26", "ccel": "which has", "1845": "which hath", "proposed": "hath", "page": "540", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§13 God who is always consistent with himself", "ccel": "consistent With himself", "1845": "consistent with himself", "proposed": "with", "page": 540, "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§4 Titus 2:11", "ccel": "salvation has", "1845": "salvation hath", "proposed": "hath", "page": "II.6", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§4", "ccel": "“Therefore does", "1845": "“Therefore doth", "proposed": "doth", "page": "II.6", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§5 Eph 1:4–7", "ccel": "“He has", "1845": "“He hath", "proposed": "hath", "page": "II.7", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§5 Eph 1:4–7", "ccel": "he has made", "1845": "he hath made", "proposed": "hath", "page": "II.7", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§5 wantonness and pruriency of the human mind", "ccel": "and prurience of", "1845": "and pruriency of", "proposed": "pruriency", "page": "II.7", "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-12.typ", "anchor": "§7 the church would have been ἀκέφαλον", "ccel": "been akefalon", "1845": "been ἀκέφαλον", "proposed": "ἀκέφαλον", "page": "II.11", "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§7 to extract ridiculous paeans out of nothing", "ccel": "ridiculous plans", "1845": "ridiculous pæans", "proposed": "paeans", "page": "II.12", "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-13.typ", "anchor": "Sections, 2: Impious objections of heretics farther discussed", "ccel": "heretics further discussed", "1845": "heretics farther discussed", "proposed": "farther", "page": "II.13", "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-13.typ", "anchor": "Sections list: delete this line; 1845 lists sections 1-3 only (the chapter body does have §4)", "ccel": "#block(inset: (x: 1em))[4\\. Other three objections answered.]", "1845": "(no such line; the list ends “3. Other eight objections answered.”)", "proposed": "", "page": "II.13", "kind": "c", "confidence": "medium"}
{"file": "book-2-chapter-13.typ", "anchor": "§2", "ccel": "neither has", "1845": "neither hath", "proposed": "hath", "page": "II.16", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "§2 John 3:13", "ccel": "man has", "1845": "man hath", "proposed": "hath", "page": "II.24", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "§5 spirit, flesh, and three uncreated elements", "ccel": "three untreated elements.", "1845": "three uncreated elements.", "proposed": "uncreated", "page": "II.27", "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "§8 compounds Christ of three uncreated elements", "ccel": "three untreated elements,", "1845": "three uncreated elements,", "proposed": "uncreated", "page": "II.33", "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "§8 Nor does he acknowledge", "ccel": "God. nor does", "1845": "God. Nor does", "proposed": "Nor", "page": "II.33", "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§1", "ccel": "he “has", "1845": "he “hath", "proposed": "hath", "page": "II.36", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§1 John 4:25", "ccel": "that Messiah cometh", "1845": "that Messias cometh", "proposed": "Messias", "page": "II.36", "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "note: the Angel or Interpreter of the great counsel", "ccel": "Angel or interpreter", "1845": "Angel or Interpreter", "proposed": "Interpreter", "page": "II.36", "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§2 Isa 61:1, 2", "ccel": "Lord has", "1845": "Lord hath", "proposed": "hath", "page": "II.37", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§2 Isa 61:1, 2", "ccel": "he has sent", "1845": "he hath sent", "proposed": "hath", "page": "II.37", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§2 under the Law, prophets as well as priests", "ccel": "under the law, prophets", "1845": "under the Law, prophets", "proposed": "Law", "page": "II.37", "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§5", "ccel": "Father has given", "1845": "Father hath given", "proposed": "hath", "page": "II.42", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§5", "ccel": "God has", "1845": "God hath", "proposed": "hath", "page": "II.42", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§4", "ccel": "God “has", "1845": "God “hath", "proposed": "hath", "page": "II.51", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§4 Eph 1:3, 4", "ccel": "he has chosen", "1845": "he hath chosen", "proposed": "hath", "page": "II.51", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§5 Rom 3:25", "ccel": "God has", "1845": "God hath", "proposed": "hath", "page": "II.52", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§5 2 Cor 5:21", "ccel": "“He has", "1845": "“He hath", "proposed": "hath", "page": "II.52", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§6 Isa 53:6", "ccel": "Lord has", "1845": "Lord hath", "proposed": "hath", "page": "II.55", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§6 Gal 3:13, 14", "ccel": "“Christ has", "1845": "“Christ hath", "proposed": "hath", "page": "II.55", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§6 whenever Scripture explains the mode of redemption", "ccel": "whenever scripture explains", "1845": "whenever Scripture explains", "proposed": "Scripture", "page": "II.56", "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§7 he mortifies … and kills the old man", "ccel": "and kill the old man", "1845": "and kills the old man", "proposed": "kills", "page": "II.57", "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§8 the not unfrequent use of the term infernis", "ccel": "not infrequent use", "1845": "not unfrequent use", "proposed": "unfrequent", "page": "II.58", "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-16.typ", "anchor": "§8 the term infernis for sepulcher", "ccel": "#emph[infernos]", "1845": "infernis (italic)", "proposed": "infernis", "page": "II.58", "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§15", "ccel": "and has put", "1845": "and hath put", "proposed": "hath", "page": "II.68", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§17 1 Thess 4:17", "ccel": "meet the lord in", "1845": "meet the Lord in", "proposed": "Lord", "page": "II.71", "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§1 than the Mediator himself", "ccel": "the mediator himself", "1845": "the Mediator himself", "proposed": "Mediator", "page": "II.75", "kind": "d/case", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§2", "ccel": "“He has made us", "1845": "“He hath made us", "proposed": "hath", "page": "II.76", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§2 2 Cor 5:21", "ccel": "“He has made him", "1845": "“He hath made him", "proposed": "hath", "page": "II.77", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§5 Rom 3:24, 25", "ccel": "God has set", "1845": "God hath set", "proposed": "hath", "page": "II.79", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§5", "ccel": "Christ “has", "1845": "Christ “hath", "proposed": "hath", "page": "II.80", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§5 John 6:57", "ccel": "Father has", "1845": "Father hath", "proposed": "hath", "page": "II.81", "kind": "d/grammar", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§6 Phil 2:9", "ccel": "God has highly", "1845": "God hath highly", "proposed": "hath", "page": "II.81", "kind": "d/grammar", "confidence": "high"}
```
