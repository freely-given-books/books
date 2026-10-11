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

Contributions are welcome! Books should be submitted in one of the following formats:

- **Typst** (`.typ`) — preferred
- **AsciiDoc** (`.adoc`)
- **LaTeX** (`.tex`)

### Other Sources

If you have a book that is already in some other format such as an ebook or PDF,
or if you have some sort of Word document, please contribute it to the website project.

## Building

Clone with the Typst templates (a submodule):

```sh
git clone --recursive https://github.com/freely-given-books/books.git
# or, in an existing clone:
git submodule update --init typst/fgbooks-typst
```

Books on the TEI pipeline build with one command, into `dist/` (PDFs and
EPUBs are not kept in git):

```sh
./fgb build              # every TEI book
./fgb build perkins      # one book
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

## TODO

[x] Embed typst template in project and update commands to use the fgbooks template
[x] Instead of committing ebooks and PDFs, create a workflow that builds packages
    (`./fgb build`, for books on the TEI pipeline)
