# Freely Given Books — working notes for early printed sources

How books from early printed sources are prepared in this repo, and what
was learned doing it for William Perkins' *Christian Oeconomie* (1609,
EEBO-TCP `A09377`) and *The Anatomy of Simon Magus* (1700, `A25330`, a
heavily edited edition brought into the pipeline after it was finished).
Read this before starting a new book from the same kind of source.

## Architecture: TEI is the master, Typst is a view

```
TCP transcription (untouched)          books/<author>/<book>/source/<ID>.tcp.xml
        │  scripts/tei/build_tei.py  (+ reviewed Typst chapters, optional)
        ▼
enriched TEI edition                   books/<author>/<book>/source/<book>.tei.xml
        │  scripts/tei/tei_extract.py
        ▼
Typst chapters / PDF                   chapters/typ/*.typ, <book>.typ

enriched TEI edition
        │  scripts/tei/tei_epub.py (+ ebook-front.html, cover, CSS,
        │                           extra .typ/.html pages via --before/--after)
        ▼
EPUB 3                                 <book>.epub
```

`tei_epub.py` gets its XHTML from `tei_to_html.py`, which reuses
`tei_extract.py`'s renderer (the `R` class; its
output methods `esc`/`emph`/`sup`/`footnote` are what the HTML subclass
overrides), so the ebook and the Typst chapters cannot drift apart.

