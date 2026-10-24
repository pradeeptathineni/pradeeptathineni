#!/usr/bin/env python3

# .meta/scripts/project_metadata.py - Inspect GitHub facts and reconcile activity.
# Usage: python3 .meta/scripts/project_metadata.py --as-of 2026-10-24
#

"""Inspect explicit project cards; optionally reconcile only Activity cells.

Requires authenticated gh. Each project details element carries data-repo.
Private cards require --include-private OWNER/REPO before any API call.
GH_PUBLIC_TOKEN optionally supplies separate authentication for public cards.
Incomplete or redirected collections never write. Releases are inspection
facts; authored maturity, status and readiness remain unchanged.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo


REPOSITORY = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*/(?!\.\.?$)[A-Za-z0-9_.-]+")
PROJECT = re.compile(
    r'<details data-repo="(?P<repository>[^"\n]+)">\n'
    r'<summary>(?P<summary>[^\n]+)</summary>(?P<body>.*?)</details>',
    re.S,
)
ACTIVITY = re.compile(
    r"(\| \*\*Activity\*\*\s*\|)([^\n]*?)(\|[ \t]*)(?=\n|$)"
)


def projects(text):
    """Bind each Activity row to one explicit, consistently presented repository."""
    cards = []
    seen = set()
    for match in PROJECT.finditer(text):
        repository = match["repository"].lower()
        if not REPOSITORY.fullmatch(repository) or repository in seen:
            raise ValueError("Project repository IDs must be valid and unique")
        seen.add(repository)
        summary = match["summary"]
        private = "🔒" in summary
        links = re.findall(r'https://github\.com/([\w.-]+/[\w.-]+)', summary)
        # Identity and visibility must agree before any remote access
        if private:
            maturity = re.search(r"^\| \*\*Maturity\*\*[^\n]*", match["body"], re.M)
            if (
                re.search(r"<a\b", summary)
                or f"https://github.com/{repository}" in match[0].lower()
                or (maturity and re.search(r"\[`[^`]+`\]\(", maturity[0]))
            ):
                raise ValueError("Private project titles and versions must be unlinked")
        elif [link.lower() for link in links] != [repository]:
            raise ValueError("Public project link does not match its repository ID")
        if len(ACTIVITY.findall(match["body"])) != 1:
            raise ValueError("Each project needs exactly one Activity row")
        cards.append({"match": match, "repository": repository, "private": private})
    # Missing or malformed identifiers cannot silently drop a card from refresh
    rows = len(re.findall(r"^\| \*\*Activity\*\*", text, re.M))
    if not cards or rows != len(cards):
        raise ValueError("Every project Activity row needs an explicit data-repo ID")
    return cards


def github(path, public=False):
    """Use separate public authentication when supplied; otherwise use gh's session."""
    # Select credentials per subprocess, without changing other concurrent queries
    env = None
    if public and os.environ.get("GH_PUBLIC_TOKEN"):
        env = dict(os.environ, GH_TOKEN=os.environ["GH_PUBLIC_TOKEN"])
    result = subprocess.run(
        ["gh", "api", path], capture_output=True, text=True, check=True,
        timeout=30, env=env,
    )
    return json.loads(result.stdout)


def collect(repository, as_of, recent_days, private_allowed, private_expected=None):
    """Inspect release/activity facts without inferring project readiness."""
    # Known private cards require authorization before even the identity query
    if private_expected and repository not in private_allowed:
        return {"repository": repository, "error": "Private; explicit opt-in required"}
    public = private_expected is False
    operation = "repository"
    try:
        # Require private opt-in before querying commit or release details
        metadata = github(f"repos/{repository}", public=public)
        if metadata["private"] and repository not in private_allowed:
            return {
                "repository": repository,
                "error": "Private; explicit opt-in required",
            }
        # Keep repository redirects explicit rather than silently adopting them
        canonical = metadata["full_name"]
        if canonical.lower() != repository.lower():
            return {"repository": repository, "redirects_to": canonical}
        if private_expected is not None and metadata["private"] != private_expected:
            return {"repository": repository, "error": "Repository visibility changed"}
        # Inspect default-branch activity independently of published releases
        branch = metadata["default_branch"]
        operation = "commits"
        commits = github(
            f"repos/{repository}/commits?per_page=1&sha={branch}", public=public
        )
        operation = "releases"
        releases = github(f"repos/{repository}/releases?per_page=100", public=public)
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
        TypeError,
    ) as error:
        # Retain safe diagnostics without exposing API bodies or CLI stderr
        failure = {
            "repository": repository,
            "error": type(error).__name__,
            "operation": operation,
        }
        if isinstance(error, subprocess.CalledProcessError):
            status = re.search(r"\(HTTP ([1-5][0-9]{2})\)", error.stderr or "")
            if status:
                failure["http_status"] = int(status[1])
        return failure


