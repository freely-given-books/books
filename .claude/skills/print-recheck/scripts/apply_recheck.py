"""Apply a Classic recheck (apply-input.jsonl + manual-edits.json) to chapters/typ.

    python3 apply_recheck.py VOL_DIR [--apply]

Each row of apply-input.jsonl names a file, a CCEL snippet ("ccel"), the 1845 reading of the
same words ("1845") and the replacement words ("proposed"). The word that differs between the
two snippets is replaced in the CCEL snippet by the proposed word, keeping the punctuation
around it; the snippet must occur exactly once in its file. Rows that change more than one word,
or whose snippet is not unique, are left for a hand edit and listed. A row whose snippet a
manual edit also touches is left to the manual edit. Then manual-edits.json ([file, old, new]
triples, each old exactly once) is applied. Dry run by default: prints every change.

(Written 2026-11-23 for vol. 3; used for vols 4, 5 and 6 with VOLDIR set to the volume.)
"""
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path.home() / "Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion"
VOLDIR = "vol-6"
CORE = re.compile(r"^(\W*)(.*?)(\W*)$", re.S)


def norm(w):
    return re.sub(r"\W", "", w).lower()


def edit_for(row):
    """(old, new) for a one-word row, or a reason it needs a hand edit."""
    a, b = row["ccel"].split(" "), row["1845"].split(" ")
    ops = [o for o in difflib.SequenceMatcher(a=[norm(w) for w in a], b=[norm(w) for w in b],
                                              autojunk=False).get_opcodes() if o[0] != "equal"]
    if row["ccel"] == row["1845"] or not ops:
        # a capital letter or punctuation only: compare exactly
        ops = [("replace", i, i + 1, i, i + 1) for i, (x, y) in enumerate(zip(a, b)) if x != y]
    if len(ops) != 1 or ops[0][0] != "replace" or ops[0][2] - ops[0][1] != 1:
        return None, f"{len(ops)} changes in the snippet"
    i = ops[0][1]
    pre, _, post = CORE.match(a[i]).groups()
    words = a[:i] + [pre + row["proposed"] + post] + a[i + 1:]
    return row["ccel"], " ".join(words)


def main(argv):
    vol, apply = Path(argv[1]), "--apply" in argv
    rows = [json.loads(l) for l in (vol / "recheck/apply-input.jsonl").read_text().splitlines() if l.strip()]
    manual = json.loads((vol / "recheck/manual-edits.json").read_text())
    texts, by_hand, done = {}, [], 0
    files = sorted({r["file"] for r in rows} | {m[0] for m in manual})
    for f in files:
        texts[f] = (ROOT / "chapters/typ" / VOLDIR / f).read_text(encoding="utf-8") \
            if (ROOT / "chapters/typ" / VOLDIR / f).exists() else (ROOT / f).read_text(encoding="utf-8")
    for r in rows:
        if any(m[0] == r["file"] and (r["ccel"] in m[1] or m[1] in r["ccel"]) for m in manual):
            print(f"  (left to a manual edit) {r['file']}: {r['ccel']}")
            continue
        old, new = edit_for(r)
        if old is None:
            by_hand.append((r, new))
            continue
        n = texts[r["file"]].count(old)
        if n != 1:
            by_hand.append((r, f"snippet occurs {n} times"))
            continue
        texts[r["file"]] = texts[r["file"]].replace(old, new)
        done += 1
        print(f"{r['file']} [{r['kind']}] {old!r} -> {new!r}")
    for f, old, new in manual:
        n = texts[f].count(old)
        if n != 1:
            by_hand.append(({"file": f, "ccel": old}, f"manual edit: old occurs {n} times"))
            continue
        texts[f] = texts[f].replace(old, new)
        done += 1
        print(f"{f} [manual] {old!r} -> {new!r}")
    print(f"\n{done} applied{'' if apply else ' (dry run)'}; {len(by_hand)} by hand:")
    for r, why in by_hand:
        print(f"  {r['file']}: {r['ccel']!r} -> {r.get('1845')!r} ({why})")
    if apply:
        for f, t in texts.items():
            p = ROOT / "chapters/typ" / VOLDIR / f
            (p if p.exists() else ROOT / f).write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv)
