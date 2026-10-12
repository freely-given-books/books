# Calvin, Institutes, vol. 6 (Book IV, chapters 14–20): CCEL vs the 1845 printing

Base: `chapters/typ/vol-6/*.typ` (CCEL text, the 1953 reprint's marked
editorial notes already removed). Witness: Calvin Translation Society,
Edinburgh 1845, vol. 3 (archive.org `institutesofthec03calvuoft`): Book IV,
chapters 14–20, pp. 299–554. The OCR was aligned word by word with the
edition (difflib; scripts in `scratchpad/calvin-v6/`, adapted from the vol-5
agent's: `align.py` writes raw candidates to `cand-*.txt`, `notes.py` and
`fnl.py` compare every footnote with the 1845 notes, findings in
`findings.jsonl`, `add.py` and `build.py` check that every "ccel" string
occurs exactly once in its file). Doubtful places were read on the page
images (crops in `scratchpad/calvin-pages/`, files `r*.jpg`, `cr*.png`).

**Scan offset (measured):** scan index n = printed page + 3 throughout this
volume (read on the images of pp. 300 = n303 and later pages listed below).
"verified" in the confidence column = read on the image. Otherwise the OCR
reading is an unambiguous real word in clean OCR.

**Kinds:** **b** = 1845 words missing in CCEL. **c** = CCEL words not in 1845.
**d** = a different word (also a stop for a comma). **d/comma** = CCEL turned
the comma after a word into a final "s". **e** = Greek/Latin/Hebrew/French.
**f** = reference numbers (proposed in CCEL's Arabic style). **n** = notes
(including any note, or part of one, that 1845 does not have: proposed
"drop"). **s** = section or summary numbering. **info** = CCEL departs from
1845 but corrects a misprint there; keep CCEL.

**Not listed one by one (CCEL-wide editorial choices, kept by the edition):**
Arabic numerals in references; CCEL's spellings (baptise/baptize,
rebaptise, confectioneries); has/does/comes for hath/doth/cometh in
Scripture quotations; CCEL's punctuation around references; closed-up
compounds.

## Book IV, chapter 14 — `book-4-chapter-14.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §4 Acts 15:9 | “Purify their hearts by faith” | “Purifying their hearts by faith,” | “Purifying their hearts by faith” | 302 | d | high |
| §14 the seal of a sacrament | than by the seal of the sacrament | than by the seal of a sacrament | than by the seal of a sacrament | 313 | d | high |
| §17 We must beware | We must be aware of being led | We must beware of being led | We must beware of being led | 316 | d | high |
| §21 Rom. 4:11 | faith (Rom. 9:11) | faith, (Rom. iv. 11 | faith (Rom. 4:11) | 320 | f | high |
| §22 if you compare | that, it you compare | that, if you compare | that, if you compare | 321 | d | high |
| §23 actually confer it | actually confer that it | actually confer it | actually confer it | 322 | c | high |
| §25 which I lately quoted | which I lately quote | which I lately quoted, | which I lately quoted | 324 | d | high |
| §26 Ep. ad Januar. | Ep. ad Janur. | Ep. ad Januar. | Ep. ad Januar. | 326 | d | high |
| §26 not only false, but | is not only false. but | is not only false, but | is not only false, but | 326 | d | high |
| note on “passive”: French | “J’appel le acte passif | “J’appelle acte passif | “J’appelle acte passif | 326 | e | high |

## Book IV, chapter 15 — `book-4-chapter-15.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 4 (no stop after the number, so not set as item 4) | 4 Refutation of those | 4. Refutation of those | 4\. Refutation of those | 327 | s | high |
| Sections 5 (no stop after the number, so not set as item 5) | 5 Second thing in Baptism | 5. Second thing in Baptism | 5\. Second thing in Baptism | 327 | s | high |
| §1 commander, have not attended | commander, having not attended | commander, have not attended | commander, have not attended | 328 | d | high |
| §18 that they know not | that they knew not whether | that they know not whether | that they know not whether | 342 | d | high |
| §19 a benediction | a benedicion, or rather | a benediction, or rather | a benediction, or rather | 343 | d | high |
| note on the mode of baptism (French): digit 1 for l | en 1’Eglise | en l’Eglise | en l’Eglise | 344 | e | high |
| §22 there is neither sloth | sign, their is neither | sign, there is neither | sign, there is neither | 347 | d | high |

## Book IV, chapter 16 — `book-4-chapter-16.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 10 (no stop after the number, so not set as item 10) | 10 Second part of the chapter | 10. Second part of the chapter | 10\. Second part of the chapter | 350 | s | high |
| note on the opening (French) | pouroient faire teis seducteurs | pourroient faire tels seducteurs | pourroient faire tels seducteurs | 351 | e | verified |
| §7 βρέφη: π for ρ | βπέφη | βρέφη | βρέφη | 357 | e | verified |
| §13 kingdom of God began | the kingdom began to be extended | the kingdom of God began to be extended | the kingdom of God began to be extended | 361 | b | high |
| §16 baptism as the burial | baptism as a burial | baptism as the burial | baptism as the burial | 365 | d | high |
| §16 the rite could only be performed | though the right could | though the rite could | though the rite could | 366 | d | high |
| §20 against God than against us | God then against us | God than against us | God than against us | 369 | d | high |
| §20 by the fact | by the tact, that children | by the fact, that children | by the fact, that children | 369 | d | high |
| §22 1 Cor. 12:13 | (1 Cor. 7:13) | (1 Cor. xii. 13,) | (1 Cor. 12:13) | 372 | f | high |
| §23 his advice is | his advise is | his advice is | his advice is | 372 | d | high |
| §29 on the pretence | on the presence that | on the pretence that | on the pretence that | 378 | d | high |
| §29 no greater | in the present instance is not greater | in the present instance is no greater | in the present instance is no greater | 378 | d | high |
| note on Servetus (French) | toutesfeis | toutesfois | toutesfois | 380 | e | high |
| §31 He next falsely quotes | He nexts falsely | He next falsely | He next falsely | 381 | d | high |
| §31 they still required | they still require to be imbued | they still required to be imbued | they still required to be imbued | 382 | d | high |
| §32 their posterity | in their prosperity! | in their posterity! | in their posterity! | 385 | d | high |
| §32 not only would | not on\]y would | not only would | not only would | 385 | d | high |

