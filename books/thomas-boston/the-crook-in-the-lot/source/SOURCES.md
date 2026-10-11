# The Crook in the Lot (Boston, 1737) — sources

Puritan Paperbacks #5. First published at Edinburgh in 1737, five years after
Boston's death, with his Sermons on Church Communion; the publishers' "To the
Reader" says he was still revising it when he died and that parts are printed
from his notes as he preached them. This edition has the three parts and "To
the Reader"; the Church Communion sermons are left out (as in Banner's).

## The text: M'Millan, 1848

`crook.thml.xml` is our transcription of *The Whole Works of the Late Reverend
Thomas Boston, of Ettrick*, edited by Samuel M'Millan, vol. 3 (Aberdeen:
George and Robert King, 1848), pp. 495–590, "now first collected, and
reprinted without abridgment". It is kept as ThML (`publisherID` fgb) so the
pipeline reads it as it reads a CCEL text; colophon's `thml_to_tei.py` names
this file, not CCEL, in the TEI header.

How it was made (2026-10-10):

1. Two archive.org scans of the volume: Princeton Theological Seminary Library
   (`wholeworksoflate03bost`; OCR leaf = page + 14, page image `n` = page + 9)
   and University of Michigan (`wholeworkslater06bostgoog`; leaf = page + 7,
   image = page + 6). Their ABBYY OCR files (`*_abbyy.gz`) record italics.
2. Princeton's OCR is the base: paragraphs, italics and page numbers taken
   from it; running heads, signature marks and M'Millan's footnote to "To the
   Reader" (on the old prefatory life, which his edition omits) left out;
   line-end hyphens mended (a dictionary and the book's own words decide).
3. The two OCRs aligned word by word: where they disagree, or a word is not in
   a dictionary, the better reading taken by rule when the other OCR and
   CCEL agree on it (263 places, plus safe global fixes: "Grod", "tlie",
   "&c." and the like). About 450 more places (the remaining disagreements, a
   dictionary sweep, suspect patterns such as "to he" for "to be", line-end
   hyphens) were settled by a reader from context and the page images: 259
   corrections, among them 52 roman numerals (the OCR reads l as I), stray
   quotation marks and mangled "&c.". The OCR's space after an opening
   quotation mark was closed up (306). colophon's `refs.py` then caught three
   more (Psal. l. 15, Ezek. xxiv. 25, "my mouth").
4. Headings: a doctrine's small-capital label ("DOCTRINE I.") is the heading
   of its division, its statement in italics the first paragraph; the part
   titles in the edition are ours (the layout), M'Millan heads each part with
   its text only. M'Millan's page breaks are kept as `pb`.

The transcription keeps M'Millan's misprints; the edition corrects them as
editor decisions (`review-report.md`), the 1811 printing agreeing where it
has the passage: Gen. xxix. 31 (M'Millan xxxix.), Psal. cxlvii. 11, 12
(cxvii.), 1 Thess. ii. 16 (ii. 10), "possessions", "happiness", "desolated",
"the intercession of the Son" ("of of"). The opening "A JUST view" is set
"A just view".

The scripts are in `transcription/` (`assemble.py`, `segments.py`,
`build_thml.py`, the line-crop tool `crop.py`, ...); their working files
(OCR, page images, intermediate text) go in the git-ignored
`transcription/work/`. Every correction is kept in
`transcription/corrections/`: `1-rules.jsonl` (by rule, token spans of the
first OCR), `2-reader.jsonl` (the reader's, with the reason: image, context,
1811, CCEL), `3-final.jsonl`, and the proofread's
`4-proofread-*.jsonl` (106 more OCR slips fixed in the transcription; the
1848 printing's own misprints corrected in the edition; see
`proofread-report.md`).

## Witnesses

- **CCEL** `crook.ccel.witness.xml`, untouched
  (https://www.ccel.org/ccel/b/boston/crook.xml), from the Institute of
  Practical Bible Education etext (2000). A modernized revision, not Boston's
  wording: *you* for *thou*, *has* for *hath*, *-s* for *-eth*, verse
  references dropped, sentences recast; and an OCR text passed through a
  spell-checker: "light of the world" for "light of the word", "savvy name"
  for "savoury name", "previous and shocking" for "grievous", "saline time",
  "sovereign Manage", "honorary past", "fans here". Used only as a hint in
  the OCR correction.
- **Early printings (archive.org scans):** 1782
  `bim_eighteenth-century_crook-in-the-lot-or-the_boston-thomas_1782`; London
  1791 `crookinlotorsove` (with the Church Communion sermons); Philadelphia 1811
  `crookinlotorsove01bost`. No scan of the 1737 first edition was found.
- **Monergism:** `crook.monergism.epub` (© 2011) and `crook-2021.monergism.epub`:
  the same modernized text as CCEL, slips included ("savvy name"). Git-ignored.
- **sermonindex.net:** `crook.sermonindex.htm` (the CCEL text) and
  `crook-monergism-text.sermonindex.htm` (close to Monergism's 2021 copy).
  Neither is a separate witness. Git-ignored.
