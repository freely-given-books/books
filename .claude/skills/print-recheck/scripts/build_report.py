"""Build classic-recheck-vol6.md, apply-input.jsonl and manual-edits.json from the verified findings below.
Checks each "ccel" occurs exactly once in its file. Usage: python3 -I build_report.py"""
import json, pathlib, collections, re, unicodedata
T = pathlib.Path("/home/courtney/Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-6")
D = pathlib.Path(__file__).resolve().parent
OUT = D.parent / "classic-recheck-vol6.md"

F = []
def add(file, anchor, ccel, w1845, proposed, page, kind, conf="high"):
    F.append(dict(file=file, anchor=anchor, ccel=ccel, **{"1845": w1845}, proposed=proposed, page=page, kind=kind, confidence=conf))
C = lambda n: f"book-4-chapter-{n:02d}.typ"

# --- words (d), CCEL's verb form (d/grammar): read on the page images (w1.png, w2.png, z.png) ---
add(C(16), "§? youth who, after being imbued duly and properly with the rudiments of piety", "being embued duly", "being imbued duly", "imbued", "III.375", "d")
add(C(17), "§? the seed which fell among thorns sprang up (1845 “sprang”)", "thorns sprung up", "thorns sprang up", "sprang", "III.435", "d/grammar")
add(C(20), "§? Yet we see that amid this diversity they all tend", "amidst this diversity", "amid this diversity", "amid", "III.539", "d")
add(C(20), "§? he will take your daughters to be confectionaries (1 Sam 8:13; 1845 “confectionaries”, the women who make them)", "be confectioneries,", "be confectionaries,", "confectionaries", "III.548", "d")
add(C(16), "§? note (French): si elle n’avoit point eté instituée de Dieu", "eté institutée de", "eté instituée de", "instituée", "III.350", "d")
add(C(18), "§? note (French): ceux qui sont les plus effrontés entre les Papistes", "plus effrontées entre", "plus effrontés entre", "effrontés", "III.467", "d")
# --- references where CCEL departs from the print and the print is right ---
add(C(16), "§? all kinds of fishes? (1845 “Matth. iv. 19”, “fishers of men”; CCEL 9:19)", "(Matt 9:19; 13:47)", "(Matth. iv. 19; xiii. 47.)", "(Matt 4:19; 13:47)", "III.381", "d")
add(C(20), "§? “Who can stretch forth his hand against the Lord’s anointed” (1845 “1 Sam. xxvi. 9-11”; CCEL 24:9–11)", "(1 Sam 24:9–11)", "(1 Sam. xxvi. 9-11.)", "(1 Sam 26:9–11)", "III.550", "d")

# --- capital letters (d/case): cases.tsv, read on cs1.png and single crops (z2.png, crops/z458b.png, crops/z519.png, crops/z419.png) ---
add(C(14), "§? give a ratification of the gifts which the Divine liberality has bestowed", "the divine liberality has", "the Divine liberality has", "Divine", "III.316", "d/case")
add(C(17), "§? On hearing the words of Christ, This is my body", "Christ, this is my", "Christ, This is my", "This", "III.419", "d/case")
add(C(18), "Sections 14. Those who mutter over the Mass cannot be called priests", "mutter over the mass", "mutter over the Mass", "Mass", "III.458", "d/case")
add(C(18), "Sections 19. the views which ought to be held concerning Baptism and the Lord’s Supper", "concerning baptism and", "concerning Baptism and", "Baptism", "III.458", "d/case")
add(C(18), "§? the way in which the sounder schoolmen at first received", "sounder Schoolmen at", "sounder schoolmen at", "schoolmen", "III.458", "d/case")
add(C(18), "§? While the Supper itself is a gift of God", "While the supper itself", "While the Supper itself", "Supper", "III.465", "d/case")
add(C(18), "§? But what else is done in the Mass than", "done in the mass", "done in the Mass", "Mass", "III.472", "d/case")
add(C(19), "Argument: Impiety of the Popish teachers in attributing more", "the popish teachers", "the Popish teachers", "Popish", "III.479", "d/case")
add(C(19), "§? and shut the doors of churches?", "doors of Churches?", "doors of churches?", "churches", "III.504", "d/case")
add(C(19), "§? The last of all is Marriage, which", "is marriage, which", "is Marriage, which", "Marriage", "III.513", "d/case")
add(C(19), "§? “I am the true vine, and my Father is the husbandman”", "my father is", "my Father is", "Father", "III.514", "d/case")
add(C(20), "Argument: Next, the three forms of civil government are added", "three Forms of", "three forms of", "forms", "III.518", "d/case")
add(C(20), "Sections 12. Objection, that the lawfulness of War is not taught in Scripture", "lawfulness of war is", "lawfulness of War is", "War", "III.519", "d/case")
add(C(20), "Sections 16. All laws should be just", "All Laws should", "All laws should", "laws", "III.519", "d/case")
add(C(20), "Sections 16. Civil law of Moses; how far in force", "Civil Law of Moses", "Civil law of Moses", "law", "III.519", "d/case")
add(C(20), "§? Augustine: “If Scripture called them gods, to whom the word of God came”", "called them Gods,", "called them gods,", "gods", "III.523", "d/case")
add(C(20), "§? “The kings of the Gentiles exercise lordship over them”", "of the gentiles", "of the Gentiles", "Gentiles", "III.526", "d/case")
add(C(20), "§? defending the honor of Him whose vicegerents they are", "honor of him whose", "honor of Him whose", "Him", "III.529", "d/case")
add(C(20), "§? the passion for litigation prevailed in the church of Corinth", "in the Church of Corinth", "in the church of Corinth", "church", "III.543", "d/case")

