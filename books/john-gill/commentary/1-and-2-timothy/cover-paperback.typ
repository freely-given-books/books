#import "cover.typ": *

// Page count comes from the compiled interior; rerun the build after the
// interior changes length, or the spine will be wrong.
#cover(
  book: [1 & 2 Timothy],
  subtitle: [The Epistles of Paul the Apostle to Timothy],
  volume: none,
  pages: 216,
  division: "epistles",
  binding: "paperback",
  contents: [1 Timothy · 2 Timothy],
  // Uncomment once the volume has an ISBN; this adds the barcode field the
  // printer needs to the back cover.
  // isbn: "978-0-000000-00-0",
  epigraph: [
    All Scripture is given by inspiration of God, and is profitable for
    doctrine, for reproof, for correction, for instruction in righteousness.
  ],
  epigraph-source: [2 Timothy 3:16],
)
