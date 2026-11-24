# Calvin, Institutes, vol. 3 (Book III, Argument and chapters 1–10): Classic re-checked against the 1845 printing (Kraken OCR)

Base: `chapters/typ/vol-3/*.typ` in the `wt-institutes` worktree (book-3-argument + chapters 1–10; read only).
Witness: Calvin Translation Society, Edinburgh 1845, our own scans, Kraken OCR with ALTO beside it, page images `pages/p-NNNN.png`.
Book III ch. 1–10 lies wholly in **1845 vol. 2, pp. 83–299** (`work/institutes/vol2/kraken/`, image = printed page + 10,
images 93–309): the Book III title page is p. 83 (image 93), the SUBJECT p. 84, ch. 1 begins p. 85, and ch. 10 ends p. 299
(image 309, “…a splendour and value in the eye of God.”); ch. 11 begins p. 300 (image 310). 1845 vol. 3 is not needed. In the
**p.** column **II.n** is a page of 1845 vol. 2 (as in the vol. 2 report).
Method (as vols 1 and 2): every .typ file was aligned word by word with the Kraken text (difflib; main text first, then the
footnotes against the OCR words the main text left over; running heads dropped; line-end hyphens joined). Differences were
filtered for reference style (Roman → Arabic compared as numbers), American spelling and OCR noise; then every remaining
candidate (214 word and 64 reference rows, 21 capital-letter rows, 21 long runs) was read on the page image (line crops from the
ALTO boxes, contact sheets `g1.png`, `g2.png`, `w1.png`, `w2.png`, `k1.png`–`k3.png`, `gr.png`, `gr2.png`, `p1.png`, `x1.png`, `z.png`).
Every reference left unmatched in the OCR was also checked against the CCEL text (`refcheck.py`), which is how the one
missing footnote was found. Only what the image confirms is listed.
Scripts and raw candidates: `work/institutes/latin/vol3/recheck/` (`align.py`, `filter.py`, `refcheck.py`, `crop.py`,
`mkbatch.py`, `batch.sh`, `cand.json`, `cand.tsv`, `cand2.tsv`, `cases.tsv`, `residual.txt`, `grammar_rows.tsv`,
`build_report.py`, `apply-input.jsonl`, `manual-edits.json`).

**Rule applied (editor, 2026-11-23):** the Classic follows the 1845 print wherever CCEL's wording departs from it, including
CCEL's modernised grammar in Scripture quotations (kind **d/grammar**). Not listed: Arabic reference style, American spelling
(1845 forms: stedfast, practise, recognising, cognisance, apologising, philosophising, sepulchre, meagre, apostacy, hinderance, ingulf, axe,
stupified, neighbour, counseller, vitious, pœnitentiary…), CCEL's punctuation around references, CCEL's word joins, Greek
accents. The `proposed` column holds only the replacement words; explanations are in the anchor and kind columns; an empty
`proposed` means no change to the text (misprint-1845).

**Kinds:** b (1845 words missing in CCEL), d (a different word), d/grammar (CCEL's modernised verb form), d/case (capital
letter differs from the print), n (notes), misprint-1845 (the 1845 print is wrong; CCEL corrects or shares it).

**Counts:** b 2, d 4, d/case 14, d/grammar 43, misprint-1845 12, n 4 (total 79).

**Systematic check.** Nothing like vol-1's “Judgment”: vol-3 has no mid-sentence capital *Judgment*, and the capital
comparison (every aligned word whose first letter differs in case) gives only 21 rows, all single places (14 listed; the rest
below). The one repeated pattern is again CCEL's has/does for hath/doth in Scripture quotations and Calvin's own sentences
(43 places: 41 has → hath, 2 does → doth). No keying slip recurs; the word slips are all single (fulness for *fatness*,
Homily. for *Homil.*, Paenitentia for *Pœnitentia*; in the notes conterolleurs, recognoissent, Ps 1 for *Psal. l.* = Ps 50,
Augustine for *Augustin.*). Twelve 1845 misprints (mostly reference numbers) are listed so that nobody “restores” them.

