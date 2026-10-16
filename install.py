#!/usr/bin/env python3
"""Install this collection's skills and shared instructions for Codex and Claude Code.

Project mode (the default) installs into the project in the current directory.
User mode installs into your home folder, so every project on this machine gets them.
Works on macOS, Linux, and Windows.
"""

import argparse
import os
import stat
import sys
from pathlib import Path

WINDOWS = os.name == "nt"
MARKER = "<!-- Managed by install.py from "


# ---------- Links ----------


def is_link(path: Path) -> bool:
    """True for a symlink, or for a directory junction on Windows."""
    if path.is_symlink():
        return True
    if not WINDOWS:
        return False
    try:
        tag = os.lstat(path).st_reparse_tag
    except (OSError, AttributeError):
        return False
    return tag == stat.IO_REPARSE_TAG_MOUNT_POINT


def link_target(path: Path) -> Path:
    raw = os.readlink(path)
    if raw.startswith("\\\\?\\"):
        raw = raw[4:]
    return (path.parent / raw).resolve()


def link_directory(destination: Path, target: Path, *, relative: bool) -> None:
    if WINDOWS:
        # Junctions need no admin rights or Developer Mode, unlike symlinks.
        import _winapi

        _winapi.CreateJunction(str(target), str(destination))
    else:
        pointer = os.path.relpath(target, destination.parent) if relative else str(target)
        destination.symlink_to(pointer, target_is_directory=True)


def try_link_file(destination: Path, target: Path, *, relative: bool) -> bool:
    """Symlink a file. Return False if the OS doesn't allow it, as on Windows without Developer Mode."""
    pointer = os.path.relpath(target, destination.parent) if relative else str(target)
    try:
        destination.symlink_to(pointer)
    except OSError:
        if WINDOWS:
            return False
        raise
    return True


def remove_link(path: Path) -> None:
    try:
        path.unlink()
    except (IsADirectoryError, PermissionError):
        # Directory symlinks and junctions on Windows are removed with rmdir.
        # rmdir removes only the link, never the folder it points to.
        os.rmdir(path)


# ---------- Managed files ----------


def is_managed(path: Path) -> bool:
    if is_link(path) or not path.is_file():
        return False
    try:
        with path.open(encoding="utf-8") as file:
            return file.readline().startswith(MARKER)
    except (OSError, UnicodeDecodeError):
        return False


def import_line(destination: Path, target: Path) -> str:
    """A Claude Code @import that reaches target from destination's folder."""
    if destination.parent in target.parents:
        return "@" + target.relative_to(destination.parent).as_posix()
    try:
        return "@~/" + target.relative_to(Path.home().resolve()).as_posix()
    except ValueError:
        return "@" + target.as_posix()


def write_managed(destination: Path, body: str, source: Path) -> None:
    header = f"{MARKER}{source.as_posix()}. Rerun the installer to update it. -->\n"
    with destination.open("w", encoding="utf-8", newline="\n") as file:
        file.write(header + body)


# ---------- Plan ----------


