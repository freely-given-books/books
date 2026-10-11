"""Global OCR cleanups that are safe in this book, with counts.

usage: clean.py IN.json OUT.json
"""
import json, re, sys
from collections import Counter

src, out = sys.argv[1:3]
paras = json.load(open(src))
RULES = [
    # running heads / signatures caught inside a paragraph
    (r'\s*\b(5\d\d|6\d\d)\s+TH\S\s+C\S{3,5}\s+\S{2,3}\s+TH\S\s+LOT\.?\s*', ' '),
    (r'\s*TH\S\s+C\S{3,5}\s+I\S{1,2}\s*"?\s+TH\S\s+LOT\.\s*\d\S{1,2}\s*', ' '),
    # book abbreviations the OCR misreads
    (r'\bFsal\b', 'Psal'), (r'\bPsah\b', 'Psal.'), (r'\bPaoJL\b', 'Psal.'),
    (r'\b1 Sara\b', '1 Sam'), (r'\b2 Sara\b', '2 Sam'), (r'\bLara\.', 'Lam.'),
    (r'\bGren\.', 'Gen.'), (r'\bHeh\.', 'Heb.'),
    # &c.
    (r'(?<![A-Za-z])[S83^6&]\s?fc\b\.?', '&c.'),
    # O (vocative) read as zero
    (r'(?<![\d.,])\b0(?=\s*[!,]|\s+[A-Za-z])', 'O'),
    # w read as Av / iv / lu at word start (only where the result is a word)
    (r'\bAv(?=[a-z])', 'w'), (r'\bAV(?=[a-z])', 'W'),
    (r'\biv(?=(ho|hi|ha|he|ill|ith|ay|as|ere|ise|ord|ork|ell|e\b|orld|rath))', 'w'),
    (r'\bTT(?=hen)', 'W'), (r'\bWT(?=hat)', 'Wh'),
    (r'\bGrod', 'God'),
    (r'\btlie\b', 'the'), (r'\btliis\b', 'this'), (r'\btliese\b', 'these'), (r'\bliis\b', 'his'),
    (r'\bliim\b', 'him'), (r'\baud\b', 'and'),
    # stray marks
    (r'\s*[\^■•]\s*', ' '),
    (r'\s+([,.;:?!])', r'\1'),
    (r'  +', ' '),
]
counts = Counter()
for p in paras:
    t = p['text']
    for pat, rep in RULES:
        t, n = re.subn(pat, rep, t)
        counts[pat] += n
    p['text'] = t.strip()
json.dump(paras, open(out, 'w'), indent=0, ensure_ascii=False)
for pat, rep in RULES:
    print(f'{counts[pat]:4}  {pat}  ->  {rep}')