**Also seen, not listed:** 1845 lower case after “?” where CCEL starts a capital (II.204 “? cleanse thou me”, Ps 19:12;
II.219 “? how do they still dare”); CCEL “lib.” for 1845 “Lib.” (II.97 De Civitate Dei) and “pœnit.” for “Pœnit.”
in Gratian/Chrysostom references (II.186, II.195); CCEL “Book 4 Chap 1 sec. 29” (1845 “chap.”); “the 119th Psalm” and “the
29th chapter” (1845 “cxix.”, “xxixth”: reference style); Latin/French ligatures and small punctuation in notes (1845 “aere
alien.”, CCEL “ære”; 1845 “paene”, CCEL “pæne”; 1845 “Ecclesiæ Catholicæ”, CCEL “Ecclesiae Catholicae”; 1845
“De Incomprehensibili Dei Nat.”, CCEL “Dei. Nat.”; 1845 “quils”, CCEL “qu’ils”); CCEL “for sooth” (II.190, 1845
“forsooth”: a CCEL word split, left with the word joins); Argument III, 1845 “Repentance, viz., mortification”, CCEL
“Repentance—viz. mortification” (punctuation).

**Structural:** one Beveridge footnote is missing in CCEL: ch. 7 §5, after “the offerings under the Law.”, 1845 has note 1
“Heb. xiii. 16; 2 Cor. ix. 12.” (II.266; listed, kind b). Every other OCR run left unmatched after both passes was checked:
all are references present in CCEL in Arabic form, running heads, signatures and the Book III title page. No CCEL line is
absent from 1845. The Book III title is cut short (first row: 1845 adds “the benefits it confers, and the effects resulting from
it”; `institutes-vol-3.typ` holds it, not a chapter file), and 1845 heads Book III's opening summary “SUBJECT.” as it did
Book II's (listed, as in vol. 2).


## Book III title — `institutes-vol-3.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Book III title (heading in institutes-vol-3.typ; the subtitle on line 12 and the cover may follow) | = Book Third: The Mode of Obtaining the Grace of Christ | BOOK THIRD. THE MODE OF OBTAINING THE GRACE OF CHRIST. THE BENEFITS IT CONFERS, AND THE EFFECTS RESULTING FROM IT. | = Book Third: The Mode of Obtaining the Grace of Christ, the Benefits It Confers, and the Effects Resulting from It | II.83 | b | medium |

## book-3-argument — `book-3-argument.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| heading of the opening summary (1845 heads Books II and III “SUBJECT.”, Book I “ARGUMENT.”) | == Argument | SUBJECT. | == Subject | II.84 | d | medium |

## Book III, chapter 01 — `book-3-chapter-01.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 1 Cor 6:11 | says, “but ye | says, “But ye | But | II.87 | d/case | high |
| §4 Matt 16:17 | blood has | blood hath | hath | II.90 | d/grammar | high |
| §4 2 Thess 2:13 | “God has | “God hath | hath | II.90 | d/grammar | high |
| §4 | he has given us;” | he hath given us;” | hath | II.90 | d/grammar | high |
| §4 1 John 3:24 | he has given us of | he hath given us of | hath | II.90 | d/grammar | high |

