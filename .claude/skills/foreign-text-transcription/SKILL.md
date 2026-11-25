---
name: foreign-text-transcription
description: Transcribe an author's printed Latin or French (or other non-English) text from page scans to publishable accuracy, chapter by chapter, the way Calvin's 1559 Latin and 1560 French were done for the Institutes — two OCR engines, every disagreement and then every page read on the image, the printer's misprints corrected from the author's early prints and recorded, long chapters split across agents and joined. Use this whenever the user wants an original-language text beside the English on the site, wants a translation checked against its original (the translation-check skill needs this first), or asks to OCR, transcribe or publish a Latin/French/Greek source.
---

# Foreign-language text from the scans

The text has two jobs: it is the **authority** a translation is checked against, and it is
**published** (the site's parallel pages: original | second original | English, colophon
`parallel.py`). So it must be accurate to the letter, not just good enough to compare.

Worked example: the Institutes, `work/institutes/latin/` (README, `vol1`–`vol6`, `briefs/`).
Latin: Baum–Cunitz–Reuss 1869 (Calvini Opera 2), corrected from the 1559 Geneva print. French:
Calvini Opera 3 (1865) for Books I–II, the Paris edition of 1859 for Books III–IV (the critical
volume for those couldn't be had).

## Choosing the base

- The **best critical text** of the author's final edition is the base, with its spelling and
  punctuation. Correct it from the **author's own early prints** where it plainly errs; keep
  its deliberate editorial readings (an emendation from a later edition with an apparatus note)
  and note them. The editor's rule for Calvin (2026-11-23), and the decision is Claude's when
  the editor doesn't read the language.
- No full collation against the early print is needed when a sample shows the critical text is
  sound (Calvin: 0.38 slips per 1,000 words in a 19-page sample); check the early print at every
  doubt the transcribers flag.
- A later popular edition (the 1859 French) can stand in where the critical text can't be had;
  label it as such on the site, and treat its references as its editor's, not the author's.

## Per volume

1. **Page images** (300 dpi) of the base, and of the second original, in `vol<N>/pages-la|fr/`;
   **Kraken** (with ALTO coordinates) and **Tesseract** of every page beside them.
2. **Transcription agents**, one per stretch of about 10–15 pages, launched together. The brief
   (`references/transcribe-latin-vol.md`, `references/transcribe-french-vol.md` plus the 1859
   addendum `transcribe-french-1859.md`) and a short per-volume prompt
   (`references/latin-prompt-example.md`, `references/french-prompt-example.md`) give: the page
   range, the chapter heads by image page, the output file names, the format to match. The
   method, in the briefs: rebuild reading order from the coordinates (two columns), compare the
   two OCRs word by word and settle **every** disagreement on the image, then **read every page
   image once more** against the text (both OCRs share errors: the pilot found about 20 per
   chapter, the vol 6 agents 10–30 per stretch).
3. **Format** (what `parallel.py` and `build_review.py` read): one file per chapter named like
   the English chapter file; a header comment (source, columns or pages, what was corrected);
   `## Caput N` / `## Chapitre N`, the argument in italics, then one paragraph per numbered
   section `1.`, `2.`…; `<!-- col N -->` / `<!-- p. N -->` markers; Greek in Greek letters;
   footnote references inline in parentheses (French) or keyed `[N-k]` to an `### Apparatus`
   (the Latin editors' notes); centred subheads as their own italic or bold paragraph;
   `### Notes` at the end (corrections, doubts, things the English check should know).
4. **Long chapters** go to several agents split at page boundaries, mid-sentence if need be
   (`book-4-chapter-17.part-a.md`, `.part-b.md`, `.part-c.md`). Give each the neighbours' page
   ranges; tell the later part the note number to start from once the earlier part reports it;
   a word split over the boundary goes whole to the earlier part. Record every join in a
   `JOINS.md` (`references/joins-example.md`) and check both sides of each.
5. **Misprints of the printer**:
   - Latin: corrected from the early print, each one in the chapter's notes **and** in a
     per-volume register (`references/misprint-register-example.md`: place, base reading, early
     print, verdict). Stray specks read as commas or points are dropped when the early print has
     none.
   - French (rule of 2026-11-24): plain misprints are corrected, each listed in Notes as
     `p. N: printed "X", read "Y" (why)`; old spellings, the editor's accents and his references
     are not misprints. When in doubt, keep the print and say so.
   - Words lost at a damaged page edge are supplied from the traces and the early print, and
     listed.
6. **Compare-stage finds**: the translation check often turns up a misprint the transcriber
   missed (Calvin IV.18 §13 "hodie" for *hostiae*). Check it on the early print, correct the
   file, note it, add it to the register.
7. **Into the book**: `references/export.py` (Institutes paths) copies the finished files into
   `books/<author>/<book>/parallel/<lang>/vol-N/<chapter>.md`, joining split parts (the bodies run
   on, each part's notes at the end); `references/check.py` checks that the section numbers of
   original, second original and English line up (differences are usually the second original
   numbering its sections differently: map them in `parallel/sources.json` `fr_sections`, or let
   them fall in the nearest row). `parallel/sources.json` holds the column labels shown on the
   site. `./fgb build` then writes `<book>-vol-N-parallel.html` per volume (colophon 0.65.0).

## Notes

- One volume at a time, start to finish (originals, compare, verify, corrected text) before the
  next, so the editor reviews volume by volume.
- Agents write scratch under `vol<N>/transcribe-<lang>-<first>-<last>/` and reuse the previous
  volume's scripts (column split, OCR comparison, draft assembly); point each prompt at a fixed
  copy (the vol 4 French agents fixed a dropped first line and decomposed accents).
- 20 agents is the concurrent limit; launch the rest as slots free.
