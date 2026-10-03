# Glorious Feast: review progress (checkpoint file)

Branch `glorious-feast-review`, worktree `.claude/worktrees/agent-a092f66ec11c0830a`.
Scratch (not in git): `$SP=/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/7734942a-5f8c-443c-b192-56f7915e6a6f/scratchpad/sibbes/`
- `auto/` = 1650 text, spelling modernized only (`tei_extract.py --only-auto`)
- `dp.txt` = pdftotext of the Digital Puritan PDF (Grosart's 1862 text with his
  "Qu." footnotes), from `~/Nextcloud/.../Richard_Sibbes/The Marriage Feast Between
  Christ and His Church/src/[RS] The Glorious Feast of the Gospel.pdf`.
  The Monergism PDF is NOT on disk.
- `rep.py EDITS.json` applies exact replacements to chapters/typ (e1..e10.json applied).

## Status
- All 10 files read and fixed (To the Reader, sermons 1-9).
- Plainly mistyped references applied: Prov 12:20->12:26, 1 Cor 4:25->14:25, Heb 15:12->4:12,
  1 Cor 15:82->15:32, Phil 3:10->3:20, John 7:34->6:34, Acts 10:4->9:4, 1 Cor 3:22->3:23 (ch4),
  1 Cor 3:22->3:22, 23 (ch9).
- Remaining wrong-verse references -> questions (see report draft below).

## Next step
Emendation-list scan (review-report.md) for OCR-type substitutions missed by slips.py;
consistency table; refs.py rerun; ./fgb build sibbes; pdftotext checks; write
source/proofread-report.md; final commit; handback.
