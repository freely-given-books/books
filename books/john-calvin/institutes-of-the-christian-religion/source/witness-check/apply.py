import json,sys,re,difflib
from pathlib import Path
rep=Path(sys.argv[1]); base=Path(sys.argv[2]); dry='--dry' in sys.argv
F=[json.loads(l) for l in rep.read_text().splitlines() if l.startswith('{"file"')]
NUM=re.compile(r'\d|^(?:[ivxlc]+\.?|[IVXLC]+\.?)[,;)]*$')
done=[];skipped=[]
texts={}
for f in F:
    if f['kind'] in ('info',) : continue
    p=base/f['file']; t=texts.setdefault(p,p.read_text())
    if t.count(f['ccel'])!=1: skipped.append(('nomatch',f)); continue
    a=f['ccel'].split(); b=re.sub(r'\s*\((verified|OCR[^)]*)\)','',f['1845']).split()
    out=[]; any_=False; manual=False
    for o,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
        sa,sb=a[i1:i2],b[j1:j2]
        if o=='equal': out+=sa; continue
        if any(NUM.search(w) for w in sa+sb):
            # a lone stray note number deleted at a footnote's start
            if o=='delete' and all(re.fullmatch(r'\d+',w) for w in sa): any_=True; continue
            out+=sa; manual=True; continue
        out+=sb; any_=True
    if manual: skipped.append(('digits',f))
    if any_:
        new=' '.join(out)
        t=t.replace(f['ccel'],new,1); texts[p]=t; done.append((f['file'],f['ccel'],new))
for p,t in texts.items():
    if not dry: p.write_text(t)
print('applied',len(done))
for k,f in skipped: print('SKIP',k,f['kind'],f['file'],'|',f['ccel'][:80],'=>',f['1845'][:80])
