# Workflow: cross-reference and consistency check

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

A dedicated two-pass workflow for finding **broken cross-references and internal inconsistencies** in long contracts (typically 15+ pages). It addresses a common problem: the model reads each paragraph well on its own, but sees **the relations between distant passages** less well. That's the effect of attention dilution in a long context.

## When to run this workflow

**Automatically** (the agent decides):
- The contract is over 15 pages or over 5,000 words
- It has over 15 paragraphs
- It has over 10 cross-references between paragraphs („§ X ust. Y")
- The first analysis (stage 3 of the full review) found over 3 inconsistencies

**At the user's request:**
- "Check the cross-references in this contract"
- "Do the paragraphs line up?"
- "Check internal consistency"
- "Are there numbering errors?"

**Standalone** (without a full review): the full procedure.
**As stage 3** (inside `full-review.md`): a simpler presentation, the same method.

## Why two passes

The **attention dilution** problem in long contexts doesn't go away even with 200K windows. The model "sees" the whole contract, but its attention **isn't uniform**: relations between distant passages (for example a reference in § 18 to a definition in § 2) are tracked less well than the content of a single paragraph.

The solution: **separate the inventory from the verification**.

- **PASS 1** is a plain list. The model doesn't analyse, it only lists. That forces it to go **through the whole document** without trying to infer.
- **PASS 2** checks one item at a time. The model checks **each cross-reference separately**, in a table that forces an explicit check of every item (instead of trusting its contextual memory).

This forces the model to *see* a broken reference such as „§ 8 ust. 3", because it must write into the table what § 8 ust. 3 actually says.

---

## PASS 1: INVENTORY (a list, not an analysis)

### Step 1.1: inventory of the contract's structure

List **every paragraph** of the contract with a short description (at most 1 sentence) of what it governs. Plus the annexes.

**Output format:**

```
## STRUCTURE INVENTORY

### Paragraphs
| § | Title | Number of sections | Short description (1 sentence) |
|---|-------|----------------|------------------------|
| § 1 | Definicje | 12 | A glossary of the 12 terms used in the contract |
| § 2 | Przedmiot umowy | 4 | IT services provided by the Usługodawca to the Usługobiorca |
| § 3 | Wynagrodzenie | 6 | Hourly rate of PLN 250, monthly invoices, 14-day term |
| ... | ... | ... | ... |

### Annexes
| No. | Title | Mentioned in § | In the package? |
|----|-------|------------------|--------------------|
| 1 | Technical specification | § 2 ust. 1 | ✅ YES |
| 2 | Timesheet template | § 4 ust. 3 | ❓ Unclear (I don't see it in the material provided) |
| ... | ... | ... | ... |
```

### Step 1.2: inventory of cross-references

List **every cross-reference** in the contract: between paragraphs, to annexes, and semantic ones.

**Three categories:**

**A. Explicit references** (pointing to a specific drafting unit):
- „§ X", „§ X ust. Y", „§ X ust. Y pkt Z"
- „Załącznik nr X"

**B. Semantic references** (needing interpretation):
- „powyższe postanowienia" (the above provisions)
- „niniejszy paragraf" (this paragraph)
- „wskazane wyżej" (indicated above)
- „z zastrzeżeniem § X" (subject to § X)
- „z wyłączeniem przypadków, o których mowa w..." (excluding the cases referred to in...)

**C. References to definitions** (capitalised terms):
- „Strona", „Wykonawca", „Usługodawca", „Specjalista", „System", „Utwór", and so on

**Output format:**

```
## CROSS-REFERENCE INVENTORY

### A. Explicit references (total: N)

| # | Source location | Reference text |
|---|---------------------|-----------------|
| 1 | § 4 ust. 2 | "zgodnie z § 3 ust. 1" |
| 2 | § 5 ust. 3 | "Wynagrodzenie określone w § 3" |
| 3 | § 8 ust. 4 | "Załącznik nr 2 (Wzór Timesheet)" |
| ... | ... | ... |

### B. Semantic references (total: N)

| # | Source location | Reference text |
|---|---------------------|-----------------|
| 1 | § 5 ust. 4 | "Powyższe nie wyłącza..." |
| 2 | § 9 ust. 2 | "z zastrzeżeniem ust. 3" |
| ... | ... | ... |

### C. References to definitions (total: N)

All capitalised terms used in the text (with the number of occurrences):
- "Strona" (12×), "Wykonawca" (45×), "Specjalista" (8×), "System" (23×), and so on
```

### Step 1.3: inventory of definitions

From § Definicje (or elsewhere), list **every defined term**:

**Output format:**

```
## DEFINITIONS INVENTORY

| # | Term | Where defined | Definition (short) |
|---|--------|----------------------|-------------------|
| 1 | "Strona" | § 1 ust. 1 | Usługodawca or Usługobiorca |
| 2 | "Specjalista" | § 1 ust. 5 | The Usługodawca's employee seconded under the contract |
| 3 | "System" | § 1 ust. 8 | The software covered by the Contract |
| ... | ... | ... | ... |
```

### STOP 1: confirm the inventory

> **Question for the user:** *"Inventory done. Is the list of annexes complete? Are there documents I should take into account but can't see? Shall we move on to verification (Pass 2)?"*

Without this STOP, you could flag references to annexes as missing when they exist but simply weren't provided.

---

## PASS 2: VERIFICATION (each item separately)

### Step 2.1: verify explicit references

For **every** reference in table A from Pass 1, verify it in a table:

```
## VERIFICATION OF EXPLICIT REFERENCES

| # | Source | Reference | Target exists? | Target content (short) | Fits the context? | Status |
|---|--------|-----------|---------------|--------------------|--------------------|--------|
| 1 | § 4 ust. 2 | "zgodnie z § 3 ust. 1" | ✅ YES | "Wynagrodzenie netto wynosi 250 PLN za godzinę" | ✅ YES | ✅ OK |
| 2 | § 5 ust. 3 | "Wynagrodzenie określone w § 3" | ✅ YES | § 3 governs remuneration (whole paragraph) | ✅ YES | ✅ OK |
| 3 | § 8 ust. 4 | "Załącznik nr 2 (Wzór Timesheet)" | ❓ Annex mentioned but not in the package | | | ⚠️ TO CONFIRM |
| 4 | § 12 ust. 1 | "kary umowne, o których mowa w § 9 ust. 3" | ✅ YES | "Kara umowna za naruszenie poufności..." | ❌ NO: § 9 ust. 3 sets the penalty for CONFIDENTIALITY, but § 12 is about the penalty for DELAY | 🔴 WRONG REFERENCE |
| 5 | § 15 ust. 2 | "zgodnie z § 17" | ❌ NO. The last paragraph is § 16 | | | 🔴 NON-EXISTENT REFERENCE |
| 6 | § 11 ust. 4 | "wskazane w §___" | | | | 🔴 EMPTY REFERENCE FIELD |
```

**Status categories:**

- ✅ **OK:** the reference is correct, the target exists, and its content fits the context
- ⚠️ **TO CONFIRM:** the target exists, but the interpretation is unclear (for example a semantic reference, or an annex missing from the package)
- 🔴 **WRONG REFERENCE:** the target exists, but its content does NOT fit the context of the reference
- 🔴 **NON-EXISTENT REFERENCE:** the paragraph, section, or point referred to doesn't exist in the contract
- 🔴 **EMPTY FIELD:** the author left an unfilled placeholder (rare, but it happens)

### Step 2.2: verify semantic references

Each semantic reference needs **contextual decoding**: what exactly "the above", "this", or "indicated" refers to.

```
## VERIFICATION OF SEMANTIC REFERENCES

| # | Source | Reference | What should it point to? | What's actually there? | Status |
|---|--------|-----------|---------------------------|------------------------------------|--------|
| 1 | § 5 ust. 4 | "Powyższe nie wyłącza..." | § 5 ust. 1-3 (on obligations) | § 5 ust. 1-3 are about the Parties' obligations. Fits. | ✅ OK |
| 2 | § 9 ust. 2 | "z zastrzeżeniem ust. 3" | § 9 ust. 3 | § 9 ust. 3 exists and adds an exception | ✅ OK |
| 3 | § 14 ust. 1 | "wskazane wyżej" | Unclear. § 13 before it is about confidentiality, but § 14 is about termination | No logical link | ⚠️ UNCLEAR |
```

### Step 2.3: verify definitions

```
## VERIFICATION OF DEFINITIONS

### Defined but NOT USED in the text ("zombie definitions")
- "Materiały Marketingowe" (§ 1 ust. 7). Defined, but no paragraph uses it. **Delete it or use it.**

### USED capitalised but NOT DEFINED
- "Konsultant" (used in § 8 ust. 2). No definition in § 1. **Guess:** it means the Specjalista, but that needs aligning. 🔴
- "Punkt Kontroli" (used in § 11 ust. 3): no definition. ⚠️

### Inconsistent spelling (capitalised in some places, lower case in others)
- "Specjalista" / "specjalista". Capitalised in §§ 1, 4, 5, lower case in § 8 ust. 4. Check whether the distinction is deliberate. ⚠️

### Repeated definitions (the same term defined twice with different meanings)
- "Strona". Defined in § 1 ust. 1 (Usługodawca / Usługobiorca) and again in § 13 ust. 2 (a party to court proceedings, "Strona Postępowania"). Inconsistent. 🔴
```

### Step 2.4: verify amounts, dates, and terminology

```
## CONSISTENCY VERIFICATION

### Amounts and percentages

| Value | Where it appears | Consistency |
|---------|---------------------|----------|
| Hourly rate | Preamble: "250 PLN" / § 3 ust. 1: "250 zł netto" / Annex 1: "260 PLN" | 🔴 INCONSISTENT |
| Liability cap | § 11 ust. 2: "100% rocznego wynagrodzenia" | OK (one place) |
| Delay penalty | § 9 ust. 1: "0,5% za dzień" / § 12 ust. 3: "0,5% miesięcznego wynagrodzenia" | ⚠️ Different bases of calculation: check the intent |

### Dates and deadlines

| Value | Where it appears | Consistency |
|---------|---------------------|----------|
| Date of signing | Preamble: "12-05-2026" | OK |
| Start of services | § 2 ust. 3: "od 1 czerwca 2026" / Schedule (Annex 1): "od 15 maja 2026" | 🔴 INCONSISTENT |
| Notice period | § 14 ust. 1: "3 miesiące" / § 14 ust. 2 (for breach): "30 dni" | OK (different grounds for termination) |

### Terminology and party names

| Term | Locations | Consistency |
|--------|-------------|----------|
| Name of the first party | Preamble: "Usługodawca" / § 4 ust. 2: "Wykonawca" / § 8: "Spółka" | 🔴 INCONSISTENT |
| Name of the service | "Usługi" / "Świadczenie" / "Czynności" | ⚠️ Needs aligning |
```

---

## FINAL REPORT

```
## FINAL REPORT: CROSS-REFERENCES AND CONSISTENCY

### Statistics
- Paragraphs: N
- Annexes named: N (in the package: M, unclear: K)
- Explicit references: N (OK: X, errors: Y, to confirm: Z)
- Semantic references: N
- Defined terms: N (used: X, "zombie": Y)
- Terms used but undefined: N

### CRITICAL ERRORS (🔴): fix at once
1. § 12 ust. 1, wrong reference: "kary umowne, o których mowa w § 9 ust. 3", but § 9 ust. 3 is about a DIFFERENT penalty (confidentiality, not delay). **Fix:** change to "§ 9 ust. 1" (the delay penalty).
2. § 15 ust. 2, reference to the non-existent § 17. **Fix:** establish what it was meant to point to, possibly § 16 (a late change during editing).
3. Hourly rate: 250 vs 260 PLN across the preamble, § 3, and Annex 1. **Fix:** align them.
4. Party name: "Usługodawca" / "Wykonawca" / "Spółka". **Fix:** pick one name (under art. 750 KC, "Usługodawca").

### WARNINGS (⚠️): confirm with the author
1. § 8 ust. 4, Annex 2 "Wzór Timesheet" is named, but I don't see it in the package. Does it exist?
2. § 14 ust. 1: the unclear reference "wskazane wyżej".
3. § 9 ust. 1 vs § 12 ust. 3: the contractual penalties use different bases (% per day vs % of monthly fees). A deliberate distinction or an error?

### MINOR INCONSISTENCIES (to tidy up)
1. Spelling "Specjalista" / "specjalista": align.
2. The definition "Materiały Marketingowe" is defined but unused: delete it or use it.
```

**STOP. Ask:** *"Report ready. Shall we fix the clauses with critical errors (workflows/fix-clause.md), or do you want to discuss one of the warnings first?"*

---

## Short mode: for short contracts (under 15 pages)

If the contract is under 15 pages or has fewer than 8 paragraphs, **don't run the full two-pass procedure**. Do a short check in one step:

1. A table of (explicit) references with 5 columns: location / reference / target exists? / fits? / status
2. A list of defined vs used terms
3. A list of inconsistencies in amounts and terminology

No STOPs. No Pass 1 / Pass 2.

---

## Anti-patterns this workflow should catch (typical errors in contracts edited in stages)

1. **Renumbering after an edit:** the author added a section but didn't update references in other paragraphs. Common when several people work on it.
2. **Deletion with a leftover reference:** the author deleted § 7 (for example as unnecessary), but § 12 still says „zgodnie z § 7".
3. **A definition was renamed:** „Pracownik" was renamed „Specjalista" in § 1, but §§ 8 and 11 still say „Pracownik".
4. **A number changed in one place only:** the fee was changed in § 3 during negotiation, but the preamble and the annex still have the old amount.
5. **An annex named but missing:** § 4 ust. 3 refers to „Załącznik nr 2 (Wzór Timesheet)", but the list of annexes at the end has only Annex 1.
6. **An annex attached but never mentioned:** the reverse: the package has Annex 4, but nothing in the contract refers to it. A useless annex.
7. **An empty reference field:** „zgodnie z §___", left unfilled from the template.
8. **Circular references:** „§ 5 ust. 2 stosuje się odpowiednio do § 12 ust. 3, z zastrzeżeniem § 5 ust. 2". A logical error.
9. **A reference to a repealed section:** during editing a section was marked „(uchylony)" (repealed) or deleted, but another place still refers to it.
10. **Inconsistent past or future dates:** the preamble has today's date, but § Term has a date two months earlier (a typical template copying error).

## Operating rule: when the agent runs this workflow on its own

Without asking the user, if it detects **at least two** of these:
- The contract is over 15 pages or over 5,000 words
- Over 15 paragraphs
- Over 10 cross-references between paragraphs
- Over 3 initial inconsistencies
- Keywords that signal complexity: „Załącznik", „z zastrzeżeniem", „powyższe", „wskazane w", „stosuje się odpowiednio"

In that case, after stage 2 of the full review (the checklist), the agent says:

> *"The contract is long and has many cross-references between paragraphs. Language models are known to lose connections in long documents (attention dilution). I suggest a dedicated cross-reference check before the risk audit. It's a two-pass procedure (inventory + verification) and takes 5 to 10 minutes. OK?"*

---

## When the agent alone isn't enough: NotebookLM as a complement

Experience shows that for contracts of **30+ pages with a very dense web of cross-references**, even the two-pass check can let some errors through. In those cases **NotebookLM (Google)** gives clearly better results, for a specific architectural reason.

### Why NotebookLM is stronger on long documents

**1. RAG instead of pure long context.** NotebookLM indexes the document into chunks with embeddings and, for each question, retrieves the specific passages relevant to it. For the question *"what exactly does § 8 ust. 3 say"*, the model gets **focused context** around § 8 ust. 3, not 30 pages of scattered attention.

**2. Forced citation of the source.** With every answer, NotebookLM shows **the specific passage** it relies on. That forces the model to actually look at the document rather than infer from contextual memory. It's the architectural version of what the two-pass workflow tries to enforce through procedure.

**3. Fewer misses across many questions.** In one session you can ask 20 to 30 questions, and each gets a fresh retrieval. In a standard agent chat the conversation grows and the context gets "diluted".

### When to recommend moving to NotebookLM

The agent should **suggest** NotebookLM itself if, after running the check workflow:

- The contract is over 30 pages (an empirical threshold; above it even the two-pass process isn't enough)
- There's a **suspicion** that the workflow didn't catch everything (for example the user noticed an inconsistency by hand that wasn't in the report)
- The contract has over 30 cross-references between paragraphs
- The contract has over 5 annexes that many paragraphs refer to
- The contract was **edited many times** (negotiations, several rounds of changes), so the renumbering risk is high

### Message to the user

> *"The check found X errors, but for a contract this long (Y pages, Z cross-references) I also recommend checking it in NotebookLM (Google). NotebookLM uses RAG: it indexes the document and retrieves specific passages, which gives better accuracy on very long contracts. Suggested questions for NotebookLM (2 to 3 calls):*
> *1. "List every cross-reference between paragraphs in the contract and verify each one."*
> *2. "List every capitalised term and check that each is defined in § Definicje."*
> *3. "Check the consistency of amounts, dates, and terminology between the preamble, the body, and the annexes."*
> *After checking in NotebookLM, come back with the results. We'll compare them with my report and put together the full list of fixes."*

### Why 2 to 3 calls in NotebookLM

NotebookLM isn't perfect either, for two reasons:

**A. Chunking doesn't always respect legal structure.** NotebookLM splits the document heuristically (~500 to 1,000 tokens per chunk). It can separate § 8 ust. 3 from the rest of § 8, which breaks the local context. So differently worded questions hit different passages.

**B. Global consistency questions are the opposite of RAG.** *"Is this contract internally consistent in its terminology?"* needs a view of the whole, while RAG retrieves fragments. So the questions have to be **broken down** (terminology, amounts, and dates separately), which gives the 2 to 3 calls.

### Agent → NotebookLM → agent

The strongest path for very long contracts:

1. **The agent (this skill):** the full 5-stage review + the Pass 1 / Pass 2 check
2. **NotebookLM:** 2 to 3 calls dedicated to checking references, terminology, and amounts
3. **Back to the agent:** combine both reports, resolve conflicts, and draw up the list of fixes with the right clauses from `references/clause-bank/`

NotebookLM **doesn't replace** the skill. It complements it in a narrow but important layer: checking the internal consistency of very long contracts. The doctrinal layer (`references/knowledge-base/`), the clause layer (`references/clause-bank/`), the style layer (`references/drafting-style.md`), and the agentic workflow all stay with the agent.
