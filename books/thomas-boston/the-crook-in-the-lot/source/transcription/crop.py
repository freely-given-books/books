"""Crop the printed line(s) holding some words from McMillan's Whole Works vol. 3.

usage: crop.py PAGE "words near the place" [--lines N] [--scan p|g]

PAGE is the printed page number (497-590; 496 = To the Reader).  The words
are matched fuzzily against the OCR of that page (and the pages either side),
so give 4-8 words as they appear in the text.  Writes a PNG of the best line
plus N lines below (default 1) and prints its path.  --scan g uses the second
scan (University of Michigan copy) instead of the Princeton copy.
"""
import json, os, subprocess, sys, urllib.request
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, 'work')
SCANS = {
    'p': ('wholeworksoflate03bost', 'p.lines.json', 14, 5),   # OCR leaf = page + 14, image = leaf - 5
    'g': ('wholeworkslater06bostgoog', 'g.lines.json', 7, 1),
}

args = sys.argv[1:]
scan = 'p'
nlines = 1
if '--scan' in args:
    k = args.index('--scan'); scan = args[k + 1]; del args[k:k + 2]
if '--lines' in args:
    k = args.index('--lines'); nlines = int(args[k + 1]); del args[k:k + 2]
page, words = int(args[0]), args[1]
ident, idx_file, offset, img_shift = SCANS[scan]
index = json.load(open(os.path.join(WORK, idx_file)))


def norm(s):
    return ' '.join(s.lower().split())


best = (0, None, None)
for leaf in (page + offset, page + offset - 1, page + offset + 1):
    pg = index.get(str(leaf))
    if not pg:
        continue
    lines = pg['lines']
    for i in range(len(lines)):
        # match against this line joined with the next, so words across a break are found
        text = norm(lines[i]['text'] + ' ' + (lines[i + 1]['text'] if i + 1 < len(lines) else ''))
        sm = SequenceMatcher(None, norm(words), text, autojunk=False)
        m = sm.find_longest_match(0, len(norm(words)), 0, len(text))
        score = sum(b.size for b in sm.get_matching_blocks()) / max(1, len(norm(words)))
        score += m.size / max(1, len(norm(words)))
        if score > best[0]:
            best = (score, leaf, i)
score, leaf, i = best
if leaf is None:
    sys.exit('no match')
pg = index[str(leaf)]
sel = pg['lines'][i:i + 1 + nlines]
l = max(0, min(x['l'] for x in sel) - 30)
r = min(pg['w'], max(x['r'] for x in sel) + 30)
t = max(0, min(x['t'] for x in sel) - 12)
b = min(pg['h'], max(x['b'] for x in sel) + 12)
imgdir = os.path.join(WORK, 'img')
os.makedirs(imgdir, exist_ok=True)
n = leaf - img_shift
src = os.path.join(imgdir, f'{scan}{n}.jpg')
if not os.path.exists(src):
    urllib.request.urlretrieve(f'https://archive.org/download/{ident}/page/n{n}_w1600.jpg', src)
size = subprocess.run(['magick', 'identify', '-format', '%w %h', src], capture_output=True, text=True).stdout.split()
sx, sy = int(size[0]) / pg['w'], int(size[1]) / pg['h']
out = os.path.join(imgdir, f'crop-{scan}{leaf}-{i}-{nlines}.png')
subprocess.run(['magick', src, '-crop', f'{int((r - l) * sx)}x{int((b - t) * sy)}+{int(l * sx)}+{int(t * sy)}',
                '+repage', '-colorspace', 'Gray', '-resize', '1100x>', out], check=True)
print(out)
print('OCR:', ' / '.join(x['text'] for x in sel))
