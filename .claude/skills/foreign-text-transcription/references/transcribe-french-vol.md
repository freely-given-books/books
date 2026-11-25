# Brief: publishable French text of Calvin's Institution (1560), one stretch of pages

Freely Given Books is making three editions of the Institutes:
- **la**: Calvin's 1559 Latin, which will be published on the website;
- **en**: Beveridge's English, corrected against the Latin, then a Modern English edition;
- **fr**: Calvin's 1560 French, if possible.

The French is Calvin's own translation of 1560. It has two jobs. It is the tiebreaker when the
English is checked against the Latin, and it may be **published**, so it must be accurate to the
letter, with old spellings and accents as printed. You transcribe one stretch of pages.

Your stretch is given in the prompt that sent you here: the volume folder, the page range, and the
chapters.

## Sources (in `~/Projects/fgbooks/work/institutes/latin/<vol>/`)
- `pages-fr/p-NNN.png`: page images of Calvini Opera vol. 3 (Baum, Cunitz and Reuss, 1865), the
  French of 1560, 300 dpi, two columns. NNN is the PDF page number. The edition prints bracketed
  markers such as `[1541 p. 1; 1551 8. §. 1.]` and small-type variants and notes at the foot.
- `kraken-fr/p-NNN.txt` and `.xml`: Kraken OCR (ALTO has line coordinates). Usually the best
  reading, but lines from the two columns can be merged; the coordinates settle reading order.
- `tess-fr/p-NNN.txt`: Tesseract (lat+eng), a second vote.
A pilot did this for Book I ch. 1-5. Its result is `pilot/french-1560-ch1-5.md`: match that format.
Its scripts are `pilot/transcribe-fr/` (column crops, assembly). Reuse them.

## Method
1. Rebuild the text in reading order: column 1, then column 2, page by page.
2. Compare Kraken and Tesseract word by word. Read the page image at **every** disagreement and settle it.
3. Then read each page image once more against your text. In the pilot about 20 words were wrong
   in *both* OCRs the same way, so agreement alone is not proof. Look especially at Greek, numbers in
   references, and proper names.
4. Keep the 1560 spelling, accents and punctuation exactly as printed. Join line-end hyphens. Keep
   the bracketed edition markers out of the text, and drop the italic 1541 translation where the
   edition prints it.
5. Structure:
   - one heading per chapter: `## Chapitre N` with Arabic N, then the chapter argument;
   - then `1.`, `2.` … sections, one paragraph each;
   - verse as separate lines;
   - Scripture references as printed, Greek in Greek letters.
   - Front matter (prefaces, the letter to the king) gets `## ` plus its title as printed, with
     paragraphs as printed.
6. Leave out the foot variants and notes, except where a note says the 1560 print itself reads
   differently. List those at the end of the chapter as `### Notes`. Leave out running heads and page numbers. Mark a column or page break as
   `<!-- col 123 -->` (the 1865 page numbers), so the text can be cited.
7. Mark anything you still cannot settle as `{word?}`, and list each one at the end.

## Output
One file per chapter or preface in `<vol>/fr/`, named like the English files in
`~/Projects/fgbooks/books/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-1/`.
For example, `book-1-chapter-06.md`, and for front matter the English name with `.md`. Front matter
with no English counterpart gets a plain descriptive name.

Write with the Write tool, or a Bash heredoc if Write is refused.

If your stretch starts or ends in the middle of a chapter, write only the part on your pages and
name the file `book-1-chapter-NN.part-a.md` or `.part-b.md`. Say so in your message.

Final message (short): the files written, words per file, disagreements settled, the count of
corrections found in step 3, any `{?}` left, and anything odd in the French that the English
check should know about.
