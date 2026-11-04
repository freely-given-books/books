"""Write the corrected transcription of The Crook in the Lot as ThML.

usage: build_thml.py FINAL.json PB.json OUT.thml.xml

FINAL.json: corrected paragraphs (same indexing as assemble.py's output).
PB.json: assemble.py output with page-break contexts ('pb'), to place
McMillan's page breaks inside paragraphs.
"""
import json, re, sys
from difflib import SequenceMatcher
from xml.sax.saxutils import escape

final, pbsrc, out = sys.argv[1:4]
paras = json.load(open(final))
pbs = json.load(open(pbsrc))
assert len(paras) == len(pbs), (len(paras), len(pbs))


def x(text):
    """Escape for XML, keeping <i>...</i>."""
    parts = re.split(r'(</?i>)', text)
    return ''.join(p if p in ('<i>', '</i>') else escape(p) for p in parts)


def strip(t):
    return re.sub(r'</?i>', '', t)


def place_breaks(i, text):
    """Insert <pb n=".."/> markers into paragraph i where its page breaks fall."""
    out = text
    for pb in reversed(pbs[i]['pb']):
        after = ' '.join(pb['after'].split())[:30]
        plain = strip(out)
        # fuzzy-find the first words of the new page in the plain text
        sm = SequenceMatcher(None, plain, after, autojunk=False)
        m = max(sm.get_matching_blocks(), key=lambda b: b.size)
        if i in SPLIT_AT_BREAK:
            continue
        if m.size >= 8:
            pos = m.a - m.b                 # start of the new page in plain text
            while pos > 0 and plain[pos - 1] not in ' —-':
                pos -= 1
            if pos > 0 and plain[pos - 1] in '—-':   # inside a hyphened word: after it
                while pos < len(plain) and plain[pos] != ' ':
                    pos += 1
        else:                               # the new page opened with a running head: use the old page's end
            before = ' '.join(pb['before'].split())[-30:]
            sm = SequenceMatcher(None, plain, before, autojunk=False)
            m = max(sm.get_matching_blocks(), key=lambda b: b.size)
            if m.size < 8:
                print(f'pb {pb["n"]}: not found in para {i}: {after!r}', file=sys.stderr)
                continue
            pos = m.a - m.b + len(before)
            while pos < len(plain) and plain[pos] != ' ':
                pos += 1
        # map plain offset to tagged offset
        k = j = 0
        while j < pos:
            mt = re.match(r'</?i>', out[k:])
            if mt:
                k += len(mt.group(0)); continue
            k += 1; j += 1
        out = out[:k] + f'\x00{pb["n"]}\x00' + out[k:]
    return out


SPLIT_AT_BREAK = set()       # paragraphs whose page break is placed by hand (a heading opens the page)


def para_xml(i, text, cls=None):
    t = x(place_breaks(i, text))
    t = re.sub(r'\x00(\d+)\x00', r'<pb n="\1"/>', t)
    c = f' class="{cls}"' if cls else ''
    return f'<p{c}>{t}</p>'


def page_start(i, prev_last):
    first = paras[i]['pages'][0]
    return f'<pb n="{first}"/>' if first != prev_last else ''


# ---- structure, by paragraph index (see text.txt) ----
P = [p['text'] for p in paras]


def find(pat, start=0):
    for k in range(start, len(P)):
        if re.search(pat, strip(P[k])):
            return k
    raise SystemExit(f'not found: {pat}')


READER_HEAD = find(r'^TO THE READER')
PART1 = find(r'^E\S+ vii\. 13')
DOC1 = find(r'^DOCTRINE I\.')
DOC2 = find(r'^DOCT\S* II\.')
DOC3 = find(r'^DOCTRINE last')
PART2 = find(r'^P\S+ xvi\. 19')
DOC21 = find(r'^Doctrine,')
PART3_IN = find(r'1 PETER [Vv]\. 6\.$')     # heading run into the paragraph before
DOC31 = find(r'^DOCTRINE I\.', PART3_IN)
DOC32_IN = find(r'DOCTRINE II\.', DOC31)  # heading run into a paragraph
SPLIT_AT_BREAK.update({PART3_IN})
print('structure', READER_HEAD, PART1, DOC1, DOC2, DOC3, PART2, DOC21, PART3_IN, DOC31, DOC32_IN, file=sys.stderr)

