# Calvin, Institutes, vol. 2 (Book II): CCEL vs the 1845 printing

Base: `chapters/typ/vol-2/*.typ` (CCEL machine pass). Witness: Calvin
Translation Society, Edinburgh 1845: Book II, Argument and chapters 1–11 are at
the end of the 1845 vol. 1 (archive.org `instituteschrist01calvuoft`, pp.
280–542); chapters 12–17 open the 1845 vol. 2 (`institutesofreli02calvuoft`,
pp. 1–82; page numbers in the tables for ch. 12–17 are vol. 2's). The OCR was
aligned word by word with the edition (difflib; scripts in
`scratchpad/calvin-v2/`: `align.py`, `diff.py`, raw candidates in
`cand-*.txt`, findings in `findings.jsonl`, `build.py` writes this file).
Doubtful places were read on the page images (crops in
`scratchpad/calvin-pages/`): vol. 1 scan index n = printed page + 121 (holds
for Book II), vol. 2 n = printed page + 9 (files `q*.jpg`). "verified" in the
confidence column = read on the image. Otherwise the OCR reading is an
unambiguous real word in clean OCR.

**Kinds:** **b** = 1845 words missing in CCEL. **c** = CCEL words not in 1845
(stray letters, doubled text). **d** = a different word. **d/comma** = CCEL
turned the comma after a word into a final "s" ("will, and" → "wills and"), as
in vol. 1, CCEL's commonest slip; every case checked against the 1845 comma.
**e** = Greek/Latin. **f** = reference numbers. **n** = notes. **info** = CCEL
departs from 1845 but corrects a misprint there (or both share a misprint);
see "proposed".

**Not listed one by one (CCEL-wide editorial choices, kept by the edition):**
Arabic numerals in references; CCEL's spellings (American or British:
"worshipers", "recognise", "Phil." for "Philip."); CCEL's has/does for 1845's
hath/doth/doeth in Scripture quotations (dozens of places in every chapter);
CCEL's punctuation around references; "a universal" for 1845 "an universal".

**Greek in a private font encoding.** Book II's Greek is not Unicode in CCEL:
it is keyed in the old SGreek/Beta-like ASCII font ("filautiva kai;
filoneikiva" = φιλαυτία καὶ φιλονεικία; `v` = acute, `j`/`J` = breathings,
`”` = final ς, `\\` grave, `[` rough breathing on a vowel). Every such run
in vol. 2 is listed (kind e) with the Unicode Greek read on the 1845 page:
ch. 2 (7 places), ch. 14 (3), ch. 16 (1 run of four words), ch. 17 (1).


## Book II, Argument (p. 280) — `book-2-argument.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| III. What kind of person Christ was | Christ was, and behaved to be | Christ was, and behoved to be | behoved | 280 | d | high |

## Book II, chapter 01 — `book-2-chapter-01.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §5 The orthodox, therefore | The orthodoxy, therefore | The orthodox, therefore | orthodox | 288 | d | high |
| §6 John 3:6 | is born of the flesh is fleshy” | is born of the flesh is flesh,” | flesh | 290 | d | high |
| §10 And let no one here | let no one here glamour that God | let no one here clamour that God | clamour | 295 | d | high |
| §10 was made upright, but by his | but by his oven infatuation | but by his own infatuation | own | 295 | d | high |
| §11 For, on the same | on the same grounds the apostle says | on the same ground, the apostle says | ground, the | 296 | d/comma | high |
| note: The latter clause of this sentence | is ommitted in the French | is omitted in the French | omitted | 287 | n | high |
| note: Les enfans ne descendent point | les serviteurs de Diu ont | les serviteurs de Dieu ont | Dieu | 291 | n | high |
| note: Car en ce qui est dit | Car en ce qui est d’t, que | Car en ce qui est dit, que | dit | 292 | n | high |
| note: Car en ce qui est dit (translation) | by his transgression we are covered with confusion | by his transgression we are all covered with confusion | we are all covered | 292 | n | high |
| note: Nous nions qu’elle soit de nature | qualité survenue ˆ l’homme | qualité survenue à l’homme | à | 296 | n | high |
| note: Nous nions qu’elle soit de nature (translation) | we deny that is is of nature | we deny that it is of nature | it is | 296 | n | high |
| §6 as it is elsewhere said, “The Spirit is life | because of righteousness,” (1 Cor. 15:22) | because of righteousness,” (1 Cor. xv. 22.) | Rom. 8:10 (1845 has the same misprint, repeating the reference before) | 290 | f | high |

