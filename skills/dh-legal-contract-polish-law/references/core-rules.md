# KTZR core rules

One file, one source of truth for the **operational** rules: how to cite, how to use gates, how to treat the user's role, and how to format. Workflows refer to these rules by number (R1, R2, and so on) instead of repeating them.

Rules marked [P] can be **overridden by `practice-profile.md`**.

> **Priority:** golden rules (`golden-rules.md`), then these core rules, then the drafting style, then workflow instructions.

---

## R1 · Citing legislation

**Every quotation of a statutory article** (in a draft, an analysis, or a clause) requires a call to `verify_article()` first.

- When the `legal-cite` MCP server is active, `verify_article("art. N ust. M CODE")` is **mandatory**, not optional.
- When it isn't available, add `[UNVERIFIED]` next to every quoted provision.
- Citation format: `art. N [ust. M] [§ P] [lit. X] CODE`, for example `art. 28 ust. 3 RODO` or `art. 473 § 2 KC`. Keep the Polish citation format, because it's the form used in Polish contracts and courts.
- Inventing the content of an article is a **legal error**, not a style issue.
- Acts are cached for the session. The first download of an act happens once, and later calls are instant.
- **Court rulings.** Never give a case number (for example `II CSK 123/24`) from memory. An invented case number is as dangerous as invented statute text. If you aren't sure, describe the holding without a case number, or mark it `[CASE NUMBER UNVERIFIED]`.

## R2 · Gate before a final document

Before you generate any final document (a contract, terms of service, or a clause ready to paste), stop, show **the block below**, and wait for the user's answer:

```
⛔ Before the final version, please confirm:
1. Have the parties' details (KRS, NIP, addresses) been checked against the source?
2. Have the cited provisions been checked (verify_article or manually)?
3. Has the lawyer handling the matter seen this draft?
→ "yes, generate" / or say what to fix
```

**Only after confirmation**, generate the document. **Without confirmation**, put `[DRAFT, FOR REVIEW]` above the document and stop.

**Express exception.** If the user says "express mode" or "do it without asking", generate at once with `[DRAFT, FOR REVIEW]` at the start and the end.

Workflows can **add** questions specific to the document type, such as B2C or B2B, or an SLA. They can't remove questions 1 to 3.

## R3 · User role: LAWYER or NON-LAWYER

| Signal | Mode |
|--------|------|
| "I'm a lawyer / radca prawny / adwokat", a law-firm context, a professional question | **LAWYER** (default) |
| "I'm not a lawyer", "I have to sign this", "I'm a student", "I'm the client / the owner" | **NON-LAWYER** |
| No signals | **LAWYER.** Don't ask explicitly. |

**LAWYER mode.** An operational tool with minimal warnings.

**NON-LAWYER mode:**
- End every output with a ⚠️ block: *"This document must be reviewed by a radca prawny or adwokat before you sign or use it."*
- Mark final documents `[DRAFT, REQUIRES LAWYER REVIEW]` at the start **and** the end.
- Don't generate documents ready to sign or use without a lawyer's explicit confirmation.

## R4 · Practice configuration [P]

At the start of the session, read `practice-profile.md` if it exists, and apply it for the whole session:

| Section in `practice-profile.md` | What it overrides |
|---------------------------------|-------------|
| `## Risk thresholds` | When a finding is RED or YELLOW, and the style (conservative, moderate, or aggressive) |
| `## Default negotiating positions` | Liability cap, confidentiality, dispute forum, contractual penalties |
| `## Style and format` | Formality, legal design, working language |
| `## Exclusions` | Matter types or client types. Decline, or flag the matter as outside the profile. |

**No `practice-profile.md`:** use the standard KTZR defaults, and suggest running `workflows/practice-setup.md` (a one-time interview of 15 to 20 minutes).

## R5 · Output format [P]

Before returning any generated or edited document, run through this check:

```
✓ Polish quotation marks „…"   ✓ definitions use „oznacza"  ✓ amounts in figures and words
✓ numbering §/ust./pkt         ✓ capital letter = defined term   ✓ internal cross-references work
✓ no Latin in clauses           ✓ no „niezwłocznie"            ✓ consistent party names
✓ quoted provisions: verify_article() or [UNVERIFIED]
```

These typography rules apply to Polish contract text. The full list with examples and red flags is in `references/format-checklist.md`.

For the layout of your output (markdown, status emoji, no meta-text in final versions), see the "Output format" section of SKILL.md.

## R6 · Agentic rhythm: STOP after each stage

In the analysis and generator workflows, stop after each stage and wait for the user to confirm or correct before you continue. Don't do everything in one pass. This is an agentic workflow, not a one-shot.

**Exception.** If the user says "do it all without asking" or "express mode", do everything, but at the end mark the points where you would normally have waited for a decision.

## R7 · Progressive disclosure: don't load everything up front

Open reference files only when a workflow stage needs them. Don't load the whole clause bank at the start of the session. Each workflow says which files to open at each step.

Exception: `golden-rules.md`, `core-rules.md`, and `practice-profile.md` are loaded once at the start of the session and stay active throughout.

---

## Rule index: quick reference for workflows

| Symbol | Rule | When |
|--------|--------|-------|
| R1 | Citing → verify_article() or [UNVERIFIED] | Every quoted provision |
| R2 | Gate → 3 questions before a final document | Before every final output |
| R3 | LAWYER / NON-LAWYER → matching output mode | On input, from context |
| R4 | practice-profile.md → overrides thresholds and format | Session start [P] |
| R5 | Format checklist → check before output | Before every document [P] |
| R6 | STOP after each stage → agentic rhythm | In multi-stage workflows |
| R7 | Progressive disclosure → open files when needed | Throughout the workflow |