body = []
last_page = None


def emit_para(i, text=None, cls=None):
    global last_page
    text = P[i] if text is None else text
    body.append(page_start(i, last_page) + para_xml(i, text, cls))
    last_page = paras[i]['pages'][-1]


def doctrine_head(i, rest_from=None):
    """'DOCTRINE I. <i>statement</i>' -> h3 'Doctrine I.' + the statement as a paragraph."""
    t = P[i] if rest_from is None else rest_from
    m = re.match(r'(DOCT\S*|Doctrine)\s*(I{1,3}|last)?[.,]\s*', strip(t))
    label = m.group(0).strip().rstrip(',').rstrip('.')
    word, num = (label.split() + [''])[:2]
    head = 'Doctrine' + (f' {num.capitalize() if num == "last" else num}' if num else '') + '.'
    # cut the label off the tagged text
    plain_len = len(m.group(0))
    k = j = 0
    while j < plain_len:
        mt = re.match(r'</?i>', t[k:])
        if mt:
            k += len(mt.group(0)); continue
        k += 1; j += 1
    rest = t[k:].lstrip()
    if t[:k].count('<i>') > t[:k].count('</i>'):
        rest = '<i>' + rest
    return head, rest


def span(a, b):
    for i in range(a, b):
        emit_para(i)


title = ('<div1 title="Title Page" id="i">\n'
         '<h1>The Crook in the Lot</h1>\n'
         '<p class="Centered">or, The Sovereignty and Wisdom of God Displayed in the Afflictions of Men, '
         'together with a Christian Deportment under Them. Being the Substance of Several Sermons on '
         'Eccles. vii. 13. Prov. xvi. 19. and 1 Pet. v. 6.</p>\n'
         '<h2>Thomas Boston</h2>\n</div1>')

# To the Reader
body.append('<div1 title="To the Reader" id="ii">')
body.append('<h2>To the Reader.</h2>')
span(READER_HEAD + 1, PART1)
body.append('</div1>')

# Part I
body.append('<div1 title="Part I" id="iii">')
body.append('<h2>The Crook in the Lot.</h2>')
emit_para(PART1, cls='Centered')
emit_para(PART1 + 1, P[PART1 + 1].replace('</i>', '') + ' ' + P[PART1 + 2].replace('<i>', ''), cls='Centered')
span(PART1 + 3, DOC1)
for k, (a, b) in enumerate(((DOC1, DOC2), (DOC2, DOC3), (DOC3, PART2)), 1):
    body.append(f'<div2 title="Doctrine {["I", "II", "Last"][k - 1]}" id="iii.{k}">')
    if a == DOC2:                      # its statement is set over three OCR paragraphs
        stmt = ' '.join(P[a:a + 3])
        stmt = re.sub(r'</i>\s*<i>', ' ', stmt)
        head, rest = doctrine_head(a, stmt)
        body.append(f'<h3>{head}</h3>')
        emit_para(a, rest)
        span(a + 3, b)
    else:
        head, rest = doctrine_head(a)
        body.append(f'<h3>{head}</h3>')
        emit_para(a, rest)
        span(a + 1, b)
    body.append('</div2>')
body.append('</div1>')

# Part II
body.append('<div1 title="Part II" id="iv">')
emit_para(PART2, cls='Centered')
emit_para(PART2 + 1, P[PART2 + 1].replace('</i>', '') + ' ' + P[PART2 + 2].replace('<i>', ''), cls='Centered')
span(PART2 + 3, DOC21)
body.append('<div2 title="Doctrine" id="iv.1">')
head, rest = doctrine_head(DOC21)
body.append(f'<h3>{head}</h3>')
emit_para(DOC21, rest)
span(DOC21 + 1, PART3_IN)
# the paragraph that ends with Part III's heading
t = P[PART3_IN]
cut = t.rindex('1 PETER v. 6.')
emit_para(PART3_IN, t[:cut].rstrip())
body.append('</div2>')
body.append('</div1>')

