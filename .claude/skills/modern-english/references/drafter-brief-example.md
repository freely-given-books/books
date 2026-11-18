# Brief: Modern English draft of Thomas Brooks, The Secret Key of Heaven

You are drafting part of the **Modern English edition** of Thomas Brooks's *The Secret Key of Heaven, or Twenty
Arguments for Closet Prayer* (London 1665, *The Privie Key of Heaven*; our Classic is the EEBO-TCP text A29703,
spelling updated and lightly modernized, Brooks's grammar kept) for Freely Given Books. Thirteen drafters share it,
each a slice (yours is named in your task); write only your slice. Brooks's *Precious Remedies Against Satan's
Devices* was finished this morning the same way; the press's other Modern English books (Owen, Watson, Edwards,
Gouge, Boston, Perkins, Bunyan, Sibbes, Spurgeon) were each approved through editorial assessments and a meaning
audit.

Brooks (1608-1680) is a London Puritan pastor of warm, vivid, pithy style. This book is one long sermon on
Matt 6:6: an Introduction (the text expounded, the doctrine "Closet prayer or private prayer is an indispensable
duty"), **twenty arguments** for closet prayer, then the **application** (reproof, six objections answered, eleven
counsels, means and rules, last directions), each point numbered ("First, …", "Secondly, …", "1.", "(1)", "\[1\]"),
proved by Scripture, sayings of the Fathers and heathen ("saith one"), stories (Foxe's martyrs, emperors,
philosophers), with Latin he often translates himself. His sentences run on with semicolons, heaped phrases and
images ("the silver channel, the golden pipe of mercy"; "a nose of wax"). **Keep his images, his heaped phrases
and his voice**; split his long semicolon chains into sentences of modern length where a modern reader loses the
thread, every clause kept; never pad, never summarize, never a fresh image of our own. The test (the editor): a
reader should think "ahh, this is Brooks", never "this is a total rewording".

## Read first, in full

1. **The rules (binding):** `/home/courtney/Projects/fgbooks/wt-secretkey-modern/MODERN-ENGLISH-RULES.md`, all
   sections: §2.5 (an early-modern "?" used as an exclamation becomes "!" or "."; a real rhetorical question stays
   a question), §3 (words, the Reformed register, technical terms that stay), **§3.6 (false friends REPLACED with
   a modern word, never glossed; the standing table)**, §4 (you / you⁺), §5 (Scripture), §7, §7b, §8.6 (Latin in
   brackets).
2. **This book's Modern glossary (binding; follow it exactly):**
   `/home/courtney/Projects/fgbooks/wt-secretkey-modern/books/thomas-brooks/the-secret-key-of-heaven/source/modern-glossary.md`
   — above all the decision on **closet** (kept, as the book's term) and the shared renderings of the key verses
   (Matt 6:6 and the others). Any recurring term you render that it lacks: list it in your reply with your
   rendering.
3. **The model:** the Modern English *Precious Remedies* (Brooks himself, finished and audited today):
   `/home/courtney/Projects/fgbooks/wt-remedies-modern/books/thomas-brooks/precious-remedies-against-satans-devices/chapters/modern/`
   beside its `chapters/typ/`. Read at least two files side by side (e.g. `duties-07.typ`, `doubting-02.typ`).
4. **The corrections its reviews made** (each edit has a comment saying why):
   `/home/courtney/Projects/fgbooks/work/precious-remedies-modern/precious-audit-edits.py` (EDITS and
   FALSE_FRIENDS lists) and `/home/courtney/Projects/fgbooks/work/modern-english/assessments/precious-remedies-2026-11-16/corrections.tsv`.

## Source and output

Your slice is a small book folder of its own: `/home/courtney/Projects/fgbooks/work/secret-key-modern/<LETTER>/`
holding `chapters/typ/<file>` (the Classic of your slice). Some files are **parts** of a long chapter
(`application-02-3.typ` = the third part of application-02; it may start mid-section, under a heading in the part
before): treat each as a file. Write the Modern English to `chapters/modern/<file>` in the same folder, same file
names, the same paragraphs. The Classic's spelling is updated but British (honour, labour, Saviour); the Modern is
American (honor, labor, Savior).

## Format (Typst)

- **Paragraph for paragraph:** exactly the same number of blank-line-separated blocks, in the same order. Never
  merge or split paragraphs (split sentences inside them freely).
- **HEADINGS ARE MODERNIZED TOO.** Every `=` line (`==`, `===`, `====`) is the edition's own heading; keep its level,
  its number or letter (`=== a.`, `==== 3.`), its shape and its wording, but **no archaic word may survive in it**:
  Hath → Has, -eth → -s, Thou/Thy/Thee → You/Your, Canst/Wouldst → Can/Would, unto → to, Want → Lack, "Spend
  Not" → "Do Not Spend", "Hinders Not" → "Does Not Hinder", Discovers → Reveals, Prevalency → Prevailing Power,
  "Out of Door" → "Out of Doors", Corporal → Bodily, Wherein → In Which, Indefinite → General. A heading that is
  already plain modern English stays word for word. Readers navigate by these heads.
- Layout lines copied exactly: `#align(center)[ … ]`, `#block(...)[`, `#set par(...)`, `#text(...)[`, `#v(0.8em)`.
  Inside the Introduction's verse block only the verse words change (to the glossary's Matt 6:6; italic, no
  quotation marks); "— Matt 6:6" stays.
