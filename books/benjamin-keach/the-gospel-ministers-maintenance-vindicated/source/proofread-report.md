# The Gospel Minister's Maintenance Vindicated: proofreading report

A full read of `chapters/typ` (the recommendation and the four parts, about
23,000 words), checked against the 1689 printing as the TCP transcribes it
(`A47561`), the archive.org page images where the TCP was doubtful, and the
KJV. There is no modern witness. 2026-10-04.

## Book-wide rules (machine pass, `source/editorial.py`)

Decided by the user: lowercase the printer's capitals, modernize the
spellings the shared table missed.

- `LOWERCASE_COMMON_NOUNS`: the 1689 capitals on nouns, adjectives and other
  words mid-sentence (about 4,300) are lowercased, as on the rest of the
  shelf. Kept: God, Christ, Lord, Jesus, Spirit, Scripture(s), Saviour,
  names, books of the Bible; Father, Son, King, Mark, New, Acts and Lamb keep
  the printed capital and were settled by hand (the Father, the Son of God,
  King of saints, New Testament, Holy Spirit / Holy Ghost / Holy Scripture).
- `QUOTE_START_CASE` (new, in `build_tei.py`, off by default): the first word
  of an italic run of five words or more keeps its capital, so "saith, Thou
  shalt" stays; quotations woven into a sentence ("ascension, and sitting on
  the throne") were lowercased by hand.
- `SPELLING`: strangly, supplyed, Soveraign, injoyn, rejoyce, intangle,
  Millitant, publick, incumbred, dispenced, Livelyhood, Knowledg, lye, dye,
  Tythes, niggerly → niggardly, Thrasheth → thresheth (KJV) and the like;
  possessives printed without an apostrophe (Mens, Christs, Lords, Peoples,
  Lucres). Also pins "Obj" and "divest", which the letterform search had
  turned into "Obi" and "diuest".
- `'tis`, `'twas` are set with a typographic apostrophe (’tis): Typst curls a
  straight one after a space into an opening quote, so the PDF and EPUB
  printed ‘tis (53 times).
- `EXPAND_ETC` ("&c." → "etc.", as Brooks and Simon Magus) and
  `ITALIC_SENTENCE_QUIRK = False` (a sentence after an italic quotation
  starts with a capital: "…in every church.] So the apostle").

## Fixed by hand (348 editor decisions in all, with the case and spelling)

- **Transcription and print slips**: two cats → two coats (Matt 10:10),
  Honorur → honour, treadeth cut → out, mecked → mocked, eaterh → eateth,
  not to he covetous → be, no helps to he had → be, greaest, hinddred, meeet,
  acccount, allowanee, dispenee, turst, kindom, wordly (×2), hs → his,
  an not eat → and, 'tis but lust → just, sow or import → impart, do fellow
  → follow, studying mediation → meditation, an aw → awe, has end → base
  end, out some may → but, ever done → over-done, than they to give → do
  give, such an neglect, ashare, mans → man's, ware out → wear out, in
  dwelling sin → indwelling, whom we, serve; so be clouded → beclouded,
  them a part / set a part → apart, at previous → a previous, Zeck. →
  Ezek., Ordaination, with marry → with Mary (Mark 14:8; the name table had
  made it "marry").
- **From the page images**: "whether it be a duty" (the TCP dropped "a",
  p. 14); "upon the Altar, which they serv'd" (TCP "Alter," and a stray "1",
  a speck of type, p. 19).
- **References**: 1 Tim 17.18 → 5.17,18; Ephes 4.23 → 4.28 (Let him that
  stole); Isa 40.10 → 40.19 (the goldsmith); 2 Tim 3.4 → 2.4 (No man that
  warreth); 1 Cor 13.14 → 9.13,14; Deut 13.11 → 33.11 (Bless, Lord, his
  substance); Hag "read the 6. v." → 9 (the verse quoted); 1 Pet 3. & 22 →
  3.22.
