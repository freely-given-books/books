# Bringing in a book the user already published

Read this when the book exists already as the user's own copy (a
`chapters/typ` folder, or a single Typst file) and is moving onto the TEI
pipeline. Sibbes (*Glorious Feast*), Brooks (*Secret Key of Heaven*) and
Edwards (*Sinners*) were done this way; Simon Magus before them.

## Contents

1. Choosing the base text
2. Getting the copy into shape for a fold-in
3. Proving the round trip
4. The slip check with a modern witness
5. The text sweep
6. What to fix, what to ask
7. Encodings a finished copy may need

## 1. Choosing the base text

The base is what the TEI's printed layer holds; the user's copy becomes the
review. Look before deciding, and tell the user what you found:

- **Which edition is the TCP text?** Read `<idno>`, `<date>` and the README
  title. A first edition can be much shorter than the text readers know:
  Bunyan enlarged *Grace Abounding* to the sixth edition (1688), so TCP's 1666
  text lacked ~7,000 words. Measure (`tcp_structure.py` word counts against
  the user's copy or CCEL) and ask. The user chose CCEL's enlarged text as
  the base there, with the 1666 TCP text as the witness.
- **Is the work bound with another?** Evans N05520 is Edwards's *True Grace*
  with *Sinners* bound after it: a TEI `<group>` of two `<text>`s. The
  layout takes the second text's divisions; `SKIP_BLOCKS` takes the first.
- **The user's "umich number" may not be a TCP id.** TCP repositories are
  named `A#####`/`B#####` (EEBO), `N#####` (Evans), `K######.000` (ECCO);
  an `R#####` is an ESTC number. Search TCP by title:
  `gh api "search/code?q=%22Sinners+in+the+hands%22+org:textcreationpartnership"`.
- **CCEL or TCP?** When CCEL has the text, the user prefers CCEL as the base
  (memory: prefer CCEL); the TCP text is then a witness, kept as
  `source/<ID>.witness.xml`. When the user names a TCP id and a modern
  witness (Monergism, Chapel Library), TCP is the base.

## 2. Getting the copy into shape for a fold-in

- **One-file books** (Edwards): move everything after the title-page
  `book.with(...)` into `chapters/typ/<name>.typ` and `#include` it. Prove
  the move by compiling both (identical `pdftotext -layout`) before anything
  else.
- **Layout from the copy's own files.** Map the copy's files onto the
  printed divisions; cut runs of blocks by their printed text, never by
  position (`_cut` in Brooks's `editorial.py`): headings the fold-in inserts
  shift positions, and the layout is also read on the enriched TEI.
- **File titles** come from the copy's `==` line, character for character
  (curly apostrophes included): the build reports a mismatch as unresolved.
- **Leave the copy's layout lines alone** (`#pagebreak()`, `#linebreak()`,
  `#block(inset: ...)[...]`, `#par(first-line-indent: 0pt)[...]`, `#align`):
  they are not stored, stay in `chapters/typ`, and make `verify.py` [2]
  list the file. Note them in `REPORT_NOTES`.

## 3. Proving the round trip

Build with the copy as `--review` into a scratch file first. `0 unresolved`
and no `skipped` entries are the goal; each kind of leftover is a tool gap
to fix in `scripts/tei/` (keep the other books' TEI byte-identical:
`verify.py` [1] on every book after each change).

Then compile the print book from the old copy and from the extraction (a
scratch copy of the book folder each) and compare:

```sh
compare.py chapters EXTRACTED chapters/typ      # words, breaks, italics, notes
compare.py pdf old.pdf new.pdf                   # includes running heads
cmp <(pdftotext -layout old.pdf -) <(pdftotext -layout new.pdf -)
```

`compare.py chapters` shows `¶ ¶` around `#linebreak()` lines and headings:
an artifact of its parser, not a difference. When layout lines shift page
breaks, compare the words with running heads and folios removed (a page's
lines that are only a number and a title) before trusting a "differs".

## 4. The slip check with a modern witness

A copy made from a scanned Victorian edition carries OCR slips (he/be, b/h,
"Gentles", "the church lied into the wilderness"); a copy made from a modern
publisher's edition carries that edition's cuts. With a modern text of the
same early printing as a witness:

```sh
scripts/tei/slips.py source/<book>.tei.xml WITNESS > /tmp/slips.txt
```

WITNESS may be a PDF (Monergism), an EPUB (Chapel Library), a `.txt` or a
folder of `.typ` files. It lists every place where the edition departs from
the early printing *and* the witness agrees with the early printing. Sort
the list before showing the user:

- **misprints**: wrong words of the scanning kind (`sold` for soul)
- **dropped or added words**: "above all [other] mountains"
- **other wording**: may be an older editor's deliberate change
- **noise**: spelling and modernization the loose comparison missed
  (labours, it is/its, Saint/St), compounds (water pot), scripture
  references and the copy's own labels ("Obs.", "Ans.")

Check every "dropped" passage in context before calling it lost: an editor
who *moved* a clause looks like a drop at one place and an insertion at
another (Brooks: three of five "losses" had only moved). Write the result
to `source/witness-report.md` and ask the user what to restore.

The witness is compared, never copied, and never committed when it is under
copyright: Monergism's PDFs are (c) Monergism Books; Chapel Library's
annotations are theirs (their text is public domain).

## 5. The text sweep

```sh
scripts/tei/sweep.py books/<author>/<book> [--early]
```

Lists spacing before punctuation, `,.`/`.;`/`.....`, quotations closed with
`’’`, straight quotes, `#emph[..];` (Typst swallows the `;`: write `\;`),
straight apostrophes inside single quotations (Typst closes the quotation at
the apostrophe: write `’`), doubled and glued words; `--early` adds words in
neither the dictionary nor the early printing. Every hit is a candidate.
After the sweep, also scan the compiled PDF's text for quotes curled the
wrong way (`,‘ word`, `‘ `, `’’`): the sweep reads markup, the PDF shows what
Typst made of it.

## 6. What to fix, what to ask

- Clear slips (a misprint, a stray space, a broken quotation, a markup slip
  like `#emph[couchan]t`): fix in `chapters/typ`, sync, and list them for
  the user afterwards.
- Anything that changes the copy's wording on purpose (restoring cut text,
  reverting a modernization, Latin the copy dropped): show the list and ask.
  Restore in the copy's own style (its spelling, quotation marks, reference
  form) and say where the wording came from.
