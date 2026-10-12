# CCEL books: what to watch for, and the check against the original printing

Read this for any book whose base is a CCEL ThML text (Owen, Bunyan,
Spurgeon, Calvin). CCEL is the user's preferred base, but its text is a
keying of some later reprint and it carries that reprint's slips, CCEL's own,
and sometimes copyrighted matter.

## Before building

- **Which printing did CCEL key?** Check its `DC.Source`/introduction. Calvin's
  Institutes is Beveridge's 1845 translation keyed from the **1953 Eerdmans
  reprint**: the reprint's apparatus (John Murray's introduction, page indexes)
  is not public domain or not useful. Leave it out (`SKIP_BLOCKS`) and tell the
  user; never publish an introduction by someone who died after ~1955.
- **Monergism copies can mix texts**: Monergism's Institutes is Beveridge's body
  under chapter titles that read as Battles's (1960, in copyright). A witness
  for the body only. sermonindex.net usually mirrors CCEL.
- **The original printing on archive.org** is the real witness: search
  `advancedsearch.php?q=title:(...)` for the edition CCEL follows (Goold 1850 for
  Owen, Beveridge 1845 for Calvin, M'Millan 1848 for Boston). Keep its OCR
  (`<ID>_djvu.txt`, git-ignored in the book's `source/`; archive.org sometimes
  answers 500, retry) and note the scan index offset (image `n<N>` = printed
  page + k; it can differ between volumes).
- **Size.** Count the words per top division. Over ~150,000 words the book
  goes in volumes, cut like Gouge: Calvin (700k words) is six volumes of
  250–400 pages at 10.5pt. Calvin's `source/make_volumes.py` writes each
  volume's print file, cover and ebook front from the `LAYOUT`, so a change of
  split or titles is one command.

## CCEL quirks the converter now handles (colophon 0.10.0)

`thml_to_tei.py` and `teitok.py` learned these on Calvin; check a new book for
their cousins with `tcp_structure.py` and a first `./fgb check`:

- Greek with **decomposed accents** (letter + combining mark). Combining marks
  are word characters on both sides now; before that, every Greek word read
  as an editor's edit.
- `p.introHead` (a chapter title under "CHAPTER 2.") is a head; `p.intro`
  section summaries under "Sections." are one inset `argument` (across page
  breaks); `<hr>` and empty `<p/>` are dropped (an empty `<p/>` gave
  "skipped merge" lines).
- TEI allows `argument` only before a division's text: a stray paragraph
  between summary items, or a title left as a plain `p`, makes the TEI invalid
  (`./fgb check` [4]). Fix the encoding, not the schema.
- `font-variant:small-caps` spans (Goold's Owen) are small caps like `span.sc`;
  the book sets `SMALLCAPS = "smallcaps"` (Libertinus has real ones).

## CCEL defects to look for in the text (found in Calvin and Owen)

- **A comma keyed as a final "s"**: "the utmost diligences against" for
  "diligence, against". The commonest slip: 30–60 per 100,000 words.
- **Wrong real words**: glow/glory, axe/are, glamour/clamour, behaved/behoved,
  retake/betake, Ahab/Ahaz, levity/lenity. Only a comparison finds these.
- **Dropped, displaced or doubled lines**, including in notes and in the
  section summaries (a summary item doubled; "three persons" dropped).
- **Greek in font codes**: Latin letters from an old Greek font
  ("filautiva kai; filoneikiva" = φιλαυτία καὶ φιλονεικία; v = acute,
  j/J = breathings, ” = final sigma), or private-use characters (U+F000+, an
  SPIonic run). Search: `grep -P '[\x{E000}-\x{F8FF}]'`, and a pattern for a
  vowel + v + consonant. Read every one on the page image.
- **Hebrew in font codes**, each followed by a **false paragraph break** that
  splits the sentence (Calvin II.16); CCEL may say it has no Hebrew at all.
- **Wrong reference numbers**; some are the original printing's own misprints
  (correct them too, saying so).
- **Classes missing** on one chapter (its title and summaries plain paragraphs):
  fix by hand in `chapters/typ` (`#block(inset: (x: 1em))[...]`), recorded as
  editor decisions.

## The check against the original printing

Calvin's `source/witness-check/README.md` is the worked procedure (agent
brief, report format, scripts); copy it for the next book. In short:

1. **One background agent per volume** (~100k words), read-only, writes a
   report with one JSON line per finding: `file`, `anchor`, `ccel` (the exact
   text in the .typ file, curly quotes and Greek encoding as they are, unique,
   never cut inside `#emph[`), `1845` (the printing's text), `proposed`,
   `page`, `kind` (b missing words, c extra, d wrong word, d/comma, e
   Greek/Latin/Hebrew, f references, n notes, info keep CCEL), `confidence`.
   It aligns OCR and edition with difflib and reads doubts on the images.
   Tell it what NOT to list: the style the edition keeps (below).
2. **Apply** with Calvin's scripts: `apply.py` (word-level; skips numerals and
   markup), then the rest by hand as `[file, old, new]` JSON with `edits.py`
   (quote- and NFC/NFD-tolerant), then `reform.py` (puts CCEL's decomposed
   Greek back where an edit recomposed a file). Look at the diff for the
   printing's punctuation creeping in ("magic, (Exod. 9:11)"); `./fgb check`
   [2] shows broken markup. Then `./fgb sync`, `./fgb check`, build, Nextcloud.
3. Keep the report as `source/witness-report-vol-N.md`, update the status table
   in the README, and commit per volume.

## What the edition keeps from CCEL (the user's decisions on Calvin)

CCEL's slips are corrected; CCEL's **style** stays: Arabic numerals in
references, its spellings, its punctuation around references ("word (ref)."),
and even its modernised "has/does/goes" in Scripture quotations where the
printing has "hath/doth" ("lets keep CCELs this time"). Ask the user about
any such systematic difference before changing it book-wide. For Owen the
user ruled the other way on *wording*: the author's own first-edition word
beats a later editor's (Goold), so ask per book.
