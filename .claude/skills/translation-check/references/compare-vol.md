# Brief: where Beveridge departs from Calvin's Latin (Institutes, volume {N}: {CHAPTERS})

## Background

Freely Given Books publishes Henry Beveridge's English Institutes (Edinburgh, 1845) as its Classic
edition, as printed. The editor now wants a Modern English edition. Its base will be a **corrected
Beveridge**: his text, with the places where he really departs from Calvin's 1559 Latin put right.
A pilot on Book I ch. 1-5 found 79 real departures in 13,000 words (5 A, 74 B); the editor approved the method and the A + B threshold. Your job is to find those places and propose the smallest fix
for each.

Beveridge is broadly faithful but Victorian. He expands, smooths and sometimes misreads. We are not
retranslating. Most of his freedom is harmless and stays. We want the departures a careful reader
of the Latin would call wrong or lossy.

## Files (all under `~/Projects/fgbooks/`)

- Latin 1559 (Baum-Cunitz-Reuss 1869): `work/institutes/latin/vol{N}/la/<file>.md`. One file per chapter,
  named as the English file. A chapter split over two transcribers is `<file>.part-a.md` + `.part-b.md`;
  read both. Each chapter ends with an Apparatus. Page images: `work/institutes/latin/vol{N}/pages-la/`.
  Column markers `<!-- col N -->` give the 1869 column.
- Calvin's French 1560: `work/institutes/latin/vol{N}/fr/<file>.md` (parts as above). The tiebreaker. The
  French sometimes adds phrases the Latin lacks (the transcribers note them); those are not Beveridge's
  departures.
- The Latin is the 1869 critical text, corrected from the early prints where it errs (the editor,
  2026-11-23). Each Latin file ends with the transcriber's notes, which flag suspected 1869 misprints
  and doubtful readings. Where such a place bears on Beveridge, check it in the 1559 Geneva print
  (`work/institutes/latin/scan-1559-print/institutiochrist1559calv.pdf`; render a page with
  `pdftoppm -f N -l N -r 300 -gray -png` into your own folder) and list what you found in a section
  "Latin readings checked in 1559" (place, 1869, 1559, verdict).
- Beveridge: `wt-institutes/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-{N}/<file>.typ`.
- Allen's English (1841 ed.), raw OCR: `work/institutes/allen/ioanniscalviniin01calv.txt` (Books I–III ch. 13) or `ioanniscalviniin02calv.txt` (Book III ch. 14 on)
  (find the chapter by its "CHAPTER" heading).
- The pilot's results, as a model of judgment and format: `work/institutes/latin/pilot/compare-ch1-4.md`,
  `fixes-verified.json`.

## What to list

Go through the Latin **sentence by sentence**, every section, and read Beveridge's rendering
against it. List a departure when it falls under one of these kinds:

- `omission`: Latin words, a clause or an image that Beveridge drops.
- `addition`: words in Beveridge with nothing behind them in the Latin. This includes his inserted
  cross-references, such as "(see Calvin on John 4:10)", and explanatory glosses set in the text.
- `mistranslation`: he misreads the Latin, or the English says something the Latin does not.
- `shift`: the sense is weakened, strengthened, or theologically tilted (a doctrinal term rendered
  loosely, a modal changed, "almost" dropped, and so on).
- `reference`: a Scripture or patristic reference that is wrong, missing or added compared with the Latin.
- `structure`: section breaks, headings, or the chapter argument differ from the Latin.

Beveridge's "Sections." synopsis under each chapter heading is his own addition. The editor's decision: it stays (unlabelled since 2026-11-23). Don't list it.

Give each item a severity:
- **A**: Calvin's meaning is changed or some of his content is lost. A reader of Beveridge would
  misunderstand Calvin here.
- **B**: a real but smaller loss or tilt that a careful translator would fix.
- **C**: harmless paraphrase, normal translation freedom, or Victorian expansion that keeps the
  sense. **Do not list C items one by one.** Just give a count per chapter, with three typical
  examples.

Be honest both ways. Don't inflate harmless freedom into errors. Don't explain away a real misreading.
Where you are unsure, read the French. Then say what it showed.

## Proposed fixes

For each A and B item, propose the **smallest change to Beveridge's own text** that makes it right:
- Keep his wording, register and spelling around it. Don't modernize; that is a later step.
- If Allen renders the place correctly, you may borrow Allen's words (public domain). Say so.
- **Never use wording from Ford Lewis Battles (1960), McNeill, or any other copyrighted translation.**
  Write your own literal rendering instead, even if you remember theirs.
- For an `addition` that is Beveridge's editorial insertion (a cross-reference or explanation),
  propose moving it to a footnote marked "(Beveridge's note.)", unless it is plainly wrong. Then
  propose deleting it.
- The fix must be mechanical. `old` is an exact substring of the .typ file (unique in that chapter),
  and `new` is its replacement.

## Output

Write two files in `work/institutes/latin/vol{N}/compare/` (Write tool; if refused, a Bash heredoc; if both fail, return everything in your message):

1. `compare-{CHAPTERS}.md`, readable by the editor. Per chapter:
   - A short verdict on Beveridge's faithfulness there.
   - The A and B items as a numbered list, id `<Book>.{ch}.{sec}-{n}`, e.g. `I.17.3-2`; for (for example `II.8.27-1`). Each item
     gives the kind, the severity, the Latin (quoted), Beveridge (quoted), the French where you used
     it, Allen's reading in brief, the fix, and one line on why.
   - The C count with examples.
   - Any `{?}` Latin words that affected a judgment.
2. `fixes-{CHAPTERS}.json`, a list of
   `{"id","chapter","section","kind","severity","old","new","why"}` for A and B items. Check with
   `grep -F` that each `old` occurs exactly once in its chapter file.

Final message: the counts per chapter (A, B and C), the three most important findings, and the paths.
Keep it short.
