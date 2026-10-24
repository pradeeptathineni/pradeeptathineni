#!/usr/bin/env python3

# .meta/scripts/check_readme.py - Check public Markdown and protected bytes offline.
# Usage: python3 .meta/scripts/check_readme.py
#

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

FENCES = re.compile(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$", re.M | re.S)
THOUGHTS = "<details>\n<summary>def thoughts("


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prose(text):
    """Exclude example code from link and HTML inspection."""
    return re.sub(r"`+[^`\n]*`+", "", FENCES.sub("", text))


class Markup(HTMLParser):
    """Track the HTML containers and references used by the profile."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.links = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # Count only summaries directly owned by their disclosure
        if tag in ("details", "summary", "dl", "dd", "table"):
            if tag == "summary":
                if not self.stack or self.stack[-1][0] != "details":
                    self.errors.append("summary must be directly inside details")
                else:
                    self.stack[-1][1] += 1
            self.stack.append([tag, 0])
        # Navigation and image references share the same local-file boundary
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "img" and "src" in attrs:
            self.links.append(attrs["src"])
        for key in ("id", "name"):
            if attrs.get(key):
                self.anchors.add(attrs[key])

    def handle_endtag(self, tag):
        if tag not in ("details", "summary", "dl", "dd", "table"):
            return
        if not self.stack or self.stack[-1][0] != tag:
            self.errors.append(f"unmatched closing {tag}")
            return
        _, summaries = self.stack.pop()
        if tag == "details" and summaries != 1:
            self.errors.append("details must contain exactly one summary")


def document(text):
    headings = FENCES.sub("", text)
    text = prose(text)
    markup = Markup()
    markup.feed(text)
    if markup.stack:
        markup.errors.append("unclosed tags: " + ", ".join(t[0] for t in markup.stack))
    markup.links.extend(re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text))
    # Derive heading anchors from visible labels, including inline code
    counts = {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", headings, re.M):
        heading = re.sub(r"`+([^`]*)`+", r"\1", heading)
        heading = re.sub(r"<[^>]*>", "", heading).strip().lower()
        slug = re.sub(r"[^\w -]", "", heading).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        markup.anchors.add(f"{slug}-{count}" if count else slug)
    return markup


def local_path(root, source, target):
    # Refuse outside paths and symlinks before reading referenced content
    path = (source.parent / target).resolve()
    if not path.is_relative_to(root):
        raise ValueError("reference leaves the repository")
    if not path.is_file():
        raise ValueError("referenced file is missing")
    return path


def check(root):
    """Validate the repository's inline Markdown/HTML links without fetching URLs."""
    root = root.resolve()
    errors = []
    # Parse once so cross-file anchors use the same document snapshot
    documents = {}
    for source in sorted(root.rglob("*.md")):
        if ".git" in source.relative_to(root).parts:
            continue
        try:
            path = local_path(root, source, source.name)
            documents[path] = document(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            errors.append(f"{source.relative_to(root)}: {error}")
    for source, markup in documents.items():
        errors.extend(f"{source.relative_to(root)}: {error}" for error in markup.errors)
        for reference in markup.links:
            try:
                uri = urlsplit(reference.strip("<>"))
                # Leave external URLs to the reader; CI performs no fetches
                if uri.scheme or uri.netloc:
                    continue
                target = (
                    local_path(root, source, unquote(uri.path)) if uri.path else source
                )
                if uri.fragment:
                    if target not in documents:
                        raise ValueError(
                            "anchor target is not a checked Markdown document"
                        )
                    if unquote(uri.fragment) not in documents[target].anchors:
                        raise ValueError("local anchor is missing")
            except (OSError, ValueError) as error:
                errors.append(f"{source.relative_to(root)}: {reference}: {error}")
    # Compare protected public regions and assets against reviewed hashes
    try:
        manifest = json.loads(
            (root / ".meta/scripts/readme_invariants.json").read_text()
        )
        readme = (root / "README.md").read_bytes()
        text = readme.decode("utf-8")
        observed = {
            "title": digest(readme.splitlines()[0]),
            "code_blocks": [digest(m.group().encode()) for m in FENCES.finditer(text)],
            "thoughts_and_after": digest(text[text.index(THOUGHTS):].encode()),
        }
        for name, value in observed.items():
            if value != manifest[name]:
                errors.append(f"README.md: protected {name} differs from the baseline")
        for name, expected in manifest["files"].items():
            target = local_path(root, root / "README.md", name)
            if digest(target.read_bytes()) != expected:
                errors.append(f"{name}: protected file differs from the baseline")
    except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
        errors.append(f"Protected-content baseline: {error}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=check.__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[2]
    )
    args = parser.parse_args()
    errors = check(args.root)
    for error in errors:
        print(error)
    if not errors:
        print("README structure, protected content, local links and assets passed.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
