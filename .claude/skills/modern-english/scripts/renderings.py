"""Rendering table after the join: how each recurring thing came out across slices (and, with more PAIRS files,
across books), so the coordinator settles each once.
python3 renderings.py PAIRS.jsonl [MORE_PAIRS.jsonl ...] > renderings.md
1. Each Scripture reference quoted more than once: its distinct Modern quotation texts (one verse, one rendering;
   rules §7, Surest Way lesson). 2. Each lexicon headword in the Classic: the distinct words standing in the Modern
   paragraph where it stood (crudely: the Modern sentence with the most shared words), so "humors -> infection"
   in one slice and "bad humors" in another show up. 3. Opening formulas ("Look, as" / "Just as")."""
import json, re, sys, collections
from pathlib import Path
REF = re.compile(r"“([^”]{12,400})”\s*\(([^()]*?\d+:\d+[^()]*)\)")
quotes = collections.defaultdict(lambda: collections.defaultdict(list))
openers = collections.Counter()
for path in sys.argv[1:]:
    for l in open(path):
        r = json.loads(l)
        for q, ref in REF.findall(r["modern"]):
            key = re.sub(r"\s+", " ", q.strip(" ,.;:!?")).lower()
            quotes[ref.strip()][key].append(f"{Path(path).parent.name}:{r['file']} ¶{r['n']}")
        m = re.match(r"\s*([A-Z][a-z]+,? (?:as|so|then|now|here|there|this|that)\b)", r["modern"])
        if m: openers[m.group(1)] += 1
print("# Renderings\n\n## Verses quoted more than once with different words\n")
for ref, d in sorted(quotes.items()):
    ks = list(d)
    if len([k for k in ks if not any(k != o and k in o for o in ks)]) > 1:  # not just a shorter quotation of the same
        print(f"### {ref}")
        for q, where in d.items(): print(f"- “{q}” — {', '.join(where[:6])}{' …' if len(where) > 6 else ''}")
        print()
print("## Paragraph openers\n")
for k, v in openers.most_common(40): print(f"- {k}: {v}")
