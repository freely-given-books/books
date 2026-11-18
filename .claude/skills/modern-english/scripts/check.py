"""Check a Modern English chapter against its Classic one, paragraph by paragraph:
python3 check.py BOOK_DIR [FILE ...]  (BOOK_DIR holds chapters/typ and chapters/modern; FILE may be
part-1/stage-01.typ: subfolders are searched). VERSE=1 in the environment: verse paragraphs (#stanza/#quote set
line by line) must be identical to the Classic (rules §1.5), and #speech[#smallcaps[Name]: speakers must match.
Reports: paragraph counts; each paragraph's opening mark (I., 1., (1.), [1.], #smallcaps, ==, #block);
Scripture references and footnotes present in the Classic but missing in the Modern; length ratio
outside 0.75-1.5 (a sign of something dropped or added); archaic forms left (thou, hath, -eth)."""
import re, sys
from pathlib import Path

B = Path(sys.argv[1])
import os
VERSE = os.environ.get("VERSE") == "1"
files = sys.argv[2:] or sorted(str(p.relative_to(B / "chapters/modern")) for p in (B / "chapters/modern").rglob("*.typ"))
SPK = re.compile(r"^#speech\[#smallcaps\[[^\]]*\]:?")
REF = re.compile(r"\b(?:[1-3] )?[A-Z][a-z]+ \d+:\d+")
MARK = re.compile(r"^(=+ |#block|#smallcaps|\\?\[?\(?[0-9IVXL]+\\?\.\)?\]?|#emph\[(?:First|Secondly|Thirdly)|#pad)")
ARCH = re.compile(r"\b(thou|thee|thy|thine|ye|hath|doth|art|wilt|shalt|unto|[a-z]{2,}eth)\b")
OK_ETH = {"teeth", "beneath", "seventh", "eleventh", "twentieth", "death", "breath", "faith", "with", "doeth"}
bad = 0
for f in files:
    a = [p.strip() for p in re.split(r"\n\s*\n", (B / "chapters/typ" / f).read_text()) if p.strip()]
    mp = B / "chapters/modern" / f
    if not mp.exists():
        print(f"{f}: no modern file"); bad += 1; continue
    b = [p.strip() for p in re.split(r"\n\s*\n", mp.read_text()) if p.strip()]
    if len(a) != len(b):
        print(f"{f}: {len(a)} classic paragraphs, {len(b)} modern"); bad += 1
    for k, (x, y) in enumerate(zip(a, b), 1):
        mx, my = MARK.match(x), MARK.match(y)
        if (mx and mx.group(1)[:3]) != (my and my.group(1)[:3]):
            print(f"{f} ¶{k}: opening mark {mx and mx.group(1)!r} vs {my and my.group(1)!r}"); bad += 1
        if VERSE and re.match(r"#(stanza|quote)\[", x) and " \\\n" in x and x != y:
            print(f"{f} ¶{k}: verse changed (keep it as printed)"); bad += 1
        if VERSE and (SPK.match(x) and SPK.match(x).group()) != (SPK.match(y) and SPK.match(y).group()):
            print(f"{f} ¶{k}: speaker {SPK.match(x) and SPK.match(x).group()!r} vs {SPK.match(y) and SPK.match(y).group()!r}"); bad += 1
        miss = set(REF.findall(x)) - set(REF.findall(y))
        if miss:
            print(f"{f} ¶{k}: references missing {sorted(miss)}"); bad += 1
        if x.count("#footnote") != y.count("#footnote"):
            print(f"{f} ¶{k}: footnotes {x.count('#footnote')} vs {y.count('#footnote')}"); bad += 1
        wx, wy = len(x.split()), len(y.split())
        if wx > 25 and not 0.75 <= wy / wx <= 1.5:
            print(f"{f} ¶{k}: length {wx} -> {wy} words"); bad += 1
        isverse = VERSE and re.match(r"#(stanza|quote)\[", y) and " \\\n" in y
        arch = [] if isverse else [w for w in ARCH.findall(re.sub(r"“[^”]*”", "", y)) if w not in OK_ETH]
        if arch:
            print(f"{f} ¶{k}: old forms outside quotations {sorted(set(arch))}"); bad += 1
print(bad, "to look at")
