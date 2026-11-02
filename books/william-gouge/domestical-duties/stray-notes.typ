// Footnotes kept on their marker's page. Typst can set a note and then carry
// its marker's line to the next page (widow control, a heading kept with its
// text), or push a note on past a full page, so note and mark part. A volume
// lists, by the number of the first footnote in it, each paragraph or heading
// to set differently so they stay together (found by trying, after the
// pages are made; print_check.py reports what is left):
//   "w"   the paragraph may leave one line alone at a page's foot or head
//   "s-" / "s+" / "s--" / "s++"   its word spacing 90 / 112 / 80 / 125%
//   "ws-" / "ws+"   both
//   "t-" / "t+"   its letter spacing -/+0.01em
//   "b"   the heading starts a new page (keyed by the first note after it)
// Used as  #show: keep-notes.with((("277"): "w", ...))  after book.with.

// the numbers of the footnote marks in a paragraph as laid out: each mark is
// a styled group (tag, number, tag)
#let _marks(c) = {
  if type(c) != content { return () }
  if c.has("child") {
    let k = c.child
    if k.has("children") and k.children.len() == 3 and k.children.at(1).has("text") {
      return (k.children.at(1).text,)
    }
    return _marks(k)
  }
  let out = ()
  if c.has("children") { for x in c.children { out += _marks(x) } }
  if c.has("body") { out += _marks(c.body) }
  out
}

#let keep-notes(fixes, body) = {
  let kind(marks) = {
    for (n, k) in fixes { if n in marks { return k } }
    none
  }
  show par: it => {
    let k = kind(_marks(it.body))
    if k == none { it }
    else if k == "w" { set text(costs: (widow: 0%, orphan: 0%)); it }
    else if k == "s-" { set text(spacing: 90%); it }
    else if k == "s+" { set text(spacing: 112%); it }
    else if k == "s--" { set text(spacing: 80%); it }
    else if k == "s++" { set text(spacing: 125%); it }
    else if k == "ws-" { set text(spacing: 90%, costs: (widow: 0%, orphan: 0%)); it }
    else if k == "ws+" { set text(spacing: 112%, costs: (widow: 0%, orphan: 0%)); it }
    else if k == "t-" { set text(tracking: -0.01em); it }
    else if k == "t+" { set text(tracking: 0.01em); it }
    else { it }
  }
  show heading: it => context {
    let n = str(counter(footnote).get().first() + 1)
    if fixes.at(n, default: none) == "b" { pagebreak(weak: true) + it } else { it }
  }
  body
}
