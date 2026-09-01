// A template for verse-by-verse Scripture commentary, set for 6x9in print.
//
// The shape of a commentary is unlike a treatise: the reader arrives looking
// for one verse rather than reading front to back.  So the text is broken by
// verse rather than by argument, every verse carries its own reference and the
// text of Scripture itself, and the running head on each recto names the
// verses opened on that page.
//
//   #show: commentary.with(title: [...], book-name: [...], ...)
//   #part[1 Timothy]
//   #section[Introduction]
//   #chapter(2)
//   #verse(2, 14)[Of these things put them in remembrance...]
//   #superscription[A Psalm of David.]
//   #lemma[Of these things put them in remembrance,] Meaning either...
//   #citation[The word "gangrene" is Greek...]

#let rule-colour = luma(45%)

// A verse number set inside a block that carries more than one verse.
#let vn(number) = super(text(size: 0.9em, weight: 700)[#number])

// Records where each verse begins so the running heads can find it.
#let verse(chapter, first, body, last: none) = {
  [#metadata((chapter, first, if last == none { first } else { last })) <verse-mark>]
  let reference = if last == none [#chapter:#first] else [#chapter:#first#sym.dash.en#last]
  block(
    breakable: false,
    // Keep the verse with the comment on it; a reader should never have to
    // turn the page to find out what Gill says about the text just quoted.
    sticky: true,
    width: 100%,
    above: 1.6em,
    below: 1.1em,
    grid(
      columns: (3.4em, 1fr),
      column-gutter: 0.7em,
      align(right + top, text(size: 9.5pt, weight: 700, reference)),
      block(
        stroke: (left: 0.7pt + rule-colour),
        inset: (left: 0.85em, y: 0.1em),
        text(size: 10pt, style: "italic", body),
      ),
    ),
  )
}

// A Hebrew superscription -- "A Psalm of David." -- which belongs to the text
// itself rather than to the translation.
#let superscription(body) = block(
  width: 100%,
  above: 1.6em,
  below: 0.2em,
  align(center, text(size: 9.5pt, style: "italic", body)),
)

// A divider the translation sets between verses, such as Psalm 119's acrostic
// letters.
#let kjvheading(body) = block(
  width: 100%,
  above: 1.8em,
  below: 0.6em,
  align(center, text(size: 10pt, tracking: 0.18em, smallcaps(body))),
)

// The slice of Scripture Gill is expounding, which opens each comment.
#let lemma(body) = strong(body)

// A quotation Gill sets off from his own prose (a Targum, the Apocrypha, and
// so on).
#let citation(body) = block(
  width: 100%,
  above: 1em,
  below: 1em,
  inset: (left: 1.2em, right: 1.2em),
  text(size: 9.8pt, body),
)

// One book of Scripture: a part page, and the name the running heads use.
#let part(name, subtitle: none) = [
  #heading(level: 1, numbering: none, outlined: true)[#name]
  #if subtitle != none [#metadata(subtitle) <part-subtitle>]
]

#let section(body) = [
  #heading(level: 2, numbering: none, outlined: true)[#body]
]

#let chapter(number) = section[Chapter #numbering("I", number)]

