import sys,unicodedata,re,subprocess
from pathlib import Path
B=Path(sys.argv[1])
for p in sorted(B.glob('*.typ')):
    orig=subprocess.run(['git','show',f'HEAD:{p}'],capture_output=True,text=True).stdout
    m={}
    for w in re.findall(r"[^\s\[\]()#,.;:“”\"'’]+",orig):
        if unicodedata.normalize('NFC',w)!=w: m[unicodedata.normalize('NFC',w)]=w
    t=p.read_text(); n=0
    def sub(mo):
        global n
        w=mo.group(0)
        if w in m and m[w]!=w: n+=1; return m[w]
        return w
    t2=re.sub(r"[^\s\[\]()#,.;:“”\"'’]+",sub,t)
    if n: p.write_text(t2); print(p.name,'restored',n)
