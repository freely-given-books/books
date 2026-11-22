"""Scripture check: each quotation “…” followed by a reference (or a footnote reference) in the
Modern text, compared with the BSB. Prints quotations whose words are not found in the verse(s)
in order (ellipses allowed). python3 audit-scripture.py BOOK_DIR > scripture.tsv"""
import json, re, sys
from pathlib import Path
sys.argv, B = sys.argv[:1], Path(sys.argv[1])
src = Path(__file__).with_name("bsb.py").read_text().split("for ref in sys.argv")[0]
exec(src)                                    # D, NAMES
norm = lambda s: re.findall(r"[a-z0-9]+", s.lower().replace("’", "'").replace("'", ""))
def verses(ref, book=None):
    out = []
    m = re.fullmatch(r"\s*((?:\d )?[A-Za-z]+)?\.?\s*(\d+):([\d–,\s-]+)", ref)
    if not m: return None
    b = NAMES.get((m.group(1) or book or "").lower().strip())
    if not b: return None
    c = int(m.group(2))
    for part in re.split(r",\s*", m.group(3).strip()):
        a, _, z = part.partition("–") if "–" in part else part.partition("-")
        try:
            for v in range(int(a), int(z or a) + 1): out.append(D[b][c - 1][v - 1])
        except (IndexError, ValueError): return None
    return " ".join(out)
def contained(q, text):
    t = norm(text); pos = 0
    for chunk in re.split(r"…|\.\.\.", q):
        w = norm(chunk)
        if not w: continue
        found = next((i for i in range(pos, len(t) - len(w) + 1) if t[i:i + len(w)] == w), None)
        if found is None: return False
        pos = found + len(w)
    return True
REF = r"((?:[1-3] )?[A-Z][a-z]+\.? \d+:[\d–,\s-]+?)"
QUOTE = re.compile(r"“([^”]{12,}?)”[,.;:]?\s*(?:\(" + REF + r"\)|#footnote\[" + REF + r"\.?\]|" + REF + r"(?=[.;,]))")
print("file\tref\tquote\tbsb")
for f in sorted((B / "chapters/modern").rglob("*.typ")):
    t = re.sub(r"#smallcaps\[(\w+)\]", r"\1", f.read_text())
    t = re.sub(r"#emph\[([^\]]*)\]|you#super\[\+\]", lambda m: m.group(1) or "you", t)
    for m in QUOTE.finditer(t):
        q, ref = m.group(1), (m.group(2) or m.group(3) or m.group(4)).strip().rstrip(";,")
        ref = re.split(r";", ref)[0]
        v = verses(ref)
        if v is None:
            print(f"{f.stem}\t{ref}\t{q}\t?"); continue
        if not contained(q, v):
            print(f"{f.stem}\t{ref}\t{q}\t{v}")
