"""List words the dictionary does not know, with counts and an example.
usage: unknown.py IN.json"""
import json, re, sys
from collections import Counter, defaultdict
from spellchecker import SpellChecker
spell = SpellChecker()
EXTRA = set(open(__file__.replace('unknown.py', 'extra_words.txt')).read().split())
def known(w):
    w = w.lower().replace('’', "'").strip("'")
    if w.endswith("'s"): w = w[:-2]
    if re.fullmatch(r'[ivxlc]+', w): return True
    return w in EXTRA or bool(spell.known([w])) or (w.endswith(('eth', 'est')) and bool(spell.known([w[:-3], w[:-3] + 'e', w[:-2]])))
c, ex = Counter(), {}
for pi, p in enumerate(json.load(open(sys.argv[1]))):
    t = re.sub(r'</?i>', '', p['text'])
    for m in re.finditer(r"[A-Za-z][A-Za-z'’]*", t):
        w = m.group(0)
        if not known(w):
            c[w] += 1
            ex.setdefault(w, (p['pages'][0], t[max(0, m.start()-40):m.end()+30]))
for w, n in sorted(c.items(), key=lambda x: (-x[1], x[0])):
    print(n, w, ex[w][0], '|', ex[w][1].replace('\n', ' '))
