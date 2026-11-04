# The 1688 italics into the reading text (the editor's rule, 2026-11-01: the print's italics are
# kept). The automatic reading text of the 1688 TEI (build/typ, no review) has them as #emph;
# its words are aligned with the review's (build/review) in modern spelling and each run of
# italic words is wrapped in #emph[...] there, never across a paragraph, a heading or markup.
#   transfer_italics.py AUTO_DIR REVIEW_DIR
import re, sys
from difflib import SequenceMatcher
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from foundation import modern

WORD = re.compile(r"(#\w+(?:\([^)]*\))?\[)|(\])|([A-Za-z’']+)")


def key(w):
    return modern(re.sub(r"['’]", "", w.lower()))


def tokens(text):
    """[(start, end, word, italic?)] for the words outside headings"""
    out, stack = [], []
    for m in WORD.finditer(text):
        if m.group(1):
            stack.append(re.match(r"#(\w+)", m.group(1))[1]); continue
        if m.group(2):
            if stack: stack.pop()
            continue
        ls = text.rfind("\n", 0, m.start()) + 1
        if text.startswith("=", ls): continue
        w, end = m.group(3), m.end()
        while w and w[-1] in "’'":               # a closing quote is not part of the word
            w, end = w[:-1], end - 1
        if w: out.append((m.start(), end, w, "emph" in stack))
    return out


def transfer(auto, review):
    at, rt = tokens(auto), tokens(review)
    sm = SequenceMatcher(None, [key(t[2]) for t in at], [key(t[2]) for t in rt], autojunk=False)
    flag = [False] * len(rt)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            flag[b + k] = at[a + k][3] and not rt[b + k][3]
    # short unmatched words between italic words follow them
    for i in range(1, len(rt) - 1):
        if not flag[i] and flag[i - 1] and flag[i + 1] and len(rt[i][2]) <= 4 and not rt[i][3]:
            flag[i] = True
    runs, i = [], 0
    while i < len(rt):
        if not flag[i]: i += 1; continue
        j = i
        while j + 1 < len(rt) and flag[j + 1] and not re.search(r"[\n#\]\[]", review[rt[j][1]:rt[j + 1][0]]):
            j += 1
        runs.append((rt[i][0], rt[j][1])); i = j + 1
    out = review
    for st, en in reversed(runs):
        # a run's own closing quote or stop stays outside; an opening quote before it stays outside
        out = out[:st] + "#emph[" + out[st:en] + "]" + out[en:]
    return out, len(runs), sum(flag)


def main(auto_dir, review_dir):
    for f in sorted(Path(review_dir).glob("*.typ")):
        auto = (Path(auto_dir) / f.name).read_text()
        new, runs, words = transfer(auto, f.read_text())
        f.write_text(new)
        print(f"{f.name}: {runs} italic runs, {words} words")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
