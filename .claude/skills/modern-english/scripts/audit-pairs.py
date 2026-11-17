"""Paragraph pairs Classic/Modern for the meaning audit: python3 audit-pairs.py BOOK_DIR OUT_DIR
Writes OUT_DIR/pairs.jsonl ({file, n, classic, modern}) and OUT_DIR/pairs-<file>.md for readers."""
import json, re, sys
from pathlib import Path

B, OUT = Path(sys.argv[1]), Path(sys.argv[2])
rows = []
# every file, sub-folders too (part-1/...); its name in the pairs with "/" as "_"
# in book order: the print file's #include lines, then any other file
inc = [l.split('"')[1].split("chapters/typ/", 1)[1] for pf in sorted(B.glob("*.typ"))
       if not pf.stem.endswith("-modern") and not pf.stem.startswith("cover")
       for l in pf.read_text().split("\n") if l.lstrip().startswith("#include") and "chapters/typ/" in l]
mods = {str(p.relative_to(B / "chapters/modern")): p for p in (B / "chapters/modern").rglob("*.typ")}
for mp in [mods[f] for f in dict.fromkeys(inc) if f in mods] + [mods[f] for f in sorted(set(mods) - set(inc))]:
    f = str(mp.relative_to(B / "chapters/modern"))
    a = [p.strip() for p in re.split(r"\n\s*\n", (B / "chapters/typ" / f).read_text()) if p.strip()]
    b = [p.strip() for p in re.split(r"\n\s*\n", mp.read_text()) if p.strip()]
    assert len(a) == len(b), f
    ch = f.removesuffix(".typ").replace("/", "_")
    md = []
    for k, (x, y) in enumerate(zip(a, b), 1):
        rows.append({"file": ch, "n": k, "classic": x, "modern": y})
        md.append(f"## {ch} ¶{k}\n\nCLASSIC:\n{x}\n\nMODERN:\n{y}\n")
    (OUT / f"pairs-{ch}.md").write_text("\n".join(md))
with open(OUT / "pairs.jsonl", "w") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(rows), "pairs")