# Part III
body.append('<div1 title="Part III" id="v">')
body.append(f'<pb n="{paras[PART3_IN]["pages"][-1]}"/><p class="Centered">1 PETER v. 6.</p>')
span(PART3_IN + 1, PART3_IN + 2)
body[-1] = body[-1].replace('<p>', '<p class="Centered">', 1)
span(PART3_IN + 2, DOC31)
body.append('<div2 title="Doctrine I" id="v.1">')
head, rest = doctrine_head(DOC31)
body.append(f'<h3>{head}</h3>')
emit_para(DOC31, rest)
span(DOC31 + 1, DOC32_IN)
t = P[DOC32_IN]
cut = t.index('DOCTRINE II.')
emit_para(DOC32_IN, t[:cut].rstrip())
body.append('</div2>')
body.append('<div2 title="Doctrine II" id="v.2">')
head, rest = doctrine_head(DOC32_IN, t[cut:])
px = para_xml(DOC32_IN, rest)
lead = re.match(r'<p><pb n="\d+"/>', px)
if lead:                               # the page opens with the heading
    body.append(lead.group(0)[3:])
    px = '<p>' + px[lead.end():]
body.append(f'<h3>{head}</h3>')
body.append(px)
span(DOC32_IN + 1, len(P))
body.append('</div2>')
body.append('</div1>')

HEAD = '''<?xml version="1.0" encoding="UTF-8"?>
<ThML>
<ThML.head>
<generalInfo>
  <description>Thomas Boston's The Crook in the Lot (first published Edinburgh, 1737), transcribed from Samuel M'Millan's edition of his Whole Works for Freely Given Books.</description>
  <pubHistory>First published Edinburgh, 1737, after Boston's death (1732), with his Sermons on Church Communion; reprinted without abridgment in The Whole Works of the Late Reverend Thomas Boston, of Ettrick, ed. Samuel M'Millan, vol. 3 (Aberdeen, 1848).</pubHistory>
  <comments>Transcribed from two archive.org scans of M'Millan's vol. 3 (Princeton Theological Seminary Library, wholeworksoflate03bost; University of Michigan, wholeworkslater06bostgoog): the ABBYY OCR of the first, italics included, corrected where the two OCRs disagree and checked against the page images. M'Millan's page breaks are kept as pb. The running heads, signature marks and M'Millan's footnote to "To the Reader" are left out; a doctrine's small-capital label ("DOCTRINE I.") is set as the heading of its division, its statement as the first paragraph. The Sermons on Church Communion that follow in the volume are not included.</comments>
</generalInfo>
<printSourceInfo>
  <published>The Whole Works of the Late Reverend Thomas Boston, of Ettrick, edited by Samuel M'Millan, vol. 3 (Aberdeen: George and Robert King, 1848), pp. 495-590.</published>
</printSourceInfo>
<electronicEdInfo>
  <publisherID>fgb</publisherID>
  <authorID>boston</authorID>
  <bookID>crook</bookID>
  <DC>
    <DC.Title>The Crook in the Lot</DC.Title>
    <DC.Creator sub="Author">Thomas Boston</DC.Creator>
    <DC.Creator sub="Author" scheme="file-as">Boston, Thomas (1677-1732)</DC.Creator>
    <DC.Publisher>Freely Given Books</DC.Publisher>
    <DC.Date sub="Created">2026-10-10</DC.Date>
    <DC.Source>The Whole Works of the Late Reverend Thomas Boston, of Ettrick, ed. Samuel M'Millan, vol. 3 (Aberdeen, 1848), pp. 495-590.</DC.Source>
    <DC.Language scheme="ISO639-3">eng</DC.Language>
    <DC.Rights>Public Domain</DC.Rights>
  </DC>
</electronicEdInfo>
</ThML.head>
<ThML.body>
'''
with open(out, 'w') as f:
    f.write(HEAD)
    f.write(title + '\n')
    f.write('\n'.join(body) + '\n')
    f.write('</ThML.body>\n</ThML>\n')
print('wrote', out, file=sys.stderr)
