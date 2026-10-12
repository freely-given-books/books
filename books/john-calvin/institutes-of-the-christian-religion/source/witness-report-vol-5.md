# Calvin, Institutes, vol. 5 (Book IV, Argument and chapters 1–13): CCEL vs the 1845 printing

Base: `chapters/typ/vol-5/*.typ` (CCEL text, the 1953 reprint's marked
editorial notes already removed). Witness: Calvin Translation Society,
Edinburgh 1845, vol. 3 (archive.org `institutesofthec03calvuoft`): Book IV,
Argument and chapters 1–13, pp. 1–298. The OCR was aligned word by word
with the edition (difflib; scripts in `scratchpad/calvin-v5/`, adapted from
the vol-4 agent's: `align.py` writes raw candidates to `cand-*.txt`,
`notes.py` compares every footnote with the 1845 notes, findings in
`findings.jsonl`, `build.py` writes this file and checks that every "ccel"
string occurs exactly once in its file). Doubtful places were read on the
page images (crops in `scratchpad/calvin-pages/`, files `r*.jpg`,
`cr*.png`).

**Scan offset (measured):** scan index n = printed page + 3 for this
volume (read on the images of pp. 17 = n20, 147 = n150, 290 = n293).
"verified" in the confidence column = read on the image. Otherwise the OCR
reading is an unambiguous real word in clean OCR.

**Kinds:** **b** = 1845 words missing in CCEL. **c** = CCEL words not in 1845.
**d** = a different word. **d/comma** = CCEL turned the comma after a word
into a final "s"; every case checked against the 1845 comma. **e** =
Greek/Latin/Hebrew. **f** = reference numbers (proposed in CCEL's Arabic
style). **n** = notes (including any note, or part of one, that 1845 does not
have: proposed "drop"). **info** = CCEL departs from 1845 but corrects a
misprint there; keep CCEL.

**Not listed one by one (CCEL-wide editorial choices, kept by the edition):**
Arabic numerals in references; CCEL's spellings; has/does/comes for
hath/doth/cometh in Scripture quotations; CCEL's punctuation around
references; closed-up compounds.

**Greek and Hebrew encoding.** A search of every vol-5 file for Greek in the
old SGreek font codes, private-use characters and Hebrew font codes found
none, and no empty "()" where a Hebrew or Greek word was lost. Greek in
vol-5: IV.3 (διακονία; Acts 14:23), IV.4 (κλῆρος, χειροτονία, χειροθεσία),
IV.6 (Homer), IV.10 (ἐθελοθρησκεία, ἅπτεσθαι); each read on the image.

## Book IV, Argument — `book-4-argument.typ`

No differences beyond OCR noise.

## Book IV, chapter 01 — `book-4-chapter-01.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §5 dwell between the cherubims | (Ps 32:13 | (Ps. cxxxii. 13 | (Ps. 132:13 | 15 | f | high |
| §18 sooner than be dragged thither | sooner than suffered themselves | sooner than suffer themselves | sooner than suffer themselves | 31 | d | high |
| §20 the Novatians: believers under the burden of sin | flee for pardon. For they preten | flee for pardon. For they pretend | flee for pardon. For they pretend | 32 | d | high |
| note (Pour donner exemple) | lieu pens’t semplement | lieu pensât semplement | lieu pensât semplement | 24 | n | high (verified) |
| note (Comme s’ils eussent ete quelques anges) | had bean some | had been some | had been some | 25 | n | high |
| note (Corinthian vices) | l Cor. 1:11; 3:3; 5:l; 6:7; 9:l; 15:12 | 1 Cor. i. 11; iii. 3; v. 1; vi. 7; ix. 1; xv. 12 | 1 Cor. 1:11; 3:3; 5:1; 6:7; 9:1; 15:12 | 27 | f | high |
| note (Ce n’a pas eté seulement afin) | convertiroient alla foy | convertiroient a la foy | convertiroient a la foy | 34 | n | high |
| Sections 28 (the item lacks the stop after its number, so it is not set as item 28) | 28 Objection, that | 28. Objection, that | 28\. Objection, that | 9 | f | high |

