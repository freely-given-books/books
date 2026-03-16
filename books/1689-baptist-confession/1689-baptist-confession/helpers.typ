// Scripture reference note markers (superscript numbers)
#let note(n) = super(text(weight: "bold", str(n)))

// Get current chapter short title for page headers
#let current-chapter-header() = context {
  let elems = query(selector(<short>).before(here()))
  if elems.len() > 0 {
    let last = elems.last()
    last.value
  }
}

// ============================================================================
// Utility functions
// ============================================================================

// Pad number to 2 digits
#let pad2(n) = {
  if n < 10 { "0" + str(n) } else { str(n) }
}

// Pad number to 3 digits
#let pad3(n) = {
  if n < 10 {
    "00" + str(n)
  } else if n >= 10 and n < 100 {
    "0" + str(n)
  } else {
    str(n)
  }
}

// ============================================================================
// Data paths
// ============================================================================

#let lbcf-data-path = "symbolics-data/confessions/lbcf1689"
#let bc1695-data-path = "symbolics-data/catechisms/bc1695"
#let aoc1680-data-path = "symbolics-data/catechisms/aoc1680"

// ============================================================================
// Generic rendering functions
// ============================================================================

// Build segment content and proofs from a list of segments
#let build-segments-and-proofs(segments) = {
  let segment-content = []
  let proofs-content = []
  let note-num = 0

  for segment in segments {
    let has-proofs = "proofs" in segment and segment.proofs != none and segment.proofs != ""
    if has-proofs {
      note-num += 1
      segment-content += [#segment.text#note(note-num)]
      proofs-content += [+ #segment.proofs]
    } else {
      segment-content += [#segment.text]
    }
  }

  (content: segment-content, proofs: proofs-content)
}

// Render a confession paragraph (LBCF style)
#let render-confession-paragraph(para) = {
  let result = build-segments-and-proofs(para.segments)

  block(breakable: false)[
    *Paragraph #para.paragraph.* #result.content

    #result.proofs
  ]
}

// Render a catechism question (BC 1695 / AOC 1680 style)
#let render-catechism-question(question) = {
  let result = build-segments-and-proofs(question.segments)

  block(breakable: false)[
    *Question #question.id - * #question.question

    *Answer:* #result.content

    #result.proofs
    #line(stroke: 0.02em)
  ]
}

// ============================================================================
// LBCF 1689 - London Baptist Confession of Faith
// ============================================================================

#let lbcf-load-paragraph(chapter-num, para-num) = {
  let para-path = lbcf-data-path + "/paragraphs/" + pad2(chapter-num) + "_" + pad2(para-num) + ".yml"
  yaml(para-path)
}

#let lbcf-chapter(chapter-num) = {
  let ch-path = lbcf-data-path + "/chapters/" + pad2(chapter-num) + ".yml"
  let ch = yaml(ch-path)

  let title = upper(ch.title)
  [== #chapter-num. #title]

  for para-num in range(1, ch.num_paragraphs + 1) {
    let para = lbcf-load-paragraph(chapter-num, para-num)
    render-confession-paragraph(para)
  }
}

#let lbcf-all-chapters() = {
  for ch-num in range(1, 33) {
    lbcf-chapter(ch-num)
  }
}

// ============================================================================
// BC 1695 - Baptist Catechism
// ============================================================================

#let bc1695-load-question(q-num) = {
  let q-path = bc1695-data-path + "/questions/" + pad3(q-num) + ".yml"
  yaml(q-path)
}

#let bc1695-question(q-num) = {
  let question = bc1695-load-question(q-num)
  render-catechism-question(question)
}

#let bc1695-all-questions() = {
  for q-num in range(1, 115) {
    bc1695-question(q-num)
  }
}

// ============================================================================
// AOC 1680 - An Orthodox Catechism
// ============================================================================

#let aoc1680-load-section(section-num) = {
  let s-path = aoc1680-data-path + "/sections/" + pad2(section-num) + ".yml"
  yaml(s-path)
}

#let aoc1680-load-question(q-num) = {
  let q-path = aoc1680-data-path + "/questions/" + pad3(q-num) + ".yml"
  yaml(q-path)
}

#let aoc1680-load-prose(name) = {
  let p-path = aoc1680-data-path + "/prose/" + name + ".md"
  read(p-path)
}

#let aoc1680-section(section-num) = {
  let section = aoc1680-load-section(section-num)
  [== #section.id. #section.title]
}

#let aoc1680-question(q-num) = {
  let question = aoc1680-load-question(q-num)
  render-catechism-question(question)
}

#let aoc1680-questions-in-range(start, end) = {
  for q-num in range(start, end + 1) {
    aoc1680-question(q-num)
  }
}

#let aoc1680-all-questions() = {
  let current-section = 0
  for q-num in range(1, 153) {
    let question = aoc1680-load-question(q-num)
    // Render section heading when parent changes
    if question.parent != current-section {
      current-section = question.parent
      let section = aoc1680-load-section(current-section)
      [== #section.id. #section.title]
    }
    render-catechism-question(question)
  }
}
