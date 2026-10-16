# Agent instructions and skills

My collection of skills for Codex and Claude Code, picked from around the internet and adapted to work in both agents. You edit each skill once, and both agents read the same files.

Every skill name starts with `dh-`, so you can tell my skills apart from built-in skills and plugins. Engineering, planning, research, marketing, and legal skills also carry their category in the name, such as `dh-legal-gdpr-audit`. Writing and learning skills don't, because the name says enough on its own, such as `dh-unslop`.

## Skills

The collection has 61 skills in seven categories.

| Category | Name pattern | Skills | What they cover |
| --- | --- | --- | --- |
| Engineering | `dh-engineering-*` | 7 | Designing, debugging, securing, and reviewing code |
| Planning | `dh-planning-*` | 3 | Working out what to build before you build it |
| Writing | `dh-*` | 4 | Docs standards and plain prose |
| Learning | `dh-*` | 1 | Learning a new concept |
| Research | `dh-research-*` | 1 | Researching recent public discussion |
| Marketing | `dh-marketing-*` | 21 | Growth, SEO, conversion, pricing, and lifecycle marketing |
| Legal | `dh-legal-*` | 24 | Policies, contracts, GDPR, the EU AI Act, and security certifications for a SaaS product |

The "Runs" column says whether the agent picks the skill on its own (automatic) or only when you call it (manual). [When skills run](#when-skills-run) explains both.

### Engineering

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-engineering-blast-radius` | Manual | Finds what a change could break outside the diff, and proves the change is safe by running real code. |
| `dh-engineering-code-security-review` | Manual | Reviews Python, JavaScript/TypeScript, or Go code against security best practices. |
| `dh-engineering-codebase-design` | Automatic | Gives a shared vocabulary for designing deep modules, interfaces, and seams. |
| `dh-engineering-diagnosing-bugs` | Automatic | Runs a diagnosis loop for hard bugs and performance regressions. |
| `dh-engineering-domain-modeling` | Automatic | Builds a project's domain model, its `GLOSSARY.md`, and its ADRs. |
| `dh-engineering-improve-codebase-architecture` | Manual | Scans a codebase for deepening opportunities, reports them as an HTML page, then grills you on the one you pick. |
| `dh-engineering-retro` | Manual | Runs a retrospective on a coding session. |

### Planning

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-planning-brainstorming` | Manual | Asks what you want and why, then writes a design you approve before anything gets built. |
| `dh-planning-grilling` | Automatic | Stress-tests a plan, decision, or idea one round of questions at a time. |
| `dh-planning-sharpen` | Manual | Sharpens a task before you start: the expert approach, the real goal, and the right level of detail. |

### Writing

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-bro` | Manual | Restates the last message in plain language, with no jargon. |
| `dh-drunk-grandma` | Automatic | Rewrites text so a tipsy grandma with no technical background understands it on the first read. |
| `dh-technical-writing` | Automatic | Applies a technical-writing standard to docs, RFCs, READMEs, PR descriptions, and commit messages. |
| `dh-unslop` | Automatic | Cuts AI tells from any writing. |

### Learning

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-teach` | Manual | Teaches you a new skill or concept in a guided workspace. |

### Research

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-research-last30days` | Manual | Researches what people said about a topic in the last 30 days on Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, and the web. Needs Python 3.12 or newer. |

### Marketing

| Skill | Runs | What it does |
| --- | --- | --- |
| `dh-marketing-ads` | Automatic | Plans and audits paid campaigns on Google, Meta, LinkedIn, X, and other ad platforms. |
| `dh-marketing-ai-seo` | Automatic | Optimizes content so AI search engines and LLMs cite it. |
| `dh-marketing-analytics` | Automatic | Sets up and audits analytics tracking, such as GA4, events, and UTMs. |
| `dh-marketing-app-store-listing` | Automatic | Audits and improves an App Store or Google Play listing. |
| `dh-marketing-churn-prevention` | Automatic | Builds cancel flows, save offers, and failed-payment recovery. |
| `dh-marketing-content-strategy` | Automatic | Plans what content to create and which topics to cover. |
| `dh-marketing-cro` | Automatic | Improves conversion on marketing pages and forms. |
| `dh-marketing-customer-research` | Automatic | Runs and analyses customer research, such as interviews, reviews, and ICP work. |
| `dh-marketing-directory-submissions` | Automatic | Submits a product to startup, SaaS, AI, and review directories. |
| `dh-marketing-emails` | Automatic | Writes and improves email sequences and lifecycle flows. |
| `dh-marketing-image` | Automatic | Creates and edits marketing images, such as blog heroes, social graphics, and mockups. |
| `dh-marketing-launch` | Automatic | Plans product launches, feature announcements, and Product Hunt launches. |
| `dh-marketing-onboarding` | Automatic | Improves post-signup onboarding and activation. |
| `dh-marketing-paywalls` | Automatic | Designs in-app paywalls, upgrade screens, and feature gates. |
| `dh-marketing-popups` | Automatic | Designs popups, modals, slide-ins, and banners that convert. |
| `dh-marketing-pricing` | Automatic | Decides pricing, packaging, and monetization. |
| `dh-marketing-programmatic-seo` | Automatic | Builds SEO pages at scale from templates and data. |
| `dh-marketing-seo-audit` | Automatic | Audits a site for technical and on-page SEO issues. |
| `dh-marketing-signup` | Automatic | Improves signup, registration, and trial activation flows. |
| `dh-marketing-site-architecture` | Automatic | Plans page hierarchy, navigation, URL structure, and internal links. |
| `dh-marketing-social` | Automatic | Creates and schedules social posts, and runs social listening. |

### Legal

Every legal skill is manual, so call the one you need by name. Most come from [lawve-ai/awesome-legal-skills](https://github.com/lawve-ai/awesome-legal-skills), and each keeps its author's license in its folder. I wrote the Danish and Slovak skills for this repo. The legal skills help you prepare documents and spot issues. They don't replace a lawyer.

| Skill | Use it when |
| --- | --- |
| **Policies you publish** | |
| `dh-legal-policy-privacy` | You need a privacy policy for your website or app. It works out which laws apply from where your users are. Start here. |
| `dh-legal-policy-gdpr-notice` | You need an EU GDPR privacy notice as a Word file, for example for job applicants or one EU country. |
| `dh-legal-policy-cookies` | You need a GDPR and ePrivacy cookie policy. |
| `dh-legal-policy-terms-check` | You want your own terms or privacy policy checked for unfair clauses before you publish them. |
| **Contracts** | |
| `dh-legal-contract-saas-agreement` | You're drafting the customer agreement you send out, starting from the YC SaaS template. |
| `dh-legal-contract-dpa` | You're drafting or reviewing an Art. 28 GDPR data processing agreement, from either side. |
| `dh-legal-contract-first-pass` | You received a contract and want a quick, plain-language risk check. |
| `dh-legal-contract-tech-review` | You need a detailed review of an MSA, SLA, EULA, or API terms. |
| `dh-legal-contract-nda-triage` | You received an NDA and want it rated green, yellow, or red. |
| `dh-legal-contract-polish-law` | The contract is under Polish law. It answers in English and drafts clause text in Polish. |
| `dh-legal-contract-danish-law` | The contract is under Danish law. I wrote it from the official statutes. No Danish lawyer has reviewed it. |
| `dh-legal-contract-slovak-law` | The contract is under Slovak law. I wrote it from the official statutes. No Slovak lawyer has reviewed it. |
| **GDPR** | |
| `dh-legal-gdpr-audit` | You want your code and systems audited for GDPR issues, or you have a general GDPR question. |
| `dh-legal-gdpr-dpia` | You're starting high-risk processing, including AI, and need a data protection impact assessment. |
| `dh-legal-gdpr-transfer-assessment` | You send personal data outside the EU, for example to a US LLM provider. |
| `dh-legal-gdpr-breach-response` | You have a data breach and the 72-hour notification clock is running. |
| **AI features** | |
| `dh-legal-ai-act-triage` | You want to know whether and how the EU AI Act applies to you. Start here. |
| `dh-legal-ai-act-role` | You need to know whether you're an AI Act provider or deployer, for example when you wrap a third-party LLM. |
| `dh-legal-ai-act-transparency` | You need to know what you must disclose about AI under Art. 50. |
| `dh-legal-ai-governance-review` | You're reviewing an AI feature or a third-party AI vendor. |
| **Security and vendors** | |
| `dh-legal-security-soc2` | A customer asks for SOC 2. |
| `dh-legal-security-iso27001` | A customer asks for ISO 27001. |
| `dh-legal-security-eu-cra` | You need to check whether the EU Cyber Resilience Act covers your product. |
| `dh-legal-vendor-due-diligence` | You're vetting your own suppliers or technology vendors. |

## When skills run

A skill runs in one of three ways.

### Automatic skills (28)

The agent reads every skill's `description` at the start of a session. When your request matches a description, the agent loads that skill on its own. For example, "our signup page converts badly" loads `dh-marketing-signup`, and "this test fails only in CI" loads `dh-engineering-diagnosing-bugs`.

Matching isn't guaranteed. The agent decides, and a vague request may load nothing. If you need a specific skill, call it by name.

These skills are automatic because their descriptions are narrow, they only advise or edit, and loading one by mistake costs little:
- all 21 marketing skills
- `dh-engineering-codebase-design`, `dh-engineering-diagnosing-bugs`, and `dh-engineering-domain-modeling`
- `dh-planning-grilling`
- `dh-technical-writing`, `dh-unslop`, and `dh-drunk-grandma`

### Skills that the shared instructions load

`AGENTS.md` tells the agent to load two skills at specific moments, on top of normal matching:
- `dh-unslop` before it writes prose longer than a short reply, such as docs, READMEs, commit messages, or PR descriptions
- `dh-drunk-grandma` when it explains a concept, a decision, or a trade-off to you

`AGENTS.md` also keeps five core writing rules inline, such as leading with the answer and using no em dashes. Those rules apply to every reply, even when the agent doesn't load a skill. A skill only takes effect once the agent loads it, so the core rules cover the gap.

### Manual skills (33)

A manual skill never loads on its own. You call it by name, as described in [Use a skill](#use-a-skill). Other skills and `AGENTS.md` can't load a manual skill either.

These skills are manual for one of these reasons:
- **They take over the session.** `dh-planning-brainstorming` blocks building until you approve a design. `dh-teach` sets up a learning workspace. `dh-engineering-improve-codebase-architecture` scans the whole codebase and writes an HTML report. `dh-engineering-retro` reviews the whole session.
- **You decide when they're worth it.** `dh-planning-sharpen` and `dh-bro` rework a task or a message you point them at. `dh-engineering-blast-radius` runs real code to prove a change is safe. `dh-engineering-code-security-review` is written to run only on an explicit request.
- **They cost time or money.** `dh-research-last30days` takes minutes, can spend credits on paid APIs if you've added keys, and asks for setup on its first run.
- **They're legal.** The 24 legal skills have broad descriptions that would compete with each other in every SaaS project, and legal output should come from a skill you chose on purpose.

## Install

You need Git and Python 3.9 or newer. The installer works on macOS, Linux, and Windows. On macOS and Linux, run it with `python3`. On Windows, use `py` or `python`.

The installer has two modes:

| Mode | Where the skills go | Use it when |
| --- | --- | --- |
| User mode (recommended) | Your home folder, for every project on this machine | You want the skills everywhere, and you want to update them with one `git pull`. |
| Project mode | One project | You want the skills in only one project, or checked in with it. |

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

The installer adds these paths:

| Path | What it loads |
| --- | --- |
| `~/.agents/skills/<name>` | Skills for Codex |
| `~/.claude/skills/<name>` | The same skills for Claude Code |
| `~/.codex/AGENTS.md` | Shared instructions for Codex. If you set `CODEX_HOME`, the file goes there instead. |
| `~/.claude/CLAUDE.md` | A one-line file that imports the shared instructions for Claude Code |

### Project mode

Open a terminal in your project's root folder and run:

```sh
git clone https://github.com/dominik-hurcik/skills.git .agent-instructions
python3 .agent-instructions/install.py
```

The installer adds the same four items inside the project: `.agents/skills/<name>`, `.claude/skills/<name>`, `AGENTS.md`, and `CLAUDE.md`. Keep `.agent-instructions` inside the project, because the links point into it.

For a personal install, add `.agent-instructions/` to the project's `.gitignore`, so Git skips the nested clone. Each new checkout needs its own installation.

### Keep your own instructions

If an `AGENTS.md` or `CLAUDE.md` already exists where the installer would put one, the installer stops before it changes anything. To keep your file and install only the skills, add `--skills-only`. Add it each time you rerun the installer for that location.

The installer also stops if a skill folder with the same name already exists and isn't one of its own links.

### Update

Pull the collection, then rerun the installer with the same options:

```sh
git -C ~/agent-skills pull --ff-only
python3 ~/agent-skills/install.py --user
```

For project mode, run `git -C .agent-instructions pull --ff-only` and then `python3 .agent-instructions/install.py` from the project root.

Changes to existing skills take effect right after the pull, because the skill folders are links. Rerun the installer when skills are added, removed, or renamed. It links new skills and removes links to deleted ones. Start a new agent session afterwards.

### How the installer links files

- **Skill folders.** Symlinks on macOS and Linux. On Windows, directory junctions, which need no admin rights or Developer Mode.
- **`CLAUDE.md`.** A small file that imports `AGENTS.md` with `@`, so Claude Code always reads the current shared instructions.
- **`AGENTS.md`.** A symlink on macOS and Linux. Windows allows file symlinks only with Developer Mode turned on. Without it, the installer writes a copy and refreshes it each time you rerun the installer.

The installer marks each file it writes with a comment on the first line. On a rerun, it updates only its own files and links, never yours.

## Use a skill

In Codex CLI or its IDE extension, mention the skill with `$`:

```text
$dh-bro Explain the last message again.
```

In Claude Code, start the message with the skill's slash command:

```text
/dh-bro Explain the last message again.
```

You can call automatic skills this way too, when you want to be sure the agent uses them.

## Add a skill

1. Create a folder under `skills/`. Name it `dh-` plus the category plus the skill name, such as `skills/dh-engineering-my-skill/`. For a writing or learning skill, use `dh-` plus the skill name only.
2. Add a `SKILL.md` file with the same name, a description, and instructions:

   ```md
   ---
   name: dh-engineering-my-skill
   description: Explain when the agent should use this skill.
   ---

   Write the steps the agent should follow here.
   ```

3. Keep any scripts, references, and assets inside the skill's folder.
4. Write instructions that work in both agents. To use another skill, write "load the `dh-other-skill` skill". Don't name agent-specific tools, such as Claude Code's Skill tool, and don't use `/name` or `$name` syntax inside a skill.
5. Decide whether the skill is automatic or manual, and set it in both files. See [Set automatic or manual](#set-automatic-or-manual).
6. Add the skill to the tables in [Skills](#skills).
7. Commit the skill, pull wherever you installed the collection, and rerun the installer. See [Update](#update).

## Set automatic or manual

A skill is automatic by default. To make it manual, set it in two places:
- For Claude Code, add `disable-model-invocation: true` to the frontmatter in `SKILL.md`.
- For Codex, add `policy.allow_implicit_invocation: false` to the skill's `agents/openai.yaml`.

Set both, or neither. A setting in only one file makes the skill manual in one agent and automatic in the other.

Make a skill manual when it takes over the session, costs time or money, or should only run when you choose it. Keep a skill automatic if `AGENTS.md` or another skill loads it, because the agent can't load a manual skill.

## Edit shared instructions

Edit `AGENTS.md`. Claude Code imports the same file through `CLAUDE.md`.

Keep only rules that must apply to every reply in `AGENTS.md`. Put longer guidance in a skill, and add a line to `AGENTS.md` that says when to load it.

Commit the change, then pull it wherever you installed the collection. On Windows without Developer Mode, also rerun the installer to refresh the copied `AGENTS.md`.

## References

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [pstack source](https://github.com/cursor/plugins/tree/main/pstack)
- [Matt Pocock's engineering skills](https://github.com/mattpocock/skills/tree/main/skills/engineering)
