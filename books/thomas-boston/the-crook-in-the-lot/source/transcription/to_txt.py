"""Write assembled paragraphs as text, one per line: N<TAB>pages<TAB>text.  usage: to_txt.py IN.json OUT.txt"""
import json, sys
with open(sys.argv[2], 'w') as f:
    for i, p in enumerate(json.load(open(sys.argv[1]))):
        f.write(f"{i}\t{','.join(p['pages'])}\t{p['text']}\n")
