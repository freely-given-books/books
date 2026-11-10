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

// a printed figure opening a point: 1.  (1.)  [1.]  1st.  (1st.) (Goold's marks; Watson's 1.)
#let FIGURE = regex("^([(\\[])?(\\d{1,2})(st|nd|rd|th|d)?\\.([)\\]])?(\\s|,|$)")
// the level a figure's shape names, as Goold marks his levels
#let figure-level(m) = {
  let (open, _, sfx, ..) = m.captures
  if sfx != none { if open == "(" { 4 } else { 3 } }
  else if open == "(" { 1 } else if open == "[" { 2 } else { 0 }
}
#let fresh = [#metadata(none)<omark>]     // put before a made paragraph: not taken again

#let opening(body) = {
  let lead = lead-text(body).trim()
  let w = lead.match(regex("^(\\w+)[,.:;]"))
  if w != none and (lower(w.captures.at(0)) in ORDINALS or lower(w.captures.at(0)) == "lastly") {
    ("word", w.captures.at(0))
  } else {
    let f = lead.match(FIGURE)
    if f != none { ("figure", f) } else { none }
  }
}

// a little space before a point (beyond the paragraph spacing), then the paragraph
#let spaced(level, content) = { context v(par.spacing + space-before.at(calc.min(level, 4)), weak: true); content }

#let plain-par(body) = par(first-line-indent: (amount: 12pt, all: true), fresh + body)

// One paragraph's body; `level` from its set-in distance, or none for a top-level paragraph.
//   an ordinal word: a grey mark before it naming the level (the top level's word in small caps);
//   a figure: at a set-in level, a plain 1. restyled to the level's shape (Watson's figures);
//     otherwise the level its shape names (Goold's marks) - and the space before the point.
#let point(level, body, original: none) = {
  let o = opening(body)
  if o == none { return plain-par(body) }
  if o.at(0) == "figure" {
    let f = o.at(1)
    let shaped = f.captures.at(0) != none or f.captures.at(2) != none
    let lv = if level == none or shaped { figure-level(f) } else { level }
    if level != none and not shaped and level > 0 {
      let n = int(f.captures.at(1))
      return spaced(lv, {
        show regex("^\\d{1,2}\\.(\\s|,|$)"): it => mark-text(lv, n) + it.text.slice(it.text.position(".") + 1)
        plain-par(body)
      })
    }
    return spaced(lv, if original != none { original } else { plain-par(body) })
  }
  let word = o.at(1)
  let key = lower(word)
  let lv = if level == none { 0 } else { level }
  let k = calc.min(lv, 4)
  let num = c => if key == "lastly" { c.at(k) + 1 } else { ORDINALS.at(key) }
  show regex("^(?i:" + word + ")"): it => if lv == 0 { smallcaps(it) } else { it }
  spaced(lv, par(first-line-indent: (amount: 12pt, all: true),
    [#box(text(fill: luma(90), context mark-text(lv, num(counts.get()))))<omark>] + h(0.35em) + body))
  counts.update(c => {
    let n = if key == "lastly" { c.at(k) + 1 } else { ORDINALS.at(key) }
    let out = c
    out.at(k) = n
    for j in range(k + 1, 5) { out.at(j) = 0 }
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
  // a top-level paragraph that opens with an ordinal or a figure (a made paragraph opens
  // with a mark or `fresh`, so it is not taken again)
  show par: it => if opening(it.body) != none { point(none, it.body, original: it) } else { it }
  doc
}
