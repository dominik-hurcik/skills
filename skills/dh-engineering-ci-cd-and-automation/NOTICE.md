# Notice

This skill is copied from **ci-cd-and-automation** in Addy Osmani's agent skills.

- **Source:** https://github.com/addyosmani/agent-skills/tree/main/skills/ci-cd-and-automation
- **Copyright:** (c) 2025 Addy Osmani
- **License:** MIT. The full text is in [LICENSE](LICENSE) in this folder.

## What changed

- Renamed the skill to `dh-engineering-ci-cd-and-automation` in `SKILL.md`.
- Pointed the debugging link at `dh-engineering-diagnosing-bugs`.
- Passed the Vercel token through an environment variable instead of a command-line flag, so it does not show in the process list.
- Replaced the Vercel rollback command with a placeholder that fails until you configure your platform's rollback. The original command was not checked against Vercel's CLI.
- Converted em dashes and en dashes to commas, periods, and colons.