- Respect deliberate choices: Edwards keeps the BSB for scripture (a
  hand-out book), with one KJV quotation on purpose.

## 7. Encodings a finished copy may need

All are written by `build_tei.py` from the review and read by the
extractor, the ebook and the side-by-side page; see CLAUDE.md for the TEI.

| The copy has | Setting / encoding |
| --- | --- |
| headings of its own under the file title (`===`, `====`) | `EDITION_HEADINGS = True` → `label[@type="head"]` |
| printed blocks it leaves out (most of a dedication) | `SKIP_BLOCKS(root)` in `editorial.py` |
| a printed head under its title (Bunyan's dedication line) | the layout file's `"subtitle"` |
| part pages between groups of files (ebook) | the layout file's `"part"` |
| salutes and signatures run into the text or split | `CLOSER_PLAIN = True` |
| `#[ #set enum(numbering: "a)", start: 2) ... ]` | `list/@rend`, `item/@n` (automatic) |
| bullets made from printed phrases | `list[@type="bulleted"]` (automatic) |
| printed list items as paragraphs, or run into a sentence | `item[@rend="paragraph"]`, `list[@rend="inline"]` |
| verse lines as paragraphs | `lg[@rend="paragraphs"]` |
| a block run on without a space | `@rend="run-on"` |
| long titles in running heads | `#metadata[Short] <short>` before the `#include` |
