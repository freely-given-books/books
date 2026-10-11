"""Dump ABBYY pages to JSON lines: one record per par.
usage: abbyy_dump.py FILE.gz FIRST LAST OUT.jsonl"""
import gzip, sys, json
from lxml import etree
f, first, last, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
w = open(out, 'w')
for i, (ev, page) in enumerate(etree.iterparse(gzip.open(f), tag='{*}page')):
    if first <= i <= last:
        for bi, b in enumerate(page.iter('{*}block')):
            if b.get('blockType') != 'Text':
                continue
            for p in b.iter('{*}par'):
                lines = []
                sizes = []
                for line in p.iter('{*}line'):
                    out_l = []
                    for fm in line.iter('{*}formatting'):
                        t = ''.join(c.text or '' for c in fm.iter('{*}charParams'))
                        if fm.get('fs'):
                            sizes.append((float(fm.get('fs')), len(t)))
                        it = fm.get('italic') in ('1', 'true')
                        sc = fm.get('smallcaps') in ('1', 'true')
                        out_l.append([t, it, sc])
                    lines.append({'b': int(line.get('b')), 'l': int(line.get('l')), 'r': int(line.get('r')), 'runs': out_l})
                if not lines:
                    continue
                n = sum(k for _, k in sizes) or 1
                fs = sum(s * k for s, k in sizes) / n
                w.write(json.dumps({'leaf': i, 'block': bi, 'attrs': dict(p.attrib), 'fs': round(fs, 1), 'lines': lines}) + '\n')
    page.clear()
    if i > last:
        break
