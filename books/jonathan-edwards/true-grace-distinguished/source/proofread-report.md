# Proofread: True Grace, Distinguished from the Experience of Devils

2026-11-21. Base: Evans-TCP N05520 (New York, 1753), the only printing in Edwards's lifetime.

## How it was read

No free scan of the 1753 printing exists (SOURCES.md), so the house routine's Qwen flags and gap
marker were not run. Instead, at the editor's wish, **two full, independent close reads by Claude**
of the whole sermon against page images: the TCP text, word by word, against the Leeds *Works*
(1806, vol. 8, Sermon V, pp. 107-139), the earliest free page images, with CCEL (Hickman, 1834) as a
keyed second witness and the KJV for every quotation. Read A in five sections (TCP pp. 3-10,
11-18, 19-26, 27-34, 35-42), read B in six with other boundaries (3-9, 10-15, 16-21, 22-28,
29-35, 36-42), each section by its own reader; 144 and 150 findings, every one settled by hand
(work/true-grace/read/out-*.jsonl, review/edits.py). Most findings (188) are places where Leeds
cuts or smooths Edwards; the TCP's fuller text stands in all of them. Then a book-review pass:
refstyle, sweep, refs --quotes (55 references, none missing, no weak quote), spelling and case
against CCEL's vocabulary, the machine's sentence case checked against the print.

Since Leeds is not the 1753 printing, no TCP reading is corrected in the as-printed layer; every
fix below is a reading-text decision (`#editor`), the printed word kept beside it.

## Gaps (4, all filled; GAP_FIXES)

p. 5 "cannot [b]e"; p. 12 "mighty efforts, [restless] and indefatigable"; p. 15 "awfu[l]
threatenings"; p. 19 "as he will the[n]". Both reads, Leeds and CCEL agree on each.

## Slips corrected in the reading text (both reads found each unless marked)

| p. | as printed (TCP) | now | evidence |
| --- | --- | --- | --- |
| 8 | pare in heart | pure in heart | Leeds; Matt 5:8 |
| 12 | prevent and wrest the Scripture | pervert | Leeds, CCEL |
| 13 | Matt. xii. 27 | Matt 11:27 | the verse quoted |
| 13 | John, xvii. (no verse) | John 17:3 | Leeds; the verse quoted |
| 14 | all found | all sound | long s keyed as f |
| 15 | There will no such thing | will be no | Leeds |
| 16 | Isai. xxxvi. 10, 11 | Isa 26:10, 11 | the verses quoted |
| 16 | he will dead unjustly / ye the fire | deal / yea | Isa 26:10-11 |
| 17 | Ps. 1. 21 | Ps 50:21 | roman l keyed as 1; Leeds "l. 21" |
| 17 | wedding Grrment: And be saith | garment ... he saith | Matt 22:12 |
| 17 | the King came to see | came in to see | Matt 22:11, Leeds |
| 18 | the Hear and will | heart | Leeds |
| 19 | now, that it will be | than | Leeds |
| 20 | Inquities | iniquities | Leeds |
| 23 | It they tremble | If | Leeds |
| 24 | shining fort' | forth | Matt 13:43 |
| 25 | the comparative. Momentariness | no stop | Leeds |
| 25 | Prov. iv. 11, 12, 13 | Prov 5:11-13 | the verses quoted (Leeds has iv too: the 1753 printer's) |
| 26 | the work of immortal souls | worth | Leeds; "the worth of immortal souls" p. 25 |
| 29 | have been; mentioned | no semicolon | |
| 31 | 'Tis for the joint exercise | from | Leeds, CCEL; the parallel clauses |
| 31 | Except-your | Except your | Matt 5:20 |
| 33 | has released, him | no comma | |
| 36 | the Son of God, is REVEALED | no comma | Leeds |
| 36 | Medator | Mediator | |
| 38 | Not a novice left ... he fell | lest ... he fall | 1 Tim 3:6, Leeds |
| 39 | Thou believest there is | that there is | Jas 2:19 (the text as printed at the head), Leeds |
| 39 | walk in the light, or he is | as he is | 1 John 1:7, Leeds |
| 39 | that we keep his commandments | if we keep | 1 John 2:3, Leeds |
| 40 | approved of man | men | Rom 14:18, Leeds |
| 41 | A: Partaking | A partaking | |
| 41 | Peace with passeth | which | Phil 4:7 |
| 42 | drink's it; that suns rising | drinks; sun's | |

Also: three questions the print closes with a stop given their question marks (pp. 21, 32), and
a few points of sense punctuation (p. 28 "reasoning: that"; "at the day of judgment; when";
p. 25 "however true godliness" = although; p. 30 "of this, that is the thing"; p. 9 "things of
religion").

## Kept as printed (Edwards's own, all witnesses agree)

John 8:44 "there was no truth"; Jas 3:17 "gentle, easy to be entreated"; Rom 3:19 "them that";
Luke 6:32 "what thank have you"; 2 Cor 4:4 "shine into them"; 1 John 3:18 "in word and in
tongue"; 1 John 5:1 for "the Son of God"; "has felt them" (p. 12); "they believe ... and
believes" (p. 36); the opening's "which is the / 4. Thing observable"; the emphatic capitals
(MANIFESTS, REVEALED, BELIEVE NOT).

## Open questions (Vikunja, project 18)

1. p. 5 "unless something be added to them, beyond what is in them, or they are in the devil":
   read "as they are in the devil"? (recommended; kept as printed for now)
2. p. 26 "The awful majesty of God, are greatly made manifest": read "is"? (recommended; kept)
3. p. 37 "and not on having of it immediately suggested": read "and not the having of it"?
   (recommended; kept)
4. The wording batch above (rule 3): approve the slips corrected.
