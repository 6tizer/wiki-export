#!/usr/bin/env python3
"""Update README.md stats section from local wiki file counts.

Looks for <!-- stats:start --> and <!-- stats:end --> markers in README.md
and replaces the content between them with current file counts.

Usage: python3 update-readme-stats.py [--dry-run]
"""

import os
import sys
from pathlib import Path

WIKI_DIR = Path(__file__).parent / "wiki-export" / "wiki"
README_PATH = Path(__file__).parent / "wiki-export" / "README.md"

TYPE_DIRS = {
    "concept": "concepts",
    "entity": "entities",
    "synthesis": "syntheses",
    "summary": "summaries",
}

DESCRIPTIONS = {
    "concept": "Core concepts with definitions, key points, and cross-references",
    "entity": "Product/company/people profiles with key data and version updates",
    "synthesis": "Cross-source analytical essays on major topics",
    "summary": "Single-article summaries (linked from concepts, not in index)",
}

MARKER_START = "<!-- stats:start -->"
MARKER_END = "<!-- stats:end -->"


def count_files(directory: Path) -> int:
    """Count .md files in a directory."""
    if not directory.exists():
        return 0
    return sum(1 for f in directory.iterdir() if f.suffix == ".md")


def generate_stats_block(counts: dict[str, int]) -> str:
    """Generate the stats content between markers."""
    total = sum(counts.values())

    lines = [
        f"**{total:,}+ entries** across 14 topic areas, covering the AI agent ecosystem and beyond.",
        "",
        "## What's Inside",
        "",
        "| Type | Count | Description |",
        "|------|-------|-------------|",
    ]
    for type_name in TYPE_DIRS:
        c = counts[type_name]
        lines.append(
            f"| {type_name.capitalize()} | ~{c:,} | {DESCRIPTIONS[type_name]} |"
        )
    return "\n".join(lines)


def main():
    dry_run = "--dry-run" in sys.argv

    # Count files
    counts = {}
    for type_name, dir_name in TYPE_DIRS.items():
        counts[type_name] = count_files(WIKI_DIR / dir_name)

    total = sum(counts.values())
    print(f"File counts: {', '.join(f'{k}={v}' for k, v in counts.items())}, total={total}")

    # Read README
    if not README_PATH.exists():
        print(f"ERROR: README not found at {README_PATH}", file=sys.stderr)
        sys.exit(1)

    content = README_PATH.read_text()

    # Find markers
    start_idx = content.find(MARKER_START)
    end_idx = content.find(MARKER_END)

    if start_idx == -1 or end_idx == -1:
        print(f"ERROR: Stats markers not found in README. Expected {MARKER_START} and {MARKER_END}", file=sys.stderr)
        sys.exit(1)

    if start_idx >= end_idx:
        print("ERROR: Start marker is after end marker", file=sys.stderr)
        sys.exit(1)

    # Generate new content
    new_block = generate_stats_block(counts)
    new_content = content[: start_idx + len(MARKER_START)] + "\n" + new_block + "\n" + content[end_idx:]

    if dry_run:
        print("\n--- Preview of changes ---")
        print(new_block)
        return

    if new_content == content:
        print("No changes needed.")
        return

    README_PATH.write_text(new_content)
    print(f"README updated: {total:,}+ entries")


if __name__ == "__main__":
    main()
