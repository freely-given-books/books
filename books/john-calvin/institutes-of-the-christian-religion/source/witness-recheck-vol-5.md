# Calvin, Institutes, vol. 5 (Book IV, argument and chapters 1–13): Classic re-checked against the 1845 printing (Kraken OCR)

Base: `chapters/typ/vol-5/*.typ` in the `wt-institutes` worktree (book-4-argument, book-4-chapter-01 … book-4-chapter-13;
read only; HEAD ba56bf7c). Witness: Calvin Translation Society, Edinburgh 1845, our own scans, Kraken OCR with ALTO beside it,
page images `pages/p-NNNN.png`. Book IV argument and ch. 1–13 lie wholly in **1845 vol. 3, pp. 6–298**
(`work/institutes/vol3/kraken/`, image = printed page + 4, images 10–302): image 9 is the half-title “BOOK FOURTH. OF THE
HOLY CATHOLIC CHURCH.”, the Argument is p. 6 (image 10), ch. 1 begins p. 7 (image 11), ch. 13 begins p. 273 (image 277) and
ends p. 298 (image 302, “…but binds himself by an oath to despise it?”); ch. 14 begins p. 299 (image 303). In the **p.**
column **III.n** is a page of 1845 vol. 3.
Method (as vol. 4, same scripts adapted): every .typ file was aligned word by word with the Kraken text (difflib; main text
first, then the footnotes against the OCR words the main text left over; running heads dropped; line-end hyphens joined).
Differences were filtered for reference style (Roman → Arabic compared as numbers), American spelling and OCR noise; then
every remaining candidate (189 word and 42 reference rows, 18 capital-letter rows, 14 long runs) was read, and every one
that was not plain OCR noise was checked on the page image (line crops from the ALTO boxes: `w1.png`–`w4.png`, `r1.png`–`r3.png`,
`cs1.png`, `cs2.png`, `gk.png` (the Greek), single crops in `crops/`). Every reference left unmatched in the OCR was checked
against the CCEL text of its own chapter (`refcheck.py`), every OCR run of two or more words left unmatched was read, and the
footnotes were counted chapter by chapter (`notecount.py`) and page by page (`notepages.py`) against CCEL's; every difference
in the counts was traced. Only what the image confirms is listed.
Scripts and raw candidates: `work/institutes/latin/vol5/recheck/` (`align.py`, `filter.py`, `refcheck.py`, `notepages.py`,
`notecount.py`, `crop.py`, `mkbatch.py`, `batch.sh`, `cand.json`, `cand.tsv`, `cand2.tsv`, `cases.tsv`, `residual.txt`,
`build_report.py`, `apply-input.jsonl`, `manual-edits.json`, `apply_recheck.py`).

**Rule applied (editor, 2026-11-23):** the Classic follows the 1845 print wherever CCEL's wording departs from it, including
CCEL's modernised grammar (kind **d/grammar**) and CCEL additions (kind **c**). Not listed: Arabic reference style, American
spelling (1845 forms: honour, despatch, cognisance, stedfast/stedfastly, practise/practised, immoveable, dogmatising,
catechising, styes, vitious…), CCEL's punctuation around references, CCEL's word joins (1845 “any thing”, “every where”,
“every thing”), Greek accents. The `proposed` column holds only the replacement words; explanations are in the anchor and
kind columns; an empty `proposed` means no change to the text (misprint-1845). Where a row needs more than one word changed,
or words added, `proposed` holds the whole replacement snippet and the change is in `manual-edits.json`.

**Kinds:** b (1845 words missing in CCEL), c (CCEL words absent from 1845), d (a different word), d/grammar (CCEL's
modernised verb form), d/case (capital letter differs from the print), n (notes), misprint-1845 (the 1845 print is wrong;
CCEL corrects it).

**Counts:** b 2, d 9, d/case 18, misprint-1845 5 (total 34); no rows of kind c, d/grammar or n.