- **Quotations**: they profiting → thy profiting (1 Tim 4:15); his seeds seed
  → seed's seed (Isa 59:21); Physician heal thy self → Physician, heal
  thyself; quotation openings capitalized (saying, All power; Christ saith,
  Then are ye my friends; say, Surely this great nation).
- **Punctuation**: every `▪` (the TCP's unreadable stop) set from the sense
  (; , : or .), missing parentheses closed or opened (3), "tis" without its
  apostrophe (5), a stray "&&c.", "London,July" spaced, two paragraph ends
  given their full stop, i. E. → i.e. throughout.
- **Forms**: our selves, your selves, it self, thy self, her self → one word;
  its (it is) → it's; least (lest) → lest; then and than set to the sense (2); humane
  (human) → human; GOD → God; possessives given an apostrophe (the church's
  deliverance, the pastor's duty, their master's goods, ministers' hands).
- **Case**: ordinal points read as one sentence ("Fourthly, and not in
  respect…", "Secondly, that we may…"); gods (idols), the son that sleeps in
  harvest, father or mother, the spirit of this world; "Edward Man" (a
  signatory) kept capital.
- The stray "And" at the end of a paragraph in part 4 moved to open the
  next ("And hence how careful was St. Paul").

## Decided by the user (2026-10-04) and applied

All six as recommended: "the sooner it may", "not only then", "sabaoth",
"Gal. 6:6", "thereof", and every reference in the colon style ("Matt. 10:9, 10",
69 places).

1. **"the sooner may in a little time appear"** (part 2, first paragraph): a
   word is missing; the line ends at the binding on the microfilm ("the
   soone[r]"), so a lost "it" can be neither seen nor ruled out.
   *Recommend:* "the sooner it may in a little time appear".
2. **"and not of then, but also, in all succeeding ages"** (part 2, the
   first Answer). *Recommend:* "not only then".
3. **"the Lord of sabbaths"** (part 2): James 5:4 reads "the Lord of
   sabaoth" (of hosts); "sabbaths" is a common slip for it.
   *Recommend:* "sabaoth".
4. **"He that is taught in the word ought to communicate…", 1 Tim. 5.18**
   (part 3): the words are Gal 6:6 (1 Tim 5:18 is the ox and the labourer).
   *Recommend:* "Gal. 6.6".
5. **"the ministration therefore, in any respect"** (part 2, Eleventhly).
   *Recommend:* "thereof".
6. **Reference style.** The book prints "Matt. 10.9,10." and "1 Cor. 9.7."
   (a stop between chapter and verse); Simon Magus and Brooks use a colon
   ("Matt. 10:9, 10"). *Recommend:* colon, for a shelf that reads alike
   (about 70 references); or keep the 1689 style.

## Left as printed on purpose

- Period grammar: "the churches … has been", "most weightiest", "these be",
  "for to uphold", "an husband", "his seed", "sith", "behove",
  -eth and -est forms, "expediment" (an old word for expedient), "attendency",
  "Bless Lord his power" (as quoted from Maimonides).
- Quotations given as Keach gives them where they differ from the KJV in
  small ways ("a workman that needeth not be ashamed", "who are sufficient
  for these things").
- "Christ mystical body", "Christ his church" (old genitives).
- The errata the user chose to leave (p. 8 her, p. 47 let) and the two that
  could not be placed; the recommendation's date "July, 30. 1681."

## Note

The page images show the TCP has its own slips (a dropped "a", "Alter").
This read caught those that make a sentence fail; a slip that leaves good
sense (a dropped article, a singular for a plural) can only be found by
reading the 86 pages against the images.

## Checks

- `sweep.py --early`: what remains is period verb forms (-eth, -est).
- `refs.py --quotes`: 67 references, none missing, no weak quotation matches.
- `./fgb check`: OK (rebuild, round trip 5/5, TCP words, tei_all, compile).
- `./fgb build`: 86 pages, within Lulu's margins, no footnote warnings;
  epubcheck 0 errors, 0 warnings.
- PDF text: no ‘tis, no wrongly curled quotes, no stray markup.
- `verify.py` on every other TEI book: OK (the `build_tei.py` change is off
  by default).
