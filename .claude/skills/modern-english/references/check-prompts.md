# Prompts for the targeted checks

Short task prompts for the checks that sit between the scripts and the readers. Models and efforts are in
`models.md`. Each prompt names its input rows (a slice of a script's TSV) and an output TSV. Each also
names the book's glossary and `MODERN-ENGLISH-RULES.md` §3.6, which the agent reads first.

## 1. False-friend classifier (haiku, low): rows of `ff-hits.tsv`

> Each row is a word in a Modern English sentence that *may* be a false friend: a word that still exists but
> meant something else to a 17th–19th-century author (professors = professing Christians; discover = reveal;
> communicate = impart; temper = disposition; security = complacency; want = lack; still = always; prevent =
> go before; let = hinder; doubted = feared; starve = die of cold; convenient = fitting; gay = merry). The
> Classic paragraph is given, so you can see what the author meant.
>
> For each row, answer `mislead` if a modern reader would take the wrong sense here, `fine` if the modern sense
> is what the author meant, or `doubt` if you are unsure. Hits marked `q` are inside a quotation: answer
> `fine` unless the quotation is the author's own words, not Scripture. Write
> `file  n  hit  answer  author's sense (3-6 words)` to OUT. Answer every row.

Rows answered `mislead` or `doubt` go to the decider.

## 2. False-friend decider (sonnet, medium): the classifier's mislead and doubt rows

> Decide each row. If the word misleads, give the replacement: the modern word that carries the author's
> sense in this context. Change only that word or the smallest phrase; keep the sentence, its order and the
> author's voice. Use the glossary's rendering where it has one. Words merely old-fashioned but still read
> rightly are left alone. Never gloss, except for the author's own technical term that no modern word can
> carry (rules §3.6). Write `file  n  current_modern  proposed_modern  reason` (current_modern an exact
> substring of the paragraph), or `file  n  keep  reason`. List any word you decide that the glossary lacks,
> so it can be added.

## 3. Sentence check (haiku, low): rows of `split-points.tsv`

> Each row names a paragraph where the Modern text has more or fewer sentences than the Classic, or a
> quotation's framing changed. Read the Modern paragraph (from the pairs file) and check each sentence: is it
> a complete English sentence? Mark a fragment ("If he does this." on its own), a sentence that lost its
> verb, a dangling "which", and a Latin or old verb used as a modern one. Write `file  n  ok` or
> `file  n  fragment|grammar  excerpt  note` for every row.

## 4. Referent check (opus, high): the same rows, with the Classic

> For each paragraph, read the Classic and Modern side by side. For every pronoun and every sentence subject
> in the Modern, name what it refers to, and check that it is what the author's sentence referred to. Where
> speech changed between direct and indirect, check the speaker and every I / my / me / you. Report only
> real shifts, with the smallest fix in the author's wording: `file  n  excerpt  refers to (Modern)  should
> refer to (Classic)  fix`. Write `file  n  ok` for clean paragraphs. Every row gets a line.

## 5. Scripture lean check (sonnet, medium): the quotations of `audit-scripture.py` and the BSB

> For each quotation: does the author's next sentence or two lean on a word of the verse (explain it, repeat
> it, argue from it)? If the Modern quotation (BSB) has lost that word, propose the light adjustment (rules §5,
> §7.2, §7.9) restoring just that word. Check particles too ("that" as outcome vs "so that" as purpose; "and"
> vs "but"). Write `file  n  ref  ok`, or `file  n  ref  word leaned on  current  proposed  reason`.

## 6. Review of the edits (sonnet, high): the diff of one edit script

> Here is every change a correction pass made to the Modern English text, each with the Classic paragraph
> and the pass's reason. Check each change once more. Does it say what the author said? Does it read as
> English? Does it break the glossary or a settled wording (rules §7b)? Does it overreach, for example "nothing"
> for "not all", or a rules-table rendering that does not fit this context ("purges away no infection")? Write
> `n  ok`, or `n  problem  fix` for every change.

Run it on the audit's edits and again on the assessment's: earlier passes introduced errors no later stage
looked at.
