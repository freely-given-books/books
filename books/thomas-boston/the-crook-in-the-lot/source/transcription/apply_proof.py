"""Apply proofreaders' proposals: `ocr` lines to the transcription and the
chapters, `fix` lines (the 1848 printing's own misprints) to the chapters only.

usage: apply_proof.py CHAPTERS_DIR TEXT.json OUT.json PROPOSALS.jsonl [...]

An `old` must occur exactly once in its chapter file, and (for `ocr`) once
in the transcription after converting Typst to its markup (#emph[..] ->
<i>..</i>, curly quotes -> straight). Anything that fails is reported and
not applied anywhere.
"""
import json, re, sys
from pathlib import Path

chapters, text_in, text_out, *props = sys.argv[1:]
paras = json.load(open(text_in))


def to_src(s):
    s = s.replace('#emph[', '<i>').replace(']', '</i>')
    s = s.replace('\\;', ';').replace('\\(', '(').replace('\\[', '[')
    return s.translate(str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"}))


files = {}
done = {'ocr': 0, 'fix': 0}
failed = []
for prop in props:
    for line in open(prop):
        if not line.strip():
            continue
        p = json.loads(line)
        if p.get('class') not in ('ocr', 'fix') or p.get('new') is None:
            continue
        f = Path(chapters) / p['file']
        t = files.setdefault(f, f.read_text())
        if t.count(p['old']) != 1:
            failed.append(('typ', p)); continue
        if p['class'] == 'ocr':
            old, new = to_src(p['old']), to_src(p['new'])
            hits = [i for i, q in enumerate(paras) if old in q['text']]
            if len(hits) != 1 or paras[hits[0]]['text'].count(old) != 1:
                failed.append(('src', p)); continue
            paras[hits[0]]['text'] = paras[hits[0]]['text'].replace(old, new)
        files[f] = t.replace(p['old'], p['new'])
        done[p['class']] += 1
for f, t in files.items():
    f.write_text(t)
json.dump(paras, open(text_out, 'w'), indent=0, ensure_ascii=False)
print(done, len(failed), 'failed')
for where, p in failed:
    print('FAILED', where, json.dumps(p, ensure_ascii=False))
