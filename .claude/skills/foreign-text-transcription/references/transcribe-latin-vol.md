# Brief: publishable Latin text of Calvin's Institutio (1559), one stretch of pages

Freely Given Books is making three editions of the Institutes:
- **la**: Calvin's 1559 Latin, which will be published on the website;
- **en**: Beveridge's English, corrected against the Latin, then a Modern English edition;
- **fr**: Calvin's 1560 French, if possible.

The Latin has two jobs. It is the authority for correcting the English, and it will be **published**,
so it must be accurate to the letter. You transcribe one stretch of pages.

Your stretch is given in the prompt that sent you here: the volume folder, the page range, and the
chapters.

## Sources (in `~/Projects/fgbooks/work/institutes/latin/<vol>/`)
- `pages-la/p-NNN.png`: page images of Baum, Cunitz and Reuss, Brunswick 1869 (the text of Calvini
  Opera vol. 2), 300 dpi, two columns. NNN is the PDF page number.
- `kraken-la/p-NNN.txt` and `.xml`: Kraken OCR (ALTO has line coordinates). Usually the best
  reading, but lines from the two columns can be merged; the coordinates settle reading order.
- `tess-la/p-NNN.txt`: Tesseract (lat), a second vote.
- The 1559 Geneva print itself: `../scan-1559-print/institutiochrist1559calv.pdf`. Render a page with
  `pdftoppm -f N -l N -r 300 -gray -png` into a folder of your own under `<vol>/transcribe-<your-range>/`.
  Use it only for doubtful readings. Book I ch. 1-5 = PDF pages 9-19, about 1.1 PDF pages per 1869
  page; find your place by searching.

A pilot did this for Book I ch. 1-5. Its result is `pilot/latin-1559-ch1-5.md`: match that format.
Its scripts are `pilot/transcribe/` (column split by coordinates, OCR comparison). Reuse them.

## Method
1. Rebuild the text in reading order: column 1, then column 2, page by page.
2. Compare Kraken and Tesseract word by word. Read the page image at **every** disagreement and settle it.
3. Then read each page image once more against your text. In the pilot about 20 words were wrong
   in *both* OCRs the same way, so agreement alone is not proof. Look especially at Greek, numbers in
   references, and proper names.
4. Keep the 1869 spelling and punctuation exactly. Join line-end hyphens. Don't keep italics. In 1869
   italics mark text new in 1559; note that in the header comment only.
5. Structure:
   - one heading per chapter: `## Caput N` with Arabic N, then the chapter argument;
   - then `1.`, `2.` … sections, one paragraph each;
   - verse as separate lines;
   - Scripture references as printed, Greek in Greek letters.
   - Front matter (prefaces, the letter to the king) gets `## ` plus its title as printed, with
     paragraphs as printed.
6. Move the editors' footnotes to an `### Apparatus` list after each chapter, keyed `[N-k]` in the
   text. Leave out running heads and page numbers. Mark a column or page break as
   `<!-- col 123 -->` (the 1869 column numbers), so the text can be cited.
7. Mark anything you still cannot settle as `{word?}`, and list each one at the end.

## Output
One file per chapter or preface in `<vol>/la/`, named like the English files in
`~/Projects/fgbooks/books/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-1/`.
For example, `book-1-chapter-06.md`, and for front matter the English name with `.md`. Front matter
with no English counterpart gets a plain descriptive name.

Write with the Write tool, or a Bash heredoc if Write is refused.

If your stretch starts or ends in the middle of a chapter, write only the part on your pages and
name the file `book-1-chapter-NN.part-a.md` or `.part-b.md`. Say so in your message.

Final message (short): the files written, words per file, disagreements settled, the count of
corrections found in step 3, any `{?}` left, and anything odd in the 1869 text that the English
check should know about.
