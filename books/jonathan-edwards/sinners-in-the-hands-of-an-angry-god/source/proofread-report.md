# Sinners in the Hands of an Angry God: proofreading report

I read all of `chapters/typ/sermon.typ` for sense. I checked it against the printed text of the "second edition", which is the TEI's printed layer. I also checked every scripture quotation against the Berean Standard Bible, the version this edition quotes on purpose.

## Fixed

- **John 3:18 quoted the wrong half of the verse.** The edition said "Whoever believes in Him is not condemned", which is the opposite of Edwards's point. It now reads "Whoever does not believe has already been condemned." That is the BSB wording of the part Edwards quotes: "He that believeth not is condemned already." I also added the full stop after the reference, as every other reference in the book has.
- **A semicolon was lost after Job 38:11.** "…but no farther" but if God…" is now "…but no farther"; but if God…", as in the print.
- **A comma and a capital were lost.** "that shall keep out of hell longest will be there in a little time! your damnation" now reads "longest, will be there in a little time! Your damnation", as in the print.
- **Spelling:** "harken" is now "hearken", the printed word.
- **Dashes:** the dashes in Isaiah 66:15 had spaces around them. They are now closed up, like the BSB's and like every other dash in the book.

## Checked and kept

- The sermon's text (Deut. 32:35) does not head the sermon, but it is on the title page and the ebook front. Nothing is missing.
- Edwards's other quotations match the BSB word for word. Two places keep his own words on purpose, because he builds on them: "laugh and mock" (Prov. 1:25-26) and "who knows the power of God's anger?"
- Revelation 19:15 is in the KJV on purpose: Edwards expounds "the fierceness and wrath of Almighty God".
- "raiment (clothing)" is the edition's own gloss, and I left it.
- Paragraphs, the APPLICATION heading and the closing paragraph follow the print.

## Changed after asking (2026-10-03)

1. Psalm 73:18-19 stays in the KJV on purpose, because point 2 rests on "as in a moment". The README now names both KJV quotations.
2. The Suffield footnote now reads "the neighbouring town". The print has "The next neighbour Town."

## Checklist

- `sweep.py --early`: 5 hits, none of them errors (KJV, etc., disproportioned).
- `refs.py --quotes --bible bsb`: 20 references, 0 missing, 0 weak matches.
- `./fgb check`: OK. [2] lists `sermon.typ` only because of the layout block that keeps the Suffield footnote on its page, as before.
- `./fgb build`: 44 pages, Lulu clean, with no footnote warning.
- epubcheck: 0 errors, 0 warnings.
- PDF text: no stray markup and no wrongly curled quotes.
