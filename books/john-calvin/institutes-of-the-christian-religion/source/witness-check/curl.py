"""Curl straight double quotes on lines changed since HEAD (a fix taken from
the 1845 text can bring its straight quotes into CCEL's curly ones):
opening after a space, bracket or dash, closing otherwise."""
import sys,subprocess,re
from pathlib import Path
for p in sorted(Path(sys.argv[1]).glob('*.typ')):
    old=subprocess.run(['git','show',f'HEAD:{p}'],capture_output=True,text=True).stdout.split('\n')
    new=p.read_text().split('\n'); n=0; olds=set(old)
    for i,l in enumerate(new):
        if l in olds or '"' not in l: continue
        def q(m):
            nonlocal_n[0]+=1
            pre=l[m.start()-1] if m.start() else ' '
            return '“' if pre.isspace() or pre in '([—–[' else '”'
        nonlocal_n=[0]; new[i]=re.sub('"',q,l); n+=nonlocal_n[0]
    if n: p.write_text('\n'.join(new)); print(p.name,n)
