# Calvin, Institutes, vol. 3 (Book III, Argument and chapters 1–10): CCEL vs the 1845 printing

Base: `chapters/typ/vol-3/*.typ` (CCEL machine pass). Witness: Calvin
Translation Society, Edinburgh 1845, vol. 2 (archive.org
`institutesofreli02calvuoft`): Book III, Argument p. 83, chapters 1–10 pp.
85–300. The OCR was aligned word by word with the edition (difflib; scripts in
`scratchpad/calvin-v3/`: `align.py` writes raw candidates to `cand-*.txt`,
`notes.py` compares each footnote with its best OCR window, findings in
`findings.jsonl`, `build.py` writes this file and checks that every "ccel"
string occurs exactly once in its file). Doubtful places were read on the
page images (crops in `scratchpad/calvin-pages/`, files `q*.jpg`): the scan
index n = printed page + 9 holds for Book III too (checked on pp. 93, 99, 124,
144 and others). "verified" in the confidence column = read on the image.
Otherwise the OCR reading is an unambiguous real word in clean OCR.

**Kinds:** **b** = 1845 words missing in CCEL. **c** = CCEL words not in 1845.
**d** = a different word. **d/comma** = CCEL turned the comma after a word
into a final "s" ("subject, we" → "subjects we"); every case checked against
the 1845 comma. **e** = Greek/Latin. **f** = reference numbers (proposed in
CCEL's Arabic style). **n** = notes. **info** = CCEL departs from 1845 but
corrects a misprint there; keep CCEL.

**Not listed one by one (CCEL-wide editorial choices, kept by the edition):**
Arabic numerals in references; CCEL's spellings (fulfill, instill,
recognize, offense, dullness, Mt. for Matth.); has/does for hath/doth in
Scripture quotations; CCEL's punctuation around references; closed-up
compounds (nobleman, thereafter, cannot).

**Greek and Hebrew encoding.** A search of every vol-3 file for Greek in the
old SGreek font codes (Latin letters such as "filautiva kai;"), private-use
characters and Hebrew font codes found none: all Greek here is Unicode
(decomposed accents). Some of it is misspelt; those words are listed (kind e).

**"divcs":** not in vol-3 (no match in any vol-3 file).


## Book III, Argument (p. 83) — `book-3-argument.typ`

No differences beyond OCR noise.

