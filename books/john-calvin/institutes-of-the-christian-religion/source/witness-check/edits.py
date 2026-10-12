"""Apply exact (file, old, new) edits, tolerant of quote style and Greek
normalization; each old must occur exactly once (as written or normalised)."""
import sys,unicodedata,re,json
from pathlib import Path
def apply(base, edits):
    base=Path(base)
    for f,a,b in edits:
        p=base/f; t=p.read_text()
        if t.count(a)==1:
            p.write_text(t.replace(a,b,1)); print('ok  ',f,b[:70]); continue
        T=unicodedata.normalize('NFC',t); A=unicodedata.normalize('NFC',a)
        pat=re.escape(A).replace('"','["“”]').replace("'","['’]")
        ms=list(re.finditer(pat,T))
        if len(ms)!=1: print('MISS',len(ms),f,a[:70]); continue
        old=ms[0].group(0)
        if t.count(old)==1: p.write_text(t.replace(old,b,1))
        else: p.write_text(T[:ms[0].start()]+b+T[ms[0].end():])
        print('ok~ ',f,b[:70])
if __name__=='__main__':
    apply(sys.argv[1], json.load(open(sys.argv[2])))