## Book III, chapter 02 — `book-3-chapter-02.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 | he has sent. | he hath sent. | hath | II.96 | d/grammar | high |
| §3 only with the appended condition, If such is the faith | condition, if such | condition, If such | If | II.98 | d/case | high |
| note (Augustine, Latin): possunt ista discernere [keep CCEL (Latin)] | discernere, pæne | discernera, paene |  | II.99 | misprint-1845 | - |
| §12 Matt 15:13 | Father has | Father hath | hath | II.111 | d/grammar | high |
| §13 in the same Epistle where Paul enjoins the deacons | same epistle where | same Epistle where | Epistle | II.111 | d/case | high |
| §12 Matt 15:13 “Every plant which my heavenly Father hath not planted” [keep CCEL] | (Matt 15:13) | (Matth. xvi. 13.) |  | II.111 | misprint-1845 | - |
| §13 Col 2:3 “treasures of wisdom and knowledge” [keep CCEL; 1845's chapter is wrong] | (Col 2:3) | (Col. i. 2, 3,) |  | II.112 | misprint-1845 | - |
| note (God's word called faith): 2 Tim 3:8 [keep CCEL (2 Tim 3 has 17 verses)] | 2 Tim 2:15; 3:8 | 2 Tim. ii. 15; iii. 18 |  | II.112 | misprint-1845 | - |
| §14 | which has been | which hath been | hath | II.113 | d/grammar | high |
| §17 | God: “Has | God: “Hath | Hath | II.117 | d/grammar | high |
| §17 Ps 77:9 | gracious? has | gracious? hath | hath | II.117 | d/grammar | high |
| §27 1 John 4:18 | fear has | fear hath | hath | II.127 | d/grammar | high |
| §28 Ps 33:12 | he has chosen | he hath chosen | hath | II.129 | d/grammar | high |
| §30 Noah, “when as yet it was not seen” [keep CCEL (the verse is Heb 11:7)] | (Heb 11:7) | (Heb. xi. 17.) |  | II.131 | misprint-1845 | - |
| §32 Eph 1:6 | he has made | he hath made | hath | II.135 | d/grammar | high |
| §34 Matt 16:17 | blood” does | blood” doth | doth | II.137 | d/grammar | high |
| §34 Rom 11:34 | who has known | who hath known | hath | II.137 | d/grammar | high |
| §34 Rom 11:34 | who has been | who hath been | hath | II.137 | d/grammar | high |
| §34 | which has sent me draw | which hath sent me draw | hath | II.137 | d/grammar | high |
| §34 John 6:44, 45, 46 | that has | that hath | hath | II.137 | d/grammar | high |
| §34 John 6:44, 45, 46 | man has seen | man hath seen | hath | II.137 | d/grammar | high |
| §34 John 6:44, 45, 46 | he has seen | he hath seen | hath | II.137 | d/grammar | high |
| §35 “the work of faith with power” [keep CCEL (the verse is 2 Thess 1:11)] | (2 Thess 1:11) | (2 Thess. i. 2.) |  | II.138 | misprint-1845 | - |
| §35 John 6:44 | which has sent me, | which hath sent me, | hath | II.139 | d/grammar | high |
| §36 2 Cor 1:22 | “God has | “God hath | hath | II.140 | d/grammar | high |
| §37 in the words of the psalm, “God is our refuge” (Ps 46:1) | the Psalm, “God | the psalm, “God | psalm | II.140 | d/case | high |
| §38 Eccl 9:2 | since “All things | since “all things | all | II.141 | d/case | high |
| §39 1 John 3:24 | he has given us,” | he hath given us,” | hath | II.142 | d/grammar | high |
| §39 But if it is sacrilege to charge | is Sacrilege to | is sacrilege to | sacrilege | II.142 | d/case | high |
| §43 | who has said, | who hath said, | hath | II.148 | d/grammar | high |

## Book III, chapter 03 — `book-3-chapter-03.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Hos 6:1 | he has torn, | he hath torn, | hath | II.153 | d/grammar | high |
| §2 Hos 6:1 | he has smitten, | he hath smitten, | hath | II.153 | d/grammar | high |
| §7 Acts 17:30, 31 | he has appointed | he hath appointed | hath | II.158 | d/grammar | high |
| §13 Jas 1:15 | lust has | lust hath | hath | II.164 | d/grammar | high |
| §15 the Apostle's description of repentance [keep CCEL (the verse is 2 Cor 7:11)] | (2 Cor 7:11) | (2 Cor. vii. 2,) |  | II.166 | misprint-1845 | - |
| note (French): qui veulent testifier quils se recognoissant | se recognoissent avoir | se recognoissant avoir | recognoissant | II.170 | n | medium |
| §19 Matt 3:2 | proclaimed, “repent, | proclaimed, “Repent, | Repent | II.172 | d/case | high |
| §19 Acts 5:31 | “Him has | “Him hath | hath | II.173 | d/grammar | high |
| §21 Acts 11:18 | “Then has | “Then hath | hath | II.175 | d/grammar | high |
| §21 Eph 2:10 | God has | God hath | hath | II.175 | d/grammar | high |
| §22 defamed him by the name of Beelzebub [keep CCEL (1559 Latin: Matth. 9, 34)] | (Matt 9:34; 12:24) | (Matth. ix. 3, 4; xii. 24.) |  | II.178 | misprint-1845 | - |
| §24 | he has committed,” | he hath committed,” | hath | II.180 | d/grammar | high |
| §24 the Prophet means by crying, and the Apostle by tears | the apostle by tears | the Apostle by tears | Apostle | II.180 | d/case | high |
| §25 Gen 27:39 (Esau) should be filled with the fatness of the earth | the fulness of the earth | the fatness of the earth | fatness | II.181 | d | high |

## Book III, chapter 04 — `book-3-chapter-04.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| note: the second (Ambrose) is given in the same place [keep CCEL (1845 drops “in the”)] | is given in the same place | is given same place |  | II.185 | misprint-1845 | - |
| §6 | Scripture has | Scripture hath | hath | II.193 | d/grammar | high |
| note: Eccles. Hist. Lib. 7 cap. 17 (Sozomen) [keep CCEL (CO note to the Latin: Sozomen lib. 7, c. 16)] | Lib. 7 cap. 17 | Lib. viii. cap. 17 |  | II.194 | misprint-1845 | medium |
| note: Chrysost. Hom. 2 in Psal. l. (= Ps 50; CCEL read the Roman l as 1; cf. “Hom. 2 in Ps 50” later in the chapter) | Ps 1.Serm. | Psal. l. Serm. | Ps 50. Serm. | II.195 | n | high |
| §13 Matt 5:23, 24 | brother has | brother hath | hath | II.200 | d/grammar | high |
| §18 Ezek 18:21 | he has committed, and keep | he hath committed, and keep | hath | II.207 | d/grammar | high |
| §22 ask at these good doctors, Whether the sinner is reconciled | doctors, whether | doctors, Whether | Whether | II.212 | d/case | high |
| note (French): si les prestres se faisoyent contrerolleurs de Dieu | faisoyent conterolleurs | faisoyent contrerolleurs | contrerolleurs | II.213 | n | high |
| §25 2 Cor 5:19, 20 | he has made | he hath made | hath | II.215 | d/grammar | high |
| §29 | he has done shall | he hath done shall | hath | II.220 | d/grammar | high |
| §29 Ezek 18:24, 27 | he has committed, and does | he hath committed, and does | hath | II.220 | d/grammar | high |
| §29 Ezek 18:24, 27 | and does that | and doth that | doth | II.220 | d/grammar | high |
| §31 Prov 16:6 | says, “by mercy | says, “By mercy | By | II.223 | d/case | high |
| §34 in short, can never persuade himself | short, Can never | short, can never | can | II.228 | d/case | high |
| §35 (Chrysos. Homil. iii. de Provid.) | (Chrysos. Homily. 3 | (Chrysos. Homil. iii. | Homil. | II.229 | d | medium |
| §35 (Calvin's sentence: our infinitely wise Parent hath seen it meet) | Parent has | Parent hath | hath | II.230 | d/grammar | high |
| §36 (see Calv. in Harm. Evang.) | Calv. In Harm. | Calv. in Harm. | in | II.231 | d/case | high |
| §37 | faith has | faith hath | hath | II.232 | d/grammar | high |
| §39 extracts are from the book of Augustine De Pœnitentia | #emph[De Paenitentia] | De Pœnitentia (italic) | Pœnitentia | II.234 | d | medium |

## Book III, chapter 05 — `book-3-chapter-05.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 | “He has | “He hath | hath | II.238 | d/grammar | high |
| §2 Heb 10:14 | he has perfected | he hath perfected | hath | II.238 | d/grammar | high |
| §5 2 Cor 5:20, 21 | he has made | he hath made | hath | II.241 | d/grammar | high |
| §8 the history of the Maccabees [keep CCEL (the verse is 2 Macc 12:43)] | (2 Macc. 12:43) | (1 Maccab. xii. 43,) |  | II.245 | misprint-1845 | - |
| §10 solid comfort is furnished by Scripture | by scripture when | by Scripture when | Scripture | II.249 | d/case | high |

## Book III, chapter 07 — `book-3-chapter-07.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| note: see Augustin. De Moribus Ecclesiae Catholicae | see Augustine, De | see Augustin. De | Augustin. | II.259 | n | medium |
| §5 note missing after “the offerings under the Law.” (1845 footnote 1: Heb. xiii. 16; 2 Cor. ix. 12.) | corresponding to the offerings under the Law. | corresponding to the offerings under the Law.¹ [note: Heb. xiii. 16; 2 Cor. ix. 12.] | Law.#footnote[Heb 13:16; 2 Cor 9:12.] | II.266 | b | high |

## Book III, chapter 08 — `book-3-chapter-08.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Ps 30:6 | I Said, I | I said, I | said | II.275 | d/case | high |
| §4 God tempted Abraham [1845 and CCEL both; the passage is Gen 22:1, 12 if the editor fixes plain misprints] | (Gen 21:1, 12) | (Gen. xxi. 1, 12,) |  | II.277 | misprint-1845 | medium |

## Findings (one JSON line each)

```
{"file": "/home/courtney/Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion/institutes-vol-3.typ", "anchor": "Book III title (heading in institutes-vol-3.typ; the subtitle on line 12 and the cover may follow)", "ccel": "= Book Third: The Mode of Obtaining the Grace of Christ", "1845": "BOOK THIRD. THE MODE OF OBTAINING THE GRACE OF CHRIST. THE BENEFITS IT CONFERS, AND THE EFFECTS RESULTING FROM IT.", "proposed": "= Book Third: The Mode of Obtaining the Grace of Christ, the Benefits It Confers, and the Effects Resulting from It", "page": "II.83", "kind": "b", "confidence": "medium"}
{"file": "book-3-argument.typ", "anchor": "heading of the opening summary (1845 heads Books II and III “SUBJECT.”, Book I “ARGUMENT.”)", "ccel": "== Argument", "1845": "SUBJECT.", "proposed": "== Subject", "page": "II.84", "kind": "d", "confidence": "medium"}
{"file": "book-3-chapter-01.typ", "anchor": "§1 1 Cor 6:11", "ccel": "says, “but ye", "1845": "says, “But ye", "proposed": "But", "page": "II.87", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-01.typ", "anchor": "§4 Matt 16:17", "ccel": "blood has", "1845": "blood hath", "proposed": "hath", "page": "II.90", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-01.typ", "anchor": "§4 2 Thess 2:13", "ccel": "“God has", "1845": "“God hath", "proposed": "hath", "page": "II.90", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-01.typ", "anchor": "§4", "ccel": "he has given us;”", "1845": "he hath given us;”", "proposed": "hath", "page": "II.90", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-01.typ", "anchor": "§4 1 John 3:24", "ccel": "he has given us of", "1845": "he hath given us of", "proposed": "hath", "page": "II.90", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§1", "ccel": "he has sent.", "1845": "he hath sent.", "proposed": "hath", "page": "II.96", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§3 only with the appended condition, If such is the faith", "ccel": "condition, if such", "1845": "condition, If such", "proposed": "If", "page": "II.98", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "note (Augustine, Latin): possunt ista discernere [keep CCEL (Latin)]", "ccel": "discernere, pæne", "1845": "discernera, paene", "proposed": "", "page": "II.99", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-02.typ", "anchor": "§12 Matt 15:13", "ccel": "Father has", "1845": "Father hath", "proposed": "hath", "page": "II.111", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§13 in the same Epistle where Paul enjoins the deacons", "ccel": "same epistle where", "1845": "same Epistle where", "proposed": "Epistle", "page": "II.111", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§12 Matt 15:13 “Every plant which my heavenly Father hath not planted” [keep CCEL]", "ccel": "(Matt 15:13)", "1845": "(Matth. xvi. 13.)", "proposed": "", "page": "II.111", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-02.typ", "anchor": "§13 Col 2:3 “treasures of wisdom and knowledge” [keep CCEL; 1845's chapter is wrong]", "ccel": "(Col 2:3)", "1845": "(Col. i. 2, 3,)", "proposed": "", "page": "II.112", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-02.typ", "anchor": "note (God's word called faith): 2 Tim 3:8 [keep CCEL (2 Tim 3 has 17 verses)]", "ccel": "2 Tim 2:15; 3:8", "1845": "2 Tim. ii. 15; iii. 18", "proposed": "", "page": "II.112", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-02.typ", "anchor": "§14", "ccel": "which has been", "1845": "which hath been", "proposed": "hath", "page": "II.113", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§17", "ccel": "God: “Has", "1845": "God: “Hath", "proposed": "Hath", "page": "II.117", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§17 Ps 77:9", "ccel": "gracious? has", "1845": "gracious? hath", "proposed": "hath", "page": "II.117", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§27 1 John 4:18", "ccel": "fear has", "1845": "fear hath", "proposed": "hath", "page": "II.127", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§28 Ps 33:12", "ccel": "he has chosen", "1845": "he hath chosen", "proposed": "hath", "page": "II.129", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§30 Noah, “when as yet it was not seen” [keep CCEL (the verse is Heb 11:7)]", "ccel": "(Heb 11:7)", "1845": "(Heb. xi. 17.)", "proposed": "", "page": "II.131", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-02.typ", "anchor": "§32 Eph 1:6", "ccel": "he has made", "1845": "he hath made", "proposed": "hath", "page": "II.135", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§34 Matt 16:17", "ccel": "blood” does", "1845": "blood” doth", "proposed": "doth", "page": "II.137", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§34 Rom 11:34", "ccel": "who has known", "1845": "who hath known", "proposed": "hath", "page": "II.137", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§34 Rom 11:34", "ccel": "who has been", "1845": "who hath been", "proposed": "hath", "page": "II.137", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§34", "ccel": "which has sent me draw", "1845": "which hath sent me draw", "proposed": "hath", "page": "II.137", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§34 John 6:44, 45, 46", "ccel": "that has", "1845": "that hath", "proposed": "hath", "page": "II.137", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§34 John 6:44, 45, 46", "ccel": "man has seen", "1845": "man hath seen", "proposed": "hath", "page": "II.137", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§34 John 6:44, 45, 46", "ccel": "he has seen", "1845": "he hath seen", "proposed": "hath", "page": "II.137", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§35 “the work of faith with power” [keep CCEL (the verse is 2 Thess 1:11)]", "ccel": "(2 Thess 1:11)", "1845": "(2 Thess. i. 2.)", "proposed": "", "page": "II.138", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-02.typ", "anchor": "§35 John 6:44", "ccel": "which has sent me,", "1845": "which hath sent me,", "proposed": "hath", "page": "II.139", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§36 2 Cor 1:22", "ccel": "“God has", "1845": "“God hath", "proposed": "hath", "page": "II.140", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§37 in the words of the psalm, “God is our refuge” (Ps 46:1)", "ccel": "the Psalm, “God", "1845": "the psalm, “God", "proposed": "psalm", "page": "II.140", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§38 Eccl 9:2", "ccel": "since “All things", "1845": "since “all things", "proposed": "all", "page": "II.141", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§39 1 John 3:24", "ccel": "he has given us,”", "1845": "he hath given us,”", "proposed": "hath", "page": "II.142", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§39 But if it is sacrilege to charge", "ccel": "is Sacrilege to", "1845": "is sacrilege to", "proposed": "sacrilege", "page": "II.142", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-02.typ", "anchor": "§43", "ccel": "who has said,", "1845": "who hath said,", "proposed": "hath", "page": "II.148", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§2 Hos 6:1", "ccel": "he has torn,", "1845": "he hath torn,", "proposed": "hath", "page": "II.153", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§2 Hos 6:1", "ccel": "he has smitten,", "1845": "he hath smitten,", "proposed": "hath", "page": "II.153", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§7 Acts 17:30, 31", "ccel": "he has appointed", "1845": "he hath appointed", "proposed": "hath", "page": "II.158", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§13 Jas 1:15", "ccel": "lust has", "1845": "lust hath", "proposed": "hath", "page": "II.164", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§15 the Apostle's description of repentance [keep CCEL (the verse is 2 Cor 7:11)]", "ccel": "(2 Cor 7:11)", "1845": "(2 Cor. vii. 2,)", "proposed": "", "page": "II.166", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-03.typ", "anchor": "note (French): qui veulent testifier quils se recognoissant", "ccel": "se recognoissent avoir", "1845": "se recognoissant avoir", "proposed": "recognoissant", "page": "II.170", "kind": "n", "confidence": "medium"}
{"file": "book-3-chapter-03.typ", "anchor": "§19 Matt 3:2", "ccel": "proclaimed, “repent,", "1845": "proclaimed, “Repent,", "proposed": "Repent", "page": "II.172", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§19 Acts 5:31", "ccel": "“Him has", "1845": "“Him hath", "proposed": "hath", "page": "II.173", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§21 Acts 11:18", "ccel": "“Then has", "1845": "“Then hath", "proposed": "hath", "page": "II.175", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§21 Eph 2:10", "ccel": "God has", "1845": "God hath", "proposed": "hath", "page": "II.175", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§22 defamed him by the name of Beelzebub [keep CCEL (1559 Latin: Matth. 9, 34)]", "ccel": "(Matt 9:34; 12:24)", "1845": "(Matth. ix. 3, 4; xii. 24.)", "proposed": "", "page": "II.178", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-03.typ", "anchor": "§24", "ccel": "he has committed,”", "1845": "he hath committed,”", "proposed": "hath", "page": "II.180", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§24 the Prophet means by crying, and the Apostle by tears", "ccel": "the apostle by tears", "1845": "the Apostle by tears", "proposed": "Apostle", "page": "II.180", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-03.typ", "anchor": "§25 Gen 27:39 (Esau) should be filled with the fatness of the earth", "ccel": "the fulness of the earth", "1845": "the fatness of the earth", "proposed": "fatness", "page": "II.181", "kind": "d", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: the second (Ambrose) is given in the same place [keep CCEL (1845 drops “in the”)]", "ccel": "is given in the same place", "1845": "is given same place", "proposed": "", "page": "II.185", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-04.typ", "anchor": "§6", "ccel": "Scripture has", "1845": "Scripture hath", "proposed": "hath", "page": "II.193", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Eccles. Hist. Lib. 7 cap. 17 (Sozomen) [keep CCEL (CO note to the Latin: Sozomen lib. 7, c. 16)]", "ccel": "Lib. 7 cap. 17", "1845": "Lib. viii. cap. 17", "proposed": "", "page": "II.194", "kind": "misprint-1845", "confidence": "medium"}
{"file": "book-3-chapter-04.typ", "anchor": "note: Chrysost. Hom. 2 in Psal. l. (= Ps 50; CCEL read the Roman l as 1; cf. “Hom. 2 in Ps 50” later in the chapter)", "ccel": "Ps 1.Serm.", "1845": "Psal. l. Serm.", "proposed": "Ps 50. Serm.", "page": "II.195", "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§13 Matt 5:23, 24", "ccel": "brother has", "1845": "brother hath", "proposed": "hath", "page": "II.200", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§18 Ezek 18:21", "ccel": "he has committed, and keep", "1845": "he hath committed, and keep", "proposed": "hath", "page": "II.207", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§22 ask at these good doctors, Whether the sinner is reconciled", "ccel": "doctors, whether", "1845": "doctors, Whether", "proposed": "Whether", "page": "II.212", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "note (French): si les prestres se faisoyent contrerolleurs de Dieu", "ccel": "faisoyent conterolleurs", "1845": "faisoyent contrerolleurs", "proposed": "contrerolleurs", "page": "II.213", "kind": "n", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§25 2 Cor 5:19, 20", "ccel": "he has made", "1845": "he hath made", "proposed": "hath", "page": "II.215", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§29", "ccel": "he has done shall", "1845": "he hath done shall", "proposed": "hath", "page": "II.220", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§29 Ezek 18:24, 27", "ccel": "he has committed, and does", "1845": "he hath committed, and does", "proposed": "hath", "page": "II.220", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§29 Ezek 18:24, 27", "ccel": "and does that", "1845": "and doth that", "proposed": "doth", "page": "II.220", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§31 Prov 16:6", "ccel": "says, “by mercy", "1845": "says, “By mercy", "proposed": "By", "page": "II.223", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§34 in short, can never persuade himself", "ccel": "short, Can never", "1845": "short, can never", "proposed": "can", "page": "II.228", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§35 (Chrysos. Homil. iii. de Provid.)", "ccel": "(Chrysos. Homily. 3", "1845": "(Chrysos. Homil. iii.", "proposed": "Homil.", "page": "II.229", "kind": "d", "confidence": "medium"}
{"file": "book-3-chapter-04.typ", "anchor": "§35 (Calvin's sentence: our infinitely wise Parent hath seen it meet)", "ccel": "Parent has", "1845": "Parent hath", "proposed": "hath", "page": "II.230", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§36 (see Calv. in Harm. Evang.)", "ccel": "Calv. In Harm.", "1845": "Calv. in Harm.", "proposed": "in", "page": "II.231", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§37", "ccel": "faith has", "1845": "faith hath", "proposed": "hath", "page": "II.232", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-04.typ", "anchor": "§39 extracts are from the book of Augustine De Pœnitentia", "ccel": "#emph[De Paenitentia]", "1845": "De Pœnitentia (italic)", "proposed": "Pœnitentia", "page": "II.234", "kind": "d", "confidence": "medium"}
{"file": "book-3-chapter-05.typ", "anchor": "§2", "ccel": "“He has", "1845": "“He hath", "proposed": "hath", "page": "II.238", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§2 Heb 10:14", "ccel": "he has perfected", "1845": "he hath perfected", "proposed": "hath", "page": "II.238", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§5 2 Cor 5:20, 21", "ccel": "he has made", "1845": "he hath made", "proposed": "hath", "page": "II.241", "kind": "d/grammar", "confidence": "high"}
{"file": "book-3-chapter-05.typ", "anchor": "§8 the history of the Maccabees [keep CCEL (the verse is 2 Macc 12:43)]", "ccel": "(2 Macc. 12:43)", "1845": "(1 Maccab. xii. 43,)", "proposed": "", "page": "II.245", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-3-chapter-05.typ", "anchor": "§10 solid comfort is furnished by Scripture", "ccel": "by scripture when", "1845": "by Scripture when", "proposed": "Scripture", "page": "II.249", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-07.typ", "anchor": "note: see Augustin. De Moribus Ecclesiae Catholicae", "ccel": "see Augustine, De", "1845": "see Augustin. De", "proposed": "Augustin.", "page": "II.259", "kind": "n", "confidence": "medium"}
{"file": "book-3-chapter-07.typ", "anchor": "§5 note missing after “the offerings under the Law.” (1845 footnote 1: Heb. xiii. 16; 2 Cor. ix. 12.)", "ccel": "corresponding to the offerings under the Law.", "1845": "corresponding to the offerings under the Law.¹ [note: Heb. xiii. 16; 2 Cor. ix. 12.]", "proposed": "Law.#footnote[Heb 13:16; 2 Cor 9:12.]", "page": "II.266", "kind": "b", "confidence": "high"}
{"file": "book-3-chapter-08.typ", "anchor": "§2 Ps 30:6", "ccel": "I Said, I", "1845": "I said, I", "proposed": "said", "page": "II.275", "kind": "d/case", "confidence": "high"}
{"file": "book-3-chapter-08.typ", "anchor": "§4 God tempted Abraham [1845 and CCEL both; the passage is Gen 22:1, 12 if the editor fixes plain misprints]", "ccel": "(Gen 21:1, 12)", "1845": "(Gen. xxi. 1, 12,)", "proposed": "", "page": "II.277", "kind": "misprint-1845", "confidence": "medium"}
```

## Applied (2026-11-23)

All 65 rows of apply-input.jsonl and the 3 manual edits were applied (`work/institutes/latin/vol3/recheck/apply_recheck.py`), and the word-level diff was read: 67 changes, exactly the rows. By hand: "see Augustin. De" (no comma after "Augustin."). The Book III title is in full, as 1845 prints it (`BOOK_TITLES` in editorial.py), as Book II's is. Not taken, for consistency with the rest of the book: "SUBJECT." for the Argument heading (Book II keeps "Argument" too), and "De Pœnitentia" (the ligature, house style as elsewhere).
