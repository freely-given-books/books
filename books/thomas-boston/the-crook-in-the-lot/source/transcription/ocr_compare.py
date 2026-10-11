"""Align two OCRs of the same printing and flag doubtful words.

usage: ocr_compare.py P.json G.json CCEL.thml.xml OUT.jsonl

P is the primary OCR (assemble.py output), G the second scan.  Each flag:
{i: token index in P, page, p: P's word, g: G's word, c: CCEL's word,
 ctx: words around it, kind}.  CCEL (a modernized text) is aligned too, as
a third, weaker voice.
"""
import json, re, sys
from difflib import SequenceMatcher
from lxml import etree
from spellchecker import SpellChecker

P, G, C, out = sys.argv[1:5]
spell = SpellChecker()
spell.word_frequency.load_words(['thou', 'thee', 'thy', 'thine', 'hath', 'doth', 'hast', 'dost',
    'shew', 'shewed', 'shewn', 'shews', 'ye', 'wilt', 'shalt', 'canst', 'wouldst', 'shouldst',
    'couldst', 'art', 'viz', 'ver', 'saith', 'seest', 'findest', 'lookest', 'turnest', 'eying',
    'thereof', 'therein', 'whereof', 'wherein', 'howbeit', 'dehorts', 'unto', 'amongst', 'ay',
    'thereby', 'reproveable', 'meet', 'withal', 'mayest', 'knowest', 'lest'])

TOK = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’]*|[^\sA-Za-z0-9]")


def words(paras):
    toks = []
    for pi, p in enumerate(paras):
        text = re.sub(r'</?i>', '', p['text'])
        for m in TOK.finditer(text):
            toks.append((m.group(0), pi, p['pages'][0]))
    return toks


pt = words(json.load(open(P)))
gt = words(json.load(open(G)))

# CCEL text
root = etree.parse(C, etree.XMLParser(load_dtd=False, resolve_entities=False, no_network=True)).getroot()
body = root.find('.//ThML.body')
ctext = ' '.join(body.itertext())
ct = [(m.group(0), 0, '') for m in TOK.finditer(ctext)]


def norm(w):
    return w.lower().replace('’', "'")


def align(a, b):
    sm = SequenceMatcher(None, [norm(x[0]) for x in a], [norm(x[0]) for x in b], autojunk=False)
    m = {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(i2 - i1):
                m[i1 + k] = ('=', b[j1 + k][0])
        elif op == 'replace':
            seg = ' '.join(x[0] for x in b[j1:j2])
            for k in range(i1, i2):
                m[k] = ('~', seg if i2 - i1 > 1 else seg)
        elif op == 'delete':
            for k in range(i1, i2):
                m[k] = ('-', '')
    return m


# align in chunks to keep SequenceMatcher fast: by paragraph windows on P
def chunked_align(a, b, size=400):
    """Greedy: align successive windows of a against a slightly larger window of b."""
    result = {}
    j = 0
    for start in range(0, len(a), size):
        aw = a[start:start + size]
        bw = b[j:j + int(size * 1.6) + 50]
        sm = SequenceMatcher(None, [norm(x[0]) for x in aw], [norm(x[0]) for x in bw], autojunk=False)
        last_b = 0
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                for k in range(i2 - i1):
                    result[start + i1 + k] = ('=', bw[j1 + k][0])
                last_b = j2
            elif op == 'replace':
                seg = ' '.join(x[0] for x in bw[j1:j2])
                for k in range(i1, i2):
                    result[start + k] = ('~', seg)
                last_b = j2
            elif op == 'delete':
                for k in range(i1, i2):
                    result[start + k] = ('-', '')
        j += last_b
    return result


def full_align(a, b):
    try:
        from cydifflib import SequenceMatcher as SM
    except ImportError:
        SM = SequenceMatcher
    sm = SM(None, [norm(x[0]) for x in a], [norm(x[0]) for x in b], autojunk=False)
    result = {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(i2 - i1):
                result[i1 + k] = ('=', b[j1 + k][0])
        elif op == 'replace':
            seg = ' '.join(x[0] for x in b[j1:j2]) if j2 - j1 <= 4 else '…'
            for k in range(i1, i2):
                result[k] = ('~', seg)
        elif op == 'delete':
            for k in range(i1, i2):
                result[k] = ('-', '')
    return result


mg = full_align(pt, gt)
mc = full_align(pt, ct)

CONF = str.maketrans({'b': 'h', 'y': 'v', 'u': 'n', 'c': 'e'})


def known(w):
    w = norm(w).strip("'")
    return (not w.isalpha()) or bool(spell.known([w])) or w in ('i',)


flags = []
for i, (w, pi, page) in enumerate(pt):
    g = mg.get(i, ('-', ''))
    c = mc.get(i, ('-', ''))
    kind = None
    if w.isalpha() or "'" in w:
        gw = g[1]
        gconf = gw and ' ' not in gw and norm(gw).translate(CONF) == norm(w).translate(CONF)
        if not known(w):
            kind = 'unknown' if g[0] != '=' else None
        elif g[0] == '=' or gconf:
            if norm(w) in ('he', 'be') and c[0] != '=' and norm(c[1]) in ('he', 'be'):
                kind = 'hebe'
        elif gw and known(gw) and ' ' not in gw:
            kind = 'differs'
        elif c[0] != '=' and g[0] != '-':
            kind = 'weak'
    elif not w.isalnum():
        if g[0] != '=' and c[0] != '=':
            kind = 'punct'
    elif w.isdigit() and g[0] != '=':
        kind = 'digit'
    if kind:
        ctx = ' '.join(x[0] for x in pt[max(0, i - 6):i]) + ' [' + w + '] ' + ' '.join(x[0] for x in pt[i + 1:i + 7])
        flags.append({'i': i, 'para': pi, 'page': page, 'kind': kind, 'p': w, 'g': g[1], 'c': c[1], 'ctx': ctx})

with open(out, 'w') as f:
    for fl in flags:
        f.write(json.dumps(fl, ensure_ascii=False) + '\n')
from collections import Counter
print(len(pt), 'tokens;', Counter(f['kind'] for f in flags))
