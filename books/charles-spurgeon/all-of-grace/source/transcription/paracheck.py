# paragraph breaks: ours against CCEL's (which follows the print closely but not always)
import re, sys
from difflib import SequenceMatcher
from pathlib import Path
def stream(xml, para_re):
    words, starts = [], set()
    for m in re.finditer(para_re, xml, re.S):
        w = re.findall(r"[a-z]+", re.sub(r"<[^>]+>", " ", m.group(1)).lower().replace("’", "").replace("'", ""))
        if w: starts.add(len(words)); words += w
    return words, starts
ours = open(sys.argv[1]).read(); ours = ours[ours.index('id="ch1"'):]
ccel = Path.home().joinpath("Projects/fgbooks/books/books/charles-spurgeon/all-of-grace/source/grace.ccel.witness.xml").read_text()
ccel = ccel[ccel.index('<div1 title="To You"'):]
ow, os_ = stream(ours, r"<p[^>]*>(.*?)</p>"); cw, cs = stream(ccel, r"<p[^>]*>(.*?)</p>")
sm = SequenceMatcher(None, ow, cw, autojunk=False)
o2c = {a + k: b + k for a, b, n in sm.get_matching_blocks() for k in range(n)}
c2o = {v: k for k, v in o2c.items()}
near = lambda s, x: any(x + d in s for d in range(-3, 4))
print(f"ours {len(os_)}, CCEL {len(cs)}")
for i in sorted(os_):
    if i in o2c and not near(cs, o2c[i]): print("OURS-ONLY  …", " ".join(ow[i-6:i]), "¶", " ".join(ow[i:i+6]))
for j in sorted(cs):
    if j in c2o and not near(os_, c2o[j]): k = c2o[j]; print("CCEL-ONLY  …", " ".join(ow[k-6:k]), "¶", " ".join(ow[k:k+6]))
