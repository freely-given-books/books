import json,sys,re,unicodedata
from pathlib import Path
rep=Path(sys.argv[1]); base=Path(sys.argv[2])
F=[json.loads(l) for l in rep.read_text().splitlines() if l.startswith('{"file"')]
def norm(s): return unicodedata.normalize('NFC',s).replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
for k,f in enumerate(F):
    if f['kind']=='info': continue
    t=(base/f['file']).read_text()
    if t.count(f['ccel'])==1: continue
    nt=norm(t); key=norm(f['ccel'])
    target=norm(re.sub(r'\s*\((verified|OCR[^)]*)\)','',f['1845']))
    if target in nt: continue
    # search a distinctive middle chunk
    words=[w for w in key.split() if len(w)>3]
    pos=-1
    for w in sorted(words,key=len,reverse=True)[:3]:
        if nt.count(w)==1: pos=nt.index(w); break
    snip=nt[max(0,pos-80):pos+120] if pos>=0 else '??'
    print(f'#{k} {f["kind"]} {f["file"]}\n  CCEL : {f["ccel"][:150]}\n  1845 : {f["1845"][:150]}\n  FILE : {snip}\n')
