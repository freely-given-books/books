# Independent assessment: Brooks, The Secret Key of Heaven, Modern English (2026-11-16)

You assess the Modern English edition of Thomas Brooks's *The Secret Key of Heaven* (1665; twenty arguments for closet prayer, on Matt 6:6) for Freely
Given Books, as the earlier books were assessed (models: `../pilgrim-2026-11-15/assessment.md` and
`../domestical-duties-vol1-2026-11-15/assessment.md`, read them for the form only). **Independent: do not open
`/home/courtney/Projects/fgbooks/work/secret-key-modern/audit/`, its `secret-key-audit-edits.py`, `coordinator-edits.py` or `drafter-notes.md`.**

## Material
- Pairs, Classic then Modern, paragraph by paragraph: `pairs/pairs-*.md` (and `pairs/pairs.jsonl`). Book files:
  `/home/courtney/Projects/fgbooks/wt-secretkey-modern/books/thomas-brooks/the-secret-key-of-heaven/chapters/{typ,modern}/`.
- The rules: `/home/courtney/Projects/fgbooks/wt-secretkey-modern/MODERN-ENGLISH-RULES.md` (§1-8, §7b), the book's glossary
  `.../the-secret-key-of-heaven/source/modern-glossary.md` and the drafting brief
  `/home/courtney/Projects/fgbooks/work/secret-key-modern/brief.md`.
- BSB lookups: `python3 /home/courtney/Projects/fgbooks/work/modern-english/bsb.py "Matt 6:6"`.

## Task
1. A paired read for meaning: spawn up to 4 reader subagents (general-purpose), each a group of pairs files (about
   21,000 Classic words each), all at once; give them this file's rules and ask for TSV findings (`readers/r<N>.tsv`:
   file, paragraph, severity meaning/nuance/query, kind, classic excerpt, modern excerpt, explanation, suggested fix).
   Ask them to read every sentence, not sample. Check their findings yourself against the files before you take them.
2. Whole-book checks you run yourself: paragraph and footnote counts; Scripture references kept; archaic forms left;
   straight quotes; **headings** (every `=` line modernized, none keeping archaic words: betwixt, unto, -eth, hath,
   thereof, closing with, want = lack); the glossary's renderings applied consistently (closet, the key verses,
   professors, closing with Christ); plural marks (you⁺) on every plural you of a genuine plural address;
   old words in their old sense left unexplained (still, presently, discover, want, conversation, prevent, bravery,
   naught, spoil, temper, conceit, large, light, several, lighted upon, rout, "and what not").
3. Judge especially: is Brooks's voice kept (his heaped images, his pithy sayings, "the golden pipe of mercy", "a nose of wax")?
   Is anything modernized that did not need it, or left that now misleads or that a modern reader cannot understand?
4. Write `assessment.md` (coverage, score of 10, verdict, strengths, the findings that matter) and `corrections.tsv`
   (file, paragraph, current_modern, proposed_modern, reason; current_modern an exact substring of the Modern
   paragraph), each correction the smallest change, in the wording closest to Brooks. Do not edit any book file.

Reply (under 300 words): score, verdict, number of corrections, the five most important.

Note: this book's Classic has no footnotes; its references stand in parentheses. "Closet" is kept on purpose (glossary); judge whether that serves a modern reader, but do not count it as a fault.
