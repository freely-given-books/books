"""A books release's downloads and covers into the R2 bucket the files Worker serves.

    python upload.py RELEASE_DIR [--prune] [--dry-run]

RELEASE_DIR holds the release's catalog.json and its .pdf, .epub, .png and .webp
files (gh release download TAG -p catalog.json -p '*.pdf' -p '*.epub' -p '*.png'
-p '*.webp'; the covers are the site's images, linked here by their names). Each
download goes up under its release name (the-book-v3.pdf), once: a name
never changes its bytes, so one already in the bucket is left alone. Each
print book also gets its print-ready zip (interior and cover, as a printer
takes them: the-book-v3-print-ready.zip), made here.

The bucket keeps each edition's current version and the one before it
(the editor, 2026-11-23). --prune deletes older ones; without it they are
only listed. A book no longer in the catalog is never touched.

R2 through its S3 API: R2_ACCOUNT_ID, R2_BUCKET, R2_ACCESS_KEY_ID,
R2_SECRET_ACCESS_KEY from the environment (the books repository's secrets
and variables). Needs boto3.
"""

import argparse
import json
import os
import re
import sys
import zipfile
from pathlib import Path

TYPES = {".pdf": "application/pdf", ".epub": "application/epub+zip", ".zip": "application/zip",
         ".png": "image/png", ".webp": "image/webp"}
# the covers go up too (front PNGs, the wrap's WebPs): the site links them here
FILES = (".pdf", ".epub", ".png", ".webp")
CACHE = "public, max-age=31536000, immutable"
COVER = re.compile(r"^(.+?-v\d+(?:\.\d+)?)-cover(.*)\.pdf$")
VERSION = r"v(\d+)(?:\.(\d+))?"


def downloads(cat):
    """{edition key: [release names]} of what goes to the bucket, the zips
    included; an edition key is (folder, modern?)."""
    out = {}
    for e in cat["books"]:
        names = [f["name"] for f in e["files"] if Path(f["name"]).suffix in FILES]
        for n in list(names):
            m = COVER.match(n)
            if m and f"{m.group(1)}{m.group(2)}.pdf" in names:
                names.append(f"{m.group(1)}{m.group(2)}-print-ready.zip")
        key = (e["folder"], e.get("edition") == "modern")
        out.setdefault(key, []).extend(names)
    return out


def print_ready(rel, name):
    """Make the-book-v3-print-ready.zip from the-book-v3.pdf and
    the-book-v3-cover.pdf in rel: stored, not compressed, with fixed dates,
    so the same files make the same zip."""
    stem = name[:-len("-print-ready.zip")]
    m = re.match(rf"^(.+?-{VERSION})(.*)$", stem)
    cover = f"{m.group(1)}-cover{m.group(4)}.pdf"
    path = rel / name
    with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as z:
        for f in (f"{stem}.pdf", cover):
            info = zipfile.ZipInfo(f, date_time=(1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o644 << 16
            z.writestr(info, (rel / f).read_bytes())
    return path


def version_of(name, folder, modern):
    """(major, minor) of a release name of that edition, or None."""
    if ("-modern" in name) != modern:
        return None
    m = re.match(rf"^{re.escape(folder)}-{VERSION}[-.]", name)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else None


def to_prune(keys, editions):
    """The bucket keys older than each edition's version before the current."""
    old = []
    for (folder, modern), names in editions.items():
        current = {version_of(n, folder, modern) for n in names} - {None}
        mine = {k: version_of(k, folder, modern) for k in keys}
        mine = {k: v for k, v in mine.items() if v}
        if not current:
            continue
        # the version before: all of it (v16 and its point versions v16.1 ...: a point
        # version's print is v16's)
        low = min(v[0] for v in current)
        before = max((v[0] for v in mine.values() if v[0] < low), default=None)
        old += [k for k, v in mine.items() if v not in current and v[0] != before]
    return sorted(old)


def client():
    import boto3
    return boto3.client(
        "s3", region_name="auto",
        endpoint_url=f"https://{os.environ['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
        aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"])


def bucket_keys(s3, bucket):
    keys = set()
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket):
        keys |= {o["Key"] for o in page.get("Contents", [])}
    return keys


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("release", type=Path)
    ap.add_argument("--prune", action="store_true", help="delete versions older than the previous")
    ap.add_argument("--dry-run", action="store_true", help="say what would change, change nothing")
    a = ap.parse_args(argv)
    cat = json.loads((a.release / "catalog.json").read_text(encoding="utf-8"))
    editions = downloads(cat)
    s3, bucket = client(), os.environ["R2_BUCKET"]
    have = bucket_keys(s3, bucket)
    sent = kept = 0
    for name in sorted({n for names in editions.values() for n in names}):
        if name in have:
            kept += 1
            continue
        path = a.release / name
        if name.endswith("-print-ready.zip") and not a.dry_run:
            path = print_ready(a.release, name)
        print(f"up: {name}")
        if not a.dry_run:
            s3.upload_file(str(path), bucket, name, ExtraArgs={
                "ContentType": TYPES[path.suffix], "CacheControl": CACHE})
        sent += 1
    old = to_prune(have, editions)
    for k in old:
        print(f"{'delete' if a.prune else 'older than the previous version'}: {k}")
        if a.prune and not a.dry_run:
            s3.delete_object(Bucket=bucket, Key=k)
    print(f"release {cat['release']}: {sent} sent, {kept} already there, "
          f"{len(old)} older {'deleted' if a.prune and not a.dry_run else 'kept'}")


if __name__ == "__main__":
    sys.exit(main())
