# Agent instructions and skills

My shared instructions and selected skills for Codex and Claude Code. Edit each skill once. Both agents read the same files.

## Install in a project

Requires Git and Python 3.9 or newer. This setup uses symbolic links on macOS and Linux.

Open a terminal in your project's root folder and run:

```sh
git clone https://github.com/dominik-hurcik/skills.git .agent-instructions
python3 .agent-instructions/install.py
```

The installer creates these links in your project:

| Project path | What it loads |
| --- | --- |
| `AGENTS.md` | Shared instructions for Codex |
| `CLAUDE.md` | Imports the shared instructions for Claude Code |
| `.agents/skills/<name>` | Skills available to Codex |
| `.claude/skills/<name>` | The same skills available to Claude Code |

Start a new agent session in the project after installation. Keep `.agent-instructions` inside the project, since the links point into it.

If any destination contains an existing file or a different link, the installer stops before changing anything. To keep your repo's existing instructions, use `--skills-only`.

For a personal install, add `.agent-instructions/` to the project's `.gitignore` so Git skips the nested clone. Each new checkout needs its own installation.

## Install only skills

Use this mode when your repo already has custom `AGENTS.md` or `CLAUDE.md` instructions that you want to keep.

For a first installation, run these commands from your project's root:

```sh
git clone https://github.com/dominik-hurcik/skills.git .agent-instructions
python3 .agent-instructions/install.py --skills-only
```

If `.agent-instructions` already exists, update it and run:

```sh
git -C .agent-instructions pull --ff-only
python3 .agent-instructions/install.py --skills-only
```

This mode adds links under `.agents/skills` and `.claude/skills`. It leaves `AGENTS.md` and `CLAUDE.md` untouched and does not create them if they are missing. Existing skills with conflicting names still stop installation before any changes.

Use `--skills-only` each time you rerun the installer for this project. Start a new agent session after installation to pick up the skills.

## Use a skill

In Codex CLI or its IDE extension, mention the skill with `$`:

```text
$unslop Rewrite this paragraph.
$diagnosing-bugs Diagnose this error.
```

In Claude Code, start the message with the skill's slash command:

```text
/unslop Rewrite this paragraph.
/diagnosing-bugs Diagnose this error.
```

Installing a skill makes it available. It does not make every skill run on every response.

## Add a skill

1. Create a folder under `skills/`, such as `skills/my-skill/`.
2. Add a `SKILL.md` file with a name, description, and instructions:

   ```md
   ---
   name: my-skill
   description: Explain when the agent should use this skill.
   ---

   Write the steps the agent should follow here.
   ```

3. Keep any scripts, references, and assets inside that skill's folder.
4. Commit the new skill to this repository.
5. In each installed project, pull the update and rerun the installer:

   ```sh
   git -C .agent-instructions pull --ff-only
   python3 .agent-instructions/install.py
   ```

   For a skills-only installation, add `--skills-only` to the installer command each time.

The installer adds links for new skills and keeps existing links. Changes to an existing skill take effect as soon as its files are updated in the project's clone. Start a new agent session if it still uses the old instructions.

## Choose when a skill runs

Agents can select a skill when its description matches the task. You can also request a skill by name.

Claude Code uses `disable-model-invocation: true` in `SKILL.md` to make a skill manual-only. Codex uses `policy.allow_implicit_invocation: false` in that skill's `agents/openai.yaml` for the same purpose. Configure both if you want the same behavior in both agents.

Six skills in this collection currently have the Claude manual-only setting. `diagnosing-bugs` allows automatic selection. The Codex settings have not been aligned with those manual-only settings.

For behavior you want on every response, add a rule to `AGENTS.md` and allow the agent to invoke the required skill. Skill matching alone does not guarantee that behavior.

## Edit shared instructions

Edit `AGENTS.md`. `CLAUDE.md` contains `@AGENTS.md`, so Claude Code imports the same instructions.

Commit changes in the source repository, then pull them into each project's `.agent-instructions` clone. Existing links continue to work.

## Skills that need adaptation

Some skills came from Cursor's pstack collection. `why` still refers to Cursor tools, Cursor model settings, and companion workflows outside this collection. Those instructions need adaptation for Codex and Claude Code.

## References

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [pstack source](https://github.com/cursor/plugins/tree/main/pstack)
- [Matt Pocock's engineering skills](https://github.com/mattpocock/skills/tree/main/skills/engineering)
