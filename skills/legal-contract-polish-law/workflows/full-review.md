# Workflow: full contract review (5 stages)

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

A 5-stage contract review workflow. **After each stage, stop and wait for the user's corrections** before moving on. This isn't a one-shot. It's a dialogue.

## Express mode (optional)

If the user explicitly says "do it all without asking", "express mode", or "all 5 stages at once", do every stage in one answer, still with each stage as its own section with a heading. Otherwise, go one stage at a time.

---

## STAGE 0/5: the firm's memory

If a firm memory tool is available, check it before the analysis. Earlier notes about this matter or counterparty can change the priorities.

1. `list_categories()`: if the memory is empty, skip the rest of this stage and go to STAGE 1.
2. If it isn't empty:
   - `recall("counterparty name")`: if the name appears in the contract
   - `recall("contract type")`: for example "body leasing", "NDA", "implementation"
   - `recall("risks negotiations")`: negotiating positions and risks flagged earlier

Show the hits before STAGE 1:

```
📋 Firm memory: context for this matter:
[summary of the hits, at most 5 entries, only what matters for this analysis]
```

If there are no hits, or no memory tool, **skip this section** and go to STAGE 1.

---

## STAGE 1/5: essentialia negotii

**Open:** `references/essentialia-map.md`

Map the five elements: contract type, parties, subject, remuneration, term. Then list the **critical elements for this contract type** from the reference file.

**Output format:**

```
## STAGE 1/5: ESSENTIALIA NEGOTII

- **Type:** [...]
- **Parties:** [Party A] (role) / [Party B] (role)
- **Subject:** [briefly, 1 to 2 sentences]
- **Remuneration:** [model + amount or rate + due date]
- **Term:** [fixed or indefinite + details]

### Critical elements for this contract type
- [...]
- [...]
```

**STOP. Ask:** "Do you confirm this mapping? Anything to add or correct before the completeness checklist?"

---

## STAGE 2/5: completeness checklist (15 points)

**Open:** `references/checklist-15.md`

Go through all 15 points. Mark each with a status (✅ / ⚠️ / ❌ / ➖) and a short reason (1 to 2 sentences).

**Output format:**

```
## STAGE 2/5: COMPLETENESS CHECKLIST (15 points)

1. **Preamble and date:** ✅ Date dd-mm-yyyy, Gdańsk, correct structure.
2. **Parties and representation:** ⚠️ No KRS number for the client; represented by a commercial proxy (prokurent) without stating the proxy.
3. **Definitions:** ❌ No definition of "Specjalista", although the text uses it.
[...]
15. **Final provisions:** ✅ All fine.

### Result: X/15 points met
```

At the end, list the **TOP 3 gaps** to fix.

**STOP. Ask:** "Shall we move on to the internal logic, or do you want to fix one of the gaps first?"

---

## STAGE 3/5: internal logic and consistency

Check the contract's internal consistency:

1. **Undefined terms:** every capitalised word must have a definition.
2. **Inconsistent party names:** for example "Wykonawca" in one paragraph and "Zleceniobiorca" in another.
3. **Broken internal cross-references:** "zgodnie z § 5 ust. 3" where § 5 has no section 3.
4. **Orphaned annexes:** named in the preamble but never referred to, or referred to but missing.
5. **Inconsistent deadlines:** for example "30 dni" in one place and "miesiąc" (a month) in another for the same thing.
6. **Repeated rules:** the same clause in two places.

### ⚠️ AUTOMATIC TRIGGER for long contracts

**Language models are known to lose connections in long documents** (attention dilution: the model's attention isn't uniform over a long context, especially for relations between distant passages).

**Check whether at least two of these hold:**
- The contract is over 15 pages or over 5,000 words.
- It has over 15 paragraphs.
- It has over 10 cross-references between paragraphs („§ X ust. Y").
- The first analysis (points 1 to 6 above) found over 3 inconsistencies.
- Keywords that signal complexity: „Załącznik", „z zastrzeżeniem", „powyższe", „stosuje się odpowiednio" (annex, subject to, the above, applies accordingly).

**If at least two hold:** instead of a 1 to 2 sentence summary, **open `workflows/cross-reference-check.md`** and follow its two-pass procedure (inventory, then verification). It takes 5 to 10 minutes, but it catches errors a single pass misses.

Tell the user:

> *"The contract is long and has many cross-references between paragraphs. Language models lose connections in long documents. I suggest a dedicated cross-reference check (a two-pass workflow: inventory, then verification). It takes 5 to 10 minutes. OK?"*

If the user agrees, run `cross-reference-check.md` in full (Pass 1 → STOP → Pass 2 → report). Put its result into STAGE 3 in place of the standard format below.

If the user declines, or the contract is short, do the standard analysis below.

### Standard output format (short contracts)

```
## STAGE 3/5: INTERNAL LOGIC

### Undefined terms
- "Timesheet" (§ 5 ust. 2): used without a definition
- "Wada Krytyczna" (§ 8): definition missing

### Inconsistent naming
- ✅ Consistent ("Usługodawca" throughout)

### Internal cross-references
- ❌ § 6 ust. 4 refers to "§ 4 ust. 5", but § 4 has only 3 sections

### Annexes
- ⚠️ Annex 2 (timesheet template) is named in the text but missing from the list of annexes

### Repetitions
- ⚠️ A late-delivery penalty appears in § 9 ust. 2 and § 13 ust. 1. Check whether it's a deliberate distinction or a duplicate.
```

**STOP. Ask:** "Shall we move on to the risk audit, or fix the logic first?"

---

## STAGE 4/5: risk audit

Identify all legal and business risks, each with a level and location.

**Levels:**
- 🔴 **CRITICAL:** can lead to invalidity, unlimited liability, loss of rights, or enforcement by the other side
- 🟠 **HIGH:** significant financial or operational risk; needs immediate negotiation
- 🟡 **MEDIUM:** worth fixing, but not a deal-breaker
- 🟢 **LOW:** minor inaccuracies, style improvements

**Output format (each risk):**

```
🔴 CRITICAL | § 11 ust. 2: Unlimited liability
No cap on the contractor's liability. For damage caused by ordinary fault, the contractor is liable in full, including lost profits.
**Recommendation:** Add a cap (for example 12 months of fees), exclude lost profits, and keep the intentional-fault exception (art. 473 § 2 KC). Clauses to use: `references/clause-bank/11-odpowiedzialnosc.md`.
```

At the end, give a **safety score (0 to 100)** with the reasoning.

**STOP. Ask:** "Shall we move on to the recommendations, or discuss one of the risks first?"

---

## STAGE 5/5: summary and recommendations

**Output format:**

```
## STAGE 5/5: SUMMARY AND RECOMMENDATIONS

### TOP 3 to fix
1. **[Problem]:** `[paragraph]`. Recommended clause from: `[bank file]`
2. [...]
3. [...]

### Suggested terminology changes
- "Zleceniobiorca" → "Wykonawca" (consistent with § 1)
- [...]

### Overall assessment
[2 to 3 sentences: sign, negotiate, or rework thoroughly]
```

**At the end (only here):**

> *This analysis is supporting material and doesn't replace the assessment of the radca prawny handling the matter.*

---

## Agentic behaviour: what to do when the user interrupts

- If after stage 2 the user writes "fix § 5 ust. 3": pause the workflow, run `workflows/fix-clause.md`, then ask "shall we resume the analysis from stage 3?"
- If the user writes "that's enough" or "thanks" after a stage: stop, don't push.
- If the user pastes a different contract: it's a new task, so start the workflow again.
- If the user asks for a clause from the bank: point to the right file in `references/clause-bank/` and return to the workflow.
