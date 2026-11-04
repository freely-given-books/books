# The Death of Death in the Death of Christ (Owen, 1648) — sources, 2026-10-23

*Salus Electorum, Sanguis Jesu: or, The Death of Death in the Death of Christ*
(London, 1648). ~160,000 words.

- **Base:** CCEL `deathofdeath.thml.xml`
  (https://www.ccel.org/ccel/o/owen/deathofdeath.xml), Goold's text (*The Works
  of John Owen*, vol. 10, Johnstone and Hunter, 1850–53) keyed via AGES from
  Banner's 1967 photolithographic reprint, with Goold's page breaks. No Banner
  apparatus (no Packer introduction). Goold's prefatory note and Analysis are
  left out of the edition (`SKIP_BLOCKS`); his footnotes stay, marked as his.
  CCEL's PDF of the same text: `deathofdeath.ccel.pdf` (git-ignored).
- **EEBO-TCP:** none. The 1648 edition is not in TCP (catalogue checked
  2026-10-23: only Owen's 1650 reply to Baxter, A90278, and replies to Owen
  such as Horne's, A86564).
- **The 1648 first edition (scan):** archive.org
  `bim_early-english-books-1641-1700_salus-electorum-sanguis_owen-john_1648`;
  OCR kept as `*_djvu.txt` (git-ignored). The witness for Owen's own wording.
  This copy has a contemporary hand correction ("publick faith" struck,
  "Comon hope" written in, To the Reader, leaf 12), which Goold follows.
- **Goold's printing (scan):** archive.org `worksofjohnowend0000owen` (vol. 10,
  1850); OCR kept as `*_djvu.txt` (git-ignored). The check of CCEL's keying.
- **Monergism:** `death-of-death.monergism.epub` (Monergism Books): Banner's
  1959 paperback, Packer's introductory essay (in copyright) and Goold's text of
  Books I–IV only. Spot checks only, never copied. Its "Modern" EPUB is
  truncated at 1 MB in the Wayback Machine and was not kept.
- **sermonindex.net:** `death-of-death.sermonindex.htm`
  (/books/the-death-of-death-in-the-death-of-christ/, 41 chapters): Goold's text
  via AGES (":--" dashes), not a separate witness. Spot checks only.

## Goold against 1648 (sample, 2026-10-23)

Goold is faithful in Owen's prose, modernizing spelling and punctuation. He
also brings Owen's Scripture quotations to the KJV (leaf 33: "his Church" → "the
church", "iniquities" → "iniquity", "unto God" → "to God", "sins" →
"trespasses", "in himself" → "in his flesh"), corrects Owen's Latin poets to
the standard texts with references (Virgil "Ergo"/"dare" → "Quare"/"date",
Ovid "gradiendum" → "gradieris"), writes "namely" for "viz." and sometimes
"to" for "unto", and drops the 1648 marginal section captions.

The editor's rule (2026-10-23): Goold is the base; Owen's 1648 words are
restored in his Scripture and his prose; Goold's corrected classical quotations
and light modernizing stand.

## Decisions (2026-10-23)

- One volume, 10.5pt (484 pages), not split after Book III.
- Order: the 1648 collation (Book by Book), the scheme of "the world" as an
  outline, covers and ebook, then the book review (proofread) last, on the
  text with Owen's words restored.
- The collation's rules, settled on Book I: a 1648 word that is a printer's
  misprint Goold corrected for sense ("prisoners" for princes, "portion" for
  potion) keeps Goold's; Owen's habitual wording stands even where small
  ("the right hand of Majesty on high", without "the"). The 1648 margin
  captions (Owen's running outline beside his section numbers) stay out of
  the text, as Goold has it; they are kept in `source/collation/*.jsonl`.
- **Owen's errata leaf** (1648, the last leaf; scan page 370, its OCR in
  `ocr-witnesses/owen-death-1648/glm/pages/000370.txt`): about 30
  corrections by page and line, which Goold carries out. A 1648 reading on
  one of those lines is Owen's misprint, not his wording: the edition keeps
  the correction (Goold's). Found 2026-10-27, after six restorations had
  undone corrections (pp. 29, 35, 36, 143, 239, 250; set right, logged in
  `goold-ccel.jsonl` as `errata`). One exception: p. 230, Owen's
  "Zedekiah" for "Jeremiah", in a quotation of Jer. xxix. 2, where the
  verse reads "Jeconiah"; the edition keeps Goold's (the Bible's) word.

## Local OCR (2026-10-25)

Both scans were read again locally, GLM-OCR (bf16, through Ollama) and
Tesseract 5 on 300 dpi page images: the 1648 edition's Book IV and
appendices (leaves 195-370) and Goold's pp. 139-428. The records, with the
settings and a checksum for every output file, are
`source/ocr/<scan>.ocr-witness.json`; the scans and raw output are in the
git-ignored `source/ocr/ocr-witnesses/`.

The OCR finds differences; it never decides them. GLM modernizes spelling,
skips margin notes and Greek, and sometimes writes a plausible wrong word
(acceptation → "acceptance"); all three readings (GLM, Tesseract,
archive.org's ABBYY) misread b/h and ſ/f. Every difference was aligned
against the edition, filtered for spelling and reference style, and settled
on a crop of the page image.

- CCEL against Goold's printing, the whole book:
  `source/collation/goold-ccel.jsonl` (11 slips, among them two English
  glosses CCEL added after Owen's Greek).
- Book IV and the appendices against 1648: `source/collation/book-4.jsonl`.
- The held readings of Books II-IV and the appendices (140, settled
  2026-10-25 on a review page showing each 1648 page): 85 of Owen's words
  restored, 55 Goold's kept, each recorded as `decision` in
  `source/collation/*.held.jsonl`. Numbering was left to Claude: Goold's
  continuous argument numbers (Book III, Arg. I-XVI; 1648 skips 9 and leaves
  the later ones unnumbered) and his ordering of lists stand where they keep
  a sequence whole or match the list they answer.
