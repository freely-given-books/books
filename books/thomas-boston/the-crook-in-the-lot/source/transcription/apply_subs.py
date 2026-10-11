"""Apply exact substring fixes to assembled paragraphs.

usage: apply_subs.py IN.json FIXES.jsonl OUT.json
Each fix: {"para": N (optional), "old": "...", "new": "..."}; "old" must occur
exactly once (in paragraph N if given, else in the whole text).  Reports any
that do not.
"""
import json, sys
paras = json.load(open(sys.argv[1]))
bad = 0
n = 0
for line in open(sys.argv[2]):
    if not line.strip():
        continue
    f = json.loads(line)
    old, new = f['old'], f['new']
    cands = [f['para']] if isinstance(f.get('para'), int) else range(len(paras))
    hits = [(i, paras[i]['text'].count(old)) for i in cands if old in paras[i]['text']]
    if len(hits) != 1 or hits[0][1] != 1:
        bad += 1
        print('NOT APPLIED', hits, json.dumps(f, ensure_ascii=False))
        continue
    i = hits[0][0]
    paras[i]['text'] = paras[i]['text'].replace(old, new)
    n += 1
json.dump(paras, open(sys.argv[3], 'w'), indent=0, ensure_ascii=False)
print(n, 'applied,', bad, 'not applied')
