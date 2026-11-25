# Calvin, Institutes, vol. 4 (Book III, chapters 11–25): CCEL vs the 1845 printing

Base: `chapters/typ/vol-4/*.typ` (CCEL machine pass). Witness: Calvin
Translation Society, Edinburgh 1845, vol. 2 (archive.org
`institutesofreli02calvuoft`): Book III, chapters 11–25, pp. 301–630. The
OCR was aligned word by word with the edition (difflib; scripts in
`scratchpad/calvin-v4/`, adapted from the vol-3 agent's: `align.py` writes raw
candidates to `cand-*.txt`, findings in `findings.jsonl`, `build.py` writes
this file and checks that every "ccel" string occurs exactly once in its
file). Doubtful places were read on the page images (crops in
`scratchpad/calvin-pages/`, files `q*.jpg`): the scan index n = printed page
+ 9 holds to the end of Book III (checked on pp. 311, 318, 322 and late in the
volume). "verified" in the confidence column = read on the image. Otherwise
the OCR reading is an unambiguous real word in clean OCR.

**Kinds:** **b** = 1845 words missing in CCEL. **c** = CCEL words not in 1845.
**d** = a different word. **d/comma** = CCEL turned the comma after a word
into a final "s" ("Scripture, while" → "Scriptures while"); every case checked
against the 1845 comma. **e** = Greek/Latin/Hebrew. **f** = reference numbers
(proposed in CCEL's Arabic style). **n** = notes. **info** = CCEL departs from
1845 but corrects a misprint there; keep CCEL.

**Not listed one by one (CCEL-wide editorial choices, kept by the edition):**
Arabic numerals in references; CCEL's spellings (fulfill, instill,
unskillful, steadfastness, stupefied, unblamable, Rabbis, acceptor);
has/does/comes for hath/doth/cometh in Scripture quotations; CCEL's
punctuation around references; closed-up compounds (throughout, cannot,
cuttlefish).

**Greek and Hebrew encoding.** A search of every vol-4 file for Greek in the
old SGreek font codes, private-use characters and Hebrew font codes found
none. The only Hebrew in 1845 here, דעת (III.11 §12), is missing from CCEL
altogether ("For the word () is"); it is given below. Greek in vol-4: one
quotation in III.15 (with two encoding faults, listed) and single words in
III.17, III.19, III.20.

