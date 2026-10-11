"""Join paragraphs a page break split, in both the text and the page-break file.
usage: merge.py TEXT.json PB.json OUT_TEXT.json OUT_PB.json N [N ...]   (joins N with N+1)"""
import json, sys
t, pb = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
for n in sorted(map(int, sys.argv[5:]), reverse=True):
    for d in (t, pb):
        a, b = d[n], d.pop(n + 1)
        a['text'] = a['text'].rstrip() + ' ' + b['text'].lstrip()
        a['pb'] = a.get('pb', []) + [{'n': b['pages'][0], 'before': a['text'][:0], 'after': b['text'][:40]}] + b.get('pb', [])
        a['pages'] = a['pages'] + [p for p in b['pages'] if p not in a['pages']]
json.dump(t, open(sys.argv[3], 'w'), indent=0, ensure_ascii=False)
json.dump(pb, open(sys.argv[4], 'w'), indent=0, ensure_ascii=False)
