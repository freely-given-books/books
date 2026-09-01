# John Gill on 1 & 2 Timothy

John Gill's verse-by-verse exposition of both Epistles to Timothy, set for
6×9in print. **PDF only** — there is no ebook edition. 216 pages.

## Building

```
typst compile 1-and-2-timothy.typ
```

The generated chapter files are committed, so that is all a plain rebuild
needs. To regenerate them from the JSON in `src/`, or after changing the
shared template:

```
../../../../scripts/gill_build_volume.py 1TI 2TI \
    --slug 1-and-2-timothy --title "1 & 2 Timothy"
```

That re-runs the whole pipeline — fetch (cached), convert, compile, and write
`review.md`. It leaves this `README.md` and `1-and-2-timothy.typ` alone, so
hand edits to the front matter survive.

See `../REVIEW.md` for how the conversion works and what to check in
`review.md`.

## Layout

- `commentary.typ` — the template. Written for this book rather than reusing
  `@local/fgbooks`, because a commentary is entered at a verse rather than read
  front to back: the text is divided by verse, each verse carries its reference
  and the King James text, and the recto running head names the book and the
  verses opened on that page. Each epistle is a part, with its own title page,
  Gill's introduction, and chapters.
- `chapters/` — generated Typst, one directory per epistle.
- `src/` — the JSON as fetched, kept so the build is reproducible offline.

## Sources

- Commentary: John Gill, *An Exposition of the Old and New Testament*
  (1746–1763), public domain, via https://bible.helloao.org/api/c/john-gill/.
- Scripture: the King James (Authorized) Version, via the same API.

The API serves each verse's comment as one plain-text blob with no markup.
Gill opens every paragraph with the slice of Scripture he is about to expound;
in the first paragraph that slice is marked by a trailing `....`, and
afterwards it is only recoverable by matching the paragraph against the verse
itself, which is what the converter does. 645 of 686 comment paragraphs are
matched this way; the rest are places where Gill carries his own prose on
past a quotation, and correctly have no bolded lemma.

Two defects in the source data are worth knowing about:

- The API has no entry for 1 Timothy 5:12 — the comment filed under it is
  actually on 5:13. The converter follows the lemmas rather than the labels, so
  that entry is set as a single `5:12–13` block carrying both verses' text, and
  no Scripture goes missing.
- Hebrew and Greek words are stripped from the text before the API serves it,
  leaving a handful of small gaps in Gill's prose ("opposed to, *one strong in
  the law*"). Nothing can be done about this short of a different source.
