#!/bin/bash
# usage: batch.sh out.png page:word page:word ...
out=$1; shift; files=()
for pw in "$@"; do p=${pw%%:*}; w=${pw#*:}; f=crops/b-$p-${w//[^A-Za-z0-9]/_}.png
python3 -I /home/courtney/Projects/fgbooks/work/institutes/latin/vol6/recheck/crop.py $p "$w" 0 $f >/dev/null || echo "MISS $pw"; files+=($f); done
magick "${files[@]}" -resize 60% -append $out
