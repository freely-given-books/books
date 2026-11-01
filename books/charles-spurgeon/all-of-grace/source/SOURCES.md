# All of Grace (Spurgeon, 1886): sources

## The text: the 1886 New York printing

`grace.thml.xml` is our transcription of *All of Grace: An Earnest Word with
Those Who Are Seeking Salvation by the Lord Jesus Christ* (New York: Robert
Carter & Brothers, 1886), from the archive.org scan of Princeton Theological
Seminary Library's copy (`allofgraceearnes00spur`; printed page = scan page
− 6). It is kept as ThML (`publisherID` fgb) so the pipeline reads it as it
reads a CCEL text. The transcription is released under CC0 1.0.

Until 2026-11-01 the edition was CCEL's text. CCEL's All of Grace is a
modernized revision, not Spurgeon's printing: it drops sentences and a whole
closing paragraph and rewords freely ("Listen to a little sermon" → "This
message is for you", "the Sabbath" → "Sunday", "sixpence" → "small favors",
"I trow not" → "I think not", "O sirs" → "Oh believe that"). CCEL's file is
kept untouched as `grace.ccel.witness.xml`, a witness only.

How it was made (2026-11-01; scripts in `transcription/`, run from a work
folder outside the repository):

1. **Kraken** 7.1.1 with the CATMuS-Print (fondue large) recognition model
   (zenodo 10592716, CC-BY 4.0) read every page at 300 dpi; its text is
   `ocr/spurgeon-all-of-grace-1886.kraken.txt`. It is the base.
2. **The vote** (`foundation.py`): Kraken's words and punctuation marks
   against four witnesses, GLM-OCR and Tesseract of the same scan (the
   2026-10-25 local witness export), archive.org's own OCR, and CCEL's text.
   Kraken's reading stands when two others share it; three of the four
   agreeing on another reading replace it (243 places: letters such as
   "vour", "carth", "seck"; quotation marks Kraken missed; running heads
   inside a line; 21 words it split or ran together). The 16 places with
   no majority were read on the page image (`decide.py`, `decisions.json`).
   Every replacement was reviewed by eye. A word sweep against a word list
   and CCEL's vocabulary (`wordsweep.py`) then found what every OCR got
   wrong the same way, fixed after the vote (`POST` in `decide.py`): words
   run together ("doneit", "itis", "isyet spacefor"), "jusf" (a blot after
   "just"), "th t" (the a lost in printing), "Gop" (GOD in small capitals),
   "to he a" (to | be a). Quotation marks Kraken missed where only GLM had
   them were found where a paragraph's quotes did not balance and added
   (`QUOTES_ADD`), and a few marks set the wrong way round were read on the
   page (`QUOTES_SET`). The local proofread (Qwen 3.8 27B and the
   gap-marker, the press's policy) was read through; its flags and the
   one-word differences from the earlier edition were settled on the page
   images.
3. **Layout from the print** (`assemble.py`): Tesseract's line boxes give
   the paragraph indents and the small type of quoted verse (set line by
   line, 18 quotations); the chapters are the 20 pages that open with a
   title in capitals, no page number and the first words in capitals;
   running heads and page numbers are left out; the printed pages are kept
   as `pb`.
4. **Italics** (`italics.py`): the print's italic (Scripture quoted in the
   text, Spurgeon's emphasis) measured as the slant of each word on the
   page image, against the word's own upright slant elsewhere in the book
   (168 italic runs). Small capitals (each chapter's opening words and the
   centred appeals) are set as the print sets them.
5. **Completeness** (`completeness.py`): every word of the corrected Kraken
   text is in the transcription, and no run of words that GLM, Tesseract or
   archive.org's OCR found on the pages is missing from it (what they have
   besides is running heads, page numbers and the library's plates).

The title page is transcribed by hand (its epigraph is in black letter).

The 1886 printer's own misprints stay in the transcription as printed
("sarpe", "godness", "scarely", "trangression", "Spirt", "checque"; each
read on the page image) and are corrected in the reg layer.

## Modernizing (the reg layer)

The orig layer is the 1886 print. The reg layer (`transcription/modernize.py`,
applied to a fresh extraction, then `./fgb sync` records each change as a
reg decision, then `refstyle.py`):

- American spelling (the editor, 2026-11-01): Saviour → Savior, offence →
  offense, marvellous → marvelous, towards → toward, fulfil → fulfill and
  the like, the pairs the edition used before;
- the printer's misprints corrected (sarpe → spare, godness → goodness,
  "their evils ways", "when be yielded", "better that merely" …);
- headings in title case; dashes spaced (the edition's style);
- Scripture references in the edition's style ("Romans viii. 33" →
  "Rom 8:33").

Not modernized: the 1886 wording ("I trow not", "O sirs", "sixpence"),
lower-case pronouns for God as printed, hyphenated compounds ("to-day",
"week-days").

## Witnesses

- CCEL ThML, `grace.ccel.witness.xml` (https://www.ccel.org/ccel/s/spurgeon/grace.xml)
- GLM-OCR and Tesseract of the 1886 scan (local export, 2026-10-25)
- archive.org's OCR of the scan (`allofgraceearnes00spur_djvu.txt`)
- Monergism's PDF (2015), which follows CCEL: `proofread-report.md`
