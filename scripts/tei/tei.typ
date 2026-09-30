// tei.typ — typeset an (enriched) EEBO-TCP TEI file directly in Typst.
//
//   #import "tei.typ": tei-division, tei-book
//   #let ed = xml("source/christian-economy.tei.xml")
//
//   #tei-division(ed, "dedication")          // modern reading text
//   #tei-division(ed, 1)                     // chapter 1
//   #tei-division(ed, 1, layer: "orig")      // as printed in 1609
//   #tei-book(ed, layer: "reg")              // dedication + all chapters
//
// Options (all functions):
//   layer:          "reg" (modern reading, default) or "orig" (as printed)
//   expand:         orig layer only — show abbreviations expanded (fro̅ -> from)
//   mark-supplied:  wrap letters reconstructed from illegible print in ⟨ ⟩
//   show-gaps:      orig layer only — show illegible print as transcribed (•)
//   only-auto:      reg layer only — ignore the editor's decisions (audit view)
//   heading-level:  level for division headings (default 2)
//
// Pass the parsed XML (not the path): Typst resolves paths relative to the
// file that calls xml(), so the book file should load it.

#let _is-el(n) = type(n) == dictionary
#let _kids(n, tag) = n.children.filter(c => _is-el(c) and c.tag == tag)
#let _first(n, tag) = {
  let k = _kids(n, tag)
  if k.len() > 0 { k.at(0) } else { none }
}
#let _text-of(n) = n.children.filter(c => type(c) == str).join(default: "")

#let _defaults = (
  layer: "reg", expand: false, mark-supplied: false, show-gaps: false,
  only-auto: false, heading-level: 2, numbered: false,
)

// ---------------------------------------------------------------------------
// Inline content is built as an array of pieces (strings and content) so
// that whitespace can be collapsed across element boundaries.
// ---------------------------------------------------------------------------

#let _norm(pieces) = {
  let out = ()
  let buf = ""
  let last-space = true
  for p in pieces {
    if type(p) == str {
      buf += p
    } else if p != none {
      if buf != "" {
        let s = buf.replace(regex("\s+"), " ").replace(regex("(\w)'"), m => m.captures.at(0) + "’")
        if last-space and s.starts-with(" ") { s = s.slice(1) }
        if s != "" {
          out.push(s)
          last-space = s.ends-with(" ")
        }
        buf = ""
      }
      out.push(p)
      last-space = false
    }
  }
  if buf != "" {
    let s = buf.replace(regex("\s+"), " ").replace(regex("(\w)'"), m => m.captures.at(0) + "’")
    if last-space and s.starts-with(" ") { s = s.slice(1) }
    if s != "" { out.push(s) }
  }
  // trim trailing space
  if out.len() > 0 and type(out.last()) == str {
    let s = out.pop().trim(at: end)
    if s != "" { out.push(s) }
  }
  out
}

