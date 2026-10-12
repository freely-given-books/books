"""Write calvin-vol2-1845.md from findings.jsonl (+ head.md, tail.md); check that every ccel string is in its file.

findings.jsonl lines: [file-stem, anchor, ccel, 1845, proposed, page, kind, confidence]
An anchor not starting with "note" or "§" gets "§N " prepended (section containing ccel).
"""
import json, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "calvin-vol2-1845.md")
ED = "/home/courtney/Projects/fgbooks/books/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-2"

TITLES = {"book-2-argument": "Book II, Argument (p. 280)"}
for i in range(1, 18):
    TITLES[f"book-2-chapter-{i:02d}"] = f"Book II, chapter {i:02d}"
ORDER = list(TITLES)
DONE = set(open(HERE + "/done.txt").read().split()) if os.path.exists(HERE + "/done.txt") else set()


def section_of(src, pos):
    sec = None
    for m in re.finditer(r"^(\d+)\\\. ", src, re.M):
        if m.start() > pos:
            break
        sec = m.group(1)
    return sec


F = []
problems = []
for ln in open(HERE + "/findings.jsonl", encoding="utf-8"):
    ln = ln.strip()
    if not ln or ln.startswith("#"):
        continue
    r = json.loads(ln)
    fn, anchor, ccel = r[0], r[1], r[2]
    src = open(f"{ED}/{fn}.typ", encoding="utf-8").read()
    n = src.count(ccel) if ccel else 0
    if r[6] != "b-note" and n == 0:
        problems.append(f"NOT FOUND {fn}: {ccel!r}")
    elif n > 1:
        problems.append(f"x{n} {fn}: {ccel!r}")
    if n and not anchor.startswith(("note", "§", "heading", "summary", "Sections")):
        sec = section_of(src, src.index(ccel))
        if sec:
            anchor = f"§{sec} {anchor}"
    r[1] = anchor
    F.append(r)

head = open(HERE + "/head.md", encoding="utf-8").read()
tail = open(HERE + "/tail.md", encoding="utf-8").read() if os.path.exists(HERE + "/tail.md") else ""


def esc(s):
    return str(s).replace("|", "\\|").replace("\n\n", " ¶ ")


out = [head]
for fn in ORDER:
    rows = [x for x in F if x[0] == fn]
    if fn not in DONE and not rows:
        continue
    out.append(f"## {TITLES[fn]} — `{fn}.typ`\n")
    if not rows:
        out.append("No differences beyond OCR noise.\n")
        continue
    out.append("| anchor | CCEL | 1845 | proposed | p. | kind | conf. |\n|---|---|---|---|---|---|---|")
    for r in rows:
        out.append("| " + " | ".join(esc(x) for x in r[1:]) + " |")
    out.append("")
out.append(tail)
out.append("## Findings as JSON lines\n\n```json")
for r in F:
    out.append(json.dumps(dict(file=r[0] + ".typ", anchor=r[1], ccel=r[2], **{"1845": r[3]}, proposed=r[4], page=r[5], kind=r[6], confidence=r[7]), ensure_ascii=False))
out.append("```\n")
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print(len(F), dict(collections.Counter(r[6] for r in F)))
print("\n".join(problems) or "all ccel strings found once")
