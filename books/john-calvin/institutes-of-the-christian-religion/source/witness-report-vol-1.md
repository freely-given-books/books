# Calvin, Institutes, vol. 1 (prefaces + Book I): CCEL vs the 1845 printing

Base: `chapters/typ/vol-1/*.typ` (CCEL machine pass). Witness: Calvin
Translation Society, Edinburgh 1845, vol. 1 (archive.org
`instituteschrist01calvuoft`). The OCR was aligned word by word with the edition
(difflib; scripts in `scratchpad/calvin-v1/`: `align.py`, `diff.py`, raw
candidates in `cand-*.txt`). Doubtful places were read on the page images
(scan index n = printed page + 121; crops in `scratchpad/calvin-pages/`).
"(verified)" = read on the image. Otherwise the OCR reading is an unambiguous
real word in clean OCR.

**Kinds:** **b** = 1845 words missing in CCEL. **c** = CCEL words not in 1845
(here a displaced line). **d** = a different word. **d/comma** = CCEL turned the
comma after a word into a final "s" ("diligence, against" → "diligences
against"). This is CCEL's commonest slip: 50+ cases, every one checked against
the 1845 comma. **e** = Greek/Latin. **f** = reference numbers. **n** = notes.
**info** = CCEL departs from 1845 but corrects a misprint there; keep CCEL.

**Not listed one by one (CCEL-wide editorial choices, not slips):**
- Roman numerals in references become Arabic ("John iv. 10" → "John 4:10").
- Some British spellings are Americanised ("worshipers", "dishonored",
  "acknowledgement", "baptised"/"baptized", "stupefy").
- *hath/doth* are modernised in quotations (see the section at the end).

**Stray note numbers:** some CCEL footnotes start with a stray number ("70 The
French adds", "80 …", "90 …", "apply:L Nec") left over from CCEL's own note
numbering. 1845 has none. They are listed per chapter.

**Structural:**
- Between the 1559 Epistle and Book I, the 1845 volume also prints "Method and
  Arrangement, or Subject of the Whole Work" (pp. 34–38) and a "General Index
  of Chapters" (pp. 39–44). Our vol-1 files do not have them; decide whether
  the edition wants them.
- Section numbers and "Sections." summaries agree with 1845 in every chapter.
  No section is missing, doubled or renumbered. The one summary fault is ch. 13
  Sections 16, which drops "three persons".
- Footnotes are present and in place throughout. There are no merged or missing
  notes apart from the truncated Gregory note in ch. 11.
- Greek: 1845 has no Greek that CCEL lacks altogether, except οἰκονομίας in the
  Tertullian note (ch. 13). CCEL's Greek often has wrong letters (ε for η, τ for
  σ or θ).
- CCEL turned 1845's italic Latin *dulia*/*latria*/*idolodulia*/*idolatria*
  into Greek letters (ch. 11–12).


## Prefatory Address to Francis I (pp. 3–26) — `01-prefatory-address.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| they greatly concerned though they should see | should see the glow of God dishonoured | should see the glory of God dishonoured | glory | 9 | d | high |
| by constant miracles down to the present day! | Way rather, they allege miracles | Nay rather, they allege miracles | Nay rather | 11 | d | high |
| Our Saviour having declared this | declared this to be test of doctrine | declared this to be the test of doctrine | to be the test of doctrine | 11 | b | high |
| not lord it over us | but that we axe Christ's only | but that we are Christ's only | are | 13 | d | high |
| so much delighted with gold | gold, driver, ivory, marble, gems | gold, silver, ivory, marble, gems | silver | 14 | d | high |
| Nor was this pronounced | by the voice era single individual | by the voice of a single individual | of a | 14 | d | high |
| contaminating the word of God | with the subtleties sophists, and involving it | with the subtleties of sophists, and involving it | subtleties of sophists | 16 | b | high |
| that it may not grow and bear | grow and bear knit. But it will be in vain | grow and bear fruit. But it will be in vain | fruit | 23 | d | high |
| note: Instead of the words here translated | "exquisito splendore vel potius insanc luxu," | "exquisito splendore vel potius insano luxu," | insano | 14 | n | high |
| note xiv. August. lib. 2 De Peccat. Mer. | De Peccat. Mer. cap. uit. | De Peccat. Mer. cap. ult. | ult. | 15 | n | high |
| note: In the last Ed., "justae Dei ultionis:" | in Ed. 1536, "divinae zustitiae." | in Ed. 1536, "divinae justitiae." | justitiae | 20 | n | high |
| note: Instead of "Rex" simply | the E. 1536 has "magnanime Rex." | the Ed. 1536 has "magnanime Rex." | Ed. 1536 | 24 | n | high |
| note: Instead of the whole passage, beginning at bottom of p. 11 | beginning at bottom of p. 11, "It is a Father who testifies," | beginning at bottom of p. 14, "It is a Father who testifies," | 1845's own page: reword as "beginning above" (CCEL's p. 11 is meaningless here) | 15 | n | medium |

## Epistle to the Reader, 1539 (pp. 27–28) — `02-epistle-1539.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| to enter into long discussions | long discussions of doctrines or dilate on common places | long discussions of doctrine, or dilate on common places | doctrine, or | 28 | d/comma | high |

## Subject of the Present Work, 1545 (pp. 29–30) — `03-subject-1545.typ`

No differences beyond OCR noise.

## Epistle to the Reader, 1559 (pp. 31–33) — `04-epistle-1559.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| most ardent desire has been | to advance his kingdoms and promote the public good | to advance his kingdom, and promote the public good | kingdom, and | 32 | d/comma | high |

## Book I, Argument (p. 46) — `book-1-argument.typ`

No differences beyond OCR noise.

## Book I, chapter 01 — `book-1-chapter-01.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 On the other hand, it is evident | until he has previously contemplated the face of God | until he have previously contemplated the face of God | have | 48 | d | high |

## Book I, chapter 02 — `book-1-chapter-02.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 he manifests himself always guarding | with the utmost diligences against transgressing his will | with the utmost diligence, against transgressing his will | diligence, against | 53 | d/comma | high |
| §2 same sentence | wandering, with daring presumptions from the right path | wandering, with daring presumption, from the right path | presumption, from | 53 | d/comma | high |

## Book I, chapter 03 — `book-1-chapter-03.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 That there exists in the human | in the human minds and indeed by natural instinct | in the human mind, and indeed by natural instinct | mind, and | 55 | d/comma | high |
| §2 before the God whom he professedly studied | whom he professedly studied to condemn. | whom he professedly studied to contemn. | contemn | 57 | d | high |
| §3 Though Diagoras | and others of like stamps make themselves merry | and others of like stamp, make themselves merry | stamp, make | 57 | d/comma | high |
| §3 same sentence | and Dionysus scoffs at the judgment of heaven | and Dionysius scoffs at the judgment of heaven | Dionysius | 57 | d | high |
| §3 Thus Gryllus, also, in Plutarch | (lib. guod bruta anim. ratione utantur) | (lib. quod bruta anim. ratione utantur) | quod | 58 | e | high |

## Book I, chapter 04 — `book-1-chapter-04.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §4 with Lactantius | (Instit. Div. lib 1:2, 6) | (Instit. Div. lib. i. 2, 6,) | (Instit. Div. lib. 1. 2, 6) — not a verse reference | 62 | f | medium |

## Book I, chapter 05 — `book-1-chapter-05.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 at the dictation of experience | heathen poets call him the father of men | heathen poets called him the father of men | called | 68 | d | high |
| §5 Virgil verse ("Hence to the bee") | Dwell in high heaven, art star th' ethereal way. | Dwell in high heaven, and star th' ethereal way. | and star | 71 | d | high |
| §5 I admit, indeed that | that the expressions "Nature is God," may be piously used | that the expression, "Nature is God," may be piously used | expression, | 71 | d/comma | high |
| §10 end, in its own place | (Book I. c. 16, see. 6-9) | (Book I. c. 16, sec. 6-9.) | sec. 6-9 | 76 | d | high |
| §12 when they saw that the wisest | contradicted each others they hesitated not | contradicted each other, they hesitated not | each other, they | 78 | d/comma | high |
| note to the verse "Hence to the bee" | Dryden's Virgil, Æneid, Book 4 1. 980-990. | Dryden's Virgil, Book iv. l. 252-262. (verified) | Dryden's Virgil, Book 4, l. 252-262. (Georgics, not Æneid) | 71 | n | high |
| §10 lays his chastening rod on the righteous | far less will the unrighteous ultimately escape | far less will the righteous ultimately escape (verified) | keep CCEL (1845 misprint; sense needs 'unrighteous'); no change | 75 | info | - |

