# Calvin, Institutes: proofreading report (2026-10-16)

A targeted review (the editor's choice): CCEL had already been compared word by
word with the 1845 printing (999 corrections, `witness-check/`), so there was no
sentence-by-sentence read. Instead: the tools, consistency across the book,
headings, and a typesetting sweep of the six print volumes (one agent per
volume, every wording proposal checked against the 1845 OCR).

## Fixed

- **Thin spaces** (a Victorian printer's thin space keyed as a full space): 26,
  e.g. "Cicero : Qui", "“ Prince of Peace.”", "incontinent; ”". None left.
- **References** wrong against 1845: Jer. 50:25 (CCEL read roman *l*, 50, as
  1), Isa. 55:3 (*lv*), Col. 2:3, 2 Thess. 1:11, Job 14:4, Rom. 8:34,
  Rom. 11:32, 35, 2 Pet. 2:9, 1 Thess. 1:3, 1 John 3:22 (1845's own slip),
  1 Cor. 2:13.
- **Typesetting sweep**, vols 1–6: 17 + 21 + 18 + 23 + 24 + 30 fixes. Among them:
  - quotations never closed (Augustine, vol. 1; Cyprian, vol. 5; vols 4, 6);
  - stray quotation marks and parentheses;
  - "(Gen. 31:20.⁸⁶ ) By and bye";
  - a leftover note number ("kingdoms.6566");
  - stops 1845 prints;
  - spaced dashes;
  - wrong words where 1845 differs ("importers" → imposters, "deforming" → deforcing, "Curios" → Curius, "perrogative");
  - glued words ("anyburdens", "wil1");
  - Greek accents and spellings (εἰδωλοδουλεία, λατρεία, Κυρίου as 1845, ἰδιώματα);
  - Latin (discernere, Ecclesiæ Catholicæ, "August. de Gen. cont. Manich.");
  - French misprints in Calvin's French notes ("veuillins … conseli", "viloer", "Nous avous", "Roy ou Due", "Aristoeratie"). Some of these are 1845's own misprints, corrected as plain misprints.
- **Headings**:
  - the three prefatory subtitles printed all lowercase (CCEL's lost small capitals);
  - Book II ch. 15's running head read "Briefly" (CCEL) where the chapter has 1845's "Chiefly". `make_volumes.py` now builds from the TEI, and keeps the pinned template version.
- **Spelling: American throughout** (editor's choice, 2026-10-16): honor, Savior, favor, neighbor, labor, baptize, recognize, defense, offense, pretense, license, sepulcher, scepter, theater, worshiper, counselor, traveler, fulfill, acknowledgment, gray… (1,605 words). French words and English words that only end in "-ise" are untouched. Towards, amongst, whilst, burnt and learnt kept, since they are word choices, not spellings.
- **References one style** (editor's choice): one abbreviation per book in references (Isa., Ps., Exod., Eph., Num., Tit., Hos., Mic., Eccl., 1 Pet., Col., Dan., Mt. …; 248 changes). Running prose keeps its own form ("the remarkable prophecy in Isaiah 7:14"). Number ranges with a hyphen (58).

## Kept on purpose

- 16th-century French forms 1845 prints: "que est", "que estoit", "d'heure en d'heure", "baptéme", "ce ne'st"-type period spellings (where not plain misprints).
- Doubled words that are English: "to it it is owing", "spirit spirit", "in in the time", "that that", "had had".
- `refs.py` "missing" verses that are not errors: "Ps. 14:1, 53" and "Ps. 115:4, 135" (a second psalm), "Isa. 2:8, 31" (a second chapter), "Gregor. Hom. in Ezek. 11:26" (Gregory's homilies, not a verse).
- Greek 1845 prints unaccented or so (θυσια, ευχαριστικὸν), as the 1845 check verified.

## Checklist

- [x] `sweep.py`: spacing 0; punctuation hits are abbreviation stops ("&c.,", "Lib. 1.,"); doubled words are English.
- [x] `refs.py`: no wrong verse left (the four "missing" above are explained).
- [x] `./fgb check calvin` OK; `./fgb build calvin`: Lulu's rules met, one footnote set a page from its marker (accepted), six EPUBs pass epubcheck.
- [x] The printed text has no stray markup and no quotes curled the wrong way.
