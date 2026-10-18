# Proofreading Bunyan, *Grace Abounding to the Chief of Sinners*

You are the copy editor of a light, faithful modern-spelling edition of John
Bunyan's *Grace Abounding* (Bunyan's enlarged text, as he left it by 1688).
The base text is CCEL's, a 19th-century keyed text; it has been proofread
once (2026-10-02) and those fixes are in place. This is a second, careful
pass so the book can go to print. You **propose** fixes in a file; you do
NOT edit any book file.

## Files

- The edition (what you proofread), Typst markup:
  `/home/courtney/Projects/fgbooks/books/books/john-bunyan/grace-abounding/chapters/typ/<file>.typ`
  `#emph[...]` italic, `#smallcaps[...]` small capitals (Bunyan's emphasis),
  `#footnote[...]`, `\` escapes (`1\.` is a paragraph number), `==` a
  heading. Leave markup alone unless it is the error.
- The previous proofread, what was already decided (do not re-propose these):
  `/home/courtney/Projects/fgbooks/books/books/john-bunyan/grace-abounding/source/proofread-report.md`
- Witness 1, the 1666 first edition (EEBO-TCP A30143), plain text, old
  spelling, one paragraph per blank-line block. It lacks Bunyan's later
  additions (about 9,000 words), and Bunyan revised some wording later, so
  a difference is not by itself an error:
  `/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/244a32ab-28d3-4210-886c-be97e0b49ab1/scratchpad/ga/1666.txt`
- Witness 2, George Offor's edition (1855), the enlarged text, as archive.org
  OCR (two-column pages, so OCR noise: "tlie" = "the", "mj" = "my", running
  heads and Offor's footnotes mixed in). It has the later additions, so it is
  the witness for passages not in 1666:
  `/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/244a32ab-28d3-4210-886c-be97e0b49ab1/scratchpad/ga/offor-1855.txt`
- Where the edition already differs from 1666 at length (Bunyan's additions):
  `/home/courtney/Projects/fgbooks/books/books/john-bunyan/grace-abounding/source/witness-report.md`
  (skim only if needed).
- Period English guide (read it first):
  `/home/courtney/Projects/fgbooks/books/.claude/skills/book-review/references/period-english.md`

Use the Read tool on these files, and Grep to find a passage in the
witnesses (search for 2-3 distinctive words; OCR may garble one). If you
need a shell command, use one plain command per call with absolute paths: no
`cd … &&`, no shell variables, no `for` loops, no `$(…)`. Put any logic in a
script file under
`/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/244a32ab-28d3-4210-886c-be97e0b49ab1/scratchpad/ga/proof/`
and run it with `python3 /that/path/script.py`. Be lean: read each edition
file (or your part of it) once, in chunks; consult the witnesses only where
you doubt.

## The book's style (keep it; flag departures from it)

- Paragraphs numbered as Bunyan numbered them: `1\.`, `2\.` … in order, none
  skipped or doubled (check this).
- Scripture quoted in single curly quotes ‘…’; spoken words in double “…”.
  References in parentheses after the quotation, Arabic chapter, period
  separator: `(Eph. 2.2, 3)`, `(Heb. 12.22-24)`, `(1 Sam. 16.14)`,
  `(Ps. 109.6-20)`. Book numbers Arabic (1 Cor., not I Cor.).
- He/Him/His for God and Christ capitalized in Bunyan's own sentences;
  quotations keep the KJV's lowercase.
- British spelling as CCEL has it (labour, saviour, honour); period words
  kept (forasmuch, overstood, holloa, "an hedge", -eth, -est, hath, doth).

## What to look for

Read every paragraph for sense, as a careful reader. A sentence that does
not parse usually hides a slip. Check every doubtful place against 1666
and/or Offor.

Fix (class `fix`), with the evidence on your side:
- **Keying/OCR misprints** in CCEL: real words in the wrong place (he/be,
  lie/he, sins/fits, world/word, form/for me, l/I, 1/I), letters swapped.
- **Lost or doubled words**, a clause missing that both witnesses have,
  "the the".
- **Punctuation**: unclosed or wrongly curled quotes (‘ for ’ in ’twas,
  ’tis), a full stop mid-sentence, doubled marks, a capital after a
  semicolon or colon where it is a keying quirk (only if clearly a slip,
  as "now; Those scriptures" — mark these `ask` if many), a lost comma that
  changes the sense, stray spaces.
- **Scripture references**: wrong verse for the quotation (check the KJV
  from memory and the witnesses), malformed (`Heb 4.16` missing its stop,
  `I Cor.`), a quotation's wording garbled against the KJV where Bunyan
  plainly quotes it (Bunyan often paraphrases: then leave it).
- **Scripture quotations not in quotation marks** where the book elsewhere
  quotes the same kind of passage — propose as `ask`, kind `quotes`.
- Spelling variants: an old spelling next to modern text in one place only.

Ask (class `ask`): anything that changes wording on purpose, or where the
witnesses split; a sentence that reads as a mistake but may be Bunyan; a
place where CCEL differs from both 1666 and Offor in wording (is CCEL's
reading a slip?).

Do NOT change: period grammar and words, Bunyan's later revisions (if Offor
agrees with the edition against 1666, it is Bunyan's revision, keep it),
italics, the reference style, anything only a modernizing editor would
change. When in doubt, ask rather than fix; when it is plainly fine, say
nothing.

Also note (class `note`, no change) spelling variants used two ways in your
part (e.g. Sion/Zion, shew/show, gaol/jail, burthen/burden, to-day/today),
with counts.

## Output

Append as you go (after every ~40 paragraphs, so a cutoff loses little) to
the JSON-lines file
`/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/244a32ab-28d3-4210-886c-be97e0b49ab1/scratchpad/ga/proof/<PART>.jsonl`,
one object per line:

```
{"file": "relation.typ", "old": "exact text in the edition file", "new": "replacement", "class": "fix", "kind": "misprint", "why": "§57; 1666 'yet'; Offor 'yet'"}
```

- `old` must occur **exactly once** in that file, copied exactly (markup,
  curly quotes ’ ‘ “ ”, spacing). Short, but unique. Never let `old` or
  `new` end inside `#emph[` or another markup call.
- `kind`: misprint, words, punctuation, quotes, reference, spelling,
  numbering, other.
- Start `why` with the paragraph number (§57).

When done, run a script that checks every `old` occurs exactly once in its
file; fix any that don't. Then reply in under 250 words: counts by class
and kind, the `ask` items in one line each, and anything notable.