def reconcile(text, facts, as_of):
    """Require a complete collection and preserve everything outside Activity cells."""
    cards = projects(text)
    by_repository = {row["repository"].lower(): row for row in facts}
    expected = {card["repository"] for card in cards}
    if len(by_repository) != len(facts) or set(by_repository) != expected:
        raise ValueError("Repository facts do not match the project cards")
    for card in cards:
        row = by_repository[card["repository"]]
        if "error" in row or "redirects_to" in row or not row.get("updated"):
            raise ValueError("Repository facts are incomplete or redirected")
        if date.fromisoformat(row["updated"]) > as_of:
            raise ValueError("Repository date is in the future")
        if row.get("activity") not in {"Recent", "Quiet", "Archived"}:
            raise ValueError("Repository activity is unknown")
        if row.get("visibility") != ("Private" if card["private"] else "Public"):
            raise ValueError("Repository visibility does not match the project card")

    changed = 0

    def project(match):
        nonlocal changed
        row = by_repository[match["repository"].lower()]
        value = f"Updated {row['updated']} · `{row['activity']}`"

        def activity(cell):
            nonlocal changed
            # Identical facts retain their exact padding and create no diff
            if cell[2].strip() == value:
                return cell[0]
            changed += 1
            content = (" " + value + " ").ljust(len(cell[2]))
            return cell[1] + content + cell[3]

        # Keep the source card intact, including locks, versions and author claims
        return ACTIVITY.sub(activity, match[0])

    return PROJECT.sub(project, text), changed


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
        "--quiet", action="store_true",
        help="Report counts only; omit repository facts from public workflow logs",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Reconcile Activity cells only after complete collection",
    )
    # Validate every input before starting repository collection
    args = parser.parse_args()
    if args.recent_days < 0:
        parser.error("--recent-days must be nonnegative")
    if any(not REPOSITORY.fullmatch(r) for r in args.include_private):
        parser.error("private repositories must use OWNER/REPO syntax")
    readme = args.readme.expanduser().resolve()
    if not readme.is_file():
        parser.error(f"README not found: {readme}")
    try:
        text = readme.read_text(encoding="utf-8")
        cards = projects(text)
        private_allowed = {repo.lower() for repo in args.include_private}
        private_cards = {c["repository"] for c in cards if c["private"]}
        if not private_allowed <= private_cards:
            parser.error("Private opt-ins must identify displayed private cards")
    except (OSError, ValueError) as error:
        parser.error(str(error))

    # Query only declared cards, retaining their order and visibility expectations
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(
            pool.map(
                lambda card: collect(
                    card["repository"],
                    args.as_of,
                    args.recent_days,
                    private_allowed,
                    card["private"],
                ),
                cards,
            )
        )
    cells = 0
    try:
        reconciled, cells = reconcile(text, results, args.as_of)
    except (ValueError, KeyError, TypeError):
        print("README unchanged: incomplete repository facts.", file=sys.stderr)
        if args.quiet:
            # Source IDs are public; response text and redirect targets stay hidden
            for card, row in zip(cards, results):
                if "error" not in row and "redirects_to" not in row:
                    continue
                operation = row.get("operation", "metadata")
                if operation not in {"repository", "commits", "releases"}:
                    operation = "metadata"
                status = row.get("http_status")
                detail = (
                    f"{operation}, HTTP {status}"
                    if isinstance(status, int) and 100 <= status <= 599
                    else operation
                )
                print(
                    f"Collection failed for {card['repository']} ({detail}).",
                    file=sys.stderr,
                )
        if not args.quiet:
            print(
                json.dumps(
                    {
                        "as_of": args.as_of.isoformat(),
                        "recent_days": args.recent_days,
                        "projects": results,
                    },
                    indent=2,
                )
            )
        return 1

    # Successful checks produce no date-only or padding-only writes
    if args.write and reconciled != text:
        readme.write_text(reconciled, encoding="utf-8")
    if args.quiet:
        print(f"Activity changes found: {cells}; projects checked: {len(cards)}.")
    else:
        print(
            json.dumps(
                {
                    "as_of": args.as_of.isoformat(),
                    "recent_days": args.recent_days,
                    "activity_cells_reconciled": cells if args.write else 0,
                    "projects": results,
                },
                indent=2,
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
