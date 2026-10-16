# Workflow: fix a clause

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

A workflow for editing **a specific passage of a contract**: when the user pastes a clause and asks for a fix, or pauses a wider analysis to fix one paragraph.

Use it when:
- The user pastes a passage and asks for a correction.
- The user writes "fix § X in this contract".
- During a full analysis or audit, the user stops the workflow to fix one place.

---

## Step 1: understand what you're fixing

**Open now:** `references/drafting-style.md`, always before editing a clause. The KTZR style rules apply to small fixes too.

Work out:
- **What exactly should change?** A whole paragraph, one section, one sentence?
- **Why?** To align the style, add a missing element, fix a legal error, match other clauses, or make it more precise.
- **In what context?** Does the passage stand alone, or does it refer to other parts of the contract?

If the user's instruction is unclear ("fix this"), **ask once**: "What exactly do you want to change? For example, add a cap on penalties, align it with § 4, or make the deadline precise?"

---

## Step 2: pick a clause from the bank, or rework the text

### Scenario A: add or replace with a clause from the bank

If the user wants to add a missing element (for example "add an anti-copyleft clause", "add a liability cap"):

1. Open `references/clause-bank/INDEX.md`.
2. Find the right category and open its file.
3. Pick the best clause for the context (usually from the KTZR contract closest to this type).
4. Fit it to the passage: party names, deadlines, cross-references.

### Scenario B: rework the existing passage

If the user wants to fix the existing text (for example "align it with the rest of the contract", "simplify the language"):

1. Read the passage and understand its legal purpose.
2. Check `references/golden-rules.md`: does the passage break any rule?
3. Apply the KTZR style rules.
4. Keep the legal meaning. You change the form, not the substance (unless the substance is wrong).

### Scenario C: full replacement

If the passage is beyond saving (for example a void clause trying to exclude intentional fault, art. 473 § 2 KC):

> _(R1): `verify_article()` before every cited article, or `[UNVERIFIED]` without the MCP server._

1. Explain briefly why the passage is a problem.
2. Propose a replacement clause from the bank.
3. Show "before and after".

---

## Step 3: output format

**Brief and action-oriented.** Don't write long explanations unless the user asks.

### Default variant (the fixed text is enough)

> ⛔ If the fixed passage is ready to paste into a contract for signing, first ask: "Has the lawyer handling the matter seen this change?" Without confirmation, add `[DRAFT, FOR REVIEW]` above the passage.

```
[the fixed passage, ready to paste into the document]
```

Then **one or two lines** explaining what you changed and why (if the change needs explaining).

### Extended variant (when the change is significant)

```
## CHANGE

**Before:**
[original passage]

**After:**
[fixed passage]

**What I changed:**
- [1 to 3 points, one sentence each]

**Clause from the bank:** `references/clause-bank/XX-yyy.md`
```

---

## Rules for fixing

1. **Keep the legal meaning**, unless changing it is the deliberate goal.
2. **Apply the KTZR golden rules** (especially consistent terminology, definitions, no repetition).
3. **Fit the context.** If the contract uses "Wykonawca", the fixed passage uses "Wykonawca" too, not "Zleceniobiorca".
4. **Don't invent clauses from scratch.** Take them from the KTZR bank.
5. **No comments inside the text.** A finished clause must paste into the document without cleanup. Comments go separately.

---

## Anti-patterns: what NOT to do

- ❌ Don't change a passage the user didn't ask about (for example the user asks for a fix to § 5, and you "improve" § 6 along the way).
- ❌ Don't add legal substance the user didn't ask for (for example the user asks to align the style, and you add contractual penalties "because they're missing").
- ❌ Don't write a long introduction ("I understood the request, here is the corrected passage taking into account..."). Go straight to the result.
- ❌ Don't leave placeholders like [insert amount here]. If you don't know something, **ask** instead of inserting placeholders.
