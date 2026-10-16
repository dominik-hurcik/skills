# Agent instructions and skills

Collection of my handpicked skills from all around the internet for Codex and Claude Code. Edit each skill once. Both agents read the same files.

## Skills

This collection has 35 skills in six categories. Each skill name starts with its category. Automatic skills can run when the task matches their description. Manual skills run only when you call them by name. See [Choose when a skill runs](#choose-when-a-skill-runs).

| Category | Skills | What they cover |
| --- | --- | --- |
| `engineering-` | 6 | Designing, debugging, and reviewing code |
| `planning-` | 3 | Working out what to build before building it |
| `writing-` | 3 | Docs standards and plain, human prose |
| `learning-` | 1 | Learning a new concept |
| `research-` | 1 | Researching recent public discussion |
| `marketing-` | 21 | Growth, SEO, conversion, pricing, and lifecycle marketing |

### Engineering

| Skill | Runs | What it does |
| --- | --- | --- |
| `engineering-blast-radius` | Manual | Finds what a change could break outside the diff, and proves the change is safe by running real code. |
| `engineering-codebase-design` | Automatic | Gives a shared vocabulary for designing deep modules, interfaces, and seams. |
| `engineering-diagnosing-bugs` | Automatic | Runs a diagnosis loop for hard bugs and performance regressions. |
| `engineering-domain-modeling` | Automatic | Builds a project's domain model, its `GLOSSARY.md`, and its ADRs. |
| `engineering-improve-codebase-architecture` | Manual | Scans a codebase for deepening opportunities, reports them as an HTML page, then grills through the one you pick. |
| `engineering-retro` | Manual | Runs a retrospective on a coding session. |

### Planning

| Skill | Runs | What it does |
| --- | --- | --- |
| `planning-brainstorming` | Automatic | Asks what you want and why before any creative work, then writes a design you approve before anything gets built. |
| `planning-grilling` | Automatic | Stress-tests a plan, decision, or idea one round of questions at a time. |
| `planning-sharpen` | Manual | Sharpens a task before starting: the expert approach, the real goal, and the right level of detail. |

### Writing

| Skill | Runs | What it does |
| --- | --- | --- |
| `writing-bro` | Manual | Restates the last message in plain language, with no jargon. |
| `writing-technical-writing` | Automatic | Applies a technical-writing standard to docs, RFCs, readmes, PR descriptions, and commit messages. |
| `writing-unslop` | Automatic | Cuts AI tells from any writing. |

### Learning

| Skill | Runs | What it does |
| --- | --- | --- |
| `learning-teach` | Manual | Teaches a new skill or concept in a guided workspace. |

### Research

| Skill | Runs | What it does |
| --- | --- | --- |
| `research-last30days` | Manual | Researches what people said about a topic in the last 30 days on Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, and the web. Needs Python 3.12 or newer. |

### Marketing

| Skill | Runs | What it does |
| --- | --- | --- |
| `marketing-ads` | Automatic | Plans and audits paid campaigns on Google, Meta, LinkedIn, X, and other ad platforms. |
| `marketing-ai-seo` | Automatic | Optimizes content so AI search engines and LLMs cite it. |
| `marketing-analytics` | Automatic | Sets up and audits analytics tracking, such as GA4, events, and UTMs. |
| `marketing-app-store-listing` | Automatic | Audits and improves an App Store or Google Play listing. |
| `marketing-churn-prevention` | Automatic | Builds cancel flows, save offers, and failed-payment recovery. |
| `marketing-content-strategy` | Automatic | Plans what content to create and which topics to cover. |
| `marketing-cro` | Automatic | Improves conversion on marketing pages and forms. |
| `marketing-customer-research` | Automatic | Runs and synthesizes customer research, such as interviews, reviews, and ICP work. |
| `marketing-directory-submissions` | Automatic | Submits a product to startup, SaaS, AI, and review directories. |
| `marketing-emails` | Automatic | Writes and improves email sequences and lifecycle flows. |
| `marketing-image` | Automatic | Creates and edits marketing images, such as blog heroes, social graphics, and mockups. |
| `marketing-launch` | Automatic | Plans product launches, feature announcements, and Product Hunt. |
| `marketing-onboarding` | Automatic | Improves post-signup onboarding and activation. |
| `marketing-paywalls` | Automatic | Designs in-app paywalls, upgrade screens, and feature gates. |
| `marketing-popups` | Automatic | Designs popups, modals, slide-ins, and banners that convert. |
| `marketing-pricing` | Automatic | Decides pricing, packaging, and monetization. |
| `marketing-programmatic-seo` | Automatic | Builds SEO pages at scale from templates and data. |
| `marketing-seo-audit` | Automatic | Audits a site for technical and on-page SEO issues. |
| `marketing-signup` | Automatic | Improves signup, registration, and trial activation flows. |
| `marketing-site-architecture` | Automatic | Plans page hierarchy, navigation, URL structure, and internal links. |
| `marketing-social` | Automatic | Creates and schedules social posts, and runs social listening. |

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
$skill-name Describe the task.
```

In Claude Code, start the message with the skill's slash command:

```text
/skill-name Describe the task.
```

Installing a skill makes it available. It does not make every skill run on every response.

## Add a skill

1. Create a folder under `skills/` whose name starts with the skill's category, such as `skills/engineering-my-skill/`. Use the same name in the `name` field of `SKILL.md`, and add the skill to the tables in [Skills](#skills).
2. Add a `SKILL.md` file with a name, description, and instructions:

   ```md
   ---
   name: engineering-my-skill
   description: Explain when the agent should use this skill.
   ---

   Write the steps the agent should follow here.
   ```

3. Keep any scripts, references, and assets inside that skill's folder.
4. Write instructions that work in both agents. To use another skill, write "load the `other-skill` skill". Don't name agent-specific tools such as Claude Code's Skill tool, and don't use `/name` or `$name` syntax inside a skill.
5. Set when the skill runs. See [Choose when a skill runs](#choose-when-a-skill-runs).
6. Commit the new skill to this repository.
7. In each installed project, pull the update and rerun the installer:

   ```sh
   git -C .agent-instructions pull --ff-only
   python3 .agent-instructions/install.py
   ```

   For a skills-only installation, add `--skills-only` to the installer command each time.

The installer adds links for new skills, keeps existing links, and removes links to skills deleted from this collection. Changes to an existing skill take effect as soon as its files are updated in the project's clone. Start a new agent session if it still uses the old instructions.

## Choose when a skill runs

Agents can select a skill when its description matches the task. You can also request a skill by name.

Claude Code uses `disable-model-invocation: true` in `SKILL.md` to make a skill manual-only. Codex uses `policy.allow_implicit_invocation: false` in that skill's `agents/openai.yaml` for the same purpose. Configure both if you want the same behavior in both agents.

A skill without either setting can run automatically in both agents. When you add or change a skill, check both files. A setting in only one file makes the skill manual-only in one agent and automatic in the other.

A skill that other skills load must allow automatic selection. A manual-only skill can't be loaded by the agent, only by you.

For behavior you want on every response, add a rule to `AGENTS.md` and allow the agent to invoke the required skill. Skill matching alone does not guarantee that behavior.

## Edit shared instructions

Edit `AGENTS.md`. `CLAUDE.md` contains `@AGENTS.md`, so Claude Code imports the same instructions.

Commit changes in the source repository, then pull them into each project's `.agent-instructions` clone. Existing links continue to work.

## References

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [pstack source](https://github.com/cursor/plugins/tree/main/pstack)
- [Matt Pocock's engineering skills](https://github.com/mattpocock/skills/tree/main/skills/engineering)
