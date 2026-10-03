# Simon Magus review: progress (branch simon-magus-review)

## Tools
- sweep.py --early: 163 candidates, all Latin/period words or abbreviations-guide
  definition lists (`/ term:`), no real hits.
- slips.py: skipped. There is no modern witness; the old html/xhtml files in the
  main checkout are the user's own earlier copy of this same edition.
- refs.py --quotes: 128 refs, 0 missing, 0 weak matches.

## Read
All files read in full: foreword, ch1–8, abbreviations, ebook-front/appendix.

## Fixes applied (44, chapters/typ)
Scratchpad script fix.py has the list. In short:
- apostle's → apostles' (ch1)
- quotation capitals the edition had lowercased, restored from print (ch2 Lay,
  ch6 ×5, ch7 ×4); stray "ye" → you (ch3)
- punctuation: fragments made by "." (ch2 ×2, ch4 Zech, ch5 Leo), "!" restored (ch5
  ×2), stray commas (ch4), missing commas (ch2, ch3), "days' penance", "yourselves"
- Athalaricus "condemn" → "condemns" (doth dropped)
- refs: Matt 19:16 → 16:19; Acts 9:17 → 9:15, 16; Act./Acts./1 King. → Acts/1
  Kings; missing stops in ch1 notes; Compost./Decret. stops; Caus. 1.
- Ananias "that had he" → "that he had"; á → à; pertimiscamus → pertimescamus

## Open questions (draft)
1. Ch6 ends mid-sentence. Restore the end from print.
2. The Hebrew in ch2 (יָדמָלֵא) is typed in reverse order → מָלֵא יָד
3. "John the Seer" → Jehu (2 Chr 19:2)
4. Apollo → Apollos
5. ch6–8 British spellings vs ch1–5 American
6. pedler/pedlers/pedlars
7. Simoniacs/simoniack(s)
8. Holy Ghost ×2 (ch5)
9. headings: title case, ch6 trailing period, ch4 short title
10. modernizing (thereof/unto/shall) is uneven between chapters; leave it?
11. satyr → satire (ch4)
12. foreword note "See especially 17-20." has no source
13. abbreviations guide: John XXII should be John II; Lib. 4 Dist. qu. is Durandus, not Lombard

## Status
The 44 fixes are synced. `./fgb check simon` is OK (8/8; chapter-08.typ was
replaced by its extraction, which renders the same: the Cyprian italic is now split
across two `#emph` calls). Committed as WIP.

## Next step (done 2026-10-03: build OK, report written, final commit)
1. `./fgb build simon` (Lulu checks, epubcheck), then search the pdftotext output for
   `,‘ `, `‘ `, `’’`, `#emph`, `\[`.
2. Write source/proofread-report.md in the shape of Grace Abounding's report, using
   the open questions above as "Needs your decision", with the print readings: ch6
   end "may breed in him, yet the Sincerity of his Intentions, and the Evidences of a
   Call from God, may give him confidence to rely upon his Grace, as sufficient for
   him, whose Strength is made perfect in Weakness."; "John the Seer", "Apollo",
   "Pedlers", "Satyr" are all as printed.
3. Remove this progress file or keep it, then make the final commit "The Anatomy of
   Simon Magus: proofread, pending decisions".
