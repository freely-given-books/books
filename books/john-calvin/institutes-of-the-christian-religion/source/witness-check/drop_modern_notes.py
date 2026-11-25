"""Remove the 1953 reprint's editorial footnotes (CCEL keeps their numbers:
"#footnote[100 D100 These two assertions…]") from chapters/typ. Only the
public-domain notes of the 1845 printing stay in the edition."""
import re,sys
from pathlib import Path
def footnotes(t):
    i=0
    while True:
        i=t.find('#footnote[',i)
        if i<0: return
        j=i+len('#footnote['); d=1
        while d:
            c=t[j]
            if c=='\\': j+=2; continue
            d+= c=='['; d-= c==']'; j+=1
        yield i,j
        i=j
total=0
for p in sorted(Path(sys.argv[1]).glob('*/*.typ')):
    t=p.read_text(); spans=[(i,j) for i,j in footnotes(t) if re.match(r'#footnote\[\d+ D\d+ ',t[i:j])]
    for i,j in reversed(spans): t=t[:i]+t[j:]
    if spans: p.write_text(t); total+=len(spans); print(p.parent.name+'/'+p.name, len(spans))
print('removed',total)
