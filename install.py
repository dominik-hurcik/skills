#!/usr/bin/env python3
"""Link this collection into the project in the current directory."""

import argparse
import os
import sys
from pathlib import Path


def install(*, skills_only: bool = False) -> None:
    source = Path(__file__).resolve().parent
    project = Path.cwd().resolve()
    if source == project or not source.is_relative_to(project):
        raise ValueError(
            "Run this from your project root, with this collection cloned inside it."
        )

    skills = sorted(path.parent for path in (source / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No skills found in the collection.")

    links = []
    if not skills_only:
        links.extend((project / name, source / name) for name in ("AGENTS.md", "CLAUDE.md"))
    directories = []
    for agent in (".agents", ".claude"):
        directories.extend([project / agent, project / agent / "skills"])
        links.extend((project / agent / "skills" / skill.name, skill) for skill in skills)

    # Check every destination before creating anything.
    conflicts = []
    for directory in directories:
        if directory.is_symlink() or (directory.exists() and not directory.is_dir()):
            conflicts.append(f"{directory.relative_to(project)} must be a real directory")
    for destination, target in links:
        if destination.is_symlink():
            if destination.resolve() != target.resolve():
                conflicts.append(f"{destination.relative_to(project)} points elsewhere")
        elif destination.exists():
            conflicts.append(f"{destination.relative_to(project)} already exists")
        if not target.exists():
            conflicts.append(f"Missing source: {target}")
    if conflicts:
        raise ValueError(
            "Installation stopped. No files changed.\n"
            + "\n".join(f"  {message}" for message in conflicts)
            + "\nResolve the listed conflicts before retrying."
            + (
                "\nUse --skills-only to keep existing AGENTS.md and CLAUDE.md files."
                if not skills_only
                else ""
            )
        )

    created = 0
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    for destination, target in links:
        if not destination.is_symlink():
            destination.symlink_to(
                os.path.relpath(target, destination.parent),
                target_is_directory=target.is_dir(),
            )
            created += 1

    print(f"Connected {len(skills)} skills for Codex and Claude Code.")
    if skills_only:
        print(f"Skills-only install. Created {created} new links.")
    else:
        print(f"Linked AGENTS.md and CLAUDE.md. Created {created} new links.")
    print("Start a new agent session in this project to load the installed files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skills-only",
        action="store_true",
        help="Install skill links without reading or changing project AGENTS.md or CLAUDE.md files.",
    )
    arguments = parser.parse_args()
    try:
        install(skills_only=arguments.skills_only)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