**Systematic check.** Unlike vol. 4 there is **no modernised grammar** here: the -th forms agree word for word (the
OCR of pp. 6–298 and the fourteen .typ files alike give has 284, Has 1, hath 11, Hath 1, does 96, Does 10, saith 11, cometh 3,
goeth 1, maketh 2), and the aligner found no has/hath, does/doth or comes/cometh pair. Beveridge's Book IV writes “has” and “does” in
Calvin's own sentences, and CCEL keeps every -th form the print has. The one repeated word pattern is the print's
**“an” before u- and h-** (an unity, an universal ×4, an useful, an hundred), which CCEL has modernised to “a” in all seven
places (kind d). The two kind-b rows are the print's “that that” (III.71, III.120), which CCEL reduced to one “that”; both
read correctly as printed (“so that that ordination was just”, “confess that that arrangement was preposterous”). The capital
comparison (every aligned word whose first letter differs in case) gives 18 rows: 17 are listed, one
(III.176 “the Old Testament”) is an OCR misreading; the eighteenth d/case row is the Greek οὐκ (III.116), lower-case in the print. Otherwise the word slips are single (insure for *ensure*, and the cross-
reference “Book III. chap. iv. 5” given as sec. 6). CCEL adds nothing to the text that the print lacks (no kind c), and none
of the vol. 4 additions (glosses, Scripture references) recur. Five 1845 misprints are listed so that nobody “restores” them.
This volume had already been checked against 1845 once (`b91e83b4`, 75 findings, and the typesetting sweep `99808b6f`), which
is why so little is left.

**Also seen, not listed:** CCEL “Mt.” for 1845 “Matth.” in two Father references (III.48 “Lib. Quæst. in Evang. Matth.”,
III.251 “Hom. 83, in Matth.”) and “Chapter 3.”… for “Chap. III.”… in the Argument's chapter list (reference style); the
footnote at III.36 (“Gen 37:18, 28; … 2 Sam 11:4, 15; xii 13.”), where CCEL's last reference is still Roman (1845 “xii. 13”;
modern style would be **12:13**, a style fix for the reference sweep, not a wording change); Luke 11:16 for “touch … with one
of your fingers” (III.192): **1845 and CCEL both** print xi. 16 / 11:16, where the verse is Luke 11:46 (the Classic already
follows the print; a correction would be an editorial choice); 1845 “ceux-la” in the French note at III.170 (CCEL “ceux la”,
punctuation); Greek accents (1845 ἀγαθὸν, πολυκοιρανίη; CCEL unaccented); the half-title “BOOK FOURTH. OF THE HOLY CATHOLIC
CHURCH.” (structural, as our volume sets it); spellings in the rule above.

**Structural:** no Beveridge footnote is missing in vol. 5 and none is added: chapters 2, 7–11 and 13 give the same count in
1845 and CCEL; the differences in ch. 1, 3, 4, 5, 6 and 12 were notes whose first line the counter missed (a note marked “*”
or “«”, or a note line run into a reference, as “11 Sam. vii. 6” for “¹ 1 Sam. vii. 6”); each was found on its page (III.27,
III.36, III.57, III.75, III.95, III.117, III.262 …), and the note texts agree. Every OCR run left unmatched after both passes
is a reference present in CCEL in Arabic form (`refcheck.py` flags only OCR misreadings and the listed misprints), a running
head, a signature (“VOL. III.”) or the half-title; one line Kraken skipped (III.77, “of the Church. But if, disregarding the
term, we look to the”) is in the print. No CCEL line is absent from 1845 and no 1845 line from CCEL; the chapter titles and the
Sections lists agree (capitals apart, listed).


## Book IV, argument — `book-4-argument.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| The first head occupies the first thirteen Chapters | thirteen chapters; but | thirteen Chapters; but | Chapters | III.6 | d/case | high |

## Book IV, chapter 1 — `book-4-chapter-01.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 1. The Church now to be considered | The church now to | The Church now to | Church | III.7 | d/case | high |
| §2 By the unity of the Church we must understand an unity | understand a unity | understand an unity | an | III.11 | d | high |
| §12 The words of the apostle are, “Let us therefore | of the Apostle are, | of the apostle are, | apostle | III.24 | d/case | high |
| §23 For they pretend that in Baptism | that in baptism, the | that in Baptism, the | Baptism | III.35 | d/case | high |

## Book IV, chapter 3 — `book-4-chapter-03.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| note: Luke 21:15; 24:49; Mark 16:15 [keep CCEL (“Go ye into all the world”; 1845 “Mark vi. 15”)] | Mark 16:15; Acts | Mark vi. 15; Acts |  | III.68 | misprint-1845 | - |
| §15 Cyprian: so that that ordination was just and legitimate (1845 “that that”) | so that ordination was | so that that ordination was | so that that ordination was | III.71 | b | high |
| §16 (see ch. 14, sec. 20; ch. 19, sec. 31) [keep CCEL (1845 “chap. xiv., sec. 29”; Book IV ch. 14 has 26 sections)] | ch. 14, sec. 20; | chap. xiv., sec. 29; |  | III.72 | misprint-1845 | medium |

