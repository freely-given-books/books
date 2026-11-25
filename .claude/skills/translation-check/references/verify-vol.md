# Brief: second opinion on proposed corrections to Beveridge's Institutes (volume {N})

Freely Given Books is preparing a corrected Beveridge (his 1845 English Institutes, put right only
where he really departs from Calvin's 1559 Latin) as the base for a Modern English edition. A first
reader went through the Latin and proposed fixes. You are the second reader. Judge each proposal on
its merits. The first reader can be wrong in either direction: calling harmless freedom an error,
misreading the Latin, or making a "fix" that is itself inaccurate or clumsy.

## Files
- The proposals: `~/Projects/fgbooks/work/institutes/latin/vol{N}/compare/fixes-<PART>.json`, where the
  prompt names the parts. Each has `id`, `chapter`, `section`, `kind`, `severity` (A = Calvin's meaning
  changed or lost; B = a smaller loss or tilt), `old` (exact Beveridge text), `new`, and `why`.
- The Latin: `vol{N}/la/<file>.md`, with parts `.part-a.md` and `.part-b.md` where a chapter is split. Page
  images are in `vol{N}/pages-la/`.
- Calvin's French of 1560, the tiebreaker: `vol{N}/fr/<file>.md`.
- Beveridge: `~/Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-{N}/<file>.typ`.
  It has just been corrected against the 1845 print, which is why it has hath and doth.
- Allen's English: `~/Projects/fgbooks/work/institutes/allen/ioanniscalviniin01calv.txt`.
- The editor's decisions so far: fix A and B; Beveridge's inline cross-references go to footnotes marked
  "(Beveridge's note.)"; his chapter synopses stay (unlabelled). Model verdicts: `pilot/fixes-verified.json`.

Don't read the `compare-*.md` reports. Form your own view from the texts.

## For each proposal decide
- `accept`: Beveridge really departs from the Latin, and the fix is accurate and minimal.
- `adjust`: the departure is real, but the fix needs changing. Give your `new`, and keep `old` exact.
- `downgrade`: the departure is real but only harmless freedom (C). No fix.
- `reject`: Beveridge is right, or defensible given the Latin or the French.

Also check that each fix:
- fits Beveridge's sentence grammatically;
- keeps his register (no modernizing);
- doesn't echo Battles or McNeill (copyrighted translations). If a fix reads like a phrase you know
  from Battles, reword it literally.

Finally, read each chapter's Latin once yourself, section by section. Look for **A-level departures
the first reader missed** and add them in the same format (`verdict: "new"`), with `old` exact and
unique in its chapter file.

## Output
Write `vol{N}/compare/verified-<PART>.json`, one file per part. Include every proposal, in the original format
plus `verdict` and `note` (one line, why). For `adjust` items, `new` should be your version. Keep
severity as the first reader set it, unless you have reason to change it, and say so in the note.
Use the Write tool, or a Bash heredoc if Write is refused. If both fail, return the JSON in your
message.

Final message: counts per verdict, plus the 3-5 cases where you disagreed most, in one line each.
