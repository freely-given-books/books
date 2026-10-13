# Resolving gaps from a second witness

Read this when a `GAP_FIXES` entry can't be settled from context: Greek or
Hebrew, citation digits, long spans.

A text later gathered into a collected *Workes* was usually reset from the
same copy, and the reset margins are often legible where the original's are
not. For *Christian Oeconomie* the witness was the 1609 folio *Workes of that
famous and worthie minister of Christ, M. W. Perkins*, vol. 3, scanned on
archive.org as
`bim_early-english-books-1475-1640_the-workes-of-that-famou_perkins-william_1609_3`.
It resolved all eight gaps that context could not, including the Greek and
Hebrew ones.

## Finding the passage without "search inside"

The search text has no page breaks, but the page index gives each leaf's
character range:

```sh
ID=<archive.org identifier>
curl -sL -o st.txt.gz  "https://archive.org/download/$ID/${ID}_hocr_searchtext.txt.gz"
curl -sL -o pi.json.gz "https://archive.org/download/$ID/${ID}_hocr_pageindex.json.gz"
# idx[leaf] == [char_start, char_end, ...]: slice the text by it, grep the slices
```

Then fetch that leaf's image and crop the margin:

```sh
curl -sL -o p.jpg "https://archive.org/download/$ID/page/n<LEAF>_w2000.jpg"
magick p.jpg -crop WxH+X+Y +repage -resize 700% -normalize -sharpen 0x1 out.png
```

- Search the OCR for short, odd words ("Paternus", "glue"), not phrases.
  Early-modern OCR mangles long-s, u/v and word spacing, so a four-word
  query usually misses.
- Read the **image**, never the OCR, for the answer. The OCR of the note
  that turned out to be `Aristot. Politic. 1.` was `AY tot.Pe, - facet.`
- Record the witness in the evidence note, e.g.
  `"1609 Workes vol. 3, leaf 412 margin"`, with certainty `high` when the
  image is clear.

## When there is no witness

Leave the gap out of `GAP_FIXES` (it renders as the TCP's `•` / `〈…〉`) and
list it for the user with its page-image id from `build_tei.py --list`
(`tcp:NNNN:NN`). The user may have access to page images you don't.
