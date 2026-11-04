# crops of the printed lines holding each phrase (first page where Kraken has it): cropwords.py OUT.png PHRASE...
import re, subprocess, sys
from pathlib import Path
from PIL import Image
B = str(Path.home()/"temp_codex/books/charles-spurgeon/all-of-grace/source/ocr-witnesses/spurgeon-all-of-grace-1886")
S = str(Path.home()/"Projects/fgbooks/local-tools/show.py")
pages = {int(f.stem[2:]): re.sub(r"[^a-z ]", "", re.sub(r"[-¬]\n", "", f.read_text().lower()).replace("\n", " ")) for f in Path("kraken").glob("p-*.txt")}
ims = []
for k, t in enumerate(sys.argv[2:]):
    words = re.sub(r"[^a-z ]", "", t.lower()).split()
    pg = next((n for n, x in sorted(pages.items()) if " ".join(words[:4]) in x), None) or \
         next((n for n, x in sorted(pages.items()) if " ".join(words[1:4]) in x), None)
    if pg is None: print("not found:", t); continue
    out = f"crops/cw-{k}.png"
    subprocess.run([sys.executable, S, B, str(pg), out] + t.split() + ["--lines", "3"], capture_output=True)
    ims.append(Image.open(out).convert("L")); print(k, pg, t)
w = max(i.width for i in ims); h = sum(i.height + 12 for i in ims)
o = Image.new("L", (w, h), 255); y = 0
for im in ims: o.paste(im, (0, y)); y += im.height + 12
o.thumbnail((900, 2600)); o.save(sys.argv[1])
