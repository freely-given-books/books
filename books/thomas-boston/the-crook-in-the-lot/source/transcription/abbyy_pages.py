"""Print ABBYY pages as text, italics marked _..._. usage: abbyy_pages.py FILE.gz FIRST LAST"""
import gzip, sys, re
from lxml import etree
f, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ns = None
for i, (ev, page) in enumerate(etree.iterparse(gzip.open(f), tag='{*}page')):
    if first <= i <= last:
        print(f'=== page {i}')
        for line in page.iter('{*}line'):
            out = []
            for fm in line.iter('{*}formatting'):
                t = ''.join(c.text or '' for c in fm.iter('{*}charParams'))
                if fm.get('italic') in ('1', 'true'):
                    t = '_' + t + '_'
                out.append(t)
            print(''.join(out))
    page.clear()
    if i > last: break
