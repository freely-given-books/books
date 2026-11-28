# Addendum for Books III-IV: the 1859 Paris (Meyrueis) edition

Read `briefs/transcribe-french-vol.md` first. It still applies, with these changes for vol. 3 on.

- **Source.** CO vol. 4 (1866) can't be had, so the source is the 1859 Paris edition, vol. 2
  (`scan-1859-french/README.md`). It is the 1560 French, lightly edited by the 1859 editor:
  accents are added and Scripture references are corrected. `pages-fr/p-NNN.png` is the archive
  image number. The text is in two columns with a rule between them, and there are no bracketed
  edition markers or italic 1541 text.
- **Running heads.** Each page has a running head ("LIVRE III, CHAPITRE III." and the page
  number). Leave it out, but mark each page start as `<!-- p. 37 -->`, using the printed 1859
  page number, not the image number. Do not mark the columns.
- **Footnotes.** The footnotes are Scripture references, cued by superscript numbers
  (`cieux estoit prochain¹` with `1) Matth. III, 2; IV, 17.` at the foot). Put each reference
  into the text at its cue, in parentheses, as printed: `prochain (Matth. III, 2; IV, 17).`
  Each column has its own footnotes, and the numbers restart. If a footnote is anything other
  than a reference, keep it as a `### Notes` entry at the end of the chapter.
- **Sections.** Sections start with a bare number ("2 Jésus-Christ…"). Write them as `2.` and
  so on, one paragraph each, as in the pilot.
- **Chapter head.** The chapter head is `CHAPITRE III.` plus its argument. Write it as
  `## Chapitre 3`, then the argument. If your stretch starts the Book ("LIVRE TROISIEME" and its
  title), put that first as `# ` plus the title, as printed.
- **Keep everything as printed:** the spelling (droict, cognu, mesmes), the accents, and the
  punctuation, including the spaced colons. Do not modernize anything.
- **Your stretch.** Your stretch is a range of image numbers. Begin at the first word that
  belongs to your part, and end at the last word of your last image (or before the next
  chapter's head, if the prompt says so). A part file may begin or end mid-sentence; say so in
  your final message.

## Conventions settled on vol. 3 (2026-11-23): follow them so the files need no tidying
- **Every footnote that is a citation goes inline**, in parentheses at its cue. That covers Scripture and every other source: Fathers, Lombard, the canon law, Seneca and so on. Titles go in italics as printed, e.g. `(*De civit. Dei*, lib. XI, cap. II)`.
- Only a footnote that is a remark rather than a citation goes under `### Notes`, e.g. "Ce pape a esté le 183." Write it as `- p. N, « cue words »: the 1859 editor's footnote reads « … »`. Don't use markdown footnotes (`[^x]`).
- **Inside a reference, semicolons are spaced as the 1859 footnotes print them:** `(Rom. VIII, 28 ; XIII, 14)`. In the prose, punctuation follows the print. Colons are spaced (" :").
- **Page markers:** `<!-- p. N -->` (the printed 1859 page) goes at each page start. If a word is split across the page break, join it and put the marker after the joined word.
- **Part files:** if your part starts mid-sentence, begin with the page marker and the text, with no heading. If it ends mid-word, give the whole word in your part, and say so in your final message.
- Equally, if your part starts with the second half of a word split across the page, leave that fragment out: the part before gives the word whole.

## Misprints in the 1859 text (settled 2026-11-24, Claude's call under the Latin rule)
Correct a plain misprint of the 1859 printer in the text, for example "Comme ussi" → "aussi", "par" → "pas" where the sense
needs the negative, "nourrris" → "nourris", or "an mesme" → "au mesme". List each one under Notes as
`p. N: printed "X", read "Y" (why)`. A plain misprint is one that the Latin, the context or the same word elsewhere
settles beyond doubt. Old spellings, the 1859 editor's accents and its own Scripture references are not misprints: keep them.
When in doubt, keep the print and say so in Notes.
