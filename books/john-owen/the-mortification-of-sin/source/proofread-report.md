# Proofread, 2026-10-10

The whole book (preface and chapters I–XIV, about 42,700 words) was read
for sense by two readers, each file compared word for word with Goold's 1850
printing (OCR of the archive.org scan) and doubtful places checked against
the 1668 edition (`A53715.witness.xml`). `sweep.py` and `refs.py` were run
(269 references, none to a missing verse; one loose quotation, Isa. xxxv. 7,
is Owen's paraphrase). The corrections made before the proofread (two
dropped lines and three slips, chapters II and X) are in
`witness-report.md`.

## Fixed

These are editor decisions in the TEI (`review-report.md`).

**Greek**
- ch. XII: δι’ ἐσύπτρου → δι’ ἐσόπτρου (1 Cor. xiii. 12)
- ch. XII: Ἀνακεκαλυμμένῳ προσώπω → προσώπῳ (2 Cor. iii. 18)
- ch. XIV: λαβωμεν → λάβωμεν (Heb. iv. 16)
- ch. XII: “αἰνίγματι — in” → “αἰνίγματι, — in” (Goold has the comma)

**References**
- ch. XIV: Col. i. 18, 14 → Col. i. 13, 14 (Goold; verse 13 is the one quoted)
- missing stop after a chapter numeral: Zech. xii. 10 (III), 1 John ii. 15,
  iii. 17 (IV, also "John." → "John"), Rom. xiii. 14 (VI), Gen. xxxix. 9 (IX),
  1 Cor. ii. 8 (XIV)

**Spacing**
- a stray space inside a quotation mark: “If by the Spirit” (I), “they shall
  not be healed” (IV); before a comma after Greek (XII, twice)
- “of it —Not” → “of it — Not” (V), “one,— “sealing” → “one, — “sealing” (X)
- five footnote markers CCEL keyed after the word space (“he was ¹ ready”):
  now set against their word, by the machine (colophon 0.6.0, `note_spaces`)

## Questions, settled by the editor (2026-10-10)

Goold's readings, which CCEL follows, set against the 1668 edition.

1. ch. III, “Duties are excellent food for an unhealthy soul; they are no
   physic for a sick soul.” 1668 “an healthy Soul”; Goold's “unhealthy”
   contradicts the sentence. **Now “a healthy soul”.**
2. ch. XIII, “thou hast done it overtly”. 1668 “overly” (superficially),
   what the passage is about. **Now “overly”.**
3. ch. XIV, “considered absolutely and in it itself”. 1668 “in its self”.
   **Now “in itself”.**
4. ch. VI, “disquiet and perplex the killing of its life”. 1668 has a
   semicolon after “perplex”, which the sentence needs. **Added.**
5. ch. II, “nor boast by other men’s lives of what God hath not done for
   us”. Goold's page (vol. 6, p. 10) prints “lines”; 1668 has “lives”, and
   CCEL “lives”. **Kept “lives”, Owen's word.**
6. ch. VIII, “verse 2 “They seek me daily” (no comma, as Goold). **Left.**
7. Goold's prefatory note: **left out of the edition.**
8. Goold's notes: ch. I, “There seems to be an oversight here … — Ed.”:
   **kept**. ch. XIV, “Communion with Christ, vol. ii. chapters vii. viii.”
   is Owen's own margin note (1668: “Communion with Christ, chap. 7, 8.”)
   with Goold's volume number added: **kept, without “vol. ii.”**

## Left as is

- Period and Goold spellings, each used one way throughout: Saviour,
  labour, any thing, every one, whilst, farther, staid, vail.
- “subtlety” (I, II) and “subtilties” (VI); “deep-rooted” (III) and
  “deeply-rooted” (VI): both Goold's.
- References where Goold and 1668 agree, even when another verse fits as
  well (“John x. 4” for “My sheep know my voice”).
