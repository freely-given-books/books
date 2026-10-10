"""Apply proofread fixes (JSON lines) to Precious Remedies' chapters/typ.

python3 apply.py g1.jsonl [g2.jsonl ...]            # dry run: report
python3 apply.py --apply g1.jsonl ...               # apply class "fix"
python3 apply.py --apply --also asks-ok.jsonl ...   # (asks accepted later)

Only entries whose class is "fix" (or every entry of a file given after
--also) are applied; each `old` must occur exactly once in its file.
"""
import json
import sys
from collections import Counter
from pathlib import Path

CH = Path("/home/courtney/Projects/fgbooks/books/books/thomas-brooks/"
          "precious-remedies-against-satans-devices/chapters/typ")


def load(path, force=False):
    out = []
    for n, line in enumerate(Path(path).read_text().splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError as err:
            print(f"{path}:{n}: bad JSON ({err})")
            continue
        e["_src"] = f"{Path(path).name}:{n}"
        if force:
            e["class"] = "fix"
        out.append(e)
    return out


def main(argv):
    apply = "--apply" in argv
    args = [a for a in argv if a != "--apply"]
    entries, force = [], False
    for a in args:
        if a == "--also":
            force = True
            continue
        entries += load(a, force)
    fixes = [e for e in entries if e.get("class") == "fix" and e.get("old")]
    kinds = Counter((e.get("class"), e.get("kind")) for e in entries)
    texts, bad = {}, []
    for e in fixes:
        f = CH / e["file"]
        if f not in texts:
            texts[f] = f.read_text()
        n = texts[f].count(e["old"])
        if n != 1:
            bad.append((e, n))
            continue
        texts[f] = texts[f].replace(e["old"], e["new"], 1)
    for e, n in bad:
        print(f"SKIP {e['_src']} {e['file']}: old found {n}x: {e['old']!r}")
    print(f"{len(fixes) - len(bad)} fixes applicable, {len(bad)} skipped")
    for (c, k), n in sorted(kinds.items(), key=lambda x: (str(x[0][0]), str(x[0][1]))):
        print(f"  {c:5} {k}: {n}")
    if apply:
        for f, t in texts.items():
            f.write_text(t)
        print("applied")


if __name__ == "__main__":
    main(sys.argv[1:])
