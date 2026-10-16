#!/usr/bin/env python3
"""Install, update, or remove this skill collection for Codex and Claude Code.

Run it with no options and it asks you what to do. It works on macOS, Linux, and Windows.

  python3 install.py

You can also run this file on its own, without cloning the collection first.
It then downloads the collection for you.

Options skip the questions, for scripts:

  --user            install for every project on this computer
  --project         install into the Git repository in the current folder
  --remove          remove an install (combine with --user or --project)
  --skills-only     install skills only, not the shared instructions
  --gitignore       in project mode, add the installed files to .gitignore
  --no-gitignore    in project mode, leave .gitignore alone
  --no-pull         don't fetch the latest version first
  --yes             accept the recommended answer to every remaining question
"""

import argparse
import hashlib
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

REPO_URL = "https://github.com/dominik-hurcik/skills.git"
USER_CLONE = "agent-skills"
PROJECT_CLONE = ".agent-instructions"
WINDOWS = os.name == "nt"
MARKER = "<!-- Managed by install.py from "
IMPORT_NOTE = "<!-- Added by install.py: loads the shared instructions -->"
GITIGNORE_START = "# >>> agent skills (managed by install.py)"
GITIGNORE_END = "# <<< agent skills"
BLOCK_START = "<!-- >>> shared instructions (managed by install.py, rerun it to refresh) -->"
BLOCK_END = "<!-- <<< shared instructions -->"
BACKUP_SUFFIX = ".backup"


class Stop(Exception):
    """Ends the run with a message and no changes."""


# ---------- Questions ----------


class Asker:
    def __init__(self, assume_yes: bool):
        self.assume_yes = assume_yes

    def _read(self, prompt: str) -> str:
        try:
            return input(prompt).strip()
        except EOFError:
            raise Stop("No answer received. Run the installer in a terminal, or pass --yes.")

    def choice(self, question: str, options: list, default: int) -> int:
        """Return the 0-based index of the chosen option."""
        if self.assume_yes:
            return default
        print(f"\n{question}")
        for number, option in enumerate(options, 1):
            print(f"  {number}) {option}" + ("  (recommended)" if number - 1 == default else ""))
        while True:
            answer = self._read(f"Choose 1-{len(options)} [{default + 1}]: ")
            if not answer:
                return default
            if answer.isdigit() and 1 <= int(answer) <= len(options):
                return int(answer) - 1
            print(f"Please type a number from 1 to {len(options)}.")

    def yes_no(self, question: str, default: bool) -> bool:
        if self.assume_yes:
            return default
        hint = "Y/n" if default else "y/N"
        while True:
            answer = self._read(f"\n{question} [{hint}]: ").lower()
            if not answer:
                return default
            if answer in ("y", "yes"):
                return True
            if answer in ("n", "no"):
                return False
            print("Please answer y or n.")


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


def points_into(path: Path, source: Path) -> bool:
    return is_link(path) and link_target(path).parent == source.resolve()


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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def has_import(path: Path, line: str) -> bool:
    return any(existing.strip() == line for existing in read_text(path).splitlines())


def strip_block(text: str, start: str, end: str) -> str:
    """Remove every block between start and end, markers included."""
    out, inside = [], False
    for line in text.splitlines(keepends=True):
        if line.strip() == start:
            inside = True
            continue
        if line.strip() == end:
            inside = False
            continue
        if not inside:
            out.append(line)
    return "".join(out).rstrip("\n") + ("\n" if out else "")


