"""False-friend scan: every Modern paragraph's hits of the lexicon (references/false-friends.tsv: the 2026-11-16
sweep's ~430 headwords and idioms, with past renderings), each with its Modern sentence and the Classic paragraph,
for a cheap model to classify (misleading here / fine) and a strong one to settle the doubtful.
python3 ff-scan.py PAIRS.jsonl [LEXICON.tsv [KEPT,WORDS]] > ff-hits.tsv
Hits inside quotation marks are marked q (Scripture: leave the BSB alone unless rules §5 applies). A word the
book's source/modern-glossary.md decided to keep is still listed: the classifier is told the glossary."""
import json, re, sys
from pathlib import Path

LEX = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent.parent / "references/false-friends.tsv"
rows = [l.split("\t") + ["", ""] for l in LEX.read_text().splitlines()[1:] if l.strip()]
alts = [r[3] if r[3] else r"\b" + re.escape(r[0]).replace(r"\ ", r"\s+") + r"(?:s|es|ed|d|ing)?\b"
        for r in rows if r[3] != "-"]
SKIP = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else set()  # the glossary's kept words, e.g. closet,closets
pat = re.compile("|".join(f"(?:{a})" for a in sorted(alts, key=len, reverse=True)), re.I)
plain = lambda s: re.sub(r"\s+", " ", re.sub(r"#[a-z]+(\.[a-z]+)*(\([^)]*\))?|[\[\]]", " ", s.replace("#super[+]", "⁺")))
sentences = lambda s: re.split(r"(?<=[.?!])\s+(?=[“A-Z])", s)
print("file\tn\thit\tq\tmodern_sentence\tclassic_paragraph")
n = 0
for l in open(sys.argv[1]):
    r = json.loads(l)
    m, c = plain(r["modern"]), plain(r["classic"])
    for s in sentences(m):
        for h in pat.finditer(s):
            if h.group(0).lower() in SKIP: continue
            q = "q" if s[:h.start()].count("“") > s[:h.start()].count("”") else ""
            print(f"{r['file']}\t{r['n']}\t{h.group(0).lower()}\t{q}\t{s.strip()}\t{c[:1500]}")
            n += 1
print(n, "hits", file=sys.stderr)
