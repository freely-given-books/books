# Checking CCEL against the 1845 printing — how it is done

CCEL's text of Beveridge's translation (keyed from the 1953 Eerdmans reprint)
has many slips. Each of our six volumes is compared word by word with the
1845 Edinburgh printing, and every real slip is corrected in `chapters/typ`
and folded into the TEI as an editor decision (`./fgb sync calvin`).

| our volume | contents | done | report |
|---|---|---|---|
| vol-1 | prefaces, Book I | 2026-10-11, 156 findings | `../witness-report-vol-1.md` |
| vol-2 | Book II | 2026-10-12, 226 findings | `../witness-report-vol-2.md` |
| vol-3 | Book III ch. 1–10 | 2026-10-12, 164 findings | `../witness-report-vol-3.md` |
| vol-4 | Book III ch. 11–25 | 2026-10-12, 244 findings | `../witness-report-vol-4.md` |
| vol-5 | Book IV ch. 1–13 | 2026-10-12, 75 findings (Book IV is keyed far more cleanly: no commas as "s") | `../witness-report-vol-5.md` |
| vol-6 | Book IV ch. 14–20 | not yet | |

## The 1845 printing (archive.org)

OCR text is kept in `source/*.djvu.txt` (git-ignored; fetch again with
`curl -sL -o ID.djvu.txt https://archive.org/download/ID/ID_djvu.txt`, retrying on a 500).
Page images: `https://archive.org/download/ID/page/n<N>_w1600.jpg`.

| 1845 volume | archive.org ID | holds | scan index N |
|---|---|---|---|
| 1 | `instituteschrist01calvuoft` | prefaces, Book I, Book II ch. 1–11 | printed page + 121 |
| 2 | `institutesofreli02calvuoft` | Book II ch. 12–17, Book III | printed page + 9 (Books II and III) |
| 3 | `institutesofthec03calvuoft` | Book IV | printed page + 3 |

OCR never reads Greek or Hebrew; read those on the page images.

## Step 1: the comparison (one background agent per volume)

Give the agent the brief below, with the volume filled in. It writes a
report (`scratchpad/calvin-volN-1845.md`, then copied here as
`../witness-report-vol-N.md`) with a table per chapter and one JSON line per
finding at the end:
`{"file", "anchor", "ccel", "1845", "proposed", "page", "kind", "confidence"}`.
Kinds: b (1845 words missing in CCEL), c (CCEL words not in 1845), d (a
different word), d/comma (a comma keyed as a final "s": "diligences against"),
e (Greek/Latin/Hebrew), f (reference numbers), n (notes), info (keep CCEL).
`agent/` holds the volume 2 agent's scripts (align.py, build.py, crop.py,
sgreek.py: paths inside point to its scratchpad; adapt them).

> Compare our edition of Calvin's Institutes (CCEL text) with the 1845 printing
> for our volume N (Book …, chapters …). Read-only; write the report as you go.
> Method: difflib alignment per .typ file after normalising (strip Typst markup,
> de-hyphenate, drop running heads and page numbers), footnotes separately;
> classify; read doubtful places on the page images (crop with ImageMagick,
> view with Read). The "ccel" field must be the EXACT text in the .typ file
> (curly quotes, the file's Greek encoding), occurring once. Do NOT list
> CCEL-wide style the edition keeps: Arabic references, CCEL's spellings,
> has/does/goes in Scripture quotations (the editor keeps CCEL's), CCEL's
> punctuation around references ("word (ref)."). DO list wrong words,
> commas-as-"s", missing/extra/displaced lines, wrong reference numbers
> (proposed in CCEL's Arabic style), Greek/Latin errors, Greek or Hebrew in
> font codes, stray note numbers. One plain command per Bash call, absolute
> paths, logic in script files run with `python3 -I`.

## Step 2: applying the report

From the repository root (`R` = the report, `T` = `books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-N`):

1. `python3 -I source/witness-check/apply.py R T --dry`, then without `--dry`.
   It applies each finding word by word (CCEL's words → 1845's), skipping any
   change that touches a numeral (reference style) or Typst markup (a "ccel"
   field can stop inside `#emph[`), and lists what it skipped.
2. The skipped ones by hand: write `[[file, old, new], ...]` as JSON (see
   `example-edits.json`) and run `python3 -I source/witness-check/edits.py T edits.json`
   (it tolerates curly or straight quotes and composed or decomposed Greek).
   For kind f, give the corrected number in CCEL's Arabic style.
3. `python3 -I source/witness-check/curl.py T`: curls straight double quotes
   a fix brought in from the 1845 text (vol-4 had 12).
   `python3 -I source/witness-check/reform.py T`: puts CCEL's decomposed
   Greek back wherever an edit wrote a whole file composed (otherwise every
   Greek word reads as an edit).
4. `./fgb check calvin` [2] shows any markup an edit broke. Look at the diff for 1845 punctuation brought in with a word fix
   ("magic, (Exod. 9:11)", "(αὐτός.)") and put it back in CCEL's style.
5. `./fgb sync calvin`, `./fgb check calvin` (must be OK), commit, `./fgb build calvin`,
   copy the volume's PDF, EPUB, cover and side-by-side page to Nextcloud.

## What CCEL gets wrong (so far)

- A comma keyed as a final "s": the commonest slip (50–60 a volume).
- Wrong words (glow/glory, axe/are, glamour/clamour, behaved/behoved).
- Lines displaced or dropped (I.8, I.11 note).
- Greek in an old Greek font's codes, as Latin letters ("filautiva kai;
  filoneikiva"), or in private-use characters (one word, I.13). A search of
  vols 3–6 found none, but look again in each.
- Hebrew as font codes with a false paragraph break after it (II.16).
- Summary items doubled (II.8 item 59); a section number keyed as the letter
  "l" ("l. The doctrine", so it is not set as a number) or replaced by a
  stray sentence (III.22 §2).
- Modern editors' notes from the 1953 reprint CCEL keyed, marked "100 D100"
  … "134 D134" (III.24–25 and Book IV, 35 in all): removed by
  `drop_modern_notes.py` (recorded as dropped notes). Watch in vols 5–6 for
  modern text without the marker, inside or after a Beveridge note.
- Section summaries without their markup (I.7, II.8 "29."); the converter now
  catches the second kind.

## The editor's decisions

- CCEL is the base. Its slips are corrected; its style is kept: Arabic
  references, its spellings, its modernised has/does/goes in Scripture
  quotations (2026-10-11: "lets keep CCELs this time"), its punctuation
  around references.
- References wrong in both CCEL and 1845 are corrected to the right verse.
- A note's page cross-reference to another printing names the passage instead.
- Only the public-domain notes of the 1845 printing go in (2026-10-12: "make
  sure none of the footnotes from the 1953 make it in"; "only the public
  domain footnotes from the older prints should go in"). The comparison agent
  lists any note, or part of one, that 1845 lacks; drop it.
