"""where.py CH REGEX [width] : show exact text around matches in book-2-chapter-CH.typ (or 'argument')."""
import sys, re
ED = "/home/courtney/Projects/fgbooks/books/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-2"
ch = sys.argv[1]
fn = "book-2-argument" if ch.startswith("a") else f"book-2-chapter-{int(ch):02d}"
src = open(f"{ED}/{fn}.typ", encoding="utf-8").read()
w = int(sys.argv[3]) if len(sys.argv) > 3 else 70
for m in re.finditer(sys.argv[2], src):
    print(repr(src[max(0, m.start() - w):m.end() + w]))
    print("---")