# --- 1845 misprints (the Classic keeps CCEL) ---
add(C(15), "§? nothing which is appropriate would be omitted [keep CCEL (1845 “which i appropriate”)]", "which is appropriate", "which i appropriate", "", "III.344", "misprint-1845", "-")
add(C(17), "§? “Every spirit that confesseth not …” (1 John 4:3) [keep CCEL (1845 “1 John iv. 23”; the chapter has 21 verses)]", "(1 John 4:3; 2 John 7)", "(1 John iv. 23; 2 John ver. 7.)", "", "III.432", "misprint-1845", "-")
add(C(17), "§? neglecting and almost suppressing them [keep CCEL (1845 “suppresing”)]", "almost suppressing them", "almost suppresing them", "", "III.432", "misprint-1845", "-")
add(C(19), "§? note: John 2:15; 10:7; Luke 4:17; Mark 7:33 [keep CCEL (1845 “Matth. vii. 33”; Matthew 7 has 29 verses, the spittle and the tongue are Mark 7:33)]", "Mark 7:33;", "Matth. vii. 33;", "", "III.503", "misprint-1845", "-")
add(C(20), "§? note: Exod 2:12; Acts 7:24 [keep CCEL (1845 “Acts vii. 21”; Moses strikes the Egyptian in 7:24)]", "Exod 2:12; Acts 7:24;", "Exod. ii. 12; Acts vii. 21;", "", "III.532", "misprint-1845", "-")
add(C(20), "§? note: Prov … 17:15; 17:11; 24:24 [keep CCEL (1845 “xvii. 14”; the text quotes 17:11, “An evil man seeketh only rebellion”, III.533)]", "17:15; 17:11; 24:24.]", "xvii. 15; xvii. 14; xxiv. 24.", "", "III.532", "misprint-1845", "-")
add(C(20), "§? from the governor to Cæsar’s judgment seat [keep CCEL (1845 “Cesar’s” here; vol. 5 has “Cæsars”, III.149)]", "governor to Cæsar’s", "governor to Cesar’s", "", "III.541", "misprint-1845", "medium")
add(C(20), "§? raised up by him to punish the people for their iniquity [keep CCEL (1845 “so punish”)]", "by him to punish", "by him so punish", "", "III.546", "misprint-1845", "-")

# section numbers in hand-written anchors: recompute from the file
for f in F:
    src = (T / f["file"]).read_text(); pos = src.find(f["ccel"])
    if pos < 0: continue
    secs = [m for m in re.finditer(r"(?m)^(\d+)\\\. ", src[:pos])]
    f["anchor"] = re.sub(r"§(\d+|\?)", ("§" + secs[-1].group(1)) if secs else "Sections/heads,", f["anchor"], count=1)
bad = [(n, f["file"], f["ccel"]) for f in F if (n := (T / f["file"]).read_text().count(f["ccel"])) != 1]
if bad:
    for b in bad: print("NOT UNIQUE", b)
    raise SystemExit(1)

