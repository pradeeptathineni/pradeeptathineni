#!/usr/bin/env python3
"""Read GitHub release and commit facts without rewriting the profile.

Requires an authenticated `gh` CLI. Public repositories come from README links.
Private repositories are queried only when explicitly supplied with
--include-private OWNER/REPO; their URLs are omitted from the output.
Maturity describes publication, not quality. Activity describes commit recency,
not maintenance intent. Human judgment still owns project goals and status.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
import json
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo


def github(path):
    result = subprocess.run(
        ["gh", "api", path], capture_output=True, text=True, check=True, timeout=30
    )
    return json.loads(result.stdout)


def collect(repository, as_of, recent_days, private_allowed):
    try:
        metadata = github(f"repos/{repository}")
        if metadata["private"] and repository not in private_allowed:
            return {"repository": repository, "error": "Private; explicit opt-in required"}
        canonical = metadata["full_name"]
        if canonical.lower() != repository.lower():
            return {"repository": repository, "redirects_to": canonical}
        branch = metadata["default_branch"]
        commits = github(f"repos/{repository}/commits?per_page=1&sha={branch}")
        releases = github(f"repos/{repository}/releases?per_page=100")
        published = [r for r in releases if not r["draft"] and r["published_at"]]
        latest = max(published, key=lambda r: r["published_at"], default=None)
        timestamp = commits[0]["commit"]["committer"]["date"] if commits else None
        updated = (
            datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            .astimezone(ZoneInfo("America/New_York"))
            .date()
            if timestamp else None
        )
        age = (as_of - updated).days if updated else None
        activity = (
            "Archived" if metadata["archived"] else
            "Unknown" if age is None or age < 0 else
            "Recent" if age <= recent_days else "Quiet"
        )
        return {
            "repository": canonical,
            "visibility": "Private" if metadata["private"] else "Public",
            "url": None if metadata["private"] else metadata["html_url"],
            "maturity": latest["tag_name"] if latest else "Experimental",
            "preview": latest["prerelease"] if latest else False,
            "release_url": latest["html_url"] if latest and not metadata["private"] else None,
            "updated": updated.isoformat() if updated else None,
            "activity": activity,
        }
    except (subprocess.SubprocessError, ValueError, KeyError, IndexError) as error:
        # Report gaps without printing CLI stderr, which may contain private context.
        return {"repository": repository, "error": type(error).__name__}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", type=date.fromisoformat,
                        default=datetime.now(ZoneInfo("America/New_York")).date())
    parser.add_argument("--recent-days", type=int, default=90)
    parser.add_argument("--include-private", action="append", default=[], metavar="OWNER/REPO")
    args = parser.parse_args()
    if args.recent_days < 0:
        parser.error("--recent-days must be nonnegative")
    if any(not re.fullmatch(r"[\w.-]+/[\w.-]+", r) for r in args.include_private):
        parser.error("private repositories must use OWNER/REPO syntax")
    readme = Path(__file__).resolve().parents[2] / "README.md"
    linked = re.findall(r"https://github\.com/([\w.-]+/[\w.-]+)(?=[/\s)\"?#]|$)",
                        readme.read_text())
    repositories = sorted(set(linked + args.include_private))
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(
            lambda r: collect(r, args.as_of, args.recent_days, args.include_private),
            repositories,
        ))
    print(json.dumps({"as_of": args.as_of.isoformat(), "recent_days": args.recent_days,
                      "projects": results}, indent=2))
    return int(any("error" in result for result in results))


if __name__ == "__main__":
    sys.exit(main())