#let commentary(
  // The book's title, as it appears on the title page.
  title: [Commentary],
  subtitle: none,
  author: none,

  // Short form used in the verso running head.
  book-name: none,

  // Copyright and provenance, set at the foot of the second page.
  publishing-info: none,

  epigraph: none,

  page-width: 6in,
  page-height: 9in,
  page-margin: (top: 0.85in, bottom: 0.9in, inside: 0.9in, outside: 0.75in),

  body,
) = {
  set document(title: title, author: if author != none { author } else { () })
  set text(font: ("Libertinus Serif", "Liberation Serif"), size: 10.5pt)
  set page(width: page-width, height: page-height, margin: page-margin)

  let ornament = text(0.8em, tracking: 0.6em)[#sym.diamond.filled#sym.diamond.filled#sym.diamond.filled]

  // Title page.
  page(align(center + horizon, {
    ornament
    v(2.2em)
    text(15pt, tracking: 0.28em, upper[An Exposition of])
    v(1.4em)
    text(30pt, weight: 700, tracking: 0.06em, smallcaps(title))
    v(1.6em)
    line(length: 42%, stroke: 0.75pt)
    v(1.6em)
    if subtitle != none {
      text(1.1em, style: "italic", subtitle)
      v(2.2em)
    }
    text(0.9em, tracking: 0.3em, sym.diamond.filled)
    v(1.6em)
    if author != none {
      text(1.3em, tracking: 0.15em, smallcaps(author))
    }
    v(3em)
    ornament
  }))

  if publishing-info != none {
    align(center + bottom, text(0.8em, publishing-info))
  }
  pagebreak()

  if epigraph != none {
    v(22%)
    align(center, block(width: 78%, {
      set par(justify: false)
      text(size: 11pt, style: "italic", epigraph)
    }))
    pagebreak(to: "odd", weak: true)
  }

  // A comment runs on without indentation, so paragraphs are separated by
  // space instead -- which also sets each bold lemma off from the comment
  // above it.
  set par(justify: true, leading: 0.62em, spacing: 1.15em, first-line-indent: 0pt)

  // Contents.
  show outline.entry.where(level: 1): it => {
    let loc = it.element.location()
    v(1em)
    link(loc, text(1.1em, weight: 600, smallcaps(it.element.body)))
    box(width: 1fr)
    link(loc, text(1.1em, weight: 600, str(loc.page())))
    linebreak()
  }
  show outline.entry.where(level: 2): it => {
    let loc = it.element.location()
    pad(left: 1.4em, link(loc)[
      #it.element.body
      #box(width: 1fr, it.fill)
      #loc.page()
      #linebreak()
    ])
  }
  {
    v(4%)
    align(center, text(18pt, weight: 700, smallcaps[Contents]))
    v(2em)
    outline(title: none, depth: 2)
  }

  // Running heads.  The verso names the volume, the recto the book and verses
  // opened on the page -- what a reader thumbing for a reference needs.
  set page(header: context {
    let n = here().page()
    if query(heading).any(it => it.location().page() == n) {
      return
    }
    let marks = query(<verse-mark>)
    let on-page = marks.filter(it => it.location().page() == n)
    let earlier = marks.filter(it => it.location().page() < n)

    // A comment can run over a page break, in which case the verse it belongs
    // to is still open at the top of this page even though its mark is not
    // here.  Anything set more than a line or two below the top of the text
    // block has such a comment above it.
    let carried = if on-page.len() == 0 {
      earlier.at(-1, default: none)
    } else if earlier.len() > 0 and on-page.first().location().position().y > 1.5in {
      earlier.last()
    } else {
      none
    }

    let first = if carried != none { carried } else { on-page.at(0, default: none) }
    let last = if on-page.len() > 0 { on-page.last() } else { carried }

    let books = query(selector(heading.where(level: 1)).before(here()))
    let book = if books.len() > 0 { books.last().body }

    // Before the first verse -- in an introduction, say -- name the book alone.
    let label = if first == none {
      if book == none { return }
      book
    } else {
      let (c1, v1, ..) = first.value
      let (c2, .., v2) = last.value
      let dash = sym.dash.en
      let range = if c1 == c2 and v1 == v2 [#c1:#v1] else if c1 == c2 [#c1:#v1#dash#v2] else [#c1:#v1#dash#c2:#v2]
      if book == none { range } else [#book #range]
    }

    set text(9pt)
    grid(
      columns: (1fr, 8fr, 1fr),
      align: (left, center, right),
      if calc.even(n) [#n],
      if calc.even(n) { smallcaps(book-name) } else { smallcaps(label) },
      if calc.odd(n) [#n],
    )
    v(-0.45em)
    line(length: 100%, stroke: 0.5pt + rule-colour)
  })

  // A book of Scripture opens on its own page.
  show heading.where(level: 1): it => context {
    set text(weight: 400)
    pagebreak(to: "odd", weak: true)
    let subtitle = query(selector(<part-subtitle>).after(here())).at(0, default: none)
    v(1fr)
    align(center, {
      line(length: 32%, stroke: 0.75pt)
      v(1.1em)
      text(28pt, weight: 700, tracking: 0.1em, smallcaps(it.body))
      v(1.1em)
      line(length: 32%, stroke: 0.75pt)
      if subtitle != none {
        v(1.6em)
        text(11pt, style: "italic", subtitle.value)
      }
    })
    v(1fr)
    pagebreak(weak: true)
  }

  show heading.where(level: 2): it => {
    set text(weight: 400)
    pagebreak(weak: true)
    v(5%)
    align(center, {
      line(length: 30%, stroke: 0.75pt)
      v(0.9em)
      text(20pt, weight: 700, tracking: 0.12em, smallcaps(it.body))
      v(0.9em)
      line(length: 30%, stroke: 0.75pt)
    })
    v(2.2em)
  }

  set footnote.entry(separator: line(length: 30%, stroke: 0.5pt + rule-colour))
  show footnote.entry: set text(size: 8.5pt)
  show footnote.entry: set par(justify: true, leading: 0.5em, spacing: 0.6em)

  body
}
