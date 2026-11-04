#!/bin/bash
# Grace Abounding 1688: transcription -> TEI source -> reading text (review) -> enriched TEI, in build/
set -e
cd ~/Projects/fgbooks/work/grace-abounding
PY=~/Projects/fgbooks/colophon/.venv/bin/python
C=~/Projects/fgbooks/books/colophon
CPY="uv run --quiet --locked --project $C python"
$PY emit_tei.py
cp grace-1688.tcp.xml build/source/grace-abounding-1688.tcp.xml
(cd build/source && $CPY $C/build_tei.py grace-abounding-1688.tcp.xml auto.tei.xml >/dev/null)
rm -rf build/typ && mkdir build/typ && $CPY $C/tei_extract.py build/source/auto.tei.xml $PWD/build/typ >/dev/null
$PY triage.py >/dev/null && python3 bucket.py
$PY apply_1688.py build/review
$PY transfer_italics.py build/typ build/review | tail -1
(cd build/source && $CPY $C/build_tei.py grace-abounding-1688.tcp.xml grace-abounding.tei.xml --review ../review --report review-report.md | tail -1)
rm -rf build/out && mkdir build/out && $CPY $C/tei_extract.py build/source/grace-abounding.tei.xml $PWD/build/out >/dev/null
$PY paradiff.py build/out
# into the book: chapters, Scripture reference style, sync, check (the TEI's extraction is the fixed point)
BK=~/Projects/fgbooks/books; B=$BK/books/john-bunyan/grace-abounding
cp grace-1688.tcp.xml $B/source/grace-abounding-1688.tcp.xml
cp build/review/*.typ $B/chapters/typ/
cd $BK
./fgb sync grace-abounding >/dev/null
D=$(mktemp -d); $CPY $C/tei_extract.py $B/source/grace-abounding.tei.xml $D >/dev/null; cp $D/*.typ $B/chapters/typ/
$CPY $C/refstyle.py $B --write >/dev/null
./fgb sync grace-abounding >/dev/null
./fgb check grace-abounding | tail -1
