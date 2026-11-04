# The Crook in the Lot — proofread (2026-10-10)

Two readers (To the Reader + Part I; Parts II–III) read the whole edition for
sense against M'Millan's printed page (about 145 line images), the 1811
Philadelphia printing and the KJV, with CCEL's modernized text as a hint.
Their proposals, with the evidence for each, are in
`transcription/corrections/4-proofread-*.jsonl`.

## OCR slips: fixed in the transcription (106)

These are places where our transcription differed from the printed page, so
`crook.thml.xml` was corrected, not the edition (they are not editor
decisions):

- **Punctuation (64)**, mostly "." for "," before a reference ("worth. Gen."
  → "worth, Gen."; "some will say. *The crook*" → "say, *The crook*");
  "7-—" for "7.—".
- **References (13)**: "Is. x. 6." → "x. 5." and the like, read from the page.
- **Letters (13)** and **spacing (7)**: "take plea,sure" → "take pleasure",
  b/h and similar.
- **Quotation marks (6)**: stray marks from specks ("Deut xxxii. 4. ‘“ He").
- **Other**: the heading "Directions for right managing the application for
  removing the crook in the lot." set as one line (the OCR had broken it in
  two); "2 0 3", scan debris on p. 570, removed and the paragraph rejoined; a
  page break inside "evil-speaking" no longer prints as a space.

## Misprints of the 1848 printing: corrected in the edition (33 + 4)

Editor decisions in `review-report.md`; each checked against the KJV and the
1811 printing (which agrees in every case):

- **References (13)**: Job xxxiv. 23 → 33; Numb. xiv. "verse 7" → 27; Mark
  v. 21 → x. 21; Psal. xxix. 3 → xxxix. 3; Psal. xxxii. 6 → lxxxii. 6; Is.
  xiv. 9 → xlv. 9; Psal. xlvi. 4 → xlv. 5; Job xxxviii. → xxxvii.; Rom. viii.
  22 → 29; Is. xliii. 9 → lxiii. 9; Job vii. 11 → vi. 11; "John ix. 16" →
  Job; Eph. vi. 10 → iv. 10.
- **Words (15)**: "a hidden slightness" → "sightliness" (the section is on
  *Unsightliness*); "rational" → "relational" part; "he performed" →
  "performeth" (Job xxiii. 14); "tempeth" → "tempteth"; "reigns" → "reins";
  "affections of Christ" → "afflictions" (Col. i. 24); "lower that any" →
  "than"; "yea would I not" → "yet"; "11." → "II." (between I. and III.);
  "(2.)" restored before "It is no easy thing"; the words "crook, than the"
  restored, lost by eye-skip ("submit to the crook, than the crook evened to
  your heart's desire").
- **Quotation marks and punctuation (5)**: a closing mark after "chastening
  of the Lord."; stray opening marks in "your time “is always ready", "the
  “yoke in his youth" and "“And we would have thought"; a doubled stop
  "26.."; a missing stop "goes softly under it. They see".

Settled with the editor (all as recommended):

1. "Since the crook in **the** lot is of God's making" (1848 "my lot", 1811
   "the lot").
2. "5\. A crook thus evened is a double mercy." (1848 unnumbered; 1811 "5.").
3. Exod. xv. 9, 10 (1848 xv. 19, 20; 1811 9, 10: the enemy's boast and his
   ruin).
4. "to bring us down" (1848 prints a stray comma, "us, down").

Earlier (before the proofread): Gen. xxix. 31, Psal. cxlvii. 11, 12, 1 Thess.
ii. 16, "possessions", "happiness", "desolated", "the intercession of the
Son", "A just view".

## Left as printed, on purpose

- Quotations the printer left open (8): e.g. "weeping for their slain
  children … because they were not" (Matth. ii. 18), "Satan smote him with
  sore boils". The edition does not invent their closing marks.
- References that are Boston's own (1811 agrees): Prov. v. 10, 11, 12 (the
  words are vv. 11, 12), Luke xviii. 7, 8, 31, Rom. vi. 7; Psal. cxlvii.
  11, 12 (KJV 10, 11).
- "the cross events presseth down" (1848; 1811 "press").
- Spelling and grammar as M'Millan prints them (favour, shew, intangled,
  befal, chastize, irresistable),
  and Boston's Scots words (airth, lippened, foyson, coldrife, baulk, ay).

## Checklist

- `sweep.py`: one hit, "her her" in Hos. ii. 15, which is the KJV.
- `refs.py --quotes`: 646 references, 0 missing; the 8 weak quote matches are
  references standing after a different quotation, as Boston places them.
- `./fgb check`: OK (52 editor decisions, 0 unresolved). `./fgb build`: 170
  pages, Lulu margins pass, epubcheck 0 errors 0 warnings.
- Compiled PDF text: no wrongly curled quotation marks, no stray markup.