def plan(source: Path, mode: str, skills_only: bool):
    """Return the skills, the skill folders, and the shared-instruction entries."""
    skills = sorted(path.parent for path in (source / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No skills found in the collection.")

    if mode == "project":
        root = Path.cwd().resolve()
        if source == root or root not in source.parents:
            raise ValueError(
                "Run project mode from your project root, with this collection cloned inside it. "
                "To install for every project instead, use --user."
            )
        skill_dirs = [root / ".agents" / "skills", root / ".claude" / "skills"]
        codex_file = root / "AGENTS.md"
        claude_file = root / "CLAUDE.md"
    else:
        home = Path.home().resolve()
        codex_home = Path(os.environ.get("CODEX_HOME") or home / ".codex")
        skill_dirs = [home / ".agents" / "skills", home / ".claude" / "skills"]
        codex_file = codex_home / "AGENTS.md"
        claude_file = home / ".claude" / "CLAUDE.md"

    # Codex reads AGENTS.md as a file: a symlink, or a managed copy where symlinks aren't allowed.
    # Claude Code gets a small CLAUDE.md that imports AGENTS.md, which works on every OS.
    instructions = [] if skills_only else [("copy", codex_file), ("import", claude_file)]
    return skills, skill_dirs, instructions


def instruction_ok(kind: str, destination: Path, source: Path) -> bool:
    """True if destination is already ours: a managed file or a link into this collection."""
    if is_managed(destination):
        return True
    if is_link(destination):
        return link_target(destination) in {(source / "AGENTS.md").resolve(), (source / "CLAUDE.md").resolve()}
    return False


# ---------- Install ----------


def install(*, mode: str, skills_only: bool) -> None:
    source = Path(__file__).resolve().parent
    agents_md = source / "AGENTS.md"
    skills, skill_dirs, instructions = plan(source, mode, skills_only)
    relative = mode == "project"

    # Check every destination before changing anything.
    conflicts = []
    for directory in skill_dirs:
        for folder in (directory.parent, directory):
            if is_link(folder) or (folder.exists() and not folder.is_dir()):
                conflicts.append(f"{folder} must be a real folder")
        for skill in skills:
            destination = directory / skill.name
            if is_link(destination):
                if link_target(destination) != skill.resolve():
                    conflicts.append(f"{destination} points elsewhere")
            elif destination.exists():
                conflicts.append(f"{destination} already exists")
    for kind, destination in instructions:
        if (destination.exists() or is_link(destination)) and not instruction_ok(kind, destination, source):
            conflicts.append(f"{destination} already exists")
    if conflicts:
        raise ValueError(
            "Installation stopped. No files changed.\n"
            + "\n".join(f"  {message}" for message in sorted(set(conflicts)))
            + "\nResolve the listed conflicts before retrying."
            + ("" if skills_only else "\nUse --skills-only to keep your existing AGENTS.md and CLAUDE.md files.")
        )

    for directory in skill_dirs:
        directory.mkdir(parents=True, exist_ok=True)

    # Remove links to skills that were deleted from the collection.
    removed = 0
    skills_root = (source / "skills").resolve()
    for directory in skill_dirs:
        for entry in directory.iterdir():
            if is_link(entry) and not entry.exists() and link_target(entry).parent == skills_root:
                remove_link(entry)
                removed += 1

    created = 0
    for directory in skill_dirs:
        for skill in skills:
            destination = directory / skill.name
            if not is_link(destination):
                link_directory(destination, skill, relative=relative)
                created += 1

    notes = []
    for kind, destination in instructions:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if is_link(destination):
            continue  # Already a link into this collection.
        if kind == "import":
            write_managed(destination, import_line(destination, agents_md) + "\n", source)
        elif destination.exists() or not try_link_file(destination, agents_md, relative=relative):
            write_managed(destination, agents_md.read_text(encoding="utf-8"), source)
            notes.append(
                f"{destination} is a copy, because this system doesn't allow file links. "
                "Rerun the installer after pulling to refresh it, or turn on Windows Developer Mode for a live link."
            )

    where = "this project" if mode == "project" else "your user folder, for every project"
    print(f"Connected {len(skills)} skills for Codex and Claude Code in {where}.")
    print(f"Created {created} new skill links." + ("" if skills_only else " Installed the shared instructions."))
    if removed:
        print(f"Removed {removed} links to deleted skills.")
    for note in notes:
        print(note)
    print("Start a new agent session to load the installed files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    target = parser.add_mutually_exclusive_group()
    target.add_argument("--project", action="store_true", help="Install into the project in the current folder (default).")
    target.add_argument("--user", action="store_true", help="Install into your home folder for every project.")
    parser.add_argument(
        "--skills-only",
        action="store_true",
        help="Install skills only. Leave AGENTS.md and CLAUDE.md files untouched.",
    )
    arguments = parser.parse_args()
    try:
        install(mode="user" if arguments.user else "project", skills_only=arguments.skills_only)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