## Book II, chapter 02 — `book-2-chapter-02.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary: II. The opinions of others | the subject of human freedom, see. 2–9. | the subject of human freedom, sec. 2–9. | sec. 2–9 | 297 | d | high |
| summary: III. The true doctrine | doctrine on the subject, see. 10–27. | doctrine on the subject, sec. 10–27. | sec. 10–27 | 297 | d | high |
| Sections 15 | The rise of this knowledge of things terrestrial | The use of this knowledge of things terrestrial | use | 298 | d | high (verified) |
| Sections 18 | proved and thus tested by a simile | proved and illustrated by a simile | illustrated | 298 | d | high |
| §4 the Greeks were not ashamed to use | viz. aujtexouvsion, as if | viz., αὐτεξούσιον, as if | αὐτεξούσιον | 305 | e | high (verified) |
| §4 writers appear to me to have exalted | exalted human strengths from a fear | exalted human strength, from a fear | strength, from | 303 | d/comma | high |
| §4 Chrysostom, If any one is lying | (Homily. 18, in Genesis) | (Homil. 18, in Genesim.) | (Homil. 18, in Genesim) | 303 | e | medium |
| §4 we cannot obtain favour from above | (Homily. 52) | (Homil. 52.) | (Homil. 52) | 303 | d | medium |
| §4 the indestructible liberty of the | liberty of the wills and the inalienable | liberty of the will, and the inalienable | will, and | 305 | d/comma | high |
| §4 Thomas Aquinas says | (Part 1 Quast. 83, Art. 3) | (Part I. Quæst. 83, Art. 3,) | (Part 1, Quæst. 83, Art. 3) | 305 | e | high |
| §6 either to nullify the first grace | by rejecting its or to confirm it | by rejecting it, or to confirm it | it, or | 307 | d/comma | high |
| §7 while he is, however, | ejthelodou’lo” (a voluntary slave) | ἐθελόδουλος, (a voluntary slave;) | ἐθελόδουλος | 308 | e | high (verified) |
| §8 In another passage he is offended | In another passages he is offended | In another passage, he is offended | passage, he | 308 | d/comma | high |
| §11 seeing that in ourselves | in ourselves eve are altogether wicked | in ourselves we are altogether wicked | we | 313 | d | high |
| §11 getting quit of the disease of self-love | filautiva kai; filoneikiva, under the blinding of which | φιλαυτία καὶ φιλονεικία, under the blinding influences of which | φιλαυτία καὶ φιλονεικία, under the blinding influences of which | 313 | e | high (verified) |
| §13 how human societies must | human societies must he regulated by laws | human societies must be regulated by laws | be | 316 | d | high |
| §15 not to reject or | not to reject or condemn truth wherever it appears | not to reject or contemn truth wherever it appears | contemn | 318 | d | high |
| §16 construction of the Tabernacle | Tabernacle behaved to be imparted | Tabernacle behoved to be imparted | behoved | 318 | d | high |
| §17 Nay, even in Homer | oJion ejp e\\ma” a\[geisi. | οἷον ἐπ’ ἦμαρ ἄγῃσι. | οἷον ἐπ’ ἦμαρ ἄγῃσι (Od. 18.137) | 320 | e | high (verified) |
| §18 in regard to the kingdom of God, and spiritual | spiritual discernments which consists | spiritual discernment, which consists | discernment, which | 320 | d/comma | high |
| §22 So indulgent is man | So indulgent is man towards himself | So indulgent is man toward himself | toward | 326 | d | low |
| §23 Where incontinence | (ajkrasiva) | (ἀκρασία) | (ἀκρασία) | 326 | e | high (verified) |
| §23 through the passion | (pavtho”) | (πάθος) | (πάθος) | 327 | e | high (verified) |
| §23 Intemperance | (ajkolasiva) | (ἀκολασία,) | (ἀκολασία) | 327 | e | high (verified) |
| §27 to the primary grace of | to the primary grace of Gods (#emph[supra] | to the primary grace of God, (supra | God (#emph[supra] | 331 | d/comma | high |
| §27 adopted from | adopted from Origin and certain | adopted from Origen and certain | Origen | 331 | d | high |
| §27 what answer shall we give to the | give to the apostles who declares | give to the apostle, who declares | apostle, who | 332 | d/comma | high |
| §27 incapable of thinking a good thought | a good thought?” (2 Cor. 3:6) | a good thought?” (2 Cor. iii. 5.) | 2 Cor. 3:5 | 332 | f | high |
| note: et qui plus est | et qui plue est | et qui plus est | plus | 301 | n | high |
| note: Pour en dire franchement | ce qu en est | ce qui en est | qui | 304 | n | high |
| note: qu’en attribue à St Ambroise | qu’en attribue ˆ St Ambroise | qu’en attribue a St Ambroise | à | 306 | n | high |
| note: qu’en attribue à St Ambroise (translation) | which is attributed St. Ambrose. | which is attributed to St Ambrose. | attributed to St. Ambrose | 306 | n | high |
| note: Au commencement de ce traité | at the commencment of this treatise | at the commencement of this treatise | commencement | 311 | n | high |
| note: August. Homil. in Joann. 49 | and in Psalms 45. set 70 | and in Psalms xlv. et lxx. | and in Psalms 45 et 70 | 313 | n | high |
| note: de ce que l’ame savoit | mis dedlans le corps | mis dedans le corps | dedans | 317 | n | high |
| note: Or l’entendement humain | l’entendement humaiu a eté | l’entendement humain a eté | humain | 327 | n | high |

## Book II, chapter 03 — `book-2-chapter-03.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary: proving, from passages of | from passages of Scriptures that the intellect | from passages of Scripture, that the intellect | Scripture, that | 334 | d/comma | high |
| §1 his glory should be seen upon it | (Isaiah 40:2) | (Isaiah lx. 2.) | Isaiah 60:2 | 337 | f | high |
| §4 impelled by the greatest | by the greatest ambitions (a stain | by the greatest ambition, (a stain | ambition (a stain | 341 | d/comma | high |
| §5 the necessary bondage of sin | (August. de Nature et Gratia, et alibi) | (August. de Natura et Gratia, et alibi.) | de Natura et Gratia | 342 | e | high |
| §6 is turned from evil to good. This, | This, I maintains is wholly | This, I maintain, is wholly | maintain, is | 345 | d/comma | high |
| §9 I will walk in thy truth | I will walk in thy truths” adds | I will walk in thy truth,” adds | truth,” adds | 350 | d/comma | high |
| §10 those only begin to ask whom | whom heaven by grace inspires | whom heavenly grace inspires | heavenly | 351 | d | high |
| §10 Hear Christ exclaiming | ‘No man comets unto me | ‘No man cometh unto me | cometh | 352 | d | high |
| §13 second chapter of his Treatise | De Correptione et Gratis, | De Correptione et Gratia, | Gratia | 355 | e | high |
| note: Nous voyons que ce mouvement | ce qu’ils disent, qu Dieu offre | ce qu’ils disent, que Dieu offre | que | 352 | n | high |
| note: French, Comme une pierre | “Come une pierre;” | “Comme une pierre;” | Comme | 356 | n | high |
| note: Qui a esté une peste mortelle | une peste mortelle ˆ l’Eglise | une peste mortelle a l’Eglise | à | 343 | n | high |

## Book II, chapter 04 — `book-2-chapter-04.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 When God is said to have | not that the wills while reluctant | not that the will, while reluctant | will, while | 359 | d/comma | high |
| §3 simply holding what Scripture delivers | delivers. when Augustine was not always | delivers. Even Augustine was not always | Even | 361 | d | high |
| §3 this subtilty is repudiated | passages of Scriptures which clearly show | passages of Scripture, which clearly show | Scripture, which | 361 | d/comma | high |
| §4 In accordance with the former | the former methods it seems | the former method, it seems | method, it | 362 | d/comma | high |
| §4 The law shall perish | from the priests and counsel | from the priest, and counsel | priest, and | 362 | d/comma | high |
| §4 relating the same history | The Psalmists relating the same history | The Psalmist, relating the same history | Psalmist, relating | 362 | d/comma | high |
| §4 he was not inactive among | among theme when he called | among them, when he called | them, when | 363 | d/comma | high |
| §6 promised in the Law that he would give them | give them a nn “trembling heart”? | give them a “trembling heart?” | drop stray “nn” | 365 | c | high |
| note: Ezek. 7:26; Psalm 107:40 | Isiah 63:17 | Isaiah lxiii. 17 | Isaiah 63:17 | 362 | n | high |
| note: Isa. 5:26; 7:18 | Jer. 2:.23 | Jer. l. 23 | Jer. 50:23 | 363 | n | high |

## Book II, chapter 05 — `book-2-chapter-05.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary: class of arguments in defence of free will | God and bad works described as our own | Good and bad works described as our own | Good | 368 | d | high |
| §4 without me ye can do nothing | (John i5:5) | (John xv. 5.) | John 15:5 | 372 | f | high |
| §7 We should rather gather from the promises | the promises hove ill provided | the promises how ill provided | how | 376 | d | high |
| §8 between the commands and grace | (Augustin. de Doctrine Christiana, lib. 3) | (Augustin. de Doctrina Christiana, Lib. iii.) | de Doctrina Christiana | 377 | e | high |
| §8 every degree of purity, piety, holiness | holiness, and justices which we possess | holiness, and justice, which we possess | justice, which | 378 | d/comma | high |
| §10 which I command thee this | thee this days that the Lord | thee this day, that the Lord | day, that | 379 | d/comma | high |
| §10 his kindness depends on our | depends on our wills if we are not | depends on our will, if we are not | will, if | 380 | d/comma | high |
| §10 if we are not masters of our | masters of our wills—that it would | masters of our will, that it would | will—that | 380 | d/comma | high |
| §10 thus it is, that in the protestations | #emph[if we be willing] | if ye be willing | #emph[if ye be willing] | 381 | d | high |
| §11 He elsewhere gives the | gives the reasons “This is the victory | gives the reason, “This is the victory | reason, “This | 384 | d/comma | high |
| §14 observed both in Scripture and in common discourse | God works are said to be ours | Good works are said to be ours | Good | 387 | d | high |
| §14 by the kindness and free gift of | free gift of Gods that becomes ours | free gift of God, that becomes ours | God, that | 387 | d/comma | high |
| §17 I am aware they can quote | can quote Origin and Jerome | can quote Origen and Jerome | Origen | 391 | d | high |
| §18 to curb the malignity of the | malignity of the fleshy which | malignity of the flesh, which | flesh, which | 392 | d/comma | high |
| §19 Paul, when he speaks of our redemption | (Eph. 2:5, 6; 5:14) | (Eph. ii. 5, 30; v. 14,) | keep CCEL's correction | 393 | info | - |
| note: Mais c’est comme si un capitaine | nullement duits ˆ la guerre | nullement duits a la guerre | à | 375 | n | high |
| note: Mais c’est comme si un capitaine (2) | joindre eontre son ennemi | joindre contre son ennemi | contre | 375 | n | high |
| note: Et de fait cette raison | on peut deduire gue ce seroit | on peut deduire que ce seroit | que | 380 | n | high |
| note: Où est-ce que sera cette facilité | veu que notre natute succombe | veu que notre nature succombe | nature | 385 | n | high |
| note: Orig. Lib. 7 in Epist. ad Rom. | Orig. Lig. 7 in Epist. | Orig. Lib. vii. in Epist. | Orig. Lib. 7 | 391 | n | high |

## Book II, chapter 06 — `book-2-chapter-06.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 the covenant which God had made in David | his successors behaved to stand | his successors behoved to stand | behoved | 398 | d | high |
| §2 whom thou madest strong | (or best fitted) | (or hast fitted) | hast | 400 | d | high |
| §2 the psalm laments the dispersion | of the whole nations he prays | of the whole nation, he prays | nation, he | 400 | d/comma | high |
| §3 After seeing that the unbelieving king | the unbelieving king Ahab repudiated | the unbelieving king Ahaz repudiated | Ahaz | 400 | d | high |
| §4 as we lately observed, there is no | there is no having knowledge of God | there is no saving knowledge of God | saving | 403 | d | high |

## Book II, chapter 07 — `book-2-chapter-07.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 17 | attest our guilt and impunity. | attest our guilt and impurity. | impurity | 405 | d | high (verified) |
| §1 accordance with reason, than that the sons of | the sons of Adams who, from hereditary | the sons of Adam, who, from hereditary | Adam, who | 407 | d/comma | high |
| §2 2 Cor. 3:6 | but the split giveth life | but the spirit giveth life | spirit | 408 | d | high |
| §3 at every individual without | without exceptions rise up | without exception, rise up | exception, rise | 409 | d/comma | high |
| §6 if it be not brought forth from its | from its lurkingplaces, it | from its lurking-places, it | lurking-places | 412 | d | low |
| §12 by its demands and | by its demands and threatening, it overawes | by its demands and threatenings, it overawes | threatenings | 419 | d | high |
| §16 Why it behoved the Church | Why it behaved the Church | Why it behoved the Church | behoved | 422 | d | high |
| note: August. Ep. 89, Quæst. 2 | in Ps. 70 et 117; | In Ps. lxx. et cxviii.; | in Ps. 70 et 118; | 415 | n | high (verified) |

## Book II, chapter 08 — `book-2-chapter-08.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 4 Hence, God has annexed | annexed promises and threatening to his promises | annexed promises and threatenings to his promises | threatenings | 425 | d | high |
| Sections 59 (a second copy of the end of 58) | #block(inset: (x: 1em))[59\. Refutation drawn, 1. From a consideration of the whole Decalogue. 2. The testimony of an Apostle. 3. The authority of Christ. 4. The nature and majesty of God. 5. The sentence pronounced against sin. Conclusion.] | (no item 59; the words close item 58) | drop the doubled item 59 | 429 | c | high |
| §1 were overawed by the fear of | fear of judgments and so drawn | fear of judgment, and so drawn | judgment, and | 429 | d/comma | high |
| §4 he has added promises and | he has added promises and threatening. The eye | he has added promises and threatenings. The eye | threatenings | 432 | d | high |
| §4 Ezek. 18:4 | “The souls that sinneth | “The soul that sinneth | soul | 432 | d | high |
| §4 attest the spotless purity of God | The threatening attest the spotless | The threatenings attest the spotless | threatenings | 432 | d | high |
| §4 while the threatenings denounced | while the threatening denounced are intended | while the threatenings denounced are intended | threatenings | 433 | d | high |
| §6 under the prohibition of murder | adultery, and thefts includes | adultery, and theft, includes | theft, includes | 435 | d/comma | high |
| §8 still making it apparent | that no appending of human glosses | that no appendix of human glosses | appendix | 437 | d | high |
| §9 might otherwise not be understood | though understood mighty perhaps | though understood, might, perhaps | understood, might, perhaps | 438 | d/comma | high |
| §9 And not to assert without giving | giving my reasons I prove it | giving my reason, I prove it | reason, I | 438 | d/comma | high |
| §12 This division | This division Origin adopts | This division Origen adopts | Origen | 441 | d | high |
| §15 In like manner, to keep us | In like manners to keep us | In like manner, to keep us | manner, to | 444 | d/comma | high |
| §18 a word meaning strength | I have had no hesitations in order | I have had no hesitation, in order | hesitation, in | 448 | d/comma | high |
| §28 First, under the rest of the seventh | the seventh days the divine Lawgiver | the seventh day, the divine Lawgiver | day, the | 460 | d/comma | high |
| §32 do all things decently and | decently and in orders (1 Cor. 14:40) | decently and in order, (1 Cor. xiv. 40.) | order (1 Cor. 14:40) | 464 | d/comma | high |
| §32 without this politic | this politic arrangements that the dissolution | this politic arrangement, that the dissolution | arrangement, that | 464 | d/comma | high |
| §33 necessary to retain decency | decency, orders and peace | decency, order, and peace | order, and | 465 | d/comma | high |
| §35 For to those whom he raises to | raises to eminences he communicates | raises to eminence, he communicates | eminence, he | 467 | d/comma | high |
| §36 be put to death, they being | as it where, unworthy | as it were, unworthy | were | 468 | d | high |
| §36 when he commands that | that whose curseth his father | that whoso curseth his father | whoso | 468 | d | high |
| §38 pronounces sentence of death | upon theme and orders it | upon them, and orders it | them, and | 469 | d/comma | high |
| §42 since natural feeling and the passions | the passions unnamed by the fall | the passions inflamed by the fall | inflamed | 472 | d | high |
| §42 unable successfully to war against it | should retake themselves | should betake themselves | betake | 472 | d | high |
| §42 that is, in his | in his callings from which | in his calling, from which | calling, from | 472 | d/comma | high |
| §42 have made themselves eunuchs | for the kingdom of heavenly sake | for the kingdom of heaven’s sake | heaven’s | 473 | d | high |
| §43 The incontinent, therefore | The incontinent, therefore, neglecting | The incontinent, therefore, in neglecting | therefore, in neglecting | 474 | b | high |
| §44 who abhors all | abhors all contaminations whatever | abhors all contamination, whatever | contamination, whatever | 475 | d/comma | high |
| §48 an unbecoming proneness to | censorious judgments are here forbidden | censorious judgment, are here forbidden | judgment, are | 480 | d/comma | high |
| §49 permitted to insinuate itself | and inhale them with a noxious | and inflame them with a noxious | inflame | 481 | d | high |
| §57 were too difficult for Christians to | for Christians to hear! | for Christians to bear! | bear | 489 | d | high |
| note: See Augustin. De Civitate Dei | and Lib. 12 c. 20, | and Lib. xiii. c. 20, | Lib. 13 c. 20 | 434 | n | high |
| note: Nous avons aussi un autre ancien Pere | celui que a ecrit | celui qui a ecrit | qui | 442 | n | high |
| note: Nous avons aussi un autre ancien Pere (2) | sur Sainct Matthiue.” | sur Sainct Matthieu.” | Matthieu | 442 | n | high |
| note: Calvin. in Catechismo | De Necessitate Reformandæ Ecclesiæ Ratio. | De Necessitate Reformandæ Ecclesiæ; Vera Reformandæ Ecclesiæ Ratio. | De Necessitate Reformandæ Ecclesiæ; Vera Reformandæ Ecclesiæ Ratio. | 445 | n | high |
| note: 2 Cor. 11:2; Eph. 5:30 | Jer. 62:5 | Jer. lxii. 5 | Isa. 62:5 (1845 has the same misprint; Jeremiah has 52 chapters) | 449 | f | medium |
| note: 1 Sam. 14:44 | 2 Kings 5:31 | 2 Kings vi. 31 | 2 Kings 6:31 | 455 | n | high |
| note: Num. 13:22; Ezek. 20:12 | Jer. 27:21, 22, 27 | Jer. xvii. 21, 22, 27 | Jer. 17:21, 22, 27 | 460 | n | high |
| note: Num. 13:22; Ezek. 20:12 (2) | Isiah 55:2 | Isaiah lvi. 2 | Isaiah 56:2 | 460 | n | high |
| note: Finem istum politicum | N“Finem istum politicum et ecclesiasticum ordinem.”P—French | “Finem istum politicum et ecclesiasticum ordinem.” French | “Finem istum politicum et ecclesiasticum ordinem.”—French (drop stray N and P) | 464 | n | high |
| note: ne discernans entre le Dimanche | mais qu’il on faloit | mais qu’il en faloit | en | 466 | n | high |
| note: leur conviendroyent mieux | whould be more applicable | would be more applicable | would | 466 | n | high |
| note: Exod. 21:17; Lev. 20:9 | Mt. 25:4 | Matth. xv. 4 | Mt. 15:4 | 468 | n | high |
| note: Book 3, Chap. 7 sec 4—7 | Chap. 17 sec. 38, 40. | Chap. xviii. sec. 38, 40. | Chap. 18 sec. 38, 40 (as 1845; neither checked against Book IV) | 471 | n | medium |
| note: D’avantage ce precepte | s’estend jusques lˆ, | s’estend jusques la, | là | 480 | n | high |
| note: D’avantage ce precepte (2) | faire vergogne ˆ quelqu’un | faire vergogne à quelqu’un | à | 480 | n | high |
| note: See August. Ep. 200, ad Asellicum | et Quæstio, Lib. 88, sub fin. | et Quæstio, Lib. lxxxiii., sub fin. | Lib. 83 (De diversis quaestionibus LXXXIII) | 482 | n | high |
| note: See August. Ep. 200, ad Asellicum (2) | touched on in Ps. 142 and | touched on in Ps. cxliii. and | Ps. 143 | 482 | n | high |
| note: Is. 1:17 | Is. 1:17; 57:6; | Is. i. 17; lviii. 6; | Is. 1:17; 58:6; | 485 | n | high |

## Book II, chapter 09 — `book-2-chapter-09.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §5 he that is least in the kingdom of heaven | is greater than he,” (Mt. 11:28) | is greater than he,” (Matth. xi. 11.) | Mt. 11:11 | 497 | f | high |
| §5 Behold, I will send you Elijah | Elijah the prophets before the coming | Elijah the prophet, before the coming | prophet, before | 498 | d/comma | high |

## Book II, chapter 10 — `book-2-chapter-10.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary: III. The Old Testament | and examples, see. 5–23. | and examples, sec. 5–23. | sec. 5–23 | 499 | d | high |
| §3 where any of the others requires | requires explanations to supply it | requires explanation, to supply it | explanation, to | 503 | d/comma | high |
| §6 Paul, again, knowing that the | knowing that the Lords when he rained | knowing that the Lord, when he rained | Lord, when | 506 | d/comma | high |
| §15 For, in another passage | in another passages after speaking | in another passage, after speaking | passage, after | 516 | d/comma | high |
| §19 the mysteries of God, which all in common | all in common behaved to learn | all in common behoved to learn | behoved | 520 | d | high |
| §23 spiritual and eternal life, the expectation | the expectation of which behaved to be | the expectation of which behoved to be | behoved | 523 | d | high |
| §23 the substantive existence of spirits | both of which where attested | both of which were attested | were | 523 | d | high |
| note: Veu qu’ils pensent | pensent qu notre Seigneur | pensent que notre Seigneur | que | 501 | n | high |
| note: Veu qu’ils pensent (2) | sans seperance aucune | sans esperance aucune | esperance | 501 | n | high |
| note: Et encore ne peut il pas | par eclui du quel | par celui du quel | celui | 512 | n | high |

## Book II, chapter 11 — `book-2-chapter-11.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 12 Why the calling of the Gentiles | the Gentiles scented to the Apostles | the Gentiles seemed to the Apostles | seemed | 526 | d | high |
| §2 Sion overflow with every species | every species at abundance | every species of abundance | of | 528 | d | high |
| §4 had foretold concerning the priesthood of Christ | (Ps. 110:4). seeing that an eternal | (Ps. cx. 4.) Seeing that an eternal | Seeing | 530 | d | medium |
| §4 whether or not the ceremonies ordained in the Law | the Law behaved to give way | the Law behoved to give way | behoved | 530 | d | high |
| §4 the Apostle contends that it | it behaved to be annulled | it behoved to be annulled | behoved | 531 | d | high |
| §7 to explain the meaning of the Prophet | the worlds of the one furnish us | the words of the one furnish us | words | 533 | d | high |
| §8 Being a shadow of things to come | it behaved in time to perish | it behoved in time to perish | behoved | 534 | d | high |
| §8 riches of the grace with which the same | the same Lawgivers assuming, as it were a new characters honoured | the same Lawgiver, assuming, as it were, a new character, honoured | the same Lawgiver, assuming, as it were, a new character, honoured | 535 | d/comma | high |
| §8 of ancient Israel who, with sincere and heartfelt | heartfelt affections embraced the covenant | heartfelt affection, embraced the covenant | affection, embraced | 535 | d/comma | high |
| §9 the term bondage is applied to the Old | the Old Testaments because it begets fear | the Old Testament, because it begets fear | Testament, because | 535 | d/comma | high |
| §9 he explains more fully in the | in the Epistles to the Galatians | in the Epistle to the Galatians | Epistle | 535 | d | high |
| §9 could never attain to the | attain to the inheritances while | attain to the inheritance, while | inheritance, while | 535 | d/comma | high |
| §11 the only means of preventing their | preventing their destructions—viz. | preventing their destruction, viz., | destruction—viz. | 538 | d/comma | high |
| §14 the alternate changes of summer and winter | of clay and night | of day and night | day | 541 | d | high |
| note: et à icelle se doivent reduire | “et ˆ icelle se doivent | “et à icelle se doivent | à | 530 | n | high |
| note: et à icelle (translation) | by way of camparison, opposed | by way of comparison, opposed | comparison | 530 | n | high |
| note: Passim | “cá et lá;” | “çà et là;” | çà et là | 534 | n | medium |

## Book II, chapter 12 — `book-2-chapter-12.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 4 objection against the orthodox doctrine | Answer to it. Conformation from the sacrifices | Answer to it. Confirmation from the sacrifices | Confirmation | 2 | d | high |
| §1 sons of Adam? All of them | with their parents, shuddered | with their parent, shuddered | parent | 2 | d | high |
| §1 Son of God behoved to become our Emmanuel | our Emmanuel, the God with us; | our Emmanuel, i.e. God with us; | our Emmanuel, i.e. God with us | 2 | d | high |
| §4 to bring relief to miserable sinners | sinners, whose overleaps these limits | sinners, whoso overleaps these limits | whoso | 5 | d | high |
| §6 God has distinguished Adam above the other animals | And likewise, with one consent | All, likewise, with one consent | All, likewise, | 9 | d | high |
| note: John 3:16; 5:25 | John 3:16; 5:25; Mt. 18:11 | John iii. 16; v. 25; xi. 25; Matth. xviii. 11 | John 3:16; 5:25; 11:25; Mt. 18:11 | 6 | n | high |

## Book II, chapter 13 — `book-2-chapter-13.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary: I. The orthodox doctrine | I. The orthodoxy doctrine | I. The orthodox doctrine | orthodox | 13 | d | high |
| Sections 4 | #block(inset: (x: 1em))[4\. Other three objections answered.] | (no item 4 in 1845's list of sections) | keep CCEL (it matches the chapter's four sections) | 13 | info | - |
| §2 1 Pet. 3:18 | quickened by the Spirits” (1 Pet. 3:18) | quickened by the Spirit,” (1 Pet. iii. 18,) | Spirit” (1 Pet. 3:18) | 15 | d/comma | high |
| §3 that they are classified with men. For this | For this reasons wives | For this reason, wives | reason, wives | 18 | d/comma | high |
| §3 I, in my turn | I, in my turn, asks whether | I, in my turn, ask, whether | ask, whether | 19 | d/comma | high |
| note: The last clause of this sentence | The last clause of the sentence is omited in the French. | The last clause of this sentence is omitted in the French. | this sentence is omitted | 16 | n | high |

## Book II, chapter 14 — `book-2-chapter-14.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 a figure of speech which the ancients termed | ijdiwmavtwn koinoniva | ἰδιωμάτων κοινωνία | ἰδιωμάτων κοινωνία | 23 | e | high (verified) |
| §2 There is a communication of | communication of ijdiwvmata, or properties | communication of ἰδιωμάτα, or properties | ἰδιώματα | 24 | e | high (verified; 1845's accent is misplaced) |
| §2 transferred improperly, but not | but not ceaselessly, to his divinity | but not causelessly, to his divinity | causelessly | 24 | d | high |
| §4 in those of Constantinople and | Constantinople and Chalcedony, it being | Constantinople and Chalcedon, it being | Chalcedon | 27 | d | high |
| §5 This is intimated by the angel’s | the angel’s word to Mary | the angel’s words to Mary | words | 28 | d | high |
| §8 he admits that his flesh is | is oJmoouvsion, of the same | is ὁμοούσιον, of the same | ὁμοούσιον | 33 | e | high (verified) |
| note: Augustine employs the same similitude | the same similitude, Epist. 52.] | the same similitude, Epist. cii. | Epist. 102 | 23 | n | high |
| note: Isaiah 41:1, &c.; John 5:17 | Isiah 41:1, &c. | Isaiah xli. 1, &c. | Isaiah 41:1 | 24 | n | high |
| note: Vide Calv. Epist. ad Polonos | VideCalv. Epist. ad Polonos | Vide Calv. Epist. ad Polonos | Vide Calv. | 26 | n | high |
| note: See Irenæus, lib. 4 | The above passages from The Proverbs is quoted | The above passage from The Proverbs is quoted | passage | 32 | n | high |

## Book II, chapter 15 — `book-2-chapter-15.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| heading | THREE THINGS BRIEFLY TO BE REGARDED IN | THREE THINGS CHIEFLY TO BE REGARDED IN | CHIEFLY | 35 | d | high |
| §2 Is. 61:1, 2 | the acceptable year of the Lord,” (Is. 60:1, 2) | the acceptable year of the Lord,” (Is. lx. 1, 2.) | Is. 61:1, 2 (1845 has the same misprint) | 37 | f | high (verified) |
| §3 immediately after Solomon’s death the kingdom | the kingdom in n great measure | the kingdom in a great measure | a | 39 | d | high |
| §5 that God may be all in all | that God may be all in and” | that God may be all in all,” | all in all” | 42 | d | high |

## Book II, chapter 16 — `book-2-chapter-16.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §5 by the whole course of his obedience | This id proved by the | This is proved by the | is | 51 | d | high |
| §5 might provide for us. We must bear in | We must bear in minds that Christ | We must bear in mind, that Christ | mind, that | 53 | d/comma | high |
| §5 both by giving himself up to | himself up to condemnations and undertaking | himself up to condemnation, and undertaking | condemnation, and | 53 | d/comma | high |
| §6 This was also shadowed in the Law, since | since twm\`a ¶ , the word | since אשמות, the word | since אשמות, the word (Hebrew in a font encoding, with a false paragraph break) | 54 | e | high (verified) |
| §6 that they were a kind of | kind of kaqarmavton (purifications) | kind of καθαρμάτων, (purifications,) | καθαρμάτων | 54 | e | high (verified) |
| §6 (purifications), bearing, by | bearing, by substitutions the curse | bearing, by substitution, the curse | substitution, the | 54 | d/comma | high |
| §6 in order to accomplish a full expiation, he made his soul | made his soul to !\`a ¶ , #emph[i.e.], a propitiatory | made his soul אשם, i. e., a propitiatory | made his soul אשם, #emph[i.e.], a propitiatory (Hebrew in a font encoding, with a stray “to” and a false paragraph break) | 55 | e | high (verified) |
| §6 we could have no sure conviction of his being | ajpoluvtrwsi”, ajntivlutron, kai; iJlasthvrion, | ἀπολύτρωσις, ἀντίλυτρον, καὶ ἱλαστήριον, | ἀπολύτρωσις, ἀντίλυτρον, καὶ ἱλαστήριον, | 56 | e | high (verified; 1845 prints the accents loosely) |
| §7 An effect of his burial, moreover | An effect of his burials moreover is | An effect of his burial, moreover, is | burial, moreover | 57 | d/comma | high |
| §7 ingrafted into the likeness of | the likeness of Christ’s deaths and that | the likeness of Christ’s death, and that | death, and | 57 | d/comma | high |
| §15 All that the Apostles | All that the Apostles intends when | All that the Apostles intend, when | intend, when | 69 | d/comma | high |
| §19 we must beware of deriving even the | even the minutes portion of it | even the minutest portion of it | minutest | 72 | d | high |
| note: Jusques ici j’ay suivi (translation) | understand on that things we ought | understand on what things we ought | what | 72 | n | high |
| note: Acts 4:12; 1 Cor. 1:30 | Heb. 2:17; Gal. 3:3.] | Heb. ii. 17; Gal. iii. 13. | Gal. 3:13 | 72 | n | high |
| note: Les autres translatent Reverence | c’est mal ˆ propos. | c’est mal a propos. | à | 61 | n | high |

## Book II, chapter 17 — `book-2-chapter-17.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 as the only begotten Son | the only begotten Son at God, could merit | the only begotten Son of God, could merit | of | 75 | d | high |
| §5 designates him by the pronoun | (aujtov”) | (αὐτός.) | (αὐτός) | 81 | e | high (verified) |
| §5 Isaiah 37:35 | for mine own sakes and for my servant | for mine own sake, and for my servant | sake, and | 80 | d/comma | high |

### Structural

- Section numbers agree with 1845 in every chapter. No section is missing,
  doubled or renumbered. Two "Sections." lists differ: in ch. 8, CCEL adds an
  item 59 that copies the second half of item 58 (1845 has no 59; listed, kind
  c). In ch. 13, CCEL has an item 4 ("Other three objections answered") that
  1845's list lacks, though the chapter has four sections (info: keep it).
- Footnotes are present and in place throughout. No note is merged or missing.
  One note has stray letters ("N“Finem … ordinem.”P", ch. 8). French quotations
  in the notes have CCEL's "ˆ" for "à" in 9 places, all listed.
- **Hebrew:** 1845 prints Hebrew twice in Book II, both in ch. 16 §6: אשמות
  (p. 54) and אשם (p. 55). CCEL has them in a Hebrew font's ASCII encoding
  ("twm\`a", "!\`a"), each followed by a false paragraph break (shown as ¶ in the tables; the JSON keeps the exact `\n\n`), so the edition
  now prints garbage and splits the sentence into two paragraphs. (`SOURCES.md`
  says CCEL has no Hebrew; these two are the exception.)
- 1845's own misprints that CCEL silently corrects are not listed, apart from
  two kept as info. Where 1845 and CCEL share a wrong reference (ch. 1 "1 Cor.
  15:22" for Rom. 8:10; ch. 8 "Jer. 62:5" for Isa. 62:5; ch. 15 "Is. 60:1, 2"
  for Isa. 61:1, 2), it is listed as kind f with the right reference.
- CCEL often drops the final "s" of 1845's "threatenings" (ch. 7–8, 5 places).
  These are listed: in each the plural verb or the context shows the 1845
  reading is right.

### Systematic: *hath*/*doth* (not listed one by one)

The alignment found about 80 places in Book II where 1845 prints *hath*,
*doth*, *doeth* or *seeth* in a Scripture quotation and CCEL has *has*, *does*
or *sees*. The most are in ch. 3 (14), ch. 9 (8), ch. 8 and ch. 16 (7 each),
and ch. 17 (6). As in vol. 1, the editor keeps CCEL's forms. Two related
words *are* listed, because they are wrong words rather than modernised ones:
"comets" for "cometh" (ch. 3) and "behaved" for "behoved" (argument; ch. 2,
6, 7, 10, 11: 9 places in all).


## Findings as JSON lines

```json
{"file": "book-2-argument.typ", "anchor": "III. What kind of person Christ was", "ccel": "Christ was, and behaved to be", "1845": "Christ was, and behoved to be", "proposed": "behoved", "page": 280, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "§5 The orthodox, therefore", "ccel": "The orthodoxy, therefore", "1845": "The orthodox, therefore", "proposed": "orthodox", "page": 288, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "§6 John 3:6", "ccel": "is born of the flesh is fleshy”", "1845": "is born of the flesh is flesh,”", "proposed": "flesh", "page": 290, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "§10 And let no one here", "ccel": "let no one here glamour that God", "1845": "let no one here clamour that God", "proposed": "clamour", "page": 295, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "§10 was made upright, but by his", "ccel": "but by his oven infatuation", "1845": "but by his own infatuation", "proposed": "own", "page": 295, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "§11 For, on the same", "ccel": "on the same grounds the apostle says", "1845": "on the same ground, the apostle says", "proposed": "ground, the", "page": 296, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "note: The latter clause of this sentence", "ccel": "is ommitted in the French", "1845": "is omitted in the French", "proposed": "omitted", "page": 287, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "note: Les enfans ne descendent point", "ccel": "les serviteurs de Diu ont", "1845": "les serviteurs de Dieu ont", "proposed": "Dieu", "page": 291, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "note: Car en ce qui est dit", "ccel": "Car en ce qui est d’t, que", "1845": "Car en ce qui est dit, que", "proposed": "dit", "page": 292, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "note: Car en ce qui est dit (translation)", "ccel": "by his transgression we are covered with confusion", "1845": "by his transgression we are all covered with confusion", "proposed": "we are all covered", "page": 292, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "note: Nous nions qu’elle soit de nature", "ccel": "qualité survenue ˆ l’homme", "1845": "qualité survenue à l’homme", "proposed": "à", "page": 296, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "note: Nous nions qu’elle soit de nature (translation)", "ccel": "we deny that is is of nature", "1845": "we deny that it is of nature", "proposed": "it is", "page": 296, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-01.typ", "anchor": "§6 as it is elsewhere said, “The Spirit is life", "ccel": "because of righteousness,” (1 Cor. 15:22)", "1845": "because of righteousness,” (1 Cor. xv. 22.)", "proposed": "Rom. 8:10 (1845 has the same misprint, repeating the reference before)", "page": 290, "kind": "f", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "summary: II. The opinions of others", "ccel": "the subject of human freedom, see. 2–9.", "1845": "the subject of human freedom, sec. 2–9.", "proposed": "sec. 2–9", "page": 297, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "summary: III. The true doctrine", "ccel": "doctrine on the subject, see. 10–27.", "1845": "doctrine on the subject, sec. 10–27.", "proposed": "sec. 10–27", "page": 297, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "Sections 15", "ccel": "The rise of this knowledge of things terrestrial", "1845": "The use of this knowledge of things terrestrial", "proposed": "use", "page": 298, "kind": "d", "confidence": "high (verified)"}
{"file": "book-2-chapter-02.typ", "anchor": "Sections 18", "ccel": "proved and thus tested by a simile", "1845": "proved and illustrated by a simile", "proposed": "illustrated", "page": 298, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§4 the Greeks were not ashamed to use", "ccel": "viz. aujtexouvsion, as if", "1845": "viz., αὐτεξούσιον, as if", "proposed": "αὐτεξούσιον", "page": 305, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-02.typ", "anchor": "§4 writers appear to me to have exalted", "ccel": "exalted human strengths from a fear", "1845": "exalted human strength, from a fear", "proposed": "strength, from", "page": 303, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§4 Chrysostom, If any one is lying", "ccel": "(Homily. 18, in Genesis)", "1845": "(Homil. 18, in Genesim.)", "proposed": "(Homil. 18, in Genesim)", "page": 303, "kind": "e", "confidence": "medium"}
{"file": "book-2-chapter-02.typ", "anchor": "§4 we cannot obtain favour from above", "ccel": "(Homily. 52)", "1845": "(Homil. 52.)", "proposed": "(Homil. 52)", "page": 303, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-02.typ", "anchor": "§4 the indestructible liberty of the", "ccel": "liberty of the wills and the inalienable", "1845": "liberty of the will, and the inalienable", "proposed": "will, and", "page": 305, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§4 Thomas Aquinas says", "ccel": "(Part 1 Quast. 83, Art. 3)", "1845": "(Part I. Quæst. 83, Art. 3,)", "proposed": "(Part 1, Quæst. 83, Art. 3)", "page": 305, "kind": "e", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§6 either to nullify the first grace", "ccel": "by rejecting its or to confirm it", "1845": "by rejecting it, or to confirm it", "proposed": "it, or", "page": 307, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§7 while he is, however,", "ccel": "ejthelodou’lo” (a voluntary slave)", "1845": "ἐθελόδουλος, (a voluntary slave;)", "proposed": "ἐθελόδουλος", "page": 308, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-02.typ", "anchor": "§8 In another passage he is offended", "ccel": "In another passages he is offended", "1845": "In another passage, he is offended", "proposed": "passage, he", "page": 308, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§11 seeing that in ourselves", "ccel": "in ourselves eve are altogether wicked", "1845": "in ourselves we are altogether wicked", "proposed": "we", "page": 313, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§11 getting quit of the disease of self-love", "ccel": "filautiva kai; filoneikiva, under the blinding of which", "1845": "φιλαυτία καὶ φιλονεικία, under the blinding influences of which", "proposed": "φιλαυτία καὶ φιλονεικία, under the blinding influences of which", "page": 313, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-02.typ", "anchor": "§13 how human societies must", "ccel": "human societies must he regulated by laws", "1845": "human societies must be regulated by laws", "proposed": "be", "page": 316, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§15 not to reject or", "ccel": "not to reject or condemn truth wherever it appears", "1845": "not to reject or contemn truth wherever it appears", "proposed": "contemn", "page": 318, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§16 construction of the Tabernacle", "ccel": "Tabernacle behaved to be imparted", "1845": "Tabernacle behoved to be imparted", "proposed": "behoved", "page": 318, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§17 Nay, even in Homer", "ccel": "oJion ejp e\\\\ma” a\\[geisi.", "1845": "οἷον ἐπ’ ἦμαρ ἄγῃσι.", "proposed": "οἷον ἐπ’ ἦμαρ ἄγῃσι (Od. 18.137)", "page": 320, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-02.typ", "anchor": "§18 in regard to the kingdom of God, and spiritual", "ccel": "spiritual discernments which consists", "1845": "spiritual discernment, which consists", "proposed": "discernment, which", "page": 320, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§22 So indulgent is man", "ccel": "So indulgent is man towards himself", "1845": "So indulgent is man toward himself", "proposed": "toward", "page": 326, "kind": "d", "confidence": "low"}
{"file": "book-2-chapter-02.typ", "anchor": "§23 Where incontinence", "ccel": "(ajkrasiva)", "1845": "(ἀκρασία)", "proposed": "(ἀκρασία)", "page": 326, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-02.typ", "anchor": "§23 through the passion", "ccel": "(pavtho”)", "1845": "(πάθος)", "proposed": "(πάθος)", "page": 327, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-02.typ", "anchor": "§23 Intemperance", "ccel": "(ajkolasiva)", "1845": "(ἀκολασία,)", "proposed": "(ἀκολασία)", "page": 327, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-02.typ", "anchor": "§27 to the primary grace of", "ccel": "to the primary grace of Gods (#emph[supra]", "1845": "to the primary grace of God, (supra", "proposed": "God (#emph[supra]", "page": 331, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§27 adopted from", "ccel": "adopted from Origin and certain", "1845": "adopted from Origen and certain", "proposed": "Origen", "page": 331, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§27 what answer shall we give to the", "ccel": "give to the apostles who declares", "1845": "give to the apostle, who declares", "proposed": "apostle, who", "page": 332, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "§27 incapable of thinking a good thought", "ccel": "a good thought?” (2 Cor. 3:6)", "1845": "a good thought?” (2 Cor. iii. 5.)", "proposed": "2 Cor. 3:5", "page": 332, "kind": "f", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "note: et qui plus est", "ccel": "et qui plue est", "1845": "et qui plus est", "proposed": "plus", "page": 301, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "note: Pour en dire franchement", "ccel": "ce qu en est", "1845": "ce qui en est", "proposed": "qui", "page": 304, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "note: qu’en attribue à St Ambroise", "ccel": "qu’en attribue ˆ St Ambroise", "1845": "qu’en attribue a St Ambroise", "proposed": "à", "page": 306, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "note: qu’en attribue à St Ambroise (translation)", "ccel": "which is attributed St. Ambrose.", "1845": "which is attributed to St Ambrose.", "proposed": "attributed to St. Ambrose", "page": 306, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "note: Au commencement de ce traité", "ccel": "at the commencment of this treatise", "1845": "at the commencement of this treatise", "proposed": "commencement", "page": 311, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "note: August. Homil. in Joann. 49", "ccel": "and in Psalms 45. set 70", "1845": "and in Psalms xlv. et lxx.", "proposed": "and in Psalms 45 et 70", "page": 313, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "note: de ce que l’ame savoit", "ccel": "mis dedlans le corps", "1845": "mis dedans le corps", "proposed": "dedans", "page": 317, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-02.typ", "anchor": "note: Or l’entendement humain", "ccel": "l’entendement humaiu a eté", "1845": "l’entendement humain a eté", "proposed": "humain", "page": 327, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "summary: proving, from passages of", "ccel": "from passages of Scriptures that the intellect", "1845": "from passages of Scripture, that the intellect", "proposed": "Scripture, that", "page": 334, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§1 his glory should be seen upon it", "ccel": "(Isaiah 40:2)", "1845": "(Isaiah lx. 2.)", "proposed": "Isaiah 60:2", "page": 337, "kind": "f", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§4 impelled by the greatest", "ccel": "by the greatest ambitions (a stain", "1845": "by the greatest ambition, (a stain", "proposed": "ambition (a stain", "page": 341, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§5 the necessary bondage of sin", "ccel": "(August. de Nature et Gratia, et alibi)", "1845": "(August. de Natura et Gratia, et alibi.)", "proposed": "de Natura et Gratia", "page": 342, "kind": "e", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§6 is turned from evil to good. This,", "ccel": "This, I maintains is wholly", "1845": "This, I maintain, is wholly", "proposed": "maintain, is", "page": 345, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§9 I will walk in thy truth", "ccel": "I will walk in thy truths” adds", "1845": "I will walk in thy truth,” adds", "proposed": "truth,” adds", "page": 350, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§10 those only begin to ask whom", "ccel": "whom heaven by grace inspires", "1845": "whom heavenly grace inspires", "proposed": "heavenly", "page": 351, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§10 Hear Christ exclaiming", "ccel": "‘No man comets unto me", "1845": "‘No man cometh unto me", "proposed": "cometh", "page": 352, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "§13 second chapter of his Treatise", "ccel": "De Correptione et Gratis,", "1845": "De Correptione et Gratia,", "proposed": "Gratia", "page": 355, "kind": "e", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "note: Nous voyons que ce mouvement", "ccel": "ce qu’ils disent, qu Dieu offre", "1845": "ce qu’ils disent, que Dieu offre", "proposed": "que", "page": 352, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "note: French, Comme une pierre", "ccel": "“Come une pierre;”", "1845": "“Comme une pierre;”", "proposed": "Comme", "page": 356, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§1 When God is said to have", "ccel": "not that the wills while reluctant", "1845": "not that the will, while reluctant", "proposed": "will, while", "page": 359, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§3 simply holding what Scripture delivers", "ccel": "delivers. when Augustine was not always", "1845": "delivers. Even Augustine was not always", "proposed": "Even", "page": 361, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§3 this subtilty is repudiated", "ccel": "passages of Scriptures which clearly show", "1845": "passages of Scripture, which clearly show", "proposed": "Scripture, which", "page": 361, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§4 In accordance with the former", "ccel": "the former methods it seems", "1845": "the former method, it seems", "proposed": "method, it", "page": 362, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§4 The law shall perish", "ccel": "from the priests and counsel", "1845": "from the priest, and counsel", "proposed": "priest, and", "page": 362, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§4 relating the same history", "ccel": "The Psalmists relating the same history", "1845": "The Psalmist, relating the same history", "proposed": "Psalmist, relating", "page": 362, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§4 he was not inactive among", "ccel": "among theme when he called", "1845": "among them, when he called", "proposed": "them, when", "page": 363, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "§6 promised in the Law that he would give them", "ccel": "give them a nn “trembling heart”?", "1845": "give them a “trembling heart?”", "proposed": "drop stray “nn”", "page": 365, "kind": "c", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "note: Ezek. 7:26; Psalm 107:40", "ccel": "Isiah 63:17", "1845": "Isaiah lxiii. 17", "proposed": "Isaiah 63:17", "page": 362, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-04.typ", "anchor": "note: Isa. 5:26; 7:18", "ccel": "Jer. 2:.23", "1845": "Jer. l. 23", "proposed": "Jer. 50:23", "page": 363, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "summary: class of arguments in defence of free will", "ccel": "God and bad works described as our own", "1845": "Good and bad works described as our own", "proposed": "Good", "page": 368, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§4 without me ye can do nothing", "ccel": "(John i5:5)", "1845": "(John xv. 5.)", "proposed": "John 15:5", "page": 372, "kind": "f", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§7 We should rather gather from the promises", "ccel": "the promises hove ill provided", "1845": "the promises how ill provided", "proposed": "how", "page": 376, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§8 between the commands and grace", "ccel": "(Augustin. de Doctrine Christiana, lib. 3)", "1845": "(Augustin. de Doctrina Christiana, Lib. iii.)", "proposed": "de Doctrina Christiana", "page": 377, "kind": "e", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§8 every degree of purity, piety, holiness", "ccel": "holiness, and justices which we possess", "1845": "holiness, and justice, which we possess", "proposed": "justice, which", "page": 378, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§10 which I command thee this", "ccel": "thee this days that the Lord", "1845": "thee this day, that the Lord", "proposed": "day, that", "page": 379, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§10 his kindness depends on our", "ccel": "depends on our wills if we are not", "1845": "depends on our will, if we are not", "proposed": "will, if", "page": 380, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§10 if we are not masters of our", "ccel": "masters of our wills—that it would", "1845": "masters of our will, that it would", "proposed": "will—that", "page": 380, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§10 thus it is, that in the protestations", "ccel": "#emph[if we be willing]", "1845": "if ye be willing", "proposed": "#emph[if ye be willing]", "page": 381, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§11 He elsewhere gives the", "ccel": "gives the reasons “This is the victory", "1845": "gives the reason, “This is the victory", "proposed": "reason, “This", "page": 384, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§14 observed both in Scripture and in common discourse", "ccel": "God works are said to be ours", "1845": "Good works are said to be ours", "proposed": "Good", "page": 387, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§14 by the kindness and free gift of", "ccel": "free gift of Gods that becomes ours", "1845": "free gift of God, that becomes ours", "proposed": "God, that", "page": 387, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§17 I am aware they can quote", "ccel": "can quote Origin and Jerome", "1845": "can quote Origen and Jerome", "proposed": "Origen", "page": 391, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§18 to curb the malignity of the", "ccel": "malignity of the fleshy which", "1845": "malignity of the flesh, which", "proposed": "flesh, which", "page": 392, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "§19 Paul, when he speaks of our redemption", "ccel": "(Eph. 2:5, 6; 5:14)", "1845": "(Eph. ii. 5, 30; v. 14,)", "proposed": "keep CCEL's correction", "page": 393, "kind": "info", "confidence": "-"}
{"file": "book-2-chapter-05.typ", "anchor": "note: Mais c’est comme si un capitaine", "ccel": "nullement duits ˆ la guerre", "1845": "nullement duits a la guerre", "proposed": "à", "page": 375, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "note: Mais c’est comme si un capitaine (2)", "ccel": "joindre eontre son ennemi", "1845": "joindre contre son ennemi", "proposed": "contre", "page": 375, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "note: Et de fait cette raison", "ccel": "on peut deduire gue ce seroit", "1845": "on peut deduire que ce seroit", "proposed": "que", "page": 380, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "note: Où est-ce que sera cette facilité", "ccel": "veu que notre natute succombe", "1845": "veu que notre nature succombe", "proposed": "nature", "page": 385, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-05.typ", "anchor": "note: Orig. Lib. 7 in Epist. ad Rom.", "ccel": "Orig. Lig. 7 in Epist.", "1845": "Orig. Lib. vii. in Epist.", "proposed": "Orig. Lib. 7", "page": 391, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-06.typ", "anchor": "§2 the covenant which God had made in David", "ccel": "his successors behaved to stand", "1845": "his successors behoved to stand", "proposed": "behoved", "page": 398, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-06.typ", "anchor": "§2 whom thou madest strong", "ccel": "(or best fitted)", "1845": "(or hast fitted)", "proposed": "hast", "page": 400, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-06.typ", "anchor": "§2 the psalm laments the dispersion", "ccel": "of the whole nations he prays", "1845": "of the whole nation, he prays", "proposed": "nation, he", "page": 400, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-06.typ", "anchor": "§3 After seeing that the unbelieving king", "ccel": "the unbelieving king Ahab repudiated", "1845": "the unbelieving king Ahaz repudiated", "proposed": "Ahaz", "page": 400, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-06.typ", "anchor": "§4 as we lately observed, there is no", "ccel": "there is no having knowledge of God", "1845": "there is no saving knowledge of God", "proposed": "saving", "page": 403, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "Sections 17", "ccel": "attest our guilt and impunity.", "1845": "attest our guilt and impurity.", "proposed": "impurity", "page": 405, "kind": "d", "confidence": "high (verified)"}
{"file": "book-2-chapter-07.typ", "anchor": "§1 accordance with reason, than that the sons of", "ccel": "the sons of Adams who, from hereditary", "1845": "the sons of Adam, who, from hereditary", "proposed": "Adam, who", "page": 407, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§2 2 Cor. 3:6", "ccel": "but the split giveth life", "1845": "but the spirit giveth life", "proposed": "spirit", "page": 408, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§3 at every individual without", "ccel": "without exceptions rise up", "1845": "without exception, rise up", "proposed": "exception, rise", "page": 409, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§6 if it be not brought forth from its", "ccel": "from its lurkingplaces, it", "1845": "from its lurking-places, it", "proposed": "lurking-places", "page": 412, "kind": "d", "confidence": "low"}
{"file": "book-2-chapter-07.typ", "anchor": "§12 by its demands and", "ccel": "by its demands and threatening, it overawes", "1845": "by its demands and threatenings, it overawes", "proposed": "threatenings", "page": 419, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "§16 Why it behoved the Church", "ccel": "Why it behaved the Church", "1845": "Why it behoved the Church", "proposed": "behoved", "page": 422, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-07.typ", "anchor": "note: August. Ep. 89, Quæst. 2", "ccel": "in Ps. 70 et 117;", "1845": "In Ps. lxx. et cxviii.;", "proposed": "in Ps. 70 et 118;", "page": 415, "kind": "n", "confidence": "high (verified)"}
{"file": "book-2-chapter-08.typ", "anchor": "Sections 4 Hence, God has annexed", "ccel": "annexed promises and threatening to his promises", "1845": "annexed promises and threatenings to his promises", "proposed": "threatenings", "page": 425, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "Sections 59 (a second copy of the end of 58)", "ccel": "#block(inset: (x: 1em))[59\\. Refutation drawn, 1. From a consideration of the whole Decalogue. 2. The testimony of an Apostle. 3. The authority of Christ. 4. The nature and majesty of God. 5. The sentence pronounced against sin. Conclusion.]", "1845": "(no item 59; the words close item 58)", "proposed": "drop the doubled item 59", "page": 429, "kind": "c", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§1 were overawed by the fear of", "ccel": "fear of judgments and so drawn", "1845": "fear of judgment, and so drawn", "proposed": "judgment, and", "page": 429, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§4 he has added promises and", "ccel": "he has added promises and threatening. The eye", "1845": "he has added promises and threatenings. The eye", "proposed": "threatenings", "page": 432, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§4 Ezek. 18:4", "ccel": "“The souls that sinneth", "1845": "“The soul that sinneth", "proposed": "soul", "page": 432, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§4 attest the spotless purity of God", "ccel": "The threatening attest the spotless", "1845": "The threatenings attest the spotless", "proposed": "threatenings", "page": 432, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§4 while the threatenings denounced", "ccel": "while the threatening denounced are intended", "1845": "while the threatenings denounced are intended", "proposed": "threatenings", "page": 433, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§6 under the prohibition of murder", "ccel": "adultery, and thefts includes", "1845": "adultery, and theft, includes", "proposed": "theft, includes", "page": 435, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§8 still making it apparent", "ccel": "that no appending of human glosses", "1845": "that no appendix of human glosses", "proposed": "appendix", "page": 437, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§9 might otherwise not be understood", "ccel": "though understood mighty perhaps", "1845": "though understood, might, perhaps", "proposed": "understood, might, perhaps", "page": 438, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§9 And not to assert without giving", "ccel": "giving my reasons I prove it", "1845": "giving my reason, I prove it", "proposed": "reason, I", "page": 438, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§12 This division", "ccel": "This division Origin adopts", "1845": "This division Origen adopts", "proposed": "Origen", "page": 441, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§15 In like manner, to keep us", "ccel": "In like manners to keep us", "1845": "In like manner, to keep us", "proposed": "manner, to", "page": 444, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§18 a word meaning strength", "ccel": "I have had no hesitations in order", "1845": "I have had no hesitation, in order", "proposed": "hesitation, in", "page": 448, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§28 First, under the rest of the seventh", "ccel": "the seventh days the divine Lawgiver", "1845": "the seventh day, the divine Lawgiver", "proposed": "day, the", "page": 460, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§32 do all things decently and", "ccel": "decently and in orders (1 Cor. 14:40)", "1845": "decently and in order, (1 Cor. xiv. 40.)", "proposed": "order (1 Cor. 14:40)", "page": 464, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§32 without this politic", "ccel": "this politic arrangements that the dissolution", "1845": "this politic arrangement, that the dissolution", "proposed": "arrangement, that", "page": 464, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§33 necessary to retain decency", "ccel": "decency, orders and peace", "1845": "decency, order, and peace", "proposed": "order, and", "page": 465, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§35 For to those whom he raises to", "ccel": "raises to eminences he communicates", "1845": "raises to eminence, he communicates", "proposed": "eminence, he", "page": 467, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§36 be put to death, they being", "ccel": "as it where, unworthy", "1845": "as it were, unworthy", "proposed": "were", "page": 468, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§36 when he commands that", "ccel": "that whose curseth his father", "1845": "that whoso curseth his father", "proposed": "whoso", "page": 468, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§38 pronounces sentence of death", "ccel": "upon theme and orders it", "1845": "upon them, and orders it", "proposed": "them, and", "page": 469, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§42 since natural feeling and the passions", "ccel": "the passions unnamed by the fall", "1845": "the passions inflamed by the fall", "proposed": "inflamed", "page": 472, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§42 unable successfully to war against it", "ccel": "should retake themselves", "1845": "should betake themselves", "proposed": "betake", "page": 472, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§42 that is, in his", "ccel": "in his callings from which", "1845": "in his calling, from which", "proposed": "calling, from", "page": 472, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§42 have made themselves eunuchs", "ccel": "for the kingdom of heavenly sake", "1845": "for the kingdom of heaven’s sake", "proposed": "heaven’s", "page": 473, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§43 The incontinent, therefore", "ccel": "The incontinent, therefore, neglecting", "1845": "The incontinent, therefore, in neglecting", "proposed": "therefore, in neglecting", "page": 474, "kind": "b", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§44 who abhors all", "ccel": "abhors all contaminations whatever", "1845": "abhors all contamination, whatever", "proposed": "contamination, whatever", "page": 475, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§48 an unbecoming proneness to", "ccel": "censorious judgments are here forbidden", "1845": "censorious judgment, are here forbidden", "proposed": "judgment, are", "page": 480, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§49 permitted to insinuate itself", "ccel": "and inhale them with a noxious", "1845": "and inflame them with a noxious", "proposed": "inflame", "page": 481, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "§57 were too difficult for Christians to", "ccel": "for Christians to hear!", "1845": "for Christians to bear!", "proposed": "bear", "page": 489, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: See Augustin. De Civitate Dei", "ccel": "and Lib. 12 c. 20,", "1845": "and Lib. xiii. c. 20,", "proposed": "Lib. 13 c. 20", "page": 434, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Nous avons aussi un autre ancien Pere", "ccel": "celui que a ecrit", "1845": "celui qui a ecrit", "proposed": "qui", "page": 442, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Nous avons aussi un autre ancien Pere (2)", "ccel": "sur Sainct Matthiue.”", "1845": "sur Sainct Matthieu.”", "proposed": "Matthieu", "page": 442, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Calvin. in Catechismo", "ccel": "De Necessitate Reformandæ Ecclesiæ Ratio.", "1845": "De Necessitate Reformandæ Ecclesiæ; Vera Reformandæ Ecclesiæ Ratio.", "proposed": "De Necessitate Reformandæ Ecclesiæ; Vera Reformandæ Ecclesiæ Ratio.", "page": 445, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: 2 Cor. 11:2; Eph. 5:30", "ccel": "Jer. 62:5", "1845": "Jer. lxii. 5", "proposed": "Isa. 62:5 (1845 has the same misprint; Jeremiah has 52 chapters)", "page": 449, "kind": "f", "confidence": "medium"}
{"file": "book-2-chapter-08.typ", "anchor": "note: 1 Sam. 14:44", "ccel": "2 Kings 5:31", "1845": "2 Kings vi. 31", "proposed": "2 Kings 6:31", "page": 455, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Num. 13:22; Ezek. 20:12", "ccel": "Jer. 27:21, 22, 27", "1845": "Jer. xvii. 21, 22, 27", "proposed": "Jer. 17:21, 22, 27", "page": 460, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Num. 13:22; Ezek. 20:12 (2)", "ccel": "Isiah 55:2", "1845": "Isaiah lvi. 2", "proposed": "Isaiah 56:2", "page": 460, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Finem istum politicum", "ccel": "N“Finem istum politicum et ecclesiasticum ordinem.”P—French", "1845": "“Finem istum politicum et ecclesiasticum ordinem.” French", "proposed": "“Finem istum politicum et ecclesiasticum ordinem.”—French (drop stray N and P)", "page": 464, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: ne discernans entre le Dimanche", "ccel": "mais qu’il on faloit", "1845": "mais qu’il en faloit", "proposed": "en", "page": 466, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: leur conviendroyent mieux", "ccel": "whould be more applicable", "1845": "would be more applicable", "proposed": "would", "page": 466, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Exod. 21:17; Lev. 20:9", "ccel": "Mt. 25:4", "1845": "Matth. xv. 4", "proposed": "Mt. 15:4", "page": 468, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Book 3, Chap. 7 sec 4—7", "ccel": "Chap. 17 sec. 38, 40.", "1845": "Chap. xviii. sec. 38, 40.", "proposed": "Chap. 18 sec. 38, 40 (as 1845; neither checked against Book IV)", "page": 471, "kind": "n", "confidence": "medium"}
{"file": "book-2-chapter-08.typ", "anchor": "note: D’avantage ce precepte", "ccel": "s’estend jusques lˆ,", "1845": "s’estend jusques la,", "proposed": "là", "page": 480, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: D’avantage ce precepte (2)", "ccel": "faire vergogne ˆ quelqu’un", "1845": "faire vergogne à quelqu’un", "proposed": "à", "page": 480, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: See August. Ep. 200, ad Asellicum", "ccel": "et Quæstio, Lib. 88, sub fin.", "1845": "et Quæstio, Lib. lxxxiii., sub fin.", "proposed": "Lib. 83 (De diversis quaestionibus LXXXIII)", "page": 482, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: See August. Ep. 200, ad Asellicum (2)", "ccel": "touched on in Ps. 142 and", "1845": "touched on in Ps. cxliii. and", "proposed": "Ps. 143", "page": 482, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-08.typ", "anchor": "note: Is. 1:17", "ccel": "Is. 1:17; 57:6;", "1845": "Is. i. 17; lviii. 6;", "proposed": "Is. 1:17; 58:6;", "page": 485, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§5 he that is least in the kingdom of heaven", "ccel": "is greater than he,” (Mt. 11:28)", "1845": "is greater than he,” (Matth. xi. 11.)", "proposed": "Mt. 11:11", "page": 497, "kind": "f", "confidence": "high"}
{"file": "book-2-chapter-09.typ", "anchor": "§5 Behold, I will send you Elijah", "ccel": "Elijah the prophets before the coming", "1845": "Elijah the prophet, before the coming", "proposed": "prophet, before", "page": 498, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "summary: III. The Old Testament", "ccel": "and examples, see. 5–23.", "1845": "and examples, sec. 5–23.", "proposed": "sec. 5–23", "page": 499, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§3 where any of the others requires", "ccel": "requires explanations to supply it", "1845": "requires explanation, to supply it", "proposed": "explanation, to", "page": 503, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§6 Paul, again, knowing that the", "ccel": "knowing that the Lords when he rained", "1845": "knowing that the Lord, when he rained", "proposed": "Lord, when", "page": 506, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§15 For, in another passage", "ccel": "in another passages after speaking", "1845": "in another passage, after speaking", "proposed": "passage, after", "page": 516, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§19 the mysteries of God, which all in common", "ccel": "all in common behaved to learn", "1845": "all in common behoved to learn", "proposed": "behoved", "page": 520, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§23 spiritual and eternal life, the expectation", "ccel": "the expectation of which behaved to be", "1845": "the expectation of which behoved to be", "proposed": "behoved", "page": 523, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "§23 the substantive existence of spirits", "ccel": "both of which where attested", "1845": "both of which were attested", "proposed": "were", "page": 523, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "note: Veu qu’ils pensent", "ccel": "pensent qu notre Seigneur", "1845": "pensent que notre Seigneur", "proposed": "que", "page": 501, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "note: Veu qu’ils pensent (2)", "ccel": "sans seperance aucune", "1845": "sans esperance aucune", "proposed": "esperance", "page": 501, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-10.typ", "anchor": "note: Et encore ne peut il pas", "ccel": "par eclui du quel", "1845": "par celui du quel", "proposed": "celui", "page": 512, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "Sections 12 Why the calling of the Gentiles", "ccel": "the Gentiles scented to the Apostles", "1845": "the Gentiles seemed to the Apostles", "proposed": "seemed", "page": 526, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§2 Sion overflow with every species", "ccel": "every species at abundance", "1845": "every species of abundance", "proposed": "of", "page": 528, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§4 had foretold concerning the priesthood of Christ", "ccel": "(Ps. 110:4). seeing that an eternal", "1845": "(Ps. cx. 4.) Seeing that an eternal", "proposed": "Seeing", "page": 530, "kind": "d", "confidence": "medium"}
{"file": "book-2-chapter-11.typ", "anchor": "§4 whether or not the ceremonies ordained in the Law", "ccel": "the Law behaved to give way", "1845": "the Law behoved to give way", "proposed": "behoved", "page": 530, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§4 the Apostle contends that it", "ccel": "it behaved to be annulled", "1845": "it behoved to be annulled", "proposed": "behoved", "page": 531, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§7 to explain the meaning of the Prophet", "ccel": "the worlds of the one furnish us", "1845": "the words of the one furnish us", "proposed": "words", "page": 533, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§8 Being a shadow of things to come", "ccel": "it behaved in time to perish", "1845": "it behoved in time to perish", "proposed": "behoved", "page": 534, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§8 riches of the grace with which the same", "ccel": "the same Lawgivers assuming, as it were a new characters honoured", "1845": "the same Lawgiver, assuming, as it were, a new character, honoured", "proposed": "the same Lawgiver, assuming, as it were, a new character, honoured", "page": 535, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§8 of ancient Israel who, with sincere and heartfelt", "ccel": "heartfelt affections embraced the covenant", "1845": "heartfelt affection, embraced the covenant", "proposed": "affection, embraced", "page": 535, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§9 the term bondage is applied to the Old", "ccel": "the Old Testaments because it begets fear", "1845": "the Old Testament, because it begets fear", "proposed": "Testament, because", "page": 535, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§9 he explains more fully in the", "ccel": "in the Epistles to the Galatians", "1845": "in the Epistle to the Galatians", "proposed": "Epistle", "page": 535, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§9 could never attain to the", "ccel": "attain to the inheritances while", "1845": "attain to the inheritance, while", "proposed": "inheritance, while", "page": 535, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§11 the only means of preventing their", "ccel": "preventing their destructions—viz.", "1845": "preventing their destruction, viz.,", "proposed": "destruction—viz.", "page": 538, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "§14 the alternate changes of summer and winter", "ccel": "of clay and night", "1845": "of day and night", "proposed": "day", "page": 541, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "note: et à icelle se doivent reduire", "ccel": "“et ˆ icelle se doivent", "1845": "“et à icelle se doivent", "proposed": "à", "page": 530, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "note: et à icelle (translation)", "ccel": "by way of camparison, opposed", "1845": "by way of comparison, opposed", "proposed": "comparison", "page": 530, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-11.typ", "anchor": "note: Passim", "ccel": "“cá et lá;”", "1845": "“çà et là;”", "proposed": "çà et là", "page": 534, "kind": "n", "confidence": "medium"}
{"file": "book-2-chapter-12.typ", "anchor": "Sections 4 objection against the orthodox doctrine", "ccel": "Answer to it. Conformation from the sacrifices", "1845": "Answer to it. Confirmation from the sacrifices", "proposed": "Confirmation", "page": 2, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§1 sons of Adam? All of them", "ccel": "with their parents, shuddered", "1845": "with their parent, shuddered", "proposed": "parent", "page": 2, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§1 Son of God behoved to become our Emmanuel", "ccel": "our Emmanuel, the God with us;", "1845": "our Emmanuel, i.e. God with us;", "proposed": "our Emmanuel, i.e. God with us", "page": 2, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§4 to bring relief to miserable sinners", "ccel": "sinners, whose overleaps these limits", "1845": "sinners, whoso overleaps these limits", "proposed": "whoso", "page": 5, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "§6 God has distinguished Adam above the other animals", "ccel": "And likewise, with one consent", "1845": "All, likewise, with one consent", "proposed": "All, likewise,", "page": 9, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-12.typ", "anchor": "note: John 3:16; 5:25", "ccel": "John 3:16; 5:25; Mt. 18:11", "1845": "John iii. 16; v. 25; xi. 25; Matth. xviii. 11", "proposed": "John 3:16; 5:25; 11:25; Mt. 18:11", "page": 6, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-13.typ", "anchor": "summary: I. The orthodox doctrine", "ccel": "I. The orthodoxy doctrine", "1845": "I. The orthodox doctrine", "proposed": "orthodox", "page": 13, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-13.typ", "anchor": "Sections 4", "ccel": "#block(inset: (x: 1em))[4\\. Other three objections answered.]", "1845": "(no item 4 in 1845's list of sections)", "proposed": "keep CCEL (it matches the chapter's four sections)", "page": 13, "kind": "info", "confidence": "-"}
{"file": "book-2-chapter-13.typ", "anchor": "§2 1 Pet. 3:18", "ccel": "quickened by the Spirits” (1 Pet. 3:18)", "1845": "quickened by the Spirit,” (1 Pet. iii. 18,)", "proposed": "Spirit” (1 Pet. 3:18)", "page": 15, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-13.typ", "anchor": "§3 that they are classified with men. For this", "ccel": "For this reasons wives", "1845": "For this reason, wives", "proposed": "reason, wives", "page": 18, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-13.typ", "anchor": "§3 I, in my turn", "ccel": "I, in my turn, asks whether", "1845": "I, in my turn, ask, whether", "proposed": "ask, whether", "page": 19, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-13.typ", "anchor": "note: The last clause of this sentence", "ccel": "The last clause of the sentence is omited in the French.", "1845": "The last clause of this sentence is omitted in the French.", "proposed": "this sentence is omitted", "page": 16, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "§1 a figure of speech which the ancients termed", "ccel": "ijdiwmavtwn koinoniva", "1845": "ἰδιωμάτων κοινωνία", "proposed": "ἰδιωμάτων κοινωνία", "page": 23, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-14.typ", "anchor": "§2 There is a communication of", "ccel": "communication of ijdiwvmata, or properties", "1845": "communication of ἰδιωμάτα, or properties", "proposed": "ἰδιώματα", "page": 24, "kind": "e", "confidence": "high (verified; 1845's accent is misplaced)"}
{"file": "book-2-chapter-14.typ", "anchor": "§2 transferred improperly, but not", "ccel": "but not ceaselessly, to his divinity", "1845": "but not causelessly, to his divinity", "proposed": "causelessly", "page": 24, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "§4 in those of Constantinople and", "ccel": "Constantinople and Chalcedony, it being", "1845": "Constantinople and Chalcedon, it being", "proposed": "Chalcedon", "page": 27, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "§5 This is intimated by the angel’s", "ccel": "the angel’s word to Mary", "1845": "the angel’s words to Mary", "proposed": "words", "page": 28, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "§8 he admits that his flesh is", "ccel": "is oJmoouvsion, of the same", "1845": "is ὁμοούσιον, of the same", "proposed": "ὁμοούσιον", "page": 33, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-14.typ", "anchor": "note: Augustine employs the same similitude", "ccel": "the same similitude, Epist. 52.]", "1845": "the same similitude, Epist. cii.", "proposed": "Epist. 102", "page": 23, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "note: Isaiah 41:1, &c.; John 5:17", "ccel": "Isiah 41:1, &c.", "1845": "Isaiah xli. 1, &c.", "proposed": "Isaiah 41:1", "page": 24, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "note: Vide Calv. Epist. ad Polonos", "ccel": "VideCalv. Epist. ad Polonos", "1845": "Vide Calv. Epist. ad Polonos", "proposed": "Vide Calv.", "page": 26, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-14.typ", "anchor": "note: See Irenæus, lib. 4", "ccel": "The above passages from The Proverbs is quoted", "1845": "The above passage from The Proverbs is quoted", "proposed": "passage", "page": 32, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "heading", "ccel": "THREE THINGS BRIEFLY TO BE REGARDED IN", "1845": "THREE THINGS CHIEFLY TO BE REGARDED IN", "proposed": "CHIEFLY", "page": 35, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§2 Is. 61:1, 2", "ccel": "the acceptable year of the Lord,” (Is. 60:1, 2)", "1845": "the acceptable year of the Lord,” (Is. lx. 1, 2.)", "proposed": "Is. 61:1, 2 (1845 has the same misprint)", "page": 37, "kind": "f", "confidence": "high (verified)"}
{"file": "book-2-chapter-15.typ", "anchor": "§3 immediately after Solomon’s death the kingdom", "ccel": "the kingdom in n great measure", "1845": "the kingdom in a great measure", "proposed": "a", "page": 39, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-15.typ", "anchor": "§5 that God may be all in all", "ccel": "that God may be all in and”", "1845": "that God may be all in all,”", "proposed": "all in all”", "page": 42, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§5 by the whole course of his obedience", "ccel": "This id proved by the", "1845": "This is proved by the", "proposed": "is", "page": 51, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§5 might provide for us. We must bear in", "ccel": "We must bear in minds that Christ", "1845": "We must bear in mind, that Christ", "proposed": "mind, that", "page": 53, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§5 both by giving himself up to", "ccel": "himself up to condemnations and undertaking", "1845": "himself up to condemnation, and undertaking", "proposed": "condemnation, and", "page": 53, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§6 This was also shadowed in the Law, since", "ccel": "since twm\\`a\n\n, the word", "1845": "since אשמות, the word", "proposed": "since אשמות, the word (Hebrew in a font encoding, with a false paragraph break)", "page": 54, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-16.typ", "anchor": "§6 that they were a kind of", "ccel": "kind of kaqarmavton (purifications)", "1845": "kind of καθαρμάτων, (purifications,)", "proposed": "καθαρμάτων", "page": 54, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-16.typ", "anchor": "§6 (purifications), bearing, by", "ccel": "bearing, by substitutions the curse", "1845": "bearing, by substitution, the curse", "proposed": "substitution, the", "page": 54, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§6 in order to accomplish a full expiation, he made his soul", "ccel": "made his soul to !\\`a\n\n, #emph[i.e.], a propitiatory", "1845": "made his soul אשם, i. e., a propitiatory", "proposed": "made his soul אשם, #emph[i.e.], a propitiatory (Hebrew in a font encoding, with a stray “to” and a false paragraph break)", "page": 55, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-16.typ", "anchor": "§6 we could have no sure conviction of his being", "ccel": "ajpoluvtrwsi”, ajntivlutron, kai; iJlasthvrion,", "1845": "ἀπολύτρωσις, ἀντίλυτρον, καὶ ἱλαστήριον,", "proposed": "ἀπολύτρωσις, ἀντίλυτρον, καὶ ἱλαστήριον,", "page": 56, "kind": "e", "confidence": "high (verified; 1845 prints the accents loosely)"}
{"file": "book-2-chapter-16.typ", "anchor": "§7 An effect of his burial, moreover", "ccel": "An effect of his burials moreover is", "1845": "An effect of his burial, moreover, is", "proposed": "burial, moreover", "page": 57, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§7 ingrafted into the likeness of", "ccel": "the likeness of Christ’s deaths and that", "1845": "the likeness of Christ’s death, and that", "proposed": "death, and", "page": 57, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§15 All that the Apostles", "ccel": "All that the Apostles intends when", "1845": "All that the Apostles intend, when", "proposed": "intend, when", "page": 69, "kind": "d/comma", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "§19 we must beware of deriving even the", "ccel": "even the minutes portion of it", "1845": "even the minutest portion of it", "proposed": "minutest", "page": 72, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "note: Jusques ici j’ay suivi (translation)", "ccel": "understand on that things we ought", "1845": "understand on what things we ought", "proposed": "what", "page": 72, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "note: Acts 4:12; 1 Cor. 1:30", "ccel": "Heb. 2:17; Gal. 3:3.]", "1845": "Heb. ii. 17; Gal. iii. 13.", "proposed": "Gal. 3:13", "page": 72, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-03.typ", "anchor": "note: Qui a esté une peste mortelle", "ccel": "une peste mortelle ˆ l’Eglise", "1845": "une peste mortelle a l’Eglise", "proposed": "à", "page": 343, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-16.typ", "anchor": "note: Les autres translatent Reverence", "ccel": "c’est mal ˆ propos.", "1845": "c’est mal a propos.", "proposed": "à", "page": 61, "kind": "n", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§1 as the only begotten Son", "ccel": "the only begotten Son at God, could merit", "1845": "the only begotten Son of God, could merit", "proposed": "of", "page": 75, "kind": "d", "confidence": "high"}
{"file": "book-2-chapter-17.typ", "anchor": "§5 designates him by the pronoun", "ccel": "(aujtov”)", "1845": "(αὐτός.)", "proposed": "(αὐτός)", "page": 81, "kind": "e", "confidence": "high (verified)"}
{"file": "book-2-chapter-17.typ", "anchor": "§5 Isaiah 37:35", "ccel": "for mine own sakes and for my servant", "1845": "for mine own sake, and for my servant", "proposed": "sake, and", "page": 80, "kind": "d/comma", "confidence": "high"}
```
