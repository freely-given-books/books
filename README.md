# Books

A collection of books for the [Freely Given Books](https://books.freely.giving) project.

## Finished books

`main` is where books are worked on, so it also holds books that are not
finished. For finished books only, use the **`stable`** branch:

```sh
git clone --recursive -b stable https://github.com/freely-given-books/books.git
cd books && ./fgb build
```

Every book on `stable` has been signed off by the editor with a signed tag
(`<author>/<book>/vN`) and is exactly as it was signed off. Its
`CATALOG.md` lists each book with its source and the checksum of that
source, and each release on GitHub has the built PDFs and EPUBs with a
`SHA256SUMS` file. To check a sign-off yourself:

```sh
git -c gpg.ssh.allowedSignersFile=allowed_signers tag -v <author>/<book>/vN
```

## Contributing

Contributions are welcome: a typo fixed, a wrong scripture reference, a
dropped word, or a whole new book. Every book here is **Typst**. Books
in other formats (an ebook, a PDF, a Word document) belong to the
[website project](https://books.freely.giving) instead.

### How a book is made

Most books are built from an early printed source (an EEBO-TCP
transcription or a CCEL text) by **colophon**, the pipeline in the
`colophon/` submodule. Each book folder, `books/<author>/<book>/`, holds:

| Path | What it is |
| --- | --- |
| `chapters/typ/*.typ` | the edition's text, one file per chapter: **edit here** |
| `<book>.typ`, `cover.typ` | the print edition and its cover (they import the `@local/fgbooks` template) |
| `source/<ID>.tcp.xml`, `source/<work>.thml.xml` | the source, untouched: never edit it |
| `source/<book>.tei.xml` | the master: the source plus every editorial decision, written by `./fgb sync` |
| `source/editorial.py` | the book's settings |
| `README.md` | where the text comes from and what this edition does with it |

`./fgb list` names the books on the pipeline. The 1689 Confession is
plain Typst outside it; edit its `.typ` files directly.

### Fixing the text

1. Find the place: `./fgb find BOOK WORD` shows where a word is, as printed
   and as the edition reads it; `./fgb page BOOK --open` sets the printed
   text and the edition side by side.
2. Edit `chapters/typ`. Text, italics (`_..._`, `#emph[...]`), footnotes,
   `#quote[...]` and headings are all kept. Layout commands
   (`#linebreak()`, `#pagebreak()`, `#v(...)`, `#par(...)`) are not: they do
   not belong in `chapters/typ`.
3. `./fgb sync BOOK` folds your edit into the TEI as an editor decision and
   shows what changed. Commit both `chapters/typ` and the TEI.
4. `./fgb check BOOK` must pass: `chapters/typ` has to be exactly what the
   TEI gives back, so the print book and the ebook cannot drift apart.
5. Open a pull request saying what you changed and why (the page, the
   witness you checked against).

Keep the old words: *hath*, *-eth*, *'tis*, *shew* and the like are the
author's, not mistakes. A book that has been signed off (see
[Finished books](#finished-books)) goes back to not finished when its folder
changes, until the editor signs it off again; that is expected.

### A new book

Open an issue first with the title and the source you have in mind
(an EEBO-TCP `A#####` number, a CCEL link). The steps are in
`CLAUDE.md` and `.claude/skills/eebo-tcp-book/SKILL.md`; colophon's own
notes are in `colophon/CLAUDE.md`.

### Changes to the tools

colophon and the Typst templates are submodules with their own
repositories ([colophon](https://github.com/freely-given-books/colophon),
[fgbooks-typst](https://github.com/freely-given-books/fgbooks-typst)), and
this repository pins each to a release tag. Send changes there; `CLAUDE.md`
has the release steps.

## Building

You need git, [uv](https://docs.astral.sh/uv/) and
[Typst](https://typst.app). [epubcheck](https://www.w3.org/publishing/epubcheck/)
(with Java) checks the EPUBs when installed; without it `./fgb` says it
skipped the check.

Clone with the submodules (colophon and the Typst templates):

```sh
git clone --recursive https://github.com/freely-given-books/books.git
# or, in an existing clone:
git submodule update --init
```

Books build with one command, into `dist/` (PDFs and EPUBs are not kept in
git). `./fgb` sets up colophon's Python environment itself the first time:

```sh
./fgb build              # every book on the pipeline
./fgb build perkins      # one book, by part of its name
./fgb --help             # everything else
```

### The Typst templates

`@local/fgbooks` and `@local/fgbooksLBCF` come from
[fgbooks-typst](https://github.com/freely-given-books/fgbooks-typst), checked
out at `typst/fgbooks-typst`. Each release is a tag there (`0.5.2`;
`fgbooksLBCF-0.1.0` for any other package), and a book pins its version in
its import. `./fgb` unpacks every imported version from its tag into
`~/.cache/fgb-typst/packages` and points Typst at it, so nothing has to be
installed by hand. `./fgb packages` lists them and shows how to use them with
`typst` or an editor outside `./fgb`.

A new template version: commit in `typst/fgbooks-typst`, bump `typst.toml`,
tag it, push; then commit the submodule's new position here. While it is
untagged, a book importing the version in the working copy's `typst.toml`
builds against the working copy.