def write_text(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as file:
        file.write(text)


def backup_path(path: Path) -> Path:
    return path.with_name(path.name + BACKUP_SUFFIX)


# ---------- Git ----------


def git(*args: str, cwd: Path = None, check: bool = True) -> subprocess.CompletedProcess:
    if shutil.which("git") is None:
        raise Stop("Git isn't installed. Install Git, then run the installer again.")
    return subprocess.run(["git", *args], cwd=cwd, check=check, capture_output=True, text=True)


def repo_root(folder: Path):
    result = git("rev-parse", "--show-toplevel", cwd=folder, check=False)
    return Path(result.stdout.strip()).resolve() if result.returncode == 0 else None


def is_collection(folder: Path) -> bool:
    return (folder / "skills").is_dir() and (folder / "AGENTS.md").is_file()


def clone_to(target: Path) -> Path:
    if is_collection(target):
        return target.resolve()
    if target.exists():
        raise Stop(f"{target} already exists and isn't this collection. Move it away, then try again.")
    print(f"\nDownloading the collection to {target} ...")
    # Windows limits paths to 260 characters unless Git is told to allow longer ones.
    options = ["-c", "core.longpaths=true"] if WINDOWS else []
    result = git(*options, "clone", "--quiet", REPO_URL, str(target), check=False)
    if result.returncode != 0 or not is_collection(target):
        raise Stop("Couldn't download the collection.\n" + (result.stderr or result.stdout).strip())
    if WINDOWS:
        git("-C", str(target), "config", "core.longpaths", "true", check=False)
    return target.resolve()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else ""


def pull_latest(source: Path, ask: Asker) -> bool:
    """Pull the collection. Return True if install.py itself changed."""
    if not (source / ".git").exists():
        return False
    if not ask.yes_no("Get the latest version of the collection first (git pull)?", True):
        return False
    before = file_hash(source / "install.py")
    result = git("-C", str(source), "pull", "--ff-only", check=False)
    if result.returncode != 0:
        print("Couldn't pull the latest version. Continuing with the copy you have.")
        print((result.stderr or result.stdout).strip())
        return False
    print("The collection is up to date.")
    return file_hash(source / "install.py") != before


# ---------- Plan ----------


class Target:
    """Where an install goes, and the files it owns there."""

    def __init__(self, mode: str, root: Path, source: Path):
        self.mode = mode
        self.root = root
        self.source = source
        if mode == "user":
            codex_home = Path(os.environ.get("CODEX_HOME") or root / ".codex")
            self.skill_dirs = [root / ".agents" / "skills", root / ".claude" / "skills"]
            self.codex_file = codex_home / "AGENTS.md"
            self.claude_file = root / ".claude" / "CLAUDE.md"
        else:
            self.skill_dirs = [root / ".agents" / "skills", root / ".claude" / "skills"]
            self.codex_file = root / "AGENTS.md"
            self.claude_file = root / "CLAUDE.md"
        self.relative = mode == "project"
        self.skills = sorted(path.parent for path in (source / "skills").glob("*/SKILL.md"))

    @property
    def agents_md(self) -> Path:
        return self.source / "AGENTS.md"

    def ours(self, path: Path) -> bool:
        """True if path is a link into the collection or a file this installer wrote."""
        return is_managed(path) or (is_link(path) and link_target(path) in {
            self.agents_md.resolve(), (self.source / "CLAUDE.md").resolve()})


def skill_conflicts(target: Target) -> list:
    conflicts = []
    for directory in target.skill_dirs:
        for folder in (directory.parent, directory):
            if is_link(folder) or (folder.exists() and not folder.is_dir()):
                conflicts.append(f"{folder} must be a real folder")
        for skill in target.skills:
            destination = directory / skill.name
            if is_link(destination):
                if link_target(destination) != skill.resolve():
                    conflicts.append(f"{destination} points somewhere else")
            elif destination.exists():
                conflicts.append(f"{destination} already exists and isn't from this collection")
    return sorted(set(conflicts))


# ---------- Install ----------


def link_skills(target: Target) -> tuple:
    for directory in target.skill_dirs:
        directory.mkdir(parents=True, exist_ok=True)
    removed = 0
    skills_root = (target.source / "skills").resolve()
    for directory in target.skill_dirs:
        for entry in directory.iterdir():
            if is_link(entry) and not entry.exists() and link_target(entry).parent == skills_root:
                remove_link(entry)
                removed += 1
    created = 0
    for directory in target.skill_dirs:
        for skill in target.skills:
            destination = directory / skill.name
            if not is_link(destination):
                link_directory(destination, skill, relative=target.relative)
                created += 1
    return created, removed


def install_codex_file(target: Target) -> str:
    path = target.codex_file
    path.parent.mkdir(parents=True, exist_ok=True)
    if is_link(path):
        return f"{path} already links to the shared instructions."
    if path.exists() or not try_link_file(path, target.agents_md, relative=target.relative):
        write_managed(path, target.agents_md.read_text(encoding="utf-8"), target.source)
        return (f"{path} is a copy of the shared instructions, because this system doesn't allow file links. "
                "Rerun the installer after updates to refresh it, or turn on Windows Developer Mode for a live link.")
    return f"Linked {path} to the shared instructions."


def install_claude_file(target: Target) -> str:
    path = target.claude_file
    path.parent.mkdir(parents=True, exist_ok=True)
    line = import_line(path, target.agents_md)
    if is_link(path):
        return f"{path} already links to the shared instructions."
    write_managed(path, line + "\n", target.source)
    return f"Wrote {path}, which loads the shared instructions."


def add_import(path: Path, line: str) -> str:
    if has_import(path, line):
        return f"{path} already loads the shared instructions."
    text = read_text(path)
    with path.open("a", encoding="utf-8", newline="\n") as file:
        file.write(("" if text.endswith("\n") or not text else "\n") + f"\n{IMPORT_NOTE}\n{line}\n")
    return f"Added one line to {path} that loads the shared instructions."


def append_block(path: Path, body: str) -> str:
    """Put a copy of the shared instructions at the end of the user's own file, or refresh that copy."""
    had_block = BLOCK_START in read_text(path)
    text = strip_block(read_text(path), BLOCK_START, BLOCK_END)
    block = f"{BLOCK_START}\n\n{body.strip()}\n\n{BLOCK_END}\n"
    write_text(path, text + ("\n" if text.strip() else "") + block)
    if had_block:
        return f"Refreshed the shared instructions at the end of {path}."
    return f"Added the shared instructions to the end of {path}. Your own text stays on top."


def back_up(path: Path) -> str:
    backup = backup_path(path)
    os.replace(path, backup)
    return f"Saved your old {path.name} as {backup}."


def gitignore_lines(target: Target, wrote_codex: bool, wrote_claude: bool) -> list:
    """Build the block from the skills found now, so new skills are always covered."""
    try:
        clone = target.source.relative_to(target.root).as_posix()
    except ValueError:
        clone = PROJECT_CLONE
    lines = [f"/{clone}/"]
    prefixed = all(skill.name.startswith("dh-") for skill in target.skills)
    for folder in (".agents/skills", ".claude/skills"):
        if prefixed:
            lines.append(f"/{folder}/dh-*")
        else:
            lines.extend(f"/{folder}/{skill.name}" for skill in target.skills)
    if wrote_codex:
        lines.append("/AGENTS.md")
    if wrote_claude:
        lines.append("/CLAUDE.md")
    return lines


def update_gitignore(root: Path, lines: list) -> str:
    path = root / ".gitignore"
    existed = path.exists()
    text = strip_block(read_text(path), GITIGNORE_START, GITIGNORE_END)
    block = "\n".join([GITIGNORE_START, *lines, GITIGNORE_END]) + "\n"
    write_text(path, text + ("\n" if text.strip() else "") + block)
    return f"{'Updated' if existed else 'Created'} {path}."


# ---------- Remove ----------


def remove_install(target: Target) -> list:
    done = []
    count = 0
    skills_root = (target.source / "skills").resolve()
    for directory in target.skill_dirs:
        if not directory.is_dir():
            continue
        for entry in directory.iterdir():
            if is_link(entry) and link_target(entry).parent == skills_root:
                remove_link(entry)
                count += 1
    done.append(f"Removed {count} skill links.")
    for path in (target.codex_file, target.claude_file):
        backup = backup_path(path)
        if target.ours(path):
            remove_link(path) if is_link(path) else path.unlink()
            done.append(f"Removed {path}.")
            if backup.is_file():
                os.replace(backup, path)
                done.append(f"Put your old {path.name} back from {backup.name}.")
            continue
        if path.is_file() and BLOCK_START in read_text(path):
            write_text(path, strip_block(read_text(path), BLOCK_START, BLOCK_END))
            done.append(f"Removed the shared instructions from the end of {path}. Your own text stays.")
        if path.is_file() and IMPORT_NOTE in read_text(path):
            lines = read_text(path).splitlines(keepends=True)
            kept = []
            skip_next = False
            for line in lines:
                if line.strip() == IMPORT_NOTE:
                    skip_next = True
                    continue
                if skip_next:
                    skip_next = False
                    continue
                kept.append(line)
            path.write_text("".join(kept).rstrip("\n") + "\n", encoding="utf-8")
            done.append(f"Removed the import line from {path}.")
    gitignore = target.root / ".gitignore"
    if target.mode == "project" and GITIGNORE_START in read_text(gitignore):
        rest = strip_block(read_text(gitignore), GITIGNORE_START, GITIGNORE_END)
        if rest.strip():
            gitignore.write_text(rest, encoding="utf-8")
            done.append(f"Removed the agent skills block from {gitignore}.")
        else:
            gitignore.unlink()
            done.append(f"Removed {gitignore}, which only held the agent skills block.")
    done.append(f"The collection itself is still in {target.source}. Delete that folder if you don't need it.")
    return done


# ---------- Flow ----------


def choose_mode(args, ask: Asker) -> tuple:
    """Return (action, mode), where action is install or remove."""
    if args.remove:
        action = "remove"
    elif args.user or args.project:
        action = "install"
    else:
        picked = ask.choice(
            "What do you want to do?",
            ["Install or update for every project on this computer (user mode)",
             "Install or update for one project only (project mode)",
             "Remove an install"],
            0)
        if picked < 2:
            return "install", ["user", "project"][picked]
        action = "remove"
    if args.user:
        return action, "user"
    if args.project:
        return action, "project"
    mode = ask.choice("Which install do you want to remove?",
                      ["The one for every project (user mode)", "The one in a project (project mode)"], 0)
    return action, ["user", "project"][mode]


def confirm_project(ask: Asker, action: str) -> Path:
    into = "remove the install from" if action == "remove" else "install into"
    here = Path.cwd().resolve()
    root = repo_root(here)
    if root is None:
        print(f"\nThe current folder isn't inside a Git repository:\n  {here}")
        print("Project mode installs into a project's top folder. Open a terminal in your project, then run the installer again.")
        if not ask.yes_no(f"{into[0].upper() + into[1:]} this folder anyway?", False):
            raise Stop("Nothing changed.")
        return here
    if root != here:
        print(f"\nYou're in a subfolder. The project's top folder is:\n  {root}")
    else:
        print(f"\nThe project's top folder is:\n  {root}")
    if not ask.yes_no(f"Is this the project you want to {into}?", True):
        raise Stop("Nothing changed. Open a terminal in the right project, then run the installer again.")
    return root


def locate_source(mode: str, root: Path) -> Path:
    """Find the collection, or download it to the right place."""
    script_dir = Path(__file__).resolve().parent
    if mode == "user":
        if is_collection(script_dir):
            return script_dir
        return clone_to(Path.home() / USER_CLONE)
    project_copy = root / PROJECT_CLONE
    if is_collection(script_dir) and root in script_dir.parents:
        return script_dir
    if not is_collection(project_copy):
        print(f"\nProject mode keeps its own copy of the collection inside the project, in {PROJECT_CLONE}/.")
    return clone_to(project_copy)


def imports_file(path: Path, other: Path) -> bool:
    """True if path already loads other with an @import, such as a CLAUDE.md that holds @AGENTS.md."""
    return path.parent == other.parent and has_import(path, "@" + other.name)


def plan_existing(path: Path, target: Target, ask: Asker, agent: str):
    """Decide what to do with one instructions file. Return install, add, replace, or None to leave it alone."""
    if not path.exists() or target.ours(path):
        return "install"
    text = read_text(path)
    if BLOCK_START in text or IMPORT_NOTE in text or has_import(path, import_line(path, target.agents_md)):
        print(f"\n{path} holds your own text and the shared instructions. The installer refreshes its part only.")
        return "add"
    backup = backup_path(path)
    how = ("a copy of mine goes at the end, in a marked part the installer refreshes on every run"
           if path == target.codex_file else "one line goes at the end that loads mine")
    picked = ask.choice(
        f"You already have your own instructions for {agent} in:\n  {path}\nWhat should happen to them?",
        [f"Keep yours and add mine. Yours stay on top, and {how}.",
         f"Keep yours only. {agent} won't get my instructions here.",
         f"Replace yours with mine. Yours are saved as {backup.name}, and remove puts them back."],
        0)
    if picked == 1:
        return None
    if picked == 2:
        if backup.exists():
            raise Stop(f"{backup} already exists, so there's no safe place for your old file. "
                       "Move it away, then try again. Nothing changed.")
        return "replace"
    return "add"


def run(args) -> None:
    ask = Asker(args.yes)
    print("Agent skills installer for Codex and Claude Code.")
    script_dir = Path(__file__).resolve().parent
    if is_collection(script_dir) and not args.no_pull:
        if pull_latest(script_dir, ask):
            print("The installer itself changed, so it's restarting with the new version.", flush=True)
            command = [sys.executable, str(script_dir / "install.py"), *sys.argv[1:], "--no-pull"]
            if not sys.stdin.isatty():
                # Python has already read piped answers into its buffer, so pass the rest on.
                sys.exit(subprocess.run(command, input=sys.stdin.read(), text=True).returncode)
            if WINDOWS:
                # On Windows, execv starts a new process and ends this one, so the terminal
                # takes back its prompt while the new installer still waits for answers.
                sys.exit(subprocess.call(command))
            os.execv(sys.executable, command)

    action, mode = choose_mode(args, ask)
    root = confirm_project(ask, action) if mode == "project" else Path.home().resolve()

    if action == "remove":
        # Removing never downloads anything. It needs the copy the install points to.
        candidates = [script_dir, Path.home() / USER_CLONE] if mode == "user" else [root / PROJECT_CLONE]
        if mode == "project" and root in script_dir.parents:
            candidates.insert(0, script_dir)
        source = next((c.resolve() for c in candidates if is_collection(c)), None)
        if source is None:
            raise Stop(f"Couldn't find the collection for this {mode}-mode install, so there's nothing to remove.")
        target = Target(mode, root, source)
        if not ask.yes_no(f"Remove the {mode}-mode install from {root}?", True):
            raise Stop("Nothing changed.")
        print()
        for line in remove_install(target):
            print(line)
        return

    source = locate_source(mode, root)
    unfilled = [part for part in source.parts if part.startswith(("$", "%"))]
    if unfilled:
        raise Stop(
            f"The collection is in a folder named {unfilled[0]}:\n  {source}\n"
            f"Your terminal didn't fill in {unfilled[0]}, so Git made a folder with that name. "
            "This happens when you paste the PowerShell commands into Command Prompt. "
            "Delete that folder, then use the commands for your terminal from the README. Nothing changed.")
    target = Target(mode, root, source)
    if not target.skills:
        raise Stop(f"No skills found in {source}.")

    conflicts = skill_conflicts(target)
    if conflicts:
        raise Stop("Installation stopped. Nothing changed.\n" + "\n".join(f"  {c}" for c in conflicts))

    # Shared instructions.
    install_instructions = not args.skills_only and ask.choice(
        "Install my shared instructions (AGENTS.md) as well as the skills?",
        ["Skills and shared instructions", "Skills only"], 0) == 0
    codex_plan = claude_plan = None
    if install_instructions:
        codex_plan = plan_existing(target.codex_file, target, ask, "Codex")
        if codex_plan in ("install", "add", "replace") and imports_file(target.claude_file, target.codex_file):
            print(f"\n{target.claude_file.name} already loads {target.codex_file.name}, so Claude Code gets the "
                  "shared instructions from there. It needs no change.")
        else:
            claude_plan = plan_existing(target.claude_file, target, ask, "Claude Code")

    # .gitignore, project mode only.
    use_gitignore = False
    if mode == "project":
        if args.gitignore:
            use_gitignore = True
        elif not args.no_gitignore:
            use_gitignore = ask.yes_no(
                "Add the installed files to the project's .gitignore, so they aren't committed? "
                "Pick this if only you use these skills.", True)

    # Summary before changing anything. Paths are shown relative to the project or home folder.
    def short(path: Path) -> str:
        try:
            return ("~/" if mode == "user" else "") + path.resolve().relative_to(root).as_posix()
        except ValueError:
            return str(path)

    print(f"\nThe installer will make these changes in {root}:")
    print(f"  - link {len(target.skills)} skills into {short(target.skill_dirs[0])} and {short(target.skill_dirs[1])}")
    for path, plan in ((target.codex_file, codex_plan), (target.claude_file, claude_plan)):
        if plan == "install":
            print(f"  - write {short(path)}, which loads the shared instructions")
        elif plan == "add":
            print(f"  - add the shared instructions to the end of {short(path)}, below your own text")
        elif plan == "replace":
            print(f"  - save your {short(path)} as {short(backup_path(path))}, then write mine in its place")
    if use_gitignore:
        print(f"  - add the installed files to {short(root / '.gitignore')}")
    if not ask.yes_no("Go ahead?", True):
        raise Stop("Nothing changed.")

    print()
    created, removed = link_skills(target)
    print(f"Linked {len(target.skills)} skills for both agents ({created} new links, {removed} old links removed).")
    if codex_plan == "replace":
        print(back_up(target.codex_file))
    if codex_plan in ("install", "replace"):
        print(install_codex_file(target))
    elif codex_plan == "add":
        print(append_block(target.codex_file, target.agents_md.read_text(encoding="utf-8")))
    if claude_plan == "replace":
        print(back_up(target.claude_file))
    if claude_plan in ("install", "replace"):
        print(install_claude_file(target))
    elif claude_plan == "add":
        print(add_import(target.claude_file, import_line(target.claude_file, target.agents_md)))
    if use_gitignore:
        print(update_gitignore(root, gitignore_lines(target, codex_plan == "install", claude_plan == "install")))
    print("\nDone. Start a new agent session to load the skills.")
    rerun = "python3" if not WINDOWS else "py"
    print(f"To update later, run:  {rerun} {source / 'install.py'}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    where = parser.add_mutually_exclusive_group()
    where.add_argument("--user", action="store_true", help="Install for every project on this computer.")
    where.add_argument("--project", action="store_true", help="Install into the Git repository in the current folder.")
    parser.add_argument("--remove", action="store_true", help="Remove an install instead.")
    parser.add_argument("--skills-only", action="store_true", help="Install skills only, not the shared instructions.")
    ignore = parser.add_mutually_exclusive_group()
    ignore.add_argument("--gitignore", action="store_true", help="In project mode, add the installed files to .gitignore.")
    ignore.add_argument("--no-gitignore", action="store_true", help="In project mode, leave .gitignore alone.")
    parser.add_argument("--no-pull", action="store_true", help="Don't fetch the latest version first.")
    parser.add_argument("--yes", action="store_true", help="Accept the recommended answer to every remaining question.")
    args = parser.parse_args()
    try:
        run(args)
    except Stop as stop:
        print(f"\n{stop}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nCancelled. Nothing more changed.", file=sys.stderr)
        sys.exit(1)
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"\n{error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
