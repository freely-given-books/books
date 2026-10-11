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

**Modern witnesses: Monergism and sermonindex.net.** Look on both for every
new book; they are witnesses only, never the text. Kept beside the sources as
`source/*.monergism.*` and `source/*.sermonindex.htm`, git-ignored.
Monergism's pages are behind Cloudflare: read a page through
`https://web.archive.org/web/2024/<page>` and fetch its files through
`https://web.archive.org/web/2025id_/<file url>`. sermonindex.net lists books
at `/books/letter-<x>/` by title (a book can have several copies there); a
book's chapters are `/books/<slug>/<N>`, the text in
`#book-reader-content`. Many of its copies mirror CCEL or Monergism
(including W. H. Gross's modernizations), so measure each against the base
before counting it as a separate witness; say in `SOURCES.md` which is which.

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

colophon is a submodule: after cloning, `git submodule update --init`. It
is **pinned to colophon's release tags** (`0.2.0`, like the Typst templates'
tags), never to a branch or an untagged commit; the `colophon release`
workflow fails a PR that pins anything else. `./fgb` reports colophon's
version in each `build-info.txt` (`git describe`: `0.2.0`, or
`0.2.0-3-gabc1234` while working on it).

A change to the tools:

1. In `colophon/`, on a branch: make the change, run `./fgb check --all`
   here (it must pass, or the books' TEI must be updated with it), commit,
   push, PR to freely-given-books/colophon; its CI runs the same check.
2. Bump `version` in `colophon/pyproject.toml` (and `uv lock`) in that PR:
   patch (0.2.1) when no book's output changes, minor (0.3.0) for new
   features or anything that changes a book's TEI or builds.
3. After the merge, tag the merge commit and publish the release:
   `git -C colophon fetch && git -C colophon tag -a X.Y.Z origin/main -m
   "colophon X.Y.Z" && git -C colophon push origin X.Y.Z`, then
   `gh release create X.Y.Z --repo freely-given-books/colophon --verify-tag`
   with notes.
4. Pin it here, in a commit of its own: `git -C colophon checkout X.Y.Z`,
   `./fgb check --all`, `git add colophon`.

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
