"""Count footnotes per page: 1845 (note-start lines in the Kraken text) vs CCEL (#footnote per chapter, mapped to pages by alignment).
Usage: python3 -I notecount.py"""
import re, pathlib, json, collections
K = pathlib.Path("/home/courtney/Projects/fgbooks/work/institutes/vol3/kraken")
T = pathlib.Path("/home/courtney/Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-6")
# chapter starts in 1845
starts = {}
for p in range(303, 559):
    t = (K / f"p-{p:04d}.txt").read_text()
    m = re.search(r"^CHAPTER ([XVILC]+?)\.", t, re.M)
    if m: starts[p] = m.group(1)
print(starts)
ROM = {"XIV":14,"XV":15,"XVI":16,"XVII":17,"XVIII":18,"XIX":19,"XX":20}
cnt = collections.Counter(); pages = collections.defaultdict(list)
ch = 0
for p in range(303, 559):
    if p in starts and starts[p] in ROM: ch = ROM[starts[p]]
    for ln in (K / f"p-{p:04d}.txt").read_text().splitlines():
        if re.match(r"^(\d|[¹²³])\s?(See|French|Latin|The|This|In|It|Heb|Rom|Matth|Isa|Ps|Gen|Exod|Deut|Job|Jer|Ezek|John|Luke|Mark|Acts|Eph|Gal|Col|Phil|Tit|Tim|Cor|Thess|Pet|James|Jam|Prov|Eccl|Dan|Hos|Calv|Aug|Ambr|Chrys|Bern|Greg|Lomb|Sent|August|On|Here|Some|For|Calvin|Instead|[A-Z])", ln.strip()) and not re.match(r"^\d+\.\s", ln.strip()):
            cnt[ch] += 1; pages[ch].append(p - 4)
for n in range(14, 21):
    c = (T / f"book-4-chapter-{n:02d}.typ").read_text().count("#footnote[")
    print(n, "CCEL", c, "1845~", cnt[n], "" if c == cnt[n] else "<<", pages[n] if c != cnt[n] else "")

import sys
if len(sys.argv) > 1:
    for n in map(int, sys.argv[1:]):
        print(f"===== ch {n}")
        lo = [p for p, r in starts.items() if ROM.get(r) == n][0]
        hi = min([p for p, r in starts.items() if ROM.get(r) == n + 1] or [559])
        for p in range(lo, hi + 1):
            for ln in (K / f"p-{p:04d}.txt").read_text().splitlines():
                s = ln.strip()
                if re.match(r"^(\d{1,2}|[¹²³])\s?[A-Z“\"]", s) and not re.match(r"^\d+\.\s", s) and not re.match(r"^\d{3}$", s):
                    print(f"  1845 {p-4}: {s[:110]}")
        src = (T / f"book-4-chapter-{n:02d}.typ").read_text()
        for m in re.finditer(r"#footnote\[", src):
            print("  CCEL:", src[m.end():m.end()+100].replace("\n", " "))
