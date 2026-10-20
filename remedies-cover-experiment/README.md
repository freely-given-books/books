# Engraved cover experiment (WIP)

A new cover system, mocked up on Thomas Brooks's *Precious Remedies Against
Satan's Devices* (2026-10-19). Not used by any book yet; the printed books
still use `scripts/panel_cover.typ`. How covers are made, and the design
rules agreed here, are in the `cover-design` skill
(`.claude/skills/cover-design/SKILL.md`).

`cover.jpg` is the current state (full wrap, 300 dpi).

## Files

| file | what |
|---|---|
| `Precious Remedies Vintage Book Wrap.png` | the user's AI mock-up: the look to match (its back-cover text is invented, not Brooks) |
| `Engraved Swords and Serpent Relic.png` | AI art: the sword (left) for the spine, the sword, shield and serpent (right) for the front |
| `extract.py` | cuts art off its dark ground into ink on transparent (see the skill) |
| `art/sword.png`, `art/vignette.png` | made by `extract.py` from the relic image (commands below) |
| `art/corner.svg` | the frame's corner: the inner rule ending in scrolls, a fleur-de-lis |
| `engraved_cover.typ` | the design: `engraved-cover(...)` |
| `cover.typ` | Precious Remedies in it |
| `fonts/` | Cinzel, EB Garamond (OFL, static instances; licence in `OFL.txt`) |

## Rebuild

Needs typst (0.15), uv, ImageMagick (`magick`). The `@preview/droplet`
package downloads on first compile.

```sh
cd remedies-cover-experiment
# the art (only if the source or extract.py changes)
x() { uv run -q --no-project --with numpy --with pillow --with scipy python -I extract.py "$@"; }
x "Engraved Swords and Serpent Relic.png" art/sword.png 60 40 380 1000
x "Engraved Swords and Serpent Relic.png" art/vignette.png 520 60 1420 1010
# the cover
typst compile --root .. --font-path "$PWD/fonts" cover.typ cover.pdf
typst compile --root .. --font-path "$PWD/fonts" --input front-only=true cover.typ front.png --ppi 150
typst compile --root .. --font-path "$PWD/fonts" cover.typ cover.png --ppi 300
magick cover.png -quality 92 cover.jpg
```

`cover.pdf`, `cover.png` and `front.png` are not committed (`.gitignore`).

## Decided with the user

- System: house identity fixed (ground, frame, type, rules, spine layout,
  imprint places); per author an emblem at the spine's head and an accent
  colour; per book the title, front engraving, spine art, back passages.
- Spine: surname, author emblem (placeholder: four gold diamonds, 0.3in),
  title, the book's art small and pinned at one height (sword 1.05in, foot
  1.75in above the trim), "Against / Satan's / Devices" under it with open
  leading, imprint mark, gold rules at head and foot. The sword is this
  book's art, not Brooks's emblem.
- Corners: the inner rule flows into the ornament (scrolls + fleur-de-lis),
  as in the mock-up; not a separate ornament inside a square frame.
- Back text is Brooks's own, from this edition: the Epistle Dedicatory
  ("Christ, the Scripture, your own hearts, and Satan's devices…") and A Word
  to the Reader ("'Tis not hasty reading…"). The "First published in 1652…"
  paragraph is Claude's and needs the editor's approval.

## Open

- **Imprint mark**: the user is making one. Dotted "MARK" circles hold its
  three places (front foot, spine foot, back foot) at print size. Wanted as a
  single-colour SVG. The imprint name is set as "Freely Given Books"; confirm.
- **Author emblems**: none drawn yet. Ideas offered: Bunyan a pilgrim's staff
  and scrip; Owen a lamp or pruning knife; Calvin his seal (heart in an open
  hand); Gouge an olive branch; Perkins a key or house; Sibbes a bruised reed;
  Boston a crook; Keach a trumpet; Brooks still to choose.
- **Art quality**: the relic image is 1536×1024 and lit on black; the
  vignette prints ~300 dpi at 3in only because it is cropped tight, with a
  faint glow ghost at leaf edges. Regenerate as black line engraving on
  plain white, one subject per image, largest size.
- **Not wired into `./fgb`**: to adopt, move `engraved_cover.typ` to
  `scripts/`, the fonts into the repository with `./fgb` passing
  `--font-path`, art into each book's folder, and teach `fgb.build_pdf` /
  `render_front` to recognise `engraved-cover(` as it does `panel-cover(`
  (that is a colophon change and release).
- Thin spines (<0.5in) have a fallback layout, never yet rendered on a real
  thin book (Keach, 74 pages).
- Fleur-de-lis is slightly smaller and further from the outer rule than in
  the mock-up; tune in `art/corner.svg` or `frame(ornament: ...)`.
- `book-review` and this experiment: when a book moves to the new design,
  its signed-off release is held back (its folder changes).
