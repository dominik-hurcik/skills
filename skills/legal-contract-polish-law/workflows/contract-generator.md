# Workflow: contract generator (5 steps, with context)

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

> **R3, NON-LAWYER:** extra signals for contracts: "I have to sign a contract", "I'm a client of [company X]", "check whether I can sign this".

A 5-step workflow for generating a new contract in the KTZR style. **Each step needs the user's approval** before moving on. The generator can work with extra **context** (client emails, notes, a brief, reference documents).

The contract text itself is drafted in Polish. Your explanations, questions, and QA notes are in English.

## Taking the brief and context

The minimum brief from the user:
- **Contract type** (from this list: IT body leasing, NDA, IT services, implementation, SaaS, transfer of copyright, cooperation, mandate, accounting, settlement, assignment, other)
- **Party A** (the client: name, legal form, KRS/NIP, address)
- **Party B** (the counterparty: name, legal form, KRS/NIP, address)
- **Key terms** (subject, remuneration, term, special requirements)

**Extra context (optional):** emails, meeting notes, the counterparty's draft, reference documents. If the user provides context, treat it as **a source of facts about the matter**, not as binding on the contract's content. From the context, take the parties' actual agreements, intentions, business risks, and preferred terminology.

**Important: the generator is cut off from any "current contract".** Unlike the analysis workflow, the generator doesn't read any existing contract as a basis. Exception: the user says explicitly "base it on this contract" or "use this as a template".

---

## STEP 0/5: the firm's memory

If a firm memory tool is available, check it for this matter after you receive the brief and before the analysis.

1. `list_categories()`: if the memory is empty, skip the rest of this step and go to STEP 1.
2. If it isn't empty:
   - `recall("counterparty name")`: Party B from the brief
   - `recall("contract type")`: for example "body leasing", "NDA", "SaaS"
   - `recall("negotiation position")`: earlier negotiation agreements

Show the hits in the STEP 1 section as:

```
### 📋 Firm memory: context for this matter
[summary of the hits, what matters for this contract]
```

If there are no hits, or no memory tool, **skip this section** and go to STEP 1.

---

## STEP 1/5: analyse the brief

**Open:** `references/essentialia-map.md`

Analyse the brief and context. Answer **briefly** (at most one page):

1. **Type of legal relationship** (with its basis: art. 750 KC for services, 627 KC for a specific work, 41 PrAut for a licence, and so on)
2. **The parties and their roles** (who delivers what, who pays for what)
3. **Key risks:** the top 3 legal risks typical for this contract type, plus any others from the context
4. **Missing information:** what the brief lacks for a complete contract (amounts, deadlines, fields of exploitation, and so on)
5. **Recommendation:** go ahead with what we have, or complete the brief first

Also list the **mandatory elements** for this contract type from `essentialia-map.md`.

**STOP. Ask:** "Can we plan the structure, or do you want to complete the brief first?"

---

## STEP 2/5: plan the structure

**Open:** `references/clause-bank/INDEX.md`

Plan **the contract's structure paragraph by paragraph**. Format:

```
## CONTRACT STRUCTURE

§ 1. Przedmiot Umowy
   → clauses from: `04-przedmiot-umowy.md` (IT body leasing)

§ 2. Definicje
   → clauses from: `03-definicje.md` (IT body leasing)
   → definitions to add: Specjalista, Timesheet, Utwór, Informacje Poufne

§ 3. Obowiązki Stron
   → clauses from: `05-obowiazki-stron.md`

§ 4. Wynagrodzenie
   → clauses from: `06-wynagrodzenie.md`

§ 5. Prawa autorskie
   → clauses from: `08-prawa-autorskie-ip.md`

[...]

§ N. Postanowienia końcowe
   → clauses from: `17-postanowienia-koncowe.md`

### Annexes
- Załącznik nr 1: Wzór Zamówienia (order template)
- Załącznik nr 2: Wzór Timesheet (timesheet template)
- Załącznik nr 3: Lista Specjalistów (list of Specialists)
```

**Planning rules:**
- Use **only clauses from the KTZR bank** (`references/clause-bank/`). Don't invent new ones.
- Pick the source closest to the contract type (for body leasing, the clauses specific to IT body leasing, not generic patterns).
- List the **definitions to add**.
- List the **annexes** with specific names.

**STOP. Ask:** "Do you accept this structure? Anything to add or change before I write the draft?"

If the user asks for changes, apply them and show the UPDATED structure before STEP 3.

---

## STEP 3/5: write the draft

**Open now (if not already open):** `references/drafting-style.md`. It holds the specific KTZR syntax patterns (conditional constructions, definitions, lists, party names). Write the draft **in this style**, not by generic contract conventions.

Using the approved structure, write **the full contract**.

### Writing rules

1. **Only clauses from the KTZR bank.** No improvising. If the bank has no clause for something the structure needs, **stop and ask the user** instead of inventing one.

