// How this book sets its speeches and Scripture proofs.
//
// colophon writes each confession paragraph, catechism question and answer
// as #speech[#smallcaps[Paragraph 1]: ... #footnote[proofs] ...] (the TEI
// keeps each proof as a note after the words it proves). Every chapter file
// imports these two in place of Typst's own (TYPST_PREAMBLE), so the book
// prints as it always has: the label in bold, a bold number after each
// proved clause, and the proofs as a numbered list under the paragraph or
// answer, which is kept on one page when it fits (but for a chapter's first
// paragraph, which may run on rather than leave the heading alone on its
// page). In the catechisms a thin rule closes each answer.
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

#let speech(body) = {
  _proofs.update(())
  _turn.update(n => n + 1)
  let whole = {
    show smallcaps: it => strong(it.body)
    par(first-line-indent: 0pt, hanging-indent: 0pt, body)
    context {
      let ps = _proofs.get()
      if ps.len() > 0 { enum(..ps) }
      if _catechism.get() and calc.even(_turn.get()) { line(length: 100%, stroke: 0.02em) }
    }
  }
  // kept on one page when it fits; a speech longer than a page breaks, and
  // so may the first after a chapter heading
  layout(size => {
    let h = measure(block(width: size.width, whole)).height
    block(breakable: h > size.height or _first.get(), whole)
  })
  _first.update(false)
}
