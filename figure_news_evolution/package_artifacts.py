#!/usr/bin/env python3
"""Create the downloadable artifact archive for the news-evolution figures.

Run from the repository root:

    python figure_news_evolution/package_artifacts.py

The script writes `figure_news_evolution_artifacts.zip` to the repository root.
The zip is intentionally not committed because GitHub/Codex PR creation does not
support binary files in the diff.
"""
from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIR = REPO_ROOT / "figure_news_evolution"
OUTPUT_ZIP = REPO_ROOT / "figure_news_evolution_artifacts.zip"

INCLUDE_SUFFIXES = {".py", ".md", ".txt", ".svg"}
EXCLUDE_DIRS = {"__pycache__"}


def iter_artifact_files() -> list[Path]:
    """Return source, README, requirements, and generated text figure artifacts."""
    files: list[Path] = []
    for path in sorted(PACKAGE_DIR.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        if path.suffix in INCLUDE_SUFFIXES:
            files.append(path)
    return files


def main() -> None:
    if OUTPUT_ZIP.exists():
        OUTPUT_ZIP.unlink()

    files = iter_artifact_files()
    with ZipFile(OUTPUT_ZIP, "w", compression=ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, path.relative_to(REPO_ROOT))

    print(f"Created {OUTPUT_ZIP}")
    print("Included files:")
    for path in files:
        print(f"- {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
