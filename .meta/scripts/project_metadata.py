#!/usr/bin/env python3

# .meta/scripts/project_metadata.py - Inspect GitHub facts and reconcile activity.
# Usage: python3 .meta/scripts/project_metadata.py --as-of 2026-10-24
#

"""Read GitHub release and commit facts; optionally reconcile activity rows.

Requires an authenticated `gh` CLI. Public repositories come from README links.
Private repositories are queried only when explicitly supplied with
--include-private OWNER/REPO; their URLs are omitted from the output.
--write updates only linked project Activity rows and the facts-check date, and
refuses incomplete collections. Maturity describes publication, not quality.
Activity describes commit recency,
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
    """Use the caller's authenticated gh session."""
    result = subprocess.run(
        ["gh", "api", path], capture_output=True, text=True, check=True, timeout=30
    )
    return json.loads(result.stdout)


def collect(repository, as_of, recent_days, private_allowed):
    try:
        # Require private opt-in before querying commit or release details
        metadata = github(f"repos/{repository}")
        if metadata["private"] and repository not in private_allowed:
            return {
                "repository": repository,
                "error": "Private; explicit opt-in required",
            }
        # Keep repository redirects explicit rather than silently adopting them
        canonical = metadata["full_name"]
        if canonical.lower() != repository.lower():
            return {"repository": repository, "redirects_to": canonical}
        # Inspect default-branch activity independently of published releases
        branch = metadata["default_branch"]
        commits = github(f"repos/{repository}/commits?per_page=1&sha={branch}")
        releases = github(f"repos/{repository}/releases?per_page=100")
        published = [r for r in releases if not r["draft"] and r["published_at"]]
        latest = max(published, key=lambda r: r["published_at"], default=None)
        # Compare New York calendar dates rather than elapsed UTC hours
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
        # Keep authorized private facts while omitting their links
        return {
            "repository": canonical,
            "visibility": "Private" if metadata["private"] else "Public",
            "url": None if metadata["private"] else metadata["html_url"],
            "maturity": latest["tag_name"] if latest else "Experimental",
            "preview": latest["prerelease"] if latest else False,
            "release_url": (
                latest["html_url"] if latest and not metadata["private"] else None
            ),
            "updated": updated.isoformat() if updated else None,
            "activity": activity,
        }
    except (
        OSError,
        subprocess.SubprocessError,
        ValueError,
        KeyError,
        IndexError,
    ) as error:
        # Report gaps without exposing potentially private CLI stderr
        return {"repository": repository, "error": type(error).__name__}


def reconcile(text, facts, as_of):
    """Change only linked project Activity cells and the check date."""
    by_repository = {row["repository"].lower(): row for row in facts}
    changed = 0

    def project(match):
        nonlocal changed
        block = match.group()
        # The linked summary binds this block to collected repository facts
        link = re.search(
            r"https://github\.com/([\w.-]+/[\w.-]+)",
            block.split("</summary>", 1)[0],
        )
        row = by_repository.get(link.group(1).lower()) if link else None
        if not row or not row.get("updated") or "error" in row:
            return block
        # Limit replacements to Activity cells and preserve table alignment
        value = f" Updated {row['updated']} · `{row['activity']}` "
        replacement, count = re.subn(
            r"(\| \*\*Activity\*\*\s*\|)([^\n]*?)(\|[ \t]*)(?=\n|$)",
            lambda cell: (
                cell.group(1) + value.ljust(len(cell.group(2))) + cell.group(3)
            ),
            block,
        )
        changed += count
        return replacement

    # Traverse project disclosures without rebuilding authored Markdown
    result = re.sub(
        r"<details>\n<summary>(?=[^\n]*https://github\.com/)"
        r"[^\n]*</summary>.*?</details>",
        project,
        text,
        flags=re.S,
    )
    result = re.sub(
        r"(?:Public r|R)elease and activity facts last checked on "
        r"\d{4}-\d{2}-\d{2}\.",
        f"Release and activity facts last checked on {as_of.isoformat()}.",
        result,
    )
    return result, changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "README.md",
    )
    parser.add_argument(
        "--as-of",
        type=date.fromisoformat,
        default=datetime.now(ZoneInfo("America/New_York")).date(),
    )
    parser.add_argument("--recent-days", type=int, default=30)
    parser.add_argument(
        "--include-private", action="append", default=[], metavar="OWNER/REPO"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Reconcile only linked project Activity rows and the check date",
    )
    # Validate every input before starting repository collection
    args = parser.parse_args()
    if args.recent_days < 0:
        parser.error("--recent-days must be nonnegative")
    if any(not re.fullmatch(r"[\w.-]+/[\w.-]+", r) for r in args.include_private):
        parser.error("private repositories must use OWNER/REPO syntax")
    readme = args.readme.expanduser().resolve()
    if not readme.is_file():
        parser.error(f"README not found: {readme}")
    # Collect authored links plus explicit private opt-ins, with no discovery
    linked = re.findall(
        r"https://github\.com/([\w.-]+/[\w.-]+)(?=[/\s)\"?#]|$)",
        readme.read_text(),
    )
    repositories = sorted(set(linked + args.include_private))
    # Bound concurrent queries while retaining sorted output order
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(
            pool.map(
                lambda r: collect(
                    r, args.as_of, args.recent_days, args.include_private
                ),
                repositories,
            )
        )
    # Any gap or redirect prevents a partial README refresh
    incomplete = any(
        "error" in result or "redirects_to" in result for result in results
    )
    cells = 0
    if args.write:
        if incomplete:
            print(
                "README unchanged: resolve incomplete repository facts first.",
                file=sys.stderr,
            )
        else:
            reconciled, cells = reconcile(readme.read_text(), results, args.as_of)
            readme.write_text(reconciled)
    # Return the collected evidence even when a requested write was refused
    print(
        json.dumps(
            {
                "as_of": args.as_of.isoformat(),
                "recent_days": args.recent_days,
                "activity_cells_reconciled": cells,
                "projects": results,
            },
            indent=2,
        )
    )
    return int(incomplete)


if __name__ == "__main__":
    sys.exit(main())
