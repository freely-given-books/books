# The Pilgrim's Progress: proofreading report

A full read of `chapters/typ`: the Apology, Part I (stages 1–10 and the
Conclusion) and Part II (the title page, The Author's Way, To the Reader
and stages 1–8), all read for sense. The base text is CCEL's (the user's
preference). Part I was checked against the 1678 first edition
(`A30170.witness.xml`) and the KJV. The repo has no early printing of Part
II. Its suspect places were checked against sense and, for the questions
below, against a second modern copy (biblebb.com, *Pilgrim's Progress
Part 2*), which is compared only and not committed.

## Needs your decision

**Decided 2026-10-03 and applied** (synced, check OK 23/23, rebuilt: 404 pages,
epubcheck clean): 1 the lost words in Part II stage 4 restored ("and they sent
for him, and he came. When he was entered the room"); 2 the three Author's Way
lines restored; 3 Formalist in Part I stage 3; 4 Immanuel; 5 Hymenaeus; 6
aught (×2); 7 wholesome, lilies, befall, skull, Apostasy, stayed, show; 8
Savior (×8); 9 Mount Sion kept; 10 Standfast's speech joined: `build_tei.py`
now runs a paragraph on into the last paragraph of the speech before it (every
book's TEI rebuilds unchanged); 11 the user found a 1732 printing of Part II (see "Part II witness" below).

1. **Words CCEL lost in Part II, stage 4** (Christiana and the sick boy).
   CCEL has "So Christiana desired it, and entered the room, and had a
   little observed the boy, he concluded". The biblebb copy (and the
   standard 1684 text) has "So Christiana desired it, and they sent for
   him, and he came. And when he was entered the room, and had a little
   observed the boy, he concluded". **Recommend:** restore it.
2. **Verse lines CCEL shortened in The Author's Way** (Part II). The
   biblebb copy reads:
   - "Are nothing else but groundless fears" → "but ground for groundless fears"
   - "Things of greater bulk" → "Things of a greater bulk"
   - "love him at first" → "love him at the first"

   All three restore the metre. **Recommend:** restore them.
3. **"Formality and Hypocrisy"** (Part I, stage 3; Part II, stages 3 and
   8). In Part I, 1678 names the character "Formalist", and the rest of
   Part I does too (5 times). **Recommend:** "Formalist" in Part I stage 3
   and keep Part II as CCEL has it. Or use "Formalist" in all three, if you
   want one name.
4. **Emmanuel's land** (Part I, stage 8) / **Immanuel's land** (stage 3).
   1678 has Immanuel in both. **Recommend:** Immanuel.
5. **"Hymenius"** (Part I, stage 8). 1678 has "Hymeneus" and the KJV
   "Hymenaeus". **Recommend:** Hymenaeus.
6. **ought / aught.** The edition has "aught" 9 times, but "for ought I
   know" and "they that had ought to say" also appear (1678 "ought").
   **Recommend:** "aught" wherever it means "anything".
7. **One-off spellings** (the majority form is in brackets): wholsome
   (wholesome ×5), lillies (lilies), befal (befall), scull (skull),
   Apostacy (Apostasy), staid ×2 (stayed ×10), shew ×1 (show ×71).
   **Recommend:** use the majority form.
8. **Saviour ×8 beside labor, honor, neighbor.** CCEL mixes the British
   spelling of Saviour with American spellings elsewhere. **Recommend:**
   "Savior", to match the other American forms.
9. **Two Mount Sion / sixteen Zion.** Part I stage 10 quotes Heb 12:22
   ("Mount Sion", as in the KJV), and Part II stage 8 uses the same form.
   **Recommend:** keep them as they are.
10. **Standfast's speech is split in Part II, stage 8** ("…to give thanks
    for this my" / "great deliverance…"). CCEL put the second half in a
    plain paragraph after the speech. `build_tei.py` cannot run a paragraph
    into the speech before it, so the fix had to be reverted to keep
    `./fgb check` OK. This is a pipeline change (it would let `@prev` join
    an `sp`), not a text edit. **Recommend:** I add it to the pipeline.
11. **Part II has no early witness.** Its changes rest on sense alone.
    Compared word by word, the biblebb copy differs from CCEL in hundreds of
    places, but it is itself a modernized text (eats, lives for eateth,
    liveth), so it cannot settle them. **Recommend:** a later pass against
    the 1684 printing if an EEBO-TCP copy can be found.

## Part II witness (2026-10-04)

The user found a scan of Part II: London, 1732, archive.org
`bim_eighteenth-century_the-pilgrims-progress-_bunyan-john_1732` (192 page
images, OCR text; not kept in the repo). Checked against it:

- Confirmed: the stage 4 restoration ("So Christiana desired it, and they
  sent for him, and he came; When he was entered the Room"); the three
  Author's Way lines ("but Ground for groundless Fears", "Things of a greater
  Bulk", "love him at the first"); "neat and fine", "the Loss of other
  Things", "Let's know", the single "when" ("coming, when, in my Opinion,
  going down"), "these Pilgrims had been"; "Formality and Hypocrisy" in Part
  II.
- Reversed: "God make it a true saying" back to "made", as printed (scan
  n41).
- Not found in the OCR (too rough there): "loth to die", "come to be tried",
  Prov. 8:35, Standfast's speech.

EEBO-TCP A58733 is not Bunyan's Part II but the spurious *Second Part* of
1683 by "T. S." (Thomas Sherman, Wing S179), an imitation: no witness.

## Fixed (113 edits, all synced; the evidence is 1678 unless marked)

### Wrong or lost words

- Apology: "in toad's head" → "in a toad's head" (1678, metre).
- Part I s2: "the picture a very grave person" → "the picture **of** a".
- Part I s9: "fleshy" → "fleshly"; "the God of this world" → "god" (2 Cor 4:4); "action's sake" → "actions' sake".
- Part I s10: "such conviction as tend" → "convictions"; "the sight of at it first" → "of it at first".
- Part I s1: "straight gate" → "strait gate" (KJV Luke 13:24).
- Part II s2: "neat and find" → "neat and fine". ("God made it a true saying upon me" was changed to "make" on sense, then put back: the 1732 printing has "made".)
- Part II s3: a doubled "when" was removed ("coming when, in my opinion, going down").
- Part II s4: "there come to the door" → "came"; "Christana" → "Christiana"; "pilgrim's had been" → "pilgrims".
- Part II s5: "when we come be tried" → "come to be tried".
- Part II s6: "the loss other things" → "the loss of other things".
- Part II s7: "very loth die" → "loth to die"; "Let's knew" → "know".

### Capitals after a comma or semicolon (CCEL keying)

Thirty-odd places. Examples: "cried, you are" → "You"; "said Hopeful, let us" → "Let"; "God speed; So" → ". So"; "stand; For" → "for"; "said, stand back" → "Stand". Small capitals that CCEL keyed in lowercase are now "Blessed", "Enter ye into the joy of your Lord", and so on. "His Candle", "His Head" and "tender Conscience" are now lowercase.

### Punctuation and quotation marks

- Lost question marks: "traitor." → "?"; "live with him; And" → "? And"; "pilgrim's life." → "?"; "heart's delight." → "?".
- Missing closing quotation marks after Eccles. 10:3 (Part I s9) and Psa. 120:3,4 (Part II s4). Part II To the Reader: Christiana's speech "The thoughts … that land." now has its quotation marks. Part II s8: "Who would true valor see" now has its closing mark.
- Hyphens used as dashes are now em dashes: "slander-a lot", "Secondly-", "he is-", "thousand-else", "I am-and", "City-he", "add-in", "My end-thy good".
- "pilgrims guide" → "pilgrims' guide"; "welltuned" → "well-tuned"; "Mr. Mnason So" → "Mnason. So"; stray spaces in "before you ." and "one ."; "throne.Rev." spacing; the stray apostrophe in "King of' the".

### Scripture references

- References wrong in CCEL, now corrected from the 1678 margin: Matt. 18:30 → 13:30 (the tares), 1 Cor. 4:10 → 5:10, 1 John 5:21 → 2:21.
- Part II s5: Prov. 8:36 → 8:35 ("whoso findeth me findeth life"; *sense*).
- Style: "1 John, 3:12" → "1 John 3:12" (×4, also "1 Peter, 2:8" and "Jude, 14,15"). Spaces are fixed in "Phil. 3: 20,21", "Job 10: 21,22", "Heb. 9: 17-21", "John 10: 27-29", "John 5: 28,29", "Exod. 13:8-10" and "Lev. 7:32-34". Missing stops: "Isa 64:6", "Rev 7:16", "Matt.26:14", "Rom.10:4", "Num.13:32". "Job. 7:15" → "Job 7:15"; "Habak 1:2,3" → "Hab." (the book's form).
- Part II s4: the stray paragraph "Isa. 26:2." is joined to the paragraph it belongs to.

## Checked and kept

- Period forms such as "for that", "quoth", "staid" (in its old sense), "'twould", "aye", "prithee" and "Soho".
- The verse convention in Part II: a quotation set over several stanzas opens on the first stanza and closes on the last.
- `sweep.py`: 509 hits. All are period forms or names, except the ones fixed above (Christana, throne.Rev., the spacing) and the variants in question 7.
- `slips.py`: against 1678, none left. Against the biblebb copy (Part II), 2 hits, both spacing that is CCEL's and kept ("'twas", "well-tuned").
- `refs.py`: 477 references, none missing. The 6 weak matches are references attached to text that is not a quotation.

## Shelf-ready checklist

- [x] Whole text read for sense (all 23 files).
- [x] `sweep.py` hits fixed or explained.
- [x] `slips.py` resolved.
- [x] `refs.py`: no missing verses; weak matches read.
- [x] `./fgb check pilgrim` OK (23/23 identical).
- [x] `./fgb build pilgrim`: 404 pages, the same as main; inside margin 1.125in (Lulu 1.125in for 401–600 pages); nothing within 0.5in of the trim; the cover is set for 404 pages; epubcheck reports 0 errors and 0 warnings.
- [x] The PDF text has no wrongly curled quotes and no stray markup.
- [ ] Questions 1–8 are open. Questions 1 and 2 restore lost text and should be settled before printing. Question 10 needs a pipeline change.