2. **Fit the context:**
   - Specific party names (from the brief, not placeholders like "[Strona A]")
   - Specific amounts, rates, and deadlines (from the brief)
   - Consistent naming (if "Usługodawca" in § 1, then "Usługodawca" throughout)
   - Working cross-references (after the draft, check every „§ X ust. Y")

3. **Definitions in § Definicje:**
   - Every capitalised term in the text must be defined here.
   - Definitions in alphabetical order.
   - Definition format: „Termin" oznacza (...). No dashes.

4. **The KTZR golden rules** take precedence over the clause bank. For example, if a bank clause refers to "zgodnie z § 5" but § 5 is something else in your structure, fix the reference.

5. **Quoted provisions must be verified.** For every article cited in a clause (for example „art. 473 § 2 KC", „art. 28 RODO"), call `verify_article()` before writing its wording. If the MCP server isn't available, add `[UNVERIFIED]` next to the citation. An invented provision disqualifies the draft.

### Output format

```
UMOWA [TYP]

zawarta w dniu [data] w [miejscu], pomiędzy:

[Strona A z pełnymi danymi i reprezentacją]
zwaną dalej „[Rola]"

a

[Strona B z pełnymi danymi i reprezentacją]
zwaną dalej „[Rola]"

Strony postanawiają, co następuje:

§ 1. Przedmiot Umowy

[Clause text from the bank, fitted]

§ 2. Definicje

W rozumieniu niniejszej Umowy:
1. „Termin1" oznacza (...);
2. „Termin2" oznacza (...);
[...]

[Clause text from the bank, fitted]

[...]

§ N. Postanowienia końcowe

1. [Severability clause]
2. [Form of amendments]
3. [Annexes]
4. [Copies]
5. [Entry into force]

___________________            ___________________
[Strona A]                     [Strona B]

Załączniki:
1. [Annex name]
2. [...]
```

**STOP. Ask:** "Shall we check completeness, or do you want to fix something in the draft first?"

---

## STEP 4/5: check completeness

**Open:** `references/checklist-15.md`

Check the draft against **the 15-point checklist**. For each point: ✅ / ⚠️ / ❌ / ➖ (N/A). Then:

1. **Missing elements:** what should be there and isn't
2. **Comment on the contract type:** whether type-specific elements (from `essentialia-map.md`) are missing
3. **Surplus elements:** what's unnecessary and can go
4. **Recommendations:** what to add before the quality check

Then **add the missing paragraphs** (full text, from the clause bank) and return **the WHOLE draft with the fixes** (not just the changes: the full text, ready for further work).

**STOP. Ask:** "Shall we do the quality check, or do you want to add or change anything else?"

---

## STEP 5/5: quality check (QA)

Do a final check:

1. **Consistent definitions:** every capitalised use = a definition in § Definicje
2. **Internal cross-references:** every „§ X ust. Y" leads to an existing provision
3. **Terminology:** one concept, one term
4. **Annexes:** every annex named in the preamble or at the end is also referred to in the body
5. **Numbering:** paragraphs, sections, and points numbered consistently
6. **Party details:** KRS, NIP, REGON, and addresses complete and correctly formatted
7. **Dates and deadlines:** full dates (dd-mm-yyyy), deadlines in consistent units (days or working days)
8. **KTZR golden rules:** check each of the 12 rules

Return **the FINAL VERSION** of the contract: the contract text only, **with no comments inside it**. Put the QA comments separately, BEFORE the final version, in this format:

```
## QUALITY CHECK

✅ All definitions consistent (12 terms checked)
✅ Internal cross-references: 8/8 lead to existing provisions
⚠️ The term "Dni Robocze" in § 5 ust. 3. § 1 defines it as "dni od pn. do pt. z wyłączeniem dni ustawowo wolnych" (Monday to Friday, excluding public holidays); check consistency
[...]
```

---

## FINAL GATE

Show the user these questions and **wait for an answer** before generating:

```
⛔ Before the final version, please confirm:
1. Have the parties' details (KRS, NIP, addresses) been checked against the source?
2. Have the cited provisions been checked (verify_article or manually)?
3. Has the lawyer handling the matter seen this draft?

→ "yes, generate the final version" / or say what to fix
```

Generate only after confirmation. Without confirmation, put `[DRAFT, FOR REVIEW]` above the document and stop.

Exception: if the user said "express mode" or "do it without asking", generate, but add `[DRAFT, FOR REVIEW]` at the start and end of the document.

---

## FINAL CONTRACT

[clean text ready to paste into the document, with no comments inside it]

---

## Iteration: REDRAFT

If after step 5 the user wants to change the draft ("change § 4, add indexation", "remove clause X", "add non-solicitation"):

1. Open the right file in the clause bank and take the clause.
2. Apply the change to the final text.
3. Run STEP 5 (QA) again. Check the change didn't break cross-references, definitions, or numbering.
4. Return the whole draft again.

---

## Special mode: generating with context

If the user provided **context** (emails, notes, the counterparty's draft, a business brief), add this section in **STEP 1**:

```
### What I took from the context
- Agreement 1: [...]
- Agreement 2: [...]
- The parties' preferred terminology: "Klient" instead of "Zamawiający"
- Risk identified by your client: [...]
```

This lets the user check that you understood the context before you start writing. In later steps, take the context's agreements into account (amounts, terminology, risks), but don't copy text from the context into the contract. The contract is always built from KTZR clauses.
