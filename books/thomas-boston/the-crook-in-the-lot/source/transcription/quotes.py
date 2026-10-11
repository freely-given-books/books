"""Close up the OCR's space after an opening quotation mark; list paragraphs
whose quotation marks don't pair.  usage: quotes.py IN.json OUT.json"""
import json, re, sys
t = json.load(open(sys.argv[1]))
n = 0
for i, p in enumerate(t):
    s, k = re.subn(r'(^|[\s—(\[])"\s+(?=(<i>)?[\w\'])', r'\1"', p['text'])
    n += k
    p['text'] = s
    plain = re.sub('</?i>', '', s)
    if plain.count('"') % 2:
        print(i, p['pages'][0], '|', re.sub(r'\s+', ' ', plain)[:0], *[plain[max(0, m.start() - 40):m.end() + 30] for m in re.finditer('"', plain)], sep='\n   ')
json.dump(t, open(sys.argv[2], 'w'), indent=0, ensure_ascii=False)
print(n, 'spaces closed up', file=sys.stderr)
