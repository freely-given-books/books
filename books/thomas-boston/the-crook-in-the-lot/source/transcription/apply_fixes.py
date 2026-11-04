"""Apply token-span fixes (segments.py *.auto.jsonl) to assembled paragraphs.

usage: apply_fixes.py P.json AUTO.jsonl OUT.json

Token indices are those of segments.py (tag-stripped text, TOK regex, over all
paragraphs in order).  Italic tags are kept around the replaced span when
the span sits inside one italic run.
"""
import json, re, sys

P, A, out = sys.argv[1:4]
paras = json.load(open(P))
TOK = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’]*|[^\sA-Za-z0-9]")

# global token index -> (para, start, end) in the tagged text
index = []
for pi, p in enumerate(paras):
    t = p['text']
    stripped, omap = [], []
    k = 0
    while k < len(t):
        m = re.match(r'</?i>', t[k:])
        if m:
            k += len(m.group(0))
            continue
        stripped.append(t[k])
        omap.append(k)
        k += 1
    omap.append(len(t))
    s = ''.join(stripped)
    for m in TOK.finditer(s):
        index.append((pi, omap[m.start()], omap[m.end() - 1] + 1))

fixes = [json.loads(l) for l in open(A)]
by_para = {}
skipped = 0
for f in fixes:
    i1, i2 = f['i1'], f['i2']
    if i2 > i1:
        a, b = index[i1], index[i2 - 1]
        if a[0] != b[0]:
            skipped += 1
            continue
        by_para.setdefault(a[0], []).append((a[1], b[2], f['to']))
    else:                       # insertion before token i1
        a = index[i1]
        by_para.setdefault(a[0], []).append((a[1], a[1], f['to'] + ' '))
for pi, edits in by_para.items():
    t = paras[pi]['text']
    for s, e, new in sorted(edits, reverse=True):
        old = t[s:e]
        # keep italics balanced: drop tags inside the span, re-add if the span opened/closed one
        opens, closes = old.count('<i>'), old.count('</i>')
        inner = new
        if opens > closes:
            inner = new + '<i>'
        elif closes > opens:
            inner = '</i>' + new
        t = t[:s] + inner + t[e:]
    paras[pi]['text'] = t
json.dump(paras, open(out, 'w'), indent=0, ensure_ascii=False)
print(len(fixes) - skipped, 'applied,', skipped, 'skipped (span across paragraphs)')
