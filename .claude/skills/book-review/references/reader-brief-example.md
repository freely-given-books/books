# Proofreading Brooks, *Precious Remedies Against Satan's Devices*

You are the copy editor of a light, faithful modern-spelling edition of
Thomas Brooks's *Precious Remedies against Satans Devices* (2nd edition,
London 1653, EEBO-TCP A77614). The text has been through a machine pass:
spelling modernized, capitals lowercased, gaps filled, margin notes set as
footnotes, the margin's "1 Remedy." labels dropped. Your job is to find
what is still wrong, so the book can go to print. You **propose** fixes in
a file; you do NOT edit any book file.

## Files

- The edition (what you proofread):
  `/home/courtney/Projects/fgbooks/books/books/thomas-brooks/precious-remedies-against-satans-devices/chapters/typ/<file>.typ`
  It is Typst markup: `#emph[...]` is italic, `#footnote[...]` a footnote,
  `#strong[...]` a bold run-in head, `\` escapes. Leave the markup as it is
  unless it is the error.
- The 1653 printing, as printed (long s, old spelling), same file names:
  `/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/87818929-be21-55ca-9ebd-88c68d957bb7/scratchpad/orig/<file>.typ`
- A modern witness, Grosart's edition (1866) via Monergism, plain text:
  `/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/87818929-be21-55ca-9ebd-88c68d957bb7/scratchpad/wit/monergism.txt`
  Grosart modernized lightly, put scripture references in brackets and
  moved notes into the text. It is evidence, never a text to copy: our
  edition keeps Brooks's 1653 wording.
- Period English guide (read it first):
  `/home/courtney/Projects/fgbooks/books/.claude/skills/book-review/references/period-english.md`

Use the Read tool on these files. Use Grep to find a passage in
monergism.txt. If you need a shell command, use one plain command per call
with absolute paths: no `cd … &&`, no shell variables, no `for` loops, no
`$(…)`. Put any logic in a script file under
`/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/87818929-be21-55ca-9ebd-88c68d957bb7/scratchpad/proof/`
and run it with `python3 /that/path/script.py`.

## What to look for

Read every paragraph and footnote of your files for sense, side by side
with the 1653 text, and check doubtful places against Grosart.

Fix (class `fix`) — clear errors, with the evidence on your side:
- **Printer's and keying misprints** in 1653 that the machine carried
  over: "underastanding", "Nevertherless", "covevenant", "ignonorance",
  letters swapped or doubled, "cho isest" split words, "theis" for
  "their", "nor" for "not", "u/n" confusions ("loueth" for "loveth").
- **Words the machine left unmodernized or modernized wrongly**: an old
  spelling next to modern text ("loueth", "Ambassadours", "subtill"), a
  verb taken as a noun ("cloth us" → "clothe us"), a possessive printed
  without its apostrophe ("Gods love" → "God's love", "the Saints
  graces" → "the saints' graces").
- **then / than**: 1653 often prints "then" for "than" ("better then",
  "more then", "rather … then"). Modernize to the sense; likewise "loose"
  meaning "lose", "of" meaning "off", "to" meaning "too", "least" meaning
  "lest" where the sense is plain.
- **Doubled or lost words, stray or doubled punctuation**, a full stop in
  mid-sentence, "life,,".
- **Scripture references** that are wrong: a verse that does not fit the
  quotation, a garbled one ("the 12 Rom. 9." = Rom. 12. 9.; "1 Pet. 15.
  16" = 1 Pet. 1. 15, 16), digits misprinted. Check against the KJV and
  Grosart. Keep the book's reference style (`Rom. 12. 9.`); only fix what
  is wrong.
- **Latin, Greek and Hebrew** misprints: fix to the standard text
  (Augustine, Bernard, Seneca, the Vulgate, the Greek NT, LXX, Hebrew
  Bible); keep Brooks's word order. Greek needs correct accents and
  breathings. Known: "Nonματα" should be "Νοήματα"; "מוסרΠαιδεία" needs a
  space between the Hebrew and the Greek. The Greek/Hebrew notes listed
  at the end of
  `/home/courtney/Projects/fgbooks/books/books/thomas-brooks/precious-remedies-against-satans-devices/source/gap_fixes.py`
  give the printer's errors found so far (e.g. "μετα" → "μετά", "των
  λοιμων" → "τῶν λοιμῶν"); propose the correction where it falls in your
  files.
- Spacing errors: "seleternals" (sell eternals), "bemerry", glued words.

Ask (class `ask`) — anything that changes the wording on purpose, or where
the evidence is split: a sentence that reads as a mistake but may be
Brooks; a reading where 1653 and Grosart disagree and neither is plainly
right; a name form.

Do NOT change: period grammar (hath, doth, -eth, thou, ye, "these be",
"an hope"), old words still in use or with changed meaning (see the
guide), Brooks's own word choices, his Latin beside its translation, the
book's reference style, italics, or anything only a modernizing editor
would change. When in doubt, don't propose it.

Also note (class `note`, no change) spelling variants you see used two ways
in your files (e.g. "Sathan"/"Satan", "burthen"/"burden", "shew"/"show"),
with counts, for a book-wide consistency pass.

## Output

Write, appending as you go (every file or two, so a cutoff loses little),
the JSON-lines file
`/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/87818929-be21-55ca-9ebd-88c68d957bb7/scratchpad/proof/<GROUP>.jsonl`,
one object per line:

```
{"file": "sin-01.typ", "old": "exact text in the edition file", "new": "replacement", "class": "fix", "kind": "misprint", "why": "1653 'underastanding' (keying); Grosart 'understanding'"}
```

- `old` must occur **exactly once** in that file and be copied exactly
  (including markup, curly ’ apostrophes and spacing). Keep it short, but
  give enough context to be unique (a few words around the error).
- `kind`: misprint, modernize, then-than, possessive, words, punctuation,
  reference, latin, greek, hebrew, spacing, other.
- `class`: fix, ask or note (for note, `old`/`new` may be empty).

When done, run a script that checks every `old` occurs exactly once in its
file. Fix any that don't. Then reply in under 250 words: counts by class
and kind, the `ask` items in one line each, and anything notable.
