# Freely Given Books — working notes for early printed sources

How books from early printed sources are prepared in this repo, and what
was learned doing it for William Perkins' *Christian Oeconomie* (1609,
EEBO-TCP `A09377`) and *The Anatomy of Simon Magus* (1700, `A25330`, a
heavily edited edition brought into the pipeline after it was finished).
Read this before starting a new book from the same kind of source.

The tools are **colophon**, the `colophon/` submodule
(github.com/freely-given-books/colophon): its architecture, the TEI
encodings, book settings and the lessons learned building it are in
`colophon/CLAUDE.md`, imported here:

@colophon/CLAUDE.md

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
`source/<work>.thml.xml`; how colophon reads it is in `colophon/CLAUDE.md`.

When the user published a book before from another copy, **CCEL is the
text** (the user's preference): build the machine pass, extract it into
`chapters/typ`, fix only clear CCEL errors there, and compare the old copy
and any other witness (an EEBO-TCP first edition, kept untouched as
`source/<ID>.witness.xml`, which `sources.find` does not pick up) with
`colophon/drift.py` into `source/witness-report.md`, instead of folding
the old copy in as the review.

## Commands

Day to day, use `./fgb` at the repo root: it works from any folder, keeps
colophon's environment up to date (uv, `colophon/uv.lock`), and takes a book
by part of its name (or none inside the book):

```sh
./fgb sync gouge          # after editing chapters/typ: fold into the TEI, show changes
./fgb find gouge thorow   # where a word is, as printed, and what was decided
./fgb page gouge --open   # side-by-side page(s)
./fgb changes gouge --open  # before-after.html: the EPUB published before the TEI
                          # next to the one built now (--old REV|FILE.epub, --new FILE.epub)
./fgb check gouge         # verify.py
./fgb check --all         # every book in parallel (after a change to colophon)
./fgb epub gouge          # EPUB + epubcheck (settings: EPUB in editorial.py;
                          # EPUB["volumes"]: one EPUB per volume, as Gouge)
./fgb pdf gouge           # print edition(s) (PRINT in editorial.py)
./fgb build [gouge ...]   # PDFs + covers + checked EPUB into dist/ (git-ignored);
                          # no book = every TEI book; --pdf/--epub, --out DIR
```

Built PDFs and EPUBs of TEI books are not kept in git (the root
`.gitignore` lists each book's folder); `./fgb build` remakes them.

colophon is a submodule: after cloning, `git submodule update --init`. A
change to the tools is made and committed in `colophon/` (and pushed there),
then the new commit is recorded here (`git add colophon`), after
`./fgb check --all` passes, since a tool change can change a book's TEI.

## Lessons from the books

1. **A finished copy from a scanned Victorian edition** (Sibbes, from a
   Grosart-type text) carries OCR misprints (he/be, b/h, "Gentles"). With a
   second modern witness of the same early text (Monergism), list the places
   where the copy departs from the early text *and* the witness agrees with
   the early text (`source/witness-report.md`); those are the likely slips,
   for the user to accept or reject. Folding the copy in keeps them until
   then.
2. **Gaps are often Greek or Hebrew the transcription dropped** (TCP
   `<gap reason="foreign">`; check CCEL texts for missing Greek too).
   Restore them, never leave them out: read each from the page images
   (archive.org `bim_early-english-books-*`, scan index = 2 x TCP image - 3
   or - 2 for two-page images; verify the printed page) and record it as an
   `#editor` entry in `GAP_FIXES`. Give only what the gap stands for: the
   TCP usually keeps the note's closing stop outside the gap. Put the same
   text in `chapters/typ` before syncing, or the review records it as
   deleted. Gouge: 240 restored, and 177 medium-certainty letter fills
   checked on the same images (32 wrong guesses, e.g. "sacrifice" for
   "lust").

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
   `RUN_IN_DIVS`); see `colophon/layout.py` and Gouge's `editorial.py`.
   In a layout book, division heads are text of the file (`=` lines),
   aligned and editable like the rest; the file titles belong to the layout.
