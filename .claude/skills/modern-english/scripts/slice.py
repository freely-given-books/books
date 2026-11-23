"""Slice a book's Classic chapters into drafter folders and write plan.json:
python3 slice.py BOOK_DIR WORK_DIR [--words 7500]

Whole chapter files are grouped in order into slices of about --words Classic words; a file much larger than
that is cut at paragraph boundaries (preferring a heading line) into part files <stem>-<n>.typ, put back together
by join.py. Each slice is a mini book folder WORK_DIR/<A, B, ...>/chapters/{typ,modern}, so check.py runs on it.
Order: the print file's #include lines. Prints the plan; never touches the book."""
import json, re, sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
B, W = Path(args[0]), Path(args[1])
TARGET = int(sys.argv[sys.argv.index("--words") + 1]) if "--words" in sys.argv else 7500
T = B / "chapters/typ"
# book order: the print file's #include lines (volumes too), then any chapter file they don't name
inc = [l.split('"')[1].split("chapters/typ/", 1)[1] for pf in sorted(B.glob("*.typ"))
       if not pf.stem.endswith("-modern") and pf.stem not in ("cover", "cover-modern")
       for l in pf.read_text().split("\n") if l.lstrip().startswith("#include") and "chapters/typ/" in l]
files = list(dict.fromkeys(inc)) + sorted(set(p.relative_to(T).as_posix() for p in T.rglob("*.typ")) - set(inc))
words = lambda s: len(re.findall(r"[A-Za-z’']+", s))


def cut(text):
    """Cut text into ~TARGET-word parts at blank-line paragraph starts, preferring heading lines."""
    blocks = text.rstrip("\n").split("\n\n")
    parts, cur, n = [], [], 0
    for i, b in enumerate(blocks):
        cur.append(b); n += words(b)
        nxt = blocks[i + 1] if i + 1 < len(blocks) else None
        if nxt is None: break
        if n >= TARGET * (0.8 if nxt.startswith("=") else 1.0) and words("\n\n".join(blocks[i + 1:])) > TARGET * 0.3:
            parts.append("\n\n".join(cur) + "\n"); cur, n = [], 0
    parts.append("\n\n".join(cur) + "\n")
    assert "\n\n".join(p.rstrip("\n") for p in parts) == text.rstrip("\n")
    return parts


units, cuts = [], {}
for f in files:
    t = (T / f).read_text()
    if words(t) > TARGET * 1.4:
        ps = cut(t)
        cuts[f[:-4]] = len(ps)
        units += [(f"{f[:-4]}-{i}.typ", p) for i, p in enumerate(ps, 1)]
    else:
        units.append((f, t))

slices, cur, n = [], [], 0
for name, t in units:
    if cur and n + words(t) > TARGET * 1.25:
        slices.append(cur); cur, n = [], 0
    cur.append((name, t)); n += words(t)
if cur: slices.append(cur)

letters = [chr(65 + i) if i < 26 else f"Z{i - 25}" for i in range(len(slices))]
plan = []
for L, s in zip(letters, slices):
    for name, t in s:
        p = W / L / "chapters/typ" / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(t)
    (W / L / "chapters/modern").mkdir(parents=True, exist_ok=True)
    plan.append({"drafter": L, "files": [x for x, _ in s], "words": sum(words(t) for _, t in s)})
(W / "plan.json").write_text(json.dumps({"book": str(B.resolve()), "cuts": cuts, "slices": plan}, indent=1))
for p in plan: print(p["drafter"], p["words"], " ".join(p["files"]))
print(len(plan), "slices,", sum(p["words"] for p in plan), "words")
