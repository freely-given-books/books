# Glorious Feast: review progress (checkpoint file)

Branch `glorious-feast-review`, worktree `.claude/worktrees/agent-a092f66ec11c0830a`.
Scratch (not in git): `$SP=/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/7734942a-5f8c-443c-b192-56f7915e6a6f/scratchpad/sibbes/`
- `auto/` = 1650 text, spelling modernized only (`tei_extract.py --only-auto`)
- `dp.txt` = pdftotext of the Digital Puritan PDF (Grosart's 1862 text with his
  "Qu." footnotes), from `~/Nextcloud/.../Richard_Sibbes/The Marriage Feast Between
  Christ and His Church/src/[RS] The Glorious Feast of the Gospel.pdf`.
  The Monergism PDF is NOT on disk (not in the main checkout or Nextcloud).
- `rep.py EDITS.json` applies exact replacements to chapters/typ.

## Tools
- sweep.py --early: 63 hits, all period/British words (savour, -eth, camphire...). OK.
- slips.py vs Grosart/Digital Puritan: 31 places, in `$SP/slips.txt`; handled per file.
- refs.py --quotes: 266 refs, 3 missing (ch7 1 Cor 4:25, Heb 15:12; ch8 1 Cor 15:82),
  24 weak; in `$SP/refs.txt`. Reference fixes are batched: see below (NOT yet applied).

## Files read
- tothereader.typ: done, fixed
- chapter1-8.typ: done, fixed
- chapter9.typ: NOT yet read

## Fixed so far
- Misprints: needs he wonderful -> be (ch1); truths he pressed -> be (ch3); when be looketh -> he (ch5);
  moveth its -> us (ch5); vale of ignorance -> veil (ch3); the way's of wisdom -> ways (ch2);
  aqua vita: -> aqua vitae (ch2, 1650 Aquavitae).
- Quotes: ch1 'not to be high-minded, but fear;' closed; ch4 'let this cup pass from me;' closed.
- Punctuation: ",'." after dropped &c. (ch1 x2) -> ".'"; "?." (ch1); "glory 'In" -> "glory. 'In" (ch1);
  "grief And" / "hereafter, If" (ch5); "employments but" (ch4); "Mat 22:4  for" -> "Mat 22:4, for";
  double spaces (To the Reader); "gaudy - day" -> gaudy-day; "holy-feast" -> holy feast.
- ch5 "men break the law" -> "brake" (1650 and Grosart; "break" changed the tense).
- ch5 anymore -> any more (Isa 1:5 sense).
- References: "1Cor. xv." -> "1 Corinthians 15" (ch4); "1\nCorinthians", "2\nSamuel" rejoined.

## Reference fixes to apply (editor-added refs pointing at wrong verse)
- tothereader: 1 Samuel 31:9 (head of Goliah) -> 17:54; 2 Corinthians 12:9 (spirit of glory rests) -> 1 Peter 4:14
- ch2: John 7:34 -> 6:34; 2 Samuel 19:32 (Barzillai) -> 19:35
- ch3: 2 Corinthians 6:14 ('darkness itself') -> Ephesians 5:8
- ch4: Colossians 2:10 -> 2:14, 15; Romans 5:21 -> 5:10; 1 Cor 3:22 ('You are Christ's') -> 3:23;
  Ephesians 1:8 -> 2:6; Romans 6:7 -> 8:2
- ch5: Acts 10:4 -> 9:4

## Needs your decision (draft)
1. Restore "etc." where 1650 has "&c." after a quotation (ch1 x2, ch3, ch6, ch8, ch9)? rec: no, keep as is (old editor dropped them), punctuation tidied.
2. ch3 "and where it is taken off there is none of it" -> "where it is not taken off" (Grosart Qu.; sense requires). rec yes.
3. ch3 "God doth take away his veil" -> "this veil" (Grosart Qu.). rec yes.
4. ch3 "to see the things that to nature are visible" -> "invisible" (Grosart Qu.). rec yes.
5. ch4 "but removal of it ever may damp the feast" -> "removal of whatever may damp the feast". rec yes.
6. Spellings: "high price of God's calling" (ch3) -> prize (Phil 3:14); "troubles and combers" (ch4) -> cumbers;
   Sampson -> Samson, Goliah -> Goliath (To the Reader). rec: prize, cumbers yes; names keep? decide.
7. Reference style: Mat/Philip/Ephes/2 Chron vs full names (Isaiah, Romans...). rec: write out (Matthew, Philippians, Ephesians, 2 Chronicles).
- ch3 "intritively" (x3; 1650 same; Grosart Qu. intuitively). rec: intuitively?

## Next step
Read chapter9.typ, fix, sync, check, commit after each.
Then apply reference fixes, consistency table (practise/practice verb, Aye/Ay, Austin, St), build, report.
