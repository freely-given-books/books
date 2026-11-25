---
name: print-recheck
description: Recheck a keyed or transcribed base text (CCEL, Monergism, an older edition's e-text) word for word against the printed book it claims to reproduce, from page scans and OCR, and restore the print wherever the e-text departs from it — the way the Institutes' CCEL text was rechecked against Beveridge's 1845 printing. Use this whenever a book's base is CCEL or any modern transcription of a Victorian or earlier print, when the user wants the Classic "as printed", asks whether CCEL (or another e-text) matches the printed edition, wants typos traced to the e-text, or before signing a CCEL-based book. Includes the two checks first written for the Institutes vol. 6 that catch doubled-letter slips and swapped Bible book names.
---

# Print recheck: the e-text against the printed book

A Classic is the book **as printed**. A keyed e-text (CCEL) is not: it drops and adds words,
modernizes grammar here and there (hath → has), mis-keys letters and references. The recheck
finds each departure, confirms it on the page image, and restores the print. The editor's rule
(2026-11-23, "classic to be classic"): the Classic follows the print wherever the e-text's
wording departs from it.

**Not changed** (house style, not departures): Arabic reference style, American spelling (the
editor's one stated exception), the e-text's punctuation around references, its word joins
(the print's "any thing", "every where"), Greek accents. **Kept against the print**: the
print's own misprints the e-text corrects (a reference to a chapter that doesn't exist, a
wrong book), listed as `misprint-1845` with an empty `proposed`.

Worked example: the Institutes, six volumes, 1845 scans of the University of Toronto copies
(archive.org), Kraken OCR with ALTO in `work/institutes/vol*/kraken/`; reports
`work/institutes/latin/vol*/classic-recheck-vol*.md`. About 30–170 changes a volume.

## Scripts (copy into `work/<book>/…/recheck/` and set their constants)

Each was written for one Institutes volume: set `T` (the chapters folder), `W`/`K` (the OCR),
the page ranges and the image offset (image = printed page + 4 for 1845 vol. 3) at the top.

| script | does |
|---|---|
| `align.py` | aligns every chapter (main text, then footnotes against the OCR words left over) with the OCR, running heads dropped, line-end hyphens joined; writes `cand.json`/`cand.tsv`, one candidate difference per row |
| `filter.py` | drops OCR noise, note marks, reference-style and American-spelling differences → `cand2.tsv` |
| **`doubles.py`** | the pairs `align.py`'s fold calls equal because it collapses doubled letters: catches *foretel*/*foretell*, *suppresing*/*suppressing* → `doubles.tsv` |
| **`bookcheck.py`** | the reference rows `filter.py` drops because the numbers agree, where the book names differ (CCEL "Mark" for the print's "Matth.") |
| `refcheck.py` | every reference left unmatched in the OCR is checked against the chapter's text |
| `notecount.py`, `notepages.py` | footnotes counted per chapter and per page, print against e-text; trace every difference |
| `crop.py`, `mkbatch.py`, `batch.sh` | cut the line(s) holding a word from the page image (ALTO boxes) and stack them in labelled contact sheets to read |
| `build_report.py` | from the confirmed rows: the report, `apply-input.jsonl`, `manual-edits.json` |
| `apply_recheck.py VOL_DIR [--apply]` | applies them to `chapters/typ` (dry run by default; set `VOLDIR`) |

`doubles.py` and `bookcheck.py` came after vols 1–5 were rechecked (their run on vols 1–5 found
one more slip); run them **every time**. Most of what `doubles.py` lists is American spelling
(fulfil/fulfill, worshipper/worshiper) or OCR noise (jjesus); `bookcheck.py`'s list is mostly
misalignment, plus the print's own reference misprints the e-text corrects (keep those).

## Method

1. Run the alignment and the filters; read **every** remaining candidate, and every long run of
   unmatched words.
2. Confirm each on the **page image**, never on the OCR alone: only what the image shows is
   listed. Use the crops; the label `mkbatch.py` gives can point at the wrong line when a word is
   on the page twice: re-crop those by hand.
3. Count the footnotes both ways and trace every difference.
4. Kinds in the report: `d` wording, `d/case`, `d/grammar` (the e-text's has/does for the
   print's hath/doth), `c` e-text additions (deleted), `b` omissions (restored), `n` notes,
   `misprint-1845` (kept).
5. If the recheck runs beside a translation check (`translation-check` skill), apply it **after**
   the translation fixes are verified, then rebuild the corrected text and fix its misses: a
   recheck change inside a fix's `old`, or a fix making the same change (reject that fix).
6. Apply, then read the word diff of the chapters (`git diff --word-diff`): every change should be
   one of the report's. `./fgb sync BOOK`, `./fgb check BOOK`, commit with the report's counts.
   Never hand-edit the TEI.
7. Typos found later by other passes (the compare agents meet them) go in a list beside the
   report and are applied the same way; check each on the print first: if the print has it too,
   it's the translator's, not the e-text's, and the Classic keeps it (the corrected text fixes it).
