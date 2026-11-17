"""Reader assignments for the meaning audit: python3 assign.py PAIRS.jsonl OUT_DIR [--words 10000] [--pass B]
Cuts the book's paragraph pairs, in order, into runs of about --words Classic words and writes, per reader,
OUT_DIR/<pass><k>.md (the pairs to read) and OUT_DIR/<pass><k>.ids (file<TAB>n, for coverage.py).
Pass B starts half a run later than pass A, so every seam of one pass sits mid-run in the other and every
paragraph is read by two readers of different models (models.md)."""
import json, sys
from pathlib import Path
args = [a for a in sys.argv[1:] if not a.startswith("--")]
rows = [json.loads(l) for l in open(args[0])]
OUT = Path(args[1]); OUT.mkdir(parents=True, exist_ok=True)
W = int(sys.argv[sys.argv.index("--words") + 1]) if "--words" in sys.argv else 10000
P = sys.argv[sys.argv.index("--pass") + 1] if "--pass" in sys.argv else "A"
runs, cur, n, budget = [], [], 0, W // 2 if P == "B" else W
for r in rows:
    cur.append(r); n += len(r["classic"].split())
    if n >= budget: runs.append(cur); cur, n, budget = [], 0, W
if cur:
    if runs and n < W * 0.3: runs[-1] += cur
    else: runs.append(cur)
for k, run in enumerate(runs, 1):
    (OUT / f"{P}{k}.md").write_text("\n".join(f"## {r['file']} ¶{r['n']}\n\nCLASSIC:\n{r['classic']}\n\nMODERN:\n{r['modern']}\n" for r in run))
    (OUT / f"{P}{k}.ids").write_text("".join(f"{r['file']}\t{r['n']}\n" for r in run))
    print(f"{P}{k}: {run[0]['file']} ¶{run[0]['n']} – {run[-1]['file']} ¶{run[-1]['n']}, {sum(len(r['classic'].split()) for r in run)} words")
