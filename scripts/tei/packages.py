"""
The imprint's Typst templates (@local/fgbooks, @local/fgbooksLBCF), versioned
as git tags in the typst/fgbooks-typst submodule rather than installed by hand.

Typst finds @local/NAME:VERSION in NAME/VERSION under its local package
directory. Before anything is compiled, ./fgb unpacks every version the books
import from its tag into a cache and points TYPST_PACKAGE_PATH at it:

  fgbooks 0.5.2        tag 0.5.2
  fgbooksLBCF 0.1.0    tag fgbooksLBCF-0.1.0   (any other package: NAME-VERSION)

A version with no tag yet is the one being worked on: if the submodule's
working copy declares it (typst.toml), the cache links to the working copy, so
edits show up without tagging. Tagged versions are unpacked once and checked
against their tag's commit each run.
"""

import os
import re
import shutil
import subprocess
import tarfile
import io
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
SUBMODULE = REPO / "typst" / "fgbooks-typst"
CACHE = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache") / "fgb-typst" / "packages"
IMPORT_RE = r"@local/[A-Za-z0-9_-]+:[0-9]+\.[0-9]+\.[0-9]+"
MARKER = ".fgb-commit"


class PackageError(Exception):
    pass


def git(*args, check=True):
    r = subprocess.run(["git", "-C", str(SUBMODULE), *args], capture_output=True)
    if check and r.returncode:
        raise PackageError(f"git {' '.join(args)}: {r.stderr.decode().strip()}")
    return r


def imported():
    """Every (name, version) a book's Typst file imports from @local."""
    r = subprocess.run(["git", "-C", str(REPO), "grep", "--untracked", "-h", "-o",
                        "-E", IMPORT_RE, "--", "books/*.typ"],
                       capture_output=True, text=True)
    found = set()
    for m in r.stdout.split():
        name, ver = m[len("@local/"):].split(":")
        found.add((name, ver))
    return sorted(found)


def tag_for(name, ver):
    return ver if name == "fgbooks" else f"{name}-{ver}"


def working_copy_declares(name, ver):
    toml = SUBMODULE / "typst.toml"
    if not toml.exists():
        return False
    t = toml.read_text(encoding="utf-8")
    return (re.search(rf'^name\s*=\s*"{re.escape(name)}"', t, re.M) is not None and
            re.search(rf'^version\s*=\s*"{re.escape(ver)}"', t, re.M) is not None)


def ensure(name, ver):
    """Put NAME/VERSION in the cache; return where it came from."""
    if not (SUBMODULE / ".git").exists():
        raise PackageError("the Typst templates are not checked out: run "
                           "git submodule update --init typst/fgbooks-typst")
    dest = CACHE / "local" / name / ver
    tag = tag_for(name, ver)
    r = git("rev-parse", "--verify", "-q", f"refs/tags/{tag}^{{commit}}", check=False)
    if r.returncode:
        if working_copy_declares(name, ver):
            if not (dest.is_symlink() and dest.resolve() == SUBMODULE.resolve()):
                if dest.is_symlink() or dest.is_file():
                    dest.unlink()
                elif dest.exists():
                    shutil.rmtree(dest)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.symlink_to(SUBMODULE)
            return "working copy (not tagged yet)"
        raise PackageError(
            f"@local/{name}:{ver} is imported but typst/fgbooks-typst has no tag "
            f"'{tag}' (git -C typst/fgbooks-typst fetch --tags, or move the "
            f"submodule to a commit that has it)")
    commit = r.stdout.decode().strip()
    if (dest / MARKER).exists() and (dest / MARKER).read_text().strip() == commit \
            and not dest.is_symlink():
        return f"tag {tag}"
    if dest.is_symlink():
        dest.unlink()
    elif dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    tar = git("archive", "--format=tar", commit).stdout
    with tarfile.open(fileobj=io.BytesIO(tar)) as tf:
        tf.extractall(dest, filter="data")
    (dest / MARKER).write_text(commit + "\n")
    return f"tag {tag} (unpacked)"


def setup():
    """Make every imported version available and point Typst at the cache
    (for this process and everything it runs). Returns [(name, ver, source)]."""
    out = [(n, v, ensure(n, v)) for n, v in imported()]
    os.environ["TYPST_PACKAGE_PATH"] = str(CACHE)
    return out
