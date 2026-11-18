"""Join the slices' Modern English chapters into the book, by WORK_DIR/plan.json (from slice.py), putting the
part files of a cut chapter back together: python3 join.py WORK_DIR [BOOK_DIR]  (BOOK_DIR defaults to the plan's)."""
import json, sys
from pathlib import Path

W = Path(sys.argv[1])
plan = json.loads((W / "plan.json").read_text())
DST = Path(sys.argv[2] if len(sys.argv) > 2 else plan["book"]) / "chapters/modern"
where = {f: s["drafter"] for s in plan["slices"] for f in s["files"]}
read = lambda f: (W / where[f] / "chapters/modern" / f).read_text()
missing = [f for f in where if not (W / where[f] / "chapters/modern" / f).exists()]
assert not missing, f"not drafted yet: {missing}"
done = set()
for stem, n in plan["cuts"].items():
    parts = [read(f"{stem}-{i}.typ").strip("\n") for i in range(1, n + 1)]
    out = DST / f"{stem}.typ"; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n\n".join(parts) + "\n")
    done |= {f"{stem}-{i}.typ" for i in range(1, n + 1)}
for f in where:
    if f in done: continue
    out = DST / f; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(read(f).rstrip("\n") + "\n")
print("joined", len(list(DST.rglob("*.typ"))), "files into", DST)
