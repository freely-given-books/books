# Of Domestical Duties — William Gouge

*Of Domesticall Dvties: Eight Treatises* (London, printed by John Haviland for
William Bladen, 1622). Preached to the parish of Blackfriars: an exposition of
Ephesians 5:21–6:9, then the duties of husband and wife, of wives, of husbands,
of children, of parents, of servants, and of masters — each set against the
faults that answer to it.

Set from the Text Creation Partnership transcription of the first edition,
EEBO-TCP `A68107`, with the spelling modernized. 290,000 words.

**In print it is four volumes; as an ebook it is one file.** 795 pages of text
will not perfect-bind as a single block, and a reader searching for a duty
should not have to search four books.

| Volume | Contents | Pages |
| --- | --- | --- |
| I — The First Treatise | An exposition of Ephesians 5:21–6:4 | 195 |
| II — The Second, Third and Fourth Treatises | Of husband and wife | 295 |
| III — The Fifth and Sixth Treatises | Of children and parents | 194 |
| IV — The Seventh and Eighth Treatises | Of servants and masters, with the exposition of Ephesians 6:5–9 | 153 |

## Volumes and chapters

The volumes follow Gouge's own eight treatises. Volume IV takes Treatises VII
and VIII together with the part of Treatise I that expounds Ephesians 6:5–9,
which belongs with them.

Gouge wrote in numbered sections, not chapters, so the 50 chapters are an
editorial division for reading: a treatise of 133 sections needs somewhere to
stop. **Every one of his section headings is kept underneath**, at its own
heading level and in his own words, so nothing of his arrangement is lost — a
chapter title is a signpost over his sections, not a replacement for them.

`sources/edition.json` is the map: which sections of which division make up
each chapter. Chapters are cut by **ordinal position** among a treatise's
sections, never by the printed section number — Gouge prints "§. 15", "§. 43",
"§. 46" and "§. 58" twice each in Treatise IV alone, and two sections have no
number at all.

## Layout

| Path | What it is |
| --- | --- |
| `sources/edition.json` | the volume and chapter map — **edit this, not the generated files** |
| `sources/build_edition.py` | turns that map into chapters, volumes, ebook and covers |
| `chapters/typ/vol-N/` | one `.typ` per chapter, plus the front and back matter each volume claims |
| `domestical-duties-vol-N.typ` | print edition of one volume (generated) |
| `cover-vol-N.typ` | its wrap cover (generated; page count read from the compiled PDF) |
| `ebook-domestical-duties.typ` | the whole work as one ebook (generated) |
| `cover-ebook.typ` | a wrap with no volume line; the epub's cover image is cut from its front panel |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `sources/` | the TEI source and the converter |
| `sources/original-spelling/` | the same text with the 1622 spelling untouched, for reference and for checking the modernizer |

`sources/CLAUDE.md` documents the conversion pipeline and what was learned
building it — read that before changing anything under `sources/`.

## Editorial decisions

- **Spelling is modernized; wording is not.** `hath`, `doth`, `thou`, `ye`,
  `shalt` and the rest are different grammatical forms, not alternate
  spellings, and are left alone. So is `then` for `than`, and possessives
  without an apostrophe (`Gods word`, `his wives duty`).
- **Marginal notes are modernized too**, unlike the Perkins volume. Gouge's
  margins carry a running analytical summary in English alongside the
  citations, and leaving those in 1622 spelling beside modernized text reads as
  an accident. Latin quotations in the margins are detected and left exactly as
  printed.
- **Illegible letters have been reconstructed.** TCP marks 477 spans it could
  not read; 475 are filled, mostly from the book's own vocabulary and the rest
  by hand from context or from the work being cited. One is left as `…` — a
  lost word in Volume III, "Children Getting Parents' Permission".
- **Greek and Hebrew in the margins is dropped**, not marked. TCP could not key
  it and there is no page image here to read it from; a bracketed
  "in non-Latin alphabet" placeholder is noise in a reading edition.
