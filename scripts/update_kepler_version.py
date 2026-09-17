#!/usr/bin/env python3
"""Sync the Kepler version in the docs with the latest kepler-releases release.

Reads the latest published release from rubixkube-io/kepler-releases and writes
its version into kepler/installation.mdx. Run by .github/workflows/sync-kepler-version.yml,
or by hand:

    python scripts/update_kepler_version.py           # rewrite the page
    python scripts/update_kepler_version.py --check    # exit 1 if out of date, change nothing

The version is written as literal text rather than an MDX expression on purpose:
Mintlify evaluates {expressions} in the browser, so their values are missing from
the initial HTML that crawlers and LLMs read.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = "rubixkube-io/kepler-releases"
API_URL = f"https://api.github.com/repos/{REPO}/releases/latest"

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "kepler" / "installation.mdx"

# Anchored on the <span id="kepler-version"> in installation.mdx, which is also what
# kepler-version.js rewrites in the browser. Anchoring on the id rather than the
# surrounding prose means the sentence can be reworded freely.
VERSION_RE = re.compile(r'(<span id="kepler-version">)([^<]+)(</span>)')


def latest_version() -> str:
    """Return the latest release version, without the leading 'v'."""
    request = urllib.request.Request(
        API_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "rubixkube-docs-version-sync",
        },
    )
    # Raises the rate limit from 60/hr to 1000/hr in CI. Optional locally.
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            release = json.load(response)
    except urllib.error.HTTPError as error:
        sys.exit(f"GitHub API returned {error.code} for {API_URL}")
    except urllib.error.URLError as error:
        sys.exit(f"could not reach the GitHub API: {error.reason}")

    if release.get("draft"):
        sys.exit("latest release is still a draft, leaving the docs alone")

    tag = release.get("tag_name")
    if not tag:
        sys.exit("latest release has no tag_name")

    return tag.lstrip("v")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 if the docs are out of date, without writing",
    )
    args = parser.parse_args()

    version = latest_version()
    text = TARGET.read_text()

    updated, count = VERSION_RE.subn(rf"\g<1>{version}\g<3>", text)
    if count == 0:
        sys.exit(
            f'could not find <span id="kepler-version"> in {TARGET.relative_to(ROOT)}. '
            "If the span was removed or renamed, update VERSION_RE to match."
        )

    if updated == text:
        print(f"Already current: {version}")
        return

    current = VERSION_RE.search(text).group(2)
    if args.check:
        sys.exit(f"Out of date: docs say {current}, latest release is {version}")

    TARGET.write_text(updated)
    print(f"Updated {TARGET.relative_to(ROOT)}: {current} -> {version}")


if __name__ == "__main__":
    main()
