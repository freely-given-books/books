"""Page fit: wrap a chapter's #include in a slightly tighter letter spacing so no chapter ends on 1-4 lines
(print_check's page warning), as Precious Remedies. python3 pagefit.py PRINT.typ DIR FILE=TRACKING ...  (tracking
"0" removes the wrap)"""
import re, sys
from pathlib import Path
p = Path(sys.argv[1]); d = sys.argv[2]; t = p.read_text()
for arg in sys.argv[3:]:
    f, tr = arg.split("=")
    inc = f'#include "chapters/{d}/{f}.typ"'
    t = re.sub(r'// a short chapter ending pulled back[^\n]*\n#\[\n  #set text\(tracking: [^)]*\)\n  ' + re.escape(inc) + r'\n\]', inc, t)
    if tr != "0":
        assert t.count(inc) == 1, f
        t = t.replace(inc, f"// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter\n#[\n  #set text(tracking: {tr})\n  {inc}\n]")
p.write_text(t)
