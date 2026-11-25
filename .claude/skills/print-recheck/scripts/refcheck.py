"""Check that every reference left in residual.txt (OCR words unmatched by both passes) is present in the CCEL text
(Arabic form) of the chapter that page belongs to (per chapter, as vol. 5; vol. 6 = Book IV ch. 14-20, 1845 vol. 3).
Usage: python3 -I refcheck.py"""
import re, pathlib
T = pathlib.Path("/home/courtney/Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-6")
D = pathlib.Path(__file__).resolve().parent
# first printed page of each chapter in 1845 vol. 3 (0 = the Argument)
START = {14: 299, 15: 327, 16: 349, 17: 386, 18: 457, 19: 479, 20: 518}
def chap(p):
    return max(c for c, s in START.items() if s <= p)
TX = {c: (T / f"book-4-chapter-{c:02d}.typ").read_text() for c in START}
def roman(s):
    s = s.lower().replace("ï","i").replace("ü","ii").replace("î","i").replace("í","i").replace("n̈","ii").replace("ini","iii").replace("vin","vii")
    s = re.sub(r"^[l1]", "l", s)
    s = re.sub(r"^i(?=[xv])", "l", s) if len(s) > 2 else s
    v = {"i":1,"v":5,"x":10,"l":50,"c":100}
    if not s or any(c not in v for c in s): return None
    t=0
    for k,c in enumerate(s):
        t += -v[c] if k+1<len(s) and v[c]<v[s[k+1]] else v[c]
    return t
for l in (D/"residual.txt").read_text().splitlines():
    p, n, run = l.split("\t", 2)
    pn = int(p.split(".")[1])
    txt = TX[chap(pn)] + (TX.get(chap(pn) - 1, "") if pn - START[chap(pn)] < 2 else "")
    for m in re.finditer(r"\b([ivxlcIVXLCïün̈]+)\.\s*(\d+)", run):
        c = roman(m.group(1)); v = m.group(2)
        if c is None: continue
        if not re.search(rf"\b{c}:{v}\b|\b{c}:\d+[-–, ]+(\d+[-–, ]+)*{v}\b|\b{c}:{v}[-–]", txt):
            print(p, run[:120], "-> missing", f"{c}:{v}")
