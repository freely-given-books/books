"""Apply a collation report's clear findings to chapters/typ; list the rest.
usage: apply_collation.py REPORT.jsonl CHAPTERS_DIR HELD.jsonl [--dry]"""
import json, sys, re
from pathlib import Path
report, chdir, held_path = sys.argv[1], Path(sys.argv[2]), sys.argv[3]
dry = "--dry" in sys.argv
APPLY = {"scripture", "wording", "slip", "omission", "reference"}
MISPRINT = re.compile(r"misprint", re.I)
rows = [json.loads(l) for l in open(report) if l.strip()]
rows = [r for r in rows if "kind" in r]
applied, held, failed = [], [], []
texts = {}
for r in rows:
    why = None
    if r["kind"] not in APPLY:
        why = r["kind"]
    elif r.get("confidence") != "high":
        why = "confidence " + r.get("confidence", "?")
    elif r["kind"] == "wording" and MISPRINT.search(r.get("note", "")):
        why = "1648 misprint?"
    if why:
        held.append({**r, "held": why}); continue
    f = chdir / r["file"]
    t = texts.setdefault(f, f.read_text())
    n = t.count(r["goold"])
    if n != 1:
        failed.append({**r, "held": f"found {n} times"}); continue
    texts[f] = t.replace(r["goold"], r["proposed"])
    applied.append(r)
if not dry:
    for f, t in texts.items():
        f.write_text(t)
with open(held_path, "w") as out:
    for r in held + failed:
        out.write(json.dumps(r, ensure_ascii=False) + "\n")
from collections import Counter
print("applied", len(applied), dict(Counter(r["kind"] for r in applied)))
print("held", len(held), dict(Counter(r["held"] for r in held)))
print("failed", len(failed))
for r in failed:
    print("  ", r["file"], r["goold"][:80], r["held"])