#let _join(pieces) = {
  let ps = _norm(pieces)
  if ps.len() == 0 { [] } else { ps.map(p => if type(p) == str [#p] else { p }).join() }
}

#let _inline(n, o) = {
  if type(n) == str { return (n,) }
  if not _is-el(n) { return () }
  let t = n.tag
  let children(o2: o) = {
    let cs = n.children
    let rs = cs.map(c => _inline(c, o2))
    let ps = ()
    for (i, c) in cs.enumerate() {
      let r = rs.at(i)
      if _is-el(c) and c.tag == "note" and r.len() > 0 {
        // what precedes: did the source have a space before the anchor?
        let before = ps.filter(x => type(x) == str).join(default: "")
        let spaced = before.match(regex("\s$")) != none
        // like Typst markup, no space before the footnote mark
        if ps.len() > 0 and type(ps.last()) == str { ps.push(ps.pop().trim(at: end)) }
        ps += r
        // footnote anchored between two words: keep the words apart
        let rest = rs.slice(i + 1).flatten()
        let nxt = rest.at(0, default: none)
        if spaced and type(nxt) == str and nxt.len() > 0 and nxt.first().match(regex("\w")) != none {
          ps.push(" ")
        }
      } else {
        ps += r
      }
    }
    ps
  }
  if t == "choice" {
    let orig = _first(n, "orig")
    let regs = _kids(n, "reg")
    let abbr = _first(n, "abbr")
    let expan = _first(n, "expan")
    if orig != none and regs.len() > 0 {
      if o.layer == "reg" {
        let ed = regs.filter(r => r.attrs.at("resp", default: "") == "#editor")
        let au = regs.filter(r => r.attrs.at("resp", default: "") == "#auto")
        if o.only-auto {
          if au.len() > 0 { return (_text-of(au.at(0)),) }
          return _inline(orig, o)
        }
        let pick = if ed.len() > 0 { ed.at(0) } else if au.len() > 0 { au.at(0) } else { regs.at(0) }
        return (_text-of(pick),)
      }
      return _inline(orig, o)
    }
    if abbr != none and expan != none {
      if o.layer == "reg" or o.expand { return (_text-of(expan),) }
      return _inline(abbr, o)
    }
    return children()
  }
  if t == "orig" or t == "abbr" or t == "seg" or t == "q" or t == "bibl" { return children() }
  if t == "supplied" {
    if o.show-gaps and o.layer == "orig" {
      let g = _first(n, "gap")
      if g != none { return _inline(g, o) }
    }
    let s = _text-of(n).trim()
    return (if o.mark-supplied { "⟨" + s + "⟩" } else { s },)
  }
  if t == "gap" {
    if n.attrs.at("reason", default: "") == "duplicate" { return () }
    let d = _first(n, "desc")
    return (if d != none { _text-of(d) } else { "•" },)
  }
  if t == "g" {
    let ref = n.attrs.at("ref", default: "")
    if ref == "char:EOLhyphen" or ref == "char:EOLunhyphen" { return () }
    if ref == "char:abque" { return ("ꝗ",) }
    return (_text-of(n),)
  }
  if t == "hi" {
    let inner = children()
    let flat = inner.filter(x => type(x) == str).join(default: "")
    let lead = if inner.len() > 0 and type(inner.first()) == str and inner.first().match(regex("^\s")) != none { " " } else { "" }
    let trail = if inner.len() > 0 and type(inner.last()) == str and inner.last().match(regex("\s$")) != none { " " } else { "" }
    let body = _join(inner)
    if n.attrs.at("rend", default: "") == "sup" { return (super(body),) }
    return (lead, emph(body), trail)
  }
  if t == "note" {
    let body = _join(children())
    return (footnote(body),)
  }
  if t == "label" {
    if o.layer == "reg" and o.numbered { return () }
    return children()
  }
  if t == "expan" {
    if o.layer == "orig" and not o.expand {
      let am = _first(n, "am")
      return if am != none { am.children.filter(_is-el).map(c => _inline(c, o)).flatten() } else { () }
    }
    let ex = _first(n, "ex")
    return (if ex != none { _text-of(ex) } else { "" },)
  }
  if t == "am" { return children() }
  if t in ("pb", "lb", "milestone", "fw", "desc") { return () }
  children()
}

#let _para(n, o) = _join(_inline(n, o))

// Item text (without nested lists) and its nested lists.
#let _item-parts(item, o) = {
  let is-list(c) = _is-el(c) and c.tag == "list"
  let body = (tag: "item-body", attrs: (:), children: item.children.filter(c => not is-list(c)))
  (text: _norm(_inline(body, o)), subs: item.children.filter(is-list))
}