## Book IV, chapter 4 — `book-4-chapter-04.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §1 the form of the early Church | the early church, as | the early Church, as | Church | III.74 | d/case | high |
| §7 bad examples arose, Canons were framed | arose, canons were | arose, Canons were | Canons | III.80 | d/case | high |
| §9 since the whole Church is by Peter denominated κληρος | whole church is by | whole Church is by | Church | III.82 | d/case | high |
| note (French): Afin qu’il n’allât nulle part [keep CCEL (1845 “n’allâ”, the t dropped)] | qu’il n’allât nulle | qu’il n’allâ nulle |  | III.82 | misprint-1845 | - |

## Book IV, chapter 5 — `book-4-chapter-05.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §8 as soon as he has seized upon the Roman see | the Roman See, may | the Roman see, may | see | III.97 | d/case | high |
| §10 and the administration of the sacraments | of the Sacraments, they | of the sacraments, they | sacraments | III.99 | d/case | high |

## Book IV, chapter 6 — `book-4-chapter-06.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 4. Another answer. The keys given to the other Apostles | other apostles as well | other Apostles as well | Apostles | III.108 | d/case | high |
| §8 no ground for making an universal rule out of a special example | making a universal rule | making an universal rule | an | III.115 | d | high |
| §8 quoting from Homer, οὐκ ἀγαθὸν πολυκοιρανίη (small omicron in 1845; accents not compared) | Homer, Οὐκ ἀγαθον | Homer, οὐκ ἀγαθον | οὐκ | III.116 | d/case | medium |
| §11 whosoever becomes bishop of that city | becomes Bishop of | becomes bishop of | bishop | III.118 | d/case | high |
| §13 Let them either confess that that arrangement was preposterous (1845 “that that”) | confess that arrangement was | confess that that arrangement was | confess that that arrangement was | III.120 | b | high |
| §15 “all seek their own” [keep CCEL (the verse is Phil 2:21; 1845 “Phil. ii. 20”)] | (Phil 2:21) . | (Phil. ii. 20.) |  | III.121 | misprint-1845 | - |

## Book IV, chapter 7 — `book-4-chapter-07.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 Nay, even in Italy itself, an universal council was held (that of Aquileia) | itself, a universal council | itself, an universal council | an | III.129 | d | high |
| §16 Gregory: by calling me universal Pope | me Universal Pope. | me universal Pope. | universal | III.142 | d/case | high |
| §30 associates of kings and Cæsars [keep CCEL (1845 “Cesars” here, “Cæsars” at III.149)] | and Cæsars. And | and Cesars. And |  | III.156 | misprint-1845 | medium |

## Book IV, chapter 8 — `book-4-chapter-08.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 or apostles, or successors of apostles | successors of Apostles, | successors of apostles, | apostles | III.160 | d/case | high |
| §10 But if this power of the Church which is here described | power of the church which | power of the Church which | Church | III.167 | d/case | high |

## Book IV, chapter 9 — `book-4-chapter-09.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §2 as to an universal council | as to a universal council | as to an universal council | an | III.178 | d | high |
| §4 For in addressing the elders of Ephesus | the Elders of Ephesus | the elders of Ephesus | elders | III.180 | d/case | high |

## Book IV, chapter 10 — `book-4-chapter-10.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §6 we have adverted to this subject (1845 “Book III. chap. iv. 5,”; CCEL sec. 6; neither section speaks of human traditions, so the print is followed) | ch. 4 sec. 6), yet | ch. 4 sec. 5), yet | ch. 4 sec. 5), yet | III.197 | d | medium |
| §27 government is necessary to ensure the common peace | to insure the common | to ensure the common | ensure | III.220 | d | high |

## Book IV, chapter 11 — `book-4-chapter-11.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §14 about an hundred and thirty years ago | about a hundred and | about an hundred and | an | III.242 | d | high |
| §16 when the Emperor Maurice had commanded | the emperor Maurice | the Emperor Maurice | Emperor | III.244 | d/case | high |

