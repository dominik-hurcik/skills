# Agent instructions and skills

Collection of my handpicked skills from all around the internet for Codex and Claude Code. Edit each skill once. Both agents read the same files.

The collection has 61 skills and my shared instructions. A skill is a set of instructions for one kind of job, such as reviewing a contract or fixing a bug. Every skill name starts with `dh-`, so you can tell my skills apart from built-in ones.

## Contents

- [Install](#install)
  - [Install on macOS](#install-on-macos)
  - [Install on Windows](#install-on-windows)
  - [What the installer asks](#what-the-installer-asks)
  - [Update](#update) · [Remove](#remove)
- [Use a skill](#use-a-skill)
- [When skills run](#when-skills-run)
- [The skills](#the-skills)
  - [Engineering](#engineering) · [Planning](#planning) · [Writing](#writing) · [Learning](#learning) · [Research](#research) · [Marketing](#marketing) · [Legal](#legal)
- [Add a skill](#add-a-skill)
- [Set automatic or manual](#set-automatic-or-manual)
- [Edit the shared instructions](#edit-the-shared-instructions)
- [References](#references)

## Install

You need Git and Python 3.9 or newer. The installer asks you a few questions and does the rest.

### Install on macOS

These steps also work on Linux. Open Terminal and run:

```sh
git clone https://github.com/dominik-hurcik/skills.git ~/agent-skills
python3 ~/agent-skills/install.py
```

Answer the questions, then start a new agent session.

### Install on Windows

Open PowerShell and run:

```powershell
git clone https://github.com/dominik-hurcik/skills.git $HOMEgent-skills
py $HOMEgent-skills\install.py
```

If `py` isn't found, use `python` instead. Answer the questions, then start a new agent session.

### What the installer asks

1. **Where to install.** Pick user mode for every project on this computer. Pick project mode for one project only. User mode is recommended.
2. **Which project, in project mode.** Run the installer from inside your project. It finds the project's top folder and asks you to confirm it. It refuses a folder that isn't a Git repository, unless you say yes.
3. **What to install.** Pick skills and my shared instructions, or skills only.
4. **What to do with your own instructions, if you already have some.** It asks once for `AGENTS.md` and once for `CLAUDE.md`:
   - Keep yours and add mine. This is recommended. Your text stays on top. `AGENTS.md` gets a copy of mine at the end, in a marked part that every rerun refreshes. `CLAUDE.md` gets one line at the end that loads mine.
   - Keep yours only. Nothing changes, and that agent won't get my instructions.
   - Replace yours with mine. Yours are saved as `AGENTS.md.backup` or `CLAUDE.md.backup` first. Remove puts them back.
5. **Whether to update `.gitignore`, in project mode.** Say yes if only you use these skills. It creates `.gitignore` if there's none, or adds a marked block to the end of yours.
6. **Whether to go ahead.** It shows every change first, and changes nothing until you say yes.

In project mode, the installer keeps its own copy of the collection in `.agent-instructions/` inside the project. If that copy is missing, it downloads it there for you.

Each run finds the skills again. New skills get linked, and links to deleted or renamed skills get removed.

### What gets installed

| Mode | Skills | Shared instructions |
| --- | --- | --- |
| User mode | `~/.agents/skills/` for Codex and `~/.claude/skills/` for Claude Code | `~/.codex/AGENTS.md` for Codex (or `$CODEX_HOME/AGENTS.md`), and `~/.claude/CLAUDE.md` for Claude Code |
| Project mode | `.agents/skills/` and `.claude/skills/` in the project | `AGENTS.md` and `CLAUDE.md` in the project |

### Update

Run the installer again, the same way you installed it. It asks whether to get the latest version first, then links new skills and removes old ones.

On macOS:

```sh
python3 ~/agent-skills/install.py
```

On Windows:

```powershell
py $HOMEgent-skills\install.py
```

For a project install, run `.agent-instructions/install.py` from inside the project instead.

### Remove

Run the installer and pick "Remove an install". It removes the skill links, its own instruction files, the part it added to your `AGENTS.md` or `CLAUDE.md`, and its block in `.gitignore`. If you picked replace, it puts your old files back. Your own text stays. It keeps the downloaded collection, so you can delete that folder yourself.

### Run it without questions

For scripts, pass options instead of answering questions. For example, `python3 install.py --user --yes` installs for every project with the recommended answers. Run `python3 install.py --help` to see every option.

### How the installer connects things

The installer doesn't copy the skills. It makes shortcuts that point back to your clone, so a `git pull` updates everything at once.

- **Skill folders.** On macOS and Linux, these are symlinks, a kind of shortcut. On Windows, they're junctions, a folder shortcut that needs no admin rights.
- **`CLAUDE.md`.** A tiny file with one `@` line that loads `AGENTS.md`. Claude Code always sees the latest version.
- **`AGENTS.md`.** A symlink on macOS and Linux. Windows allows file symlinks only with Developer Mode on. Without it, the installer writes a copy instead, and refreshes the copy each time it runs.

The installer marks everything it writes, so on later runs it only updates its own files and links, never yours.

## Use a skill

To be sure a skill runs, call it by name at the start of your message.

In Claude Code:

```text
/dh-bro Explain the last message again.
```

In Codex:

```text
$dh-bro Explain the last message again.
```

You don't have to call every skill. Many run on their own, as [When skills run](#when-skills-run) explains.

## When skills run

Each skill runs in one of three ways.

### On its own (28 skills)

The agent reads a short description of every skill when a session starts. When your request matches one, it uses that skill without being asked.

For example, "our signup page converts badly" pulls in `dh-marketing-signup`. "This test fails only in CI" pulls in `dh-engineering-diagnosing-bugs`.

This isn't guaranteed. The agent decides, and a vague request may match nothing. If a skill matters, call it by name.

These skills run on their own because their job is narrow, and using one by mistake costs little:
- all 21 marketing skills
- `dh-engineering-codebase-design`, `dh-engineering-diagnosing-bugs`, and `dh-engineering-domain-modeling`
- `dh-planning-grilling`
- `dh-technical-writing`, `dh-unslop`, and `dh-drunk-grandma`

### Because the shared instructions say so (2 skills)

`AGENTS.md` holds my rules for every agent. It names two skills to use at set moments:
- `dh-unslop` before writing anything longer than a short reply, such as docs or commit messages
- `dh-drunk-grandma` when explaining an idea, a decision, or a trade-off

`AGENTS.md` also keeps five core rules for every reply. One example is "no em dashes". Those rules work even when the agent doesn't open a skill.

### Only when you call it (33 skills)

These never start on their own. Each has a reason:
- **They take over the session.** `dh-planning-brainstorming` won't let anything be built until you approve a design. `dh-teach` sets up a learning workspace. `dh-engineering-improve-codebase-architecture` scans the whole codebase and writes a report. `dh-engineering-retro` looks back over the whole session.
- **You choose the moment.** `dh-planning-sharpen` and `dh-bro` rework something you point at. `dh-engineering-blast-radius` runs real code to check a change is safe. `dh-engineering-code-security-review` runs only when asked, by design.
- **They cost time or money.** `dh-research-last30days` takes a few minutes. It can also spend credits on paid services, if you've added keys for them.
- **They're legal.** All 24 legal skills cover overlapping topics, so they'd compete in every SaaS project. Legal work should also come from a skill you picked on purpose.

## The skills

The skills fall into seven groups. Most names include the group, such as `dh-legal-gdpr-audit`. Writing and learning skills skip it, because the name says enough, such as `dh-unslop`.

| Group | Name pattern | Skills | What they cover |
| --- | --- | --- | --- |
| Engineering | `dh-engineering-*` | 7 | Designing, debugging, securing, and reviewing code |
| Planning | `dh-planning-*` | 3 | Working out what to build before you build it |
| Writing | `dh-*` | 4 | Clear docs and plain writing |
| Learning | `dh-*` | 1 | Learning something new |
| Research | `dh-research-*` | 1 | What people are saying online right now |
| Marketing | `dh-marketing-*` | 21 | Growth, SEO, sign-ups, pricing, and email |
| Legal | `dh-legal-*` | 24 | Policies, contracts, GDPR, the EU AI Act, and security certificates for a SaaS product |

In the tables below, "Runs" shows how a skill starts. "Automatic" means on its own. "Manual" means only when you call it.

### Engineering

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-engineering-blast-radius` | Manual | Finds what a change could break outside the diff, and runs real code to prove it's safe. |
| `dh-engineering-code-security-review` | Manual | Checks Python, JavaScript/TypeScript, or Go code against security best practices. |
| `dh-engineering-codebase-design` | Automatic | Gives shared words for designing modules, interfaces, and seams. |
| `dh-engineering-diagnosing-bugs` | Automatic | Walks through a step-by-step hunt for hard bugs and slowdowns. |
| `dh-engineering-domain-modeling` | Automatic | Builds a project's shared vocabulary, its `GLOSSARY.md`, and its decision records (ADRs). |
| `dh-engineering-improve-codebase-architecture` | Manual | Finds places to simplify the code, shows them in a web page, then questions you about the one you pick. |
| `dh-engineering-retro` | Manual | Looks back on a coding session: what worked and what didn't. |

### Planning

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-planning-brainstorming` | Manual | Asks what you want and why, then writes a design you approve before anything gets built. |
| `dh-planning-grilling` | Automatic | Tests a plan or idea with tough questions, one round at a time. |
| `dh-planning-sharpen` | Manual | Sharpens a task before you start: the expert approach, the real goal, and the right level of detail. |

### Writing

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-bro` | Manual | Says the last message again in plain words. |
| `dh-drunk-grandma` | Automatic | Rewrites text so a tipsy grandma with no technical background gets it on the first read. |
| `dh-technical-writing` | Automatic | Applies a writing standard to docs, READMEs, pull request descriptions, and commit messages. |
| `dh-unslop` | Automatic | Removes the habits that make text sound machine-written. |

### Learning

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-teach` | Manual | Teaches you a new skill or idea, step by step, in a workspace. |

### Research

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-research-last30days` | Manual | Finds what people said about a topic in the last 30 days, on Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, and the web. Needs Python 3.12 or newer. |

### Marketing

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-marketing-ads` | Automatic | Plans and checks paid ads on Google, Meta, LinkedIn, X, and other platforms. |
| `dh-marketing-ai-seo` | Automatic | Helps AI search tools and chatbots find and quote your content. |
| `dh-marketing-analytics` | Automatic | Sets up and checks tracking, such as GA4, events, and UTM tags. |
| `dh-marketing-app-store-listing` | Automatic | Checks and improves an App Store or Google Play page. |
| `dh-marketing-churn-prevention` | Automatic | Keeps customers from leaving: cancel flows, save offers, and failed-payment recovery. |
| `dh-marketing-content-strategy` | Automatic | Plans what content to create and which topics to cover. |
| `dh-marketing-cro` | Automatic | Gets more visitors on marketing pages and forms to sign up or buy. |
| `dh-marketing-customer-research` | Automatic | Runs and sums up customer research, such as interviews and reviews. |
| `dh-marketing-directory-submissions` | Automatic | Lists a product in startup, SaaS, AI, and review directories. |
| `dh-marketing-emails` | Automatic | Writes and improves automated email sequences. |
| `dh-marketing-image` | Automatic | Makes and edits marketing images, such as blog headers and social posts. |
| `dh-marketing-launch` | Automatic | Plans product launches, feature announcements, and Product Hunt launches. |
| `dh-marketing-onboarding` | Automatic | Helps new users get value from the product soon after signing up. |
| `dh-marketing-paywalls` | Automatic | Designs upgrade screens and paid-feature prompts inside the app. |
| `dh-marketing-popups` | Automatic | Designs popups, slide-ins, and banners that people act on. |
| `dh-marketing-pricing` | Automatic | Decides prices, plans, and what each plan includes. |
| `dh-marketing-programmatic-seo` | Automatic | Builds many search-friendly pages from one template and a data set. |
| `dh-marketing-seo-audit` | Automatic | Finds what stops a site from ranking in search. |
| `dh-marketing-signup` | Automatic | Makes sign-up, registration, and trial start smoother. |
| `dh-marketing-site-architecture` | Automatic | Plans a site's pages, menus, web addresses, and internal links. |
| `dh-marketing-social` | Automatic | Creates and schedules social posts, and tracks what people say. |

### Legal

Every legal skill is manual, so call the one you need. Most come from [lawve-ai/awesome-legal-skills](https://github.com/lawve-ai/awesome-legal-skills). Each keeps its author's license in its folder. I wrote the Danish and Slovak skills for this repo.

These skills help you prepare documents and spot problems. They don't replace a lawyer.

| Skill | Use it when |
| --- | --- |
| **Policies you publish** | |
| `dh-legal-policy-privacy` | You need a privacy policy for your website or app. It works out which laws apply from where your users live. Start here. |
| `dh-legal-policy-gdpr-notice` | You need an EU GDPR privacy notice as a Word file, for example for job applicants. |
| `dh-legal-policy-cookies` | You need a cookie policy for EU visitors. |
| `dh-legal-policy-terms-check` | You want your own terms or privacy policy checked for unfair clauses before you publish. |
| **Contracts** | |
| `dh-legal-contract-saas-agreement` | You're writing the customer agreement you send out, starting from the YC SaaS template. |
| `dh-legal-contract-dpa` | You're writing or reviewing a data processing agreement (DPA), from either side. |
| `dh-legal-contract-first-pass` | You got a contract and want a quick risk check in plain words. |
| `dh-legal-contract-tech-review` | You need a detailed review of a service agreement, SLA, software licence, or API terms. |
| `dh-legal-contract-nda-triage` | You got an NDA and want it rated green, yellow, or red. |
| `dh-legal-contract-polish-law` | The contract is under Polish law. It answers in English and writes the contract text in Polish. |
| `dh-legal-contract-danish-law` | The contract is under Danish law. I wrote it from the official laws. No Danish lawyer has checked it. |
| `dh-legal-contract-slovak-law` | The contract is under Slovak law. I wrote it from the official laws. No Slovak lawyer has checked it. |
| **GDPR** | |
| `dh-legal-gdpr-audit` | You want your code and systems checked for GDPR problems, or you have a GDPR question. |
| `dh-legal-gdpr-dpia` | You're starting risky use of personal data, including AI, and need an impact assessment (DPIA). |
| `dh-legal-gdpr-transfer-assessment` | You send personal data outside the EU, for example to a US AI provider. |
| `dh-legal-gdpr-breach-response` | You had a data breach, and you have 72 hours to report it. |
| **AI features** | |
| `dh-legal-ai-act-triage` | You want to know whether the EU AI Act applies to you, and how. Start here. |
| `dh-legal-ai-act-role` | You need to know if you count as an AI "provider" or "deployer", for example when you build on someone else's AI model. |
| `dh-legal-ai-act-transparency` | You need to know what you must tell users about your AI (Art. 50). |
| `dh-legal-ai-governance-review` | You're reviewing an AI feature, or an AI supplier. |
| **Security and suppliers** | |
| `dh-legal-security-soc2` | A customer asks for SOC 2. |
| `dh-legal-security-iso27001` | A customer asks for ISO 27001. |
| `dh-legal-security-eu-cra` | You need to check whether the EU Cyber Resilience Act covers your product. |
| `dh-legal-vendor-due-diligence` | You're vetting your own suppliers. |

## Add a skill

1. Make a folder in `skills/` named `dh-` plus the group plus the skill, such as `skills/dh-engineering-my-skill/`. For a writing or learning skill, skip the group.
2. Add a `SKILL.md` file. Its header block holds the same name and a description of when to use it:

   ```md
   ---
   name: dh-engineering-my-skill
   description: Explain when the agent should use this skill.
   ---

   Write the steps the agent should follow here.
   ```

3. Keep the skill's scripts and extra files inside its folder.
4. Write instructions that work in both agents. To use another skill, write "load the `dh-other-skill` skill". Don't name one agent's tools, and don't write `/name` or `$name` inside a skill.
5. Decide whether it runs on its own or only when called, and set it in both files. See [Set automatic or manual](#set-automatic-or-manual).
6. Add it to the tables in [The skills](#the-skills).
7. Commit it, then run the installer wherever you use the collection. It pulls the change and links the new skill.

## Set automatic or manual

A skill runs on its own by default. To make it manual-only, change two files:
- For Claude Code, add `disable-model-invocation: true` to the header block of `SKILL.md`.
- For Codex, add `policy.allow_implicit_invocation: false` to the skill's `agents/openai.yaml`.

Set both or neither. If you set only one, the skill behaves differently in each agent.

Make a skill manual if it takes over the session or costs time or money. Do the same if it should only run when you choose. Keep it automatic if `AGENTS.md` or another skill needs to load it, because an agent can't load a manual skill.

## Edit the shared instructions

My shared instructions live in `AGENTS.md`. Claude Code reads the same file through `CLAUDE.md`.

Keep `AGENTS.md` short. Put only rules that must apply to every reply there. Put longer guidance in a skill, and add a line to `AGENTS.md` saying when to load it.

After editing, commit, then run the installer wherever you use the collection. It pulls the change, and on Windows without Developer Mode it also refreshes its copy of `AGENTS.md`.

## References

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [pstack source](https://github.com/cursor/plugins/tree/main/pstack)
- [Matt Pocock's engineering skills](https://github.com/mattpocock/skills/tree/main/skills/engineering)
