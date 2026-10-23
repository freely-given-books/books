# Image-generator prompts (ChatGPT image)

Each prompt has three paragraphs: the subject, the composition, the style.
Keep the composition and style paragraphs as they are; write the subject from
the book's own image. Ask for portrait 2:3 at the largest size offered.

## The two fixed paragraphs

Composition (adjust the subject's place, keep the bands):

```
Composition: tall portrait, 2:3. The [subject] sits in the middle of the
image, slightly below centre. The top third is open, empty sky with almost
nothing in it, because a title will go there. The bottom sixth is plain
ground with little detail, because a small emblem will go there. No other
objects, no people [unless the subject is a person], no animals.
```

Style:

```
Style: 19th-century steel engraving, light and open: fine black ink linework
with sparing cross-hatching, mostly white paper, shading only where needed to
show form, in the manner of Victorian book illustration, black ink on plain
white paper, crisp lines. No colour, no grey wash, no glow, no paper texture,
no vignette shading, no border, no text, no signature.
```

If it comes back heavy: add "lightly drawn, at least two-thirds of the image
white paper". Light, fire and smoke: "drawn only with fine engraved lines,
the paper left white at its centre".

## Prompts that were used

**All of Grace** (Spurgeon ch. 1: "a fountain by the wayside ... a cup near
to it by a little chain"):

```
A humble Victorian wayside drinking fountain set into an old stone wall beside
a dusty country road: a plain stone basin with a simple carved surround, a
spout pouring a thin, steady stream of clear water into the basin, which is
brimming and running over its lip. An iron drinking cup hangs beside the spout
on a little chain, waiting. A hot, still summer day, strong sunlight and short
shadows; a few weeds and wildflowers at the foot of the wall; the road
stretching away behind into the distance. No people.
```
(It came back with mismatched pillars; one edit: "Make the two stone pillars
on either side of the arched niche identical in height and width, with their
capitals level, and the arch springing evenly from both. Change nothing
else.")

**Precious Remedies** (Brooks: "the shield of faith, whereby you shall be
able to quench all the fiery darts of the devil"), the version that worked
after two too busy:

```
A plain kite-shaped shield standing upright on its own, its point set into
bare ground, its face bearing a simple cross. A single arrow is stuck in the
face of the shield, its head buried in the wood, its feathers outward; the
fire on it has gone out, and one thin thread of smoke rises from where it
struck, straight up into still air. The shield is old and worn but whole: a
few scratches, no holes, no cracks. Nothing else: no other arrows, no rocks,
no figures. Still, quiet, the moment after: the dart quenched, the shield
unmoved.
```

**Pilgrim's Progress** (the opening: rags, book, burden; "Do you see yonder
shining light?"):

```
A lone man seen from behind, standing at the near edge of a very wide, open
field: he is clothed in rags, a book open in one hand, and a great burden
bound upon his back, heavy enough to bow his shoulders. His face is turned
away from us and from a small, poor house and cottage roofs just behind him at
the far left edge. Across the field, very far off on the low horizon, stands
a small wicket gate in a long hedge, and above it a single shining light,
drawn as fine rays of engraved lines spreading softly through the sky. A
faint footpath leads from his feet toward it. Vast, quiet, hopeful: the whole
journey ahead of him.
```
(Check: the burden must be a roped bundle, not a backpack; no second figure.)

## Marks and devices: woodcut, not engraving

Fine hatching fills in at a quarter inch, so the press's marks are woodcut
weight: white cut from a solid black roundel, few bold shapes, water as solid
bands, never dashes ("dashes read as a sprinkler"; a plain post with knobs
read as a fire hydrant). No lettering in the image; words are set in type.
The seal that was chosen:

```
A printer's device in the manner of 16th-century woodcut printers' marks: a
solid black roundel with a white fountain cut out of it, perfectly
symmetrical, seen straight on. A wide, shallow lower basin on a short
pedestal; a stout baluster column rising from its centre to a small upper
bowl. From the top a single jet of water rises and falls back in two smooth,
solid, unbroken streams, one to each side, curving down into the lower
basin. A plain cup hangs on a short chain from the centre of the lower
basin's front rim, directly below the column. A thin white ring just inside
the edge of the black roundel.

Few, bold shapes with plenty of black between them; the water drawn as
solid white bands, never dashes, drops or dotted lines. It must read clearly
as a fountain when printed a quarter of an inch tall.

Style: hand-cut woodcut, white cut out of solid black, with the slightly
irregular edges of a cutting knife; only a few cut lines of shading on the
bowls. Pure black and white, no grey, no gradients, no hatching, no
stippling, no texture. No text, letters, banners, people, animals or faces.
```

To keep a second image matching the first (the device's fountain), upload
the first with the prompt: "Using the fountain in the attached image as the
model ...". Pure black-and-white marks trace cleanly:
`magick IN -colorspace gray -filter Lanczos -resize 300% -blur 0x1.2 -threshold 50% bw.pbm`
then `potrace -s --turdsize 20 --alphamax 1.1 --opttolerance 0.3`.