- **Six pages are missing from the source.** Pages 191–196 of the 1622 edition
  were not captured on the microfilm TCP transcribed. They fall in Volume II,
  chapter 1 ("Seeking Marriage"), where Gouge is setting out how a marriage
  contract is made. An editorial note stands in their place. Filling them needs
  a second copy — the 1626 or 1634 edition on archive.org — and has not been
  done.
- **The original table of contents is not reproduced.** It indexes the 1622
  pagination, which this edition does not share; each volume's generated
  outline and the ebook's 645-entry table of contents replace it. The author's
  *parallel* of husbands' and wives' duties, which he designed as a reading aid
  and which keys to § numbers rather than pages, opens Volume II.
- **The author's brace diagrams are set as lists, not as tables.** Gouge's
  compositor drew braces to show one thing dividing into several — "Behold
  here the mutual relation betwixt {Christ, / The Church.}" — and 76 of them
  survive in the source as TEI tables. Each becomes a lead-in and an
  enumerated list, read down the columns as the brace groups them. The one
  that interrupts a sentence — "a family consisteth of these three orders,
  husbands, wives, parents, children, masters, servants, all which he
  reckoneth up" — is flattened into the sentence instead.
- **The 1622 errata are printed at the back of Volume IV but not applied.**
  They key to original page and line numbers, which cannot be resolved against
  this setting.

## Steps for Generation

### chapters, volumes and the ebook source

Run from `sources/`. Everything comes out of `edition.json`.

``` sh
$ python3 build_edition.py                # chapters, four volume files, ebook
$ python3 build_edition.py --original     # ...and the old-spelling reference
```

Needs `lxml` and `pyspellchecker`.

To work on the text itself rather than its arrangement, call the renderer
directly — `tcp_to_typst.py --list` prints the divisions, `--gap-report
gaps.tsv` writes the illegible-span report, and every unresolved or
wrongly-resolved line in it is a candidate for `GAP_FIXES` in
`gap_resolver.py`.

### pdf

``` sh
$ for n in 1 2 3 4
      typst compile domestical-duties-vol-$n.typ domestical-duties-vol-$n.pdf
  end
```

### covers

A cover needs the interior's page count, so it is a second pass: compile the
volumes first, then generate the covers from the compiled PDFs. `--covers`
reads the count out of each PDF rather than taking it on trust — a stale
`pages:` is a wrong spine, and a wrong spine is a wrecked print run.

``` sh
$ python3 sources/build_edition.py --covers
$ for n in 1 2 3 4
      typst compile --root ../../../ cover-vol-$n.typ cover-vol-$n.pdf
  end
$ typst compile --root ../../../ cover-ebook.typ cover-ebook.pdf
```

Each generated cover carries, in a comment, the exact `magick` command that
cuts its front panel out of the wrap. The crop offset is `bleed + trim +
spine`, so it moves when the page count does.

### ebook

``` sh
$ typst compile --features html ebook-domestical-duties.typ -f html
$ ebook-convert ebook-domestical-duties.html domestical-duties.epub \
        --authors "William Gouge" \
        --title "Of Domestical Duties" \
        --cover cover-ebook-front.jpg \
        --extra-css ../../resources/css/ebook.css \
        --extra-css ebook-override.css \
        --epub-version 2 \
        --level1-toc '//h:h3' \
        --level2-toc '//h:h4'
```

The second TOC level is what makes the ebook usable: the book has 592 numbered
sections, and a 53-entry table of contents for 290,000 words is not navigation.

## Before printing

- **Verify each wrap against a live template.** Download the 6×9 perfect-bound
  template for the actual page count and paper and check the cover against it.
- **The spine formulas disagree on thick books.** `pages × caliper` and Lulu's
  own `pages / 444 + 0.06in` agree under about 240 pages and drift apart above
  it. The generated covers use the Lulu figure explicitly, via the `spine:`
  override added to `scripts/panel_cover.typ`.
- **All four volumes are inside the range that binds and opens flat.** 153–295
  pages, against Lulu's 32–800 for perfect binding and the ~420 at which a
  glued block stops opening flat.
