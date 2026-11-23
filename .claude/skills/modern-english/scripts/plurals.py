"""Plural marks (rules §4.2, the editor 2026-11-19): EVERY plural you/your/yours/yourselves carries you⁺, not only
the first of its sentence. Lists, in every Modern paragraph that carries a you⁺, the you/your forms still unmarked,
numbered, with the Classic paragraph beside it, to be settled one by one: plural (ye, or you to a group) or singular
(thou, or a polite singular you; a speaker may turn from the group to one person mid-paragraph).
python3 plurals.py BOOK_DIR [--show] [--write]
  --show   print each paragraph (Classic, then Modern with the unmarked forms numbered ⟨n⟩)
  --write  mark every unmarked form in those paragraphs whose Classic has no singular thou/thee/thy. Only for a book
           whose plural-address paragraphs speak to the group throughout (Owen's or Brooks's readers); in a
           dialogue book (Bunyan) read --show and mark by hand (work/you-plus-2026-11-19/apply.py).
A ; ( or [ straight after #super[+] is swallowed by Typst: the script escapes a ; it creates (\\;)."""
import re, sys
from pathlib import Path
THOU = re.compile(r"\b(thou|thee|thy|thine|thyself)\b", re.I)
YOU = re.compile(r"\b([Yy]ou(?:rs|r|rselves)?)\b(?!#super)")
B = Path(sys.argv[1]) / "chapters"
total = 0
for mp in sorted((B / "modern").rglob("*.typ")):
    rel = mp.relative_to(B / "modern")
    cps = [p for p in re.split(r"\n\s*\n", (B / "typ" / rel).read_text()) if p.strip()]
    mps = re.split(r"(\n\s*\n)", mp.read_text())
    k, n = 0, 0
    for i in range(0, len(mps), 2):
        if not mps[i].strip(): continue
        c = cps[k]; k += 1
        if "#super[+]" not in mps[i] or not YOU.search(mps[i]): continue
        hits = len(YOU.findall(mps[i])); n += hits
        if "--show" in sys.argv:
            c_ = [0]
            def num(m):
                c_[0] += 1; return f"{m.group(1)}⟨{c_[0]}⟩"
            print(f"=== {rel} ¶{k}{'  (Classic has thou)' if THOU.search(c) else ''}\nC: {c}\nM: {YOU.sub(num, mps[i])}\n")
        if "--write" in sys.argv and not THOU.search(c):
            mps[i] = re.sub(r"#super\[\+\];", r"#super[+]\\;", YOU.sub(r"\1#super[+]", mps[i]))
    if n and "--write" in sys.argv: mp.write_text("".join(mps))
    if n: print(f"{rel}: {n} unmarked in plural-address paragraphs")
    total += n
print(total, "unmarked you/your in paragraphs carrying a you⁺", "(marked where the Classic has no thou)" if "--write" in sys.argv else "")