#let _bullets(lst, o) = {
  // An item holding only a nested list continues the previous item.
  let entries = ()
  for item in _kids(lst, "item") {
    let parts = _item-parts(item, o)
    if parts.text.len() > 0 {
      entries.push((body: _join(parts.text), subs: parts.subs))
    } else if entries.len() > 0 {
      let e = entries.pop()
      e.subs += parts.subs
      entries.push(e)
    } else {
      entries.push((body: [], subs: parts.subs))
    }
  }
  list(..entries.map(e => [#e.body#for s in e.subs { _bullets(s, o) }]))
}

#let _list(lst, o) = {
  let head = _first(lst, "head")
  let numbered = lst.attrs.at("type", default: "") == "numbered"
  let oo = o + (numbered: numbered)
  let out = []
  if head != none { out += [#strong(_para(head, o))] + parbreak() }
  if numbered {
    let items = _kids(lst, "item").map(i => _join(_item-parts(i, oo).text))
    if o.layer == "reg" {
      out += enum(numbering: "I.", ..items)
    } else {
      for i in items { out += i + parbreak() }
    }
  } else {
    out += _bullets(lst, o)
  }
  out
}

#let _closer(c, o) = {
  let signed = _first(c, "signed")
  if signed == none { return [] }
  let his = _kids(signed, "hi")
  if his.len() == 0 { return align(right, _para(signed, o)) }
  let last = his.last()
  let before = (tag: "signed", attrs: (:), children: ())
  for ch in signed.children {
    if ch == last { break }
    before.children.push(ch)
  }
  linebreak() + linebreak() + parbreak()
  align(left, _para(before, o)) + parbreak()
  align(right, _join(_inline(last, o)))
}

#let _blocks(div, o) = {
  let out = []
  for c in div.children.filter(_is-el) {
    let t = c.tag
    if t == "head" or t == "pb" { continue }
    if t == "p" {
      out += _para(c, o) + parbreak()
    } else if t == "list" {
      out += _list(c, o) + parbreak()
    } else if t == "closer" {
      out += _closer(c, o)
    } else if t == "trailer" {
      if o.layer == "orig" { out += align(center, _para(c, o)) + parbreak() }
    } else if t == "div" {
      out += _blocks(c, o)
    } else {
      out += _para(c, o) + parbreak()
    }
  }
  out
}

#let _heading(div, o) = {
  let heads = _kids(div, "head")
  let lvl = o.heading-level
  if div.attrs.at("type", default: "") == "chapter" {
    let sub = heads.find(h => h.attrs.at("type", default: "") == "sub")
    let first = heads.find(h => "type" not in h.attrs)
    if o.layer == "reg" {
      let s = _norm(_inline(sub, o))
      if s.len() > 0 and type(s.last()) == str {
        let l = s.pop()
        s.push(l.trim(".", at: end))
      }
      return heading(level: lvl)[#div.attrs.n. #_join(s)]
    }
    return heading(level: lvl, _para(first, o)) + emph(_para(sub, o)) + parbreak()
  }
  let ed = heads.find(h => h.attrs.at("type", default: "") == "edition")
  let printed = heads.find(h => "type" not in h.attrs)
  let h = if o.layer == "reg" and ed != none { ed } else { printed }
  if h == none { [] } else { heading(level: lvl, _para(h, o)) }
}

#let _root(doc) = if type(doc) == array { doc.find(_is-el) } else { doc }

#let _find-divs(n) = {
  if not _is-el(n) { return () }
  if n.tag == "div" and n.attrs.at("type", default: "") in ("dedication", "chapter") { return (n,) }
  n.children.map(_find-divs).flatten()
}

#let _divisions(doc) = _find-divs(_root(doc))

/// One division: "dedication" or a chapter number.
#let tei-division(doc, which, ..opts) = {
  let o = _defaults + opts.named()
  let div = _divisions(doc).find(d => if which == "dedication" {
    d.attrs.at("type", default: "") == "dedication"
  } else {
    d.attrs.at("type", default: "") == "chapter" and d.attrs.at("n", default: "") == str(which)
  })
  if div == none { panic("no division " + repr(which)) }
  _heading(div, o)
  _blocks(div, o)
}

/// Dedication and every chapter, in order.
#let tei-book(doc, ..opts) = {
  let o = _defaults + opts.named()
  for div in _divisions(doc) {
    _heading(div, o)
    _blocks(div, o)
  }
}
