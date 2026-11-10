// Outline marks: a book's numbered points set full width, each with a mark that names
// its level (the editor's choice, 2026-11-09, for Owen's nested "First ... Secondly").
//
// The chapters keep their outline levels as colophon writes them (a set-in paragraph
// is `#pad(left: Xem)[#par(...)[...]]`, the TEI's p[@rend="levelN"]); this only changes
// how they are drawn, so chapters/typ and the TEI are untouched:
//   - every level shares the text's edge (no set-in column), a normal first-line indent;
//   - a paragraph that opens with an ordinal word ("First,", "Secondly,") gets a small
//     grey mark before it, by level: 1.  (1.)  [1.]  1st.  as Goold marked them;
//     at the top level the ordinal itself is set in small capitals;
//   - a little space before each numbered point: 6pt at the top level, 3pt below, 2pt deeper.
// The marks are the edition's, not the author's (his words are as printed); the ebook
// sets the same (colophon's outline_marks, ebook.css .omark).
//
// Use: `#import "../../../scripts/outline_marks.typ": outline-marks` and, after the
// book's `#show: book.with(...)`, `#show: outline-marks`.

#let ORDINALS = (
  "first": 1, "firstly": 1, "secondly": 2, "second": 2, "thirdly": 3, "third": 3,
  "fourthly": 4, "fourth": 4, "fifthly": 5, "fifth": 5, "sixthly": 6, "sixth": 6,
  "seventhly": 7, "seventh": 7, "eighthly": 8, "eightly": 8, "eighth": 8,
  "ninthly": 9, "ninth": 9, "tenthly": 10, "tenth": 10, "eleventhly": 11, "twelfthly": 12,
)

#let ordinal-suffix(n) = if calc.rem(calc.quo(n, 10), 10) == 1 { "th" } else {
  ("th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th").at(calc.rem(n, 10))
}

#let mark-text(level, n) = (
  str(n) + ".", "(" + str(n) + ".)", "[" + str(n) + ".]",
  str(n) + ordinal-suffix(n) + ".", "(" + str(n) + ordinal-suffix(n) + ".)",
).at(calc.min(level, 4))

#let space-before = (6pt, 3pt, 2pt, 2pt, 2pt)

// the plain text a piece of content begins with (enough to find its first word)
#let lead-text(c) = {
  if type(c) == str { c }
  else if c.at("label", default: none) == <omark> { "§" }     // already marked
  else if c.has("child") { lead-text(c.child) }
  else if c.has("text") { c.text }
  else if c.has("children") { c.children.slice(0, calc.min(6, c.children.len())).map(lead-text).join("") }
  else if c.has("body") { lead-text(c.body) }
  else if c == [ ] { " " }
  else { "" }
}

// set-in distance -> level: colophon's layout.level_em (2em a level to 3, then 1em)
#let em-level(em) = if em <= 0.1 { 0 } else if em <= 6.1 { int(calc.round(em / 2)) } else { 3 + int(calc.round(em - 6)) }

#let counts = state("outline-marks-counts", (0, 0, 0, 0, 0))

// One paragraph's body at a level: mark and space if it opens with an ordinal word.
#let point(level, body) = {
  let m = lead-text(body).trim().match(regex("^(\w+)[,.:;]"))
  let word = if m == none { none } else { m.captures.at(0) }
  let key = if word == none { none } else { lower(word) }
  if key == none or (key not in ORDINALS and key != "lastly") {
    return block(par(first-line-indent: (amount: 12pt, all: true), body))
  }
  context {
    let c = counts.get()
    let n = if key == "lastly" { c.at(calc.min(level, 4)) + 1 } else { ORDINALS.at(key) }
    // at the top level the ordinal itself in small capitals
    show regex("^(?i:" + word + ")"): it => if level == 0 { smallcaps(it) } else { it }
    block(above: par.spacing + space-before.at(calc.min(level, 4)), below: par.spacing,
      par(first-line-indent: (amount: 12pt, all: true),
        [#box(text(fill: luma(90), mark-text(level, n)))<omark>] + h(0.35em) + body))
  }
  counts.update(c => {
    let n = if key == "lastly" { c.at(calc.min(level, 4)) + 1 } else { ORDINALS.at(key) }
    let out = c
    out.at(calc.min(level, 4)) = n
    for k in range(calc.min(level, 4) + 1, 5) { out.at(k) = 0 }
    out
  })
}

#let outline-marks(doc) = {
  // a set-in paragraph: full width, its level from its distance
  show pad: it => {
    let lv = em-level(it.left.length.em)
    if lv == 0 or it.body.func() != par { return it }
    point(lv, it.body.body)
  }
  // a top-level paragraph that opens with an ordinal (its mark makes the made one open
  // with a digit or bracket, so it is not taken again)
  show par: it => {
    let m = lead-text(it.body).trim().match(regex("^(\w+)[,.:;]"))
    if m != none and (lower(m.captures.at(0)) in ORDINALS or lower(m.captures.at(0)) == "lastly") {
      point(0, it.body)
    } else { it }
  }
  doc
}
