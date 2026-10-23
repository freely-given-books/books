// How this book sets its speeches and Scripture proofs.
//
// colophon writes each confession paragraph, catechism question and answer
// as #speech[#smallcaps[Paragraph 1]: ... #footnote[proofs] ...] (the TEI
// keeps each proof as a note after the words it proves). Every chapter file
// imports these two in place of Typst's own (TYPST_PREAMBLE). The book's own
// design (2026-10-23): a confession paragraph opens with its bold number
// ("1."), catechism labels are bold small capitals, a bold number follows
// each proved clause, and the proofs run together in one small block under
// the paragraph or answer, short enough that a speech is kept whole on one
// page when it fits (but for a chapter's first paragraph, which may run on
// rather than leave the heading alone on its page). In the catechisms a
// question is kept with its answer, and a small diamond closes each answer.
//
// The ebook and the web pages read the TEI, not this file: there the proofs
// are the usual pop-up notes.

#let _proofs = state("lbcf-proofs", ())
#let _catechism = state("lbcf-catechism", false)
#let _turn = state("lbcf-turn", 0)
#let _first = state("lbcf-first", false)

// A chapter heading (the main file shows each with this after it): the
// speech after it may break.
#let chapter-start = _first.update(true)

// The catechisms (the main file switches this on before them): speeches
// come in pairs, question then answer, and a rule follows each answer.
#let catechism(on) = { _catechism.update(on); _turn.update(0) }

// A proof: its number in the text now, its references after the speech.
#let footnote(body) = {
  _proofs.update(p => p + (body,))
  context super(text(weight: "bold", str(_proofs.get().len())))
}

// "Paragraph 1:" opening a speech becomes a bold "1." as the 1677 printing
// numbers them; a catechism's labels stay, in bold small capitals.
#let _label(body) = {
  if not body.has("children") or body.children.len() < 2 { return body }
  let (first, ..rest) = body.children
  if first.func() != smallcaps or not first.body.has("text") { return body }
  let m = first.body.text.match(regex("^Paragraph (\d+)$"))
  if m == none { return body }
  // drop the colon after the label
  let (next, ..tail) = rest
  let next = if next.has("text") { text(next.text.trim(":", at: start).trim(at: start)) } else { next }
  strong(m.captures.at(0) + ".") + h(0.45em) + next + tail.join()
}

// The proofs: one small justified block under a short rule, each reference
// after its bold number, run together, so a speech and its proofs stay short
// enough to keep whole.
#let _proof-block(ps) = block(above: 0.75em, below: 0.3em, {
  line(length: 0.7in, stroke: 0.4pt + luma(40%))
  v(0.15em)
  set text(size: 8.5pt)
  set par(justify: true, leading: 0.5em)
  ps.enumerate().map(((i, p)) => text(weight: "bold", str(i + 1)) + sym.space.nobreak + p)
    .join(h(0.9em, weak: true) + sym.zws)
})

#let speech(body) = {
  _proofs.update(())
  _turn.update(n => n + 1)
  let whole = {
    show smallcaps: it => strong(it)
    par(first-line-indent: 0pt, hanging-indent: 0pt, _label(body))
    context {
      let ps = _proofs.get()
      if ps.len() > 0 { _proof-block(ps) }
      if _catechism.get() and calc.even(_turn.get()) {
        // placed, not set as a paragraph, so it sits on the column's centre
        v(0.3em)
        block(width: 100%, height: 7pt, place(top + center, text(7pt, fill: luma(45%), sym.diamond.filled)))
      }
    }
  }
  // kept on one page when it fits; a speech longer than a page breaks, and
  // so may the first after a chapter heading
  // (a question is sticky outside the layout, which would hide it)
  context block(below: 1.1em, sticky: _catechism.get() and calc.odd(_turn.get()),
    layout(size => {
      let h = measure(block(width: size.width, whole)).height
      block(breakable: h > size.height or _first.get(), whole)
    }))
  _first.update(false)
}
