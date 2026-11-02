# The 1688 transcription

`grace-abounding-1688.tcp.xml` is our transcription of *Grace Abounding*, the
sixth edition ("Corrected, and much Enlarged now by the Author", London:
Nath. Ponder, 1688), the last printed in Bunyan's lifetime, made 2026-11-01
and dedicated to the public domain (CC0). It replaces CCEL's text, a later
printing's, as the edition's source (CCEL's file stays as
`grace.ccel.witness.xml`). The scripts are in `transcription/`.

## The copy

The British Library copy on Early English Books microfilm
(archive.org `bim_early-english-books-1641-1700_grace-abounding-to-the-c_bunyan-john_1688`),
193 frames. The film photographs four spreads twice (frames 62-63, 87-88,
106-107, 120-121): the cleaner shot of each was used. The film is black at
the gutter, so on many pages the letters, and sometimes whole words, next to
the binding are lost.

## How it was read

1. **Kraken** (CATMuS-Print large) read every frame, cropped to its page.
2. **The vote.** Six witnesses voted on every word, compared in modern
   spelling: Kraken's reading of the 1692 copy (a photograph of a printed
   book, nearly line for line with 1688), GLM-OCR, Tesseract and archive.org's
   OCR of the same 1688 film, CCEL and the 1905 RTS text (Gutenberg #654).
   Where another reading had the most votes it replaced Kraken's; every
   disagreement without a clear majority (about 3,800 places) was read on
   the page image, by a vision model (gemma4, checked first on 60 known
   answers) and by hand. A word cut short at the gutter was completed from
   the 1692 copy.
3. **Assembly** (`emit_tei.py`): paragraphs from the section numbers and the
   print's indents; italics from the slant of each word on the page (the
   preface is set in italic with roman for names and Scripture, read by
   hand); page breaks with the printed page numbers (`facs` gives the film
   frame); the title page and the heads set by hand from the frames.
   Catchwords and signature marks ("C", "F", "G") are left out.
4. **Checked against the edition.** Every place where the 1688 text and the
   previous edition differ in wording was sorted by which side the 1692 copy
   and the 1666 first edition support; every place where they support the
   edition against us, and every unclear one (about 190), was read on the
   page image. That found 18 transcription errors, now corrected: the
   signature marks read into the text, "I" read as "1" or "l" or lost (8),
   two catchwords kept beside the next page's first word, "male may" for
   "make way", "is was" for "it was", a lost "was", and §90's number.

## What the film lost

- **Letters at the gutter** (174 words cut short): supplied from the 1692
  copy, `<supplied reason="gutter" resp="#p1692">`.
- **Whole words at the gutter** (37, nearly all "I", "of", "a", "the"):
  supplied where the previous edition has the word and the 1692 copy, the
  1666 first edition or the RTS text has it in the same context
  (`transcription/gutter.py`); `resp` names the text (`#p1692`, `#e1666`,
  `#rts`).

## As printed

The orig layer is the print: its spelling (the long s as s), its capitals,
its italics, and its slips, among them "Psal. 73" for Ps 77 (preface),
"1 Cor. 1. 33", "to comfort my" for "me", "neither indeed did think",
"what is was" (in a damaged line: read "it"). Its section numbers are
kept: the print skips 73, sets "20" for 90, and gives 285 twice; the
reading text has the standard numbering. §233's middle digit is damaged
(232 and 234 stand round it).

## The reading text

The reading text is the previous edition's (its modern spelling and
punctuation, its Scripture reference style and the editor's decisions)
with the 1688 wording put back wherever the editor's rule of 2026-10-26 says
1688 wins and the old collation (against GLM OCR) had missed it: 254
places (`transcription/apply_1688.py`, every change listed by
`apply-1688.md` when it runs). The edition keeps:

- its spelling, and the period grammar and old words the rule keeps modern
  (them words, mine eyes, an help, 'twas, betwixt);
- the passages 1688 cut, from 1666: the five the rule names, and "for I
  feared that it shut me out of all the blessings ..." and "might in this
  deceive myself" (both in 1666);
- the rule's "not changed" places (for that treasure hid, This for many
  days, unless that, there were no way, I was tore).

Three passages the previous edition had from CCEL are in no lifetime
printing and go: "he will raise us up, and" (Hos 6:2), the quotation of
Matt 10:37 after "dead to them" (§325), and "but, alas! it was all in vain"
(§168). The print's paragraphs are kept where the edition ran them in (the
errors of §124, "Secondly" and "Thirdly" in §223), and its italics are
carried into the reading text (the editor, 2026-11-01).

## The measure

32 passages of 8 printed lines (2,078 words, about 5% of the book, seed
1688, `transcription/measure.py`) were read on the page images against the
previous edition and the new text, counting words missing, added or changed
against the print (spelling, punctuation, the rule's modern forms and the
1666 passages left aside):

| | wording errors | per 1,000 words |
| --- | --- | --- |
| previous edition (CCEL-based, main 2026-11-01) | 15 | 7.2 |
| new text, as first measured | 3 | 1.4 |

The previous edition's errors were CCEL's later-printing wording ("through"
for "by", "find" for "feel", "asleep" for "to sleep", "which" for "that", an
added "also", "again", "my"). The new text's three ("a-going" twice where the
print has "going", "those" for "these", "awaked" for "awakened") came from a
filter that took a few different words for spellings; it was fixed for the
whole book (49 more places), so all three are corrected.