## Book III, chapter 11 — `book-3-chapter-11.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 7 | Seventh and eighth arguments. | Seventh and eighth arguments. Answers. | Seventh and eighth arguments. Answers. | 301 | b | high |
| §2 a man accused before an impartial judge | by the judge, as a | by the judge, so a | so | 303 | d | high |
| §6 Osiander confounds the two gifts | But Scriptures while | But Scripture, while | Scripture, while | 309 | d/comma | high |
| §6 Abraham's faith | righteousness of Gad | righteousness of God | God | 309 | d | high |
| §8 Isa. 53:11, the Father speaks | For the word () is | For the word דעת is | For the word דעת is | 311 | b | high (verified) |
| §11 Osiander's objection, forensic term | because it behaves | because it behoves | behoves | 315 | d | high |
| §11 Hebrew usage of justify | moderately verdant | moderately versant | versant | 316 | d | high |
| §11 Paul, Rom. 7:24 | but retaking | but betaking | betaking | 317 | d | high |
| §11 Moses' intercession | taking affect | taking effect | effect | 318 | d | high (verified) |
| §12 supply the wants of his members | When, although | Then, although | Then | 320 | d | high |
| §13 remission of sins | the minutes portion | the minutest portion | minutest | 321 | d | high |
| §17 let no prater here allege | no pester here | no prater here | prater | 325 | d | high |
| §17 Paul declares | without exceptions that | without exception, that | exception, that | 325 | d/comma | high |
| §18 excluding the Law | aided by worlds | aided by works | works | 326 | d | high |
| §19 the exclusive word alone | has no part in its and | has no part in it, and | it, and | 327 | d/comma | high |
| §19 subterfuge from ancient writers | taken from Origin | taken from Origen | Origen | 327 | d | high |
| §20 works of Law | justifying to theme | justifying to them, | them | 328 | d | high |
| §20 faith which works by love | love (Gal. 3:6) | love, (Gal. v. 6 | love (Gal. 5:6) | 329 | f | high |
| §20 Could he express more clearly | than in this word, | than in this way, | way | 329 | d | high |
| §21 the wrath of God lies upon all men | to the axioms that | to the axiom, that | axiom, that | 329 | d/comma | high |
| §23 Christ communicates his righteousness | wondrous ways in | wondrous way, in | way, in | 332 | d/comma | high |
| §23 Christ communicates his righteousness | justice of Gods transfuses | justice of God, transfuses | God, transfuses | 332 | d/comma | high |
| §23 obedience of Christ imputed | if it where our | if it were our | were | 332 | d | high |
| §23 Ambrose on Jacob | Vita Beats | Vita Beata | Beata | 332 | d | high |
| note (the two things, To be justified) | as oppopsites | as opposites | opposites | 306 | n | high |
| note (cuttle-fish) | trougle l’eau | trouble l'eau | trouble l’eau | 308 | n | high |
| note (Faisant semblant) | samblant | semblant | semblant | 310 | n | high (verified) |
| note (bonne reputation) | reputation au monde, qu d’etre | reputation au monde, que d'etre | que d’etre | 313 | n | high |
| note (crassa mixtura) | viandes qu nous | viandes que nous | que nous | 314 | n | high |
| note (bonnes œuvres des fideles) | Thus they say that has | Thus they say that that has | say that that has | 322 | n | high (verified) |
| note (word Alone) | having it added | having added it | having added it | 326 | n | high |

## Book III, chapter 12 — `book-3-chapter-12.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Who among us shall dwell | says the prophets “shall | says the prophet, “shall | prophet, “shall | 335 | d/comma | high |
| §6 thou wilt save the afflicted | hear from the prophets “thou | hear from the prophet, “thou | prophet, “thou | 340 | d/comma | high |

## Book III, chapter 13 — `book-3-chapter-13.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 that he might be just, and the justifier | Jesus,” (Rom. 3:25) | Jesus," (Rom. iii. 25.) | Jesus,” (Rom. 3:26) (1845 has the same misprint; the words quoted are v. 26) | 345 | f | medium |
| §3 flattery to the judgment of God | without hesitations to | without hesitation, to | hesitation, to | 347 | d/comma | high |
| §4 if its fulfillment depends | our merits when pray | our merit, when, pray | merit, when, pray | 348 | d/comma | high |
| §4 Augustine on Ps. 88 | Tract. 50) | Tract. 1.) | Tract. 1) | 348 | f | high (verified) |
| §4 Bernard, In Dedicatione Templi | (Bert. in | (Berd. in | (Bern. in (1845 misprints Berd.) | 349 | d | medium (verified) |
| §4 Let us thus briefly conclude | are not surer unless | are not sure, unless | sure, unless | 349 | d | high |
| §5 the heavenly inheritance | being in grafted | being ingrafted | ingrafted | 350 | d | high |
| §5 faith merely passive | merely passives bringing | merely passive, bringing | passive, bringing | 350 | d/comma | high |
| note (two previous sentences) | ommited | omitted | omitted | 347 | n | high |

## Book III, chapter 14 — `book-3-chapter-14.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 2 | blessings of he present | blessings of the present | the | 351 | d | high |
| Sections 17 | four different classes | four different causes | causes | 352 | d | high |
| §2 Titus and Trajan | Titus and Trojan | Titus and Trajan | Trajan | 353 | d | high |
| §3 Augustine against Julian | contra Julia. | contra Julian, | contra Julian. | 354 | d | high |
| §7 convicted of a wicked and impious mind | impious minds they | impious mind, they | mind, they | 359 | d/comma | high |
| §7 no man, however flagitious | however flagitous | however flagitious | flagitious | 359 | d | high |
| §8 Isa. 1:13-16 | feasts my foul | feasts my soul | soul | 360 | d | high |
| §8 notorious to all | tolerably verdant with Scriptures that | tolerably versant with Scripture, that | versant with Scripture, that | 360 | d/comma | high |
| §9 the fourth class | We admits that | We admit, that | admit, that | 361 | d/comma | high |
| §9 retarded by much weakness | we see theft the | we see that the | that | 361 | d | high |
| §10 constant remission of sins | the statement which we set out | the statement with which we set out | with which | 362 | b | high |
| §11 not of works | In like manners when | In like manner, when | manner, when | 363 | d/comma | high |
| §15 the boast of Paul | they ceaselessly allege | they causelessly allege | causelessly | 366 | d | high |
| §15 blustering dogmas | will behave to | will behove to | behove | 367 | d | high |
| §16 to stand dumb | bar of Gods all | bar of God, all | God, all | 368 | d/comma | high |
| §20 Bernard, This only I say | this asks this | this ask, this | ask, this | 372 | d/comma | high |
| §20 Bernard, See in me thy work | If thou sees mine, thou condemnest; if thou sees thine | If thou seest mine, thou condemnest; if thou seest thine | seest ... seest | 372 | d | high |
| note (Jer. 17:9; Gen. 8:21 ...) | Gen. 7:21 | Gen. viii. 21 | Gen. 8:21 | 353 | f | high |
| note (le poure monde) | perpare | prepare | prepare | 363 | n | high |
| note (blustering dogmas) | like the smoke | like smoke | like smoke | 367 | n | high |

## Book III, chapter 15 — `book-3-chapter-15.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 8 | Summery | Summary | Summary | 374 | d | high |
| §1 justification, if dependent upon works | as justifications | as justification, | justification, | 375 | d/comma | high |
| §4 Ecclesiasticus, the Greek | ἑλεημοσύνῃ | ἐλεημοσύνῃ | ἐλεημοσύνῃ (smooth breathing) | 378 | e | high (verified) |
| §4 Ecclesiasticus, the Greek | τόπον̀ | τόπον· | τόπον· (a raised stop, not a grave accent on ν) | 378 | e | high (verified) |
| §4 Ecclesiasticus, the Greek | αὑτου̑ | αὐτοῦ | αὐτοῦ (smooth breathing; circumflex, not an inverted breve) | 378 | e | high (verified) |
| §6 testimony borne to him in Scripture | that whose believeth | that whoso believeth | whoso | 380 | d | high |
| §6 John 5:24 | He that hearth my word, and believeth in him | He that heareth my word, and believeth on him | heareth ... believeth on him | 380 | d | high |
| §6 is passed from death unto life | Whose believeth | Whoso believeth | Whoso | 380 | d | high |
| §6 an opportunity of procuring justification | procuring justifications | procuring justification, | justification, | 381 | d/comma | high |
| §7 the words of the Apostle | of the Apostles who | of the Apostle, who | Apostle, who | 382 | d/comma | high |
| §8 cut off the root of all evil | all evils so | all evil, so | evil, so | 383 | d/comma | high |
| note (1 Cor. 1:30 ...) | 1\. Cor. 1:30 | 1 Cor. i. 30 | 1 Cor. 1:30 | 381 | f | high |
| note (He that hath the Son ...) | John 5:12; John 5:24; Rom. 3:24; John 3:24 | 1 John v. 12; John v. 24; Rom. iii. 24; 1 John iii. 24 | 1 John 5:12; John 5:24; Rom. 3:24; 1 John 3:24 | 381 | f | high |
| note (2 Cor. 4:8 ... Rom. 8) | Rom. 7:29, 39 | Rom. viii. 29, 39 | Rom. 8:29, 39 | 383 | f | high |

## Book III, chapter 16 — `book-3-chapter-16.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 a stronger argument in exciting us to charity | argument in eliciting | argument in exciting | exciting | 388 | d | high |
| §3 when he comes to exhortation | comes to exhortations beseeches | comes to exhortation, beseeches | exhortation, beseeches | 389 | d/comma | high |
| §3 this one reason | Andy indeed | And, indeed, | And, indeed, | 389 | d | high |
| §3 Chrysostom on Genesis | Chrysost. Homily. | Chrysost. Homil. | Homil. | 389 | d | medium |
| note (This sentence is wholly omitted) | ommitted | omitted | omitted | 386 | n | high |
| note (1 John 4:10, 19 ...) | 1 John 5:10, 19 | 1 John iv. 10, 19 | 1 John 4:10, 19 | 388 | f | high |
| note (Heb. 9:14; 10:29) | 9:14; 10 29; | ix. 14; x. 29 | 9:14; 10:29; | 388 | f | high |

## Book III, chapter 17 — `book-3-chapter-17.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 13 (summary) | but the doors of | but the doers of | doers | 391 | d | high |
| Sections 3 (summary) | #emph[er parts] | ex pacto | #emph[ex pacto] | 391 | e | high |
| Sections 13 (summary) | #emph[reduction ad impossibili] | reductio ad impossibili | #emph[reductio ad impossibili] | 392 | e | high |
| §1 none such are any where to be found | The results therefore is that | The result, therefore, is, that | The result, therefore, is that | 394 | d/comma | high |
| §2 disclaim justification by the law | Therefore, whose will | Therefore, whoso will | whoso | 394 | d | high |
| §2 Ps. 25:10 | saying, “the paths | saying, "All the paths | saying, “All the paths | 395 | b | high |
| §3 Lev. 18:5; Ezek. 20:11 | Ezek. 20:10 | Ezek. xx. 10 | Ezek. 20:11 (1845 has the same misprint; the words quoted are v. 11) | 395 | f | medium |
| §4 except merely his wretchedness | merely big wretchedness | merely his wretchedness | his | 396 | d | high |
| §5 regeneration is a renewal | We have else here said | We have elsewhere said | elsewhere | 398 | d | high |
| §6 God himself fulfils the promise | God himself fulfill the | God himself fulfils the | fulfills | 399 | d | high |
| §7 the Hebrew word חקים | Hebrew word !yqj ¶ has been | Hebrew word חקים has been | Hebrew word חקים has been (CCEL has the Hebrew in font codes, with a false paragraph break after it) | 401 | e | high (verified) |
| §9 a transgressor of the law | life lie is a | life he is a | he | 403 | d | high |
| §12 Abraham justified by faith | How thee can | How then can | then | 408 | d | high |
| §13 greatest despisers | time they where its | time they were its | were | 409 | d | high |
| §14 Ps. 18:20 | The Lord regarded me | The Lord rewarded me | rewarded | 410 | d | high |
| §14 Distrusting their own works | their own words, they | their own works, they | works | 411 | d | high |
| §15 Ezek. 18:9, 21; 33:15 | 18:9, 21; 23:15 | xviii. 9, 21; xxxiii. 15 | 18:9, 21; 33:15 | 412 | f | high |
| §15 perish from the presence of God | or retake themselves | or betake themselves | betake | 412 | d | high |
| note (The French here adds the two following sentences) | Nostre response done est, merites | Nostre response donc est, que quand les œuvres des saincts sont nommées justice, cela ne vient point de leurs merites | Nostre response donc est, que quand les œuvres des saincts sont nommées justice, cela ne vient point de leurs merites | 402 | n | high (verified) |
| note (The whole sentence in French) | stnads | stands | stands | 405 | n | high |
| note (The whole sentence in French) | œvres | oeuvres | œuvres | 405 | n | high |

## Book III, chapter 18 — `book-3-chapter-18.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Every man shall receive his own reward | his own rewards according | his own reward, according | reward, according | 414 | d/comma | high |
| §2 Gal. 4:30 | the bond-women | the bond-woman | bond-woman | 415 | d | high |
| §3 the name of adoption | For this reasons also | For this reason also | reason | 418 | d | high |
| §5 Augustine, precedence of grace | grace which justified the | grace which justifies the | justifies | 419 | d | high |
| §5 what we so strongly maintain | strongly maintains that | strongly maintain, that | maintain, that | 420 | d/comma | high |
| §7 that ye may be counted worthy | (2 Thess. 1:6-7) | (2 Thess. i. 5-7.) | (2 Thess. 1:5-7) | 422 | f | high |
| §7 conformed to Christ the first born | as it behaved him | as it behoved him | behoved | 422 | d | high |
| §9 how should they betake themselves to Christ | should they retake | should they betake | betake | 425 | d | high |
| §9 another remedy | we must retake | we must betake | betake | 426 | d | high |
| note (en misericorde) | judement | judgment | judgment | 420 | n | high |
| note (Answer to Sadolet) | chairty | charity | charity | 423 | n | high |

## Book III, chapter 19 — `book-3-chapter-19.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 1 | with the previous one on | with the previous ones on | ones | 428 | d | high |
| Sections 7 | the free rise of | the free use of | use | 428 | d | high |
| §5 invited by God with paternal lenity | with paternal levity | with paternal lenity | lenity | 433 | d | high |
| §5 God does not regard any work of ours | regard any sock of | regard any work of | work | 433 | d | high |
| §8 forced to do many things repugnant | repugnant to their consciences are | repugnant to their conscience, are | conscience, are | 435 | d/comma | high |
| §8 praise God in their works | God in their words; but not being persuaded shalt these | God in their works; but not being persuaded that these | works ... that | 435 | d | high |
| §9 Isa. 5:12 | the tablet and pipe | the tabret and pipe | tabret | 437 | d | high |
| §9 beds of ivory ... wine in their feasts | (Amos 6:6; Isa. 5:8, 10) | (Amos vi. 6; Is. v. 8, 10.) | (Amos 6:4, 6; Isa. 5:8, 12) (1845 has the same references; beds of ivory is Amos 6:4, the harp and viol Isa. 5:12) | 437 | f | medium |
| §11 sinister interpreters causelessly take offence | interpreters ceaselessly take | interpreters causelessly take | causelessly | 438 | d | high |
| §15 duties as men and citizens | we are bold to performs ( | we are bound to perform, ( | we are bound to perform ( | 443 | d/comma | high |
| §15 of spiritual government | of spiritual governments would | of spiritual government, would | government, would | 444 | d/comma | high |
| §15 by the mind and intellect | mind and intellects are | mind and intellect, are | intellect, are | 444 | d/comma | high |
| §16 1 Tim. 1:5 | of a good consciences and | of a good conscience, and | conscience, and | 444 | d/comma | high |
| note (Rom. 14:1, 13; 15:1 ...) | 13; 16:1; | 13; xv. 1; | 13; 15:1; | 439 | f | high (verified) |

## Book III, chapter 20 — `book-3-chapter-20.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 15 | greatest use. Objection | greatest use. 2. Objection | greatest use. 2. Objection | 447 | b | medium |
| §2 that they may learn by experience | learn by experiences that | learn by experience, that | experience, that | 451 | d/comma | high |
| §3 he wakes and watches for us | watches for use and | watches for us, and | us, and | 452 | d/comma | high |
| §3 no desire, no longing | that no desires, no | that no desire, no | desire | 453 | d | high |
| §3 government of the universe | of the universes is | of the universe, is | universe, is | 453 | d/comma | high |
| §3 The eyes of the Lord are upon the righteous | the psalms to which many others corresponds: | the psalm, to which many others correspond, | the psalm, to which many others correspond: | 453 | d/comma | high |
| §5 vindicating his own right | his own light, places | his own right, places | right | 456 | d | high |
| §7 Isa. 29:13 | heart far from men” | heart far from me," | heart far from me” | 459 | d | high |
| §7 James 4:3 | receive note because | receive not, because | not, because | 459 | d/comma | high |
| §8 Dan. 9:18 | for our righteousness but | for our righteousnesses, but | righteousnesses, but | 460 | d | high |
| §10 John 9:31 | truth, And God | truth, "God | truth, “God | 463 | c | high |
| §10 lay aside all thought of their own merit | own merits and found | own merit, and found | merit, and | 464 | d/comma | high |
| §11 anxiously dreads new evils | at the same times have | at the same time, have | time, have | 465 | d/comma | high |
| §13 Call upon me in the day of trouble | contained in the psalms: | contained in the psalm, | psalm: | 468 | d/comma | high |
| §13 meditation as well on the nature as the word | nature as on the word | nature as the word | nature as the word | 469 | c | medium |
| §14 Jacob, not worthy of the least of all the mercies | (Gen. 32:13) | (Gen. xxxii. 10.) | (Gen. 32:10) | 471 | f | high |
| §16 leave him to perish | leave him to relish in | leave him to perish in | perish | 475 | d | high |
| §16 Lam. 3:8 | shutteth out my prayers” | shutteth out my prayer," | shutteth out my prayer” | 476 | d/comma | high |
| §19 these depend on that one intercession | 1 Tim. 2:1); yet these | 1 Tim. ii. 1;) still these | 1 Tim. 2:1); still these | 480 | d | high |
| §23 for the salvation of the people | salvation of the peoples while | salvation of the people, while | people, while | 485 | d/comma | high |
| §25 Isa. 63:16 | declares in the prophets “Doubtless | declares in the prophet, "Doubtless | prophet, “Doubtless | 488 | d/comma | high |
| §26 Gen. 32:10 | my staff l passed | my staff I passed | I | 490 | d | high |
| §28 1 Tim. 4:5 | word of God and prayers” | word of God and prayer," | word of God and prayer” | 493 | d/comma | high |
| §28 without the word and prayer | word and prayers none | word and prayer, none | prayer, none | 493 | d/comma | high |
| §29 the vain speaking our Saviour prohibited | βαττολογίαν | Βαττολογία | βαττολογία (1845 nominative; CCEL's accusative does not fit "from the") | 495 | e | medium (verified) |
| §34 open our lips before God without danger | without dangers unless | without danger, unless | danger, unless | 503 | d/comma | high |
| §40 Which art in heaven | of the expressions therefore | of the expression, therefore | expression, therefore | 508 | d/comma | high |
| §44 Ps. 4:7 | wine, and oil, so | wine, and oil, (Ps. iv. 8:) so | wine, and oil (Ps. 4:7), so | 514 | b | high |
| §45 Forgive us our debts | FORGIVE ITS OUR | FORGIVE US OUR | US | 516 | d | high |
| §45 the sins of the flesh | remain subject to the | remain obnoxious to the | obnoxious | 517 | d | high |
| §46 temptations presented by the craft of Satan | craft of Satan’s war | craft of Satan, war | Satan, war | 520 | d/comma | high |
| §49 this form of prayer | so restricted to this | so astricted to this | astricted | 523 | d | high |
| §51 the servant of their lusts | servant of their lust, | servant of their lusts, | lusts | 525 | d | high |
| §52 the very terms of our prayer | terms of our prayers but | terms of our prayer, but | prayer, but | 526 | d/comma | high |
| note (et qui sont endormis) | superflous | superfluous | superfluous | 452 | n | high |
| note (The French adds, duquel) | dequel | duquel | duquel | 474 | n | high |
| note (Erasmus to Sadolet) | divcs | divos | divos | 484 | n | high (verified) |
| note (Erasmus to Sadolet) | huc placte | huc placet | huc placet | 484 | n | high (verified) |
| note (Erasmus to Sadolet) | invoction | invocation | invocation | 484 | n | high (verified) |
| note (Mais encore qu'ils taschent) | conleur qu’il ne se commet point en leurs serviteurs | d'autant qu'il ne se commet point en leurs messes ni en leurs vespres; sous quelle couleur defendront ils ces blasphemes qu'il lisent a pleine gorge, ou ils prient St Eloy ou St Medard, de regarder du ciel leurs serviteurs | d’autant qu’il ne se commet point en leurs messes ni en leurs vespres; sous quelle couleur defendront ils ces blasphemes qu’il lisent a pleine gorge, ou ils prient St Eloy ou St Medard, de regarder du ciel leurs serviteurs (CCEL lost a line and a half of the French) | 484 | n | high |
| note (Mais encore qu'ils taschent) | mesmes o˜ ils | mesmes où ils | mesmes où ils | 484 | n | high |
| note (Mais encore qu'ils taschent) | vierge Maire | vierge Marie | Marie | 484 | n | high |
| note (Mais encore qu'ils taschent) | endeavour to was their | endeavour to wash their | wash | 484 | n | high |
| note (C'est chose trop notoire) | bourbieu de quelle | bourbieu ou de quelle | bourbieu ou de quelle | 488 | n | high |
| note (Cette longueur de priere) | aujord’hui | aujourd'hui | aujourd’hui | 496 | n | high |
| note (Cette longueur de priere) | jour et nuiet, et barbotant leur breviare | jour et nuict, et barbotant leur breviaire | nuict ... breviaire | 496 | n | high |
| note (Cette longueur de priere) | among the Papists, over their beads | among the Papists, and proceeds from the same cause: some muttering a host of Ave Marias, and going over their beads | among the Papists, and proceeds from the same cause: some muttering a host of Ave Marias, and going over their beads (CCEL lost a line) | 496 | n | high |
| note (The French adds, où on en avoit) | “o˜ on en | "où on en | “où on en | 500 | n | high |
| note (Mais il adjouste) | quand il souvenoit | quand il se souvenoit | quand il se souvenoit | 500 | n | high |
| note (Qui est-ce donc) | audace tant tent et | audace tant effrenee qu'ont eu les Papistes et ont encore, qui contre la defense de l'Apostre, chantent et | audace tant effrenee qu’ont eu les Papistes et ont encore, qui contre la defense de l’Apostre, chantent et (CCEL lost a line) | 501 | n | high |
| note (Qui est-ce donc) | others uncerstand | others understand | understand | 501 | n | high |
| note (Dont il est facile de juger) | aucuns ent pris | aucuns ont pris | ont | 503 | n | high |
| note (Quelque mauvaistié) | ayons eië | ayons euë | euë | 506 | n | high (verified) |

## Book III, chapter 21 — `book-3-chapter-21.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary of the chapter | sec. l, 2 | sec. 1, 2 | sec. 1, 2 | 528 | d | high |
| Sections 1 | l. The doctrine of Election | 1. The doctrine of Election | 1\. The doctrine of Election (the number keyed as a letter l, so it is not set as a section number) | 528 | d | high |
| §1 others to destruction | How ceaselessly they | How causelessly they | causelessly | 529 | d | high |
| §1 when they inquire into predestination | let then remember | let them remember | them | 530 | d | high |
| §1 inextricable labyrinth | enter in inextricable | enter an inextricable | an | 530 | d | high |
| §5 Deut. 32:8 | nation lives entirely | nation was entirely | was | 534 | d | high |
| §5 Deut. 10:14 | the same intimations, “Behold | the same intimation, "Behold | intimation, “Behold | 535 | d/comma | high |
| §5 Isa. 14:1 | applies the terms “The | applies the term, "The | term, “The | 537 | d/comma | high |
| note (On predestination, Luther) | obsesrvations | observations | observations | 538 | n | high |

## Book III, chapter 22 — `book-3-chapter-22.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 3 | declarations of one Savior | declarations of our Saviour | our Savior | 541 | d | high |
| §2 opening (after Eph. 1:4, 5) | Holiness of life springs from election, and is the object of it2. | 2. | 2\. (CCEL has a line not in 1845 in place of the section number; section 2 is unnumbered) | 544 | c | high |
| §4 blessed in respect of hereditary right | hereditary rights yet | hereditary right, yet | right, yet | 546 | d/comma | high |
| §6 Rom. 11:2, foreknown | inactive contemplations but | inactive contemplation, but | contemplation, but | 549 | d/comma | high |
| §6 1 Pet. 1:20 | in the same chapters that | in the same chapter, that | chapter, that | 549 | d/comma | high |
| §7 Out of the world | in another passages “Out | in another passage, "Out | passage, “Out | 551 | d/comma | high |
| §8 Ambrose, Origen, and Jerome | Ambrose, Origin, and | Ambrose, Origen, and | Origen | 552 | d | high |
| §8 Augustine, elected before the foundation of the world | because God foreknow that | because God foreknew that | foreknew | 552 | d | high |
| §8 had he chosen us | because he foreknow that | because he foreknew that | foreknew | 553 | d | high |
| §9 de Vocatione Gentium | (Ambrose. de Vocat. | (Ambros. de Vocat. | (Ambros. de Vocat. | 554 | d | medium |
| §10 forbidding Paul to preach in Asia | preach in Asian and | preach in Asia, and | Asia, and | 555 | d | high |
| §10 Isa. 53:1 | perversely condemned, | perversely contemned, | contemned | 555 | d | high |
| §10 Bernard, His friends hear apart | “His friend hear | "His friends hear | friends | 556 | d | high |
| §10 Bernard, Epist. 107 | ad Thomas Præpos. | ad Thomam Præpos. | Thomam | 556 | d | high |
| note (Il y en a d'aucuns) | y en a d’a aucuns | y en a d'aucuns | y en a d’aucuns | 542 | n | high |
| note (Il y en a d'aucuns) | ce n’est par raison | ce n'est pas raison | pas | 542 | n | high |

## Book III, chapter 23 — `book-3-chapter-23.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 those whom in lenity he tolerates | whom in levity he | whom in lenity he | lenity | 561 | d | high |
| §4 when they perish in their corruption | their corruptions they | their corruption, they | corruption, they | 564 | d/comma | high |
| §5 Ps. 36:6, the narrowness of your own mind | own minds and say | own mind, and say | mind, and | 566 | d/comma | high |
| §7 Augustine, made all things very good | both foreknow that | both foreknew that | foreknew | 569 | d | high |
| §11 Augustine, De Bono Persever. c. 12 | Gratia; De Bone | Gratia; De Bono | Bono | 573 | d | high |
| §12 they feel secure in vice | in vices because | in vice, because | vice, because | 574 | d/comma | high |
| §13 Augustine, De Bono Persever. c. 15 | treatise, De Bone | treatise, De Bono | Bono | 575 | d | high |
| §13 if God foreknew that they would be wicked | if God foreknow that | if God foreknew that | foreknew | 576 | d | high |
| §14 senseless teachers or sinister and ill-omened prophets | teachers or minister and | teachers or sinister and | sinister | 577 | d | high |
| §14 draws them by the wills which he has wrought | by the will, which | by the wills which | wills which | 577 | d | high |
| note (Si leur constance) | constance er fermeté | constance et fermeté | et | 565 | n | high |
| note (Si leur constance) | bon plasir | bon plaisir | plaisir | 565 | n | high |

## Book III, chapter 24 — `book-3-chapter-24.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Abraham, God's friend | (Isaiah 41:8) | (Isaiah xxiv. 3;) | keep (Isaiah 41:8) (CCEL corrects 1845's misprint) | 583 | info | high (verified) |
| §5 to him also must we betake ourselves | must we retake | must we betake | betake | 586 | d | high |
| §5 a belief of our election animates us to invoke God | animates us to involve | animates us to invoke | invoke | 587 | d | high |
| §17 an asylum from the bondage of sin | they may retake | they may betake | betake | 603 | d | high |
| §17 I have spread out my hands all the day | (Isa. 65:1), exerting | (Isa. lxv. 1,) exerting | (Isa. 65:2), exerting (1845 has the same misprint) | 604 | f | medium |
| note (possibilitatis profectus) | possililitatis | possibilitatis | possibilitatis | 581 | n | high |
| note (Mais quelcun dira) | “Mas quelcun | "Mais quelcun | “Mais quelcun | 588 | n | high |
| note on God's will (§17) | 100 D100 These two assertions | (no such note in 1845) | a modern editor's note (from the 1953 reprint), not Beveridge's: drop it, or keep it marked as a later editor's, without the stray "100 D100" | 604 | n | high |

## Book III, chapter 25 — `book-3-chapter-25.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 11 | Without rewarding questions | Without regarding questions | regarding | 607 | d | high |
| §2 Phil. 3:8, until they reach it | until they reach its | until they reach it, | it | 608 | d/comma | high |
| §5 grace of God and power of Christ | full effects unless | full effect, unless | effect, unless | 616 | d/comma | high |
| §7 2 Cor. 7:1, then denounces the judgment | (2 Cor. 7:1 the judgment | (2 Cor. vii. 1,) and then denounces the judgment | (2 Cor. 7:1), and then denounces the judgment | 618 | b | high |
| §8 from the view of the tomb | view of the tombs which | view of the tomb, which | tomb, which | 622 | d/comma | high |
| §8 Abraham, burial of his wife | the religious views and | the religious view, and | view, and | 622 | d/comma | high |
| §8 Isa. 26:21 | the Lore comes out | the Lord cometh out | the Lord comes out | 624 | d | high |
| §11 every one pleased with his own view | his own views there | his own view, there | view, there | 629 | d/comma | high |
| §12 terrified by his thunderbolt | his thunderbolts and | his thunderbolt, and | thunderbolt, and | 630 | d/comma | high |
| §12 that he may stimulate them | stimulate then, | stimulate them, | them | 630 | d | high |
| note (2 Tim. 1:10 ... Rom. 8:16-18) | Rom. 7:16-18 | Rom. viii. 16-18 | Rom. 8:16-18 | 607 | f | high |
| note (nous recevions un povre salaire) | rench, “nous | French, "nous | French, “nous | 608 | n | high |
| note on the Chiliasts (§5) | 101 D101 Chiliasm | (no such note in 1845) | a modern editor's note (from the 1953 reprint), not Beveridge's: drop it, or keep it marked as a later editor's, without the stray "101 D101" | 622 | n | high |
| note on the Chiliasts (§5) | 102 D102 Calvin’s chief objection | (no such note in 1845) | a modern editor's note (from the 1953 reprint), not Beveridge's: drop it, or keep it marked as a later editor's, without the stray "102 D102" | 622 | n | high |
| note (la question du lieu) | sould | soul | soul | 618 | n | high |
| note (ut vivificas esse doceat) | monstrer quells | monstrer quelles | quelles | 622 | n | high |
| note (Et encore quand nous aurons) | meditation, se nous | meditation, si nous | si | 627 | n | high |

## Notes on the findings

- **The two known items.** III.11 §12 "For the word () is": 1845 prints the
  Hebrew דעת (Isa. 53:11, "by his knowledge"), read on the page image (p. 311).
  III.20 note "divcs": 1845 has "divos" (Erasmus to Sadolet, p. 484, verified);
  the same note also has "huc placte" for "huc placet" and "invoction".
- **Hebrew in font codes:** III.17 §8 "Hebrew word !yqj" is חקים in 1845
  (p. 401, verified), with a false paragraph break after it, as in II.16.
- **Lines lost in French notes:** III.17 (p. 402, "que quand les œuvres des
  saincts sont nommées justice, cela ne vient point de leurs"), III.20 (p. 484,
  a line and a half: "d'autant qu'il ne se commet point en leurs messes ..."),
  III.20 (p. 496, the English "and proceeds from the same cause: some
  muttering a host of Ave Marias, and going"), III.20 (p. 501, "effrenee
  qu'ont eu les Papistes ... chantent").
- **Modern editor's notes:** three footnotes in III.24–25 ("100 D100 These two
  assertions", "101 D101 Chiliasm", "102 D102 Calvin's chief objection") are
  not Beveridge's; they come from the reprint CCEL keyed, with its note
  numbers left in. The editor should decide whether to keep them (marked) or
  drop them.
- **III.22 §2** has no section number; in its place CCEL has a sentence not in
  1845, "Holiness of life springs from election, and is the object of it",
  with the "2" stuck to its end.
- **French accent faults:** "o˜" (U+02DC) for "où" twice in III.20 notes.
- **Scan offset:** n = printed page + 9 to the end of the volume (pp. 583, 604
  region checked).

## Findings as JSON lines

```json
{"file": "book-3-chapter-11.typ", "anchor": "Sections 7", "ccel": "Seventh and eighth arguments.", "1845": "Seventh and eighth arguments. Answers.", "proposed": "Seventh and eighth arguments. Answers.", "page": 301, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§2 a man accused before an impartial judge", "ccel": "by the judge, as a", "1845": "by the judge, so a", "proposed": "so", "page": 303, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§6 Osiander confounds the two gifts", "ccel": "But Scriptures while", "1845": "But Scripture, while", "proposed": "Scripture, while", "page": 309, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§6 Abraham's faith", "ccel": "righteousness of Gad", "1845": "righteousness of God", "proposed": "God", "page": 309, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§8 Isa. 53:11, the Father speaks", "ccel": "For the word () is", "1845": "For the word דעת is", "proposed": "For the word דעת is", "page": 311, "kind": "b", "confidence": "high (verified)"}
{"file": "book-3-chapter-11.typ", "anchor": "§11 Osiander's objection, forensic term", "ccel": "because it behaves", "1845": "because it behoves", "proposed": "behoves", "page": 315, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§11 Hebrew usage of justify", "ccel": "moderately verdant", "1845": "moderately versant", "proposed": "versant", "page": 316, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§11 Paul, Rom. 7:24", "ccel": "but retaking", "1845": "but betaking", "proposed": "betaking", "page": 317, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§11 Moses' intercession", "ccel": "taking affect", "1845": "taking effect", "proposed": "effect", "page": 318, "kind": "d", "confidence": "high (verified)"}
{"file": "book-3-chapter-11.typ", "anchor": "§12 supply the wants of his members", "ccel": "When, although", "1845": "Then, although", "proposed": "Then", "page": 320, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§13 remission of sins", "ccel": "the minutes portion", "1845": "the minutest portion", "proposed": "minutest", "page": 321, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§17 let no prater here allege", "ccel": "no pester here", "1845": "no prater here", "proposed": "prater", "page": 325, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§17 Paul declares", "ccel": "without exceptions that", "1845": "without exception, that", "proposed": "exception, that", "page": 325, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§18 excluding the Law", "ccel": "aided by worlds", "1845": "aided by works", "proposed": "works", "page": 326, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§19 the exclusive word alone", "ccel": "has no part in its and", "1845": "has no part in it, and", "proposed": "it, and", "page": 327, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§19 subterfuge from ancient writers", "ccel": "taken from Origin", "1845": "taken from Origen", "proposed": "Origen", "page": 327, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§20 works of Law", "ccel": "justifying to theme", "1845": "justifying to them,", "proposed": "them", "page": 328, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§20 faith which works by love", "ccel": "love (Gal. 3:6)", "1845": "love, (Gal. v. 6", "proposed": "love (Gal. 5:6)", "page": 329, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§20 Could he express more clearly", "ccel": "than in this word,", "1845": "than in this way,", "proposed": "way", "page": 329, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§21 the wrath of God lies upon all men", "ccel": "to the axioms that", "1845": "to the axiom, that", "proposed": "axiom, that", "page": 329, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§23 Christ communicates his righteousness", "ccel": "wondrous ways in", "1845": "wondrous way, in", "proposed": "way, in", "page": 332, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§23 Christ communicates his righteousness", "ccel": "justice of Gods transfuses", "1845": "justice of God, transfuses", "proposed": "God, transfuses", "page": 332, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§23 obedience of Christ imputed", "ccel": "if it where our", "1845": "if it were our", "proposed": "were", "page": 332, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "§23 Ambrose on Jacob", "ccel": "Vita Beats", "1845": "Vita Beata", "proposed": "Beata", "page": 332, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "note (the two things, To be justified)", "ccel": "as oppopsites", "1845": "as opposites", "proposed": "opposites", "page": 306, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "note (cuttle-fish)", "ccel": "trougle l’eau", "1845": "trouble l'eau", "proposed": "trouble l’eau", "page": 308, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "note (Faisant semblant)", "ccel": "samblant", "1845": "semblant", "proposed": "semblant", "page": 310, "kind": "n", "confidence": "high (verified)"}
{"file": "book-3-chapter-11.typ", "anchor": "note (bonne reputation)", "ccel": "reputation au monde, qu d’etre", "1845": "reputation au monde, que d'etre", "proposed": "que d’etre", "page": 313, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "note (crassa mixtura)", "ccel": "viandes qu nous", "1845": "viandes que nous", "proposed": "que nous", "page": 314, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-11.typ", "anchor": "note (bonnes œuvres des fideles)", "ccel": "Thus they say that has", "1845": "Thus they say that that has", "proposed": "say that that has", "page": 322, "kind": "n", "confidence": "high (verified)"}
{"file": "book-3-chapter-11.typ", "anchor": "note (word Alone)", "ccel": "having it added", "1845": "having added it", "proposed": "having added it", "page": 326, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-12.typ", "anchor": "§1 Who among us shall dwell", "ccel": "says the prophets “shall", "1845": "says the prophet, “shall", "proposed": "prophet, “shall", "page": 335, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-12.typ", "anchor": "§6 thou wilt save the afflicted", "ccel": "hear from the prophets “thou", "1845": "hear from the prophet, “thou", "proposed": "prophet, “thou", "page": 340, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§1 that he might be just, and the justifier", "ccel": "Jesus,” (Rom. 3:25)", "1845": "Jesus,\" (Rom. iii. 25.)", "proposed": "Jesus,” (Rom. 3:26) (1845 has the same misprint; the words quoted are v. 26)", "page": 345, "kind": "f", "confidence": "medium"}
{"file": "book-3-chapter-13.typ", "anchor": "§3 flattery to the judgment of God", "ccel": "without hesitations to", "1845": "without hesitation, to", "proposed": "hesitation, to", "page": 347, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§4 if its fulfillment depends", "ccel": "our merits when pray", "1845": "our merit, when, pray", "proposed": "merit, when, pray", "page": 348, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§4 Augustine on Ps. 88", "ccel": "Tract. 50)", "1845": "Tract. 1.)", "proposed": "Tract. 1)", "page": 348, "kind": "f", "confidence": "high (verified)"}
{"file": "book-3-chapter-13.typ", "anchor": "§4 Bernard, In Dedicatione Templi", "ccel": "(Bert. in", "1845": "(Berd. in", "proposed": "(Bern. in (1845 misprints Berd.)", "page": 349, "kind": "d", "confidence": "medium (verified)"}
{"file": "book-3-chapter-13.typ", "anchor": "§4 Let us thus briefly conclude", "ccel": "are not surer unless", "1845": "are not sure, unless", "proposed": "sure, unless", "page": 349, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§5 the heavenly inheritance", "ccel": "being in grafted", "1845": "being ingrafted", "proposed": "ingrafted", "page": 350, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "§5 faith merely passive", "ccel": "merely passives bringing", "1845": "merely passive, bringing", "proposed": "passive, bringing", "page": 350, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-13.typ", "anchor": "note (two previous sentences)", "ccel": "ommited", "1845": "omitted", "proposed": "omitted", "page": 347, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "Sections 2", "ccel": "blessings of he present", "1845": "blessings of the present", "proposed": "the", "page": 351, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "Sections 17", "ccel": "four different classes", "1845": "four different causes", "proposed": "causes", "page": 352, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§2 Titus and Trajan", "ccel": "Titus and Trojan", "1845": "Titus and Trajan", "proposed": "Trajan", "page": 353, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§3 Augustine against Julian", "ccel": "contra Julia.", "1845": "contra Julian,", "proposed": "contra Julian.", "page": 354, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§7 convicted of a wicked and impious mind", "ccel": "impious minds they", "1845": "impious mind, they", "proposed": "mind, they", "page": 359, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§7 no man, however flagitious", "ccel": "however flagitous", "1845": "however flagitious", "proposed": "flagitious", "page": 359, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§8 Isa. 1:13-16", "ccel": "feasts my foul", "1845": "feasts my soul", "proposed": "soul", "page": 360, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§8 notorious to all", "ccel": "tolerably verdant with Scriptures that", "1845": "tolerably versant with Scripture, that", "proposed": "versant with Scripture, that", "page": 360, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§9 the fourth class", "ccel": "We admits that", "1845": "We admit, that", "proposed": "admit, that", "page": 361, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§9 retarded by much weakness", "ccel": "we see theft the", "1845": "we see that the", "proposed": "that", "page": 361, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§10 constant remission of sins", "ccel": "the statement which we set out", "1845": "the statement with which we set out", "proposed": "with which", "page": 362, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§11 not of works", "ccel": "In like manners when", "1845": "In like manner, when", "proposed": "manner, when", "page": 363, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§15 the boast of Paul", "ccel": "they ceaselessly allege", "1845": "they causelessly allege", "proposed": "causelessly", "page": 366, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§15 blustering dogmas", "ccel": "will behave to", "1845": "will behove to", "proposed": "behove", "page": 367, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§16 to stand dumb", "ccel": "bar of Gods all", "1845": "bar of God, all", "proposed": "God, all", "page": 368, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§20 Bernard, This only I say", "ccel": "this asks this", "1845": "this ask, this", "proposed": "ask, this", "page": 372, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "§20 Bernard, See in me thy work", "ccel": "If thou sees mine, thou condemnest; if thou sees thine", "1845": "If thou seest mine, thou condemnest; if thou seest thine", "proposed": "seest ... seest", "page": 372, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "note (Jer. 17:9; Gen. 8:21 ...)", "ccel": "Gen. 7:21", "1845": "Gen. viii. 21", "proposed": "Gen. 8:21", "page": 353, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "note (le poure monde)", "ccel": "perpare", "1845": "prepare", "proposed": "prepare", "page": 363, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-14.typ", "anchor": "note (blustering dogmas)", "ccel": "like the smoke", "1845": "like smoke", "proposed": "like smoke", "page": 367, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "Sections 8", "ccel": "Summery", "1845": "Summary", "proposed": "Summary", "page": 374, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§1 justification, if dependent upon works", "ccel": "as justifications", "1845": "as justification,", "proposed": "justification,", "page": 375, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§4 Ecclesiasticus, the Greek", "ccel": "ἑλεημοσύνῃ", "1845": "ἐλεημοσύνῃ", "proposed": "ἐλεημοσύνῃ (smooth breathing)", "page": 378, "kind": "e", "confidence": "high (verified)"}
{"file": "book-3-chapter-15.typ", "anchor": "§4 Ecclesiasticus, the Greek", "ccel": "τόπον̀", "1845": "τόπον·", "proposed": "τόπον· (a raised stop, not a grave accent on ν)", "page": 378, "kind": "e", "confidence": "high (verified)"}
{"file": "book-3-chapter-15.typ", "anchor": "§4 Ecclesiasticus, the Greek", "ccel": "αὑτου̑", "1845": "αὐτοῦ", "proposed": "αὐτοῦ (smooth breathing; circumflex, not an inverted breve)", "page": 378, "kind": "e", "confidence": "high (verified)"}
{"file": "book-3-chapter-15.typ", "anchor": "§6 testimony borne to him in Scripture", "ccel": "that whose believeth", "1845": "that whoso believeth", "proposed": "whoso", "page": 380, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6 John 5:24", "ccel": "He that hearth my word, and believeth in him", "1845": "He that heareth my word, and believeth on him", "proposed": "heareth ... believeth on him", "page": 380, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6 is passed from death unto life", "ccel": "Whose believeth", "1845": "Whoso believeth", "proposed": "Whoso", "page": 380, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§6 an opportunity of procuring justification", "ccel": "procuring justifications", "1845": "procuring justification,", "proposed": "justification,", "page": 381, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§7 the words of the Apostle", "ccel": "of the Apostles who", "1845": "of the Apostle, who", "proposed": "Apostle, who", "page": 382, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "§8 cut off the root of all evil", "ccel": "all evils so", "1845": "all evil, so", "proposed": "evil, so", "page": 383, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "note (1 Cor. 1:30 ...)", "ccel": "1\\. Cor. 1:30", "1845": "1 Cor. i. 30", "proposed": "1 Cor. 1:30", "page": 381, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "note (He that hath the Son ...)", "ccel": "John 5:12; John 5:24; Rom. 3:24; John 3:24", "1845": "1 John v. 12; John v. 24; Rom. iii. 24; 1 John iii. 24", "proposed": "1 John 5:12; John 5:24; Rom. 3:24; 1 John 3:24", "page": 381, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-15.typ", "anchor": "note (2 Cor. 4:8 ... Rom. 8)", "ccel": "Rom. 7:29, 39", "1845": "Rom. viii. 29, 39", "proposed": "Rom. 8:29, 39", "page": 383, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§2 a stronger argument in exciting us to charity", "ccel": "argument in eliciting", "1845": "argument in exciting", "proposed": "exciting", "page": 388, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§3 when he comes to exhortation", "ccel": "comes to exhortations beseeches", "1845": "comes to exhortation, beseeches", "proposed": "exhortation, beseeches", "page": 389, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§3 this one reason", "ccel": "Andy indeed", "1845": "And, indeed,", "proposed": "And, indeed,", "page": 389, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "§3 Chrysostom on Genesis", "ccel": "Chrysost. Homily.", "1845": "Chrysost. Homil.", "proposed": "Homil.", "page": 389, "kind": "d", "confidence": "medium"}
{"file": "book-3-chapter-16.typ", "anchor": "note (This sentence is wholly omitted)", "ccel": "ommitted", "1845": "omitted", "proposed": "omitted", "page": 386, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "note (1 John 4:10, 19 ...)", "ccel": "1 John 5:10, 19", "1845": "1 John iv. 10, 19", "proposed": "1 John 4:10, 19", "page": 388, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-16.typ", "anchor": "note (Heb. 9:14; 10:29)", "ccel": "9:14; 10 29;", "1845": "ix. 14; x. 29", "proposed": "9:14; 10:29;", "page": 388, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "Sections 13 (summary)", "ccel": "but the doors of", "1845": "but the doers of", "proposed": "doers", "page": 391, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "Sections 3 (summary)", "ccel": "#emph[er parts]", "1845": "ex pacto", "proposed": "#emph[ex pacto]", "page": 391, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "Sections 13 (summary)", "ccel": "#emph[reduction ad impossibili]", "1845": "reductio ad impossibili", "proposed": "#emph[reductio ad impossibili]", "page": 392, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§1 none such are any where to be found", "ccel": "The results therefore is that", "1845": "The result, therefore, is, that", "proposed": "The result, therefore, is that", "page": 394, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§2 disclaim justification by the law", "ccel": "Therefore, whose will", "1845": "Therefore, whoso will", "proposed": "whoso", "page": 394, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§2 Ps. 25:10", "ccel": "saying, “the paths", "1845": "saying, \"All the paths", "proposed": "saying, “All the paths", "page": 395, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§3 Lev. 18:5; Ezek. 20:11", "ccel": "Ezek. 20:10", "1845": "Ezek. xx. 10", "proposed": "Ezek. 20:11 (1845 has the same misprint; the words quoted are v. 11)", "page": 395, "kind": "f", "confidence": "medium"}
{"file": "book-3-chapter-17.typ", "anchor": "§4 except merely his wretchedness", "ccel": "merely big wretchedness", "1845": "merely his wretchedness", "proposed": "his", "page": 396, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§5 regeneration is a renewal", "ccel": "We have else here said", "1845": "We have elsewhere said", "proposed": "elsewhere", "page": 398, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§6 God himself fulfils the promise", "ccel": "God himself fulfill the", "1845": "God himself fulfils the", "proposed": "fulfills", "page": 399, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§7 the Hebrew word חקים", "ccel": "Hebrew word !yqj\n\nhas been", "1845": "Hebrew word חקים has been", "proposed": "Hebrew word חקים has been (CCEL has the Hebrew in font codes, with a false paragraph break after it)", "page": 401, "kind": "e", "confidence": "high (verified)"}
{"file": "book-3-chapter-17.typ", "anchor": "§9 a transgressor of the law", "ccel": "life lie is a", "1845": "life he is a", "proposed": "he", "page": 403, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§12 Abraham justified by faith", "ccel": "How thee can", "1845": "How then can", "proposed": "then", "page": 408, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§13 greatest despisers", "ccel": "time they where its", "1845": "time they were its", "proposed": "were", "page": 409, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§14 Ps. 18:20", "ccel": "The Lord regarded me", "1845": "The Lord rewarded me", "proposed": "rewarded", "page": 410, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§14 Distrusting their own works", "ccel": "their own words, they", "1845": "their own works, they", "proposed": "works", "page": 411, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§15 Ezek. 18:9, 21; 33:15", "ccel": "18:9, 21; 23:15", "1845": "xviii. 9, 21; xxxiii. 15", "proposed": "18:9, 21; 33:15", "page": 412, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "§15 perish from the presence of God", "ccel": "or retake themselves", "1845": "or betake themselves", "proposed": "betake", "page": 412, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "note (The French here adds the two following sentences)", "ccel": "Nostre response done est, merites", "1845": "Nostre response donc est, que quand les œuvres des saincts sont nommées justice, cela ne vient point de leurs merites", "proposed": "Nostre response donc est, que quand les œuvres des saincts sont nommées justice, cela ne vient point de leurs merites", "page": 402, "kind": "n", "confidence": "high (verified)"}
{"file": "book-3-chapter-17.typ", "anchor": "note (The whole sentence in French)", "ccel": "stnads", "1845": "stands", "proposed": "stands", "page": 405, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-17.typ", "anchor": "note (The whole sentence in French)", "ccel": "œvres", "1845": "oeuvres", "proposed": "œuvres", "page": 405, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§1 Every man shall receive his own reward", "ccel": "his own rewards according", "1845": "his own reward, according", "proposed": "reward, according", "page": 414, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§2 Gal. 4:30", "ccel": "the bond-women", "1845": "the bond-woman", "proposed": "bond-woman", "page": 415, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§3 the name of adoption", "ccel": "For this reasons also", "1845": "For this reason also", "proposed": "reason", "page": 418, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§5 Augustine, precedence of grace", "ccel": "grace which justified the", "1845": "grace which justifies the", "proposed": "justifies", "page": 419, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§5 what we so strongly maintain", "ccel": "strongly maintains that", "1845": "strongly maintain, that", "proposed": "maintain, that", "page": 420, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§7 that ye may be counted worthy", "ccel": "(2 Thess. 1:6-7)", "1845": "(2 Thess. i. 5-7.)", "proposed": "(2 Thess. 1:5-7)", "page": 422, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§7 conformed to Christ the first born", "ccel": "as it behaved him", "1845": "as it behoved him", "proposed": "behoved", "page": 422, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§9 how should they betake themselves to Christ", "ccel": "should they retake", "1845": "should they betake", "proposed": "betake", "page": 425, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "§9 another remedy", "ccel": "we must retake", "1845": "we must betake", "proposed": "betake", "page": 426, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "note (en misericorde)", "ccel": "judement", "1845": "judgment", "proposed": "judgment", "page": 420, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-18.typ", "anchor": "note (Answer to Sadolet)", "ccel": "chairty", "1845": "charity", "proposed": "charity", "page": 423, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "Sections 1", "ccel": "with the previous one on", "1845": "with the previous ones on", "proposed": "ones", "page": 428, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "Sections 7", "ccel": "the free rise of", "1845": "the free use of", "proposed": "use", "page": 428, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§5 invited by God with paternal lenity", "ccel": "with paternal levity", "1845": "with paternal lenity", "proposed": "lenity", "page": 433, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§5 God does not regard any work of ours", "ccel": "regard any sock of", "1845": "regard any work of", "proposed": "work", "page": 433, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§8 forced to do many things repugnant", "ccel": "repugnant to their consciences are", "1845": "repugnant to their conscience, are", "proposed": "conscience, are", "page": 435, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§8 praise God in their works", "ccel": "God in their words; but not being persuaded shalt these", "1845": "God in their works; but not being persuaded that these", "proposed": "works ... that", "page": 435, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§9 Isa. 5:12", "ccel": "the tablet and pipe", "1845": "the tabret and pipe", "proposed": "tabret", "page": 437, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§9 beds of ivory ... wine in their feasts", "ccel": "(Amos 6:6; Isa. 5:8, 10)", "1845": "(Amos vi. 6; Is. v. 8, 10.)", "proposed": "(Amos 6:4, 6; Isa. 5:8, 12) (1845 has the same references; beds of ivory is Amos 6:4, the harp and viol Isa. 5:12)", "page": 437, "kind": "f", "confidence": "medium"}
{"file": "book-3-chapter-19.typ", "anchor": "§11 sinister interpreters causelessly take offence", "ccel": "interpreters ceaselessly take", "1845": "interpreters causelessly take", "proposed": "causelessly", "page": 438, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§15 duties as men and citizens", "ccel": "we are bold to performs (", "1845": "we are bound to perform, (", "proposed": "we are bound to perform (", "page": 443, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§15 of spiritual government", "ccel": "of spiritual governments would", "1845": "of spiritual government, would", "proposed": "government, would", "page": 444, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§15 by the mind and intellect", "ccel": "mind and intellects are", "1845": "mind and intellect, are", "proposed": "intellect, are", "page": 444, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "§16 1 Tim. 1:5", "ccel": "of a good consciences and", "1845": "of a good conscience, and", "proposed": "conscience, and", "page": 444, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-19.typ", "anchor": "note (Rom. 14:1, 13; 15:1 ...)", "ccel": "13; 16:1;", "1845": "13; xv. 1;", "proposed": "13; 15:1;", "page": 439, "kind": "f", "confidence": "high (verified)"}
{"file": "book-3-chapter-20.typ", "anchor": "Sections 15", "ccel": "greatest use. Objection", "1845": "greatest use. 2. Objection", "proposed": "greatest use. 2. Objection", "page": 447, "kind": "b", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§2 that they may learn by experience", "ccel": "learn by experiences that", "1845": "learn by experience, that", "proposed": "experience, that", "page": 451, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§3 he wakes and watches for us", "ccel": "watches for use and", "1845": "watches for us, and", "proposed": "us, and", "page": 452, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§3 no desire, no longing", "ccel": "that no desires, no", "1845": "that no desire, no", "proposed": "desire", "page": 453, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§3 government of the universe", "ccel": "of the universes is", "1845": "of the universe, is", "proposed": "universe, is", "page": 453, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§3 The eyes of the Lord are upon the righteous", "ccel": "the psalms to which many others corresponds:", "1845": "the psalm, to which many others correspond,", "proposed": "the psalm, to which many others correspond:", "page": 453, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§5 vindicating his own right", "ccel": "his own light, places", "1845": "his own right, places", "proposed": "right", "page": 456, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§7 Isa. 29:13", "ccel": "heart far from men”", "1845": "heart far from me,\"", "proposed": "heart far from me”", "page": 459, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§7 James 4:3", "ccel": "receive note because", "1845": "receive not, because", "proposed": "not, because", "page": 459, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§8 Dan. 9:18", "ccel": "for our righteousness but", "1845": "for our righteousnesses, but", "proposed": "righteousnesses, but", "page": 460, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§10 John 9:31", "ccel": "truth, And God", "1845": "truth, \"God", "proposed": "truth, “God", "page": 463, "kind": "c", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§10 lay aside all thought of their own merit", "ccel": "own merits and found", "1845": "own merit, and found", "proposed": "merit, and", "page": 464, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§11 anxiously dreads new evils", "ccel": "at the same times have", "1845": "at the same time, have", "proposed": "time, have", "page": 465, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§13 Call upon me in the day of trouble", "ccel": "contained in the psalms:", "1845": "contained in the psalm,", "proposed": "psalm:", "page": 468, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§13 meditation as well on the nature as the word", "ccel": "nature as on the word", "1845": "nature as the word", "proposed": "nature as the word", "page": 469, "kind": "c", "confidence": "medium"}
{"file": "book-3-chapter-20.typ", "anchor": "§14 Jacob, not worthy of the least of all the mercies", "ccel": "(Gen. 32:13)", "1845": "(Gen. xxxii. 10.)", "proposed": "(Gen. 32:10)", "page": 471, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§16 leave him to perish", "ccel": "leave him to relish in", "1845": "leave him to perish in", "proposed": "perish", "page": 475, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§16 Lam. 3:8", "ccel": "shutteth out my prayers”", "1845": "shutteth out my prayer,\"", "proposed": "shutteth out my prayer”", "page": 476, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§19 these depend on that one intercession", "ccel": "1 Tim. 2:1); yet these", "1845": "1 Tim. ii. 1;) still these", "proposed": "1 Tim. 2:1); still these", "page": 480, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§23 for the salvation of the people", "ccel": "salvation of the peoples while", "1845": "salvation of the people, while", "proposed": "people, while", "page": 485, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§25 Isa. 63:16", "ccel": "declares in the prophets “Doubtless", "1845": "declares in the prophet, \"Doubtless", "proposed": "prophet, “Doubtless", "page": 488, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§26 Gen. 32:10", "ccel": "my staff l passed", "1845": "my staff I passed", "proposed": "I", "page": 490, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§28 1 Tim. 4:5", "ccel": "word of God and prayers”", "1845": "word of God and prayer,\"", "proposed": "word of God and prayer”", "page": 493, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§28 without the word and prayer", "ccel": "word and prayers none", "1845": "word and prayer, none", "proposed": "prayer, none", "page": 493, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§29 the vain speaking our Saviour prohibited", "ccel": "βαττολογίαν", "1845": "Βαττολογία", "proposed": "βαττολογία (1845 nominative; CCEL's accusative does not fit \"from the\")", "page": 495, "kind": "e", "confidence": "medium (verified)"}
{"file": "book-3-chapter-20.typ", "anchor": "§34 open our lips before God without danger", "ccel": "without dangers unless", "1845": "without danger, unless", "proposed": "danger, unless", "page": 503, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§40 Which art in heaven", "ccel": "of the expressions therefore", "1845": "of the expression, therefore", "proposed": "expression, therefore", "page": 508, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§44 Ps. 4:7", "ccel": "wine, and oil, so", "1845": "wine, and oil, (Ps. iv. 8:) so", "proposed": "wine, and oil (Ps. 4:7), so", "page": 514, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§45 Forgive us our debts", "ccel": "FORGIVE ITS OUR", "1845": "FORGIVE US OUR", "proposed": "US", "page": 516, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§45 the sins of the flesh", "ccel": "remain subject to the", "1845": "remain obnoxious to the", "proposed": "obnoxious", "page": 517, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§46 temptations presented by the craft of Satan", "ccel": "craft of Satan’s war", "1845": "craft of Satan, war", "proposed": "Satan, war", "page": 520, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§49 this form of prayer", "ccel": "so restricted to this", "1845": "so astricted to this", "proposed": "astricted", "page": 523, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§51 the servant of their lusts", "ccel": "servant of their lust,", "1845": "servant of their lusts,", "proposed": "lusts", "page": 525, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "§52 the very terms of our prayer", "ccel": "terms of our prayers but", "1845": "terms of our prayer, but", "proposed": "prayer, but", "page": 526, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (et qui sont endormis)", "ccel": "superflous", "1845": "superfluous", "proposed": "superfluous", "page": 452, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (The French adds, duquel)", "ccel": "dequel", "1845": "duquel", "proposed": "duquel", "page": 474, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Erasmus to Sadolet)", "ccel": "divcs", "1845": "divos", "proposed": "divos", "page": 484, "kind": "n", "confidence": "high (verified)"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Erasmus to Sadolet)", "ccel": "huc placte", "1845": "huc placet", "proposed": "huc placet", "page": 484, "kind": "n", "confidence": "high (verified)"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Erasmus to Sadolet)", "ccel": "invoction", "1845": "invocation", "proposed": "invocation", "page": 484, "kind": "n", "confidence": "high (verified)"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Mais encore qu'ils taschent)", "ccel": "conleur qu’il ne se commet point en leurs serviteurs", "1845": "d'autant qu'il ne se commet point en leurs messes ni en leurs vespres; sous quelle couleur defendront ils ces blasphemes qu'il lisent a pleine gorge, ou ils prient St Eloy ou St Medard, de regarder du ciel leurs serviteurs", "proposed": "d’autant qu’il ne se commet point en leurs messes ni en leurs vespres; sous quelle couleur defendront ils ces blasphemes qu’il lisent a pleine gorge, ou ils prient St Eloy ou St Medard, de regarder du ciel leurs serviteurs (CCEL lost a line and a half of the French)", "page": 484, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Mais encore qu'ils taschent)", "ccel": "mesmes o˜ ils", "1845": "mesmes où ils", "proposed": "mesmes où ils", "page": 484, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Mais encore qu'ils taschent)", "ccel": "vierge Maire", "1845": "vierge Marie", "proposed": "Marie", "page": 484, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Mais encore qu'ils taschent)", "ccel": "endeavour to was their", "1845": "endeavour to wash their", "proposed": "wash", "page": 484, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (C'est chose trop notoire)", "ccel": "bourbieu de quelle", "1845": "bourbieu ou de quelle", "proposed": "bourbieu ou de quelle", "page": 488, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Cette longueur de priere)", "ccel": "aujord’hui", "1845": "aujourd'hui", "proposed": "aujourd’hui", "page": 496, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Cette longueur de priere)", "ccel": "jour et nuiet, et barbotant leur breviare", "1845": "jour et nuict, et barbotant leur breviaire", "proposed": "nuict ... breviaire", "page": 496, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Cette longueur de priere)", "ccel": "among the Papists, over their beads", "1845": "among the Papists, and proceeds from the same cause: some muttering a host of Ave Marias, and going over their beads", "proposed": "among the Papists, and proceeds from the same cause: some muttering a host of Ave Marias, and going over their beads (CCEL lost a line)", "page": 496, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (The French adds, où on en avoit)", "ccel": "“o˜ on en", "1845": "\"où on en", "proposed": "“où on en", "page": 500, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Mais il adjouste)", "ccel": "quand il souvenoit", "1845": "quand il se souvenoit", "proposed": "quand il se souvenoit", "page": 500, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Qui est-ce donc)", "ccel": "audace tant tent et", "1845": "audace tant effrenee qu'ont eu les Papistes et ont encore, qui contre la defense de l'Apostre, chantent et", "proposed": "audace tant effrenee qu’ont eu les Papistes et ont encore, qui contre la defense de l’Apostre, chantent et (CCEL lost a line)", "page": 501, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Qui est-ce donc)", "ccel": "others uncerstand", "1845": "others understand", "proposed": "understand", "page": 501, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Dont il est facile de juger)", "ccel": "aucuns ent pris", "1845": "aucuns ont pris", "proposed": "ont", "page": 503, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-20.typ", "anchor": "note (Quelque mauvaistié)", "ccel": "ayons eië", "1845": "ayons euë", "proposed": "euë", "page": 506, "kind": "n", "confidence": "high (verified)"}
{"file": "book-3-chapter-21.typ", "anchor": "summary of the chapter", "ccel": "sec. l, 2", "1845": "sec. 1, 2", "proposed": "sec. 1, 2", "page": 528, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "Sections 1", "ccel": "l. The doctrine of Election", "1845": "1. The doctrine of Election", "proposed": "1\\. The doctrine of Election (the number keyed as a letter l, so it is not set as a section number)", "page": 528, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§1 others to destruction", "ccel": "How ceaselessly they", "1845": "How causelessly they", "proposed": "causelessly", "page": 529, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§1 when they inquire into predestination", "ccel": "let then remember", "1845": "let them remember", "proposed": "them", "page": 530, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§1 inextricable labyrinth", "ccel": "enter in inextricable", "1845": "enter an inextricable", "proposed": "an", "page": 530, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§5 Deut. 32:8", "ccel": "nation lives entirely", "1845": "nation was entirely", "proposed": "was", "page": 534, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§5 Deut. 10:14", "ccel": "the same intimations, “Behold", "1845": "the same intimation, \"Behold", "proposed": "intimation, “Behold", "page": 535, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "§5 Isa. 14:1", "ccel": "applies the terms “The", "1845": "applies the term, \"The", "proposed": "term, “The", "page": 537, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-21.typ", "anchor": "note (On predestination, Luther)", "ccel": "obsesrvations", "1845": "observations", "proposed": "observations", "page": 538, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "Sections 3", "ccel": "declarations of one Savior", "1845": "declarations of our Saviour", "proposed": "our Savior", "page": 541, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§2 opening (after Eph. 1:4, 5)", "ccel": "Holiness of life springs from election, and is the object of it2.", "1845": "2.", "proposed": "2\\. (CCEL has a line not in 1845 in place of the section number; section 2 is unnumbered)", "page": 544, "kind": "c", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§4 blessed in respect of hereditary right", "ccel": "hereditary rights yet", "1845": "hereditary right, yet", "proposed": "right, yet", "page": 546, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§6 Rom. 11:2, foreknown", "ccel": "inactive contemplations but", "1845": "inactive contemplation, but", "proposed": "contemplation, but", "page": 549, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§6 1 Pet. 1:20", "ccel": "in the same chapters that", "1845": "in the same chapter, that", "proposed": "chapter, that", "page": 549, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§7 Out of the world", "ccel": "in another passages “Out", "1845": "in another passage, \"Out", "proposed": "passage, “Out", "page": 551, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§8 Ambrose, Origen, and Jerome", "ccel": "Ambrose, Origin, and", "1845": "Ambrose, Origen, and", "proposed": "Origen", "page": 552, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§8 Augustine, elected before the foundation of the world", "ccel": "because God foreknow that", "1845": "because God foreknew that", "proposed": "foreknew", "page": 552, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§8 had he chosen us", "ccel": "because he foreknow that", "1845": "because he foreknew that", "proposed": "foreknew", "page": 553, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§9 de Vocatione Gentium", "ccel": "(Ambrose. de Vocat.", "1845": "(Ambros. de Vocat.", "proposed": "(Ambros. de Vocat.", "page": 554, "kind": "d", "confidence": "medium"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 forbidding Paul to preach in Asia", "ccel": "preach in Asian and", "1845": "preach in Asia, and", "proposed": "Asia, and", "page": 555, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 Isa. 53:1", "ccel": "perversely condemned,", "1845": "perversely contemned,", "proposed": "contemned", "page": 555, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 Bernard, His friends hear apart", "ccel": "“His friend hear", "1845": "\"His friends hear", "proposed": "friends", "page": 556, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "§10 Bernard, Epist. 107", "ccel": "ad Thomas Præpos.", "1845": "ad Thomam Præpos.", "proposed": "Thomam", "page": 556, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "note (Il y en a d'aucuns)", "ccel": "y en a d’a aucuns", "1845": "y en a d'aucuns", "proposed": "y en a d’aucuns", "page": 542, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-22.typ", "anchor": "note (Il y en a d'aucuns)", "ccel": "ce n’est par raison", "1845": "ce n'est pas raison", "proposed": "pas", "page": 542, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§1 those whom in lenity he tolerates", "ccel": "whom in levity he", "1845": "whom in lenity he", "proposed": "lenity", "page": 561, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§4 when they perish in their corruption", "ccel": "their corruptions they", "1845": "their corruption, they", "proposed": "corruption, they", "page": 564, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§5 Ps. 36:6, the narrowness of your own mind", "ccel": "own minds and say", "1845": "own mind, and say", "proposed": "mind, and", "page": 566, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§7 Augustine, made all things very good", "ccel": "both foreknow that", "1845": "both foreknew that", "proposed": "foreknew", "page": 569, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§11 Augustine, De Bono Persever. c. 12", "ccel": "Gratia; De Bone", "1845": "Gratia; De Bono", "proposed": "Bono", "page": 573, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§12 they feel secure in vice", "ccel": "in vices because", "1845": "in vice, because", "proposed": "vice, because", "page": 574, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13 Augustine, De Bono Persever. c. 15", "ccel": "treatise, De Bone", "1845": "treatise, De Bono", "proposed": "Bono", "page": 575, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§13 if God foreknew that they would be wicked", "ccel": "if God foreknow that", "1845": "if God foreknew that", "proposed": "foreknew", "page": 576, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§14 senseless teachers or sinister and ill-omened prophets", "ccel": "teachers or minister and", "1845": "teachers or sinister and", "proposed": "sinister", "page": 577, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "§14 draws them by the wills which he has wrought", "ccel": "by the will, which", "1845": "by the wills which", "proposed": "wills which", "page": 577, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "note (Si leur constance)", "ccel": "constance er fermeté", "1845": "constance et fermeté", "proposed": "et", "page": 565, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-23.typ", "anchor": "note (Si leur constance)", "ccel": "bon plasir", "1845": "bon plaisir", "proposed": "plaisir", "page": 565, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§2 Abraham, God's friend", "ccel": "(Isaiah 41:8)", "1845": "(Isaiah xxiv. 3;)", "proposed": "keep (Isaiah 41:8) (CCEL corrects 1845's misprint)", "page": 583, "kind": "info", "confidence": "high (verified)"}
{"file": "book-3-chapter-24.typ", "anchor": "§5 to him also must we betake ourselves", "ccel": "must we retake", "1845": "must we betake", "proposed": "betake", "page": 586, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§5 a belief of our election animates us to invoke God", "ccel": "animates us to involve", "1845": "animates us to invoke", "proposed": "invoke", "page": 587, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§17 an asylum from the bondage of sin", "ccel": "they may retake", "1845": "they may betake", "proposed": "betake", "page": 603, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "§17 I have spread out my hands all the day", "ccel": "(Isa. 65:1), exerting", "1845": "(Isa. lxv. 1,) exerting", "proposed": "(Isa. 65:2), exerting (1845 has the same misprint)", "page": 604, "kind": "f", "confidence": "medium"}
{"file": "book-3-chapter-24.typ", "anchor": "note (possibilitatis profectus)", "ccel": "possililitatis", "1845": "possibilitatis", "proposed": "possibilitatis", "page": 581, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "note (Mais quelcun dira)", "ccel": "“Mas quelcun", "1845": "\"Mais quelcun", "proposed": "“Mais quelcun", "page": 588, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-24.typ", "anchor": "note on God's will (§17)", "ccel": "100 D100 These two assertions", "1845": "(no such note in 1845)", "proposed": "a modern editor's note (from the 1953 reprint), not Beveridge's: drop it, or keep it marked as a later editor's, without the stray \"100 D100\"", "page": 604, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "Sections 11", "ccel": "Without rewarding questions", "1845": "Without regarding questions", "proposed": "regarding", "page": 607, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§2 Phil. 3:8, until they reach it", "ccel": "until they reach its", "1845": "until they reach it,", "proposed": "it", "page": 608, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§5 grace of God and power of Christ", "ccel": "full effects unless", "1845": "full effect, unless", "proposed": "effect, unless", "page": 616, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§7 2 Cor. 7:1, then denounces the judgment", "ccel": "(2 Cor. 7:1 the judgment", "1845": "(2 Cor. vii. 1,) and then denounces the judgment", "proposed": "(2 Cor. 7:1), and then denounces the judgment", "page": 618, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§8 from the view of the tomb", "ccel": "view of the tombs which", "1845": "view of the tomb, which", "proposed": "tomb, which", "page": 622, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§8 Abraham, burial of his wife", "ccel": "the religious views and", "1845": "the religious view, and", "proposed": "view, and", "page": 622, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§8 Isa. 26:21", "ccel": "the Lore comes out", "1845": "the Lord cometh out", "proposed": "the Lord comes out", "page": 624, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§11 every one pleased with his own view", "ccel": "his own views there", "1845": "his own view, there", "proposed": "view, there", "page": 629, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§12 terrified by his thunderbolt", "ccel": "his thunderbolts and", "1845": "his thunderbolt, and", "proposed": "thunderbolt, and", "page": 630, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "§12 that he may stimulate them", "ccel": "stimulate then,", "1845": "stimulate them,", "proposed": "them", "page": 630, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "note (2 Tim. 1:10 ... Rom. 8:16-18)", "ccel": "Rom. 7:16-18", "1845": "Rom. viii. 16-18", "proposed": "Rom. 8:16-18", "page": 607, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "note (nous recevions un povre salaire)", "ccel": "rench, “nous", "1845": "French, \"nous", "proposed": "French, “nous", "page": 608, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "note on the Chiliasts (§5)", "ccel": "101 D101 Chiliasm", "1845": "(no such note in 1845)", "proposed": "a modern editor's note (from the 1953 reprint), not Beveridge's: drop it, or keep it marked as a later editor's, without the stray \"101 D101\"", "page": 622, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "note on the Chiliasts (§5)", "ccel": "102 D102 Calvin’s chief objection", "1845": "(no such note in 1845)", "proposed": "a modern editor's note (from the 1953 reprint), not Beveridge's: drop it, or keep it marked as a later editor's, without the stray \"102 D102\"", "page": 622, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "note (la question du lieu)", "ccel": "sould", "1845": "soul", "proposed": "soul", "page": 618, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "note (ut vivificas esse doceat)", "ccel": "monstrer quells", "1845": "monstrer quelles", "proposed": "quelles", "page": 622, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-25.typ", "anchor": "note (Et encore quand nous aurons)", "ccel": "meditation, se nous", "1845": "meditation, si nous", "proposed": "si", "page": 627, "kind": "n", "confidence": "high"}
```
