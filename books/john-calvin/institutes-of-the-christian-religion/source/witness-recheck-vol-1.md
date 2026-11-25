# Calvin, Institutes, vol. 1 (prefaces + Book I): Classic re-checked against the 1845 printing (Kraken OCR)

Base: `chapters/typ/vol-1/*.typ` in the `wt-institutes` worktree (after the October witness check and its 156 fixes).
Witness: Calvin Translation Society, Edinburgh 1845, vol. 1, our own scans: Kraken OCR (`work/institutes/kraken/p-NNNN.txt`,
ALTO beside it), Tesseract as a second reading, page images `work/institutes/pages/p-NNNN.png` (image = printed page + 124).
Method: every .typ file of vol-1 was aligned word by word with the Kraken text of pp. 1–278 (difflib; main text first, then the
footnotes against the OCR words the main text left over; running heads dropped; line-end hyphens joined). Differences were
filtered for reference style (Roman → Arabic numbers compared as numbers), American spelling and OCR noise, then every
remaining candidate was read on the page image (line crops from the ALTO boxes). Only what the image confirms is listed.
Scripts and raw candidates: `work/institutes/latin/vol1/recheck/` (`align.py`, `filter.py`, `crop.py`, `cand2.tsv`,
`cases.tsv`, `residual.txt`, `build_report.py`).

**Rule applied (editor, 2026-11-23):** the Classic follows the 1845 print wherever CCEL's wording departs from it. So CCEL's
modernised grammar in Scripture quotations (has/does/goes for hath/doth/goeth) is now listed, kind **d/grammar**. Not listed:
Arabic reference style, American spelling (honor, Savior, stupefy, steadfast, meager, forbade, gainsaid…), CCEL's
punctuation around references, CCEL's word joins (everything, inasmuch, meantime), Greek accents (done in October).