## Book IV, chapter 02 — `book-4-chapter-02.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 the pretence of the Romanists | the presence of the Romanists | the pretence of the Romanists | the pretence of the Romanists | 44 | d | high |
| §3 make a gloss of the name of Church | name of the Church | name of Church | name of Church | 47 | c | high (verified) |
| §9 Levitical priests, entitled to hold it | (Exod. 24:9) | (Exod. xxix. 9.) | (Exod. 29:9) | 51 | f | high |
| §11 still a true sign and sacrament | still to he a | still to be a | still to be a | 54 | d | high |
| note (Secondement, qu’encore il y ait) | qu’icelui no laisse | qu’icelui ne laisse | qu’icelui ne laisse | 42 | n | high |
| note (Or tant s’en faut) | “Or tent s | “Or tant s | “Or tant s | 46 | n | high |

## Book IV, chapter 03 — `book-4-chapter-03.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §6 stewards of the mysteries of God | (I Cor. 4:1) | (1 Cor. iv. 1.) | (1 Cor. 4:1) | 63 | f | high |
| §6 woe unto me if I preach not the Gospel | (1 Cor. 4:16) | (1 Cor. ix. 16.) | (1 Cor. 9:16) | 64 | f | high |
| §15 Lay hands suddenly on no man | (l Tim. 5:22) | (1 Tim. v. 22.) | (1 Tim. 5:22) | 70 | f | high |
| §16 Lastly, it is to be observed | it is to observed | it is to be observed | it is to be observed | 72 | b | high |
| note (our Saviour sending his apostles) | Acts 1 8 | Acts i. 8 | Acts 1:8 | 68 | f | high |
| note (our Saviour sending his apostles) | Mark 6:15 | Mark vi. 15 | Mark 16:15 (1845 has the same misprint: Mark 6:15 is not the sending of the apostles; 16:15 is) | 68 | f | medium |
| note (Calv. in Acts 6:3, and Luther) | p 374 | p. 374 | p. 374 | 70 | n | high |

## Book IV, chapter 04 — `book-4-chapter-04.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Jerome: the whole charge devolved upon one (the words between are a stray line from IV.5 §6, p. 96, which CCEL also has in its right place) | devolved upon mendatory rescripts, preventions, and the like. But they all conduct one. | devolved upon one. | devolved upon one. | 75 | c | high |
| note (La cognoissance venoit aux patriarches) | concile do tous | concile de tous | concile de tous | 77 | n | high |
| note (Afin qu’il n’allâ nulle part) | n’all’ nulle | n’allâ nulle | n’allâ nulle | 82 | n | high (verified) |

## Book IV, chapter 05 — `book-4-chapter-05.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary, I. sec. 1-7 | sec. l-7 | sec. 1-7 | sec. 1-7 | 89 | f | high |
| §1 the honour of holding the first rank in this discussion | disscussion | discussion | discussion | 90 | d | high |
| §4 ceremonies concerning the cup and paten | cup and patent | cup and paten | cup and paten | 93 | d | high |
| §17 Isa. 52:1, put on thy strength | O Sion; | O Zion; | O Zion; | 105 | d | high |
| §17 those blessings which these words literally express | blessings with these | blessings which these | blessings which these | 105 | d | high |
| §17 splendid clothes, numerous attendants, and magnificent palaces | magnificent places | magnificent palaces | magnificent palaces | 106 | d | high |
| note (C’est un acte semblable) | s’il ést digne | s’il est digne | s’il est digne | 95 | n | high (verified) |
| note (les vices des personnes) | “Ies vices | “les vices | “les vices | 99 | n | high |

