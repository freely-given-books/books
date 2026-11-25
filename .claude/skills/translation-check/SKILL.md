---
name: translation-check
description: Check an old English translation against the author's own original (Latin, French, Greek, Dutch…) and correct only its real departures, section by section, the way Beveridge's 1845 Calvin was checked against the 1559 Latin. Use this whenever a book is a translation and the user wants it checked, corrected, made faithful, or used as the base for a Modern English edition; whenever the user asks how much a translator departed from the original, whether a translation is reliable, or to compare a translation with its Latin/French; and for any new translated book (Perkins's Latin works, Witsius, Turretin, à Brakel, Ursinus…) before its Modern English edition is drafted.
---

# Translation check: the translator against the author

The Classic stays the translation **as printed** (only printers' slips fixed). The check makes
a second text, the **corrected translation**: the translator's own English with his real
departures from the author put right. That corrected text is the base for the Modern English
edition. It is not a new translation: most of a good Victorian translator's freedom stays.

Worked example: Calvin's *Institutes* (2026-11-22 to 24), six volumes, about 2,200 fixes in
Beveridge's 700,000 words, roughly 3 per 1,000. Everything lives in `work/institutes/latin/`
(README, `vol*/compare/`, `briefs/`).

## The grades

Each difference between translation and original is graded:

- **A**: the author's meaning is changed or lost; a reader of the translation would misunderstand
  him (a dropped "not", subject and object swapped, "believers" for unbelievers, a concession
  read as an assertion).
- **B**: a real but smaller loss or tilt a careful translator would fix (a key term blurred, a
  clause dropped, an emphasis softened, a wrong or missing reference).
- **C**: harmless paraphrase, normal freedom, Victorian expansion. **Left alone**, and only
  counted, not listed. In the Institutes pilot C outnumbered A+B nearly two to one.

The editor approved fixing A and B (2026-11-22). Fixes are the smallest change that restores
the sense, in the translator's own register; where the translator gets a place wrong, a second
public-domain translation that gets it right (Allen 1841 for Calvin) can lend its words.

## Witnesses and authority

- **The author's original is the authority**, in its best critical text, corrected from the
  author's own early prints where the critical text errs (see the `foreign-text-transcription`
  skill: the originals must be transcribed first, to publishable accuracy).
- **A second original by the author** (Calvin's own French of 1560) is the **tiebreaker for
  sense**. A later editor's edition of it may have "corrected" its references silently; then its
  references settle nothing.
- **A second public-domain translation** for wording (Allen).
- **Never a copyrighted translation** (Battles, McNeill for Calvin) — not as a source, and every
  new wording is checked so it does not echo one. The verifier caught one such echo in the pilot.
- The editor does not read Latin: **Latin readings and Latin-based judgment calls are Claude's**
  to decide and record, not editor cards. English style, tone and policy still go to the editor.

## Settled rules (carry them to the next translated book unless the editor says otherwise)

- **References:** the corrected text gives the **author's own** reference (his margin), even
  where a later editor changed it; the one exception is a plain slip proved by the words he
  quotes, or by the subject he names when nothing is quoted (Calvin's "Deut. 18:6" for the law
  of kindred degrees is Lev 18:6). Convert verse numbering to the English Bible's (Hebrew Ps
  51:21 = Ps 51:19).
- **References the translator added** where the author only alludes stay in the text.
- **The translator's citations of the Fathers** stay in the text if they are in the author's
  margin; otherwise they become a footnote marked "(Beveridge’s note.)" (curly apostrophe).
- **The translator's cross-references and glosses** set in the text move to such footnotes; a
  wrong cross-reference is moved and corrected, not deleted. His own footnotes are not departures
  and are not labelled.
- **Margin notes the translator dropped** (Scripture, Fathers, classical authors) are restored
  inline, in the author's form.
- A word the critical editors emend but the author's print has: judge the translation against
  the author's print; if the translator followed the emendation, decide whether the printed text
  gives a real sense, and say why.
- Recurring terms are rendered the same way across volumes (keep a list: Calvin's *iudicium
  divinum* = "divine judgment", *traditur* = "delivered" in the words of institution).

## The method

Work **one volume at a time**. For each volume:

1. **Originals in place** (both languages transcribed, split parts joined and checked).
2. **Classic recheck against the translator's own print** (the `print-recheck` skill), run in
   parallel; its changes are applied *after* step 4.
3. **Compare**, one agent per part of about 10,000 English words (split long chapters by
   sections, e.g. §1–17 / §18–33 / §34–50). Brief: `references/compare-vol.md` (written for the
   Institutes, `{N}` = volume, `{CHAPTERS}` = the part's name; adapt the names for another book),
   plus a per-volume notes file overriding it (`references/prompt-notes-example.md`): which French
   edition, settled Latin readings, terms to keep consistent, known overlaps. Output per part:
   `compare-<part>.md` for the editor and `fixes-<part>.json` (id, chapter, section, kind,
   severity, old, new, why), each `old` occurring exactly once in the chapter file.
4. **Verify**, one fresh agent per part (`references/verify-vol.md`): every proposal accepted,
   adjusted, downgraded to C or rejected, A items confirmed on the author's print, its own read
   for missed A's. Output `verified-<part>.json`. Put the compare agent's open questions into the
   verify prompt; settle Latin calls yourself and say so in the prompt.
5. **Apply the print recheck to the Classic** (it changes the base the fixes apply to), then
   `./fgb sync`, `./fgb check`, commit.
6. **Build the corrected text and review pages**: `scripts/build_review.py VOL OUT` (Institutes
   paths; adapt `BOOK` and the pilot special case) writes `VOL/corrected/*.typ` and one page per
   chapter: original | second original | translation | corrected (word diff), with each finding
   under its section. It reports `miss`: a fix whose `old` is no longer found once.
7. **Fix every miss** (usually a recheck change inside an `old`, or an earlier fix that added a
   second copy of the `old`: widen its context), rebuild to 0 misses.
8. **Read the word diff of corrected against the Classic** for anything leaked into the text
   (a finding's comment written as text happened once).
9. Copy the review pages to Nextcloud `drafts/<book>-vol<N>/`, and make the editor a review card
   with: where, counts (A/B/skipped), the notable A fixes, and any English question.

## Traps met on the Institutes

- Two fixes can collide: a recheck row and a fix changing the same reference (reject the
  fix as "fixed by the Classic recheck"), or two fixes where one adds text the other looks for.
- "AV wording" items (the translator put the King James words where the author quotes
  differently) are real only where the author's argument rests on the difference.
- Agents splitting a chapter must agree on note numbering and on the words at the split;
  record each join in a JOINS file and check it.
- Keep the agents' scratch under `work/<book>/…/vol<N>/compare/work-<part>/`, never /tmp.
- Severity drifts between agents: the verifier's call stands; raise to A only when the doctrine
  or argument is reversed, not merely blurred.