## Book IV, chapter 17 — `book-4-chapter-17.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 14 (summary): The term transubstantiation | The term of transubstantiation | The term transubstantiation | The term transubstantiation | 387 | c | high |
| §5 would not have been the bread of life | would not have not been the bread | would not have been the bread | would not have been the bread | 392 | c | high |
| §11 all the other benefits | and all other benefits | and all the other benefits | and all the other benefits | 399 | b | high |
| §12 rather inclines | absurdity, rathers inclines | absurdity, rather inclines | absurdity, rather inclines | 400 | d | high |
| §15 the allusion to the rods | attend to the illusion to | attend to the allusion to | attend to the allusion to | 405 | d | high |
| §15 allegorise the expressions | allegorise the expression to mean | allegorise the expressions to mean | allegorise the expressions to mean | 406 | d | high |
| §18 must be separate from the blood | must be separated from the blood, included | must be separate from the blood, included | must be separate from the blood, included | 408 | d | high |
| §20 saying, Take, eat | disciples, saving, Take | disciples, saying, Take | disciples, saying, Take | 409 | d | high |
| §20 I am now only considering | I am not only considering | I am now only considering | I am now only considering | 410 | d | high |
| §22 1 Cor. 12:12 | (1 Cor. 7:12) | (1 Cor. xii. 12,) | (1 Cor. 12:12) | 414 | f | high |
| §24 darkness to be darkness, and flesh | darkness to be darkness, flesh to be flesh | darkness to be darkness, and flesh to be flesh | darkness to be darkness, and flesh to be flesh | 418 | b | high |
| §26 This saying, also | This saving, also | This saying, also | This saying, also | 420 | d | high |
| §26 When Christ said | When Christ says, “Me | When Christ said, “Me | When Christ said, “Me | 421 | d | high |
| §27 bidding us to look | bidding us look for him | bidding us to look for him | bidding us to look for him | 422 | b | high |
| §28 well-known passage | another well-know passage | another well-known passage | another well-known passage | 423 | d | high |
| §28 corporeal absence | leave in coporeal absence | leave in corporeal absence | leave in corporeal absence | 425 | d | high |
| §29 this hiding-place | confidence in his hiding-place | confidence in this hiding-place | confidence in this hiding-place | 425 | d | high |
| §29 the place of a first principle | occupying the place of the first principle | occupying the place of a first principle | occupying the place of a first principle | 425 | d | high |
| §29 Moreover | Morever, how weak | Moreover, how weak | Moreover, how weak | 427 | d | high |
| §29 wished to be sought | wished to he sought | wished to be sought | wished to be sought | 427 | d | high |
| §29 journeyed to Emmaus | had journed to Emmaus | had journeyed to Emmaus | had journeyed to Emmaus | 428 | d | high |
| §29 on the journey with them | on the journeying with them | on the journey with them | on the journey with them | 428 | d | high |
| §30 corporeally | Christ coporeally, that is | Christ corporeally, that is | Christ corporeally, that is | 430 | d | high |
| §32 Every spirit (1 John 4:3) | “Ever spirit that | “Every spirit that | “Every spirit that | 432 | d | high |
| §33 No better founded | Not better founded | No better founded | No better founded | 433 | d | high |
| §33 1 Cor. 11:27 | (1 Cor. 11:7) | (1 Cor. xi. 27 | (1 Cor. 11:27) | 435 | f | high |
| §34 Augustine especially maintained | Augustine especially maintaine | Augustine especially maintained | Augustine especially maintained | 435 | d | high |
| §34 Cont. Faust. Lib. 13 | Faust. Lib. 8 c. 16 | Faust. Lib. xiii. c. 16 | Faust. Lib. 13 c. 16 | 437 | f | high |
| §34 what the wicked take to the visible sign | the wicked take to be the visible sign | the wicked take to the visible sign | the wicked take to the visible sign | 437 | c | high |
| §35 dissolve the apprehension | dissolve the apprehensions by | dissolve the apprehension by | dissolve the apprehension by | 439 | d | high |
| §39 be impressed and seated | their minds, being impressed | their minds, be impressed | their minds, be impressed | 444 | d | high |
| §40 1 Cor. 11:28 (letter l for 1) | (l Cor. 11:28) | (1 Cor. xi. 28.) | (1 Cor. 11:28) | 445 | f | high |
| §43 these frigid and histrionic follies | these rigid and histrionic | these frigid and histrionic | these frigid and histrionic | 448 | d | high |
| §45 Chrysostom: Why have you taken your seat? | Why have you not taken your seat? | Why have you taken your seat? | Why have you taken your seat? | 451 | c | verified |
| §48 said Ambrose | “How,” says Ambrose | “How,” said Ambrose | “How,” said Ambrose | 454 | d | high |
| §49 only a portion | taking only the portion | taking only a portion | taking only a portion | 455 | d | high |
| note on Calvin's writings: Eccles. | Vera Eceles. | Vera Eccles. | Vera Eccles. | 453 | d | high |
| §20 will be to begin (digit 1 for l) | course wil1 be | course will be | course will be | 409 | d | high |

## Book IV, chapter 18 — `book-4-chapter-18.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| chapter title: the 1845 note on “Chapter XVIII.” is missing in CCEL (add it after the title) | ANNIHILATES THE LORD’S SUPPER. | CHAPTER XVIII.¹ … ANNIHILATES THE LORD’S SUPPER. — ¹ Vid. Calv. Ep. de Fugiend. Illic. Sacris. Item, De Sacerdotiis Eccles. Papal. Item, De Necessitate Reform. Eccles. Item, Epist. ad Sadoletum. | ANNIHILATES THE LORD’S SUPPER.#footnote[Vid. Calv. Ep. de Fugiend. Illic. Sacris. Item, De Sacerdotiis Eccles. Papal. Item, De Necessitate Reform. Eccles. Item, Epist. ad Sadoletum.] | 457 | n | verified |
| summary: Its origin described, sec. 8, 9 | described. sec. 8 | described, sec. 8 | described, sec. 8 | 457 | d | verified |
| summary: respecting the sacraments | respecting sacraments | respecting the sacraments | respecting the sacraments | 457 | b | verified |
| note on Heb. 7:17, 21 | 7:17; 21; | vii. 17, 21 ; | 7:17, 21; | 459 | f | high |
| §10 contend, on their authority | contend, or their | contend, on their | contend, on their | 467 | d | high |
| §13 προσφορὰ: π for ρ | προσφοπὰ, | προσφορὰ, | προσφορὰ, | 470 | e | verified |
| §13 τελετὴ: stray ν | τελετνὴ. | τελετὴ. | τελετὴ. | 470 | e | verified |
| §13 λατρευτικὸν: π for ρ | λατπευτικὸν, | λατρευτικὸν, | λατρευτικὸν, | 471 | e | verified |
| §13 σεβαστικὸν: χ for κ | σεβαστιχὸν, | σεβαστικὸν, | σεβαστικὸν, | 471 | e | verified |
| note on “no human authority”: French n’aucun | n’ancun authorite | n’aucun authorite | n’aucun authorite | 470 | e | high |
| §12 same note: nor length of time | no length of time | nor length of time | nor length of time | 470 | d | high |
| §16 saith the Lord of hosts (Mal. 1:11) | said the Lord | saith the Lord | saith the Lord | 474 | d | high |
| §17 1 Pet. 2:9 (letter l for 1) | name (l Pet | name, (1 Peter ii. 9 | name (1 Pet | 474 | f | high |
| §17 he the altar (1845 elliptical) | he is the altar | he the altar | he the altar | 475 | c | verified |
| note on types: Num. 20:8; 21:9 | 20:8., 21:9 | xx. 8 ; xxi. 9 | 20:8; 21:9 | 477 | f | high |

## Book IV, chapter 19 — `book-4-chapter-19.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 from a love of wrangling | a word for love | a word from a love | a word from a love | 481 | d | high |
| §2 a seal of the attestation | seal of attestation | seal of the attestation | seal of the attestation | 482 | b | high |
| §3 nowhere found in ecclesiastical writers | found in the ecclesiastical | found in ecclesiastical | found in ecclesiastical | 483 | c | high |
| §3 external rites | external writs | external rites | external rites | 483 | d | high |
| §3 the principal point | the principle point | the principal point | the principal point | 483 | d | high |
| §5 interrogated | interogated | interrogated | interrogated | 485 | d | high |
| §7 1 Cor. 6:13 (letter l for 1) | them” (l Cor | them,” (1 Cor. vi. 13.) | them” (1 Cor | 488 | f | high |
| §16 the good and the bad | good and bad alike | good and the bad alike | good and the bad alike | 496 | b | high |
| §18 the gift of healing | gift of hearing | gift of healing | gift of healing | 499 | d | high |
| §23 most notable | most noteable | most notable | most notable | 504 | d | high |
| §25 mortified the concupiscence | mortified concupiscence | mortified the concupiscence | mortified the concupiscence | 506 | b | high |
| §29 as if they were bringing | and, as they were bringing | and, as if they were bringing | and, as if they were bringing | 509 | b | high |
| §30 spiritual gifts (digit 1 for l) | spiritua1 | spiritual | spiritual | 510 | d | high |
| §33 What pious man could be induced | pious man can be | pious man could be | pious man could be | 513 | d | high |
| §35 which he had espoused | which he has espoused | which he had espoused | which he had espoused | 514 | d | high |
| §36 μυστήριον: π for ρ, accent lost | μυστηπιον | μυστήριον | μυστήριον | 515 | e | verified |
| note on the Supper's antiquity (French): temps | du ternps | du temps | du temps | 488 | e | high |
| note on the keys (French): avons | avoos | avons | avons | 497 | e | high |
| note on the orders: Mark 7:33 (1845 misprints the same, Matth. vii. 33: Matthew 7 has 29 verses; the exorcist's office, Christ's fingers in the deaf man's ears) | Mt. 7:33 | Matth. vii. 33 | Mark 7:33 | 503 | f | medium |
| note on “sacrament” (French): Ils ont ete | Ills ont eto | Ils ont ete | Ils ont ete | 515 | e | verified |
| note on marriage: Decret. 32 | in Decret. 33 | in Decret. 32 | in Decret. 32 | 515 | f | verified |

## Book IV, chapter 20 — `book-4-chapter-20.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 12 (no stop after the number, so not set as item 12) | 12 Objection, that the lawfulness | 12. Objection, that the lawfulness | 12\. Objection, that the lawfulness | 519 | s | high |
| §10 desirous to approve their piety | desirous to improve | desirous to approve | desirous to approve | 532 | d | high |
| note on magistrates' duty (French): tous ses | tou sses | tous ses | tous ses | 531 | e | high |
| §10 same note: toutesfois | toutes fois | toutesfois | toutesfois | 531 | e | high |
| §10 same note: n’empeche | empeehe | empeche | empeche | 531 | e | high |
| §10 same note: laquelle | laquelie | laquelle | laquelle | 531 | e | high |
| note on Moses: Acts 7:24 (1845 misprints the same, Acts vii. 21; Moses smote the Egyptian, 7:24) | Exod 2:12; Acts 7:21 | Exod. ii. 12 ; Acts vii. 21 | Exod 2:12; Acts 7:24 | 532 | f | medium |
| note on Proverbs: 17:11 (1845 misprints the same, xvii. 14; the quoted verse “An evil man seeketh only rebellion” is 17:11). The next reference, 24:24, is right in CCEL (1845 xxiv. 21) | 17:15; 17:14 | xvii. 15 ; xvii. 14 | 17:15; 17:11 | 532 | f | medium |
| §10 Prov. 25:5: Take away the wicked from | wicked men from | wicked from | wicked from | 533 | c | verified |
| §10 Prov. 17:15: they both are abomination | both are an abomination | both are abomination | both are abomination | 533 | c | high |
| §11 injuries inflicted | been afflicted | been inflicted | been inflicted | 534 | d | high |
| §12 the soldiers asked counsel | soldiers ask counsel | soldiers asked counsel | soldiers asked counsel | 534 | d | high |
| §16 Equity cannot but be the same in all (CCEL reverses the sense) | cannot be the same | cannot but be the same | cannot but be the same | 538 | b | high |
| §16 in a troubled condition | is in troubled | is in a troubled | is in a troubled | 539 | b | high |
| §17 What deference ought | What difference ought | What deference ought | What deference ought | 539 | d | high |
| §18 bitterness and hatred | bitterness or hatred | bitterness and hatred | bitterness and hatred | 540 | d | high |
| §19 judicial discussion | judicial distinction | judicial discussion | judicial discussion | 541 | d | high |
| §19 some bad man | some bad men | some bad man | some bad man | 541 | d | high |
| §19 Rom. 13:4 | (Rom. 13:8) | (Rom. xiii. 4.) | (Rom. 13:4) | 542 | f | high |
| §22 wicked and flagitious | wicked or flagitious | wicked and flagitious | wicked and flagitious | 544 | d | high |
| note on Job 34:30 etc.: semicolon | 10:5: Deut | x. 5 ; Deut | 10:5; Deut | 547 | f | high |
| §26 1 Sam. 8:11-17 (letter l for 1) | 8:11-l7 | viii. 11-17 | 8:11-17 | 548 | f | high |
| §27 with the pestilence (Jer. 27:8) | with pestilence | with the pestilence | with the pestilence | 549 | b | high |
| §28 Mine eye spared thee (1 Sam. 24:10) | Mine eyes spare | Mine eye spared | Mine eye spared | 550 | d | high |
| §28 1 Sam. 24 (letter l for 1; 1845 has xxvi. 9-11, but the words quoted are 1 Sam. 24:6, 10, so CCEL's chapter is kept) | (l Sam. 24 | (1 Sam. xxvi. 9-11.) | (1 Sam. 24 | 550 | f | high |
| §31 fraudulently | fradulently | fraudulently | fraudulently | 553 | d | high |

## Notes: only the 1845 printing's own

Every footnote in vol-6 (66 in all) was compared with the 1845 notes
(`notes.py`, and `fnl.py`, which lists the 1845 note lines of each chapter
beside CCEL's notes). Each chapter has the same notes as 1845, in the same
places. No 1953 matter survives, with or without a "D" marker, and no
Beveridge note has anything appended:

- IV.15 §19, the note on the mode of baptism (French "Au reste, c’est une
  chose de nulle importance…" with Beveridge's translation): it ends, as
  in 1845, at "…anciently observed in the Church." The 1953 essay on the
  mode of baptism that followed it in CCEL is gone; nothing of it remains
  in the note or the text after it (§20 follows directly).
- One 1845 note is missing in CCEL (kind n above): the note on the title of
  IV.18 ("Vid. Calv. Ep. de Fugiend. Illic. Sacris…"), p. 457.

## Other checks

- Section and summary numbering checked in every file: the body sections
  are complete in all seven chapters; four summary items lack the stop
  after their number (IV.15 items 4 and 5, IV.16 item 10, IV.20 item 12),
  so they are not set as numbered items (kind s).
- No missing, doubled or displaced lines: every run of 1845 text left
  unmatched by the alignment was a running head, a signature mark or a
  footnote.
- Greek and Hebrew: no Greek in old font codes, no private-use characters,
  no Hebrew, no empty "()" where a word was lost. The Greek of vol-6 was read
  on the images where it looked wrong: five words keyed with π for ρ, χ for κ
  or a stray letter (βπέφη, προσφοπὰ, τελετνὴ, λατπευτικὸν, σεβαστιχὸν,
  μυστηπιον), all listed. θυσια is unaccented in 1845 too; μυστήριον
  (IV.14), κυβερνήσεις (IV.20) and ευχαριστικὸν (IV.18) match the page.
- Digit for letter: "1’Eglise", "spiritua1", "wil1", and "l" for "1" in five
  references ("l Cor.", "l Pet.", "l Sam.", "11-l7"); all listed.
- French notes: accent and letter faults listed (J’appel le, pouroient/teis,
  toutesfeis, ternps, avoos, Ills ont eto, n’ancun, tou sses, laquelie,
  empeehe). 1845's own forms ("doit demeura", "il ne sont") are kept.
- Scan offset n = printed page + 3 holds to the end (pp. 300, 351, 457,
  515, 533 read).
- No comma keyed as a final "s" was found in this volume, as in vol-5.
- Not listed: spelling differences (baptise/baptize, sty/stye, embued,
  sprung/sprang, amidst/amid, confectioneries, carcasses, enroll), OCR noise
  ("Horn." for "Hom.", fl read as "n": "nourished" for "flourished",
  "earnest" for "camest"), and 1845 misprints CCEL silently corrects in
  references (e.g. IV.20 note: Prov. 24:24 for xxiv. 21; IV.17 1 John 4:3).

## Findings as JSON lines

```json
{"file": "book-4-chapter-14.typ", "anchor": "§4 Acts 15:9", "ccel": "“Purify their hearts by faith”", "1845": "“Purifying their hearts by faith,”", "proposed": "“Purifying their hearts by faith”", "page": 302, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "§14 the seal of a sacrament", "ccel": "than by the seal of the sacrament", "1845": "than by the seal of a sacrament", "proposed": "than by the seal of a sacrament", "page": 313, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "§17 We must beware", "ccel": "We must be aware of being led", "1845": "We must beware of being led", "proposed": "We must beware of being led", "page": 316, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "§21 Rom. 4:11", "ccel": "faith (Rom. 9:11)", "1845": "faith, (Rom. iv. 11", "proposed": "faith (Rom. 4:11)", "page": 320, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "§22 if you compare", "ccel": "that, it you compare", "1845": "that, if you compare", "proposed": "that, if you compare", "page": 321, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "§23 actually confer it", "ccel": "actually confer that it", "1845": "actually confer it", "proposed": "actually confer it", "page": 322, "kind": "c", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "§25 which I lately quoted", "ccel": "which I lately quote", "1845": "which I lately quoted,", "proposed": "which I lately quoted", "page": 324, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "§26 Ep. ad Januar.", "ccel": "Ep. ad Janur.", "1845": "Ep. ad Januar.", "proposed": "Ep. ad Januar.", "page": 326, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "§26 not only false, but", "ccel": "is not only false. but", "1845": "is not only false, but", "proposed": "is not only false, but", "page": 326, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-14.typ", "anchor": "note on “passive”: French", "ccel": "“J’appel le acte passif", "1845": "“J’appelle acte passif", "proposed": "“J’appelle acte passif", "page": 326, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-15.typ", "anchor": "Sections 4 (no stop after the number, so not set as item 4)", "ccel": "4 Refutation of those", "1845": "4. Refutation of those", "proposed": "4\\. Refutation of those", "page": 327, "kind": "s", "confidence": "high"}
{"file": "book-4-chapter-15.typ", "anchor": "Sections 5 (no stop after the number, so not set as item 5)", "ccel": "5 Second thing in Baptism", "1845": "5. Second thing in Baptism", "proposed": "5\\. Second thing in Baptism", "page": 327, "kind": "s", "confidence": "high"}
{"file": "book-4-chapter-15.typ", "anchor": "§1 commander, have not attended", "ccel": "commander, having not attended", "1845": "commander, have not attended", "proposed": "commander, have not attended", "page": 328, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-15.typ", "anchor": "§18 that they know not", "ccel": "that they knew not whether", "1845": "that they know not whether", "proposed": "that they know not whether", "page": 342, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-15.typ", "anchor": "§19 a benediction", "ccel": "a benedicion, or rather", "1845": "a benediction, or rather", "proposed": "a benediction, or rather", "page": 343, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-15.typ", "anchor": "note on the mode of baptism (French): digit 1 for l", "ccel": "en 1’Eglise", "1845": "en l’Eglise", "proposed": "en l’Eglise", "page": 344, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-15.typ", "anchor": "§22 there is neither sloth", "ccel": "sign, their is neither", "1845": "sign, there is neither", "proposed": "sign, there is neither", "page": 347, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "Sections 10 (no stop after the number, so not set as item 10)", "ccel": "10 Second part of the chapter", "1845": "10. Second part of the chapter", "proposed": "10\\. Second part of the chapter", "page": 350, "kind": "s", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "note on the opening (French)", "ccel": "pouroient faire teis seducteurs", "1845": "pourroient faire tels seducteurs", "proposed": "pourroient faire tels seducteurs", "page": 351, "kind": "e", "confidence": "verified"}
{"file": "book-4-chapter-16.typ", "anchor": "§7 βρέφη: π for ρ", "ccel": "βπέφη", "1845": "βρέφη", "proposed": "βρέφη", "page": 357, "kind": "e", "confidence": "verified"}
{"file": "book-4-chapter-16.typ", "anchor": "§13 kingdom of God began", "ccel": "the kingdom began to be extended", "1845": "the kingdom of God began to be extended", "proposed": "the kingdom of God began to be extended", "page": 361, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§16 baptism as the burial", "ccel": "baptism as a burial", "1845": "baptism as the burial", "proposed": "baptism as the burial", "page": 365, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§16 the rite could only be performed", "ccel": "though the right could", "1845": "though the rite could", "proposed": "though the rite could", "page": 366, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§20 against God than against us", "ccel": "God then against us", "1845": "God than against us", "proposed": "God than against us", "page": 369, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§20 by the fact", "ccel": "by the tact, that children", "1845": "by the fact, that children", "proposed": "by the fact, that children", "page": 369, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§22 1 Cor. 12:13", "ccel": "(1 Cor. 7:13)", "1845": "(1 Cor. xii. 13,)", "proposed": "(1 Cor. 12:13)", "page": 372, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§23 his advice is", "ccel": "his advise is", "1845": "his advice is", "proposed": "his advice is", "page": 372, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§29 on the pretence", "ccel": "on the presence that", "1845": "on the pretence that", "proposed": "on the pretence that", "page": 378, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§29 no greater", "ccel": "in the present instance is not greater", "1845": "in the present instance is no greater", "proposed": "in the present instance is no greater", "page": 378, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "note on Servetus (French)", "ccel": "toutesfeis", "1845": "toutesfois", "proposed": "toutesfois", "page": 380, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§31 He next falsely quotes", "ccel": "He nexts falsely", "1845": "He next falsely", "proposed": "He next falsely", "page": 381, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§31 they still required", "ccel": "they still require to be imbued", "1845": "they still required to be imbued", "proposed": "they still required to be imbued", "page": 382, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§32 their posterity", "ccel": "in their prosperity!", "1845": "in their posterity!", "proposed": "in their posterity!", "page": 385, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-16.typ", "anchor": "§32 not only would", "ccel": "not on\\]y would", "1845": "not only would", "proposed": "not only would", "page": 385, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "Sections 14 (summary): The term transubstantiation", "ccel": "The term of transubstantiation", "1845": "The term transubstantiation", "proposed": "The term transubstantiation", "page": 387, "kind": "c", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§5 would not have been the bread of life", "ccel": "would not have not been the bread", "1845": "would not have been the bread", "proposed": "would not have been the bread", "page": 392, "kind": "c", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§11 all the other benefits", "ccel": "and all other benefits", "1845": "and all the other benefits", "proposed": "and all the other benefits", "page": 399, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§12 rather inclines", "ccel": "absurdity, rathers inclines", "1845": "absurdity, rather inclines", "proposed": "absurdity, rather inclines", "page": 400, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§15 the allusion to the rods", "ccel": "attend to the illusion to", "1845": "attend to the allusion to", "proposed": "attend to the allusion to", "page": 405, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§15 allegorise the expressions", "ccel": "allegorise the expression to mean", "1845": "allegorise the expressions to mean", "proposed": "allegorise the expressions to mean", "page": 406, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§18 must be separate from the blood", "ccel": "must be separated from the blood, included", "1845": "must be separate from the blood, included", "proposed": "must be separate from the blood, included", "page": 408, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§20 saying, Take, eat", "ccel": "disciples, saving, Take", "1845": "disciples, saying, Take", "proposed": "disciples, saying, Take", "page": 409, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§20 I am now only considering", "ccel": "I am not only considering", "1845": "I am now only considering", "proposed": "I am now only considering", "page": 410, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§22 1 Cor. 12:12", "ccel": "(1 Cor. 7:12)", "1845": "(1 Cor. xii. 12,)", "proposed": "(1 Cor. 12:12)", "page": 414, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§24 darkness to be darkness, and flesh", "ccel": "darkness to be darkness, flesh to be flesh", "1845": "darkness to be darkness, and flesh to be flesh", "proposed": "darkness to be darkness, and flesh to be flesh", "page": 418, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§26 This saying, also", "ccel": "This saving, also", "1845": "This saying, also", "proposed": "This saying, also", "page": 420, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§26 When Christ said", "ccel": "When Christ says, “Me", "1845": "When Christ said, “Me", "proposed": "When Christ said, “Me", "page": 421, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§27 bidding us to look", "ccel": "bidding us look for him", "1845": "bidding us to look for him", "proposed": "bidding us to look for him", "page": 422, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§28 well-known passage", "ccel": "another well-know passage", "1845": "another well-known passage", "proposed": "another well-known passage", "page": 423, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§28 corporeal absence", "ccel": "leave in coporeal absence", "1845": "leave in corporeal absence", "proposed": "leave in corporeal absence", "page": 425, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§29 this hiding-place", "ccel": "confidence in his hiding-place", "1845": "confidence in this hiding-place", "proposed": "confidence in this hiding-place", "page": 425, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§29 the place of a first principle", "ccel": "occupying the place of the first principle", "1845": "occupying the place of a first principle", "proposed": "occupying the place of a first principle", "page": 425, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§29 Moreover", "ccel": "Morever, how weak", "1845": "Moreover, how weak", "proposed": "Moreover, how weak", "page": 427, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§29 wished to be sought", "ccel": "wished to he sought", "1845": "wished to be sought", "proposed": "wished to be sought", "page": 427, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§29 journeyed to Emmaus", "ccel": "had journed to Emmaus", "1845": "had journeyed to Emmaus", "proposed": "had journeyed to Emmaus", "page": 428, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§29 on the journey with them", "ccel": "on the journeying with them", "1845": "on the journey with them", "proposed": "on the journey with them", "page": 428, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§30 corporeally", "ccel": "Christ coporeally, that is", "1845": "Christ corporeally, that is", "proposed": "Christ corporeally, that is", "page": 430, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§32 Every spirit (1 John 4:3)", "ccel": "“Ever spirit that", "1845": "“Every spirit that", "proposed": "“Every spirit that", "page": 432, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§33 No better founded", "ccel": "Not better founded", "1845": "No better founded", "proposed": "No better founded", "page": 433, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§33 1 Cor. 11:27", "ccel": "(1 Cor. 11:7)", "1845": "(1 Cor. xi. 27", "proposed": "(1 Cor. 11:27)", "page": 435, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§34 Augustine especially maintained", "ccel": "Augustine especially maintaine", "1845": "Augustine especially maintained", "proposed": "Augustine especially maintained", "page": 435, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§34 Cont. Faust. Lib. 13", "ccel": "Faust. Lib. 8 c. 16", "1845": "Faust. Lib. xiii. c. 16", "proposed": "Faust. Lib. 13 c. 16", "page": 437, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§34 what the wicked take to the visible sign", "ccel": "the wicked take to be the visible sign", "1845": "the wicked take to the visible sign", "proposed": "the wicked take to the visible sign", "page": 437, "kind": "c", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§35 dissolve the apprehension", "ccel": "dissolve the apprehensions by", "1845": "dissolve the apprehension by", "proposed": "dissolve the apprehension by", "page": 439, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§39 be impressed and seated", "ccel": "their minds, being impressed", "1845": "their minds, be impressed", "proposed": "their minds, be impressed", "page": 444, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§40 1 Cor. 11:28 (letter l for 1)", "ccel": "(l Cor. 11:28)", "1845": "(1 Cor. xi. 28.)", "proposed": "(1 Cor. 11:28)", "page": 445, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§43 these frigid and histrionic follies", "ccel": "these rigid and histrionic", "1845": "these frigid and histrionic", "proposed": "these frigid and histrionic", "page": 448, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§45 Chrysostom: Why have you taken your seat?", "ccel": "Why have you not taken your seat?", "1845": "Why have you taken your seat?", "proposed": "Why have you taken your seat?", "page": 451, "kind": "c", "confidence": "verified"}
{"file": "book-4-chapter-17.typ", "anchor": "§48 said Ambrose", "ccel": "“How,” says Ambrose", "1845": "“How,” said Ambrose", "proposed": "“How,” said Ambrose", "page": 454, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§49 only a portion", "ccel": "taking only the portion", "1845": "taking only a portion", "proposed": "taking only a portion", "page": 455, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "note on Calvin's writings: Eccles.", "ccel": "Vera Eceles.", "1845": "Vera Eccles.", "proposed": "Vera Eccles.", "page": 453, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "chapter title: the 1845 note on “Chapter XVIII.” is missing in CCEL (add it after the title)", "ccel": "ANNIHILATES THE LORD’S SUPPER.", "1845": "CHAPTER XVIII.¹ … ANNIHILATES THE LORD’S SUPPER. — ¹ Vid. Calv. Ep. de Fugiend. Illic. Sacris. Item, De Sacerdotiis Eccles. Papal. Item, De Necessitate Reform. Eccles. Item, Epist. ad Sadoletum.", "proposed": "ANNIHILATES THE LORD’S SUPPER.#footnote[Vid. Calv. Ep. de Fugiend. Illic. Sacris. Item, De Sacerdotiis Eccles. Papal. Item, De Necessitate Reform. Eccles. Item, Epist. ad Sadoletum.]", "page": 457, "kind": "n", "confidence": "verified"}
{"file": "book-4-chapter-18.typ", "anchor": "summary: Its origin described, sec. 8, 9", "ccel": "described. sec. 8", "1845": "described, sec. 8", "proposed": "described, sec. 8", "page": 457, "kind": "d", "confidence": "verified"}
{"file": "book-4-chapter-18.typ", "anchor": "summary: respecting the sacraments", "ccel": "respecting sacraments", "1845": "respecting the sacraments", "proposed": "respecting the sacraments", "page": 457, "kind": "b", "confidence": "verified"}
{"file": "book-4-chapter-18.typ", "anchor": "note on Heb. 7:17, 21", "ccel": "7:17; 21;", "1845": "vii. 17, 21 ;", "proposed": "7:17, 21;", "page": 459, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§10 contend, on their authority", "ccel": "contend, or their", "1845": "contend, on their", "proposed": "contend, on their", "page": 467, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§13 προσφορὰ: π for ρ", "ccel": "προσφοπὰ,", "1845": "προσφορὰ,", "proposed": "προσφορὰ,", "page": 470, "kind": "e", "confidence": "verified"}
{"file": "book-4-chapter-18.typ", "anchor": "§13 τελετὴ: stray ν", "ccel": "τελετνὴ.", "1845": "τελετὴ.", "proposed": "τελετὴ.", "page": 470, "kind": "e", "confidence": "verified"}
{"file": "book-4-chapter-18.typ", "anchor": "§13 λατρευτικὸν: π for ρ", "ccel": "λατπευτικὸν,", "1845": "λατρευτικὸν,", "proposed": "λατρευτικὸν,", "page": 471, "kind": "e", "confidence": "verified"}
{"file": "book-4-chapter-18.typ", "anchor": "§13 σεβαστικὸν: χ for κ", "ccel": "σεβαστιχὸν,", "1845": "σεβαστικὸν,", "proposed": "σεβαστικὸν,", "page": 471, "kind": "e", "confidence": "verified"}
{"file": "book-4-chapter-18.typ", "anchor": "note on “no human authority”: French n’aucun", "ccel": "n’ancun authorite", "1845": "n’aucun authorite", "proposed": "n’aucun authorite", "page": 470, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§12 same note: nor length of time", "ccel": "no length of time", "1845": "nor length of time", "proposed": "nor length of time", "page": 470, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§16 saith the Lord of hosts (Mal. 1:11)", "ccel": "said the Lord", "1845": "saith the Lord", "proposed": "saith the Lord", "page": 474, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§17 1 Pet. 2:9 (letter l for 1)", "ccel": "name (l Pet", "1845": "name, (1 Peter ii. 9", "proposed": "name (1 Pet", "page": 474, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-18.typ", "anchor": "§17 he the altar (1845 elliptical)", "ccel": "he is the altar", "1845": "he the altar", "proposed": "he the altar", "page": 475, "kind": "c", "confidence": "verified"}
{"file": "book-4-chapter-18.typ", "anchor": "note on types: Num. 20:8; 21:9", "ccel": "20:8., 21:9", "1845": "xx. 8 ; xxi. 9", "proposed": "20:8; 21:9", "page": 477, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§1 from a love of wrangling", "ccel": "a word for love", "1845": "a word from a love", "proposed": "a word from a love", "page": 481, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§2 a seal of the attestation", "ccel": "seal of attestation", "1845": "seal of the attestation", "proposed": "seal of the attestation", "page": 482, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§3 nowhere found in ecclesiastical writers", "ccel": "found in the ecclesiastical", "1845": "found in ecclesiastical", "proposed": "found in ecclesiastical", "page": 483, "kind": "c", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§3 external rites", "ccel": "external writs", "1845": "external rites", "proposed": "external rites", "page": 483, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§3 the principal point", "ccel": "the principle point", "1845": "the principal point", "proposed": "the principal point", "page": 483, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§5 interrogated", "ccel": "interogated", "1845": "interrogated", "proposed": "interrogated", "page": 485, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§7 1 Cor. 6:13 (letter l for 1)", "ccel": "them” (l Cor", "1845": "them,” (1 Cor. vi. 13.)", "proposed": "them” (1 Cor", "page": 488, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§16 the good and the bad", "ccel": "good and bad alike", "1845": "good and the bad alike", "proposed": "good and the bad alike", "page": 496, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§18 the gift of healing", "ccel": "gift of hearing", "1845": "gift of healing", "proposed": "gift of healing", "page": 499, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§23 most notable", "ccel": "most noteable", "1845": "most notable", "proposed": "most notable", "page": 504, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§25 mortified the concupiscence", "ccel": "mortified concupiscence", "1845": "mortified the concupiscence", "proposed": "mortified the concupiscence", "page": 506, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§29 as if they were bringing", "ccel": "and, as they were bringing", "1845": "and, as if they were bringing", "proposed": "and, as if they were bringing", "page": 509, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§30 spiritual gifts (digit 1 for l)", "ccel": "spiritua1", "1845": "spiritual", "proposed": "spiritual", "page": 510, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§33 What pious man could be induced", "ccel": "pious man can be", "1845": "pious man could be", "proposed": "pious man could be", "page": 513, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§35 which he had espoused", "ccel": "which he has espoused", "1845": "which he had espoused", "proposed": "which he had espoused", "page": 514, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "§36 μυστήριον: π for ρ, accent lost", "ccel": "μυστηπιον", "1845": "μυστήριον", "proposed": "μυστήριον", "page": 515, "kind": "e", "confidence": "verified"}
{"file": "book-4-chapter-19.typ", "anchor": "note on the Supper's antiquity (French): temps", "ccel": "du ternps", "1845": "du temps", "proposed": "du temps", "page": 488, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "note on the keys (French): avons", "ccel": "avoos", "1845": "avons", "proposed": "avons", "page": 497, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-19.typ", "anchor": "note on the orders: Mark 7:33 (1845 misprints the same, Matth. vii. 33: Matthew 7 has 29 verses; the exorcist's office, Christ's fingers in the deaf man's ears)", "ccel": "Mt. 7:33", "1845": "Matth. vii. 33", "proposed": "Mark 7:33", "page": 503, "kind": "f", "confidence": "medium"}
{"file": "book-4-chapter-19.typ", "anchor": "note on “sacrament” (French): Ils ont ete", "ccel": "Ills ont eto", "1845": "Ils ont ete", "proposed": "Ils ont ete", "page": 515, "kind": "e", "confidence": "verified"}
{"file": "book-4-chapter-19.typ", "anchor": "note on marriage: Decret. 32", "ccel": "in Decret. 33", "1845": "in Decret. 32", "proposed": "in Decret. 32", "page": 515, "kind": "f", "confidence": "verified"}
{"file": "book-4-chapter-20.typ", "anchor": "Sections 12 (no stop after the number, so not set as item 12)", "ccel": "12 Objection, that the lawfulness", "1845": "12. Objection, that the lawfulness", "proposed": "12\\. Objection, that the lawfulness", "page": 519, "kind": "s", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§10 desirous to approve their piety", "ccel": "desirous to improve", "1845": "desirous to approve", "proposed": "desirous to approve", "page": 532, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "note on magistrates' duty (French): tous ses", "ccel": "tou sses", "1845": "tous ses", "proposed": "tous ses", "page": 531, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§10 same note: toutesfois", "ccel": "toutes fois", "1845": "toutesfois", "proposed": "toutesfois", "page": 531, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§10 same note: n’empeche", "ccel": "empeehe", "1845": "empeche", "proposed": "empeche", "page": 531, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§10 same note: laquelle", "ccel": "laquelie", "1845": "laquelle", "proposed": "laquelle", "page": 531, "kind": "e", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "note on Moses: Acts 7:24 (1845 misprints the same, Acts vii. 21; Moses smote the Egyptian, 7:24)", "ccel": "Exod 2:12; Acts 7:21", "1845": "Exod. ii. 12 ; Acts vii. 21", "proposed": "Exod 2:12; Acts 7:24", "page": 532, "kind": "f", "confidence": "medium"}
{"file": "book-4-chapter-20.typ", "anchor": "note on Proverbs: 17:11 (1845 misprints the same, xvii. 14; the quoted verse “An evil man seeketh only rebellion” is 17:11). The next reference, 24:24, is right in CCEL (1845 xxiv. 21)", "ccel": "17:15; 17:14", "1845": "xvii. 15 ; xvii. 14", "proposed": "17:15; 17:11", "page": 532, "kind": "f", "confidence": "medium"}
{"file": "book-4-chapter-20.typ", "anchor": "§10 Prov. 25:5: Take away the wicked from", "ccel": "wicked men from", "1845": "wicked from", "proposed": "wicked from", "page": 533, "kind": "c", "confidence": "verified"}
{"file": "book-4-chapter-20.typ", "anchor": "§10 Prov. 17:15: they both are abomination", "ccel": "both are an abomination", "1845": "both are abomination", "proposed": "both are abomination", "page": 533, "kind": "c", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§11 injuries inflicted", "ccel": "been afflicted", "1845": "been inflicted", "proposed": "been inflicted", "page": 534, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§12 the soldiers asked counsel", "ccel": "soldiers ask counsel", "1845": "soldiers asked counsel", "proposed": "soldiers asked counsel", "page": 534, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§16 Equity cannot but be the same in all (CCEL reverses the sense)", "ccel": "cannot be the same", "1845": "cannot but be the same", "proposed": "cannot but be the same", "page": 538, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§16 in a troubled condition", "ccel": "is in troubled", "1845": "is in a troubled", "proposed": "is in a troubled", "page": 539, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§17 What deference ought", "ccel": "What difference ought", "1845": "What deference ought", "proposed": "What deference ought", "page": 539, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§18 bitterness and hatred", "ccel": "bitterness or hatred", "1845": "bitterness and hatred", "proposed": "bitterness and hatred", "page": 540, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§19 judicial discussion", "ccel": "judicial distinction", "1845": "judicial discussion", "proposed": "judicial discussion", "page": 541, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§19 some bad man", "ccel": "some bad men", "1845": "some bad man", "proposed": "some bad man", "page": 541, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§19 Rom. 13:4", "ccel": "(Rom. 13:8)", "1845": "(Rom. xiii. 4.)", "proposed": "(Rom. 13:4)", "page": 542, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§22 wicked and flagitious", "ccel": "wicked or flagitious", "1845": "wicked and flagitious", "proposed": "wicked and flagitious", "page": 544, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "note on Job 34:30 etc.: semicolon", "ccel": "10:5: Deut", "1845": "x. 5 ; Deut", "proposed": "10:5; Deut", "page": 547, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§26 1 Sam. 8:11-17 (letter l for 1)", "ccel": "8:11-l7", "1845": "viii. 11-17", "proposed": "8:11-17", "page": 548, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§27 with the pestilence (Jer. 27:8)", "ccel": "with pestilence", "1845": "with the pestilence", "proposed": "with the pestilence", "page": 549, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§28 Mine eye spared thee (1 Sam. 24:10)", "ccel": "Mine eyes spare", "1845": "Mine eye spared", "proposed": "Mine eye spared", "page": 550, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§28 1 Sam. 24 (letter l for 1; 1845 has xxvi. 9-11, but the words quoted are 1 Sam. 24:6, 10, so CCEL's chapter is kept)", "ccel": "(l Sam. 24", "1845": "(1 Sam. xxvi. 9-11.)", "proposed": "(1 Sam. 24", "page": 550, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-20.typ", "anchor": "§31 fraudulently", "ccel": "fradulently", "1845": "fraudulently", "proposed": "fraudulently", "page": 553, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-17.typ", "anchor": "§20 will be to begin (digit 1 for l)", "ccel": "course wil1 be", "1845": "course will be", "proposed": "course will be", "page": 409, "kind": "d", "confidence": "high"}
```