- `+ ` and `- ` list items stay items, same order and count; `#[` … `]` scopes copied unchanged. Keep outline
  marks at a paragraph's start exactly as the source has them (`1\.`, `(1)`, `\[1\]`, `First,`, `#emph[First],`),
  and escapes (`\[ \]`, `1\.`). `#smallcaps[…]` stays on the (new) first word.
- This book has no footnotes; references are in parentheses in the text: keep every one, in place.
- In-text labels: `Obj.` → `Objection.`, `Ans.`/`Answ.` → `Answer.`, `Quest.` → `Question.`; `Doctrine:` stays.
- Scripture references in the edition's style (Gen 3:4, 5; 1 Pet 5:8; Matt 6:6). If you meet a reference that
  looks mangled ("the 12 Rom 9 v." style: the 1665 print names the chapter first, and our restyling may have read
  the verse as a chapter) or simply wrong (the quoted words are not in that verse), **write the right reference in
  the Modern and list it in your reply** (file, ¶ number, Classic text, the right one, evidence: the verse text).
  They will be fixed in the Classic too, after a check of the 1665 page images.
- Curly quotes and apostrophes (’ “ ”), never straight ones. Dashes as the Classic (—, –).

### Quotations and italics

The Classic already sets Scripture in curly quotation marks with the reference in parentheses after it
(`“Ye are sanctified…by the Spirit of our God” (1 Cor 6:11)`); keep that shape. Its italics (`#emph[...]`) are
Brooks's emphases, Latin, words picked out of a verse, and some point-statements: keep them on the matching
words. A quotation from a Father or anyone else keeps its quotation marks, his words his.

Quotations Brooks gives as Scripture are from the **BSB**: look each up,
`python3 /home/courtney/Projects/fgbooks/work/modern-english/bsb.py "Matt 6:6" "Gal 4:6"`.
Quote only the words Brooks quotes (trim, keeping his "…"; never fill out a partial quotation; a paraphrase or
loose recollection stays his words in modern grammar, not BSB). **Before you keep a BSB wording, read his next
sentences: if he leans on a word of the verse, that word stays**, the BSB adjusted lightly (rules §5.2, §7.2,
§7.9): the glossary gives the key ones (closet, in secret, openly, Spirit of adoption, infirmities, supplication,
effectual fervent, the secret of the Lord, hidden ones, secret places). Check particles ("that" outcome vs purpose;
"and" vs "but"). Render a verse the same way each time it recurs in your slice. LORD → `#smallcaps[Lord]`; God's
pronouns capitalized in BSB quotations as the BSB does; in Brooks's own prose as the Classic has them (it
capitalizes He/Him/His for God: keep that). Holy Ghost → Holy Spirit. Keep gendered language (man, men, he,
brethren, "no man").

