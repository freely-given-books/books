# completeness: the ThML against foundation.json (nothing lost in assembly) and against each
# OCR witness (any run of 4+ words a witness has that ours lacks)
import json, re, sys
from difflib import SequenceMatcher
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from foundation import seq, strip_heads, pages_from_export, X, FIRST, LAST, W, key
thml = Path(sys.argv[1]).read_text()
body = thml[thml.index("<ThML.body>"):]
body = body[body.index('id="ch1"'):]
body = re.sub(r"<h2>.*?</h2>", " ", body)
ours = [k for k in seq(re.sub(r"<[^>]+>", " ", body).replace("&amp;", "&"))[0] if k[0].isalnum()]
found = [key(t["t"]) for t in json.loads((W / "foundation.json").read_text())]
found = [k for k in found if k[0].isalnum()]
sm = SequenceMatcher(None, found, ours, autojunk=False)
lost = [(found[i1:i2], ours[j1:j2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
print(f"assembly: {len(found)} words in, {len(ours)} out; differences: {lost[:20]}")
wits = {
 "glm": "\n".join(strip_heads(v) for k, v in sorted(pages_from_export(X / "glm/full-text.txt").items()) if FIRST <= k <= LAST),
 "tess": "\n".join(strip_heads(v) for k, v in sorted(pages_from_export(X / "tesseract/full-text.txt").items()) if FIRST <= k <= LAST),
 "djvu": (W / "1886.djvu.txt").read_text(),
}
for name, text in wits.items():
    w = [k for k in seq(text)[0] if k[0].isalnum()]
    sm = SequenceMatcher(None, ours, w, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ("insert", "replace") and (j2 - j1) - (i2 - i1) >= 4:
            print(f"{name}: has {' '.join(w[j1:j2])[:150]!r} where ours has {' '.join(ours[i1:i2])[:60]!r} (after: {' '.join(ours[max(0,i1-6):i1])})")
