---
name: eebo-tcp-book
description: Prepare a Freely Given Books edition from an EEBO-TCP transcription — enriched TEI master, modern-spelling Typst chapters, print PDF and EPUB 3 — using scripts/tei/. Use this whenever the user wants to start a book from quod.lib.umich.edu, EEBO, the Text Creation Partnership or an A##### id; bring an already finished book into the TEI pipeline ("make it match"); fill in macron or illegible-gap decisions; rebuild the TEI after editing chapters/typ; deal with review-report.md or spelling decisions; change spelling.py; or rebuild/check a TEI-based EPUB. Use it even when the request only names one step ("rebuild the TEI", "the Perkins ebook", "add a spelling fix"), because the steps depend on each other.
---

# EEBO-TCP book pipeline

The model books are William Perkins, *Christian Economy*
(`books/william-perkins/christian-economy/`, reviewed from the machine
pass) and *The Anatomy of Simon Magus* (`books/anonymous/the-anatomy-of-simon-magus/`,
a finished, heavily edited book brought in afterwards). When in doubt, do
what they do.
The repo-root `CLAUDE.md` holds the hard-won lessons behind every script; read
its "Hard-won lessons" before changing any script in `scripts/tei/`.

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

The scripts need `lxml` and `pyspellchecker`. System pip on this machine
(Artix) refuses to install packages, so use a venv and call its python for
every script below (written `$PY`):

```sh
python3 -m venv ~/.venvs/fgb-tei && ~/.venvs/fgb-tei/bin/pip install -r scripts/tei/requirements.txt
PY=~/.venvs/fgb-tei/bin/python
```

Run the commands from the repo root unless a step says otherwise. `B` stands
for the book folder, e.g. `books/thomas-brooks/some-book`.

## Starting a new book

### 1. Get the source

The `<ID>` is the `A#####` in a quod.lib.umich.edu URL. That site blocks
scripted access, so don't try to fetch it. The same TEI is on GitHub:

```sh
git clone --depth 1 https://github.com/textcreationpartnership/<ID> /tmp/<ID>
mkdir -p $B/source && cp /tmp/<ID>/<ID>.xml $B/source/<ID>.tcp.xml
$PY scripts/tei/tcp_structure.py $B/source/<ID>.tcp.xml
```

**Check the structure before going further.** The scripts only understand
`div[@type="dedication"]` and `div[@type="chapter"]` with an `@n`, which
fit Perkins's *Christian Oeconomie*. `tcp_structure.py` prints the division
tree (marking unsupported types with `*`) and exits non-zero when text sits
in a division the scripts would skip. Many TCP texts fail this check. Perkins's
*A Cloud of Faithful Witnesses* (A09376), for instance, is built from
`commentary` and `section` divisions. For such a book, the division selection
in `build_tei.py` (`find` and `files` in `main`), `tei_extract.py` (`main`)
and `tei_to_html.py` (`divisions`) has to be extended first. Show the user
the tree, agree on how divisions map to files (e.g. `preface.typ`,
`section-03.typ`), and make the change before building anything. Don't force
a book into the wrong shape, and don't start step 2 on a book that fails the
check: text in skipped divisions would silently vanish. A printed division
the edition deliberately leaves out (a table of contents, a publisher's
advertisement) goes in `editorial.py` as `SKIP_DIVISIONS`; ask the user
before deciding that anything with text is left out.

### 2. Editorial decisions: `source/editorial.py`

```sh
$PY scripts/tei/build_tei.py $B/source/<ID>.tcp.xml --list > /tmp/<ID>-list.txt
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

`build_tei.py` finds `editorial.py` next to the TCP file automatically. The
shared script holds no book data, so never put book tables back into it.

### 3. Machine-only edition and chapters to review

```sh
cd $B/source
$PY ../../../../scripts/tei/build_tei.py <ID>.tcp.xml <book>.tei.xml
$PY ../../../../scripts/tei/tei_extract.py <book>.tei.xml ../chapters/typ --layer reg
```

Then set up the book files by copying Perkins's and changing the text:
`<book>.typ` (print, `@local/fgbooks` template, which is not in this repo, so
the user compiles it), `cover.typ` (uses `scripts/panel_cover.typ`; the spine
width depends on the page count), `ebook-front.html`, `ebook-override.css`,
`README.md` and `source/README.md`. Also copy `lcc_standard_pd.png`.

Hand `chapters/typ` to the user for review. That is their job, not yours.
Give them the side-by-side reading copy too (printed text next to the
edition, every change marked; read-only, git-ignored):

```sh
$PY scripts/tei/tei_review.py $B/source/<book>.tei.xml $B/side-by-side.html
```

Regenerate it after every rebuild of the TEI. Modern pages (foreword,
appendix) go in with the same `--before`/`--after` files as the ebook, so the
page shows the whole book.
Don't "improve" the text on your own.

## After the user reviews `chapters/typ`

```sh
cd $B/source
$PY ../../../../scripts/tei/build_tei.py <ID>.tcp.xml <book>.tei.xml \
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

## Spelling decisions

The "spelling" section of the report lists words the user corrected after
the machine pass. The 8 left in Perkins are deliberate and need nothing.
When the user wants the machine to get a word right next time, add it to
`MANUAL` in `scripts/tei/spelling.py`, keyed by the **original** spelling in
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
$PY scripts/tei/verify.py $B
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
$PY ../../../scripts/tei/tei_epub.py source/<book>.tei.xml <book>.epub \
    --title "…" --author "…" --front ebook-front.html --cover cover_front.jpg \
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
(`calibre-debug ../../../scripts/tei/check_epub.py <book>.epub`) is a second
opinion; ignore the Qt/GPU noise it prints. When replacing an older ebook, run
`compare.py epub old.epub new.epub` too. Notes become EPUB 3 pop-up footnotes; Greek and
Hebrew get `lang`. `cover_front.jpg` is cut from the compiled `cover.pdf`
(command in the book README). `books/.gitignore` ignores `*html`, so a new
`ebook-front.html` must be added once with `git add -f`; after that git
tracks its changes like any other file.

## Committing

Work on a branch, not `main`. Commit the TCP file, the TEI, `editorial.py`,
`review-report.md`, `chapters/typ`, the book files and any script changes.
Don't commit `/tmp` output, `__pycache__`, or intermediate HTML. Commit the
PDF and EPUB only if the book already tracks them (Perkins does).

## Decide vs ask

Decide yourself: n/m macrons and gaps that context settles (with evidence
notes), mechanical fixes, anything `verify.py` can prove.
Ask the user: the book's division structure and file names, gaps that need
a page image you couldn't get, anything that changes their reviewed text,
`MANUAL` entries that could be context-dependent, and the editor credit
(`build_tei.py --editor`, default "Courtney Allen Hicks").