ORDER = [C(n) for n in range(14, 21)]
def pkey(p): return int(str(p).split(".")[1])
cnt = collections.Counter(f["kind"] for f in F)
esc = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
L = []
L.append("# Calvin, Institutes, vol. 6 (Book IV, chapters 14–20): Classic re-checked against the 1845 printing (Kraken OCR)\n")
L.append("""Base: `chapters/typ/vol-6/*.typ` in the `wt-institutes` worktree (book-4-chapter-14 … book-4-chapter-20; read only;
HEAD c1b462e7). Witness: Calvin Translation Society, Edinburgh 1845, our own scans, Kraken OCR with ALTO beside it, page images
`pages/p-NNNN.png`. Book IV ch. 14–20 lie wholly in **1845 vol. 3, pp. 299–554** (`work/institutes/vol3/kraken/`, image =
printed page + 4, images 303–558): ch. 14 begins p. 299 (image 303), ch. 15 p. 327, ch. 16 p. 349, ch. 17 p. 386, ch. 18
p. 457, ch. 19 p. 479, ch. 20 p. 518 (image 522), and Book IV ends on p. 554 (image 558) with “END OF THE INSTITUTES.”; the One
Hundred Aphorisms from image 559 on are not part of this volume and were not compared. In the **p.** column **III.n** is a page
of 1845 vol. 3.
Method (as vol. 5, same scripts adapted): every .typ file was aligned word by word with the Kraken text (difflib; main text
first, then the footnotes against the OCR words the main text left over; running heads dropped; line-end hyphens joined).
Differences were filtered for reference style (Roman → Arabic compared as numbers), American spelling and OCR noise; then
every remaining candidate (116 word and 40 reference rows, 20 capital-letter rows, 17 long runs) was read, and every one
that was not plain OCR noise was checked on the page image (line crops from the ALTO boxes: `w1.png`, `w2.png`, `z.png`,
`z2.png`, `r1.png`, `r2.png`, `cs1.png`, `gk.png` (the Greek), single crops in `crops/`). Two checks were added this time:
`doubles.py` compares the aligned words again with doubled letters kept (the aligner's fold collapses them, so a slip like
“suppresing” is invisible to it), and `bookcheck.py` lists reference rows whose numbers agree but whose book names differ
(the filter drops those). Every reference left unmatched in the OCR was checked against the CCEL text of its own chapter
(`refcheck.py`), every OCR run of two or more words left unmatched was read, and the footnotes were counted chapter by
chapter (`notecount.py`) and page by page (`notepages.py`) against CCEL's; every difference in the counts was traced. Only
what the image confirms is listed.
Scripts and raw candidates: `work/institutes/latin/vol6/recheck/` (`align.py`, `filter.py`, `refcheck.py`, `notepages.py`,
`notecount.py`, `doubles.py`, `bookcheck.py`, `crop.py`, `mkbatch.py`, `batch.sh`, `cand.json`, `cand.tsv`, `cand2.tsv`,
`cases.tsv`, `doubles.tsv`, `residual.txt`, `notepages.txt`, `build_report.py`, `apply-input.jsonl`, `manual-edits.json`,
`apply_recheck.py` (now with `VOLDIR`), `dryrun.txt`).

**Rule applied (editor, 2026-11-23):** the Classic follows the 1845 print wherever CCEL's wording departs from it, including
CCEL's modernised grammar (kind **d/grammar**) and CCEL additions (kind **c**). Not listed: Arabic reference style, American
spelling (1845 forms here: honour, favour, recognising, catechising, practised, despatch, sepulchre, grey, phrenzy, stye,
counsellor, fulfil/fulfilment, worshipper, quarrelling, enrol, carcases…), CCEL's punctuation around references, CCEL's word
joins (1845 “any thing”, “every thing”, “every where”, “good-will”, “judgment-seat”), Greek accents. The `proposed` column holds
only the replacement words; explanations are in the anchor and kind columns; an empty `proposed` means no change to the text
(misprint-1845). Where a row needs more than one word changed, or words added, `proposed` holds the whole replacement snippet
and the change is in `manual-edits.json`.

**Kinds:** b (1845 words missing in CCEL), c (CCEL words absent from 1845), d (a different word), d/grammar (CCEL's
modernised verb form), d/case (capital letter differs from the print), n (notes), misprint-1845 (the 1845 print is wrong;
CCEL corrects it).

**Counts:** """ + ", ".join(f"{k} {v}" for k, v in sorted(cnt.items())) + f" (total {len(F)}); no rows of kind b, c or n.\n")
L.append("""**Systematic check.** As in vol. 5 the verb forms agree: the OCR of pp. 299–554 and the seven .typ files alike give has
220, hath 17, does 75, Does 2, doth 3, saith 4, says 130, cometh 3, maketh 1, makes 43 (comes 8 against 7 is the print's
line-end “be-comes”). The one CCEL verb change is **sprung for “sprang”** (III.435, kind d/grammar). There is no “an” before
u- or h- that CCEL has made “a” (the print's an high ×2, an honest, an ubiquity, an un- ×10 all stand in CCEL). The word rows
are single CCEL slips: embued for *imbued*, amidst for *amid*, confectioneries for the print's (and the Authorised Version's)
*confectionaries*, and two French notes, “institutée” for *instituée* (III.350) and “effrontées” for *effrontés* (III.467).
Two Scripture references in the main text are wrong in CCEL and right in the print: Matt 9:19 for **4:19** (“fishers of men”,
III.381) and 1 Sam 24:9–11 for **26:9–11** (“Who can stretch forth his hand against the Lord's anointed, and be guiltless?”,
III.550). The capital comparison gives 20 rows: 19 are listed, one (III.386, “The knowledge of the sacrament”) is an OCR
misreading. CCEL adds nothing to the text that the print lacks (no kind c), and leaves out nothing (no kind b). Eight 1845
misprints are listed so that nobody “restores” them; four are footnote or text references the print gets wrong (1 John iv. 23,
Matth. vii. 33, Acts vii. 21, Prov. xvii. 14). This volume had already been checked against 1845 once (`bca6e3c6`, 134 findings;
`a2b5470c`, 8 references; and the typesetting sweep `06d783b4`), which is why so little is left.

**Also seen, not listed:** reference style (“Chap. xiv.” / “Chapter 14”, “Book III. Chap. xix.” / “Book 3 Chapter 19”,
“2 John ver. 7” / “2 John 7”, “Lib. iii.” / “Lib. 3”); CCEL's punctuation in the Father references (“&c.;” / “&c.,” at III.394,
“Art. 4” / “Art 4”, “Ad Concil.” / “Ad. Concil.” at III.375, “Dist. 5.” / “Dist. 5,” at III.489); “coeur” / “cœur” in the
French note at III.351 (a ligature); Greek accents; the other
“the divine liberality and kindness” (III.311, lower-case in the print too); spellings in the rule above.

**Structural:** no Beveridge footnote is missing in vol. 6 and none is added: CCEL has 67 notes (ch. 14–20: 5, 5, 3, 15, 11,
17, 11) and the print has the same. Chapters 14, 15 and 18 gave the same count at once; the differences in ch. 16, 17, 19
and 20 were signatures (“2A”, “2B”, “2D”–“2F”, “2H”, “2K”–“2M”) the counter took for notes, the note at III.457 that sits
on the page where ch. 18 begins, and notes whose first line the counter missed (“1 John ii. 18…”, III.477; “du temps de
Sainct Augustin”, III.488; “On conte trois especes de regime civil”, III.527; the two notes at III.532); each was found on its
page, and the note texts agree (the references in the notes were read on the image, `r1.png`, `r2.png`). Every OCR run left
unmatched after both passes is a reference present in CCEL in Arabic form (`refcheck.py` flags only OCR misreadings and the
listed rows), a running head or a signature (“VOL. III.”, “2A”…); no CCEL word is left without an OCR partner except a note
bracket and a section number. No CCEL line is absent from 1845 and no 1845 line from CCEL; the chapter titles, arguments and
Sections lists agree (capitals apart, listed).
""")
for fn in ORDER:
    rows = sorted([f for f in F if f["file"] == fn], key=lambda r: pkey(r["page"]))
    if not rows: continue
    title = fn.replace(".typ", "").replace("book-4-chapter-", "Book IV, chapter ").replace("chapter 0", "chapter ")
    L.append(f"\n## {title} \u2014 `{fn}`\n")
    L.append("| anchor | CCEL | 1845 | proposed | p. | kind | conf. |\n|---|---|---|---|---|---|---|")
    for r in rows:
        L.append(f"| {esc(r['anchor'])} | {esc(r['ccel'])} | {esc(r['1845'])} | {esc(r['proposed'])} | {r['page']} | {r['kind']} | {r['confidence']} |")
L.append("\n## Findings (one JSON line each)\n\n```")
for fn in ORDER:
    for r in sorted([f for f in F if f["file"] == fn], key=lambda r: pkey(r["page"])):
        L.append(json.dumps(r, ensure_ascii=False))
L.append("```\n")
OUT.write_text("\n".join(L))
# apply-input.jsonl: rows the apply tool changes (as vols 2-4: no misprint-1845)
with open(D / "apply-input.jsonl", "w") as fa:
    for fn in ORDER:
        for r in sorted([f for f in F if f["file"] == fn], key=lambda r: pkey(r["page"])):
            if r["kind"] == "misprint-1845": continue
            fa.write(json.dumps(r, ensure_ascii=False) + "\n")
# rows that are not a one-word swap: whole snippets, applied by hand-checked replacement
MANUAL = [[f["file"], f["ccel"], f["proposed"]] for f in F if f["kind"] in ("b", "c") or (f["kind"] == "d" and " " in f["proposed"]) or f["proposed"].count(" ") >= 2]
for fn, old, new in MANUAL:
    assert (T / fn).read_text().count(old) == 1, old
json.dump(MANUAL, open(D / "manual-edits.json", "w"), ensure_ascii=False, indent=1)
print(OUT, len(F), dict(cnt))