## Book IV, chapter 12 — `book-4-chapter-12.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| §17 and an useful admonition to arouse them | and a useful admonition | and an useful admonition | an | III.262 | d | high |
| §22 To call an universal council belonged to the emperor alone | To call a universal | To call an universal | an | III.267 | d | high |

## Book IV, chapter 13 — `book-4-chapter-13.typ`

| anchor | CCEL | 1845 | proposed | p. | kind | conf. |
|---|---|---|---|---|---|---|
| Sections 2. Three points to be considered with regard to vows. First, To whom | First, to whom | First, To whom | To | III.273 | d/case | high |

## Findings (one JSON line each)

```
{"file": "book-4-argument.typ", "anchor": "The first head occupies the first thirteen Chapters", "ccel": "thirteen chapters; but", "1845": "thirteen Chapters; but", "proposed": "Chapters", "page": "III.6", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "Sections 1. The Church now to be considered", "ccel": "The church now to", "1845": "The Church now to", "proposed": "Church", "page": "III.7", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "§2 By the unity of the Church we must understand an unity", "ccel": "understand a unity", "1845": "understand an unity", "proposed": "an", "page": "III.11", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "§12 The words of the apostle are, “Let us therefore", "ccel": "of the Apostle are,", "1845": "of the apostle are,", "proposed": "apostle", "page": "III.24", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-01.typ", "anchor": "§23 For they pretend that in Baptism", "ccel": "that in baptism, the", "1845": "that in Baptism, the", "proposed": "Baptism", "page": "III.35", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-03.typ", "anchor": "note: Luke 21:15; 24:49; Mark 16:15 [keep CCEL (“Go ye into all the world”; 1845 “Mark vi. 15”)]", "ccel": "Mark 16:15; Acts", "1845": "Mark vi. 15; Acts", "proposed": "", "page": "III.68", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-03.typ", "anchor": "§15 Cyprian: so that that ordination was just and legitimate (1845 “that that”)", "ccel": "so that ordination was", "1845": "so that that ordination was", "proposed": "so that that ordination was", "page": "III.71", "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-03.typ", "anchor": "§16 (see ch. 14, sec. 20; ch. 19, sec. 31) [keep CCEL (1845 “chap. xiv., sec. 29”; Book IV ch. 14 has 26 sections)]", "ccel": "ch. 14, sec. 20;", "1845": "chap. xiv., sec. 29;", "proposed": "", "page": "III.72", "kind": "misprint-1845", "confidence": "medium"}
{"file": "book-4-chapter-04.typ", "anchor": "§1 the form of the early Church", "ccel": "the early church, as", "1845": "the early Church, as", "proposed": "Church", "page": "III.74", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-04.typ", "anchor": "§7 bad examples arose, Canons were framed", "ccel": "arose, canons were", "1845": "arose, Canons were", "proposed": "Canons", "page": "III.80", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-04.typ", "anchor": "§9 since the whole Church is by Peter denominated κληρος", "ccel": "whole church is by", "1845": "whole Church is by", "proposed": "Church", "page": "III.82", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-04.typ", "anchor": "note (French): Afin qu’il n’allât nulle part [keep CCEL (1845 “n’allâ”, the t dropped)]", "ccel": "qu’il n’allât nulle", "1845": "qu’il n’allâ nulle", "proposed": "", "page": "III.82", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-05.typ", "anchor": "§8 as soon as he has seized upon the Roman see", "ccel": "the Roman See, may", "1845": "the Roman see, may", "proposed": "see", "page": "III.97", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-05.typ", "anchor": "§10 and the administration of the sacraments", "ccel": "of the Sacraments, they", "1845": "of the sacraments, they", "proposed": "sacraments", "page": "III.99", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "Sections 4. Another answer. The keys given to the other Apostles", "ccel": "other apostles as well", "1845": "other Apostles as well", "proposed": "Apostles", "page": "III.108", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "§8 no ground for making an universal rule out of a special example", "ccel": "making a universal rule", "1845": "making an universal rule", "proposed": "an", "page": "III.115", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "§8 quoting from Homer, οὐκ ἀγαθὸν πολυκοιρανίη (small omicron in 1845; accents not compared)", "ccel": "Homer, Οὐκ ἀγαθον", "1845": "Homer, οὐκ ἀγαθον", "proposed": "οὐκ", "page": "III.116", "kind": "d/case", "confidence": "medium"}
{"file": "book-4-chapter-06.typ", "anchor": "§11 whosoever becomes bishop of that city", "ccel": "becomes Bishop of", "1845": "becomes bishop of", "proposed": "bishop", "page": "III.118", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "§13 Let them either confess that that arrangement was preposterous (1845 “that that”)", "ccel": "confess that arrangement was", "1845": "confess that that arrangement was", "proposed": "confess that that arrangement was", "page": "III.120", "kind": "b", "confidence": "high"}
{"file": "book-4-chapter-06.typ", "anchor": "§15 “all seek their own” [keep CCEL (the verse is Phil 2:21; 1845 “Phil. ii. 20”)]", "ccel": "(Phil 2:21) .", "1845": "(Phil. ii. 20.)", "proposed": "", "page": "III.121", "kind": "misprint-1845", "confidence": "-"}
{"file": "book-4-chapter-07.typ", "anchor": "§2 Nay, even in Italy itself, an universal council was held (that of Aquileia)", "ccel": "itself, a universal council", "1845": "itself, an universal council", "proposed": "an", "page": "III.129", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-07.typ", "anchor": "§16 Gregory: by calling me universal Pope", "ccel": "me Universal Pope.", "1845": "me universal Pope.", "proposed": "universal", "page": "III.142", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-07.typ", "anchor": "§30 associates of kings and Cæsars [keep CCEL (1845 “Cesars” here, “Cæsars” at III.149)]", "ccel": "and Cæsars. And", "1845": "and Cesars. And", "proposed": "", "page": "III.156", "kind": "misprint-1845", "confidence": "medium"}
{"file": "book-4-chapter-08.typ", "anchor": "§2 or apostles, or successors of apostles", "ccel": "successors of Apostles,", "1845": "successors of apostles,", "proposed": "apostles", "page": "III.160", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-08.typ", "anchor": "§10 But if this power of the Church which is here described", "ccel": "power of the church which", "1845": "power of the Church which", "proposed": "Church", "page": "III.167", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-09.typ", "anchor": "§2 as to an universal council", "ccel": "as to a universal council", "1845": "as to an universal council", "proposed": "an", "page": "III.178", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-09.typ", "anchor": "§4 For in addressing the elders of Ephesus", "ccel": "the Elders of Ephesus", "1845": "the elders of Ephesus", "proposed": "elders", "page": "III.180", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-10.typ", "anchor": "§6 we have adverted to this subject (1845 “Book III. chap. iv. 5,”; CCEL sec. 6; neither section speaks of human traditions, so the print is followed)", "ccel": "ch. 4 sec. 6), yet", "1845": "ch. 4 sec. 5), yet", "proposed": "ch. 4 sec. 5), yet", "page": "III.197", "kind": "d", "confidence": "medium"}
{"file": "book-4-chapter-10.typ", "anchor": "§27 government is necessary to ensure the common peace", "ccel": "to insure the common", "1845": "to ensure the common", "proposed": "ensure", "page": "III.220", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-11.typ", "anchor": "§14 about an hundred and thirty years ago", "ccel": "about a hundred and", "1845": "about an hundred and", "proposed": "an", "page": "III.242", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-11.typ", "anchor": "§16 when the Emperor Maurice had commanded", "ccel": "the emperor Maurice", "1845": "the Emperor Maurice", "proposed": "Emperor", "page": "III.244", "kind": "d/case", "confidence": "high"}
{"file": "book-4-chapter-12.typ", "anchor": "§17 and an useful admonition to arouse them", "ccel": "and a useful admonition", "1845": "and an useful admonition", "proposed": "an", "page": "III.262", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-12.typ", "anchor": "§22 To call an universal council belonged to the emperor alone", "ccel": "To call a universal", "1845": "To call an universal", "proposed": "an", "page": "III.267", "kind": "d", "confidence": "high"}
{"file": "book-4-chapter-13.typ", "anchor": "Sections 2. Three points to be considered with regard to vows. First, To whom", "ccel": "First, to whom", "1845": "First, To whom", "proposed": "To", "page": "III.273", "kind": "d/case", "confidence": "high"}
```

## Applied (2026-11-24)

All 29 rows and the 3 hand edits, plus 4 slips found during the Latin compare and checked against the 1845 print: a stray apostrophe in "lord of all things" (III.276), the semicolon in "women; that" (III.294), and commas after "Gratian" and "Therefore" (III.87). The 5 misprint-1845 rows were left unchanged. The word-level diff was read, and every change is a listed row.
