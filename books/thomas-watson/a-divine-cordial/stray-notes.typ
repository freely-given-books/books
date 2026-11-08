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
//   "h-" / "h--" / "h---"   4 / 8 / 12pt less space above the heading
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
  // section headings only: a chapter heading starts its own page already,
  // and a page break put before it here would leave its place (contents,
  // bookmark, running head) on the page before (vol. III p. 105)
  show heading: it => if it.level < 3 or it.at("label", default: none) == <bookmark-only> { it } else { context {
    let n = counter(footnote).get().first() + 1
    let k = fixes.at(str(n), default: none)
    // a note set with its own mark (*) is not counted, so the headings
    // around one share n: it is the one nearest the note's
    if k != none {
      let nh = query(selector(heading).after(here(), inclusive: false))
        .filter(h => h.at("label", default: none) != <bookmark-only>)
      if (nh.len() > 0 and counter(footnote).at(nh.first().location()).first() + 1 == n and
          query(selector(footnote).after(here()).before(nh.first().location()))
            .any(f => type(f.numbering) == function)) { k = none }
    }
    if k == "b" { pagebreak(weak: true) + it }
    else if k == "h-" { v(-4pt) + it }
    else if k == "h--" { v(-8pt) + it }
    else if k == "h---" { v(-12pt) + it }
    else { it }
  } }
  body
}

// Breaks kept tidy where no note can key a lever (the typesetting report of
// 2026-11-03): a section heading left with one line under it at a page's
// foot, a paragraph's last word or two alone at the next page's head. Keyed
// by a phrase of the heading's or paragraph's own words (as set, notes left
// out); the levers are keep-notes' ("b", "s-", "t+", ...), and "k": keep the
// paragraph's lines together (no line of it alone at a page's foot or head).
// Used as  #show: keep-text.with((("§. 38. Of the Churches"): "b", ...))
#let _plain(c) = {
  if type(c) == str { return c }
  if type(c) != content { return "" }
  if c.func() == footnote { return "" }
  if c == [ ] { return " " }
  if c.has("text") { return if type(c.text) == str { c.text } else { "" } }
  if c.has("children") { return c.children.map(_plain).join("") }
  if c.has("body") { return _plain(c.body) }
  if c.has("child") { return _plain(c.child) }
  ""
}
#let keep-text(fixes, body) = {
  let kind(c) = {
    let t = _plain(c)
    for (phrase, k) in fixes { if t.contains(phrase) { return k } }
    none
  }
  show par: it => {
    let k = kind(it.body)
    if k == none { it }
    else if k == "w" { set text(costs: (widow: 0%, orphan: 0%)); it }
    else if k == "s-" { set text(spacing: 90%); it }
    else if k == "s+" { set text(spacing: 112%); it }
    else if k == "s--" { set text(spacing: 80%); it }
    else if k == "s++" { set text(spacing: 125%); it }
    else if k == "t-" { set text(tracking: -0.01em); it }
    else if k == "t+" { set text(tracking: 0.01em); it }
    else if k == "ts-" { set text(tracking: -0.01em, spacing: 90%); it }
    else if k == "ts+" { set text(tracking: 0.01em, spacing: 112%); it }
    else if k == "k" { set text(costs: (widow: 1000%, orphan: 1000%)); it }
    else { it }
  }
  // a block set off (a proposition) or a list item, whose words are not a
  // paragraph of their own
  let lever(k, it) = {
    if k == "s-" { set text(spacing: 90%); it }
    else if k == "s+" { set text(spacing: 112%); it }
    else if k == "t-" { set text(tracking: -0.01em); it }
    else if k == "t+" { set text(tracking: 0.01em); it }
    else if k == "ts-" { set text(tracking: -0.01em, spacing: 90%); it }
    else if k == "ts+" { set text(tracking: 0.01em, spacing: 112%); it }
    else if k == "k" { set text(costs: (widow: 1000%, orphan: 1000%)); it }
    else { it }
  }
  show block: it => { let k = kind(it.body); if k == none or k == "b" { it } else { lever(k, it) } }
  show enum.item: it => { let k = kind(it.body); if k == none or k == "b" { it } else { lever(k, it) } }
  show list.item: it => { let k = kind(it.body); if k == none or k == "b" { it } else { lever(k, it) } }
  show heading: it => if it.level < 3 or it.at("label", default: none) == <bookmark-only> { it } else {
    let k = kind(it.body)
    if k == "b" { pagebreak(weak: true) + it } else { it }
  }
  body
}
