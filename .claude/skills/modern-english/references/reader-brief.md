# Brief: sentence-by-sentence meaning reader (template)

Fill in {AUTHOR}, {BOOK}, {YEAR}, {GLOSSARY}, {ASSIGNMENT}, {OUT}. The same brief serves the audit's pass A
(opus) and pass B (sonnet), and the assessment's readers.

---

You are checking a Modern English rendering of {AUTHOR}'s *{BOOK}* ({YEAR}) against the Classic text (the
author's words, spelling updated, his grammar and italics kept). Each `pairs-<chapter>.md` file gives every
paragraph as CLASSIC then MODERN (Typst markup: `#emph[...]` is italics, `#footnote[...]` is a note,
`you#super[+]` marks a plural "you").

**Your only question: does the Modern text say anything the author did not say, or fail to say anything he
did say?** Read each Classic sentence, find its Modern counterpart, and compare their meaning clause by
clause.

**Read every paragraph of your assignment. Do not sample.** For each paragraph, write one line: `ok` if you
find nothing, or one finding row per problem. Your output is checked paragraph by paragraph against the
assignment, along with the time you took, and a run with gaps or that went too fast is thrown away and done
again. If you cannot finish, stop and list the paragraphs you did not read; that is fine. Claiming to have
read them is not.

Your assignment: {ASSIGNMENT}

## Look especially for

1. **Direction / reversal.** Negations lost or added (not, no, never, nor, without, unless, scarce,
   hardly); more vs less; cause and effect swapped; who acts on whom. One lost "only" or "all" can reverse an
   argument.
2. **Dropped or added qualifiers.** only, alone, all, some, any, chiefly, in part, usually, always; may vs
   must vs will; "as it were"; conditions (if, unless, until).
3. **Referents where a sentence was split or rebuilt.** Every pronoun and subject must point where the
   author's did (the Spirit, the believer, sin, Satan, the soul, God, the hypocrite). Where speech became
   indirect, or indirect speech became direct, check that the speaker and the "I/my" are unchanged. This is
   where earlier audits missed the most ("my righteousness" changing owners; "maintain it" pointing at the
   wrong noun).
4. **Fragments and broken grammar** at a new sentence boundary ("If he does this." standing alone), and a
   Latin or old verb form left inside a modern sentence.
5. **Theological or technical terms** traded for an everyday word that loses the technical sense:
   effectual, efficacy, merit, impute, justify, habit, principle, frame, flesh, carnal, ordinance, assurance,
   and the like.
6. **False friends left in place.** These are words a modern reader will misread because their sense has
   shifted (professors, discover, communicate, temper, security, apprehension, sensible, improve, want, still,
   presently, prevent, let, conversation, gay, starve, doubted, convenient, "to this day", "for nothing",
   "may not", nearly, by accident). The house rule replaces them with a modern word, never a gloss. Report
   any left in the text, and any replacement that changes the sense.
7. **Omissions and additions.** A clause, example, proof, reference or step of the argument missing; or
   anything added that is not in the author (a gloss, an image of our own, an explanation).
8. **Scripture.** Where the author's exposition leans on a word of the verse, the Modern quotation must
   still contain that word (BSB, adjusted where needed). A reference the Modern changed must be supported by
   the quoted words. A quotation cut with "…" must still read as grammar.

## Do NOT report

These are deliberate house rules (the book's glossary is {GLOSSARY}):
- labels written out (Obj. → Objection);
- headings modernized (but DO report one that changes meaning or keeps an archaic word);
- the glossary's renderings;
- Holy Ghost → Holy Spirit;
- American spelling;
- gendered language kept (man, men, he, brethren: that is required);
- BSB wording for the KJV, unless the argument depends on the old wording;
- [bracketed] translations of Latin or Greek;
- the you⁺ mark (but DO report a plural address left unmarked, or a singular marked);
- style preferences, sentence splitting, and plainer synonyms that keep the meaning.

## Output

Write a TSV to {OUT}. The header line is:

`file	n	verdict	severity	kind	classic_excerpt	modern_excerpt	explanation	suggested_fix`

- **One row per paragraph.** Use `file  n  ok` (the other columns empty) for a paragraph with nothing to
  report, or one or more `finding` rows.
- **severity:** `meaning` (a demonstrable change of meaning), `nuance` (a real but small loss a careful
  reader of the author would notice), or `query` (unsure; say why).
- **kind:** reversal, qualifier, referent, grammar, term, false-friend, omission, addition, scripture, or
  other.
- **Excerpts:** short and exact, copied from the file.
- **suggested_fix:** the smallest change, in the wording closest to the author. Keep gendered language.

When done, reply with:
- the number of paragraphs in your assignment and the number you gave a verdict for;
- counts by severity;
- the five most important findings.

Read only your pairs files and this brief. Do not edit anything, and do not look at earlier reviews.