## Book IV, chapter 06 — `book-4-chapter-06.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §5 Peter surpasses others in fervid zeal | in doctrine, in magnanimity | in doctrine, and magnanimity | in doctrine, and magnanimity | 113 | d | high |
| §14 Peter's occupation of the Roman See | Certainly it is, that | Certain it is, that | Certain it is, that | 120 | d | high |
| §15 all seek their own | (Phil. 2:21) | (Phil. ii. 20.) | keep (Phil. 2:21) (CCEL corrects 1845's misprint) | 121 | info | high |
| §17 Cyprian, de Simplic. Prælat. | de Simplie. | de Simplic. | de Simplic. | 124 | d | high |
| note (Ils ont pour leur bouclier) | Ils ont Four leur bouelier | Ils ont pour leur bouclier | Ils ont pour leur bouclier | 114 | n | high |
| note on “one celestial Head” (§9): CCEL repeats the IV.8 §3 note on Jeremiah (p. 162, also in its place there); 1845's note here gives the references | The French adds, “Vision receue du Seigneur; Le Seigneur des armees l’a dit,”—A vision received from the Lord; The Lord of hosts hath spoken it. | Eph. i. 22; iv. 15; v. 23; Col. i. 18; ii. 10. | Eph. 1:22; 4:15; 5:23; Col. 1:18; 2:10. | 117 | n | high |

## Book IV, chapter 07 — `book-4-chapter-07.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| summary: Peter one of the chief | one ofthe chief | one of the chief | one of the chief | 125 | d | high |
| §4 the whole Church goes to ruin when that universal bishop falls | falls” (Lib. 4 Ep. 188) | falls,” (Lib. vi. Ep. 188.) | falls” (Lib. 6 Ep. 188) | 131 | f | high (verified) |
| §16 Gregory to Eulogius | Lib. 8 Ep. 30 | Lib. vii. Ep. 30 | Lib. 7 Ep. 30 | 142 | f | high (verified) |
| §18 they share the spoils of the traveller | Few (say he) | Few (says he) | Few (says he) | 144 | d | high |
| §26 so to fix the honour of the primacy to a particular spot, as that | primacy to a particular spot, so that | primacy to a particular spot, as that | primacy to a particular spot, as that | 153 | d | high (verified) |
| note (Voila l’Archeveque d’Arles) | retracter; si bon lui semble la sentence de l’Eveque Romain. au | retracter, si bon lui semble la sentence de l’Eveque Romain: au | retracter, si bon lui semble la sentence de l’Eveque Romain: au | 137 | n | high (verified) |

## Book IV, chapter 08 — `book-4-chapter-08.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 the power of the Church is not to be mischievously adorned | adorned, but it is to be confined | adorned, but is to be confined | adorned, but is to be confined | 159 | c | high |

## Book IV, chapter 09 — `book-4-chapter-09.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §11 councils cannot err, or if they err | cannot err, of if | cannot err, or if | cannot err, or if | 186 | d | high |

## Book IV, chapter 10 — `book-4-chapter-10.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §8 Col. 2, he condemns all will-worship | condemns all ἐθελοθρησκειας that | condemns all ἐθελοθρησκείας; that | condemns all ἐθελοθρησκείας; that | 200 | e | high (verified) |
| §3 the sense which sists men before the judgment-seat of God | sense which sits men | sense which sists men | sense which sists men | 195 | d | high |
| §4 Paul: some having put away a good conscience | saying, the, “some | saying, that “some | saying, that “some | 195 | d | high |
| §6 in expounding the law we have adverted to this subject | (Book 3 chap. 4 sec. 6) | (Book III. chap. iv. 5,) | (Book 3 chap. 4 sec. 5) as 1845 prints it (the section number differs; neither obviously fits "in expounding the law", which suggests Book 2 chap. 8: for the editor) | 197 | f | medium (verified) |
| §21 accommodate themselves to their brother | and to not abuse | and not to abuse | and not to abuse | 214 | d | high |
| §23 God detests the audacious attempt | no other reasons but | no other reason but | no other reason but | 217 | d | high |
| §23 In Jerusalem will I put my name | (2 Kings 22:3, 4) | (2 Kings xxi. 3, 4,) | (2 Kings 21:3, 4) | 217 | f | high |
| §25 Samuel sacrificed in Ramath | (l Sam 7:17) | (1 Sam. vii. 17,) | (1 Sam. 7:17) | 218 | f | high (verified) |
| note (tel a eté le sens de cette distinction vulgaire) | common distincti has | common distinction which has | common distinction which has | 196 | n | high |

## Book IV, chapter 11 — `book-4-chapter-11.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §10 those bishops who abused the goodness of princes | bishops who abuse the | bishops who abused the | bishops who abused the | 239 | d | high |
| §11 Bernard is speaking of civil judgments | Bernard is spearing | Bernard is speaking | Bernard is speaking | 239 | d | high |

## Book IV, chapter 12 — `book-4-chapter-12.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §3 But as our Saviour is not there speaking of secret faults | Put as our Saviour | But as our Saviour | But as our Saviour | 249 | d | high |
| §5 the Lord's Supper, which might be profaned | might he profaned | might be profaned | might be profaned | 251 | d | high |
| §11 Augustine contra Parmen.: excludes what he cannot correct | or unjustly condemns | or justly condemns | or justly condemns | 257 | d | high (verified) |
| §15 when the mind is affected as it ought | mind is effected | mind is affected | mind is affected | 261 | d | high |
| §20 the vulgar imagined that they thereby performed | thereby perform some | thereby performed some | thereby performed some | 264 | d | high |
| §22 these good successors did not abrogate | abrograte | abrogate | abrogate | 268 | d | high |
| note (J’use de ce mot de Clercs) | mot de Cleres | mot de Clercs | mot de Clercs | 248 | n | high |

## Book IV, chapter 13 — `book-4-chapter-13.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 to whom, what, with what intention we vow | In regard in the first | In regard to the first | In regard to the first | 275 | d | high |
| §2 will-worship, how specious and splendid soever | soever it be in the eyes | soever it may be in the eyes | soever it may be in the eyes | 275 | b | high |
| §10 if you take away their idleness | where will that contemplative | where will be that contemplative | where will be that contemplative | 285 | b | high |
| §12 monasticism, as it now exists, is founded | as it now exists, founded | as it now exists, is founded | as it now exists, is founded | 287 | b | high |
| §13 if the sum of perfection consists in this | sum off perfection | sum of perfection | sum of perfection | 288 | d | high |
| §14 Still there was nothing which the Fathers less intended | nothing with the Fathers | nothing which the Fathers | nothing which the Fathers | 289 | d | high |
| §17 Cyprian: if virgins have dedicated themselves to Christ in faith | themselves to Christian faith | themselves to Christ in faith | themselves to Christ in faith | 293 | d | high |
| §18 those widows who were then admitted to a public ministry | widows who were admitted | widows who were then admitted | widows who were then admitted | 294 | b | high |
| note (On the vow of celibacy, see Calv.) | celibacy. see | celibacy, see | celibacy, see | 277 | n | high |
| note (Latin, Catechismo) | “Catechism.” | “Catechismo.” | “Catechismo.” | 280 | n | high |
| note (Bernard. ad Guliel. Abbat.) | Abbat.. | Abbat. | Abbat. | 291 | n | high |

## Notes: only the 1845 printing's own

Every footnote in vol-5 (77 in all) was compared with the 1845 notes
(`notes.py`). None is modern editorial matter: no 1953 note survives here,
with or without a "D" marker, and no Beveridge note has anything appended.
One CCEL note is wrong in another way: the note on "one celestial Head"
(IV.6 §9) is a copy of the IV.8 §3 French note ("Vision receue du
Seigneur"), where 1845 gives Eph. 1:22 etc. (listed above, kind n).

## Other checks

- Section and summary numbering checked in every file: all sequences
  complete; one summary item (IV.1, 28) lacks the stop after its number.
- A stray line: IV.4 §2 carries "mendatory rescripts, preventions, and the
  like. But they all conduct" from IV.5 §6, in the middle of Jerome's
  sentence.
- Greek read on the images: the 1845 printing sets the Greek of IV.3, IV.4
  and IV.6 without accents (κατ᾽ ἐκκλησιαν, κληρος, ἀγαθον
  πολυκοιρανιη), so CCEL's forms are kept; one fault in IV.10.
- No comma keyed as a final "s" was found in this volume (vol-1–4 had 50–60
  each): every s-plural difference was checked.
- Not listed: 1845 misprints CCEL corrects silently in references beyond
  the one shown (info); spelling differences (practised/practiced,
  stedfastly, ensure/insure, Rabbi forms); OCR noise (fi ligatures read as
  "n", "Horn." for "Hom.").

## Findings as JSON lines

```json
{"file": "book-4-chapter-01.typ", "anchor": "§5 dwell between the cherubims", "ccel": "(Ps 32:13", "1845": "(Ps. cxxxii. 13", "proposed": "(Ps. 132:13", "page": 15, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "§18 sooner than be dragged thither", "ccel": "sooner than suffered themselves", "1845": "sooner than suffer themselves", "proposed": "sooner than suffer themselves", "page": 31, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "§20 the Novatians: believers under the burden of sin", "ccel": "flee for pardon. For they preten", "1845": "flee for pardon. For they pretend", "proposed": "flee for pardon. For they pretend", "page": 32, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "note (Pour donner exemple)", "ccel": "lieu pens’t semplement", "1845": "lieu pensât semplement", "proposed": "lieu pensât semplement", "page": 24, "kind": "n", "confidence": "high (verified)"}
{"file": "book-4-chapter-01.typ", "anchor": "note (Comme s’ils eussent ete quelques anges)", "ccel": "had bean some", "1845": "had been some", "proposed": "had been some", "page": 25, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "note (Corinthian vices)", "ccel": "l Cor. 1:11; 3:3; 5:l; 6:7; 9:l; 15:12", "1845": "1 Cor. i. 11; iii. 3; v. 1; vi. 7; ix. 1; xv. 12", "proposed": "1 Cor. 1:11; 3:3; 5:1; 6:7; 9:1; 15:12", "page": 27, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "note (Ce n’a pas eté seulement afin)", "ccel": "convertiroient alla foy", "1845": "convertiroient a la foy", "proposed": "convertiroient a la foy", "page": 34, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-02.typ", "anchor": "§3 the pretence of the Romanists", "ccel": "the presence of the Romanists", "1845": "the pretence of the Romanists", "proposed": "the pretence of the Romanists", "page": 44, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-02.typ", "anchor": "§3 make a gloss of the name of Church", "ccel": "name of the Church", "1845": "name of Church", "proposed": "name of Church", "page": 47, "kind": "c", "confidence": "high (verified)"}
{"file": "book-4-chapter-02.typ", "anchor": "§9 Levitical priests, entitled to hold it", "ccel": "(Exod. 24:9)", "1845": "(Exod. xxix. 9.)", "proposed": "(Exod. 29:9)", "page": 51, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-02.typ", "anchor": "§11 still a true sign and sacrament", "ccel": "still to he a", "1845": "still to be a", "proposed": "still to be a", "page": 54, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-02.typ", "anchor": "note (Secondement, qu’encore il y ait)", "ccel": "qu’icelui no laisse", "1845": "qu’icelui ne laisse", "proposed": "qu’icelui ne laisse", "page": 42, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-02.typ", "anchor": "note (Or tant s’en faut)", "ccel": "“Or tent s", "1845": "“Or tant s", "proposed": "“Or tant s", "page": 46, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-03.typ", "anchor": "§6 stewards of the mysteries of God", "ccel": "(I Cor. 4:1)", "1845": "(1 Cor. iv. 1.)", "proposed": "(1 Cor. 4:1)", "page": 63, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-03.typ", "anchor": "§6 woe unto me if I preach not the Gospel", "ccel": "(1 Cor. 4:16)", "1845": "(1 Cor. ix. 16.)", "proposed": "(1 Cor. 9:16)", "page": 64, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-03.typ", "anchor": "§15 Lay hands suddenly on no man", "ccel": "(l Tim. 5:22)", "1845": "(1 Tim. v. 22.)", "proposed": "(1 Tim. 5:22)", "page": 70, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-03.typ", "anchor": "§16 Lastly, it is to be observed", "ccel": "it is to observed", "1845": "it is to be observed", "proposed": "it is to be observed", "page": 72, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-03.typ", "anchor": "note (our Saviour sending his apostles)", "ccel": "Acts 1 8", "1845": "Acts i. 8", "proposed": "Acts 1:8", "page": 68, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-03.typ", "anchor": "note (our Saviour sending his apostles)", "ccel": "Mark 6:15", "1845": "Mark vi. 15", "proposed": "Mark 16:15 (1845 has the same misprint: Mark 6:15 is not the sending of the apostles; 16:15 is)", "page": 68, "kind": "f", "confidence": "medium"}
{"file": "book-4-chapter-03.typ", "anchor": "note (Calv. in Acts 6:3, and Luther)", "ccel": "p 374", "1845": "p. 374", "proposed": "p. 374", "page": 70, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-04.typ", "anchor": "§2 Jerome: the whole charge devolved upon one (the words between are a stray line from IV.5 §6, p. 96, which CCEL also has in its right place)", "ccel": "devolved upon mendatory rescripts, preventions, and the like. But they all conduct one.", "1845": "devolved upon one.", "proposed": "devolved upon one.", "page": 75, "kind": "c", "confidence": "high"}
{"file": "book-4-chapter-04.typ", "anchor": "note (La cognoissance venoit aux patriarches)", "ccel": "concile do tous", "1845": "concile de tous", "proposed": "concile de tous", "page": 77, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-04.typ", "anchor": "note (Afin qu’il n’allâ nulle part)", "ccel": "n’all’ nulle", "1845": "n’allâ nulle", "proposed": "n’allâ nulle", "page": 82, "kind": "n", "confidence": "high (verified)"}
{"file": "book-4-chapter-05.typ", "anchor": "summary, I. sec. 1-7", "ccel": "sec. l-7", "1845": "sec. 1-7", "proposed": "sec. 1-7", "page": 89, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-05.typ", "anchor": "§1 the honour of holding the first rank in this discussion", "ccel": "disscussion", "1845": "discussion", "proposed": "discussion", "page": 90, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-05.typ", "anchor": "§4 ceremonies concerning the cup and paten", "ccel": "cup and patent", "1845": "cup and paten", "proposed": "cup and paten", "page": 93, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-05.typ", "anchor": "§17 Isa. 52:1, put on thy strength", "ccel": "O Sion;", "1845": "O Zion;", "proposed": "O Zion;", "page": 105, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-05.typ", "anchor": "§17 those blessings which these words literally express", "ccel": "blessings with these", "1845": "blessings which these", "proposed": "blessings which these", "page": 105, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-05.typ", "anchor": "§17 splendid clothes, numerous attendants, and magnificent palaces", "ccel": "magnificent places", "1845": "magnificent palaces", "proposed": "magnificent palaces", "page": 106, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-05.typ", "anchor": "note (C’est un acte semblable)", "ccel": "s’il ést digne", "1845": "s’il est digne", "proposed": "s’il est digne", "page": 95, "kind": "n", "confidence": "high (verified)"}
{"file": "book-4-chapter-05.typ", "anchor": "note (les vices des personnes)", "ccel": "“Ies vices", "1845": "“les vices", "proposed": "“les vices", "page": 99, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "§5 Peter surpasses others in fervid zeal", "ccel": "in doctrine, in magnanimity", "1845": "in doctrine, and magnanimity", "proposed": "in doctrine, and magnanimity", "page": 113, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "§14 Peter's occupation of the Roman See", "ccel": "Certainly it is, that", "1845": "Certain it is, that", "proposed": "Certain it is, that", "page": 120, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "§15 all seek their own", "ccel": "(Phil. 2:21)", "1845": "(Phil. ii. 20.)", "proposed": "keep (Phil. 2:21) (CCEL corrects 1845's misprint)", "page": 121, "kind": "info", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "§17 Cyprian, de Simplic. Prælat.", "ccel": "de Simplie.", "1845": "de Simplic.", "proposed": "de Simplic.", "page": 124, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "note (Ils ont pour leur bouclier)", "ccel": "Ils ont Four leur bouelier", "1845": "Ils ont pour leur bouclier", "proposed": "Ils ont pour leur bouclier", "page": 114, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "note on “one celestial Head” (§9): CCEL repeats the IV.8 §3 note on Jeremiah (p. 162, also in its place there); 1845's note here gives the references", "ccel": "The French adds, “Vision receue du Seigneur; Le Seigneur des armees l’a dit,”—A vision received from the Lord; The Lord of hosts hath spoken it.", "1845": "Eph. i. 22; iv. 15; v. 23; Col. i. 18; ii. 10.", "proposed": "Eph. 1:22; 4:15; 5:23; Col. 1:18; 2:10.", "page": 117, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-07.typ", "anchor": "summary: Peter one of the chief", "ccel": "one ofthe chief", "1845": "one of the chief", "proposed": "one of the chief", "page": 125, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-07.typ", "anchor": "§4 the whole Church goes to ruin when that universal bishop falls", "ccel": "falls” (Lib. 4 Ep. 188)", "1845": "falls,” (Lib. vi. Ep. 188.)", "proposed": "falls” (Lib. 6 Ep. 188)", "page": 131, "kind": "f", "confidence": "high (verified)"}
{"file": "book-4-chapter-07.typ", "anchor": "§16 Gregory to Eulogius", "ccel": "Lib. 8 Ep. 30", "1845": "Lib. vii. Ep. 30", "proposed": "Lib. 7 Ep. 30", "page": 142, "kind": "f", "confidence": "high (verified)"}
{"file": "book-4-chapter-07.typ", "anchor": "§18 they share the spoils of the traveller", "ccel": "Few (say he)", "1845": "Few (says he)", "proposed": "Few (says he)", "page": 144, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-07.typ", "anchor": "§26 so to fix the honour of the primacy to a particular spot, as that", "ccel": "primacy to a particular spot, so that", "1845": "primacy to a particular spot, as that", "proposed": "primacy to a particular spot, as that", "page": 153, "kind": "d", "confidence": "high (verified)"}
{"file": "book-4-chapter-07.typ", "anchor": "note (Voila l’Archeveque d’Arles)", "ccel": "retracter; si bon lui semble la sentence de l’Eveque Romain. au", "1845": "retracter, si bon lui semble la sentence de l’Eveque Romain: au", "proposed": "retracter, si bon lui semble la sentence de l’Eveque Romain: au", "page": 137, "kind": "n", "confidence": "high (verified)"}
{"file": "book-4-chapter-08.typ", "anchor": "§1 the power of the Church is not to be mischievously adorned", "ccel": "adorned, but it is to be confined", "1845": "adorned, but is to be confined", "proposed": "adorned, but is to be confined", "page": 159, "kind": "c", "confidence": "high"}
{"file": "book-4-chapter-09.typ", "anchor": "§11 councils cannot err, or if they err", "ccel": "cannot err, of if", "1845": "cannot err, or if", "proposed": "cannot err, or if", "page": 186, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-10.typ", "anchor": "§8 Col. 2, he condemns all will-worship", "ccel": "condemns all ἐθελοθρησκειας that", "1845": "condemns all ἐθελοθρησκείας; that", "proposed": "condemns all ἐθελοθρησκείας; that", "page": 200, "kind": "e", "confidence": "high (verified)"}
{"file": "book-4-chapter-10.typ", "anchor": "§3 the sense which sists men before the judgment-seat of God", "ccel": "sense which sits men", "1845": "sense which sists men", "proposed": "sense which sists men", "page": 195, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-10.typ", "anchor": "§4 Paul: some having put away a good conscience", "ccel": "saying, the, “some", "1845": "saying, that “some", "proposed": "saying, that “some", "page": 195, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-10.typ", "anchor": "§6 in expounding the law we have adverted to this subject", "ccel": "(Book 3 chap. 4 sec. 6)", "1845": "(Book III. chap. iv. 5,)", "proposed": "(Book 3 chap. 4 sec. 5) as 1845 prints it (the section number differs; neither obviously fits \"in expounding the law\", which suggests Book 2 chap. 8: for the editor)", "page": 197, "kind": "f", "confidence": "medium (verified)"}
{"file": "book-4-chapter-10.typ", "anchor": "§21 accommodate themselves to their brother", "ccel": "and to not abuse", "1845": "and not to abuse", "proposed": "and not to abuse", "page": 214, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-10.typ", "anchor": "§23 God detests the audacious attempt", "ccel": "no other reasons but", "1845": "no other reason but", "proposed": "no other reason but", "page": 217, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-10.typ", "anchor": "§23 In Jerusalem will I put my name", "ccel": "(2 Kings 22:3, 4)", "1845": "(2 Kings xxi. 3, 4,)", "proposed": "(2 Kings 21:3, 4)", "page": 217, "kind": "f", "confidence": "high"}
{"file": "book-4-chapter-10.typ", "anchor": "§25 Samuel sacrificed in Ramath", "ccel": "(l Sam 7:17)", "1845": "(1 Sam. vii. 17,)", "proposed": "(1 Sam. 7:17)", "page": 218, "kind": "f", "confidence": "high (verified)"}
{"file": "book-4-chapter-10.typ", "anchor": "note (tel a eté le sens de cette distinction vulgaire)", "ccel": "common distincti has", "1845": "common distinction which has", "proposed": "common distinction which has", "page": 196, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-11.typ", "anchor": "§10 those bishops who abused the goodness of princes", "ccel": "bishops who abuse the", "1845": "bishops who abused the", "proposed": "bishops who abused the", "page": 239, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-11.typ", "anchor": "§11 Bernard is speaking of civil judgments", "ccel": "Bernard is spearing", "1845": "Bernard is speaking", "proposed": "Bernard is speaking", "page": 239, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-12.typ", "anchor": "§3 But as our Saviour is not there speaking of secret faults", "ccel": "Put as our Saviour", "1845": "But as our Saviour", "proposed": "But as our Saviour", "page": 249, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-12.typ", "anchor": "§5 the Lord's Supper, which might be profaned", "ccel": "might he profaned", "1845": "might be profaned", "proposed": "might be profaned", "page": 251, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-12.typ", "anchor": "§11 Augustine contra Parmen.: excludes what he cannot correct", "ccel": "or unjustly condemns", "1845": "or justly condemns", "proposed": "or justly condemns", "page": 257, "kind": "d", "confidence": "high (verified)"}
{"file": "book-4-chapter-12.typ", "anchor": "§15 when the mind is affected as it ought", "ccel": "mind is effected", "1845": "mind is affected", "proposed": "mind is affected", "page": 261, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-12.typ", "anchor": "§20 the vulgar imagined that they thereby performed", "ccel": "thereby perform some", "1845": "thereby performed some", "proposed": "thereby performed some", "page": 264, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-12.typ", "anchor": "§22 these good successors did not abrogate", "ccel": "abrograte", "1845": "abrogate", "proposed": "abrogate", "page": 268, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-12.typ", "anchor": "note (J’use de ce mot de Clercs)", "ccel": "mot de Cleres", "1845": "mot de Clercs", "proposed": "mot de Clercs", "page": 248, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "§2 to whom, what, with what intention we vow", "ccel": "In regard in the first", "1845": "In regard to the first", "proposed": "In regard to the first", "page": 275, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "§2 will-worship, how specious and splendid soever", "ccel": "soever it be in the eyes", "1845": "soever it may be in the eyes", "proposed": "soever it may be in the eyes", "page": 275, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "§10 if you take away their idleness", "ccel": "where will that contemplative", "1845": "where will be that contemplative", "proposed": "where will be that contemplative", "page": 285, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "§12 monasticism, as it now exists, is founded", "ccel": "as it now exists, founded", "1845": "as it now exists, is founded", "proposed": "as it now exists, is founded", "page": 287, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "§13 if the sum of perfection consists in this", "ccel": "sum off perfection", "1845": "sum of perfection", "proposed": "sum of perfection", "page": 288, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "§14 Still there was nothing which the Fathers less intended", "ccel": "nothing with the Fathers", "1845": "nothing which the Fathers", "proposed": "nothing which the Fathers", "page": 289, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "§17 Cyprian: if virgins have dedicated themselves to Christ in faith", "ccel": "themselves to Christian faith", "1845": "themselves to Christ in faith", "proposed": "themselves to Christ in faith", "page": 293, "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "§18 those widows who were then admitted to a public ministry", "ccel": "widows who were admitted", "1845": "widows who were then admitted", "proposed": "widows who were then admitted", "page": 294, "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "note (On the vow of celibacy, see Calv.)", "ccel": "celibacy. see", "1845": "celibacy, see", "proposed": "celibacy, see", "page": 277, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "note (Latin, Catechismo)", "ccel": "“Catechism.”", "1845": "“Catechismo.”", "proposed": "“Catechismo.”", "page": 280, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "note (Bernard. ad Guliel. Abbat.)", "ccel": "Abbat..", "1845": "Abbat.", "proposed": "Abbat.", "page": 291, "kind": "n", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "Sections 28 (the item lacks the stop after its number, so it is not set as item 28)", "ccel": "28 Objection, that", "1845": "28. Objection, that", "proposed": "28\\. Objection, that", "page": 9, "kind": "f", "confidence": "high"}
```
