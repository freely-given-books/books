---
name: book-review
description: A thorough editorial review of a Freely Given Books edition's text, to make it shelf ready — proofreading chapters/typ against the early printed text and any modern witness, fixing OCR and scanning slips (he/be, b/h, "Gentles", "the church lied into the wilderness"), dropped or doubled words, broken quotations and punctuation, swallowed Typst semicolons, wrong scripture references, inconsistent spellings and headings, while understanding 16th–19th century English (hath, -eth, 'tis, shew, "prevent" meaning go before) and keeping it. Use this whenever the user asks to review, proofread, edit, check, clean up or "make shelf ready" a book, asks whether a book has errors or is ready to print, wants OCR errors fixed, or wants a book's text, headings, scripture references or consistency checked — even for one chapter, and even if the book is not yet on the TEI pipeline.
---

# Book review: making the text shelf ready

You are the edition's copy editor and proofreader. The goal is a text a
reader can trust: no scanning slips, no lost words, no broken quotations,
no wrong references, no inconsistencies a careful reader would notice — and
none of the period English damaged in the process. When you finish, the
user should be confident the book can go to print.

The books are early-modern and later Christian works (1600s Puritans,
Bunyan, Edwards, Spurgeon), edited *lightly*: modern spelling and
punctuation, the author's words and grammar kept. A more modern edition may
come later from the same TEI, so this review does not modernize grammar.

## What you work on

A book is `books/<author>/<book>/`. The text is `chapters/typ/*.typ`
(Typst); for TEI books, `source/<book>.tei.xml` holds the early printed text
and every editorial decision, and `./fgb sync <book>` folds edits in
`chapters/typ` back into it. **Edit only `chapters/typ`**, never the TEI or
the untouched source files. Read the book's `README.md`,
`source/editorial.py` (`REPORT_NOTES`), `source/review-report.md` and any
`source/witness-report.md` first: they record deliberate choices (Edwards
quotes the BSB; Brooks keeps Latin beside its translation; passages left
out on purpose) that a review must respect, not "fix".

Your sources of evidence, best first:

1. **The early printing**: the TEI's printed layer. `tei_extract.py
   <tei> OUT --layer reg --only-auto` gives it with spelling modernized and
   nothing else changed; `--layer orig` gives it as printed. `./fgb find
   <book> WORD` shows a word as printed and as decided; `./fgb page <book>`
   opens the side-by-side page.
2. **A modern witness** of the same text (CCEL, Monergism PDF, Chapel
   Library EPUB, an old copy): compared, never copied — some are under
   copyright and none is committed.
3. **The Bible** the book quotes (KJV unless the book says otherwise).
4. Your own reading, and `references/period-english.md` for what looks
   wrong but is not.

## The review, in order

### 1. Run the tools (minutes, finds the mechanical errors)

```sh
PY=$PWD/colophon/.venv/bin/python                    # at the repo root (uv; ./fgb makes it)
$PY colophon/sweep.py books/<author>/<book> --early   # spacing, punctuation, quotes, \; , words
$PY colophon/slips.py <tei> WITNESS                   # if there is a witness
$PY colophon/refs.py books/<author>/<book> --quotes [--bible bsb]
./fgb check <book> && ./fgb build <book>                 # verify, Lulu checks, epubcheck
```

`slips.py` lists where the edition departs from the early printing while
the witness agrees with it — the likeliest slips. `refs.py` lists references
to verses that do not exist and quotations that do not match the verse they
cite. Every hit is a candidate to read in context, not a fix to apply.

### 2. Read the book (the part the tools cannot do)

Read every file, start to finish, in passes of a few thousand words. Read
for sense, as a careful reader would. For each sentence ask: does it say
something? A sentence that does not parse usually hides a slip. Look for:

- **Scanning and OCR slips**: real words in the wrong place (`he` for
  `be`, `lied` for `fled`, `sold` for `soul`, `bead` for `head`, `title`
  for `little`, `form` for `for me`); the confusions are listed in
  `references/period-english.md`. Check each suspect against the early
  printing before changing it.
- **Lost and doubled words**: a sentence missing its verb or object, "the
  the", a list missing a member ("believe … plead … hope" in the print,
  two of three in the copy).
- **Quotations**: every opening mark closed, in the right direction, at the
  right place; a quotation's wording matching its source; nested quotes
  consistent. Typst curls straight quotes; a straight apostrophe inside a
  single-quoted passage closes it, so the book writes `’` there.
- **Punctuation**: doubled marks, a full stop mid-sentence ("lastly.
  didst"), a lost comma that changes the sense.
- **Latin, Greek and Hebrew**: misprints (`Sapieus miner` for `Sapiens
  miser`, `harebit` for `haerebit`), accents and breathings, and that a
  translation beside them says what they say.
- **Names**: the book's own form, consistently (Zion or Sion, not both;
  KJV forms for biblical names unless the book chose otherwise).

**A whole book (tens of thousands of words) is read by subagents**, the way
Brooks's *Precious Remedies* was (2026-10). Token use matters to the user,
so:

- Split the book into parts of about 20,000–25,000 words. Give each reader
  the same written brief: what to fix, what to ask, what never to change,
  and the evidence files (the edition, the `--layer orig` extraction, the
  witness). Brooks's brief is `references/reader-brief-example.md` and its
  applier `references/apply-proposals-example.py`; adapt the paths.
- Run the readers at **medium effort** (the Agent tool's `effort`), **one
  at a time**. Two Opus readers at once hit the session limit. At medium, a
  reader found as much as one at high (about 13–15 proposals per 1,000
  words, scrambled margins and mangled Latin included) for about 25% fewer
  tokens.
- Tell readers to keep lean: read each edition file once, Grep the 1653
  text and the witness only where they doubt, and write commands that need
  no permission (one plain command per call, no `cd &&` or shell variables).
- Readers **propose; they don't edit.** Each writes JSON lines (`file`,
  exact unique `old`, `new`, `class` fix/ask/note, `kind`, `why`), appending
  after every file so a usage cutoff loses little. Apply the `fix` lines
  with a script that refuses any `old` not found exactly once, then
  `./fgb sync` and `./fgb check`.
- A slip that repeats across the book (sentence case, a spelling the
  machine got wrong) is a machine rule in colophon or `editorial.py`, not
  hundreds of hand edits. Tell later readers not to propose it.
- Settle the `ask` items yourself at **high effort**, in one batch, and put
  them to the user grouped with recommendations. Record them in
  `source/proofread-report.md` so they survive the session.

### 3. Check what spans the book

- **Scripture references**: one style through the book (`Romans 11:20` or
  `Rom 11:20`, colon or period); each points at the verse it quotes; ranges
  and lists well formed (`11:20, 21`, `3:22-23`).
- **Consistency**: the same word spelled the same way throughout (every
  one/everyone, Saviour/Savior, shew/show, labour/labor, today/to-day),
  numbering styles, quotation-mark style, dashes, `etc.`. Build a table of
  variants with counts; propose the book's majority form.
- **Headings and titles**: chapter titles, the headings the edition adds,
  running-head short titles — consistent title case (lowercase articles,
  short prepositions and conjunctions), parallel wording within a series
  ("1. The Most Eminent Saints…", "2. Christ Much Exercised…"), no typos,
  short titles that fit one line (`./fgb pdf` warns when a running head
  breaks the top margin).

### 4. Fix and ask

**Fix yourself** what is unambiguous, and list it afterwards: misprints with
the early printing (or the witness) on your side, stray spaces, broken
quotation marks, swallowed semicolons, glued or doubled words, a
reference that is plainly mistyped (`1 Kings 17:4, G` → `17:4, 6`).

**Ask first**, with a recommendation, for anything that changes the
wording on purpose: restoring text the copy lost or cut, undoing an older
editor's change, a reading where the evidence is split, normalizing
variant spellings across the book, rewording a sentence that reads as a
mistake today ("other men, good wit" → "other men of good wit"), changing
a heading. Group the questions; show each with its context and the early
printing's reading.

Edit `chapters/typ` with exact, unique replacements (match across line
breaks; keep the file's wrapping). Mind Typst: `#`, `[`, `]`, `\` are
markup; write `\;` after a call like `#emph[..]`; keep `#footnote[..]`
anchors where they were. After each batch: `./fgb sync <book>` (it lists
the decisions that changed), then `./fgb check <book>`.

### 5. Prove it and report

Before calling a book shelf ready, all of these hold:

- `sweep.py` hits are fixed or explained; `slips.py` items resolved or
  listed as kept on purpose; `refs.py` shows no missing verses and every
  weak quote match read.
- `./fgb check` is OK; `./fgb build` passes the Lulu checks (footnote
  warnings explained) and epubcheck.
- The compiled PDF's text has no quotes curled the wrong way (`,‘ word`,
  `‘ `, `’’`) and no stray markup (`#emph`, `\[`).

Report to the user in plain words: what you fixed, by kind, with a few
examples each; the questions, with your recommendation; anything left as is
on purpose and why; and the checklist above. For a long list, write it to
`source/proofread-report.md` and summarize. Commit only when the user asks.
