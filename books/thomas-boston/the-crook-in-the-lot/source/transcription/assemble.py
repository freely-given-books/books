"""Assemble ABBYY paragraph records (abbyy_dump.py) into running paragraphs.

usage: assemble.py IN.jsonl PAGES.json OUT.json

Drops running heads and signature marks, joins paragraphs split by a page
break, mends line-end hyphens, and keeps italics as <i>...</i>.  Each
paragraph keeps the printed page(s) it sits on.  Hyphen decisions that a
dictionary could not settle are listed in OUT.hyphens.txt.
"""
import json, re, sys
from collections import Counter
from spellchecker import SpellChecker

src, pages_json, out = sys.argv[1:4]
leaf_page = {p['leafNum']: p['pageNumber'] for p in json.load(open(pages_json))['pages']}
spell = SpellChecker()

recs = [json.loads(l) for l in open(src)]

HEAD = re.compile(r'^\s*([\dG][\d\-]*\s+)?T\S{1,3}\s+C\S{2,5}K\s+\S{1,3}\s+T\S{1,3}\s+L\S{2}\S?(\s+\d+)?\s*$', re.I)
SIG = re.compile(r"^\s*([VY]\S[lL]\.\s*\S{2,4}\s*)?\d\s*[a-zA-Z]{1,2}\s*\d?\s*$")


def text_of(rec):
    return ' '.join(''.join(r[0] for r in ln['runs']) for ln in rec['lines'])


def is_noise(rec):
    t = text_of(rec)
    if HEAD.match(t) or SIG.match(t):
        return True
    if t.strip() in ('TO THE READER.*', 'THE CROOK IN THE LOT.'):
        return False
    return False


# runs of (text, italic) per line, lines per paragraph
paras = []
prev_leaf = None
for rec in recs:
    t = text_of(rec)
    if is_noise(rec):
        continue
    if t.lstrip().startswith(('•', '*')) and rec['fs'] < 8:   # McMillan's note
        continue
    leaf = rec['leaf']
    first_on_page = leaf != prev_leaf
    prev_leaf = leaf
    lines = [[(r[0], r[1]) for r in ln['runs']] for ln in rec['lines']
             if not (HEAD.match(''.join(r[0] for r in ln['runs'])) or SIG.match(''.join(r[0] for r in ln['runs'])))]
    if not lines:
        continue
    indented = 'startIndent' in rec['attrs'] and int(rec['attrs']['startIndent']) > 30
    centered = rec['attrs'].get('align') == 'Center'
    page = leaf_page.get(leaf, f'leaf{leaf}')
    if first_on_page and paras and not indented and not centered and not paras[-1]['centered']:
        # continuation of the paragraph broken by the page
        paras[-1]['lines'].extend(lines)
        paras[-1]['pages'].append(page)
        paras[-1]['breaks'].append(len(paras[-1]['lines']) - len(lines))
        continue
    paras.append({'pages': [page], 'leaf': leaf, 'lines': lines, 'breaks': [],
                  'centered': centered, 'fs': rec['fs']})

# words, to decide hyphens
allwords = Counter()
for p in paras:
    for ln in p['lines']:
        for w in re.findall(r"[A-Za-z][A-Za-z'\-]*[A-Za-z]", ''.join(t for t, _ in ln)):
            allwords[w.lower()] += 1

hyph_log = []


def join_hyphen(left, right):
    """left ends with '-', right is the start of the next line: keep the hyphen?"""
    a = re.search(r"([A-Za-z]+)-$", left)
    b = re.match(r"([A-Za-z]+)", right)
    if not a or not b:
        return True
    a, b = a.group(1), b.group(1)
    joined = (a + b).lower()
    hyph = f'{a}-{b}'.lower()
    if allwords[hyph] > 0 and allwords[joined] == 0:
        return True
    if allwords[joined] > 0 or spell.known([joined]):
        return False
    if spell.known([a.lower()]) and spell.known([b.lower()]) and len(a) > 2 and len(b) > 2:
        hyph_log.append(f'kept {a}-{b}')
        return True
    hyph_log.append(f'joined {a}{b}')
    return False


def render(p):
    """Join lines into one string with <i> markup."""
    runs = []
    for i, ln in enumerate(p['lines']):
        ln = [list(r) for r in ln if r[0]]
        if not ln:
            continue
        if runs:
            prev = runs[-1]
            if prev[0].endswith('-') and not prev[0].endswith('--') and ln[0][0][:1].islower():
                if not join_hyphen(prev[0], ln[0][0]):
                    prev[0] = prev[0][:-1]
            elif prev[0].endswith('-') and ln[0][0][:1].isupper():
                pass
            else:
                prev[0] = prev[0] + ' '
        runs.extend(ln)
    out = []
    for t, it in runs:
        if it and t.strip():
            lead = t[:len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            out.append(f'{lead}<i>{t.strip()}</i>{trail}')
        else:
            out.append(t)
    s = ''.join(out)
    s = re.sub(r'</i>(\s*)<i>', r'\1', s)
    s = re.sub(r'[ \t]+', ' ', s).strip()
    return s


result = []
for p in paras:
    pbs = []
    for page, k in zip(p['pages'][1:], p['breaks']):
        first = ''.join(t for t, _ in p['lines'][k])
        prev = ''.join(t for t, _ in p['lines'][k - 1]) if k else ''
        pbs.append({'n': page, 'before': prev[-40:], 'after': first[:40]})
    result.append({'pages': p['pages'], 'centered': p['centered'], 'fs': p['fs'], 'text': render(p), 'pb': pbs})
json.dump(result, open(out, 'w'), indent=0, ensure_ascii=False)
open(out + '.hyphens.txt', 'w').write('\n'.join(hyph_log) + '\n')
print(len(result), 'paragraphs;', len(hyph_log), 'hyphen guesses')