- The **untouched TCP file** is provenance. Never edit it.
- The **enriched TEI** holds the 1609 text *and* every editorial decision
  inline, so one file yields either reading:
  - `<choice><orig>mariage</orig><reg resp="#auto">marriage</reg></choice>` spelling
  - `<choice><orig>Heere</orig><reg resp="#editor">Here</reg><reg resp="#auto">Heer</reg></choice>`
    an editor overriding the machine (editor's reg first, machine's kept)
  - `<choice><abbr>fro̅</abbr><expan>from</expan></choice>` macron abbreviations,
    `y<hi rend="sup">e</hi>` → `the`
  - `<supplied reason="illegible" cert="high" resp="#auto">eu</supplied>`
    letters lost to bad print, with an XML comment giving the evidence and
    the TCP `<gap>` kept inside
  - `<list type="numbered" change="#review">` run-in "I. … II. …" set out as
    lists, printed numerals kept in `<label>`
  - `<head type="edition">` this edition's section title, printed head kept;
    `<head type="short">` its running-head form
  - `reg/@type`: spelling, case, punctuation, spacing, grammar (archaic
    forms modernized: thou, hath, -eth), emendation (another word, a word
    added or removed, a changed number; "wording" in `tei_review.py`); a `reg`
    may hold `<hi>` (italic words of the reading) and `<anchor>`s
  - notes: `note/@target` → `<anchor>` where the edition moved the note
    (it stays where it was printed for the orig layer);
    `note[@ana="#edition-only"]` added by the editor,
    `note[@ana="#print-only"]` dropped
  - `hi[@ana="#print-only"]` italic in print, roman in the edition;
    `hi[@ana="#edition-only"]` the other way round
  - `@prev`/`@next` blocks the edition runs together (both kept as printed);
    `p[@rend="quote"]` a paragraph the edition sets as a quotation;
    `trailer[@ana="#in-edition"]` a "FINIS." the edition keeps
  - lists the review shapes (Sibbes): `list/@rend` a numbering of its own
    (`"a)"`, `"I."`; the review's `#[ #set enum(numbering: ..., start: N) ... ]`),
    `item/@n` on the first item the number it starts from, an item or a
    paragraph the review indents under an item moved inside it, a paragraph
    run on into a list's last item moved there (`@prev`);
    `@rend="run-on"` a block run on with no space between;
    `epigraph[@rend="quote"]` / `q[@rend="quote"]` set as `#quote[...]`
  - a closer with a dateline or several signatories is set one line each,
    signatories first (orig layer: as printed)
  - headings the edition adds (Brooks, `EDITION_HEADINGS`):
    `label[@type="head"][@n=level][@ana="#edition-only"]` before the block
    they stand over; the review's `=` lines below the file title
  - `lg[@rend="paragraphs"]` verse set a line to a paragraph;
    `item[@rend="paragraph"]` a printed item set as a paragraph;
    `list[@type="bulleted"]` a bullet list the review makes;
    `list[@rend="inline"]` a printed list run into its sentence;
    `CLOSER_PLAIN` salutes and signatures as plain paragraphs (run on, split)
  - `SKIP_BLOCKS(root)` in `editorial.py`: loose blocks the edition leaves
    out (most of a long dedication), kept in the TEI; a layout file's
    `"part"` is a part page before it in the ebook
  - a layout file's `"subtitle"`: a printed head set as a centred line under
    the title (Bunyan's preface dedication), aligned like a paragraph
- The header (`editorialDecl`, `respStmt`, `revisionDesc`) documents the
  rules and who `#auto` / `#editor` are. It validates against `tei_all`.
- **Typst is replaceable.** Anything that reads XML can produce LaTeX, HTML
  or EPUB from the same file.

## Getting sources

**EEBO-TCP (quod.lib.umich.edu).** The site blocks programmatic access;
don't fight it. Every text is on GitHub as plain TEI:
`git clone --depth 1 https://github.com/textcreationpartnership/<ID>` →
`<ID>.xml`. `<ID>` is the `A#####` in the quod.lib URL. The `1:N` in a
quod.lib URL is the Nth top-level `<div>` across front/body/back.
`<pb n="90" facs="tcp:2719:61"/>` gives the printed page and page image.

**CCEL** (ccel.org; first book: Spurgeon, *All of Grace*). Take the ThML,
not the plain text: `https://www.ccel.org/ccel/<letter>/<author>/<work>.xml`
(e.g. `.../s/spurgeon/grace.xml`), kept untouched as
`source/<work>.thml.xml`. It plays the TCP file's part: every tool reads the
source through `scripts/tei/sources.py`, which converts ThML in memory with
`thml_to_tei.py` (div1 → chapter, blockquote/verse → `quote`, scripRef →
`ref[@cRef]`, the title page → `front/titlePage`), so there is no converted
copy. The text is kept exactly; CCEL has no page or line information, and
the header says the TEI is paragraph-faithful. A modern text sets
`MODERNIZE = False` (no early-modern spelling or case rules) and
`TYPOGRAPHY = True` (ASCII quotes curled as Typst curls them, `--` as
`DASH`, as `#auto` punctuation readings), and `QUOTE_BLOCK = True` when
the print template sets `#quote` as a block (the ebook uses `<blockquote>`).

*The Pilgrim's Progress* (`.../b/bunyan/pilgrim.xml`, both parts) added:
div2/div3 → nested `div[@type="section"]` (the layout cuts files from
them), CCEL's contents and index divs (`SKIP_DIVISIONS`, which may also
name `titlePage`), a paragraph opening with a small-caps "Name:" →
`sp/speaker` + `p` (dialogue, as TCP texts encode it; rendered
"Christian: …"), other small caps → `seg[@rend="smallcaps"]` (`SMALLCAPS =
"strong"` sets them bold, for a font without small capitals), late
headings → `signed`, and footnotes. `VERSE_LINEBREAKS = True` sets verse
line by line (and keeps CCEL's `<br/>`); in a division that is mostly verse
(`layout.verse_division`: the Apology, the Conclusion) stanzas are plain
paragraphs, not `#quote`s.

When the user published a book before from another copy, **CCEL is the
text** (the user's preference): build the machine pass, extract it into
`chapters/typ`, fix only clear CCEL errors there, and compare the old copy
and any other witness (an EEBO-TCP first edition, kept untouched as
`source/<ID>.witness.xml`, which `sources.find` does not pick up) with
`scripts/tei/drift.py` into `source/witness-report.md`, instead of folding
the old copy in as the review.

## Commands

Day to day, use `./fgb` at the repo root: it works from any folder, sets up
the venv, and takes a book by part of its name (or none inside the book):

```sh
./fgb sync gouge          # after editing chapters/typ: fold into the TEI, show changes
./fgb find gouge thorow   # where a word is, as printed, and what was decided
./fgb page gouge --open   # side-by-side page(s)
./fgb check gouge         # verify.py
./fgb epub gouge          # EPUB + epubcheck (settings: EPUB in editorial.py)
./fgb pdf gouge           # print edition(s) (PRINT in editorial.py)
./fgb build [gouge ...]   # PDFs + covers + checked EPUB into dist/ (git-ignored);
                          # no book = every TEI book; --pdf/--epub, --out DIR
```

The Typst templates (`@local/fgbooks:X.Y.Z`, `@local/fgbooksLBCF:...`) are
tags in the `typst/fgbooks-typst` submodule; `./fgb` unpacks the imported
versions into `~/.cache/fgb-typst/packages` and sets `TYPST_PACKAGE_PATH`
(`scripts/tei/packages.py`; `./fgb packages` lists them). Run Typst through
`./fgb`, or set that variable, so builds use the pinned versions.

Print PDFs are checked against Lulu's interior rules as they are built
(`scripts/tei/print_check.py`, measured on the rendered pages): nothing
within 0.5in of the trim (running heads and page numbers included), and
the inside margin Lulu's for the page count (0.625in for 61-150 pages, 1in
for 151-400, 1.125in for 401-600). It also warns when a footnote's text is set on
another page than its marker (Typst's widow control can carry the marker's
line over after placing the note; a crowded page can push the note on). Template 0.5.3 puts the running head at
0.5in (top margin 0.9in, bottom 0.6in); a book sets its inside margin in
`page-margin`, and a cover's `pages:` must follow a page-count change.

Built PDFs and EPUBs of TEI books are not kept in git (the root
`.gitignore` lists each book's folder); `./fgb build` remakes them.

The underlying scripts, for anything else:

```sh
# enriched TEI from the TCP file, folding in reviewed Typst chapters
python3 scripts/tei/build_tei.py source/A09377.tcp.xml source/christian-economy.tei.xml \
    --review chapters/typ --report source/review-report.md

# Typst chapters (dedication.typ, chapter-NN.typ) from either layer
python3 scripts/tei/tei_extract.py source/christian-economy.tei.xml chapters/typ --layer reg
python3 scripts/tei/tei_extract.py source/christian-economy.tei.xml out/orig --layer orig
#   --expand          orig layer: fro̅ -> from
#   --show-gaps       orig layer: show illegible print as transcribed (•)
#   --mark-supplied   wrap reconstructed letters in ⟨ ⟩
#   --only-auto       reg layer: machine pass only (audit what the review changed)

# EPUB 3 straight from the TEI (no Calibre); full command in the book's README
python3 scripts/tei/tei_epub.py source/christian-economy.tei.xml christian-economy.epub \
    --title "Christian Economy" --author "William Perkins" \
    --front ebook-front.html --cover cover-front.png --css ebook.css
# or the whole book as one XHTML file, to preview in a browser
python3 scripts/tei/tei_to_html.py source/christian-economy.tei.xml preview.html
# side-by-side reading copy: printed text | edition, every change marked
# (hover a word for printed / machine / editor readings); read-only
python3 scripts/tei/tei_review.py source/christian-economy.tei.xml side-by-side.html
#   --before/--after FILE   modern pages (.typ or .html), as for tei_epub.py

# a copy against the early text and a modern witness: likely slips
python3 scripts/tei/slips.py source/<book>.tei.xml witness.pdf   # or .epub, .txt, a .typ folder
# odd spacing, punctuation, quotes, swallowed semicolons in chapters/typ
python3 scripts/tei/sweep.py books/<author>/<book> [--early]
# scripture references: verses that don't exist, quotes that don't match (KJV/BSB)
python3 scripts/tei/refs.py books/<author>/<book> --quotes [--bible bsb]

# end-to-end check: rebuild matches committed TEI, round trips, compile
python3 scripts/tei/verify.py books/william-perkins/christian-economy
```

There used to be a Typst-native reader, `scripts/tei/tei.typ`
(`#tei-division(xml(...), 1)`). It matched `tei_extract.py` for Perkins but
never learned the later encodings, so it was removed; it is in git history
(commit 72afc55) if Typst ever needs to read the TEI directly again.

Book settings live in the book's `source/editorial.py`, next to the TCP
and TEI files, read by `build_tei.py`, `tei_extract.py` and
`tcp_structure.py`: `MACRON_M`, `GAP_FIXES`, `LOWERCASE_COMMON_NOUNS`,
`REPORT_NOTES`, `SKIP_DIVISIONS` (printed divisions the edition leaves out),
`TYPST_PREAMBLE` and `TYPST_HEADING` (e.g. `"#chapter[{title}][{short}]"`
for a book with its own heading macro), `LAYOUT`/`DIV_LEVELS`/`RUN_IN_DIVS`
(any other shape, see `layout.py`). Machine-pass switches, all off by
default (Gouge turns them on): `SPELLING` (the book's own words over the
shared table, e.g. "domestical"), `MODERNIZE_NOTES`, `LATIN_RUNS` (Latin
found per run of 4+ words and left as printed), `DROP_FOREIGN_GAPS`,
`GAP_NOTES` (text for a missing-pages or unrestorable gap), `EXPAND_ETC`
("&c." -> "etc."), `DROP_CAP_CASE` ("AS there" -> "As there") and
`ITALIC_SENTENCE_QUIRK` (`True`, the Perkins/Simon Magus rule; Gouge
`"after-stop"`). A `GAP_FIXES` entry may carry a fourth item, the resp
(`"#editor"` for a gap filled by hand).

Tables are read the way early printers meant them (`layout.table_reading`):
a brace (a cell spans rows) column by column, labels as lines and branches
as a `+` list; a row-wise table row by row; a table interrupting its
sentence inline. A paragraph is split around a block table or list. The
machine records the tidying (item numbers, trailing commas, capitals, the
closing stop) as readings.

## Review workflow

The reviewed Typst chapters remain a fine place to edit. To read the
edition against the printed text, generate `side-by-side.html` with
`tei_review.py` (above); it is read-only, and it shows which
`chapters/typ` file to edit. Re-run
`build_tei.py --review chapters/typ`: it aligns the reviewed text against
the machine pass token by token and records every difference as an
`#editor` decision (macron n/m fixes and filled-in gaps are recognized as
such). Body text and footnotes are aligned separately and notes are paired
by position and text, so a note can be rewritten, moved, added or dropped.
It also carries italics (`_…_`, `#emph[…]`), the review's exact spacing,
paragraph splits and merges, a printed "I." turned into a `+ ` item,
`#quote[…]` blocks and `#chapter[long][short]` headings. Pure layout
(`#linebreak()`, `#align(...)`) is not text and is not stored. `//` comment
lines are ignored. The report lists every decision and anything it could
not apply.

**Bringing in a finished book** (Simon Magus): put the TCP file in
`source/`, give `editorial.py` the book's heading template, build with the
finished chapters as `--review`, and prove the round trip before replacing
anything: `scripts/tei/compare.py chapters` (words, notes, italics,
headings), then compile the print book from the old and the extracted
chapters and run `compare.py pdf` (spacing-sensitive) and `cmp` on
`pdftotext -layout` (every line and page), and `compare.py epub` against
the old ebook. Only then replace `chapters/typ` with the extraction.

For *Christian Oeconomie* the reg extraction reproduces the reviewed
chapters byte for byte, except the `#linebreak()` in chapter 5 (layout). A
damaged list in the review copy of chapter 5 was rebuilt from the source
and copied back into `chapters/typ`.

## Hard-won lessons

1. **Words span inline markup.** `ci<g ref="char:EOLhyphen"/>uill`,
   `fro<g ref="char:cmbAbbrStroke">̄</g>`, `cu<gap/>ome`,
   `<seg rend="decorInit">C</seg>Hristian`, `y<hi rend="sup">e</hi>`.
   `teitok.py` tokenizes a TEI element losslessly into words that can
   contain such elements (tested: rebuild without changes is byte-identical
   to the source), so a `<choice>` can wrap the whole word.
2. **Pretty-print whitespace is not a space** when it sits between two
   `g`/`gap` siblings or is an element's leading text before a `g`/`gap`.
   Treating it as a space gives "con sent", "cu stome". The enriched file
   drops it inside words so consumers need no heuristics; `tei_extract.py`
   still guards against it for raw TCP input.
3. **Macron abbreviations are ambiguous** (n or m). `MACRON_M` in the
   book's `source/editorial.py` lists, by document order, the ones that are m; everything
   else is n. Build it per book by reading each occurrence. The review
   caught 9 wrong ones here (fron→from, conmonly→commonly); those are now
   `<expan resp="#editor">`.
4. **Illegible gaps can mostly be reconstructed** from Bible quotations,
   Latin legal maxims and context (`GAP_FIXES`, with certainty and
   evidence). Use the document's *own* spelling for the letters ("euery",
   not "every"; check word frequencies). Greek/Hebrew and citation digits
   need the page image — the editor filled 8 of those by hand.
5. **The machine keeps grammatical archaisms** (hath, doth, thou, thee,
   thy, ye, shalt, wilt, art, hast, dost): different words, not spellings.
   An edition may still modernize them (Simon Magus does: hath → has, thou
   → you); those are editor decisions (`reg[@type="grammar"]`), never
   `spelling.py` entries.
   Footnotes stay in original spelling in the machine pass (abbreviations
   expanded only).
6. **Sentence case rules are legacy-compatible on purpose**: first word of
   a paragraph or after . ! ? is capitalized; an italic boundary right
   after a full stop does *not* start a sentence (so "…do.] vers. 26." stays
   lowercase); a short list of common nouns is lowercased mid-sentence;
   roman numerals are left alone. Changing these rules would make an
   unreviewed rebuild differ from what was reviewed.
7. **spelling.py** is Perkins' engine merged (2026) with Gouge's: a
   letterform search (u/v and i/j swapped until the dictionary knows the
   word), more silent-e/doubled-letter patterns, `NAMES` (checked first; a
   table entry beats `DO_NOT_TOUCH`), a large `LATIN_SKIP`. Merging moved
   some Perkins/Simon Magus decisions between `#auto` and `#editor`; the
   rendered text did not change. **spelling.py misses** found by the review (bee→be ×78, lawes→laws,
   Prou→Prov, Heere→Here, bin→been, dais→days, yong→young, reade→read,
   shew→show, KJV name forms like Isaak→Isaac, Thar→Terah…) are
   now in `spelling.py`'s `MANUAL` (so this book's TEI credits them to
   `#auto`; its report is down to 8 spelling decisions, mostly in notes,
   which stay in original spelling). Context-dependent ones were left out
   (harts/hearts, Tigres, Corinthes). `bee`→`be` is a known risk: it
   mangles "Bee-hive", which the editor layer here overrides.
8. **Typst `xml()` gotchas** (from the removed `tei.typ`): paths resolve relative to the
   file that calls `xml()`, so load the XML in the book file and pass it
   in; `while` loops hit an iteration limit on a whole book, use recursion;
   adjacent string pieces keep double spaces (collapse them yourself);
   markup drops the space before `#footnote[...]` but strings don't; smart
   apostrophes are applied to markup, not strings.
9. **TEI validation**: `tei_all.rng` is on GitHub
   (`TEIC/TEI-Simple`), tei-c.org is often unreachable; validate with jing
   (`relaxng/jing-trang` releases); keep both in `~/.cache/fgb-tei`,
   where `verify.py` finds them. lxml's RelaxNG is too slow for
   `tei_all`. `@resp` is not allowed on `list`/`head` in that schema, hence
   `@change="#review"`.
10. **EPUB checking**: `epubcheck book.epub` (installed, needs Java); both
   EPUBs pass with 0 errors and 0 warnings. Calibre's own checker is a
   second opinion that runs headless:
   `calibre-debug scripts/tei/check_epub.py book.epub` (ignore the Qt/GPU
   noise it prints).
11. **Check the rendered text, not just the tokens.** A comparison of
   parsed words is blind to spacing: Simon Magus matched word for word
   while printing "natura( of" for "natura (of" — the editor had turned a
   comma into "(" but the space after the comma was still in the source.
   The review parser now records the review's spaces, readings are joined
   with them, and a spacing pass records each added or removed space as a
   `reg[@type="spacing"]` choice. `compare.py pdf` catches the rest.
12. **Typst reads `#emph[x](y)` as a call** with more arguments, and a `;`
   straight after a call (`#emph[x];`) ends it and is swallowed, so the
   semicolon never prints. Any `(`, `[` or `;` straight after a markup call is
   escaped (`\(`, `\;`) by `tei_extract.py`;
   check against everything rendered so far, since an empty text part can
   sit in between.
13. **1700 printings differ from 1609 ones**: long s (`ſ`) throughout and
   `<g ref="char:V">Ʋ</g>` for capital U are letter forms, normalized by
   the machine pass (not spelling decisions); nouns are capitalized
   mid-sentence (the review lowercases them: thousands of `case`
   decisions, which `LOWERCASE_COMMON_NOUNS` could move to the machine);
   margin notes sit at the start of a quotation, and a modern edition
   moves them to its end.
14. **A `<q>` in a division can hold `<p>`s.** Only a quotation with text
   directly inside counts as a block; one made of paragraphs is walked
   into, and merges attach to the innermost paragraph.
15. **Quotes are curled per paragraph in the ebook**, after rendering,
   because an italic name and a roman "'s" are separate fragments
   (per-fragment curling gave "Simon‘s"), and only once a run-on block has
   joined (`finish()` in `tei_to_html.py`). The rule is Typst's own: it
   remembers open quotes, so `sacrificed,' wisdom` opens and `beasts,'`
   closes. The same rule makes a straight apostrophe inside a single
   quotation (`'You are Christ's,'`) close it, so a book quoting with
   single quotes types its apostrophes as `’` in `chapters/typ`.
16. **A finished copy from a scanned Victorian edition** (Sibbes, from a
   Grosart-type text) carries OCR misprints (he/be, b/h, "Gentles"). With a
   second modern witness of the same early text (Monergism), list the places
   where the copy departs from the early text *and* the witness agrees with
   the early text (`source/witness-report.md`); those are the likely slips,
   for the user to accept or reject. Folding the copy in keeps them until
   then.

## Starting a new TCP book

The step-by-step workflow is the `eebo-tcp-book` skill
(`.claude/skills/eebo-tcp-book/SKILL.md`). In short:

1. Clone the TCP repo; copy `<ID>.xml` to `source/<ID>.tcp.xml`.
2. `build_tei.py source/<ID>.tcp.xml --list` prints every macron and gap
   with its index, page and context. Record decisions in
   `source/editorial.py` (`MACRON_M`, `GAP_FIXES`, `LOWERCASE_COMMON_NOUNS`,
   `REPORT_NOTES`; all optional). `build_tei.py` finds it next to the TCP
   file; the shared script itself holds no book data.
3. Build without `--review` for the machine-only edition, extract the reg
   layer into `chapters/typ`, review there, then rebuild with `--review`.
4. Without setup the scripts handle `div[@type='dedication']` and
   `div[@type='chapter']` (with `@n`), one file each. Any other shape gets
   a `LAYOUT` in `editorial.py` (files -> TEI parts; `DIV_LEVELS`,
   `RUN_IN_DIVS`); see `scripts/tei/layout.py` and Gouge's `editorial.py`.
   In a layout book, division heads are text of the file (`=` lines),
   aligned and editable like the rest; the file titles belong to the layout.
