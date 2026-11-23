"""Scaffold a book's Modern English edition files (as A Divine Cordial's):
python3 scaffold.py BOOK_DIR SLUG EPIGRAPH_CLASSIC_RE EPIGRAPH_MODERN
cover.typ becomes a function cover(edition:) called at the end; cover-modern.typ labels it;
<slug>-modern.typ and ebook-front-modern.html from the Classic ones; editorial.py's EPUB and
PRINT gain the modern edition. Prints what it changed; asserts every anchor."""
import re, sys
from pathlib import Path

B, slug, ep_old, ep_new = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
NOTE_TYP = ('#v(2em)\n      #text(size: 8pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own \\ '
            'Bible where his argument rests on its wording; capitals for God in quotations \\ (He, His) follow the BSB. '
            '“You#super[+]” marks every plural “you” (the older “ye”); a plain “you” is singular or general.]')
NOTE_HTML = ('<p class="note">Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his '
             'argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You<sup>+</sup>” marks every plural '
             '“you” (the older “ye”); a plain “you” is singular or general.</p>')

c = (B / "cover.typ").read_text()
assert c.count("\n#plate-cover(") == 1
c = c.replace("\n#plate-cover(", "\n// edition: the Modern English edition's label (cover-modern.typ)\n"
              "#let cover(edition: none) = plate-cover(\n  edition: edition,", 1).rstrip() + "\n\n#cover()\n"
(B / "cover.typ").write_text(c)
(B / "cover-modern.typ").write_text(
    "// The Modern English edition's cover: the Classic cover (cover.typ), labelled\n"
    "// (MODERN-ENGLISH-RULES.md: same art and colours, a small label and a spine mark).\n"
    '#import "cover.typ": cover\n#cover(edition: [Modern English])\n')

p = (B / f"{slug}.typ").read_text()
m = p.replace("chapters/typ/", "chapters/modern/")
m = re.sub(r"(\n  title: \[[^\]]*\],)", r'\1\n  subtitle: [#text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],', m, count=1)
assert "MODERN ENGLISH" in m
n = len(re.findall(ep_old, m, flags=re.S))
assert n == 1, ("epigraph", n)
m = re.sub(ep_old, lambda _: ep_new + "\n\n      " + NOTE_TYP, m, flags=re.S)
m = ("// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as " + slug + ".typ,\n"
     "// its text from chapters/modern, paragraph for paragraph with chapters/typ.\n" + m)
(B / f"{slug}-modern.typ").write_text(m)

f = (B / "ebook-front.html").read_text()
f = re.sub(r'(<p class="title">[^<]*</p>)', r'\1\n<p class="subtitle">Modern English</p>', f, count=1)
f = f.replace("</section>", NOTE_HTML + "\n</section>")
(B / "ebook-front-modern.html").write_text(f)

e = (B / "source/editorial.py").read_text()
e2 = re.sub(r'(EPUB = \{.*?)(\})\n', lambda mm: mm.group(1) + ',\n        "modern": {"chapters": "chapters/modern", '
            f'"file": "{slug}-modern.epub",\n                   "cover": "cover-modern.typ", "front": "ebook-front-modern.html"}}'
            + mm.group(2) + "\n", e, count=1, flags=re.S)
e2 = e2.replace(f'PRINT = ["{slug}.typ"]', f'PRINT = ["{slug}.typ", "{slug}-modern.typ"]')
assert e2 != e and f'"{slug}-modern.typ"' in e2
(B / "source/editorial.py").write_text(e2)
print("scaffolded", B.name)