**Kinds:** b (1845 words missing in CCEL), d (a different word), d/comma (comma keyed as a final “s”), d/grammar
(CCEL's modernised verb form), d/case (capital letter differs from the print), f (reference numbers), n (notes),
misprint-1845 (the 1845 print is wrong; CCEL keeps or shares it).

**Counts:** b 1, d 34, d/case 71, d/comma 2, d/grammar 32, f 3, misprint-1845 4, n 8 (total 155).

**Systematic finding: “Judgment”.** Vol-1 capitalises *judgment* 63 times (the other five volumes: never; they have 313
lowercase). The 1845 print has lowercase in every one but one (ch. 10 §2 “…depends: Judgment, which is daily exercised”,
the head of a list, capital in 1845 too). The 61 lowercase places outside the “unbiassed judgment” finding are listed one
by one (kind d/case) so `apply.py` can take them; the capital looks like a vol-1 conversion slip, not CCEL's.

**Also seen, not listed:** “Gospel” capitalised by 1845 at p. 25 (three times) where CCEL has “gospel” (1845 itself is
inconsistent); 1845 lower case after “?” where CCEL starts a capital. Both left as CCEL's style. 1845 “removal” (I.15 §4) was
already decided (keep “renewal”). The four pilot finds (Epicurus, spectre, contemning, Hiero) are not yet in the text, so they
are listed again.

**Structural:** the address heading of the Prefatory Address and its two Beveridge notes are missing (first row). Two other
Beveridge footnotes are missing outright (I.3 “Calvinus De Scandalis”, I.5 “Seneca, De Benef.”). No other 1845 footnote
or line is missing (every OCR run left unmatched after both passes was checked: the rest are references and running heads),
and no CCEL passage of more than a few words is absent from 1845.


## Prefatory Address to Francis I — `01-prefatory-address.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| heading of the Address | Prefatory Address to King Francis | PREFATORY ADDRESS. TO HIS MOST CHRISTIAN MAJESTY, THE MOST MIGHTY AND ILLUSTRIOUS MONARCH, FRANCIS, KING OF THE FRENCH, HIS SOVEREIGN;¹ JOHN CALVIN PRAYS PEACE AND SALVATION IN CHRIST.² — ¹ In the last edition by Calvin, the words are, as here translated, simply, “Principi suo.” In the edition published at Basle in 1536, the words are, “Principi ac Domino suo sibi observando.” ² Ed. 1536. “In Domino.” | keep the heading; add the address lines under it with their two notes (both are Beveridge's) | 3 | b | high |
| and we be glorified in him | glorified in him? | glorified in Him? | Him? | 7 | d/case | medium |
| intimidated and terror-struck | terror—struck | terror-struck | terror-struck | 5 | d | high |
| dregs and offscourings of the world | off—scourings | off-\|scourings (broken at the line end) | off-scourings | 6 | d | medium |
| a gazing-stock, some proscribed | gazing—stock | gazing-stock | gazing-stock | 8 | d | high |
| the judgment-seat of God | judgment—seat | judgment-seat | judgment-seat | 10 | d | high |
| on our guard against those wonder-workers | wonder—workers | wonder-workers | wonder-workers | 12 | d | high |
| the seed-bed of | seed—bed | seed-bed | seed-bed | 24 | d | high |
| note: No part of this sentence is in Ed. 1536 | is in ed. 1536 | is in Ed. 1536 | Ed. | 18 | d/case | low |

## Epistle to the Reader (1559) — `04-epistle-1559.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| note: the French, beaucoup de meschans hypocrites | de mechans | de meschans | meschans | 32 | n | high |
| Judgment (systematic capital) | the Judgment | the judgment | judgment | 31 | d/case | high |

## Book I, chapter 01 — `book-1-chapter-01.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 true and solid wisdom | solid Wisdom | solid wisdom | wisdom | 47 | d/case | high |

## Book I, chapter 02 — `book-1-chapter-02.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 to join Epicurus (pilot find) | join Epicures | join Epicurus | Epicurus | 52 | d | high |
| Judgment (systematic capital) | and Judgment | and judgment | judgment | 52 | d/case | high |
| Judgment (systematic capital) | the Judgment | the judgment | judgment | 53 | d/case | high |
| Judgment (systematic capital) | of Judgment | of judgment | judgment | 53 | d/case | high |

## Book I, chapter 03 — `book-1-chapter-03.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 any interval of relief from the gnawings | gnawing of conscience | gnawings of conscience | gnawings | 57 | d | high |
| §1 not a few are found¹ who deny | not a few are found who | not a few are found¹ who … ¹ As to some Atheists of the author’s time, see Calvinus De Scandalis. | add the note after “found”: “As to some Atheists of the author’s time, see Calvinus De Scandalis.” | 56 | n | high |
| Judgment (systematic capital) | sound Judgment | sound judgment | judgment | 57 | d/case | high |
| Judgment (systematic capital) | the Judgment | the judgment | judgment | 57 | d/case | high |

## Book I, chapter 04 — `book-1-chapter-04.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Ps 10:11 | He has said in his | He hath said in his | hath | 61 | d/grammar | high |
| §2 Ps 10:11 | God has forgotten | God hath forgotten | hath | 61 | d/grammar | high |
| §3 no spectre or phantom (pilot find) | no spectra | no spectre | spectre | 61 | d | high |
| §4 contemning a majesty (pilot find) | condemning a majesty | contemning a majesty | contemning | 62 | d | high |
| Judgment (systematic capital) | divine Judgment, | divine judgment, | judgment | 60 | d/case | high |
| Judgment (systematic capital) | divine Judgment extorts | divine judgment extorts | judgment | 62 | d/case | high |
| Judgment (systematic capital) | extorts Judgment | extorts judgment | judgment | 62 | d/case | high |
| §1 (pilot note) not contented with sober inquiry, because, … because | not contented with sober inquiry, because, arrogating | not contented with sober inquiry, because, arrogating (the earlier clause also opens “because”) | 1845 and CCEL both; Latin “sed”: “but, arrogating” if the editor fixes plain misprints | 60 | misprint-1845 | medium |

## Book I, chapter 05 — `book-1-chapter-05.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Rom 1:19 | God has showed | God hath showed | hath | 66 | d/grammar | high |
| §12 King Hiero (pilot find) | King Hero | King Hiero | Hiero | 78 | d | high |
| §12 The Stoics … when they said² that | said that the various names of God | said² that the various names … ² Seneca, De Benef., lib. iv. c. 7, et Natural. Quæst. lib. i. in Præf., et lib. ii. c. 45. | add the note after “said”: “Seneca, De Benef., lib. 4 c. 7, et Natural. Quaest. lib. 1 in Praef., et lib. 2 c. 45.” (Arabic in CCEL's style) | 78 | n | high |
| note to the verse “Hence to the bee” (first Dryden note) | Æneid, Book 4 1. 980 | Æneid, Book vi. l. 980-990. | Æneid, Book 6, l. 980 | 70 | f | high |
| Judgment (systematic capital) | a Judgment | a judgment | judgment | 73 | d/case | high |
| Judgment (systematic capital) | final Judgment | final judgment | judgment | 75 | d/case | high |
| Judgment (systematic capital) | own Judgment | own judgment | judgment | 80 | d/case | high |
| §10 far less will the unrighteous ultimately escape | the unrighteous ultimately | the righteous ultimately | keep CCEL (Latin iniquos) | 75 | misprint-1845 | - |

## Book I, chapter 06 — `book-1-chapter-06.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §4 Ps 29:9 | temple does every | temple doth every | doth | 87 | d/grammar | high |
| note: Tertullian, instrumentum adjecit literaturae | literature,” | literaturæ,” | literaturae,” | 86 | n | high |
| Judgment (systematic capital) | depraved Judgment | depraved judgment | judgment | 87 | d/case | high |

## Book I, chapter 07 — `book-1-chapter-07.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 who can assure us (sic 1845 Who) | unblessed Judgment | unbiassed judgment | unbiassed judgment | 94 | d | high |
| §3 Isa 53:1 | To whom has the arm | To whom hath the arm | hath | 96 | d/grammar | high |
| note: scellée en nos cœurs | nos coueurs | nos cœurs | cœurs | 95 | n | high |
| Judgment (systematic capital) | man’s Judgment | man’s judgment | judgment | 90 | d/case | high |
| Judgment (systematic capital) | her Judgment | her judgment | judgment | 91 | d/case | high |
| Judgment (systematic capital) | universal Judgment | universal judgment | judgment | 93 | d/case | high |
| Judgment (systematic capital) | conjectures, Judgments | conjectures, judgments | judgment | 93 | d/case | high |
| Judgment (systematic capital) | own Judgment | own judgment | judgment | 95 | d/case | high |
| Judgment (systematic capital) | human Judgment | human judgment | judgment | 95 | d/case | high |
| Judgment (systematic capital) | our Judgment | our judgment | judgment | 95 | d/case | high |
| Judgment (systematic capital) | and Judgment | and judgment | judgment | 95 | d/case | high |

## Book I, chapter 08 — `book-1-chapter-08.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 Gen 49:5 | “Simon and Levi | “Simeon and Levi | Simeon | 101 | d | high |
| §4 Num 16 Korah, Dathan, and Abiram | Korah, Nathan | Korah, Dathan | Dathan | 102 | d | high |
| Judgment (systematic capital) | human Judgment | human judgment | judgment | 98 | d/case | high |

## Book I, chapter 09 — `book-1-chapter-09.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 1 Thess 5:20 | Despise not prophesying | Despise not prophesyings | prophesyings | 113 | d | high |
| §3 quenched the moment prophesyings fall | moment prophesying | moment prophesyings | prophesyings | 114 | d | high |

## Book I, chapter 10 — `book-1-chapter-10.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Judgment (systematic capital) | justice, Judgment | justice, judgment | judgment | 116 | d/case | high |
| Judgment (systematic capital) | loving-kindness, Judgment, and righteousness, in | loving-kindness, judgment, and righteousness, in | judgment | 117 | d/case | high |
| Judgment (systematic capital) | loving-kindness, Judgment, and righteousness, exist, | loving-kindness, judgment, and righteousness, exist, | judgment | 117 | d/case | high |
| Judgment (systematic capital) | with Judgment | with judgment | judgment | 117 | d/case | high |
| Judgment (systematic capital) | loving-kindness, Judgment, and righteousness, his | loving-kindness, judgment, and righteousness, his | judgment | 117 | d/case | high |

## Book I, chapter 11 — `book-1-chapter-11.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Maximus Tyrius | (Maximum Tyrius | (Maximus Tyrius | Maximus | 121 | d | high |
| §6 decreed by the Elibertine Council | Libertine Council | Elibertine Council | Elibertine (Council of Elvira; the note has “Conc. Elibert.”) | 126 | d | high |
| §8 Josh 24:2 | that Torah and | that Terah and | Terah | 129 | d | high |
| §8 Exod 32:1 | we wet not | we wot not | wot | 129 | d | high |
| §13 Luke 11:33 | when he has lighted | when he hath lighted | hath | 136 | d/grammar | high |
| note: Resp. Pastorum Tigurin. adver. Nicodemitas | Nicidenitas | Nicodemitas | Nicodemitas | 138 | n | high |
| Judgment (systematic capital) | sound Judgment | sound judgment | judgment | 123 | d/case | high |
| Judgment (systematic capital) | a Judgment | a judgment | judgment | 129 | d/case | high |
| §2 they have no authority from God | (Isa 2:8, 31:7; Hos 14:3; Mic 5:13) | (Isa. ii. 8, 31; vii. 57; Hos. xiv. 4; Mic. v. 13;) | keep CCEL (1845's “31; vii. 57” is garbled; Hos 14:4 is Hebrew numbering) | 124 | misprint-1845 | - |

## Book I, chapter 12 — `book-1-chapter-12.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 lawful and right, and thus astrict men | thus restrict men | thus astrict men | astrict | 143 | d | medium |

## Book I, chapter 13 — `book-1-chapter-13.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections, 7: the Divinity of the Son | prove the divinity of the Son | the Divinity of the Son | Divinity | 154 | d/case | low |
| §4 How strange the formulae | strange the formula | strange the formulæ | formulae | 151 | d | high |
| §5 confessed without equivocation, we dwell | without equivocations | without equivocation, | equivocation, | 153 | d/comma | high |
| §9 he who a little before was called Immanuel | called Emmanuel | called Immanuel | Immanuel | 157 | d | medium |
| §12 John 6:47 | in me has eternal | in me hath eternal | hath | 163 | d/grammar | high |
| §12 Acts 9:13 | evil he has done | evil he hath done | hath | 163 | d/grammar | high |
| §12 Acts 9:14 | here he has authority | here he hath authority | hath | 163 | d/grammar | high |
| §13 Isa 48:16 | Spirit, has sent me | Spirit, hath sent me | hath | 164 | d/grammar | high |
| §18 the Personal subsistences carry an order | Personal subsistence carry | Personal subsistences carry | subsistences | 171 | d | high |
| §22 the shapeless mass was upborne by him (Gen 1:2) | was unborn by him | was upborne by him | upborne | 175 | d | high |
| §23 something abstracted² from the essence | abstracte | abstracted² | abstracted | 177 | d | high |
| §24 addresses must have been uncreated | been untreated | been uncreated | uncreated | 180 | d | high |
| §24 nothing is uncreated except the one God | nothing is untreated | nothing is uncreated | uncreated | 180 | d | high |
| note: Comme trois ruisseaux | ruissuaux | ruisseaux | ruisseaux | 181 | n | high |
| Judgment (systematic capital) | the Judgment-seat of Christ. | the judgment-seat of Christ. | judgment | 160 | d/case | high |
| Judgment (systematic capital) | the Judgment-seat of God | the judgment-seat of God | judgment | 160 | d/case | high |

## Book I, chapter 14 — `book-1-chapter-14.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Gentile fictions. The idea that God | fictions. the idea | fictions. The idea | The | 189 | d/case | high |
| §5 they are called Virtues | called virtues. | called Virtues. | Virtues | 195 | d/case | medium |
| note to §6 (angels), Exod 14:19 … | Exod 14:19, 28, 29 | Ex. xiv. 19, 23, 20 (as printed; garbled) | Exod 14:19; 23:20 (the angel going before Israel; 1845's “19, 23, 20” reads as xiv. 19; xxiii. 20) | 196 | f | medium |
| Judgment (systematic capital) | to Judgment, “thousand | to judgment, “thousand | judgment | 195 | d/case | high |
| Judgment (systematic capital) | to Judgment. | to judgment. | judgment | 198 | d/case | high |
| Judgment (systematic capital) | of Judgment | of judgment | judgment | 199 | d/case | high |
| Judgment (systematic capital) | unto Judgment,” (2 | unto judgment,” (2 | judgment | 206 | d/case | high |
| Judgment (systematic capital) | the Judgment | the judgment | judgment | 209 | d/case | high |
| Judgment (systematic capital) | unto Judgment,” &c. | unto judgment,” &c. | judgment | 209 | d/case | high |
| §13 whom resist stedfast in the faith | (1 Pet 5:9) | (1 Pet. v. 8.) | keep CCEL (the words are 5:9) | 203 | misprint-1845 | - |

## Book I, chapter 15 — `book-1-chapter-15.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Luke 12:5 | after he has killed | after he hath killed | hath | 218 | d/grammar | high |
| §3 two words for one thing; and, secondly | thing; And, secondly | thing; and, secondly | and | 220 | d/case | high |
| §6 three appetive faculties | three appetite faculties | three appetive faculties | appetive (as CCEL already has a few lines on: “calling one appetive”) | 226 | d | high |
| §6 which he also terms the appetive intellect | the appetite intellect | the appetive intellect | appetive | 227 | d | high |
| §8 seeing He had full right | seeing he had full | seeing He had full | He (divine pronoun follows the print) | 229 | d/case | high |
| Judgment (systematic capital) | the Judgment of | the judgment of | judgment | 216 | d/case | high |
| Judgment (systematic capital) | the Judgment-seat | the judgment-seat | judgment | 216 | d/case | high |
| Judgment (systematic capital) | of Judgment | of judgment | judgment | 226 | d/case | high |
| Judgment (systematic capital) | and Judgment | and judgment | judgment | 228 | d/case | high |

## Book I, chapter 16 — `book-1-chapter-16.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 Ps 115:3 | He has done whatsoever he has pleased | He hath done whatsoever he hath pleased | hath … hath | 234 | d/grammar | high |
| §4 holds the helm, and overrules | holds the helms | holds the helm, | helm, | 236 | d/comma | high |
| §7 Gen 30:2 | who has withheld | who hath withheld | hath | 241 | d/grammar | high |
| §7 Deut 8:3 | man does not live | man doth not live | doth | 241 | d/grammar | high |
| §6 God, who enlightens all | God, Who enlightens | God, who enlightens | who (divine pronoun follows the print) | 240 | d/case | high |
| §8 De Trinit. lib. 3 | De Trinity. lib | De Trinit. Lib. | De Trinit. | 243 | d | high |
| §9 1 Sam 6:9 | Goes up by the way | goeth up by the way | Goeth | 244 | d/grammar | high |
| §9 1 Sam 6:9 | then he has done us | then he hath done us | hath | 244 | d/grammar | high |
| Judgment (systematic capital) | the Judgments | the judgments | judgment | 238 | d/case | high |
| Judgment (systematic capital) | and Judgment | and judgment | judgment | 243 | d/case | high |

## Book I, chapter 17 — `book-1-chapter-17.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 John 9:3 | Neither has this man | Neither hath this man | hath | 248 | d/grammar | high |
| §2 Rom 11:34 | who has known | who hath known | hath | 250 | d/grammar | high |
| §2 Rom 11:34 | who has been his | who hath been his | hath | 250 | d/grammar | high |
| §2 (August. Quaest. lib. 83 c. 27) | August. Quest. | August. Quæst. | Quaest. (CCEL's “ae” style, as “Quaest. Nat.” in ch. 13) | 251 | d | medium |
| §6 a body which has been uncoffined | been unconfined | been uncoffined | uncoffined | 255 | d | high |
| §8 Job 1:21 | the Lord has taken away; blessed | the Lord hath taken away; blessed | hath | 258 | d/grammar | high |
| §8 2 Sam 16:10 | Lord has said unto him | Lord hath said unto him | hath | 258 | d/grammar | high |
| §10 a cooler head betakes himself to this asylum | retakes himself | betakes himself | betakes | 263 | d | high |
| §12 Num 23:19 | has he said, and | hath he said, and | hath | 265 | d/grammar | high |
| §12 Num 23:19 | has he spoken | hath he spoken | hath | 265 | d/grammar | high |
| §13 Isa 14:27 | hosts has purposed | hosts hath purposed | hath | 266 | d/grammar | high |
| §11 the Lord to arm the fury | belongs to the lord | belongs to the Lord | Lord | 262 | d/case | high |
| note: See Luther on Genesis xxx. 7 | Luther on Gen 3:7 | Luther on Genesis xxx. 7 | Gen 30:7 (follow 1845; neither verse is obviously Luther's predestination passage, so the editor may wish to leave it) | 253 | f | low |
| Judgment (systematic capital) | hidden Judgments as | hidden judgments as | judgment | 248 | d/case | high |
| Judgment (systematic capital) | precipitate Judgment | precipitate judgment | judgment | 249 | d/case | high |
| Judgment (systematic capital) | our Judgment | our judgment | judgment | 249 | d/case | high |
| Judgment (systematic capital) | hidden Judgments of | hidden judgments of | judgment | 249 | d/case | high |
| Judgment (systematic capital) | God, Judgments | God, judgments | judgment | 249 | d/case | high |
| Judgment (systematic capital) | “his Judgments | “his judgments | judgment | 250 | d/case | high |
| Judgment (systematic capital) | his Judgments, | his judgments, | judgment | 250 | d/case | high |
| Judgment (systematic capital) | the Judgments | the judgments | judgment | 254 | d/case | high |
| Judgment (systematic capital) | exercises Judgment | exercises judgment | judgment | 265 | d/case | high |
| Judgment (systematic capital) | the Judgment which | the judgment which | judgment | 266 | d/case | high |

## Book I, chapter 18 — `book-1-chapter-18.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 Job 1:21 | the Lord has taken away; as | the Lord hath taken away; as | hath | 268 | d/grammar | high |
| §1 Job 1:21 | so it has been done | so it hath been done | hath | 268 | d/grammar | high |
| §3 Acts 3:18 | he has so fulfilled | he hath so fulfilled | hath | 269 | d/grammar | high |
| §2 Ezek 14:9 | when he has spoken a thing | when he hath spoken a thing | hath | 271 | d/grammar | high |
| §3 Job 1:21 | Lord has taken away,” when | Lord hath taken away,” when | hath | 273 | d/grammar | high |
| §3 Ps 115:3 | he has done whatsoever he has pleased | he hath done whatsoever he hath pleased | hath … hath | 273 | d/grammar | high |
| §3 Amos 3:6 | which he has not done | which he hath not done | hath | 273 | d/grammar | high |
| §4 2 Kgs 10:10 | Lord has done that | Lord hath done that | hath | 276 | d/grammar | high |
| note: Car ils meslent perversement | perversment | perversement | perversement | 274 | n | high |
| Judgment (systematic capital) | his Judgments. The | his judgments. The | judgment | 268 | d/case | high |
| Judgment (systematic capital) | his Judgments. God | his judgments. God | judgment | 269 | d/case | high |
| Judgment (systematic capital) | a Judgment | a judgment | judgment | 269 | d/case | high |
| Judgment (systematic capital) | his Judgments meanwhile | his judgments meanwhile | judgment | 270 | d/case | high |
| Judgment (systematic capital) | just Judgment | just judgment | judgment | 270 | d/case | high |
| Judgment (systematic capital) | his Judgments, | his judgments, | judgment | 271 | d/case | high |
| Judgment (systematic capital) | his Judgments willingly | his judgments willingly | judgment | 273 | d/case | high |
| Judgment (systematic capital) | those Judgments | those judgments | judgment | 277 | d/case | high |

## Findings (one JSON line each)

```
{"file": "01-prefatory-address.typ", "anchor": "heading of the Address", "ccel": "Prefatory Address to King Francis", "1845": "PREFATORY ADDRESS. TO HIS MOST CHRISTIAN MAJESTY, THE MOST MIGHTY AND ILLUSTRIOUS MONARCH, FRANCIS, KING OF THE FRENCH, HIS SOVEREIGN;¹ JOHN CALVIN PRAYS PEACE AND SALVATION IN CHRIST.² — ¹ In the last edition by Calvin, the words are, as here translated, simply, “Principi suo.” In the edition published at Basle in 1536, the words are, “Principi ac Domino suo sibi observando.” ² Ed. 1536. “In Domino.”", "proposed": "keep the heading; add the address lines under it with their two notes (both are Beveridge's)", "page": 3, "kind": "b", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "and we be glorified in him", "ccel": "glorified in him?", "1845": "glorified in Him?", "proposed": "Him?", "page": 7, "kind": "d/case", "confidence": "medium"}
{"file": "01-prefatory-address.typ", "anchor": "intimidated and terror-struck", "ccel": "terror—struck", "1845": "terror-struck", "proposed": "terror-struck", "page": 5, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "dregs and offscourings of the world", "ccel": "off—scourings", "1845": "off-|scourings (broken at the line end)", "proposed": "off-scourings", "page": 6, "kind": "d", "confidence": "medium"}
{"file": "01-prefatory-address.typ", "anchor": "a gazing-stock, some proscribed", "ccel": "gazing—stock", "1845": "gazing-stock", "proposed": "gazing-stock", "page": 8, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "the judgment-seat of God", "ccel": "judgment—seat", "1845": "judgment-seat", "proposed": "judgment-seat", "page": 10, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "on our guard against those wonder-workers", "ccel": "wonder—workers", "1845": "wonder-workers", "proposed": "wonder-workers", "page": 12, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "the seed-bed of", "ccel": "seed—bed", "1845": "seed-bed", "proposed": "seed-bed", "page": 24, "kind": "d", "confidence": "high"}
{"file": "01-prefatory-address.typ", "anchor": "note: No part of this sentence is in Ed. 1536", "ccel": "is in ed. 1536", "1845": "is in Ed. 1536", "proposed": "Ed.", "page": 18, "kind": "d/case", "confidence": "low"}
{"file": "04-epistle-1559.typ", "anchor": "note: the French, beaucoup de meschans hypocrites", "ccel": "de mechans", "1845": "de meschans", "proposed": "meschans", "page": 32, "kind": "n", "confidence": "high"}
{"file": "04-epistle-1559.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment", "1845": "the judgment", "proposed": "judgment", "page": 31, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-01.typ", "anchor": "§1 true and solid wisdom", "ccel": "solid Wisdom", "1845": "solid wisdom", "proposed": "wisdom", "page": 47, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-02.typ", "anchor": "§2 to join Epicurus (pilot find)", "ccel": "join Epicures", "1845": "join Epicurus", "proposed": "Epicurus", "page": 52, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-02.typ", "anchor": "Judgment (systematic capital)", "ccel": "and Judgment", "1845": "and judgment", "proposed": "judgment", "page": 52, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-02.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment", "1845": "the judgment", "proposed": "judgment", "page": 53, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-02.typ", "anchor": "Judgment (systematic capital)", "ccel": "of Judgment", "1845": "of judgment", "proposed": "judgment", "page": 53, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "§2 any interval of relief from the gnawings", "ccel": "gnawing of conscience", "1845": "gnawings of conscience", "proposed": "gnawings", "page": 57, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "§1 not a few are found¹ who deny", "ccel": "not a few are found who", "1845": "not a few are found¹ who … ¹ As to some Atheists of the author’s time, see Calvinus De Scandalis.", "proposed": "add the note after “found”: “As to some Atheists of the author’s time, see Calvinus De Scandalis.”", "page": 56, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "Judgment (systematic capital)", "ccel": "sound Judgment", "1845": "sound judgment", "proposed": "judgment", "page": 57, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-03.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment", "1845": "the judgment", "proposed": "judgment", "page": 57, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "§2 Ps 10:11", "ccel": "He has said in his", "1845": "He hath said in his", "proposed": "hath", "page": 61, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "§2 Ps 10:11", "ccel": "God has forgotten", "1845": "God hath forgotten", "proposed": "hath", "page": 61, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "§3 no spectre or phantom (pilot find)", "ccel": "no spectra", "1845": "no spectre", "proposed": "spectre", "page": 61, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "§4 contemning a majesty (pilot find)", "ccel": "condemning a majesty", "1845": "contemning a majesty", "proposed": "contemning", "page": 62, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "Judgment (systematic capital)", "ccel": "divine Judgment,", "1845": "divine judgment,", "proposed": "judgment", "page": 60, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "Judgment (systematic capital)", "ccel": "divine Judgment extorts", "1845": "divine judgment extorts", "proposed": "judgment", "page": 62, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "Judgment (systematic capital)", "ccel": "extorts Judgment", "1845": "extorts judgment", "proposed": "judgment", "page": 62, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-04.typ", "anchor": "§1 (pilot note) not contented with sober inquiry, because, … because", "ccel": "not contented with sober inquiry, because, arrogating", "1845": "not contented with sober inquiry, because, arrogating (the earlier clause also opens “because”)", "proposed": "1845 and CCEL both; Latin “sed”: “but, arrogating” if the editor fixes plain misprints", "page": 60, "kind": "misprint-1845", "confidence": "medium"}
{"file": "book-1-chapter-05.typ", "anchor": "§1 Rom 1:19", "ccel": "God has showed", "1845": "God hath showed", "proposed": "hath", "page": 66, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "§12 King Hiero (pilot find)", "ccel": "King Hero", "1845": "King Hiero", "proposed": "Hiero", "page": 78, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "§12 The Stoics … when they said² that", "ccel": "said that the various names of God", "1845": "said² that the various names … ² Seneca, De Benef., lib. iv. c. 7, et Natural. Quæst. lib. i. in Præf., et lib. ii. c. 45.", "proposed": "add the note after “said”: “Seneca, De Benef., lib. 4 c. 7, et Natural. Quaest. lib. 1 in Praef., et lib. 2 c. 45.” (Arabic in CCEL's style)", "page": 78, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "note to the verse “Hence to the bee” (first Dryden note)", "ccel": "Æneid, Book 4 1. 980", "1845": "Æneid, Book vi. l. 980-990.", "proposed": "Æneid, Book 6, l. 980", "page": 70, "kind": "f", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "Judgment (systematic capital)", "ccel": "a Judgment", "1845": "a judgment", "proposed": "judgment", "page": 73, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "Judgment (systematic capital)", "ccel": "final Judgment", "1845": "final judgment", "proposed": "judgment", "page": 75, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "Judgment (systematic capital)", "ccel": "own Judgment", "1845": "own judgment", "proposed": "judgment", "page": 80, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-05.typ", "anchor": "§10 far less will the unrighteous ultimately escape", "ccel": "the unrighteous ultimately", "1845": "the righteous ultimately", "proposed": "keep CCEL (Latin iniquos)", "page": 75, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-1-chapter-06.typ", "anchor": "§4 Ps 29:9", "ccel": "temple does every", "1845": "temple doth every", "proposed": "doth", "page": 87, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-06.typ", "anchor": "note: Tertullian, instrumentum adjecit literaturae", "ccel": "literature,”", "1845": "literaturæ,”", "proposed": "literaturae,”", "page": 86, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-06.typ", "anchor": "Judgment (systematic capital)", "ccel": "depraved Judgment", "1845": "depraved judgment", "proposed": "judgment", "page": 87, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "§1 who can assure us (sic 1845 Who)", "ccel": "unblessed Judgment", "1845": "unbiassed judgment", "proposed": "unbiassed judgment", "page": 94, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "§3 Isa 53:1", "ccel": "To whom has the arm", "1845": "To whom hath the arm", "proposed": "hath", "page": 96, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "note: scellée en nos cœurs", "ccel": "nos coueurs", "1845": "nos cœurs", "proposed": "cœurs", "page": 95, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "Judgment (systematic capital)", "ccel": "man’s Judgment", "1845": "man’s judgment", "proposed": "judgment", "page": 90, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "Judgment (systematic capital)", "ccel": "her Judgment", "1845": "her judgment", "proposed": "judgment", "page": 91, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "Judgment (systematic capital)", "ccel": "universal Judgment", "1845": "universal judgment", "proposed": "judgment", "page": 93, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "Judgment (systematic capital)", "ccel": "conjectures, Judgments", "1845": "conjectures, judgments", "proposed": "judgment", "page": 93, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "Judgment (systematic capital)", "ccel": "own Judgment", "1845": "own judgment", "proposed": "judgment", "page": 95, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "Judgment (systematic capital)", "ccel": "human Judgment", "1845": "human judgment", "proposed": "judgment", "page": 95, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "Judgment (systematic capital)", "ccel": "our Judgment", "1845": "our judgment", "proposed": "judgment", "page": 95, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-07.typ", "anchor": "Judgment (systematic capital)", "ccel": "and Judgment", "1845": "and judgment", "proposed": "judgment", "page": 95, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§3 Gen 49:5", "ccel": "“Simon and Levi", "1845": "“Simeon and Levi", "proposed": "Simeon", "page": 101, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "§4 Num 16 Korah, Dathan, and Abiram", "ccel": "Korah, Nathan", "1845": "Korah, Dathan", "proposed": "Dathan", "page": 102, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-08.typ", "anchor": "Judgment (systematic capital)", "ccel": "human Judgment", "1845": "human judgment", "proposed": "judgment", "page": 98, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-09.typ", "anchor": "§3 1 Thess 5:20", "ccel": "Despise not prophesying", "1845": "Despise not prophesyings", "proposed": "prophesyings", "page": 113, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-09.typ", "anchor": "§3 quenched the moment prophesyings fall", "ccel": "moment prophesying", "1845": "moment prophesyings", "proposed": "prophesyings", "page": 114, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-10.typ", "anchor": "Judgment (systematic capital)", "ccel": "justice, Judgment", "1845": "justice, judgment", "proposed": "judgment", "page": 116, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-10.typ", "anchor": "Judgment (systematic capital)", "ccel": "loving-kindness, Judgment, and righteousness, in", "1845": "loving-kindness, judgment, and righteousness, in", "proposed": "judgment", "page": 117, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-10.typ", "anchor": "Judgment (systematic capital)", "ccel": "loving-kindness, Judgment, and righteousness, exist,", "1845": "loving-kindness, judgment, and righteousness, exist,", "proposed": "judgment", "page": 117, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-10.typ", "anchor": "Judgment (systematic capital)", "ccel": "with Judgment", "1845": "with judgment", "proposed": "judgment", "page": 117, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-10.typ", "anchor": "Judgment (systematic capital)", "ccel": "loving-kindness, Judgment, and righteousness, his", "1845": "loving-kindness, judgment, and righteousness, his", "proposed": "judgment", "page": 117, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§1 Maximus Tyrius", "ccel": "(Maximum Tyrius", "1845": "(Maximus Tyrius", "proposed": "Maximus", "page": 121, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§6 decreed by the Elibertine Council", "ccel": "Libertine Council", "1845": "Elibertine Council", "proposed": "Elibertine (Council of Elvira; the note has “Conc. Elibert.”)", "page": 126, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§8 Josh 24:2", "ccel": "that Torah and", "1845": "that Terah and", "proposed": "Terah", "page": 129, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§8 Exod 32:1", "ccel": "we wet not", "1845": "we wot not", "proposed": "wot", "page": 129, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§13 Luke 11:33", "ccel": "when he has lighted", "1845": "when he hath lighted", "proposed": "hath", "page": 136, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "note: Resp. Pastorum Tigurin. adver. Nicodemitas", "ccel": "Nicidenitas", "1845": "Nicodemitas", "proposed": "Nicodemitas", "page": 138, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "Judgment (systematic capital)", "ccel": "sound Judgment", "1845": "sound judgment", "proposed": "judgment", "page": 123, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "Judgment (systematic capital)", "ccel": "a Judgment", "1845": "a judgment", "proposed": "judgment", "page": 129, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-11.typ", "anchor": "§2 they have no authority from God", "ccel": "(Isa 2:8, 31:7; Hos 14:3; Mic 5:13)", "1845": "(Isa. ii. 8, 31; vii. 57; Hos. xiv. 4; Mic. v. 13;)", "proposed": "keep CCEL (1845's “31; vii. 57” is garbled; Hos 14:4 is Hebrew numbering)", "page": 124, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-1-chapter-12.typ", "anchor": "§3 lawful and right, and thus astrict men", "ccel": "thus restrict men", "1845": "thus astrict men", "proposed": "astrict", "page": 143, "kind": "d", "confidence": "medium"}
{"file": "book-1-chapter-13.typ", "anchor": "Sections, 7: the Divinity of the Son", "ccel": "prove the divinity of the Son", "1845": "the Divinity of the Son", "proposed": "Divinity", "page": 154, "kind": "d/case", "confidence": "low"}
{"file": "book-1-chapter-13.typ", "anchor": "§4 How strange the formulae", "ccel": "strange the formula", "1845": "strange the formulæ", "proposed": "formulae", "page": 151, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§5 confessed without equivocation, we dwell", "ccel": "without equivocations", "1845": "without equivocation,", "proposed": "equivocation,", "page": 153, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§9 he who a little before was called Immanuel", "ccel": "called Emmanuel", "1845": "called Immanuel", "proposed": "Immanuel", "page": 157, "kind": "d", "confidence": "medium"}
{"file": "book-1-chapter-13.typ", "anchor": "§12 John 6:47", "ccel": "in me has eternal", "1845": "in me hath eternal", "proposed": "hath", "page": 163, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§12 Acts 9:13", "ccel": "evil he has done", "1845": "evil he hath done", "proposed": "hath", "page": 163, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§12 Acts 9:14", "ccel": "here he has authority", "1845": "here he hath authority", "proposed": "hath", "page": 163, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§13 Isa 48:16", "ccel": "Spirit, has sent me", "1845": "Spirit, hath sent me", "proposed": "hath", "page": 164, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§18 the Personal subsistences carry an order", "ccel": "Personal subsistence carry", "1845": "Personal subsistences carry", "proposed": "subsistences", "page": 171, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§22 the shapeless mass was upborne by him (Gen 1:2)", "ccel": "was unborn by him", "1845": "was upborne by him", "proposed": "upborne", "page": 175, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§23 something abstracted² from the essence", "ccel": "abstracte", "1845": "abstracted²", "proposed": "abstracted", "page": 177, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§24 addresses must have been uncreated", "ccel": "been untreated", "1845": "been uncreated", "proposed": "uncreated", "page": 180, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "§24 nothing is uncreated except the one God", "ccel": "nothing is untreated", "1845": "nothing is uncreated", "proposed": "uncreated", "page": 180, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "note: Comme trois ruisseaux", "ccel": "ruissuaux", "1845": "ruisseaux", "proposed": "ruisseaux", "page": 181, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment-seat of Christ.", "1845": "the judgment-seat of Christ.", "proposed": "judgment", "page": 160, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-13.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment-seat of God", "1845": "the judgment-seat of God", "proposed": "judgment", "page": 160, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§1 Gentile fictions. The idea that God", "ccel": "fictions. the idea", "1845": "fictions. The idea", "proposed": "The", "page": 189, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§5 they are called Virtues", "ccel": "called virtues.", "1845": "called Virtues.", "proposed": "Virtues", "page": 195, "kind": "d/case", "confidence": "medium"}
{"file": "book-1-chapter-14.typ", "anchor": "note to §6 (angels), Exod 14:19 …", "ccel": "Exod 14:19, 28, 29", "1845": "Ex. xiv. 19, 23, 20 (as printed; garbled)", "proposed": "Exod 14:19; 23:20 (the angel going before Israel; 1845's “19, 23, 20” reads as xiv. 19; xxiii. 20)", "page": 196, "kind": "f", "confidence": "medium"}
{"file": "book-1-chapter-14.typ", "anchor": "Judgment (systematic capital)", "ccel": "to Judgment, “thousand", "1845": "to judgment, “thousand", "proposed": "judgment", "page": 195, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "Judgment (systematic capital)", "ccel": "to Judgment.", "1845": "to judgment.", "proposed": "judgment", "page": 198, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "Judgment (systematic capital)", "ccel": "of Judgment", "1845": "of judgment", "proposed": "judgment", "page": 199, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "Judgment (systematic capital)", "ccel": "unto Judgment,” (2", "1845": "unto judgment,” (2", "proposed": "judgment", "page": 206, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment", "1845": "the judgment", "proposed": "judgment", "page": 209, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "Judgment (systematic capital)", "ccel": "unto Judgment,” &c.", "1845": "unto judgment,” &c.", "proposed": "judgment", "page": 209, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-14.typ", "anchor": "§13 whom resist stedfast in the faith", "ccel": "(1 Pet 5:9)", "1845": "(1 Pet. v. 8.)", "proposed": "keep CCEL (the words are 5:9)", "page": 203, "kind": "misprint-1845", "confidence": "-"}
{"file": "book-1-chapter-15.typ", "anchor": "§1 Luke 12:5", "ccel": "after he has killed", "1845": "after he hath killed", "proposed": "hath", "page": 218, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§3 two words for one thing; and, secondly", "ccel": "thing; And, secondly", "1845": "thing; and, secondly", "proposed": "and", "page": 220, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§6 three appetive faculties", "ccel": "three appetite faculties", "1845": "three appetive faculties", "proposed": "appetive (as CCEL already has a few lines on: “calling one appetive”)", "page": 226, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§6 which he also terms the appetive intellect", "ccel": "the appetite intellect", "1845": "the appetive intellect", "proposed": "appetive", "page": 227, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "§8 seeing He had full right", "ccel": "seeing he had full", "1845": "seeing He had full", "proposed": "He (divine pronoun follows the print)", "page": 229, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment of", "1845": "the judgment of", "proposed": "judgment", "page": 216, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment-seat", "1845": "the judgment-seat", "proposed": "judgment", "page": 216, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "Judgment (systematic capital)", "ccel": "of Judgment", "1845": "of judgment", "proposed": "judgment", "page": 226, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-15.typ", "anchor": "Judgment (systematic capital)", "ccel": "and Judgment", "1845": "and judgment", "proposed": "judgment", "page": 228, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§3 Ps 115:3", "ccel": "He has done whatsoever he has pleased", "1845": "He hath done whatsoever he hath pleased", "proposed": "hath … hath", "page": 234, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§4 holds the helm, and overrules", "ccel": "holds the helms", "1845": "holds the helm,", "proposed": "helm,", "page": 236, "kind": "d/comma", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§7 Gen 30:2", "ccel": "who has withheld", "1845": "who hath withheld", "proposed": "hath", "page": 241, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§7 Deut 8:3", "ccel": "man does not live", "1845": "man doth not live", "proposed": "doth", "page": 241, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§6 God, who enlightens all", "ccel": "God, Who enlightens", "1845": "God, who enlightens", "proposed": "who (divine pronoun follows the print)", "page": 240, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§8 De Trinit. lib. 3", "ccel": "De Trinity. lib", "1845": "De Trinit. Lib.", "proposed": "De Trinit.", "page": 243, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§9 1 Sam 6:9", "ccel": "Goes up by the way", "1845": "goeth up by the way", "proposed": "Goeth", "page": 244, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "§9 1 Sam 6:9", "ccel": "then he has done us", "1845": "then he hath done us", "proposed": "hath", "page": 244, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgments", "1845": "the judgments", "proposed": "judgment", "page": 238, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-16.typ", "anchor": "Judgment (systematic capital)", "ccel": "and Judgment", "1845": "and judgment", "proposed": "judgment", "page": 243, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§1 John 9:3", "ccel": "Neither has this man", "1845": "Neither hath this man", "proposed": "hath", "page": 248, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§2 Rom 11:34", "ccel": "who has known", "1845": "who hath known", "proposed": "hath", "page": 250, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§2 Rom 11:34", "ccel": "who has been his", "1845": "who hath been his", "proposed": "hath", "page": 250, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§2 (August. Quaest. lib. 83 c. 27)", "ccel": "August. Quest.", "1845": "August. Quæst.", "proposed": "Quaest. (CCEL's “ae” style, as “Quaest. Nat.” in ch. 13)", "page": 251, "kind": "d", "confidence": "medium"}
{"file": "book-1-chapter-17.typ", "anchor": "§6 a body which has been uncoffined", "ccel": "been unconfined", "1845": "been uncoffined", "proposed": "uncoffined", "page": 255, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§8 Job 1:21", "ccel": "the Lord has taken away; blessed", "1845": "the Lord hath taken away; blessed", "proposed": "hath", "page": 258, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§8 2 Sam 16:10", "ccel": "Lord has said unto him", "1845": "Lord hath said unto him", "proposed": "hath", "page": 258, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§10 a cooler head betakes himself to this asylum", "ccel": "retakes himself", "1845": "betakes himself", "proposed": "betakes", "page": 263, "kind": "d", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§12 Num 23:19", "ccel": "has he said, and", "1845": "hath he said, and", "proposed": "hath", "page": 265, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§12 Num 23:19", "ccel": "has he spoken", "1845": "hath he spoken", "proposed": "hath", "page": 265, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§13 Isa 14:27", "ccel": "hosts has purposed", "1845": "hosts hath purposed", "proposed": "hath", "page": 266, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "§11 the Lord to arm the fury", "ccel": "belongs to the lord", "1845": "belongs to the Lord", "proposed": "Lord", "page": 262, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "note: See Luther on Genesis xxx. 7", "ccel": "Luther on Gen 3:7", "1845": "Luther on Genesis xxx. 7", "proposed": "Gen 30:7 (follow 1845; neither verse is obviously Luther's predestination passage, so the editor may wish to leave it)", "page": 253, "kind": "f", "confidence": "low"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "hidden Judgments as", "1845": "hidden judgments as", "proposed": "judgment", "page": 248, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "precipitate Judgment", "1845": "precipitate judgment", "proposed": "judgment", "page": 249, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "our Judgment", "1845": "our judgment", "proposed": "judgment", "page": 249, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "hidden Judgments of", "1845": "hidden judgments of", "proposed": "judgment", "page": 249, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "God, Judgments", "1845": "God, judgments", "proposed": "judgment", "page": 249, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "“his Judgments", "1845": "“his judgments", "proposed": "judgment", "page": 250, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "his Judgments,", "1845": "his judgments,", "proposed": "judgment", "page": 250, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgments", "1845": "the judgments", "proposed": "judgment", "page": 254, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "exercises Judgment", "1845": "exercises judgment", "proposed": "judgment", "page": 265, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-17.typ", "anchor": "Judgment (systematic capital)", "ccel": "the Judgment which", "1845": "the judgment which", "proposed": "judgment", "page": 266, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§1 Job 1:21", "ccel": "the Lord has taken away; as", "1845": "the Lord hath taken away; as", "proposed": "hath", "page": 268, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§1 Job 1:21", "ccel": "so it has been done", "1845": "so it hath been done", "proposed": "hath", "page": 268, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§3 Acts 3:18", "ccel": "he has so fulfilled", "1845": "he hath so fulfilled", "proposed": "hath", "page": 269, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§2 Ezek 14:9", "ccel": "when he has spoken a thing", "1845": "when he hath spoken a thing", "proposed": "hath", "page": 271, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§3 Job 1:21", "ccel": "Lord has taken away,” when", "1845": "Lord hath taken away,” when", "proposed": "hath", "page": 273, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§3 Ps 115:3", "ccel": "he has done whatsoever he has pleased", "1845": "he hath done whatsoever he hath pleased", "proposed": "hath … hath", "page": 273, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§3 Amos 3:6", "ccel": "which he has not done", "1845": "which he hath not done", "proposed": "hath", "page": 273, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "§4 2 Kgs 10:10", "ccel": "Lord has done that", "1845": "Lord hath done that", "proposed": "hath", "page": 276, "kind": "d/grammar", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "note: Car ils meslent perversement", "ccel": "perversment", "1845": "perversement", "proposed": "perversement", "page": 274, "kind": "n", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "Judgment (systematic capital)", "ccel": "his Judgments. The", "1845": "his judgments. The", "proposed": "judgment", "page": 268, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "Judgment (systematic capital)", "ccel": "his Judgments. God", "1845": "his judgments. God", "proposed": "judgment", "page": 269, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "Judgment (systematic capital)", "ccel": "a Judgment", "1845": "a judgment", "proposed": "judgment", "page": 269, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "Judgment (systematic capital)", "ccel": "his Judgments meanwhile", "1845": "his judgments meanwhile", "proposed": "judgment", "page": 270, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "Judgment (systematic capital)", "ccel": "just Judgment", "1845": "just judgment", "proposed": "judgment", "page": 270, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "Judgment (systematic capital)", "ccel": "his Judgments,", "1845": "his judgments,", "proposed": "judgment", "page": 271, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "Judgment (systematic capital)", "ccel": "his Judgments willingly", "1845": "his judgments willingly", "proposed": "judgment", "page": 273, "kind": "d/case", "confidence": "high"}
{"file": "book-1-chapter-18.typ", "anchor": "Judgment (systematic capital)", "ccel": "those Judgments", "1845": "those judgments", "proposed": "judgment", "page": 277, "kind": "d/case", "confidence": "high"}
```
