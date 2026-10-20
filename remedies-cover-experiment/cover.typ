#import "engraved_cover.typ": *

// Precious Remedies Against Satan's Devices in the engraved design: a mock-up
// after "Precious Remedies Vintage Book Wrap.png", with its art cut from
// "Engraved Swords and Serpent Relic.png" (art/, made by extract.py).  The
// back's passages are Brooks's own, from this edition: the Epistle
// Dedicatory and A Word to the Reader.
//
//   typst compile --root .. --font-path fonts cover.typ
#engraved-cover(
  author: [Thomas Brooks],
  spine-author: [Brooks],
  title: [Precious \ Remedies],
  title-rest: [Against \ Satan’s Devices],
  spine-rest: [Against \ Satan’s \ Devices],
  subtitle: [Or, Salve for Believers’ and Unbelievers’ Sores],
  // Brooks's emblem is still to be drawn: the placeholder ornament stands in
  spine-art: image("art/sword.png"),
  engraving: image("art/vignette.png"),
  pages: 354,
  back-heading: [The Epistle Dedicatory],
  back-passage: ([C], [hrist, the Scripture, your own hearts, and Satan’s
    devices, are the four prime things that should be first and most studied
    and searched; if any cast off the study of these, they cannot be safe here,
    nor happy hereafter. ’Tis my work as a Christian, but much more as I am a
    _watchman,_ to do my best, to discover the fulness of Christ, the
    emptiness of the creature, and the snares of the great deceiver.]),
  back-quote: [’Tis not hasty reading, but serious meditating upon holy and
    heavenly truths, that makes them prove sweet and profitable to the soul.],
  back-quote-source: [A Word to the Reader],
  back-about: [First published in 1652, Brooks’s best-loved book lays open the
    devices by which Satan draws the soul to sin, keeps it from holy duties,
    and holds it in a sad and doubting condition, and sets against each the
    remedies of Scripture.],
)
