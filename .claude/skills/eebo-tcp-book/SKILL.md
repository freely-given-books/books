---
name: eebo-tcp-book
description: Add a new book to Freely Given Books, or build one — the TEI pipeline in colophon/ that turns an EEBO-TCP or Evans transcription or a CCEL text (and the user's own published copy, if any) into an enriched TEI master, modern-spelling Typst chapters, a print PDF to Lulu's rules with its cover, and an EPUB 3. Use this whenever the user wants to add, start or "do" a new book (by title, author, an A#####/N##### id, a quod.lib.umich.edu or CCEL link), bring their own copy of a book into the pipeline ("merge it in", "reference it with my work"), compare a copy with a witness such as Monergism or Chapel Library, or build books: ./fgb build/pdf/epub, print PDFs, covers and spines, EPUBs, epubcheck, Lulu margin or footnote warnings, page counts. Also for rebuilding the TEI after editing chapters/typ, macron or gap decisions, review-report.md, spelling.py. Use it even when the request only names one step ("rebuild the TEI", "build the Perkins ebook", "Sinners in the Hands next"), because the steps depend on each other. For proofreading or reviewing a book's text, use book-review instead.
---

# EEBO-TCP book pipeline

The model books are William Perkins, *Christian Economy*
(`books/william-perkins/christian-economy/`, reviewed from the machine
pass) and *The Anatomy of Simon Magus* (`books/anonymous/the-anatomy-of-simon-magus/`,
a finished, heavily edited book brought in afterwards). When in doubt, do
what they do. Later books show the other shapes a book can take:

| Book | Shape |
| --- | --- |
| Gouge, *Domestical Duties* | huge `LAYOUT`, four volumes, machine pass reviewed |
| Spurgeon, *All of Grace*; Bunyan, *Pilgrim's Progress*, *Grace Abounding* | CCEL base, TCP first edition as witness |
| Sibbes, *Glorious Feast*; Brooks, *Secret Key of Heaven* | the user's copy folded in, Monergism / Chapel Library as witness |
| Edwards, *Sinners in the Hands* | one-file copy, Evans text bound with another work |

**When the user already has a copy of the book** (any of the last two
rows), read `references/finished-copies.md` before step 1: choosing the base
text, the fold-in, the slip check and the sweep are all there.
The scripts are colophon, the `colophon/` submodule (its own repository);
`colophon/CLAUDE.md` holds the hard-won lessons behind every script; read
its "Hard-won lessons" before changing any script in `colophon/`.

```
source/<ID>.tcp.xml     untouched TCP transcription (provenance; never edit)
  │ build_tei.py (+ source/editorial.py, + chapters/typ when reviewing)
source/<book>.tei.xml   enriched TEI: 1609 text + every editorial decision
  ├─ tei_extract.py ─→ chapters/typ/*.typ ─→ <book>.typ ─→ <book>.pdf
  └─ tei_epub.py    ─→ <book>.epub
```

The TEI is the master. `chapters/typ` is where the user reviews, but every
review edit is folded back into the TEI by rebuilding, so the two never
disagree. `verify.py` proves that.

## Setup

For the user, and for routine work, `./fgb` at the repo root wraps
everything below (sync, find, page, check, epub, pdf; `./fgb --help`). It
creates the venv itself. A book's `EPUB`, `PRINT` and `SIDE_BY_SIDE`
settings in `editorial.py` hold what those commands need; give a new book
them when it is set up, and point the user at `./fgb` rather than the long
commands.


The scripts run in colophon's environment, `colophon/.venv`, which uv keeps
to the versions in `colophon/uv.lock` (any `./fgb` run brings it up to
date). Call its python for every script below (written `$PY`), by its
absolute path (Python 3.14 warns about a `../..` path to a venv):

```sh
uv sync --locked --project colophon      # at the repo root; ./fgb does this itself
PY=$PWD/colophon/.venv/bin/python
```

Run the commands from the repo root unless a step says otherwise. `B` stands
for the book folder, e.g. `books/thomas-brooks/some-book`.

## Starting a new book

### 1. Get the source

The `<ID>` is the `A#####` (EEBO) or `N#####` (Evans) in a quod.lib.umich.edu
URL. That site blocks scripted access, so don't try to fetch it. The same TEI
is on GitHub (an `R#####` the user gives is an ESTC number, not a TCP id:
search TCP by title, see `references/finished-copies.md`):

```sh
git clone --depth 1 https://github.com/textcreationpartnership/<ID> /tmp/<ID>
mkdir -p $B/source && cp /tmp/<ID>/<ID>.xml $B/source/<ID>.tcp.xml
$PY colophon/tcp_structure.py $B/source/<ID>.tcp.xml
```

**Check the structure before going further.** Without further setup the
scripts handle `div[@type="dedication"]` and `div[@type="chapter"]` with an
`@n` (one file each: `dedication.typ`, `chapter-NN.typ`), which fits
Perkins's *Christian Oeconomie*. `tcp_structure.py` prints the division
tree (marking other types with `*`) and exits non-zero when text sits in a
division that shape would skip. Many TCP texts are shaped differently:
treatises, sections, sermons, parts.

Such a book gets a **`LAYOUT`** in `editorial.py`: a function from the TEI
root to the list of chapter files, each with its title and its parts (whole
divisions, or loose blocks such as a treatise's opening epigraph).
`DIV_LEVELS` sets each division type's heading level, and `RUN_IN_DIVS` sets
types whose head is a bold run-in paragraph. `colophon/layout.py`
explains the format, and `layout.sections(div, first, last)` cuts a run of
sub-divisions by position. Gouge's *Of Domesticall Duties*
(`books/william-gouge/domestical-duties/source/editorial.py`) is the model:
8 treatises, 594 sections and 242 questions, cut into 50 chapters in 4
volumes from `edition.json`. Every tool reads the layout: build, extract,
EPUB (`--toc-depth 4` lists the sections), side-by-side (`--only vol-1/`)
and `verify.py`. With a layout, `tcp_structure.py` checks instead that the
layout covers all the text (`--layout` lists the files). Show the user the
tree and agree on the files and their names before building anything.
Don't start step 2 until the check passes: text in no file would silently
vanish. A printed division
the edition deliberately leaves out (a table of contents, a publisher's
advertisement) goes in `editorial.py` as `SKIP_DIVISIONS`; loose blocks
left out (most of a long dedication, a modern publisher's foreword) go in
`SKIP_BLOCKS(root)`. Ask the user before deciding that anything with text
is left out, and cut layouts by printed text, not by position.

Before building, check which edition the text is (`<date>`, `<idno>`) and
measure it against what the user expects: a first edition can lack a fifth
of the text readers know (Bunyan's *Grace Abounding*, 1666 vs 1688).

### 2. Editorial decisions: `source/editorial.py`

```sh
$PY colophon/build_tei.py $B/source/<ID>.tcp.xml --list > /tmp/<ID>-list.txt
```

This prints every macron abbreviation and every illegible gap, numbered in
document order exactly as `editorial.py` is keyed, with the printed page, the
page-image id (`tcp:NNNN:NN`) and the words around it. Copy Perkins's
`source/editorial.py` as the template. It defines four optional names:

- **`MACRON_M`**: the set of macron indices that stand for *m*. Everything
  else expands to *n*, which is right most of the time. Read every
  occurrence. *m* is typical in com-/cum- assimilation (cōmand, cōmonly,
  frō → from, thē → them, whō → whom). The review of Perkins still caught 9
  wrong ones, so err on reading, not guessing.
- **`GAP_FIXES`**: `{index: (letters, certainty, evidence)}` for
  illegible print. Reconstruct from Bible quotations, Latin legal maxims and
  plain context. Write the letters in **this book's own spelling** (Perkins
  spells "euery", never "every"). Check word frequencies in the TCP text
  before choosing a variant. Certainty is `high`, `medium` or `low`, and
  the evidence note is stored in the TEI. Greek, Hebrew and citation digits
  need a page image: look for a second witness, e.g. a collected *Workes*
  on archive.org. `references/second-witness.md` explains how to find the
  passage in the scan and crop it. Leave a gap out rather than guess, and
  list the open ones for the user.
- **`LOWERCASE_COMMON_NOUNS`**: capitalized common nouns to lowercase
  mid-sentence. Start from Perkins's list and adjust to the book's subject.
  Leave titles and religious terms (God, Lord, Church, King, Scripture)
  alone.
- **`REPORT_NOTES`**: lines shown under "Please check" in the report. Use
  it for anything the user must look at.
- **`SKIP_DIVISIONS`**, **`TYPST_PREAMBLE`**, **`TYPST_HEADING`**: printed
  divisions left out; a line at the top of every chapter file and a
  chapter-heading format (`{n}`, `{title}`, `{short}`) for a book with its
  own heading macro, e.g. Simon Magus's
  `#import "../../common.typ": chapter` + `#chapter[{title}][{short}]`.

- **Machine-pass switches** (all off by default; see colophon/CLAUDE.md "Book
  settings"): `SPELLING`, `MODERNIZE_NOTES`, `LATIN_RUNS`,
  `DROP_FOREIGN_GAPS`, `GAP_NOTES`, `EXPAND_ETC`, `DROP_CAP_CASE`,
  `ITALIC_SENTENCE_QUIRK`. Gouge's `editorial.py` uses them all; copy it for
  a large book whose notes are English commentary.

`build_tei.py` finds `editorial.py` next to the TCP file automatically. The
shared script holds no book data, so never put book tables back into it.

### 3. Machine-only edition and chapters to review

```sh
cd $B/source
$PY ../../../../colophon/build_tei.py <ID>.tcp.xml <book>.tei.xml
$PY ../../../../colophon/tei_extract.py <book>.tei.xml ../chapters/typ --layer reg
```

Then set up the book files by copying a recent book's (Grace Abounding,
Pilgrim's Progress) and changing the text: `<book>.typ` (print,
`@local/fgbooks:0.5.4`, 5.5x8.5 by default), `cover.typ`
(`scripts/panel_cover.typ`, one palette per author: Bunyan is ochre; it is
also the ebook cover, `"cover": "cover.typ"`), `ebook-front.html`,
`ebook-override.css`, `README.md`, and `EPUB`/`PRINT` in `editorial.py`
(`COVERS` only for a cover not named `cover*.typ`). Also copy `lcc_standard_pd.png`.

Print follows Lulu's rules (memory: lulu-margins): template 0.5.4 margins
(top 0.9in, bottom 0.6in) and the inside margin from Lulu's table for the
page count (under 60 pages 0.5in, 61-150 0.625in, 151-400 1in, 401-600
1.125in). `./fgb pdf` checks it, and also warns when a footnote's text lands
on another page than its marker (Typst's widow control or a crowded page;
accept it: no per-paragraph layout in `chapters/typ`, which must be what the
TEI gives back; a fix belongs in the template). A running head that wraps
breaks the top margin: give long titles a short one with `#metadata[Short]
<short>` before the `#include`. Covers need no page-count edits: `./fgb
build` gives each cover its interior's page count and trim, and the spine
is Lulu's formula.

Hand `chapters/typ` to the user for review. That is their job, not yours.
Give them the side-by-side reading copy too (printed text next to the
edition, every change marked; read-only, git-ignored):

```sh
$PY colophon/tei_review.py $B/source/<book>.tei.xml $B/side-by-side.html
```

Regenerate it after every rebuild of the TEI. Modern pages (foreword,
appendix) go in with the same `--before`/`--after` files as the ebook, so the
page shows the whole book.
Don't "improve" the text on your own.

## After the user reviews `chapters/typ`

```sh
cd $B/source
$PY ../../../../colophon/build_tei.py <ID>.tcp.xml <book>.tei.xml \
    --review ../chapters/typ --report review-report.md
```

Every difference between the review copy and the machine pass becomes an
`#editor` decision, with the machine's proposal kept beside it. Then:

1. Read "Please check" and any **unresolved** entries in `review-report.md`
   and tell the user about them. Unresolved edits are silently missing from
   the TEI.
2. Structural edits it understands: a printed "I." turned into a `+ ` item,
   and a paragraph split. `#linebreak()` and `#align(...)` are layout: not
   stored, and they will show as the only differences in `verify.py` [2].
   That is fine, so list them in `REPORT_NOTES`.
3. Run `verify.py` (below).

When the report shows something that looks like a slip in the review
(Perkins had "Bee pitiful" for "Be pitiful"), ask the user. Don't change
their text yourself; if they agree, edit `chapters/typ` and rebuild.

## Bringing in a book that is already finished

When the modern text exists already (made by hand, or with older tools) and
the user wants the TEI to match it, treat the finished chapters as the
review. Nothing about the book should change except what the user agreed.

1. Source and structure check as in step 1; `SKIP_DIVISIONS` for printed
   parts the edition omits. Modern matter (a foreword, an appendix) stays
   Typst-only in `chapters/typ`; it is not in the TEI.
2. `editorial.py`: the heading template if the chapters use their own macro.
3. Build with the finished chapters as the review, into a scratch copy
   first, and read the report: `unresolved` must be 0.
4. Prove the round trip before touching the book:
   - `compare.py chapters <extracted> chapters/typ` for words, paragraph
     breaks, italics, notes and headings;
   - compile the print book from the old and from the extracted chapters
     (copy the book folder to scratch), then `compare.py pdf old.pdf new.pdf`
     and `cmp` of `pdftotext -layout` for both — the rendered text must be
     identical line for line; this is what catches spacing;
   - the same for the ebook with `compare.py epub`.
   Fix the tools, not the data, when something differs, and keep Perkins
   byte-identical (`verify.py`) after every change.
5. Ask before replacing `chapters/typ` with the extraction (same rendering,
   different line wrapping and markup style), then run `verify.py`: [1]
   proves rebuilding from the new files gives the same TEI.

Expect thousands of decisions for a thorough modern edition (Simon Magus:
about 7,300 — capitalization, grammar modernized, notes rewritten and moved,
translations inserted). That is the record doing its job, not noise.

Then, for any book with a modern witness, run the slip check
(`colophon/slips.py`) and the sweep (`colophon/sweep.py`); see
`references/finished-copies.md` for reading their output, the encodings a
copy's own headings, lists and closers need, and what to fix versus ask.

## Spelling decisions

The "spelling" section of the report lists words the user corrected after
the machine pass. The 8 left in Perkins are deliberate and need nothing.
When the user wants the machine to get a word right next time, add it to
`MANUAL` in `colophon/spelling.py`, keyed by the **original** spelling in
lowercase (`"sundrie": "sundry"`), not by the machine's wrong output.
Pull the original forms from the TEI's `<choice>` elements, since the report
shows machine → editor.

Add a word only if it is the same word in every context. A `MANUAL` entry
applies everywhere, in every book:

- Leave out words whose meaning depends on context: harts (deer or hearts),
  Tigres (Tigris or tigers), Corinthes, vail (to lower, or veil).
- Footnotes stay in original spelling, so note-only fixes stay editor
  decisions.
- Group entries with a comment: period spellings, KJV name forms,
  transcription slips (aud → and).
- Known cost: `bee → be` turns "Bee-hive" into "Be-hive" unless the editor
  layer overrides it. Look for this kind of reverse conflict in the rebuilt
  report (`Be → Bee`).

**`spelling.py` is shared.** After changing it, rebuild *every* TEI book
(`ls books/*/*/source/*.tei.xml`), because `verify.py` [1] fails for any
book whose machine pass changed. Read each new report, and say in the
commit that words moved from `#editor` to `#auto`.

## Verify

```sh
$PY colophon/verify.py $B
```

This rebuilds the TEI and compares it, checks that the modern-spelling
extraction matches `chapters/typ`, that the original-spelling layer keeps
every TCP word, and that the chapters compile. Expect `OK`. [2] may list
chapters whose only differences are layout lines. Check that with
`tei_extract.py` into a temp folder and `diff`. [4] validates against
`tei_all` with jing; `verify.py` finds `jing.jar` and `tei_all.rng` in
`~/.cache/fgb-tei`. If they are missing there, fetch them once:

```sh
mkdir -p ~/.cache/fgb-tei && cd ~/.cache/fgb-tei
curl -sSLO https://github.com/relaxng/jing-trang/releases/download/V20241231/jing-20241231.zip && unzip -q jing-20241231.zip
curl -sSLO https://raw.githubusercontent.com/TEIC/TEI-Simple/master/tei_all.rng
```

## Ebook (EPUB 3, no Calibre)

```sh
cd $B
$PY ../../../colophon/tei_epub.py source/<book>.tei.xml <book>.epub \
    --title "…" --author "…" --front ebook-front.html --cover cover-front.png \
    --css ../../resources/css/ebook.css --css ebook-override.css
epubcheck <book>.epub
```

Pages that aren't in the TEI go in with `--before FILE` / `--after FILE`
(repeatable, in order): a `.typ` file is rendered with Typst's HTML export
(footnotes become the same pop-up footnotes; `--typst-root` defaults to the
book folder), a `.html` file is an XHTML fragment (e.g. an "Appendix"
divider). The contents nest by heading: h2 opens an entry, h3s go under it.
See Simon Magus's README for the full command.

epubcheck must report 0 errors and 0 warnings. Calibre's checker
(`calibre-debug ../../../colophon/check_epub.py <book>.epub`) is a second
opinion; ignore the Qt/GPU noise it prints. When replacing an older ebook, run
`compare.py epub old.epub new.epub` too. Notes become EPUB 3 pop-up footnotes; Greek and
Hebrew get `lang`. Day to day, `./fgb epub` / `./fgb build` do all of this
from the `EPUB` setting in `source/editorial.py`, into `dist/`. A cover made
with `scripts/panel_cover.typ` is named by its `.typ` (`"cover": "cover.typ"`)
and its front panel is rendered at build time (`--input front-only=true
--format png`), so no cover image is kept in git; a cover designed elsewhere
is a small front image committed with the book. Built PDFs and EPUBs are
not kept in git: add the book's folder to the root `.gitignore`.

## Committing

Work on a branch, not `main`; commit and open a PR when the user asks (they
merge). Commit the source file(s), the TEI, `editorial.py`, the reports,
`chapters/typ` and the book files. A script change is committed inside
`colophon/` (on a branch there, pushed, PR to the colophon repository with
the version bumped), released as a tag after the merge, and the books
repository then pins that tag (`git -C colophon checkout X.Y.Z`, `git add
colophon`) in its own commit, apart from the book's; CLAUDE.md "Commands"
has the steps. A book branch may use an unreleased colophon while it is
worked on, but it is pinned to a release before its PR is merged. Built PDFs and EPUBs are not kept in git: add the book's
lines to the root `.gitignore` and `git rm --cached` any it tracked.

Stage paths by name, never a whole book folder: book folders hold things
that must not be committed (the user's page scans, a publisher's EPUB under
copyright, old backups). After `git rm --cached`, commit tools with a
path-limited `git commit <paths>` so the staged deletions land in the book's
commit.

After any change to `colophon/`, run `./fgb check` on every TEI book
(`ls books/*/*/source/*.tei.xml`): each must rebuild to its committed TEI.

## Subagents and token use

The user watches token use. Large jobs (hundreds of gaps, Greek from page
images, a full proofread) go to subagents:

- At most **one or two at a time**, at **medium effort**, unless the job
  is settling hard readings. Brooks's two gap readers ran side by side; two
  Opus proofreaders at once hit the session limit.
- Each writes its results to a file as it goes (gap fixes as a dict, a
  proofread as JSON lines) and never edits book files. You merge and apply.
- Give every subagent the command rule: one plain command per call,
  absolute paths, logic in a script file. Compound commands trigger
  permission prompts.
- For page images, crop small (ImageMagick) and look up the scan's OCR
  (`<ID>_djvu.xml`, split per page) before fetching images.
- The full proofread pattern is in the book-review skill.

## Decide vs ask

Decide yourself: n/m macrons and gaps that context settles (with evidence
notes), mechanical fixes, anything `verify.py` can prove.
Ask the user: the book's division structure and file names, which text is
the base (TCP or CCEL, which edition), gaps that need a page image you
couldn't get, anything that changes their reviewed text on purpose
(restoring cut passages, undoing a modernization), what to leave out,
`MANUAL` entries that could be context-dependent, and the editor credit
(`build_tei.py --editor`, default "Courtney Allen Hicks").

The user's standing preferences: editions now are *lightly* modernized (a
separate, more modern edition may come later from the same TEI), so don't
sweep for archaic grammar unless asked; clear slips are fixed and reported;
a book's deliberate choices stand (Edwards quotes the BSB). Report what you
fixed in plain words, with examples.
