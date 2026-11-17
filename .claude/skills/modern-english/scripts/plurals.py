"""Plural marks, the house style (rules §4; Surest Way lesson): in every paragraph the drafters marked as a plural
address (it holds a you⁺) and whose Classic has no singular thou/thee/thy, mark the first you/your of EVERY
sentence; the rest of a sentence stays plain. python3 plurals.py BOOK_DIR [--write]  (without --write: counts only)"""
import re, sys
from pathlib import Path
THOU = re.compile(r"\b(thou|thee|thy|thine|thyself)\b", re.I)
YOU = re.compile(r"\b([Yy]ou(?:rs|r|rselves)?)\b(?!#super)")
B = Path(sys.argv[1]) / "chapters"
total = 0
for mp in sorted((B / "modern").rglob("*.typ")):
    cps = [p for p in re.split(r"\n\s*\n", (B / "typ" / mp.relative_to(B / "modern")).read_text()) if p.strip()]
    mps = re.split(r"(\n\s*\n)", mp.read_text())
    k, n = 0, 0
    for i in range(0, len(mps), 2):
        if not mps[i].strip(): continue
        c = cps[k]; k += 1
        if "#super[+]" not in mps[i] or THOU.search(c): continue
        out = []
        for s in re.split(r"(?<=[.?!])(\s+)", mps[i]):
            if "#super[+]" not in s and not s.isspace():
                s, a = YOU.subn(r"\1#super[+]", s, count=1); n += a
            out.append(s)
        mps[i] = "".join(out)
    if n and "--write" in sys.argv: mp.write_text("".join(mps))
    if n: print(f"{mp.name}: {n}")
    total += n
print(total, "marks", "written" if "--write" in sys.argv else "to add (run with --write)")