## Book I, chapter 06 — `book-1-chapter-06.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 or those whose sight is defective | when any books however fair, is set before them | when any book, however fair, is set before them | book, however | 84 | d/comma | high |
| §1 known not only as the Creator | Creator of the worlds and the sole author | Creator of the world, and the sole author | world, and | 84 | d/comma | high |
| §4 Accordingly, the same prophet | the firmament sheweth forth the works of his hands | the firmament showeth forth the works of his hands | showeth | 87 | d | medium |
| note 1 (The French adds, C'est à dire) | 70 The French adds, "C'est à dire, temoignages celestes;" | The French adds, "C'est à dire, temoignages celestes;" (verified) | drop the stray "70" | 85 | n | high |

## Book I, chapter 07 — `book-1-chapter-07.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 the Church herself never could have existed | Nothings therefore can be more absurd | Nothing, therefore, can be more absurd | Nothing, therefore, | 91 | d/comma | high |
| §2 the truth of God, she, as in duty | as in duty bounds shows her reverence | as in duty bound, shows her reverence | bound, shows | 91 | d/comma | high |
| §3 may read his short | his short treatises, De Utilitate Credendi | his short treatise, De Utilitate Credendi | treatise, | 93 | d/comma | high |
| §4 if we choose to proceed | in the way of arguments it is easy to establish | in the way of argument, it is easy to establish | argument, it | 93 | d/comma | high |
| §5 Deut. 30:12 | "It is not in heavens that thou shouldest say | "It is not in heaven, that thou shouldest say | heaven, that | 96 | d/comma | high |
| note 2 (diverting it from the only foundation) | the only foundation which is has in scripture | the only foundation which it has in Scripture | it has | 92 | n | high |

## Book I, chapter 08 — `book-1-chapter-08.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §6 But because the fact was too | own experience. But because the fact was too ascribed them to magic (Exod. 9:11). | own experience. But because the fact was too clear to leave it free for heathen writers to deny that Moses did perform miracles, the father of lies suggested a calumny, and ascribed them to magic, (Exod. ix. 11.) (verified) | restore the clause: "too clear to leave it free for heathen writers to deny that Moses did perform miracles, the father of lies suggested a calumny, and ascribed them" | 102 | b | high |
| §6 how could any impostures have enabled | how could any impostures have enabled clear to leave it free for heathen writers to deny that Moses did perform miracles, the father of lies suggested a calumny, and him to elude their rage? | how could any impostures have enabled him to elude their rage? | remove the displaced clause here | 103 | c | high |
| §2 our admiration is | our admiration is elicited more by the dignity of the matter | our admiration is excited more by the dignity of the matter | excited | 98 | d | high |
| §1 (1 Cor. 2:5) | (1 Cor. 2:5), this speech and preaching among them | (1 Cor. ii. 5,) his speech and preaching among them | his | 99 | d | high |
| §6 the ungodly cannot now gain anything | gain anything by their glamour. | gain anything by their clamour. | clamour | 103 | d | high |
| §8 the captivity of the people | (Isaiah 55:1) | (Isaiah xlv. 1.) | Isaiah 45:1 | 104 | f | high |
| §6 to be stoned? | (Lev. 20:27) | (Lev. xxx. 6.) (verified; misprint) | keep CCEL's correction | 102 | info | - |

## Book I, chapter 09 — `book-1-chapter-09.typ`

No differences beyond OCR noise.

## Book I, chapter 10 — `book-1-chapter-10.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| note 1 (De Idolatria … Augustine's grave and admirable reply) | admirable reply. Ep. 42. 43. | admirable reply. Ep. xliii. xliv. | Ep. 43. 44. | 118 | n | medium |

## Book I, chapter 11 — `book-1-chapter-11.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 11, §11, §16 and ch. 12 (×15) | δυλια … λατρια (Greek letters) | dulia … latria, italic Latin (verified pp. 132, 142) | #emph[dulia], #emph[latria] everywhere CCEL has δυλια/λατρια | 120 | e | high |
| §11 they cloak with the name of | εἰδωλοδυλεία (ιδολοδυλια), and deny to be εἰδωλολατρεία (ιδολατρια). | εἰδωλοδυλεία, (idolodulia,) and deny to be εἰδωλολατρεία, (idolatria.) (verified) | εἰδωλοδυλεία (#emph[idolodulia]), and deny to be εἰδωλολατρεία (#emph[idolatria]) | 132 | e | high |
| §11 same | So they speaks holding that the worship | So they speak, holding that the worship | speak, holding | 132 | d/comma | high |
| §1 For we know that the Sun was worshipped | worshipped by the Persian. | worshipped by the Persians. | Persians | 121 | d | high |
| §2 who is the most copious on this | the most copious on this subjects (Isaiah 40:18 | the most copious on this subject, (Isaiah xl. 18 | subject, | 121 | d/comma | high |
| §3 which the Lord founds on his own eternal | his own eternal essences and the uniform course of nature | his own eternal essence, and the uniform course of nature | essence, and | 122 | d/comma | high |
| §5 So said Gregory | but the Holy Spirit goes a very different decision | but the Holy Spirit gives a very different decision | gives | 125 | d | high |
| §8 we wot not what is become of him | (Exod. 22:1) | (Exod. xxxii. 1.) | Exod. 32:1 | 129 | f | high |
| §12 a body which is so like its | so like its oven must be similarly affected | so like its own must be similarly affected | own | 134 | d | high |
| §16 Theodosius Bishop of Amora | fires oft an anathema | fires off an anathema | off | 137 | d | high |
| §5 note (Gregory, Ep. ad Serenum) | See Gregory, Ep. ad Serenum Massiliens, Ep. 109. lib. 7; and Ep. 9 lib. 9; images, rather accuses it. | See Gregory, Ep. ad Serenum Massiliens, Ep. cix. lib. vii.; and Ep. ix. lib. ix.; also Ep. liii. et cxxvi. lib. ii., where Gregory, while wishing to excuse the worship of images, rather accuses it. | insert after "lib. 9;": "also Ep. 53. et 126. lib. 2., where Gregory, while wishing to excuse the worship of" | 125 | b | high |
| note (Neantmoins ils ne disoyent point) | pour cela au'un Dieu fut divisé | pour cela qu'un Dieu fut divisé | qu'un | 131 | n | high |
| note (voire jusques aux oignons et porreaux) | 80 The French adds, | The French adds, | drop the stray "80" | 121 | n | high |
| note (une mechante Proserpine nommée Irene) | 90 The French is | The French is, | drop the stray "90" | 135 | n | high |

## Book I, chapter 12 — `book-1-chapter-12.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 For all that Satan asked was | προσκὺνεσις (obeisance) | προσκύνησις, (obeisance.) (verified) | προσκύνησις | 142 | e | high |
| §2 he could not | προσκὺνει̑ν (do obeisance to) | προσκυνεῖν (do obeisance to) (verified) | προσκυνεῖν | 142 | e | high |
| §2 In like manner, when John is rebuked | In like manners when John is rebuked | In like manner, when John is rebuked | manner, when | 142 | d/comma | high |
| §2 before they came to the knowledge of | the knowledge of Gods he says that they | the knowledge of God, he says, that they | God, he says, | 142 | d/comma | high |

## Book I, chapter 13 — `book-1-chapter-13.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 16 (What view to be taken of the Trinity) | proves that there are in one essence. | proves that there are three persons in one essence. | there are three persons in one essence | 145 | b | high |
| §1 he raises us above the | he raises us above the worlds that he may shake off | he raises us above the world, that he may shake off | world, that | 146 | d/comma | high |
| §2 the term Person as being merely of human | merely of human inventions let us first consider | merely of human invention, let us first consider | invention, let | 147 | d/comma | high |
| §2 to call it his express image | his express image (χαρακτερ). | his express image, (χαρακτὴρ.) (verified) | χαρακτήρ | 147 | e | high |
| §2 the same thing as the Greek | the Greek ὑπόστατις, it betrays | the Greek ὑπόστασις, it betrays (verified) | ὑπόστασις | 148 | e | high |
| §3 by it all the thoughts of | all the thoughts of ours minds | all the thoughts of our minds | our | 149 | d | high |
| §3 same sentence | and the words of our mouths, should he tested. | and the words of our mouths, should be tested. | be | 149 | d | high |
| §4 in order to defeat | in order to defeat it is man's dishonesty, proclaimed that three subsistence were | in order to defeat this man's dishonesty, proclaimed that three subsistences were | this man's … three subsistences | 150 | d | high |
| §5 all further inquiry transcends the | transcends the significance of words | transcends the significancy of words | significancy | 152 | d | medium |
| §9 where Christ is introduced both | both us God, and as possessed of supreme powers one of the peculiar attributes | both as God, and as possessed of supreme power, one of the peculiar attributes | as God … supreme power, one | 156 | d | high |
| §11 And lest the wicked should | lest the wicked should glamour and say | lest the wicked should clamour and say | clamour | 161 | d | high |
| §12 The Lord proclaims by his | by his prophets "I, even I, am he that blotteth out | by his prophet, "I, even I, am he that blotteth out | prophet, | 162 | d/comma | high |
| §13 interprets two passages of Isaiah | "Whose believeth in him shall not be confounded," | "Whoso believeth in him shall not be confounded," | Whoso | 163 | d | high |
| §14 He searches the deep things of | the deep things of Gods and has no counsellor | the deep things of God, and has no counsellor | God, and | 165 | d/comma | high |
| §16 that were there various kinds of faith | there behaved also to be various gods | there behoved also to be various gods | behoved | 167 | d | high |
| §17 which ought to | which ought to he employed in discussing it | which ought to be employed in discussing it | be | 168 | d | high |
| §17 the words of Gregory Nanzianzen | " ̔Ου φθάνω το ἕι νοη̑σαι, καὶ τοι̑ς τρισὶ περιλάμπομαι οὐ φθάνω τὰ τρία διελει̑ν καὶ εὶς τὸ ἑν ἀναφέρομαι" | "Οὐ φθάνω τὸ ἓν νοῆσαι, καὶ τοῖς τρισὶ περιλάμπομαι· οὐ φθάνω τὰ τρία διελεῖν καὶ εἰς τὸ ἓν ἀναφέρομαι" (verified; 1845's own accents are loose) | Οὐ φθάνω τὸ ἓν νοῆσαι, καὶ τοῖς τρισὶ περιλάμπομαι· οὐ φθάνω τὰ τρία διελεῖν, καὶ εἰς τὸ ἓν ἀναφέρομαι | 168 | e | high |
| §18 but they at the same time | they at the same time admits that what they bring forward | they at the same time admit, that what they bring forward | admit, that | 169 | d/comma | high |
| §19 By those names which denote | "By those names which denote distinctions" says Augustine | "By those names which denote distinction," says Augustine | distinction, | 170 | d/comma | high |
| §19 we must always arrive at | we must always arrive at a unity of essence | we must always arrive at an unity of essence | an unity (or keep: modern usage) | 171 | d | low |
| §20 the name of Lord | the name of Lord (Κυρίος) is there put for Jehovah | the name of Lord (Κύριου) is there put for Jehovah (verified) | (Κυρίου) | 171 | e | high |
| §21 For how can the human | how can the human minds which has not yet | how can the human mind, which has not yet | mind, which | 172 | d/comma | high |
| §23 no other God than the | no other God than the Fathers this rank is clearly denied | no other God than the Father, this rank is clearly denied | Father, this | 176 | d/comma | high |
| §23 the Son, who, being thus robbed of his | robbed of his essences will be only a titular God | robbed of his essence, will be only a titular God | essence, will | 177 | d/comma | high |
| §24 assumed the form of a | assumed the form of a servants (Phil. 2:6, 7) | assumed the form of a servant, (Phil. ii. 6, 7.) | servant, | 179 | d/comma | high |
| §24 Let them | Let them glamour as they may | Let them clamour as they may | clamour | 180 | d | high |
| §27 We may | We may adds that in lib. 3 c. 9 | We may add, that in lib. iii. c. 9 | add, that | 184 | d/comma | high |
| §29 those who delight in | those who delight in speculate views | those who delight in speculative views | speculative | 187 | d | high |
| note (Tertullianus, lib. adv. Praxeam) | Perversitas hæ (Praxeæ scil.) … quasi non sic quoque unas sit omnia, … per substantæ scilicet unitatem, et nihilominus custodiatur  sacramentum, … Tres autem non statu, ded gradu … formaæ et species, … et Spriitus sancti | Perversitas hæc (Praxeæ scil.) … unus sit omnia … per substantiæ scilicet unitatem, et nihilominus custodiatur οἰκονομίας sacramentum … non statu, sed gradu … formæ et species … et Spiritus sancti (verified) | hæc; unus; substantiæ; restore οἰκονομίας; sed; formæ; Spiritus | 185 | e/n | high |
| note (August. Homil. De Temp. 38) | Aug. in Psal 59; et Tract. in Joann 89; Idem, in Psal. 68. | Aug. in Psal. cix.; et Tract. in Joann. 39; Idem, in Psal. lxviii. (verified) | Psal. 109; … Joann. 39 | 170 | n/f | high |
| note (Sainct Paul n'eust jamais ainsi parlé) | la vraie Divinté du Sainct Esprit | la vraie Divinité du Sainct Esprit | Divinité | 165 | n | high |
| note (Bernard, Serm. 80, super Cantica) | Gilbert, Bishop of Poiotiers. | Gilbert, Bishop of Poictiers. | Poictiers | 177 | n | high |
| note (veu que l'Apostre en l'allegant de Christ) | lui attribue tout ce qu' est de Dieu | lui attribue tout ce qui est de Dieu | qui est | 179 | n | high |
| note (Athanasius expresses himself thus) | Athanasuis expresses himself | Athanasius expresses himself | Athanasius | 187 | n | high |

## Book I, chapter 14 — `book-1-chapter-14.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 we see how fleeting our attention is | and holy quickly pious thoughts, if any arise, vanish away | and how quickly pious thoughts, if any arise, vanish away | how | 191 | d | high |
| §2 the sanctification of the seventh day | to which the sanctification of the seventh day invited us | to which the sanctification of the seventh day invites us | invites | 191 | d | medium |
| §4 None can deny that / When you read the work of (×2) | Dionysus | Dionysius | Dionysius | 194 | d | high |
| §8 When Daniel introduces the angel of the | the angel of the Persian and the angel of the Greeks | the angel of the Persians and the angel of the Greeks | Persians | 196 | d | high |
| §9 contradicted by so many passages of | so many passages of Scriptures that it seems strange | so many passages of Scripture, that it seems strange | Scripture, that | 199 | d/comma | high |
| §10 In this | In this ways the glory of Christ | In this way, the glory of Christ | way, the | 200 | d/comma | high |
| §11 if we consider why it is that | why it is that Gods instead of acting directly | why it is that God, instead of acting directly | God, instead | 201 | d/comma | high |
| §15 to maintain the Kingdom of Christ | the Kingdom of Christ, v. e must wage irreconcilable war | the Kingdom of Christ, we must wage irreconcileable war | we must | 204 | d | high |
| §19 lest any, by embracing that | by embracing that errors should imagine | by embracing that error, should imagine | error, should | 210 | d/comma | high |
| note (Luke 15:10; Ps. 91:11 …) | Mt. 22:80; 24:36; Eph. 30:10; | Matth. xxii. 30; xxiv. 36; Eph. iii. 10; | Mt. 22:30; … Eph. 3:10 | 199 | n/f | high |
| §19 resist steadfast in the faith | (1 Pet. 5:9) | (1 Pet. v. 8.) | keep CCEL (5:9 is the verse quoted) | 203 | info | - |

## Book I, chapter 15 — `book-1-chapter-15.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 a body formed | a body formed ant of the dust | a body formed out of the dust | out | 214 | d | high |
| §3 to remove the obscurity which was in this | in this terms adds, by way of explanation | in this term, adds, by way of explanation | term, adds | 220 | d/comma | high |
| §5 But before I proceed | before I proceed further, it is necessary | before I proceed farther, it is necessary | farther | 223 | d | medium |
| §6 having no active | having no active powers (which circumstance makes Cicero | having no active power—(which circumstance makes Cicero (verified) | power—(which | 226 | d/comma | high |
| §6 they divide into will and concupiscence | calling it βούλεσις, so whenever the appetite | calling it βούλησις, whenever the appetite (verified) | βούλησις, whenever | 226 | e | high |
| §6 runs to intemperance, they call it | they call it πάτηος. | they call it πάθος. (verified) | πάθος | 226 | e | high |
| §6 negation in the intellect | (Aristot. Ethic. lib. 6 sec. 2) | (Aristot. Ethic. lib. vi. c. 2.) | lib. 6 c. 2 | 227 | f | high |
| §6 seen in another place | (Book 2 c. 2 see. 12-26) | (Book II. c. ii. sec. 12—26,) | sec. 12-26 | 227 | d | high |
| §7 have called her | have called her τὸ ἑγεμονικὸν. | have called her τὸ ἡγεμονικόν. (verified) | τὸ ἡγεμονικόν | 228 | e | high |
| §8 his will was pliable in either | pliable in either directions and he had not received | pliable in either direction, and he had not received | direction, and | 228 | d/comma | high |
| note (As to Osiander's absurd fancy) | see Book 2. cap 12. sec. 5, squ. | see Book II. cap. 12, sec. 5, sq. | sq. | 219 | n | high |
| note (The French is, Et que par iceux) | comme en une cisteren qui recoit d'un coté | comme en une cisterne qui reçoit d'un coté (verified) | cisterne qui reçoit | 225 | n | high |
| §4 when treating of the renewal of the image | renewal | removal (verified; a reader corrected it to 'renewal' by hand) | keep CCEL (1845 misprint) | 224 | info | - |

## Book I, chapter 16 — `book-1-chapter-16.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 the perpetual condition of the world | in the perpetual condition of the world then in its first creation | in the perpetual condition of the world than in its first creation | than | 231 | d | high |
| §2 But whoso has learned | But whose has learned from the mouth of Christ | But whoso has learned from the mouth of Christ | whoso | 233 | d | high |
| §2 for spring, in its | for spring, in its turns to succeed winter | for spring, in its turn, to succeed winter | turn, to | 233 | d/comma | high |
| §3 from the very moment of their | from the very moment of their births they find an aliment | from the very moment of their birth, they find an aliment | birth, they | 235 | d/comma | high |
| §4 the future event was foreknown to | was foreknown to Gods but to resign | was foreknown to God, but to resign | God, but | 236 | d/comma | high |
| §4 In this | In this ways they make man a partner with God | In this way, they make man a partner with God | way, they | 236 | d/comma | high |
| §5 the vicissitudes of day and | the vicissitudes of day and nights summer and winter | the vicissitudes of day and night, summer and winter | night, summer | 238 | d/comma | high |
| §6 to begin to act without him! | Scriptures moreover, the better to show | Scripture, more over, the better to show | Scripture, moreover, | 239 | d/comma | high |
| §6 (Exod. 21:13). In like | In like manners who does not attribute the lot | In like manner, who does not attribute the lot | manner, who | 239 | d/comma | high |
| §6 Ps. 75:6, 7 | he putteth down ones and setteth up another | he putteth down one, and setteth up another | one, and | 240 | d/comma | high |
| §8 a single passage | (De Trinity. lib. 3 cap. 4) | (De Trinit. Lib. iii. cap. 4,) | De Trinit. | 243 | d | high |
| §9 the soothsayers of the / though the (×2) | the Philistine | the Philistines | Philistines | 244 | d | high |
| §9 If the ark, say they | "Goes up by the way of his own coast | goeth up by the way of his own coast | goeth (with the hath-class below) | 244 | d | medium |
| note (Plin. lib. 2. c. 7.) | illud, quicquid est sumum. | illud, quicquid est, summum. | summum | 236 | n | high |
| note (Cest à dire, que non seulement il voit) | ce qu'il veut estra fait | ce qu'il veut estre fait | estre | 236 | n | high |

## Book I, chapter 17 — `book-1-chapter-17.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 they will | they will note like the youth in Plautus | they will not, like the youth in Plautus | not, like | 251 | d | high |
| §3 destroy themselves in | destroy themselves in despairs as if hurried away | destroy themselves in despair, as if hurried away | despair, as | 251 | d/comma | high |
| §3 Homer's Agamemnon | ̔Εγω δ᾽ ούκ ἁίτιός ειμι, ἀλλὰ Ζεὺς και μοι̑ρα. | Ἐγὼ δ' οὐκ αἴτιός εἰμι, ἀλλὰ Ζεὺς καὶ μοῖρα (OCR only; not checked on the image) | Ἐγὼ δ᾽ οὐκ αἴτιός εἰμι, ἀλλὰ Ζεὺς καὶ μοῖρα (Iliad 19.86) | 251 | e | medium |
| §4 A man's heart deviseth his | deviseth his ways but the Lord directeth his steps | deviseth his way, but the Lord directeth his steps | way, but | 252 | d/comma | high |
| §4 the Lord enjoins you to guard against | to guard against its just because he wills | to guard against it, just because he wills | it, just | 253 | d/comma | high |
| §4 the Lord has furnished men with the | furnished men with the artful of deliberation and caution | furnished men with the arts of deliberation and caution | arts | 253 | d | high |
| §7 In this | In this ways he sends Satan | In this way, he sends Satan | way, he | 256 | d/comma | high |
| §7 he so fills them with terror and | terror and dismays that they can neither | terror and dismay, that they can neither | dismay, that | 257 | d/comma | high |
| §12 For, Balaam, even against his will | behaved to break forth into this exclamation | behoved to break forth into this exclamation | behoved | 265 | d | high |
| §14 by threatening of this kind | Who does not now see that, by threatening of this kind | Who does not now see that, by threatenings of this kind | threatenings | 266 | d | high |
| note (Here the words of Cicero admirably apply) | admirably apply:L Nec si ego | admirably apply: Nec si ego | drop stray "L" | 248 | n | high |
| §11 drag them whither he pleases | (Ezek. 29:4) | (Exod. xxix. 4.) (misprint) | keep CCEL's correction | 263 | info | - |

## Book I, chapter 18 — `book-1-chapter-18.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 that Christ should suffer, he has so fulfilled | (Acts 4:18) | (Acts iii. 18.) | Acts 3:18 | 269 | f | high |
| §1 2 Sam. 12:12 | "Thou midst it secretly, but I will do this thing | "Thou didst it secretly, but I will do this thing | didst | 269 | d | high |
| §2 while none knew of | while none knew of its because a sleep from God | while none knew of it, because a sleep from God | it, because | 270 | d/comma | high |
| §2 many would confine to | many would confine to permissions as if | many would confine to permission, as if | permission, as | 270 | d/comma | high |

### Systematic: CCEL modernises *hath*/*doth*/*-eth* in quotations

1845 prints "hath", "doth" (as the AV does) where CCEL has "has", "does"; CCEL's
vol-1 text has only 4 "hath/doth" left in all. This is a CCEL-wide
modernisation, not a slip; restoring 1845 is an editorial decision for the whole
book. Places found by the alignment (1845 reading first): ch. 4 p. 61 Ps 10:11
"He hath said … God hath forgotten"; ch. 5 p. 66 Rom 1:19 "God hath showed";
ch. 6 p. 87 Ps 29:9 "doth every one speak"; ch. 7 p. 96 Isa 53:1 "To whom hath";
ch. 11 p. 136 Luke 11:33 "when he hath lighted"; ch. 13 pp. 163–164 John 6:47
"hath eternal life", Acts 9:13–14 "hath done … hath authority", Isa 48:16 "hath
sent me"; ch. 15 p. 218 Luke 12:5 "after he hath killed"; ch. 16 p. 234 Ps 115:3
"hath done … hath pleased", p. 241 Gen 30:2 "who hath withheld", Deut 8:3 "man
doth not live", p. 244 1 Sam 6:9 "goeth up … hath done"; ch. 17 p. 246 John 9:3
"Neither hath this man", p. 250 Rom 11:34 "who hath known … who hath been",
p. 258 Job 1:21 "hath taken away", 2 Sam 16:10 "the Lord hath said", p. 265 Num
23:19 "hath he said … hath he spoken", p. 266 Isa 14:27 "hath purposed"; ch. 18
p. 268 Job 1:21 "hath taken away … so it hath been done", p. 269 Acts 3:18 "he
hath so fulfilled", p. 271 Ezek 14:9 "when he hath spoken", p. 273 Job 1:21,
Ps 115:3 (×2), Amos 3:6 "which he hath not done", p. 276 2 Kings 10:10 "the
Lord hath done". (Ch. 1 p. 48 "until he have previously" is listed separately:
a subjunctive, not a quotation.)

## Findings as JSON lines

```json
{"file": "01-prefatory-address.typ", "anchor": "they greatly concerned though they should see", "ccel": "should see the glow of God dishonoured", "1845": "should see the glory of God dishonoured", "proposed": "glory", "page": 9, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "by constant miracles down to the present day!", "ccel": "Way rather, they allege miracles", "1845": "Nay rather, they allege miracles", "proposed": "Nay rather", "page": 11, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "Our Saviour having declared this", "ccel": "declared this to be test of doctrine", "1845": "declared this to be the test of doctrine", "proposed": "to be the test of doctrine", "page": 11, "kind": "b", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "not lord it over us", "ccel": "but that we axe Christ's only", "1845": "but that we are Christ's only", "proposed": "are", "page": 13, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "so much delighted with gold", "ccel": "gold, driver, ivory, marble, gems", "1845": "gold, silver, ivory, marble, gems", "proposed": "silver", "page": 14, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "Nor was this pronounced", "ccel": "by the voice era single individual", "1845": "by the voice of a single individual", "proposed": "of a", "page": 14, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "contaminating the word of God", "ccel": "with the subtleties sophists, and involving it", "1845": "with the subtleties of sophists, and involving it", "proposed": "subtleties of sophists", "page": 16, "kind": "b", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "that it may not grow and bear", "ccel": "grow and bear knit. But it will be in vain", "1845": "grow and bear fruit. But it will be in vain", "proposed": "fruit", "page": 23, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "note: Instead of the words here translated", "ccel": "\"exquisito splendore vel potius insanc luxu,\"", "1845": "\"exquisito splendore vel potius insano luxu,\"", "proposed": "insano", "page": 14, "kind": "n", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "note xiv. August. lib. 2 De Peccat. Mer.", "ccel": "De Peccat. Mer. cap. uit.", "1845": "De Peccat. Mer. cap. ult.", "proposed": "ult.", "page": 15, "kind": "n", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "note: In the last Ed., \"justae Dei ultionis:\"", "ccel": "in Ed. 1536, \"divinae zustitiae.\"", "1845": "in Ed. 1536, \"divinae justitiae.\"", "proposed": "justitiae", "page": 20, "kind": "n", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "note: Instead of \"Rex\" simply", "ccel": "the E. 1536 has \"magnanime Rex.\"", "1845": "the Ed. 1536 has \"magnanime Rex.\"", "proposed": "Ed. 1536", "page": 24, "kind": "n", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "note: Instead of the whole passage, beginning at bottom of p. 11", "ccel": "beginning at bottom of p. 11, \"It is a Father who testifies,\"", "1845": "beginning at bottom of p. 14, \"It is a Father who testifies,\"", "proposed": "1845's own page: reword as \"beginning above\" (CCEL's p. 11 is meaningless here)", "page": 15, "kind": "n", "confidence": "medium"}
{"file": "02-epistle-1539.typ", "anchor": "to enter into long discussions", "ccel": "long discussions of doctrines or dilate on common places", "1845": "long discussions of doctrine, or dilate on common places", "proposed": "doctrine, or", "page": 28, "kind": "d/comma", "confidence": "high"}
{"file": "04-epistle-1559.typ", "anchor": "most ardent desire has been", "ccel": "to advance his kingdoms and promote the public good", "1845": "to advance his kingdom, and promote the public good", "proposed": "kingdom, and", "page": 32, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-01.typ", "anchor": "§2 On the other hand, it is evident", "ccel": "until he has previously contemplated the face of God", "1845": "until he have previously contemplated the face of God", "proposed": "have", "page": 48, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-02.typ", "anchor": "§2 he manifests himself always guarding", "ccel": "with the utmost diligences against transgressing his will", "1845": "with the utmost diligence, against transgressing his will", "proposed": "diligence, against", "page": 53, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-02.typ", "anchor": "§2 same sentence", "ccel": "wandering, with daring presumptions from the right path", "1845": "wandering, with daring presumption, from the right path", "proposed": "presumption, from", "page": 53, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "§1 That there exists in the human", "ccel": "in the human minds and indeed by natural instinct", "1845": "in the human mind, and indeed by natural instinct", "proposed": "mind, and", "page": 55, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "§2 before the God whom he professedly studied", "ccel": "whom he professedly studied to condemn.", "1845": "whom he professedly studied to contemn.", "proposed": "contemn", "page": 57, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "§3 Though Diagoras", "ccel": "and others of like stamps make themselves merry", "1845": "and others of like stamp, make themselves merry", "proposed": "stamp, make", "page": 57, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "§3 same sentence", "ccel": "and Dionysus scoffs at the judgment of heaven", "1845": "and Dionysius scoffs at the judgment of heaven", "proposed": "Dionysius", "page": 57, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "§3 Thus Gryllus, also, in Plutarch", "ccel": "(lib. guod bruta anim. ratione utantur)", "1845": "(lib. quod bruta anim. ratione utantur)", "proposed": "quod", "page": 58, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "§4 with Lactantius", "ccel": "(Instit. Div. lib 1:2, 6)", "1845": "(Instit. Div. lib. i. 2, 6,)", "proposed": "(Instit. Div. lib. 1. 2, 6) — not a verse reference", "page": 62, "kind": "f", "confidence": "medium"}
{"file": "book-1-chapter-05.typ", "anchor": "§3 at the dictation of experience", "ccel": "heathen poets call him the father of men", "1845": "heathen poets called him the father of men", "proposed": "called", "page": 68, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "§5 Virgil verse (\"Hence to the bee\")", "ccel": "Dwell in high heaven, art star th' ethereal way.", "1845": "Dwell in high heaven, and star th' ethereal way.", "proposed": "and star", "page": 71, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "§5 I admit, indeed that", "ccel": "that the expressions \"Nature is God,\" may be piously used", "1845": "that the expression, \"Nature is God,\" may be piously used", "proposed": "expression,", "page": 71, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "§10 end, in its own place", "ccel": "(Book I. c. 16, see. 6-9)", "1845": "(Book I. c. 16, sec. 6-9.)", "proposed": "sec. 6-9", "page": 76, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "§12 when they saw that the wisest", "ccel": "contradicted each others they hesitated not", "1845": "contradicted each other, they hesitated not", "proposed": "each other, they", "page": 78, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "note to the verse \"Hence to the bee\"", "ccel": "Dryden's Virgil, Æneid, Book 4 1. 980-990.", "1845": "Dryden's Virgil, Book iv. l. 252-262. (verified)", "proposed": "Dryden's Virgil, Book 4, l. 252-262. (Georgics, not Æneid)", "page": 71, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "§10 lays his chastening rod on the righteous", "ccel": "far less will the unrighteous ultimately escape", "1845": "far less will the righteous ultimately escape (verified)", "proposed": "keep CCEL (1845 misprint; sense needs 'unrighteous'); no change", "page": 75, "kind": "info", "confidence": "-"}
{"file": "book-1-chapter-06.typ", "anchor": "§1 or those whose sight is defective", "ccel": "when any books however fair, is set before them", "1845": "when any book, however fair, is set before them", "proposed": "book, however", "page": 84, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-06.typ", "anchor": "§1 known not only as the Creator", "ccel": "Creator of the worlds and the sole author", "1845": "Creator of the world, and the sole author", "proposed": "world, and", "page": 84, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-06.typ", "anchor": "§4 Accordingly, the same prophet", "ccel": "the firmament sheweth forth the works of his hands", "1845": "the firmament showeth forth the works of his hands", "proposed": "showeth", "page": 87, "kind": "d", "confidence": "medium"}
{"file": "book-1-chapter-06.typ", "anchor": "note 1 (The French adds, C'est à dire)", "ccel": "70 The French adds, \"C'est à dire, temoignages celestes;\"", "1845": "The French adds, \"C'est à dire, temoignages celestes;\" (verified)", "proposed": "drop the stray \"70\"", "page": 85, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "§1 the Church herself never could have existed", "ccel": "Nothings therefore can be more absurd", "1845": "Nothing, therefore, can be more absurd", "proposed": "Nothing, therefore,", "page": 91, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "§2 the truth of God, she, as in duty", "ccel": "as in duty bounds shows her reverence", "1845": "as in duty bound, shows her reverence", "proposed": "bound, shows", "page": 91, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "§3 may read his short", "ccel": "his short treatises, De Utilitate Credendi", "1845": "his short treatise, De Utilitate Credendi", "proposed": "treatise,", "page": 93, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "§4 if we choose to proceed", "ccel": "in the way of arguments it is easy to establish", "1845": "in the way of argument, it is easy to establish", "proposed": "argument, it", "page": 93, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "§5 Deut. 30:12", "ccel": "\"It is not in heavens that thou shouldest say", "1845": "\"It is not in heaven, that thou shouldest say", "proposed": "heaven, that", "page": 96, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "note 2 (diverting it from the only foundation)", "ccel": "the only foundation which is has in scripture", "1845": "the only foundation which it has in Scripture", "proposed": "it has", "page": 92, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§6 But because the fact was too", "ccel": "own experience. But because the fact was too ascribed them to magic (Exod. 9:11).", "1845": "own experience. But because the fact was too clear to leave it free for heathen writers to deny that Moses did perform miracles, the father of lies suggested a calumny, and ascribed them to magic, (Exod. ix. 11.) (verified)", "proposed": "restore the clause: \"too clear to leave it free for heathen writers to deny that Moses did perform miracles, the father of lies suggested a calumny, and ascribed them\"", "page": 102, "kind": "b", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§6 how could any impostures have enabled", "ccel": "how could any impostures have enabled clear to leave it free for heathen writers to deny that Moses did perform miracles, the father of lies suggested a calumny, and him to elude their rage?", "1845": "how could any impostures have enabled him to elude their rage?", "proposed": "remove the displaced clause here", "page": 103, "kind": "c", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§2 our admiration is", "ccel": "our admiration is elicited more by the dignity of the matter", "1845": "our admiration is excited more by the dignity of the matter", "proposed": "excited", "page": 98, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§1 (1 Cor. 2:5)", "ccel": "(1 Cor. 2:5), this speech and preaching among them", "1845": "(1 Cor. ii. 5,) his speech and preaching among them", "proposed": "his", "page": 99, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§6 the ungodly cannot now gain anything", "ccel": "gain anything by their glamour.", "1845": "gain anything by their clamour.", "proposed": "clamour", "page": 103, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§8 the captivity of the people", "ccel": "(Isaiah 55:1)", "1845": "(Isaiah xlv. 1.)", "proposed": "Isaiah 45:1", "page": 104, "kind": "f", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§6 to be stoned?", "ccel": "(Lev. 20:27)", "1845": "(Lev. xxx. 6.) (verified; misprint)", "proposed": "keep CCEL's correction", "page": 102, "kind": "info", "confidence": "-"}
{"file": "book-1-chapter-10.typ", "anchor": "note 1 (De Idolatria … Augustine's grave and admirable reply)", "ccel": "admirable reply. Ep. 42. 43.", "1845": "admirable reply. Ep. xliii. xliv.", "proposed": "Ep. 43. 44.", "page": 118, "kind": "n", "confidence": "medium"}
{"file": "book-1-chapter-11.typ", "anchor": "Sections 11, §11, §16 and ch. 12 (×15)", "ccel": "δυλια … λατρια (Greek letters)", "1845": "dulia … latria, italic Latin (verified pp. 132, 142)", "proposed": "#emph[dulia], #emph[latria] everywhere CCEL has δυλια/λατρια", "page": 120, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§11 they cloak with the name of", "ccel": "εἰδωλοδυλεία (ιδολοδυλια), and deny to be εἰδωλολατρεία (ιδολατρια).", "1845": "εἰδωλοδυλεία, (idolodulia,) and deny to be εἰδωλολατρεία, (idolatria.) (verified)", "proposed": "εἰδωλοδυλεία (#emph[idolodulia]), and deny to be εἰδωλολατρεία (#emph[idolatria])", "page": 132, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§11 same", "ccel": "So they speaks holding that the worship", "1845": "So they speak, holding that the worship", "proposed": "speak, holding", "page": 132, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§1 For we know that the Sun was worshipped", "ccel": "worshipped by the Persian.", "1845": "worshipped by the Persians.", "proposed": "Persians", "page": 121, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§2 who is the most copious on this", "ccel": "the most copious on this subjects (Isaiah 40:18", "1845": "the most copious on this subject, (Isaiah xl. 18", "proposed": "subject,", "page": 121, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§3 which the Lord founds on his own eternal", "ccel": "his own eternal essences and the uniform course of nature", "1845": "his own eternal essence, and the uniform course of nature", "proposed": "essence, and", "page": 122, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§5 So said Gregory", "ccel": "but the Holy Spirit goes a very different decision", "1845": "but the Holy Spirit gives a very different decision", "proposed": "gives", "page": 125, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§8 we wot not what is become of him", "ccel": "(Exod. 22:1)", "1845": "(Exod. xxxii. 1.)", "proposed": "Exod. 32:1", "page": 129, "kind": "f", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§12 a body which is so like its", "ccel": "so like its oven must be similarly affected", "1845": "so like its own must be similarly affected", "proposed": "own", "page": 134, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§16 Theodosius Bishop of Amora", "ccel": "fires oft an anathema", "1845": "fires off an anathema", "proposed": "off", "page": 137, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§5 note (Gregory, Ep. ad Serenum)", "ccel": "See Gregory, Ep. ad Serenum Massiliens, Ep. 109. lib. 7; and Ep. 9 lib. 9; images, rather accuses it.", "1845": "See Gregory, Ep. ad Serenum Massiliens, Ep. cix. lib. vii.; and Ep. ix. lib. ix.; also Ep. liii. et cxxvi. lib. ii., where Gregory, while wishing to excuse the worship of images, rather accuses it.", "proposed": "insert after \"lib. 9;\": \"also Ep. 53. et 126. lib. 2., where Gregory, while wishing to excuse the worship of\"", "page": 125, "kind": "b", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "note (Neantmoins ils ne disoyent point)", "ccel": "pour cela au'un Dieu fut divisé", "1845": "pour cela qu'un Dieu fut divisé", "proposed": "qu'un", "page": 131, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "note (voire jusques aux oignons et porreaux)", "ccel": "80 The French adds,", "1845": "The French adds,", "proposed": "drop the stray \"80\"", "page": 121, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "note (une mechante Proserpine nommée Irene)", "ccel": "90 The French is", "1845": "The French is,", "proposed": "drop the stray \"90\"", "page": 135, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-12.typ", "anchor": "§2 For all that Satan asked was", "ccel": "προσκὺνεσις (obeisance)", "1845": "προσκύνησις, (obeisance.) (verified)", "proposed": "προσκύνησις", "page": 142, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-12.typ", "anchor": "§2 he could not", "ccel": "προσκὺνει̑ν (do obeisance to)", "1845": "προσκυνεῖν (do obeisance to) (verified)", "proposed": "προσκυνεῖν", "page": 142, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-12.typ", "anchor": "§2 In like manner, when John is rebuked", "ccel": "In like manners when John is rebuked", "1845": "In like manner, when John is rebuked", "proposed": "manner, when", "page": 142, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-12.typ", "anchor": "§2 before they came to the knowledge of", "ccel": "the knowledge of Gods he says that they", "1845": "the knowledge of God, he says, that they", "proposed": "God, he says,", "page": 142, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "Sections 16 (What view to be taken of the Trinity)", "ccel": "proves that there are in one essence.", "1845": "proves that there are three persons in one essence.", "proposed": "there are three persons in one essence", "page": 145, "kind": "b", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§1 he raises us above the", "ccel": "he raises us above the worlds that he may shake off", "1845": "he raises us above the world, that he may shake off", "proposed": "world, that", "page": 146, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§2 the term Person as being merely of human", "ccel": "merely of human inventions let us first consider", "1845": "merely of human invention, let us first consider", "proposed": "invention, let", "page": 147, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§2 to call it his express image", "ccel": "his express image (χαρακτερ).", "1845": "his express image, (χαρακτὴρ.) (verified)", "proposed": "χαρακτήρ", "page": 147, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§2 the same thing as the Greek", "ccel": "the Greek ὑπόστατις, it betrays", "1845": "the Greek ὑπόστασις, it betrays (verified)", "proposed": "ὑπόστασις", "page": 148, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§3 by it all the thoughts of", "ccel": "all the thoughts of ours minds", "1845": "all the thoughts of our minds", "proposed": "our", "page": 149, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§3 same sentence", "ccel": "and the words of our mouths, should he tested.", "1845": "and the words of our mouths, should be tested.", "proposed": "be", "page": 149, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§4 in order to defeat", "ccel": "in order to defeat it is man's dishonesty, proclaimed that three subsistence were", "1845": "in order to defeat this man's dishonesty, proclaimed that three subsistences were", "proposed": "this man's … three subsistences", "page": 150, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§5 all further inquiry transcends the", "ccel": "transcends the significance of words", "1845": "transcends the significancy of words", "proposed": "significancy", "page": 152, "kind": "d", "confidence": "medium"}
{"file": "book-1-chapter-13.typ", "anchor": "§9 where Christ is introduced both", "ccel": "both us God, and as possessed of supreme powers one of the peculiar attributes", "1845": "both as God, and as possessed of supreme power, one of the peculiar attributes", "proposed": "as God … supreme power, one", "page": 156, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§11 And lest the wicked should", "ccel": "lest the wicked should glamour and say", "1845": "lest the wicked should clamour and say", "proposed": "clamour", "page": 161, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§12 The Lord proclaims by his", "ccel": "by his prophets \"I, even I, am he that blotteth out", "1845": "by his prophet, \"I, even I, am he that blotteth out", "proposed": "prophet,", "page": 162, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§13 interprets two passages of Isaiah", "ccel": "\"Whose believeth in him shall not be confounded,\"", "1845": "\"Whoso believeth in him shall not be confounded,\"", "proposed": "Whoso", "page": 163, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§14 He searches the deep things of", "ccel": "the deep things of Gods and has no counsellor", "1845": "the deep things of God, and has no counsellor", "proposed": "God, and", "page": 165, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§16 that were there various kinds of faith", "ccel": "there behaved also to be various gods", "1845": "there behoved also to be various gods", "proposed": "behoved", "page": 167, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§17 which ought to", "ccel": "which ought to he employed in discussing it", "1845": "which ought to be employed in discussing it", "proposed": "be", "page": 168, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§17 the words of Gregory Nanzianzen", "ccel": "\" ̔Ου φθάνω το ἕι νοη̑σαι, καὶ τοι̑ς τρισὶ περιλάμπομαι οὐ φθάνω τὰ τρία διελει̑ν καὶ εὶς τὸ ἑν ἀναφέρομαι\"", "1845": "\"Οὐ φθάνω τὸ ἓν νοῆσαι, καὶ τοῖς τρισὶ περιλάμπομαι· οὐ φθάνω τὰ τρία διελεῖν καὶ εἰς τὸ ἓν ἀναφέρομαι\" (verified; 1845's own accents are loose)", "proposed": "Οὐ φθάνω τὸ ἓν νοῆσαι, καὶ τοῖς τρισὶ περιλάμπομαι· οὐ φθάνω τὰ τρία διελεῖν, καὶ εἰς τὸ ἓν ἀναφέρομαι", "page": 168, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§18 but they at the same time", "ccel": "they at the same time admits that what they bring forward", "1845": "they at the same time admit, that what they bring forward", "proposed": "admit, that", "page": 169, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§19 By those names which denote", "ccel": "\"By those names which denote distinctions\" says Augustine", "1845": "\"By those names which denote distinction,\" says Augustine", "proposed": "distinction,", "page": 170, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§19 we must always arrive at", "ccel": "we must always arrive at a unity of essence", "1845": "we must always arrive at an unity of essence", "proposed": "an unity (or keep: modern usage)", "page": 171, "kind": "d", "confidence": "low"}
{"file": "book-1-chapter-13.typ", "anchor": "§20 the name of Lord", "ccel": "the name of Lord (Κυρίος) is there put for Jehovah", "1845": "the name of Lord (Κύριου) is there put for Jehovah (verified)", "proposed": "(Κυρίου)", "page": 171, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§21 For how can the human", "ccel": "how can the human minds which has not yet", "1845": "how can the human mind, which has not yet", "proposed": "mind, which", "page": 172, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§23 no other God than the", "ccel": "no other God than the Fathers this rank is clearly denied", "1845": "no other God than the Father, this rank is clearly denied", "proposed": "Father, this", "page": 176, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§23 the Son, who, being thus robbed of his", "ccel": "robbed of his essences will be only a titular God", "1845": "robbed of his essence, will be only a titular God", "proposed": "essence, will", "page": 177, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§24 assumed the form of a", "ccel": "assumed the form of a servants (Phil. 2:6, 7)", "1845": "assumed the form of a servant, (Phil. ii. 6, 7.)", "proposed": "servant,", "page": 179, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§24 Let them", "ccel": "Let them glamour as they may", "1845": "Let them clamour as they may", "proposed": "clamour", "page": 180, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§27 We may", "ccel": "We may adds that in lib. 3 c. 9", "1845": "We may add, that in lib. iii. c. 9", "proposed": "add, that", "page": 184, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§29 those who delight in", "ccel": "those who delight in speculate views", "1845": "those who delight in speculative views", "proposed": "speculative", "page": 187, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "note (Tertullianus, lib. adv. Praxeam)", "ccel": "Perversitas hæ (Praxeæ scil.) … quasi non sic quoque unas sit omnia, … per substantæ scilicet unitatem, et nihilominus custodiatur  sacramentum, … Tres autem non statu, ded gradu … formaæ et species, … et Spriitus sancti", "1845": "Perversitas hæc (Praxeæ scil.) … unus sit omnia … per substantiæ scilicet unitatem, et nihilominus custodiatur οἰκονομίας sacramentum … non statu, sed gradu … formæ et species … et Spiritus sancti (verified)", "proposed": "hæc; unus; substantiæ; restore οἰκονομίας; sed; formæ; Spiritus", "page": 185, "kind": "e/n", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "note (August. Homil. De Temp. 38)", "ccel": "Aug. in Psal 59; et Tract. in Joann 89; Idem, in Psal. 68.", "1845": "Aug. in Psal. cix.; et Tract. in Joann. 39; Idem, in Psal. lxviii. (verified)", "proposed": "Psal. 109; … Joann. 39", "page": 170, "kind": "n/f", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "note (Sainct Paul n'eust jamais ainsi parlé)", "ccel": "la vraie Divinté du Sainct Esprit", "1845": "la vraie Divinité du Sainct Esprit", "proposed": "Divinité", "page": 165, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "note (Bernard, Serm. 80, super Cantica)", "ccel": "Gilbert, Bishop of Poiotiers.", "1845": "Gilbert, Bishop of Poictiers.", "proposed": "Poictiers", "page": 177, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "note (veu que l'Apostre en l'allegant de Christ)", "ccel": "lui attribue tout ce qu' est de Dieu", "1845": "lui attribue tout ce qui est de Dieu", "proposed": "qui est", "page": 179, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "note (Athanasius expresses himself thus)", "ccel": "Athanasuis expresses himself", "1845": "Athanasius expresses himself", "proposed": "Athanasius", "page": 187, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§2 we see how fleeting our attention is", "ccel": "and holy quickly pious thoughts, if any arise, vanish away", "1845": "and how quickly pious thoughts, if any arise, vanish away", "proposed": "how", "page": 191, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§2 the sanctification of the seventh day", "ccel": "to which the sanctification of the seventh day invited us", "1845": "to which the sanctification of the seventh day invites us", "proposed": "invites", "page": 191, "kind": "d", "confidence": "medium"}
{"file": "book-1-chapter-14.typ", "anchor": "§4 None can deny that / When you read the work of (×2)", "ccel": "Dionysus", "1845": "Dionysius", "proposed": "Dionysius", "page": 194, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§8 When Daniel introduces the angel of the", "ccel": "the angel of the Persian and the angel of the Greeks", "1845": "the angel of the Persians and the angel of the Greeks", "proposed": "Persians", "page": 196, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§9 contradicted by so many passages of", "ccel": "so many passages of Scriptures that it seems strange", "1845": "so many passages of Scripture, that it seems strange", "proposed": "Scripture, that", "page": 199, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§10 In this", "ccel": "In this ways the glory of Christ", "1845": "In this way, the glory of Christ", "proposed": "way, the", "page": 200, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§11 if we consider why it is that", "ccel": "why it is that Gods instead of acting directly", "1845": "why it is that God, instead of acting directly", "proposed": "God, instead", "page": 201, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§15 to maintain the Kingdom of Christ", "ccel": "the Kingdom of Christ, v. e must wage irreconcilable war", "1845": "the Kingdom of Christ, we must wage irreconcileable war", "proposed": "we must", "page": 204, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§19 lest any, by embracing that", "ccel": "by embracing that errors should imagine", "1845": "by embracing that error, should imagine", "proposed": "error, should", "page": 210, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "note (Luke 15:10; Ps. 91:11 …)", "ccel": "Mt. 22:80; 24:36; Eph. 30:10;", "1845": "Matth. xxii. 30; xxiv. 36; Eph. iii. 10;", "proposed": "Mt. 22:30; … Eph. 3:10", "page": 199, "kind": "n/f", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§19 resist steadfast in the faith", "ccel": "(1 Pet. 5:9)", "1845": "(1 Pet. v. 8.)", "proposed": "keep CCEL (5:9 is the verse quoted)", "page": 203, "kind": "info", "confidence": "-"}
{"file": "book-1-chapter-15.typ", "anchor": "§1 a body formed", "ccel": "a body formed ant of the dust", "1845": "a body formed out of the dust", "proposed": "out", "page": 214, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§3 to remove the obscurity which was in this", "ccel": "in this terms adds, by way of explanation", "1845": "in this term, adds, by way of explanation", "proposed": "term, adds", "page": 220, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§5 But before I proceed", "ccel": "before I proceed further, it is necessary", "1845": "before I proceed farther, it is necessary", "proposed": "farther", "page": 223, "kind": "d", "confidence": "medium"}
{"file": "book-1-chapter-15.typ", "anchor": "§6 having no active", "ccel": "having no active powers (which circumstance makes Cicero", "1845": "having no active power—(which circumstance makes Cicero (verified)", "proposed": "power—(which", "page": 226, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§6 they divide into will and concupiscence", "ccel": "calling it βούλεσις, so whenever the appetite", "1845": "calling it βούλησις, whenever the appetite (verified)", "proposed": "βούλησις, whenever", "page": 226, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§6 runs to intemperance, they call it", "ccel": "they call it πάτηος.", "1845": "they call it πάθος. (verified)", "proposed": "πάθος", "page": 226, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§6 negation in the intellect", "ccel": "(Aristot. Ethic. lib. 6 sec. 2)", "1845": "(Aristot. Ethic. lib. vi. c. 2.)", "proposed": "lib. 6 c. 2", "page": 227, "kind": "f", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§6 seen in another place", "ccel": "(Book 2 c. 2 see. 12-26)", "1845": "(Book II. c. ii. sec. 12—26,)", "proposed": "sec. 12-26", "page": 227, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§7 have called her", "ccel": "have called her τὸ ἑγεμονικὸν.", "1845": "have called her τὸ ἡγεμονικόν. (verified)", "proposed": "τὸ ἡγεμονικόν", "page": 228, "kind": "e", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§8 his will was pliable in either", "ccel": "pliable in either directions and he had not received", "1845": "pliable in either direction, and he had not received", "proposed": "direction, and", "page": 228, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "note (As to Osiander's absurd fancy)", "ccel": "see Book 2. cap 12. sec. 5, squ.", "1845": "see Book II. cap. 12, sec. 5, sq.", "proposed": "sq.", "page": 219, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "note (The French is, Et que par iceux)", "ccel": "comme en une cisteren qui recoit d'un coté", "1845": "comme en une cisterne qui reçoit d'un coté (verified)", "proposed": "cisterne qui reçoit", "page": 225, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§4 when treating of the renewal of the image", "ccel": "renewal", "1845": "removal (verified; a reader corrected it to 'renewal' by hand)", "proposed": "keep CCEL (1845 misprint)", "page": 224, "kind": "info", "confidence": "-"}
{"file": "book-1-chapter-16.typ", "anchor": "§1 the perpetual condition of the world", "ccel": "in the perpetual condition of the world then in its first creation", "1845": "in the perpetual condition of the world than in its first creation", "proposed": "than", "page": 231, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§2 But whoso has learned", "ccel": "But whose has learned from the mouth of Christ", "1845": "But whoso has learned from the mouth of Christ", "proposed": "whoso", "page": 233, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§2 for spring, in its", "ccel": "for spring, in its turns to succeed winter", "1845": "for spring, in its turn, to succeed winter", "proposed": "turn, to", "page": 233, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§3 from the very moment of their", "ccel": "from the very moment of their births they find an aliment", "1845": "from the very moment of their birth, they find an aliment", "proposed": "birth, they", "page": 235, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§4 the future event was foreknown to", "ccel": "was foreknown to Gods but to resign", "1845": "was foreknown to God, but to resign", "proposed": "God, but", "page": 236, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§4 In this", "ccel": "In this ways they make man a partner with God", "1845": "In this way, they make man a partner with God", "proposed": "way, they", "page": 236, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§5 the vicissitudes of day and", "ccel": "the vicissitudes of day and nights summer and winter", "1845": "the vicissitudes of day and night, summer and winter", "proposed": "night, summer", "page": 238, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§6 to begin to act without him!", "ccel": "Scriptures moreover, the better to show", "1845": "Scripture, more over, the better to show", "proposed": "Scripture, moreover,", "page": 239, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§6 (Exod. 21:13). In like", "ccel": "In like manners who does not attribute the lot", "1845": "In like manner, who does not attribute the lot", "proposed": "manner, who", "page": 239, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§6 Ps. 75:6, 7", "ccel": "he putteth down ones and setteth up another", "1845": "he putteth down one, and setteth up another", "proposed": "one, and", "page": 240, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§8 a single passage", "ccel": "(De Trinity. lib. 3 cap. 4)", "1845": "(De Trinit. Lib. iii. cap. 4,)", "proposed": "De Trinit.", "page": 243, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§9 the soothsayers of the / though the (×2)", "ccel": "the Philistine", "1845": "the Philistines", "proposed": "Philistines", "page": 244, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§9 If the ark, say they", "ccel": "\"Goes up by the way of his own coast", "1845": "goeth up by the way of his own coast", "proposed": "goeth (with the hath-class below)", "page": 244, "kind": "d", "confidence": "medium"}
{"file": "book-1-chapter-16.typ", "anchor": "note (Plin. lib. 2. c. 7.)", "ccel": "illud, quicquid est sumum.", "1845": "illud, quicquid est, summum.", "proposed": "summum", "page": 236, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "note (Cest à dire, que non seulement il voit)", "ccel": "ce qu'il veut estra fait", "1845": "ce qu'il veut estre fait", "proposed": "estre", "page": 236, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§3 they will", "ccel": "they will note like the youth in Plautus", "1845": "they will not, like the youth in Plautus", "proposed": "not, like", "page": 251, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§3 destroy themselves in", "ccel": "destroy themselves in despairs as if hurried away", "1845": "destroy themselves in despair, as if hurried away", "proposed": "despair, as", "page": 251, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§3 Homer's Agamemnon", "ccel": "̔Εγω δ᾽ ούκ ἁίτιός ειμι, ἀλλὰ Ζεὺς και μοι̑ρα.", "1845": "Ἐγὼ δ' οὐκ αἴτιός εἰμι, ἀλλὰ Ζεὺς καὶ μοῖρα (OCR only; not checked on the image)", "proposed": "Ἐγὼ δ᾽ οὐκ αἴτιός εἰμι, ἀλλὰ Ζεὺς καὶ μοῖρα (Iliad 19.86)", "page": 251, "kind": "e", "confidence": "medium"}
{"file": "book-1-chapter-17.typ", "anchor": "§4 A man's heart deviseth his", "ccel": "deviseth his ways but the Lord directeth his steps", "1845": "deviseth his way, but the Lord directeth his steps", "proposed": "way, but", "page": 252, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§4 the Lord enjoins you to guard against", "ccel": "to guard against its just because he wills", "1845": "to guard against it, just because he wills", "proposed": "it, just", "page": 253, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§4 the Lord has furnished men with the", "ccel": "furnished men with the artful of deliberation and caution", "1845": "furnished men with the arts of deliberation and caution", "proposed": "arts", "page": 253, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§7 In this", "ccel": "In this ways he sends Satan", "1845": "In this way, he sends Satan", "proposed": "way, he", "page": 256, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§7 he so fills them with terror and", "ccel": "terror and dismays that they can neither", "1845": "terror and dismay, that they can neither", "proposed": "dismay, that", "page": 257, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§12 For, Balaam, even against his will", "ccel": "behaved to break forth into this exclamation", "1845": "behoved to break forth into this exclamation", "proposed": "behoved", "page": 265, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§14 by threatening of this kind", "ccel": "Who does not now see that, by threatening of this kind", "1845": "Who does not now see that, by threatenings of this kind", "proposed": "threatenings", "page": 266, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "note (Here the words of Cicero admirably apply)", "ccel": "admirably apply:L Nec si ego", "1845": "admirably apply: Nec si ego", "proposed": "drop stray \"L\"", "page": 248, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§11 drag them whither he pleases", "ccel": "(Ezek. 29:4)", "1845": "(Exod. xxix. 4.) (misprint)", "proposed": "keep CCEL's correction", "page": 263, "kind": "info", "confidence": "-"}
{"file": "book-1-chapter-18.typ", "anchor": "§3 that Christ should suffer, he has so fulfilled", "ccel": "(Acts 4:18)", "1845": "(Acts iii. 18.)", "proposed": "Acts 3:18", "page": 269, "kind": "f", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§1 2 Sam. 12:12", "ccel": "\"Thou midst it secretly, but I will do this thing", "1845": "\"Thou didst it secretly, but I will do this thing", "proposed": "didst", "page": 269, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§2 while none knew of", "ccel": "while none knew of its because a sleep from God", "1845": "while none knew of it, because a sleep from God", "proposed": "it, because", "page": 270, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§2 many would confine to", "ccel": "many would confine to permissions as if", "1845": "many would confine to permission, as if", "proposed": "permission, as", "page": 270, "kind": "d/comma", "confidence": "high"}
```
