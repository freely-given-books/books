"""Compare two OCRs of one printing segment by segment; resolve what rules can.

usage: segments.py P.json G.json CCEL.thml.xml OUT_PREFIX

Writes OUT_PREFIX.auto.jsonl (resolved: P segment -> chosen text, with the
rule) and OUT_PREFIX.review.jsonl (left for a reader with the page image).
Each record: {id, para, page, p, g, c, ctx_before, ctx_after}.
Tokens are words or single punctuation marks; text is compared without
italics (the italics come from P).
"""
import json, re, sys
from cydifflib import SequenceMatcher
from lxml import etree
from spellchecker import SpellChecker

P, G, C, outp = sys.argv[1:5]
spell = SpellChecker()
EXTRA = set('''thou thee thy thine hath doth hast dost shew shewed shewn shews shewing ye wilt shalt canst
wouldst shouldst couldst art viz ver saith seest findest lookest turnest eying thereof therein whereof
wherein howbeit dehorts unto amongst ay thereby reproveable meet withal mayest knowest lest hereby
thereto whereby wherewith herein hitherto heretofore cometh goeth giveth maketh taketh bringeth seemeth
pronounceth challengeth supposeth doeth saith speaketh loveth hateth sendeth worketh lieth'''.split())


def known(w):
    w = w.lower().replace('’', "'").strip("'")
    if not w or not re.search('[a-z]', w):
        return True
    if w.endswith("'s"):
        w = w[:-2]
    if re.fullmatch(r'[ivxlc]+', w):
        return True
    return w in EXTRA or bool(spell.known([w])) or (w.endswith(('eth', 'est')) and spell.known([w[:-3], w[:-3] + 'e']))


TOK = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’]*|[^\sA-Za-z0-9]")


def toks_of(paras):
    out = []
    for pi, p in enumerate(paras):
        for m in TOK.finditer(re.sub(r'</?i>', '', p['text'])):
            out.append((m.group(0), pi, p['pages'][0]))
    return out


pp = json.load(open(P))
pt = toks_of(pp)
gt = toks_of(json.load(open(G)))
root = etree.parse(C, etree.XMLParser(load_dtd=False, resolve_entities=False, no_network=True)).getroot()
ct = [(m.group(0), 0, '') for m in TOK.finditer(' '.join(root.find('.//ThML.body').itertext()))]

SKEL = [('rn', 'm'), ('b', 'h'), ('y', 'v'), ('u', 'n'), ('c', 'e'), ('li', 'h'), ('ii', 'u'),
        ('1', 'l'), ('i', 'l'), ('f', 't'), ('r', 'v')]


def skel(w):
    w = w.lower().replace('’', "'")
    for a, b in SKEL:
        w = w.replace(a, b)
    return w


def ops(a, b, key):
    sm = SequenceMatcher(None, [key(x[0]) for x in a], [key(x[0]) for x in b], autojunk=False)
    return sm.get_opcodes()


# P index -> C token, to read CCEL beside any P range
c_map = {}
for op, i1, i2, j1, j2 in ops(pt, ct, lambda w: w.lower()):
    if op == 'equal':
        for k in range(i2 - i1):
            c_map[i1 + k] = j1 + k


def c_range(i1, i2):
    """CCEL text standing where P[i1:i2] stands (bounded by aligned neighbours)."""
    lo = next((c_map[k] for k in range(i1 - 1, max(-1, i1 - 30), -1) if k in c_map), None)
    hi = next((c_map[k] for k in range(i2, min(len(pt), i2 + 30)) if k in c_map), None)
    if lo is None or hi is None or hi - lo > 40:
        return None
    return ' '.join(x[0] for x in ct[lo + 1:hi])


def text(ts):
    s = ' '.join(t[0] for t in ts)
    s = re.sub(r' ([,.;:?!)\]])', r'\1', s)
    s = re.sub(r'([(\[]) ', r'\1', s)
    return s


