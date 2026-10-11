"""Index ABBYY lines with coordinates per leaf.  usage: line_index.py FILE.gz FIRST LAST OUT.json"""
import gzip, sys, json
from lxml import etree
f, first, last, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
res = {}
for i, (ev, page) in enumerate(etree.iterparse(gzip.open(f), tag='{*}page')):
    if first <= i <= last:
        lines = []
        for ln in page.iter('{*}line'):
            t = ''.join(c.text or '' for c in ln.iter('{*}charParams'))
            lines.append({k: int(ln.get(k)) for k in 'ltrb'} | {'text': t})
        res[i] = {'w': int(page.get('width')), 'h': int(page.get('height')), 'lines': lines}
    page.clear()
    if i > last:
        break
json.dump(res, open(out, 'w'))
