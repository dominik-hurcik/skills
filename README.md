# Agent instructions and skills

Collection of my handpicked skills from all around the internet for Codex and Claude Code. Edit each skill once. Both agents read the same files.

## Skills

This collection has 61 skills in seven categories. Each skill name starts with its category. Automatic skills can run when the task matches their description. Manual skills run only when you call them by name. See [Choose when a skill runs](#choose-when-a-skill-runs).

| Category | Skills | What they cover |
| --- | --- | --- |
| `engineering-` | 7 | Designing, debugging, securing, and reviewing code |
| `planning-` | 3 | Working out what to build before building it |
| `writing-` | 4 | Docs standards and plain, human prose |
| `learning-` | 1 | Learning a new concept |
| `research-` | 1 | Researching recent public discussion |
| `marketing-` | 21 | Growth, SEO, conversion, pricing, and lifecycle marketing |
| `legal-` | 24 | Policies, contracts, GDPR, the EU AI Act, and security certifications for a SaaS product |

### Engineering

| Skill | Runs | What it does |
| --- | --- | --- |
| `engineering-code-security-review` | Manual | Reviews Python, JavaScript/TypeScript, or Go code against security best practices. |
| `engineering-blast-radius` | Manual | Finds what a change could break outside the diff, and proves the change is safe by running real code. |
| `engineering-codebase-design` | Automatic | Gives a shared vocabulary for designing deep modules, interfaces, and seams. |
| `engineering-diagnosing-bugs` | Automatic | Runs a diagnosis loop for hard bugs and performance regressions. |
| `engineering-domain-modeling` | Automatic | Builds a project's domain model, its `GLOSSARY.md`, and its ADRs. |
| `engineering-improve-codebase-architecture` | Manual | Scans a codebase for deepening opportunities, reports them as an HTML page, then grills through the one you pick. |
| `engineering-retro` | Manual | Runs a retrospective on a coding session. |

### Planning

| Skill | Runs | What it does |
| --- | --- | --- |
| `planning-brainstorming` | Manual | Asks what you want and why before you build something, then writes a design you approve before anything gets built. |
| `planning-grilling` | Automatic | Stress-tests a plan, decision, or idea one round of questions at a time. |
| `planning-sharpen` | Manual | Sharpens a task before starting: the expert approach, the real goal, and the right level of detail. |

### Writing

| Skill | Runs | What it does |
| --- | --- | --- |
| `writing-bro` | Manual | Restates the last message in plain language, with no jargon. |
| `writing-drunk-grandma` | Manual | Rewrites text so a tipsy grandma with no technical background understands it on the first read. |
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

### Legal

All legal skills are manual-only, so call the one you need by name. Most come from [lawve-ai/awesome-legal-skills](https://github.com/lawve-ai/awesome-legal-skills), and each keeps its author's license in its folder. The Danish and Slovak skills were written for this repo. They help you prepare documents and spot issues. They don't replace a lawyer.

| Skill | Use it when |
| --- | --- |
| **Policies you publish** | |
| `legal-policy-privacy` | You need a privacy policy for your website or app. It works out which laws apply from where your users are. Start here. |
| `legal-policy-gdpr-notice` | You need an EU GDPR privacy notice as a Word file, for example for job applicants or one EU country. |
| `legal-policy-cookies` | You need a GDPR and ePrivacy cookie policy. |
| `legal-policy-terms-check` | You want your own terms or privacy policy checked for unfair clauses before you publish them. |
| **Contracts** | |
| `legal-contract-saas-agreement` | You're drafting the customer agreement you send out, starting from the YC SaaS template. |
| `legal-contract-dpa` | You're drafting or reviewing an Art. 28 GDPR data processing agreement, from either side. |
| `legal-contract-first-pass` | You received any contract and want a quick, plain-language risk check. |
| `legal-contract-tech-review` | You need a detailed review of an MSA, SLA, EULA, or API terms. |
| `legal-contract-nda-triage` | You received an NDA and want it rated green, yellow, or red. |
| `legal-contract-polish-law` | The contract is under Polish law. Written in Polish. |
| `legal-contract-danish-law` | The contract is under Danish law. Written for this repo from the official statutes, not reviewed by a Danish lawyer. |
| `legal-contract-slovak-law` | The contract is under Slovak law. Written for this repo from the official statutes, not reviewed by a Slovak lawyer. |
| **GDPR** | |
| `legal-gdpr-audit` | You want your code and systems audited for GDPR issues, or have a general GDPR question. |
| `legal-gdpr-dpia` | You're starting high-risk processing, including AI, and need a data protection impact assessment. |
| `legal-gdpr-transfer-assessment` | You send personal data outside the EU, for example to a US LLM provider. |
| `legal-gdpr-breach-response` | You have a data breach and the 72-hour notification clock is running. |
| **AI features** | |
| `legal-ai-act-triage` | You want to know whether and how the EU AI Act applies to you. Start here. |
| `legal-ai-act-role` | You need to know whether you're an AI Act provider or deployer, for example when you wrap a third-party LLM. |
| `legal-ai-act-transparency` | You need to know what you must disclose about AI under Art. 50. |
| `legal-ai-governance-review` | You're reviewing an AI feature or a third-party AI vendor. |
| **Security and vendors** | |
| `legal-security-soc2` | A customer asks for SOC 2. |
| `legal-security-iso27001` | A customer asks for ISO 27001. |
| `legal-security-eu-cra` | You need to check whether the EU Cyber Resilience Act covers your product. |
| `legal-vendor-due-diligence` | You're vetting your own suppliers or technology vendors. |

## Install

You need Git and Python 3.9 or newer. The installer works on macOS, Linux, and Windows. On macOS and Linux, run it with `python3`. On Windows, use `py` or `python`.

There are two modes:

| Mode | Where the skills go | Use it when |
| --- | --- | --- |
| User mode (recommended) | Your home folder, for every project on this machine | You want the skills everywhere and update them with one `git pull`. |
| Project mode | One project | You want the skills checked in with a project, or only in that project. |

### User mode

Clone the collection once, anywhere in your home folder, and run the installer with `--user`:

```sh
git clone https://github.com/dominik-hurcik/skills.git ~/agent-skills
python3 ~/agent-skills/install.py --user
```

On Windows:

```powershell
git clone https://github.com/dominik-hurcik/skills.git $HOME\agent-skills
py $HOME\agent-skills\install.py --user
```

The installer adds:

| Path | What it loads |
| --- | --- |
| `~/.agents/skills/<name>` | Skills for Codex |
| `~/.claude/skills/<name>` | The same skills for Claude Code |
| `~/.codex/AGENTS.md` | Shared instructions for Codex. If you set `CODEX_HOME`, it goes there. |
| `~/.claude/CLAUDE.md` | A one-line file that imports the shared instructions for Claude Code |

### Project mode

Open a terminal in your project's root folder and run:

```sh
git clone https://github.com/dominik-hurcik/skills.git .agent-instructions
python3 .agent-instructions/install.py
```

The installer adds the same four items inside the project: `.agents/skills/<name>`, `.claude/skills/<name>`, `AGENTS.md`, and `CLAUDE.md`. Keep `.agent-instructions` inside the project, because the links point into it.

For a personal install, add `.agent-instructions/` to the project's `.gitignore` so Git skips the nested clone. Each new checkout needs its own installation.

### Keep your own instructions

If you already have an `AGENTS.md` or `CLAUDE.md` where the installer would put one, it stops before changing anything. To keep yours and install only the skills, add `--skills-only`. Use it each time you rerun the installer for that location.

The installer also stops if a skill folder with the same name already exists and isn't one of its links.

### Update

Pull the collection, then rerun the installer with the same options:

```sh
git -C ~/agent-skills pull --ff-only
python3 ~/agent-skills/install.py --user
```

For project mode, run `git -C .agent-instructions pull --ff-only` and `python3 .agent-instructions/install.py` from the project root.

Changes to existing skills take effect right after the pull, because the skill folders are links. Rerun the installer when skills are added or removed. It links new skills and removes links to deleted ones. Start a new agent session afterwards.

### How the installer links files

- **Skill folders.** Symlinks on macOS and Linux. Directory junctions on Windows, which need no admin rights or Developer Mode.
- **`CLAUDE.md`.** A small file with an `@` import of `AGENTS.md`, so Claude Code always reads the current shared instructions.
- **`AGENTS.md`.** A symlink on macOS and Linux. Windows allows file symlinks only with Developer Mode turned on. Without it, the installer writes a copy and refreshes it each time you rerun the installer.

The installer marks the files it writes with a comment on the first line. On a rerun it updates only its own files and links, never yours.

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
7. Pull the update wherever you installed the collection and rerun the installer. See [Update](#update).

## Choose when a skill runs

Agents can select a skill when its description matches the task. You can also request a skill by name.

Claude Code uses `disable-model-invocation: true` in `SKILL.md` to make a skill manual-only. Codex uses `policy.allow_implicit_invocation: false` in that skill's `agents/openai.yaml` for the same purpose. Configure both if you want the same behavior in both agents.

A skill without either setting can run automatically in both agents. When you add or change a skill, check both files. A setting in only one file makes the skill manual-only in one agent and automatic in the other.

A skill that other skills load must allow automatic selection. A manual-only skill can't be loaded by the agent, only by you.

For behavior you want on every response, add a rule to `AGENTS.md` and allow the agent to invoke the required skill. Skill matching alone does not guarantee that behavior.

## Edit shared instructions

Edit `AGENTS.md`. Claude Code imports the same file through `CLAUDE.md`.

Commit the change, then pull it wherever you installed the collection. On Windows without Developer Mode, also rerun the installer to refresh the copied `AGENTS.md`.

## References

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [pstack source](https://github.com/cursor/plugins/tree/main/pstack)
- [Matt Pocock's engineering skills](https://github.com/mattpocock/skills/tree/main/skills/engineering)