auto, review = [], []
n = 0
for op, i1, i2, j1, j2 in ops(pt, gt, skel):
    if op == 'equal':
        # skeleton-equal: keep P unless P's word is unknown and G's known
        for k in range(i2 - i1):
            pw, gw = pt[i1 + k][0], gt[j1 + k][0]
            if pw == gw:
                continue
            if not known(pw) and known(gw):
                auto.append({'i1': i1 + k, 'i2': i1 + k + 1, 'p': pw, 'to': gw, 'rule': 'skel-G-known'})
            elif known(pw) and known(gw) and pw.lower() != gw.lower():
                cw = c_range(i1 + k, i1 + k + 1)
                rec = {'i1': i1 + k, 'i2': i1 + k + 1, 'p': pw, 'g': gw, 'c': cw}
                if cw is not None and cw.lower() == pw.lower():
                    continue
                if cw is not None and cw.lower() == gw.lower():
                    auto.append({**rec, 'to': gw, 'rule': 'skel-G=C'})
                elif pw.lower() in ('he', 'be', 'his', 'bis', 'hut', 'but', 'hy', 'by', 'ho', 'bo', 'hear', 'bear', 'hard', 'bard'):
                    review.append(rec)
        continue
    ps, gs = pt[i1:i2], gt[j1:j2]
    ptxt, gtxt = text(ps), text(gs)
    if op == 'insert':
        # G has tokens P lacks: usually G noise (stray marks); review real words
        if any(re.search('[A-Za-z]{2}', t[0]) and known(t[0]) for t in gs) and len(gs) <= 6:
            ctxt = c_range(i1, i1)
            rec = {'i1': i1, 'i2': i1, 'p': '', 'g': gtxt, 'c': ctxt}
            if ctxt is not None and ctxt.lower() == gtxt.lower():
                auto.append({**rec, 'to': gtxt, 'rule': 'insert-G=C'})
            else:
                review.append(rec)
        continue
    ctxt = c_range(i1, i2)
    rec = {'i1': i1, 'i2': i2, 'p': ptxt, 'g': gtxt, 'c': ctxt}
    pk = all(known(t[0]) for t in ps)
    pset = [x[0] for x in ps]
    gk = op == 'replace' and all(known(t[0]) and (re.fullmatch(r"[A-Za-z'’]+", t[0]) or t[0] in pset) for t in gs)
    low = lambda s: (s or '').lower().replace(' ', '')
    if ctxt is not None and low(ctxt) == low(ptxt):
        continue                                   # CCEL backs P
    if op == 'replace' and ctxt is not None and low(ctxt) == low(gtxt):
        auto.append({**rec, 'to': gtxt, 'rule': 'G=C'}); continue
    if op == 'delete':
        if all(not re.search('[A-Za-z0-9]', t[0]) for t in ps) and len(ps) <= 2:
            review.append(rec); continue          # stray or real punctuation
        if pk:
            review.append(rec); continue
        review.append(rec); continue
    if pk and not gk:
        continue                                   # G garbled, P plausible
    if gk and not pk:
        auto.append({**rec, 'to': gtxt, 'rule': 'G-known'}); continue
    review.append(rec)

ctx = lambda a, b: (text(pt[max(0, a - 10):a]), text(pt[b:b + 10]))
with open(outp + '.auto.jsonl', 'w') as f:
    for r in auto:
        r['page'] = pt[r['i1']][2] if r['i1'] < len(pt) else ''
        r['para'] = pt[r['i1']][1] if r['i1'] < len(pt) else -1
        r['before'], r['after'] = ctx(r['i1'], r['i2'])
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(outp + '.review.jsonl', 'w') as f:
    for k, r in enumerate(review):
        r['id'] = k
        r['page'] = pt[r['i1']][2] if r['i1'] < len(pt) else ''
        r['para'] = pt[r['i1']][1] if r['i1'] < len(pt) else -1
        r['before'], r['after'] = ctx(r['i1'], r['i2'])
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
from collections import Counter
print('auto', len(auto), Counter(r['rule'] for r in auto), 'review', len(review))
