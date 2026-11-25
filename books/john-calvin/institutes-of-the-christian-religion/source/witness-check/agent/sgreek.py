"""List suspected SGreek-font (ASCII-encoded) Greek runs in vol-2 .typ files."""
import re, glob, os
ED = "/home/courtney/Projects/fgbooks/books/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-2"
pat = re.compile(r"\b[a-zA-Z]*(?:[aeiouhw][jJ]|[aeiouhw]v\b|[a-z]v[ a-z]|\b[a-z]+[;\[\]\\\/=]+[a-z]|[aeiouhw]\[|\b[aeiouhw]\[)[^\s]*")
for f in sorted(glob.glob(ED + "/*.typ")):
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r"[^\s]*(?:iva|ajk|ej|oj|uj|hj|wj|oJ|ej|ai;|\\ma|\[a-z])[^\s]*", s):
        w = m.group(0)
        if re.search(r"[a-z]v[aeiouhw]?\b|[aeiouhw][jJ]|\w;\w|\w\\\w|\w\[\w", w) and not re.search(r"^(?:obj|adj|subj|rej|proj|inj|maj|conj|dej|enjoy|object|subject)", w.lower()):
            print(os.path.basename(f), repr(s[max(0, m.start()-50):m.end()+50]))
