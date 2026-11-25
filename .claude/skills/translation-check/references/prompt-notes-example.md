# Vol. 6 notes for the compare and verify agents (read them with the brief)

- N = 6. The English files are `chapters/typ/vol-6/book-4-chapter-NN.typ` (Book IV ch. 14-20, the last volume).
- The Latin is in `vol6/la/` (ch. 17 in `.part-a.md` + `.part-b.md`). Each file's notes say where it was corrected
  from the 1559 print.
- **The French is not the 1560 critical text here.** It is the 1859 Paris (Meyrueis) edition of the 1560 French. Its
  editor added accents and silently corrected Scripture references, so a reference in the French is the 1859 editor's,
  not Calvin's, and settles nothing about `reference` items. The Latin decides those, with the 1559 print if needed. The
  French is still the tiebreaker for sense. Footnote references appear inline in parentheses; `<!-- p. N -->` gives the
  1859 page. Plain 1859 misprints are corrected and listed in each file's Notes. Chapters 16, 17, 19 and 20 are split
  into `.part-a/.part-b(/.part-c).md`: read all parts. The French has centred italic subheads in ch. 19 (*De la
  Confirmation.* etc.): they are the 1859 print's, not departures by Beveridge.
- Allen: Book IV is in `work/institutes/allen/ioanniscalviniin02calv.txt` (find the chapter by its "CHAPTER" heading).
- The 1559 print is `work/institutes/latin/scan-1559-print/institutiochrist1559calv.pdf`. Render pages into your own
  folder under `vol6/compare/`, not /tmp.
- The Classic (Beveridge) for vol. 6 is being re-checked against the 1845 print in parallel; the recheck is applied
  AFTER your work. Judge the text as it is in the worktree now; don't list 1845-vs-CCEL wording (hath/doth etc.).
- Beveridge's own footnotes are not departures, and are not to be labelled. Only his cross-references and glosses set
  in the text move to footnotes marked "(Beveridge’s note.)" (curly apostrophe). A wrong cross-reference is moved to a
  footnote and corrected, not deleted. Scripture references he added where Calvin only alludes stay in the text. His
  patristic citation stays in the text if it is in the 1559 margin, else it becomes a "(Beveridge’s note.)" footnote.
- **References in the corrected text:** give Calvin's own reference, from the 1559 margin where 1869 differs. The one
  exception is a plain slip, where the words Calvin quotes prove which verse he meant.
- Render "divini iudicii" as "divine judgment" (as vols 4-5). Keep the vol. 5 renderings for recurring terms of Book IV
  (look at `vol5/compare/verified-*.json` when a term recurs: e.g. sacramentum, mysterium, signum, obsignare).
- Never echo Battles or McNeill (in copyright). New wording: Beveridge's own words or Allen's where possible.
