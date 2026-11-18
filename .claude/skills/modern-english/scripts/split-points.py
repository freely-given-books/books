"""Split-point check: paragraphs where the Modern rebuilt the sentences (more or fewer sentences than the Classic,
or quoted speech turned indirect or the reverse). These hold the errors every audit stage missed: a pronoun now
pointing at someone else, a fragment ("If he ... ."), a quotation reframed. python3 split-points.py PAIRS.jsonl
> split-points.tsv; each row is read by a strong model for referents and grammar (models.md)."""
import json, re, sys
plain = lambda s: re.sub(r"#[a-z]+(\.[a-z]+)*(\([^)]*\))?|[\[\]]", " ", s)
sents = lambda s: [x for x in re.split(r"(?<=[.?!;:])\s+", re.sub(r"\s+", " ", plain(s)).strip()) if x]
print("file\tn\tclassic_sentences\tmodern_sentences\tquotes_classic\tquotes_modern\tfragment_suspects")
FRAG = re.compile(r"(?:^|\s)(If|When|Though|Although|Because|Unless|Whereas|While|Since)\b[^.?!]*\.\s*$")
for l in open(sys.argv[1]):
    r = json.loads(l)
    a, b = sents(r["classic"]), sents(r["modern"])
    qa, qb = r["classic"].count("“"), r["modern"].count("“")
    frag = [s for s in b if FRAG.match(s) and "," not in s][:3]
    if len(b) > len(a) + 1 or len(b) < len(a) or qa != qb or frag:
        print(f"{r['file']}\t{r['n']}\t{len(a)}\t{len(b)}\t{qa}\t{qb}\t{' | '.join(frag)}")