## Book III, chapter 01 — `book-3-chapter-01.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 But in order to have a clearer view | important subjects we | important subject, we | subject, we | 87 | d/comma | high |
| §3 so as to become our Father | become our Fathers and | become our Father, and | Father, and | 88 | d/comma | high |
| §3 boldness of access to him | to him; nays he | to him; nay, he | nay, he | 88 | d/comma | high |
| note: Rom. 8:15; 2 Cor. 1:22 (titles of the Spirit) | John 2:14; | John ii. 14 | John 4:14 (the fountain of water springing up; 1845 has the same misprint) | 89 | f | medium |
| note: Rom. 8:15; 2 Cor. 1:22 (titles of the Spirit) | John 7:37; | John viii. 37 | keep John 7:37 (CCEL corrects 1845's misprint) | 89 | info | high |

## Book III, chapter 02 — `book-3-chapter-02.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 17 | opposite example of Ahab. | opposite example of Ahaz. | Ahaz | 93 | d | high (verified) |
| Sections 19 | Conformation from | Confirmation from | Confirmation | 93 | d | high (verified) |
| §5 the Samaritans who believed | who believed the women | who believed the woman | woman | 100 | d | high |
| §6 unless you feel firmly persuaded | every word which him | every word which proceeds from him | which proceeds from him | 102 | b | high |
| §9 impugn, reject, or | reject, or condemn | reject, or contemn | contemn | 107 | d | high |
| §12 they deprecate his anger | they retake themselves | they betake themselves | betake | 110 | d | high |
| §12 Every plant which my heavenly Father | (Mt. 16:13) | (Matth. xvi. 13.) | (Mt. 15:13) (1845 has the same misprint) | 111 | f | high |
| §15 feeling of full assurance | assurance (πλεροφορία) | assurance (πληροφορία) | πληροφορία | 114 | e | high |
| §17 How did Ahaz act? | How did Ahab act? | How did Ahaz act? | Ahaz | 117 | d | high |
| §17 Take not the word of truth | my mouths” | my mouth,” | mouth,” | 118 | d/comma | high |
| §18 rising up to assail the faith | faith enlisting in | faith existing in | existing | 118 | d | high |
| §20 faith is imperfect so long as we groan | under a height of | under a weight of | weight | 119 | d | high |
| §22 not excluded from the covenant | covenant of adoptions so | covenant of adoption, so | adoption, so | 123 | d/comma | high |
| §23 worship toward thy holy temple | holy temples” | holy temple,” | temple,” | 123 | d/comma | high |
| §25 man doubtless has been made subject to vanity | man here been | man has been | has | 126 | d | high |
| §27 Mere threatenings | mere threatening have | mere threatenings have | threatenings | 128 | d | high |
| §29 give heed to his threatenings | to his threatening; | to his threatenings; | threatenings | 130 | d | high |
| §9 moved to some degree by its threatenings | its threatening and | its threatenings and | threatenings | 106 | d | high |
| §30 Noah ... feared the destruction of the world | (Heb. 11:17) | (Heb. xi. 17.) | (Heb. 11:7) (1845 has the same misprint) | 130 | f | high |
| §30 a work of faith, threatenings ought | faith, threatening ought | faith, threatenings ought | threatenings | 131 | d | high |
| §30 unless in so far as it ingrafts us | in grafts us | ingrafts us | ingrafts | 131 | d | high |
| §32 Hence, with good reason | with good reasons Paul | with good reason, Paul | reason, Paul | 135 | d/comma | high |
| §33 beholding divine mysteries | divine masteries | divine mysteries | mysteries | 137 | d | high |
| §40 an approach to arrogance | arrogance in each glorying | arrogance in such glorying | such | 144 | d | high (verified) |
| §41 For as Paul says (Rom. 8:24) | “A hope that is seen | “hope that is seen | “hope that is seen | 144 | c | high (verified) |
| §41 the Greek term being | being ἔλενγχος, | being ἔλεγχος, | ἔλεγχος | 144 | e | high (verified) |
| §43 ready to be revealed in the last time | the last times” | the last time,” | time,” | 147 | d/comma | high |
| §43 as in the same Epistle | the same Epistles “ | the same Epistle, “ | Epistle, “ | 147 | d/comma | high |
| note: The French is, “Car nous tendons | The French is“Car | The French is, “Car | is, “Car | 97 | n | high |
| note: As to the imperfection, strengthening | Book 4. chap. 4 sec | Book IV. chap. xiv. sec | Book 4. chap. 14 sec | 116 | f | high |
| note: See Calv. adv. Pighium | Pighiium | Pighium | Pighium | 117 | n | high |
| note: Latin, “Præsentim ubi ad rem | Latin“Præsentim | Latin, “Præsentim | Latin, “Præsentim | 114 | n | high |
| note: Latin, “Præsentim ubi ad rem | Principalament | Principalement | Principalement | 114 | n | high |
| note: Latin, “acsi cervicibus suis | engulfthem | engulf them | engulf them | 128 | n | high |
| note: The French adds, “En quoy ils demonstrent | leur betisc | leur betise | betise | 142 | n | high |
| Sections 21 | he retakes himself | he betakes himself | betakes | 93 | d | high (verified) |
| §21 whenever the sinner betakes himself | sinner retakes himself | sinner betakes himself | betakes | 120 | d | high |

## Book III, chapter 03 — `book-3-chapter-03.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 2 | Conformation from | Confirmation from | Confirmation | 150 | d | high |
| §1 no man can embrace the grace of the Gospel | without retaking himself | without betaking himself | betaking | 152 | d | high |
| §3 Certain learned men, who lived long before | the present days and | the present day, and | day, and | 153 | d/comma | high |
| §5 with true repentance, betake themselves | repentance, retake themselves | repentance, betake themselves | betake | 156 | d | high |
| §6 And to make the deeper impression | And to malice the | And to make the | make | 157 | d | high |
| §7 The stern threatenings which God employs | stern threatening which | stern threatenings which | threatenings | 158 | d | high |
| §8 instilling his holiness into our souls | so inspired them | so inspires them | inspires | 159 | d | high (verified) |
| §9 Be renewed in the spirit of your mind | of your minds” | of your mind,” | mind,” | 160 | d/comma | high |
| §10 the very pravity which begets | very gravity which | very pravity which | pravity | 161 | d | high |
| §10 Augustine himself does not always refrain | himself dose not | himself does not | does | 161 | d | high |
| §14 daily struggling with the evil | entangled. Hence, too | entangled. Whence, too | Whence | 166 | d | high |
| §15 The Apostle, in his description of repentance | description of repentance ( | description of repentance, (2 Cor. vii. 2,) | (2 Cor. 7:11) (1845 has the same misprint, 7:2; the seven fruits are in 7:11) | 166 | f | high (verified) |
| §17 rend your heart ... The fasting | The “fastings” | The “fasting,” | “fasting,” | 169 | d/comma | high |
| §19 repent ye, and believe the Gospel | (Mark 1:10) | (Mark i. 15.) | (Mark 1:15) | 173 | f | high |
| §19 a brief summary of the whole Gospel | he behaved “to | he behoved “to | behoved | 173 | d | high |
| §21 If God peradventure will give them repentance | God per adventure | God peradventure | peradventure | 175 | d | high |
| §22 they defamed him by the name of Beelzebub | (Mt. 9:3, 4; 12:24) | (Matth. ix. 3, 4; xii. 24.) | (Mt. 9:34; 12:24) (1845 has the same misprint) | 178 | f | high |
| §24 deny forgiveness to any who betake themselves | any who retake themselves | any who betake themselves | betake | 179 | d | high |
| §25 disregard the divine threatenings | divine threatening. | divine threatenings. | threatenings | 181 | d | high |
| note: Latin, “Initialis timor” | une erainte | une crainte | crainte | 153 | n | high |
| note: Latin, “Initialis timor” | par arison | par raison | raison | 153 | n | high |
| note: 2 Kings 20:2; Isa. ... | Isa. 37:2 | Isa. xxxviii. 2 | Isa. 38:2 | 155 | f | high |
| note: Latin, “Reatus.” | Reatus.”—the | Reatus.”—French, “l’imputation du peché;”—the | Reatus.”—French, “l’imputation du peché;”—the | 162 | b | high (verified) |
| note: French, “Circonstances qui convenoyent | specialement alore | specialement alors | alors | 170 | n | high |
| note: French, “Fust la coustume de ce temps-la | aujourduhui | aujourdhui | aujourdhui | 170 | n | high |
| note: Isaiah 56:1; 59:20 | Isiah 56 | Isaiah lvi. | Isaiah 56 | 174 | n | high |
| note: The French adds, “Et ce non seulement | jour. mais | jour, mais | jour, mais | 175 | n | high |
| note: The Greek is | Greek is “του̑ | Greek is, “τοῦ | τοῦ (CCEL has υ with a combining inverted breve, U+0311, for the circumflex) | 177 | e | high (verified) |
| note: The Greek is | blasphemiæ,”, | blasphemiæ,” | blasphemiæ,” | 177 | n | high (verified) |

## Book III, chapter 04 — `book-3-chapter-04.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 This I will do as briefly as possible | for I leave no | for I have no | have | 185 | d | high |
| §1 to bewail past evils | and not to sin to do | and not again to do | again | 185 | d | high |
| §1 miserably entangle themselves | they are pealing | they are prating | prating | 187 | d | high |
| §1 whether punishments divinely inflicted | divinely indicted | divinely inflicted | inflicted | 187 | d | high |
| §4 Adam having replied as if excepting | “The women whom | “The woman whom | woman | 189 | d | high |
| §4 in order that, in the judgment of God | judgment of Gods they | judgment of God, they | God, they | 191 | d/comma | high |
| §4 they might be more fully convicted | more filly convicted | more fully convicted | fully | 191 | d | high |
| §5 see him rise by the mere power of a word | handle hint | handle him | him | 191 | d | high |
| §6 He says, ἀλλήλους | He says, “allelous” | He says, ἀλλήλους, | He says, ἀλλήλους (CCEL transliterates the Greek) | 192 | e | high (verified) |
| §7 the decree of the Council of Lateran | Council of Lateral | Council of Lateran | Lateran | 193 | d | high |
| §7 let them charge with defection | charge with defections not | charge with defection, not | defection, not | 195 | d/comma | high |
| §9 those only which contain a summary | which contain summary | which contain a summary | contain a summary | 196 | b | high |
| §9 He is the discerner of the heart | knows all one thoughts | knows all our thoughts | our | 196 | d | high |
| §9 Another specimen of David’s confession | David’s confessions | David’s confession | confession | 196 | d | high |
| §11 if it is our duty to betake ourselves | duty to retake | duty to betake | betake | 198 | d | high |
| §12 to assure our consciences of the forgiveness of sins | forgiveness of fins | forgiveness of sins | sins | 199 | d | high |
| §14 invested with the mandate of reconciliation | mandate of reconciliations by | mandate of reconciliation, by | reconciliation, by | 201 | d/comma | high |
| §14 nevertheless remains somewhat in doubt | somewhat in doubts, | somewhat in doubt, | doubt, | 201 | d | high |
| §14 But when we treat of the keys, we | keys, us must | keys, we must | we | 202 | d | high |
| §15 the conferring of the keys must be taken with limitation | taken with limitations because | taken with limitation, because | limitation, because | 203 | d/comma | high |
| §17 First, they betook themselves to calculation | they retook | they betook | betook | 204 | d | high |
| §18 hence its only result is to destroy | only results to | only result is to | result is | 205 | d | high (verified) |
| §19 they can wipe their lips | wipe their lip, | wipe their lips | lips | 208 | d | high |
| §21 Now, I hold, either that there is no use | I holds either | I hold, either | hold, either | 210 | d/comma | high |
| §26 reinstates us in his Father’s favour | his Fathered favour | his Father’s favour | Father’s | 216 | d | high |
| §26 He, I say, takes them away | I say, took them | I say, takes them | takes | 216 | d | high |
| §27 Isaiah says that the Father hath laid on him | the Farther “has | the Father “hath | Father | 217 | d | high |
| §29 they are ever and anon telling us | telling as to | telling us to | us | 219 | d | high |
| §30 he calls it ἀπολύτρωσις | calls it ἀπολύτροσις, | calls it ἀπολύτρωσις, | ἀπολύτρωσις | 221 | e | high |
| §30 estimated by their antitype | anti type | antitype | antitype | 222 | d | high |
| §32 Pour out thy fury upon the heathen | thy furry | thy fury | fury | 224 | d | high |
| §32 though thou wast angry with me | thou west angry | thou wast angry | wast | 225 | d | high |
| §32 he denotes moderation and lenity | moderation and levity | moderation and lenity | lenity | 225 | d | high |
| §32 How much regard he has to this lenity | to this levity | to this lenity | lenity | 225 | d | high |
| §32 struck with fear and dread, betake themselves | dread, retake | dread, betake | betake | 226 | d | high |
| §33 when he rejected Saul from the kingdom | the kingdoms he | the kingdom, he | kingdom, he | 227 | d/comma | high |
| §33 the just severity which he has been compelled to use | compelled to us, | compelled to use | use | 228 | d | high |
| §35 Son, be of good cheer; thy sins | thy sina be | thy sins be | sins | 230 | d | high |
| §36 any other ἀπολύτρωσις (ransom) | other ἀπολύτροσις (#emph | other ἀπολύτρωσις (ransom) | ἀπολύτρωσις | 230 | e | high |
| note: The first definition is that of Gregory | Vera Pœitentia | Vera Pœnitentia | Pœnitentia | 185 | e | high |
| note: Latin, “Secundam tabulam post naufragium” | en lar mer | en la mer | la | 187 | n | high |
| note: Latin, “De asini umbra rixam” | De saini umbra | De asini umbra | asini | 187 | e | high |
| note: Mt. 11:28; Is. 61:1; Luke 4:18 | Is. 59:1 | Is. lxi. 1 | Is. 61:1 | 189 | f | high |
| note: Eccles. Hist. ... et Trepont. Hist. Lib. ix. | Lib. 7 cap. 17 | Lib. viii. cap. 17 | Lib. 8 cap. 17 if following 1845; Sozomen tells the story in book 7 (ch. 16), so CCEL's 7 may be a correction: check | 194 | f | low |
| note: The French is, “Mais comme les nautonniers | un perlin | un pelerin | pelerin | 205 | n | high |
| note: See Lombard, Sent. Lib. 4 Dist 10 | Non suffcit | Non sufficit | sufficit | 214 | e | high |
| note: Isa. 52:3; Rom. 5:8 | Isa. 3:3 | Isa. lii. 3 | Isa. 52:3 | 215 | f | high |
| note: French, “Et quand ils voudront satisfaire | I’m still | I am still | I am | 219 | n | high |
| note: Isa. 38:17; 44:22; Micah 7:19; Ps. 32:1 | Isa 38:17; Isa44:22; Micah 7:19; PS 32:1&gt;Ps. 32:1 | Isa. xxxviii. 17; xliv. 22; Micah vii. 19; Ps. xxxii. 1. | Isa. 38:17; 44:22; Micah 7:19; Ps. 32:1. (CCEL's note is garbled: “&gt;” and the reference doubled) | 220 | n | high |
| note: Rom. 3:24; 1 Cor. 1:30; Eph. 1:7; Col. 1:14; 1 Tim. 2:6 | Col. 1:14; Tim 2:6 | Col. i. 14; 1 Tim. ii. 6. | Col. 1:14; 1 Tim. 2:6. | 221 | f | high |
| note: For a full exposition of these passages | expositon | exposition | exposition | 223 | n | high |
| note: French, “Integrité, pitié, droiture” | intregrity | integrity | integrity | 231 | n | high |

## Book III, chapter 05 — `book-3-chapter-05.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary: Passages of Scripture quoted in support of purgatory | Impardonable | unpardonable | unpardonable | 235 | d | high |
| §1 a considerable portion of the world have begun to bethink | begun to rethink | begun to bethink | bethink | 237 | d | high |
| §3 that through him we might, without good desert | we mighty without | we might, without | might, without | 239 | d/comma | high |
| §4 all believers, behove to be exercised | believers, behave | believers, behove | behove | 240 | d | high |
| §4 Paul means not for the redemption, or reconciliation | the redemptions or reconciliations or | the redemption, or reconciliation, or | redemption, or reconciliation, or | 240 | d/comma | high |
| §4 Therefore, O hearer, whoever you be | Therefore O hearers | Therefore, O hearer, | hearer, | 240 | d/comma | high |
| §5 what is meant by the fellowship | fellowship (κοινονία) | fellowship (κοινωνία) | κοινωνία | 241 | e | high |
| §7 to cut off all hope of pardon from this flagitious wickedness | flagitous | flagitious | flagitious | 243 | d | high |
| §7 till thou hast paid the uttermost farthing | uttermost earthing | uttermost farthing | farthing | 244 | d | high |
| §8 the history of the Maccabees | (1 Macc. 12:43) | (1 Maccab. xii. 43,) | (2 Macc. 12:43) (1845 has the same misprint) | 245 | f | high |
| §10 death is not destruction, but a passage | but a passages | but a passage | passage | 249 | d | high |
| §10 His book, De Cura pro Mortuis Agenda | Mortals | Mortuis | Mortuis | 249 | e | high |
| note: French, “Il est expedient de monstrer ici | indul grences | indulgences | indulgences | 237 | n | high |
| note: French, “L’Escriture raconte souventesfois | ayent prié plour | ayent prié pour | pour | 248 | n | high |
| note: French, “Le liure qu’il a composé | qu’il à composé | qu’il a composé | a | 250 | n | high |
| note: French, “Le liure qu’il a composé | intitule. Du | intitule, Du | intitule, Du | 250 | n | high |
| note: French, “Le liure qu’il a composé | chose o˜ il | chose où il | où | 250 | n | high |
| note: The French of the latter clause | couleur pour jamais | couleur pour s’excuser, qu’ils ne soyent conveincus d’etre les plus vilains trompeurs qui furent jamais | couleur pour s’excuser, qu’ils ne soyent conveincus d’etre les plus vilains trompeurs qui furent jamais | 251 | b | high |
| note: The French of the latter clause (translation) | seeing that they have no colour | seeing they have no colour | seeing they | 251 | c | medium |
| note: The French of the latter clause (translation) | decivers | deceivers | deceivers | 251 | n | high |

## Book III, chapter 06 — `book-3-chapter-06.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 a true account of this reformation | this reformations lest | this reformation, lest | reformation, lest | 253 | d/comma | high |
| §2 we must inhabit the holy city Jerusalem | (Isaiah rev. 8 | (Isaiah xxxv. 8 | (Isaiah 35:8 | 255 | f | high |
| note: The passage in brackets is omitted | ommited | omitted | omitted | 254 | n | high |
| note: Mal. 1:6; Eph. 5:1 ... | 1Cor. 3:16, 5:17 | 1 Cor. iii. 16; vi. 17 | 1 Cor. 3:16; 6:17 | 255 | f | high |

## Book III, chapter 07 — `book-3-chapter-07.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 Righteousness comprehends all the duties of equity | in every one his due | in rendering to every one his due | in rendering to every one | 263 | b | high |
| §4 sincerely labour to promote their advantage | promote their advantages ( | promote their advantage, ( | advantage ( | 263 | d/comma | high |
| §5 spontaneously to yield our own right | own rights and | own right, and | right, and | 265 | d/comma | high |
| §6 Charity suffereth long | suffiereth | suffereth | suffereth | 267 | d | high |
| §9 In short, he who leans on the divine blessing | In shorts he | In short, he | short, he | 270 | d/comma | high |

## Book III, chapter 08 — `book-3-chapter-08.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 how necessary it is for us to bear the cross | for usto bear | for us to bear | us to | 276 | d | high |
| §4 should be applied to use, by being made sure | applied to uses by | applied to use, by | use, by | 277 | d/comma | high |
| §11 a cheerful and gladdened breast | gladdened breasts and | gladdened breast, and | breast, and | 284 | d/comma | high |

## Book III, chapter 09 — `book-3-chapter-09.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Hence our stupidity; our minds being so dazzled | minds being dazzled | minds being so dazzled | being so dazzled | 286 | b | high |
| §4 in obedience to the command of God | command of Gods he | command of God, he | God, he | 290 | d/comma | high |
| note: Latin, “Animal esse ἐφήμερον” | Animal esseεφἡμερον; | Animal esse ἐφήμερον; | esse ἐφήμερον (space; smooth breathing on the epsilon, accent on the eta) | 287 | e | high |
| note: French, “Or pource que la vie presente” (translation) | delights to attracts | delights to attract us | attract us | 287 | d | high |

## Book III, chapter 10 — `book-3-chapter-10.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 is by no means to be neglected | by no mean to | by no means to | means | 293 | d | high |
| §1 general rules for the legitimate use | legitimate uses we | legitimate use, we | use, we | 294 | d/comma | high |
| §3 boiling forth in lust through excessive indulgence | excessive indulgences infects | excessive indulgence, infects | indulgence, infects | 296 | d/comma | high |
| §4 pride, excessive show, and austerity | excessive shows and | excessive show, and | show, and | 296 | d/comma | high |
| §4 it must be his constant aim | constant aims not | constant aim, not | aim, not | 297 | d/comma | high |


## Findings as JSON lines

```json
{"file": "book-3-chapter-01.typ", "anchor": "§2 But in order to have a clearer view", "ccel": "important subjects we", "1845": "important subject, we", "proposed": "subject, we", "page": 87, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-01.typ", "anchor": "§3 so as to become our Father", "ccel": "become our Fathers and", "1845": "become our Father, and", "proposed": "Father, and", "page": 88, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-01.typ", "anchor": "§3 boldness of access to him", "ccel": "to him; nays he", "1845": "to him; nay, he", "proposed": "nay, he", "page": 88, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-01.typ", "anchor": "note: Rom. 8:15; 2 Cor. 1:22 (titles of the Spirit)", "ccel": "John 2:14;", "1845": "John ii. 14", "proposed": "John 4:14 (the fountain of water springing up; 1845 has the same misprint)", "page": 89, "kind": "f", "confidence": "medium"}
{"file": "book-3-chapter-01.typ", "anchor": "note: Rom. 8:15; 2 Cor. 1:22 (titles of the Spirit)", "ccel": "John 7:37;", "1845": "John viii. 37", "proposed": "keep John 7:37 (CCEL corrects 1845's misprint)", "page": 89, "kind": "info", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "Sections 17", "ccel": "opposite example of Ahab.", "1845": "opposite example of Ahaz.", "proposed": "Ahaz", "page": 93, "kind": "d", "confidence": "high (verified)"}
{"file": "book-3-chapter-02.typ", "anchor": "Sections 19", "ccel": "Conformation from", "1845": "Confirmation from", "proposed": "Confirmation", "page": 93, "kind": "d", "confidence": "high (verified)"}
{"file": "book-3-chapter-02.typ", "anchor": "§5 the Samaritans who believed", "ccel": "who believed the women", "1845": "who believed the woman", "proposed": "woman", "page": 100, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§6 unless you feel firmly persuaded", "ccel": "every word which him", "1845": "every word which proceeds from him", "proposed": "which proceeds from him", "page": 102, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§9 impugn, reject, or", "ccel": "reject, or condemn", "1845": "reject, or contemn", "proposed": "contemn", "page": 107, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§12 they deprecate his anger", "ccel": "they retake themselves", "1845": "they betake themselves", "proposed": "betake", "page": 110, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§12 Every plant which my heavenly Father", "ccel": "(Mt. 16:13)", "1845": "(Matth. xvi. 13.)", "proposed": "(Mt. 15:13) (1845 has the same misprint)", "page": 111, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§15 feeling of full assurance", "ccel": "assurance (πλεροφορία)", "1845": "assurance (πληροφορία)", "proposed": "πληροφορία", "page": 114, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§17 How did Ahaz act?", "ccel": "How did Ahab act?", "1845": "How did Ahaz act?", "proposed": "Ahaz", "page": 117, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§17 Take not the word of truth", "ccel": "my mouths”", "1845": "my mouth,”", "proposed": "mouth,”", "page": 118, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§18 rising up to assail the faith", "ccel": "faith enlisting in", "1845": "faith existing in", "proposed": "existing", "page": 118, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§20 faith is imperfect so long as we groan", "ccel": "under a height of", "1845": "under a weight of", "proposed": "weight", "page": 119, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§22 not excluded from the covenant", "ccel": "covenant of adoptions so", "1845": "covenant of adoption, so", "proposed": "adoption, so", "page": 123, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§23 worship toward thy holy temple", "ccel": "holy temples”", "1845": "holy temple,”", "proposed": "temple,”", "page": 123, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§25 man doubtless has been made subject to vanity", "ccel": "man here been", "1845": "man has been", "proposed": "has", "page": 126, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§27 Mere threatenings", "ccel": "mere threatening have", "1845": "mere threatenings have", "proposed": "threatenings", "page": 128, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§29 give heed to his threatenings", "ccel": "to his threatening;", "1845": "to his threatenings;", "proposed": "threatenings", "page": 130, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§9 moved to some degree by its threatenings", "ccel": "its threatening and", "1845": "its threatenings and", "proposed": "threatenings", "page": 106, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§30 Noah ... feared the destruction of the world", "ccel": "(Heb. 11:17)", "1845": "(Heb. xi. 17.)", "proposed": "(Heb. 11:7) (1845 has the same misprint)", "page": 130, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§30 a work of faith, threatenings ought", "ccel": "faith, threatening ought", "1845": "faith, threatenings ought", "proposed": "threatenings", "page": 131, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§30 unless in so far as it ingrafts us", "ccel": "in grafts us", "1845": "ingrafts us", "proposed": "ingrafts", "page": 131, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§32 Hence, with good reason", "ccel": "with good reasons Paul", "1845": "with good reason, Paul", "proposed": "reason, Paul", "page": 135, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§33 beholding divine mysteries", "ccel": "divine masteries", "1845": "divine mysteries", "proposed": "mysteries", "page": 137, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§40 an approach to arrogance", "ccel": "arrogance in each glorying", "1845": "arrogance in such glorying", "proposed": "such", "page": 144, "kind": "d", "confidence": "high (verified)"}
{"file": "book-3-chapter-02.typ", "anchor": "§41 For as Paul says (Rom. 8:24)", "ccel": "“A hope that is seen", "1845": "“hope that is seen", "proposed": "“hope that is seen", "page": 144, "kind": "c", "confidence": "high (verified)"}
{"file": "book-3-chapter-02.typ", "anchor": "§41 the Greek term being", "ccel": "being ἔλενγχος,", "1845": "being ἔλεγχος,", "proposed": "ἔλεγχος", "page": 144, "kind": "e", "confidence": "high (verified)"}
{"file": "book-3-chapter-02.typ", "anchor": "§43 ready to be revealed in the last time", "ccel": "the last times”", "1845": "the last time,”", "proposed": "time,”", "page": 147, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§43 as in the same Epistle", "ccel": "the same Epistles “", "1845": "the same Epistle, “", "proposed": "Epistle, “", "page": 147, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "note: The French is, “Car nous tendons", "ccel": "The French is“Car", "1845": "The French is, “Car", "proposed": "is, “Car", "page": 97, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "note: As to the imperfection, strengthening", "ccel": "Book 4. chap. 4 sec", "1845": "Book IV. chap. xiv. sec", "proposed": "Book 4. chap. 14 sec", "page": 116, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "note: See Calv. adv. Pighium", "ccel": "Pighiium", "1845": "Pighium", "proposed": "Pighium", "page": 117, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "note: Latin, “Præsentim ubi ad rem", "ccel": "Latin“Præsentim", "1845": "Latin, “Præsentim", "proposed": "Latin, “Præsentim", "page": 114, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "note: Latin, “Præsentim ubi ad rem", "ccel": "Principalament", "1845": "Principalement", "proposed": "Principalement", "page": 114, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "note: Latin, “acsi cervicibus suis", "ccel": "engulfthem", "1845": "engulf them", "proposed": "engulf them", "page": 128, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "note: The French adds, “En quoy ils demonstrent", "ccel": "leur betisc", "1845": "leur betise", "proposed": "betise", "page": 142, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "Sections 2", "ccel": "Conformation from", "1845": "Confirmation from", "proposed": "Confirmation", "page": 150, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§1 no man can embrace the grace of the Gospel", "ccel": "without retaking himself", "1845": "without betaking himself", "proposed": "betaking", "page": 152, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§3 Certain learned men, who lived long before", "ccel": "the present days and", "1845": "the present day, and", "proposed": "day, and", "page": 153, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§5 with true repentance, betake themselves", "ccel": "repentance, retake themselves", "1845": "repentance, betake themselves", "proposed": "betake", "page": 156, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§6 And to make the deeper impression", "ccel": "And to malice the", "1845": "And to make the", "proposed": "make", "page": 157, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§7 The stern threatenings which God employs", "ccel": "stern threatening which", "1845": "stern threatenings which", "proposed": "threatenings", "page": 158, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§8 instilling his holiness into our souls", "ccel": "so inspired them", "1845": "so inspires them", "proposed": "inspires", "page": 159, "kind": "d", "confidence": "high (verified)"}
{"file": "book-3-chapter-03.typ", "anchor": "§9 Be renewed in the spirit of your mind", "ccel": "of your minds”", "1845": "of your mind,”", "proposed": "mind,”", "page": 160, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§10 the very pravity which begets", "ccel": "very gravity which", "1845": "very pravity which", "proposed": "pravity", "page": 161, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§10 Augustine himself does not always refrain", "ccel": "himself dose not", "1845": "himself does not", "proposed": "does", "page": 161, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§14 daily struggling with the evil", "ccel": "entangled. Hence, too", "1845": "entangled. Whence, too", "proposed": "Whence", "page": 166, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§15 The Apostle, in his description of repentance", "ccel": "description of repentance (", "1845": "description of repentance, (2 Cor. vii. 2,)", "proposed": "(2 Cor. 7:11) (1845 has the same misprint, 7:2; the seven fruits are in 7:11)", "page": 166, "kind": "f", "confidence": "high (verified)"}
{"file": "book-3-chapter-03.typ", "anchor": "§17 rend your heart ... The fasting", "ccel": "The “fastings”", "1845": "The “fasting,”", "proposed": "“fasting,”", "page": 169, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§19 repent ye, and believe the Gospel", "ccel": "(Mark 1:10)", "1845": "(Mark i. 15.)", "proposed": "(Mark 1:15)", "page": 173, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§19 a brief summary of the whole Gospel", "ccel": "he behaved “to", "1845": "he behoved “to", "proposed": "behoved", "page": 173, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§21 If God peradventure will give them repentance", "ccel": "God per adventure", "1845": "God peradventure", "proposed": "peradventure", "page": 175, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§22 they defamed him by the name of Beelzebub", "ccel": "(Mt. 9:3, 4; 12:24)", "1845": "(Matth. ix. 3, 4; xii. 24.)", "proposed": "(Mt. 9:34; 12:24) (1845 has the same misprint)", "page": 178, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§24 deny forgiveness to any who betake themselves", "ccel": "any who retake themselves", "1845": "any who betake themselves", "proposed": "betake", "page": 179, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§25 disregard the divine threatenings", "ccel": "divine threatening.", "1845": "divine threatenings.", "proposed": "threatenings", "page": 181, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "note: Latin, “Initialis timor”", "ccel": "une erainte", "1845": "une crainte", "proposed": "crainte", "page": 153, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "note: Latin, “Initialis timor”", "ccel": "par arison", "1845": "par raison", "proposed": "raison", "page": 153, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "note: 2 Kings 20:2; Isa. ...", "ccel": "Isa. 37:2", "1845": "Isa. xxxviii. 2", "proposed": "Isa. 38:2", "page": 155, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "note: Latin, “Reatus.”", "ccel": "Reatus.”—the", "1845": "Reatus.”—French, “l’imputation du peché;”—the", "proposed": "Reatus.”—French, “l’imputation du peché;”—the", "page": 162, "kind": "b", "confidence": "high (verified)"}
{"file": "book-3-chapter-03.typ", "anchor": "note: French, “Circonstances qui convenoyent", "ccel": "specialement alore", "1845": "specialement alors", "proposed": "alors", "page": 170, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "note: French, “Fust la coustume de ce temps-la", "ccel": "aujourduhui", "1845": "aujourdhui", "proposed": "aujourdhui", "page": 170, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "note: Isaiah 56:1; 59:20", "ccel": "Isiah 56", "1845": "Isaiah lvi.", "proposed": "Isaiah 56", "page": 174, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "note: The French adds, “Et ce non seulement", "ccel": "jour. mais", "1845": "jour, mais", "proposed": "jour, mais", "page": 175, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "note: The Greek is", "ccel": "Greek is “του̑", "1845": "Greek is, “τοῦ", "proposed": "τοῦ (CCEL has υ with a combining inverted breve, U+0311, for the circumflex)", "page": 177, "kind": "e", "confidence": "high (verified)"}
{"file": "book-3-chapter-03.typ", "anchor": "note: The Greek is", "ccel": "blasphemiæ,”,", "1845": "blasphemiæ,”", "proposed": "blasphemiæ,”", "page": 177, "kind": "n", "confidence": "high (verified)"}
{"file": "book-3-chapter-04.typ", "anchor": "§1 This I will do as briefly as possible", "ccel": "for I leave no", "1845": "for I have no", "proposed": "have", "page": 185, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§1 to bewail past evils", "ccel": "and not to sin to do", "1845": "and not again to do", "proposed": "again", "page": 185, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§1 miserably entangle themselves", "ccel": "they are pealing", "1845": "they are prating", "proposed": "prating", "page": 187, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§1 whether punishments divinely inflicted", "ccel": "divinely indicted", "1845": "divinely inflicted", "proposed": "inflicted", "page": 187, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§4 Adam having replied as if excepting", "ccel": "“The women whom", "1845": "“The woman whom", "proposed": "woman", "page": 189, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§4 in order that, in the judgment of God", "ccel": "judgment of Gods they", "1845": "judgment of God, they", "proposed": "God, they", "page": 191, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§4 they might be more fully convicted", "ccel": "more filly convicted", "1845": "more fully convicted", "proposed": "fully", "page": 191, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§5 see him rise by the mere power of a word", "ccel": "handle hint", "1845": "handle him", "proposed": "him", "page": 191, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§6 He says, ἀλλήλους", "ccel": "He says, “allelous”", "1845": "He says, ἀλλήλους,", "proposed": "He says, ἀλλήλους (CCEL transliterates the Greek)", "page": 192, "kind": "e", "confidence": "high (verified)"}
{"file": "book-3-chapter-04.typ", "anchor": "§7 the decree of the Council of Lateran", "ccel": "Council of Lateral", "1845": "Council of Lateran", "proposed": "Lateran", "page": 193, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§7 let them charge with defection", "ccel": "charge with defections not", "1845": "charge with defection, not", "proposed": "defection, not", "page": 195, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§9 those only which contain a summary", "ccel": "which contain summary", "1845": "which contain a summary", "proposed": "contain a summary", "page": 196, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§9 He is the discerner of the heart", "ccel": "knows all one thoughts", "1845": "knows all our thoughts", "proposed": "our", "page": 196, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§9 Another specimen of David’s confession", "ccel": "David’s confessions", "1845": "David’s confession", "proposed": "confession", "page": 196, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§11 if it is our duty to betake ourselves", "ccel": "duty to retake", "1845": "duty to betake", "proposed": "betake", "page": 198, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§12 to assure our consciences of the forgiveness of sins", "ccel": "forgiveness of fins", "1845": "forgiveness of sins", "proposed": "sins", "page": 199, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§14 invested with the mandate of reconciliation", "ccel": "mandate of reconciliations by", "1845": "mandate of reconciliation, by", "proposed": "reconciliation, by", "page": 201, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§14 nevertheless remains somewhat in doubt", "ccel": "somewhat in doubts,", "1845": "somewhat in doubt,", "proposed": "doubt,", "page": 201, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§14 But when we treat of the keys, we", "ccel": "keys, us must", "1845": "keys, we must", "proposed": "we", "page": 202, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§15 the conferring of the keys must be taken with limitation", "ccel": "taken with limitations because", "1845": "taken with limitation, because", "proposed": "limitation, because", "page": 203, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§17 First, they betook themselves to calculation", "ccel": "they retook", "1845": "they betook", "proposed": "betook", "page": 204, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§18 hence its only result is to destroy", "ccel": "only results to", "1845": "only result is to", "proposed": "result is", "page": 205, "kind": "d", "confidence": "high (verified)"}
{"file": "book-3-chapter-04.typ", "anchor": "§19 they can wipe their lips", "ccel": "wipe their lip,", "1845": "wipe their lips", "proposed": "lips", "page": 208, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§21 Now, I hold, either that there is no use", "ccel": "I holds either", "1845": "I hold, either", "proposed": "hold, either", "page": 210, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§26 reinstates us in his Father’s favour", "ccel": "his Fathered favour", "1845": "his Father’s favour", "proposed": "Father’s", "page": 216, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§26 He, I say, takes them away", "ccel": "I say, took them", "1845": "I say, takes them", "proposed": "takes", "page": 216, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§27 Isaiah says that the Father hath laid on him", "ccel": "the Farther “has", "1845": "the Father “hath", "proposed": "Father", "page": 217, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§29 they are ever and anon telling us", "ccel": "telling as to", "1845": "telling us to", "proposed": "us", "page": 219, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§30 he calls it ἀπολύτρωσις", "ccel": "calls it ἀπολύτροσις,", "1845": "calls it ἀπολύτρωσις,", "proposed": "ἀπολύτρωσις", "page": 221, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§30 estimated by their antitype", "ccel": "anti type", "1845": "antitype", "proposed": "antitype", "page": 222, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§32 Pour out thy fury upon the heathen", "ccel": "thy furry", "1845": "thy fury", "proposed": "fury", "page": 224, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§32 though thou wast angry with me", "ccel": "thou west angry", "1845": "thou wast angry", "proposed": "wast", "page": 225, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§32 he denotes moderation and lenity", "ccel": "moderation and levity", "1845": "moderation and lenity", "proposed": "lenity", "page": 225, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§32 How much regard he has to this lenity", "ccel": "to this levity", "1845": "to this lenity", "proposed": "lenity", "page": 225, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§32 struck with fear and dread, betake themselves", "ccel": "dread, retake", "1845": "dread, betake", "proposed": "betake", "page": 226, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§33 when he rejected Saul from the kingdom", "ccel": "the kingdoms he", "1845": "the kingdom, he", "proposed": "kingdom, he", "page": 227, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§33 the just severity which he has been compelled to use", "ccel": "compelled to us,", "1845": "compelled to use", "proposed": "use", "page": 228, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§35 Son, be of good cheer; thy sins", "ccel": "thy sina be", "1845": "thy sins be", "proposed": "sins", "page": 230, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§36 any other ἀπολύτρωσις (ransom)", "ccel": "other ἀπολύτροσις (#emph", "1845": "other ἀπολύτρωσις (ransom)", "proposed": "ἀπολύτρωσις", "page": 230, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: The first definition is that of Gregory", "ccel": "Vera Pœitentia", "1845": "Vera Pœnitentia", "proposed": "Pœnitentia", "page": 185, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Latin, “Secundam tabulam post naufragium”", "ccel": "en lar mer", "1845": "en la mer", "proposed": "la", "page": 187, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Latin, “De asini umbra rixam”", "ccel": "De saini umbra", "1845": "De asini umbra", "proposed": "asini", "page": 187, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Mt. 11:28; Is. 61:1; Luke 4:18", "ccel": "Is. 59:1", "1845": "Is. lxi. 1", "proposed": "Is. 61:1", "page": 189, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Eccles. Hist. ... et Trepont. Hist. Lib. ix.", "ccel": "Lib. 7 cap. 17", "1845": "Lib. viii. cap. 17", "proposed": "Lib. 8 cap. 17 if following 1845; Sozomen tells the story in book 7 (ch. 16), so CCEL's 7 may be a correction: check", "page": 194, "kind": "f", "confidence": "low"}
{"file": "book-3-chapter-04.typ", "anchor": "note: The French is, “Mais comme les nautonniers", "ccel": "un perlin", "1845": "un pelerin", "proposed": "pelerin", "page": 205, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: See Lombard, Sent. Lib. 4 Dist 10", "ccel": "Non suffcit", "1845": "Non sufficit", "proposed": "sufficit", "page": 214, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Isa. 52:3; Rom. 5:8", "ccel": "Isa. 3:3", "1845": "Isa. lii. 3", "proposed": "Isa. 52:3", "page": 215, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: French, “Et quand ils voudront satisfaire", "ccel": "I’m still", "1845": "I am still", "proposed": "I am", "page": 219, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Isa. 38:17; 44:22; Micah 7:19; Ps. 32:1", "ccel": "Isa 38:17; Isa44:22; Micah 7:19; PS 32:1&gt;Ps. 32:1", "1845": "Isa. xxxviii. 17; xliv. 22; Micah vii. 19; Ps. xxxii. 1.", "proposed": "Isa. 38:17; 44:22; Micah 7:19; Ps. 32:1. (CCEL's note is garbled: “&gt;” and the reference doubled)", "page": 220, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Rom. 3:24; 1 Cor. 1:30; Eph. 1:7; Col. 1:14; 1 Tim. 2:6", "ccel": "Col. 1:14; Tim 2:6", "1845": "Col. i. 14; 1 Tim. ii. 6.", "proposed": "Col. 1:14; 1 Tim. 2:6.", "page": 221, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: For a full exposition of these passages", "ccel": "expositon", "1845": "exposition", "proposed": "exposition", "page": 223, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: French, “Integrité, pitié, droiture”", "ccel": "intregrity", "1845": "integrity", "proposed": "integrity", "page": 231, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "summary: Passages of Scripture quoted in support of purgatory", "ccel": "Impardonable", "1845": "unpardonable", "proposed": "unpardonable", "page": 235, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§1 a considerable portion of the world have begun to bethink", "ccel": "begun to rethink", "1845": "begun to bethink", "proposed": "bethink", "page": 237, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§3 that through him we might, without good desert", "ccel": "we mighty without", "1845": "we might, without", "proposed": "might, without", "page": 239, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§4 all believers, behove to be exercised", "ccel": "believers, behave", "1845": "believers, behove", "proposed": "behove", "page": 240, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§4 Paul means not for the redemption, or reconciliation", "ccel": "the redemptions or reconciliations or", "1845": "the redemption, or reconciliation, or", "proposed": "redemption, or reconciliation, or", "page": 240, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§4 Therefore, O hearer, whoever you be", "ccel": "Therefore O hearers", "1845": "Therefore, O hearer,", "proposed": "hearer,", "page": 240, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§5 what is meant by the fellowship", "ccel": "fellowship (κοινονία)", "1845": "fellowship (κοινωνία)", "proposed": "κοινωνία", "page": 241, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§7 to cut off all hope of pardon from this flagitious wickedness", "ccel": "flagitous", "1845": "flagitious", "proposed": "flagitious", "page": 243, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§7 till thou hast paid the uttermost farthing", "ccel": "uttermost earthing", "1845": "uttermost farthing", "proposed": "farthing", "page": 244, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§8 the history of the Maccabees", "ccel": "(1 Macc. 12:43)", "1845": "(1 Maccab. xii. 43,)", "proposed": "(2 Macc. 12:43) (1845 has the same misprint)", "page": 245, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§10 death is not destruction, but a passage", "ccel": "but a passages", "1845": "but a passage", "proposed": "passage", "page": 249, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§10 His book, De Cura pro Mortuis Agenda", "ccel": "Mortals", "1845": "Mortuis", "proposed": "Mortuis", "page": 249, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "note: French, “Il est expedient de monstrer ici", "ccel": "indul grences", "1845": "indulgences", "proposed": "indulgences", "page": 237, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "note: French, “L’Escriture raconte souventesfois", "ccel": "ayent prié plour", "1845": "ayent prié pour", "proposed": "pour", "page": 248, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "note: French, “Le liure qu’il a composé", "ccel": "qu’il à composé", "1845": "qu’il a composé", "proposed": "a", "page": 250, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "note: French, “Le liure qu’il a composé", "ccel": "intitule. Du", "1845": "intitule, Du", "proposed": "intitule, Du", "page": 250, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "note: French, “Le liure qu’il a composé", "ccel": "chose o˜ il", "1845": "chose où il", "proposed": "où", "page": 250, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "note: The French of the latter clause", "ccel": "couleur pour jamais", "1845": "couleur pour s’excuser, qu’ils ne soyent conveincus d’etre les plus vilains trompeurs qui furent jamais", "proposed": "couleur pour s’excuser, qu’ils ne soyent conveincus d’etre les plus vilains trompeurs qui furent jamais", "page": 251, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "note: The French of the latter clause (translation)", "ccel": "seeing that they have no colour", "1845": "seeing they have no colour", "proposed": "seeing they", "page": 251, "kind": "c", "confidence": "medium"}
{"file": "book-3-chapter-05.typ", "anchor": "note: The French of the latter clause (translation)", "ccel": "decivers", "1845": "deceivers", "proposed": "deceivers", "page": 251, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-06.typ", "anchor": "§1 a true account of this reformation", "ccel": "this reformations lest", "1845": "this reformation, lest", "proposed": "reformation, lest", "page": 253, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-06.typ", "anchor": "§2 we must inhabit the holy city Jerusalem", "ccel": "(Isaiah rev. 8", "1845": "(Isaiah xxxv. 8", "proposed": "(Isaiah 35:8", "page": 255, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-06.typ", "anchor": "note: The passage in brackets is omitted", "ccel": "ommited", "1845": "omitted", "proposed": "omitted", "page": 254, "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-06.typ", "anchor": "note: Mal. 1:6; Eph. 5:1 ...", "ccel": "1Cor. 3:16, 5:17", "1845": "1 Cor. iii. 16; vi. 17", "proposed": "1 Cor. 3:16; 6:17", "page": 255, "kind": "f", "confidence": "high"}
{"file": "book-3-chapter-07.typ", "anchor": "§3 Righteousness comprehends all the duties of equity", "ccel": "in every one his due", "1845": "in rendering to every one his due", "proposed": "in rendering to every one", "page": 263, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-07.typ", "anchor": "§4 sincerely labour to promote their advantage", "ccel": "promote their advantages (", "1845": "promote their advantage, (", "proposed": "advantage (", "page": 263, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-07.typ", "anchor": "§5 spontaneously to yield our own right", "ccel": "own rights and", "1845": "own right, and", "proposed": "right, and", "page": 265, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-07.typ", "anchor": "§6 Charity suffereth long", "ccel": "suffiereth", "1845": "suffereth", "proposed": "suffereth", "page": 267, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-07.typ", "anchor": "§9 In short, he who leans on the divine blessing", "ccel": "In shorts he", "1845": "In short, he", "proposed": "short, he", "page": 270, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-08.typ", "anchor": "§3 how necessary it is for us to bear the cross", "ccel": "for usto bear", "1845": "for us to bear", "proposed": "us to", "page": 276, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-08.typ", "anchor": "§4 should be applied to use, by being made sure", "ccel": "applied to uses by", "1845": "applied to use, by", "proposed": "use, by", "page": 277, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-08.typ", "anchor": "§11 a cheerful and gladdened breast", "ccel": "gladdened breasts and", "1845": "gladdened breast, and", "proposed": "breast, and", "page": 284, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-09.typ", "anchor": "§1 Hence our stupidity; our minds being so dazzled", "ccel": "minds being dazzled", "1845": "minds being so dazzled", "proposed": "being so dazzled", "page": 286, "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-09.typ", "anchor": "§4 in obedience to the command of God", "ccel": "command of Gods he", "1845": "command of God, he", "proposed": "God, he", "page": 290, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-09.typ", "anchor": "note: Latin, “Animal esse ἐφήμερον”", "ccel": "Animal esseεφἡμερον;", "1845": "Animal esse ἐφήμερον;", "proposed": "esse ἐφήμερον (space; smooth breathing on the epsilon, accent on the eta)", "page": 287, "kind": "e", "confidence": "high"}
{"file": "book-3-chapter-09.typ", "anchor": "note: French, “Or pource que la vie presente” (translation)", "ccel": "delights to attracts", "1845": "delights to attract us", "proposed": "attract us", "page": 287, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-10.typ", "anchor": "§1 is by no means to be neglected", "ccel": "by no mean to", "1845": "by no means to", "proposed": "means", "page": 293, "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-10.typ", "anchor": "§1 general rules for the legitimate use", "ccel": "legitimate uses we", "1845": "legitimate use, we", "proposed": "use, we", "page": 294, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-10.typ", "anchor": "§3 boiling forth in lust through excessive indulgence", "ccel": "excessive indulgences infects", "1845": "excessive indulgence, infects", "proposed": "indulgence, infects", "page": 296, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-10.typ", "anchor": "§4 pride, excessive show, and austerity", "ccel": "excessive shows and", "1845": "excessive show, and", "proposed": "show, and", "page": 296, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-10.typ", "anchor": "§4 it must be his constant aim", "ccel": "constant aims not", "1845": "constant aim, not", "proposed": "aim, not", "page": 297, "kind": "d/comma", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "Sections 21", "ccel": "he retakes himself", "1845": "he betakes himself", "proposed": "betakes", "page": 93, "kind": "d", "confidence": "high (verified)"}
{"file": "book-3-chapter-02.typ", "anchor": "§21 whenever the sinner betakes himself", "ccel": "sinner retakes himself", "1845": "sinner betakes himself", "proposed": "betakes", "page": 120, "kind": "d", "confidence": "high"}
```
