"""Harmonize the drafters' slices in the book's chapters/modern: python3 harmonize.py BOOK_DIR
LORD -> #smallcaps[Lord]; "Holy Ghost" -> "Holy Spirit"; straight quotes reported; heading checks."""
import re, sys
from pathlib import Path
B = Path(sys.argv[1]); M, T = B / "chapters/modern", B / "chapters/typ"
n = 0
for p in sorted(M.glob("*.typ")):
    t = p.read_text()
    u = re.sub(r"(?<![\w\[])LORD(?![\w\]])", "#smallcaps[Lord]", t)
    u = u.replace("Holy Ghost", "Holy Spirit")
    if u != t: p.write_text(u); n += 1
    for k, l in enumerate(u.split("\n"), 1):
        if re.search(r"[\"']", re.sub(r"#[a-z.]+\([^)]*\)", "", l)): print(f"{p.name}:{k}: straight quote")
print(n, "files harmonized")
ARCH = re.compile(r"\b(hath|doth|thou|thee|thy|thine|ye|unto|betwixt|asunder|whilst|amongst|thereof|wherein|whereby|"
                  r"canst|wouldst|shalt|wilt|art|want|discovers?|prevalency|[a-z]{2,}eth)\b", re.I)
OK = {"teeth", "beneath", "seventh", "eleventh", "twentieth", "death", "breath", "eighth", "twelfth"}
for p in sorted(M.glob("*.typ")):
    hm = [l for l in p.read_text().split("\n") if l.startswith("=")]
    hc = [l for l in (T / p.name).read_text().split("\n") if l.startswith("=")]
    assert len(hm) == len(hc), p.name
    for a, b in zip(hc, hm):
        bad = [w for w in ARCH.findall(b) if w.lower() not in OK]
        if bad: print(f"{p.name}: archaic in Modern heading {bad}: {b}")
        if a == b and ARCH.search(a) and [w for w in ARCH.findall(a) if w.lower() not in OK]:
            print(f"{p.name}: Modern heading identical to Classic with archaic word: {a}")