**The Introduction's singular "thou"** (slice A, chapter-03, the paragraph "In the text, you have a positive precept"): Brooks argues from Matt 6:6's singular: "He saith
not, when #emph[you] pray, but #emph[thou] …". With both now "you", keep his point visible this way:
`He does not say, “when #emph[you#super[+]] pray,” in the plural, but “when #emph[you] pray,” in the singular,
“go into your closet,” …` (the plural mark carries the "ye"; "in the plural / in the singular" carries his word).

## Words

Follow the glossary (kept words; recurring renderings; Brooks's false friends from Precious Remedies). **No
archaic vocabulary left unexplained**, and **false friends REPLACED in the text with the modern word that carries
his sense** (rules §3.6; never a gloss, never "that is, …", never a parenthesis): change only the misleading word
or the smallest phrase, keep the sentence and voice; words merely old-fashioned but read rightly stay. The standing
list (rules §3.6 table) plus these, by sense: *professors* (professing Christians), *conversation* (conduct, way of
life), *let* (hinder), *prevent* (go before; "to prevent mistakes" = to forestall, stays), *presently* (at once),
*discover* (reveal), *still* (always), *several* (various, separate), *mean* (lowly), *estate* (state, condition),
*sensible* (aware, felt), *silly* (simple, helpless), *wit* (mind), *fond* (foolish), *curious* (overcurious,
prying; elaborate), *admire* (wonder at), *meat* (food), *nice* (fastidious), *quick* (living), *apprehend*
(grasp), *mere* (sheer), *owned* (acknowledged), *entertain* (receive), *improve* (make use of), *interest in*
(a share in), *temper* (disposition, frame), *motions* (stirrings), *security/secure* (complacency, complacent),
*the creature* (created things), *intercourse* (fellowship), *familiar* (intimate), *passion* (anger),
*mischief* (harm), *virtue* (power), *engage* (bind, pledge), *large* (conscience: lax), *brave* (fine, noble),
*naught* (wicked, worthless), *bravery* (finery), *bowels* (tender mercy), *physic* (medicine), *cordial*
(heart-medicine), *close with* (embrace), *humours* (infection), *closet* stays (glossary). Effectual stays.
Proverbs and sayings stay proverbs, in modern grammar.

**Plural you:** `you#super[+]` (your#super[+], You#super[+]) for Scripture's "ye"/"you" to many, and for Brooks
addressing his readers as many ("ye", "yourselves", "friends", "Christians, you …", "you that …"). The first
plural you/your of EVERY sentence of a plural address is marked, the rest of that sentence plain; Brooks's
singular "thou"/"thee" to the single reader is plain "you"; a general "you" (= one, anyone) is plain. **List in
your reply the paragraphs (file ¶N) that are a plural address throughout** (a script re-marks them later). Brooks's
"we / us / our" stay.

Read every rebuilt sentence against Brooks for its **direction** (no reversals), its **qualifiers** (only, all, not,
must/may, "as it were"), its **referents** (name God, Christ, the soul, the hypocrite where a pronoun could shift).
A "?" that is really an exclamation ("Oh, how … ?") becomes "!" (rules §2.5).

## Checks

After each file run the checker on your slice folder and fix what it reports until only genuine non-issues remain:
`python3 /home/courtney/Projects/fgbooks/work/modern-english/check.py /home/courtney/Projects/fgbooks/work/secret-key-modern/<LETTER>`
Then: every heading modernized (`diff <(grep '^=' chapters/typ/F) <(grep '^=' chapters/modern/F)`, each archaic
head changed); no straight quotes: `grep -n "[\"']" chapters/modern/*.typ`; no archaic words left:
`grep -nwiE 'hath|doth|thou|thee|thy|ye|unto|betwixt|asunder|whilst|amongst|thereof|wherein|whereby|yea|nay|saith|[a-z]+eth' chapters/modern/*.typ`
(each remaining hit justified: a Latin word, a name, "teeth").

## Reply

Short (under 300 words): files written; the checker's final output; every Scripture place where you adjusted the
BSB (and why); every mangled reference, wrong reference or misprint you suspect in the Classic (kept in the
Classic, written correctly in the Modern; file, ¶ number, Classic text, evidence); the plural-address paragraphs;
every place worth the editor's eye; recurring terms the glossary lacks with your rendering. Do not touch any file
outside your slice's `chapters/modern/`. Do not commit.
