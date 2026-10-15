---
name: retro
description: "Conduct a retrospective on a coding session."
disable-model-invocation: true
---

The user has asked for a retrospective. Suggest changes to the coding agent's environment that would make future runs faster and less error-prone. Don't critique the code the session produced.

## Steps

1. Read the session. If the user names one, find its log on this machine. Otherwise use the current session.

2. Map the environment before suggesting anything. Record which of these exist, because later steps depend on them:
   - Steering files: `AGENTS.md`, `CLAUDE.md`, and the user's global versions.
   - A review stage: a reviewer agent, a review skill or command, a PR review bot, or a review guide such as `CODING_STANDARDS.md` or `REVIEW.md`.
   - Guardrails: lint, typecheck, and test scripts in `package.json` or the build tool, pre-commit hooks, and CI workflows.
   - Docs folders and installed skills.

3. Look for candidates in the categories below. Every candidate needs evidence from the session, such as a quoted tool call, error, or retry loop. Drop any candidate you can't tie to something that happened, unless it's a repo with no guardrail at all.

4. Present the candidates ordered by severity. For each one, give:
   - the category
   - what happened, with the evidence
   - the concrete change: which file, which command, which rule
   - a rough cost to implement

## Categories

**Navigation.** Did the agent take a long time to find the right file or fact? Are there hidden dependencies between files? Propose a navigation pointer, meaning a one-line reference from a file the agent already reads to the file it needed.

**Automated checks.** Did the agent make a mistake a lint rule, type check, test, or file-layout check would have caught? Read the repo's existing check commands and CI first. If a check exists but isn't wired up or is silently broken, report that instead of proposing a new one. A repo with no pre-commit hook and no CI job running its checks is a finding by itself.

**Rules.** Did the agent break a convention? Classify the violation first.

- Mechanical violations get a deterministic check. Examples are a banned API, a fixed syntax pattern, an import shape, or a file-location rule. Add a custom lint rule, a pre-commit hook, or a CI job, whichever is cheapest given the repo's language and existing guardrails. Prefer this over writing a rule in prose.
- Judgement calls get a written rule. Examples are cross-file consistency and matching the surrounding style. Put the rule where the review stage reads it. If the repo has no review stage, put it in a doc and add a one-line pointer from `AGENTS.md`. Only propose a new review guide or reviewer agent if the session shows several judgement-call misses.

**Steering file size.** Is `AGENTS.md` or `CLAUDE.md` large, in the repo or the global scope? Propose moving each instruction to a check, a review guide, or a doc behind a pointer.

**No-ops.** Find steering instructions that don't change the agent's behavior. Examples are restatements of default behavior, rules for situations the repo never hits, and instructions the session ignored without consequence. Propose deleting them.

**Tool economy.** Find expensive tool calls, such as full-file reads where a search would do, repeated identical commands, or custom CLIs and MCP servers that return large outputs. Propose a cheaper command, a flag, or a wrapper script.

**Information access.** Was a key fact unavailable to the agent? Examples are dev server output, runtime errors, and state in a third-party service. Propose teeing logs to a file, adding a read-only CLI or MCP server, or documenting where the information lives.

## Reference

### Where instructions belong

Agents load steering files into every session, so each line there costs context in every run. Choose the cheapest place that still gets the instruction read at the right time.

1. **An automated check.** It costs no context and the agent can't ignore it. Use it for anything mechanical.
2. **The review stage, if one exists.** The reviewer receives a diff, so it does no exploration and has the most spare context. Coding standards belong here, not in the implementer's steering file.
3. **A doc or skill reached through a pointer.** The agent reads it only when relevant. A skill's description loads into context, so a skill also works as a discoverable doc.
4. **`AGENTS.md` or `CLAUDE.md`.** Keep these for navigation pointers and the few rules that must apply to every task.

Look for existing docs and review guides before proposing new files.
