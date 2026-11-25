"""Second look at aligned word pairs that align.py's fold treats as equal: list pairs whose letters differ once
doubled letters are kept (fold collapses them), so slips like suppresing/suppressing are seen. Writes doubles.tsv.
Usage: python3 -I doubles.py"""
import re, pathlib, difflib, unicodedata, collections
D = pathlib.Path(__file__).resolve().parent
src = (D / "align.py").read_text().replace("\nmain()\n", "\n")
ns = {"__file__": str(D / "align.py")}; exec(compile(src, "align", "exec"), ns)
K = ns["ocr_stream"]("kraken"); fold = ns["fold"]; T = ns["T"]
def lite(w):
    w = unicodedata.normalize("NFKD", w)
    w = "".join(c for c in w if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z]", "", w)
MT, NT = [], []
for f in sorted(T.glob("*.typ")):
    m, nt = ns["parse_typ"](f.read_text())
    MT += [(w, f.name) for w, s, e in ns["tokens"](m)]
    NT += [(w, f.name) for w, s, e in ns["tokens"](nt) if w != "‖"]
out = collections.Counter(); where = {}
def run(A, Bidx):
    sm = difflib.SequenceMatcher(None, [fold(t[0]) for t in A], [fold(K[j][0]) for j in Bidx], autojunk=False)
    used = set()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal": continue
        for k in range(i2 - i1):
            j = Bidx[j1 + k]; used.add(j)
            a, b = lite(A[i1 + k][0]), lite(K[j][0])
            if a and b and a != b and len(a) > 3 and re.sub(r"(.)\1", r"\1", a) == re.sub(r"(.)\1", r"\1", b):
                out[(a, b)] += 1; where.setdefault((a, b), (A[i1 + k][1], ns["plabel"](K[j][1])))
    return used
used = run(MT, list(range(len(K))))
run(NT, [j for j in range(len(K)) if j not in used])
with open(D / "doubles.tsv", "w") as fo:
    for (a, b), n in sorted(out.items()):
        fo.write(f"{a}\t{b}\t{n}\t{where[(a, b)][0]}\t{where[(a, b)][1]}\n")
print(len(out))
