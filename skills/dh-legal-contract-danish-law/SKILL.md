---
name: dh-legal-contract-danish-law
disable-model-invocation: true
description: Review, triage, or draft B2B contracts governed by Danish law, focused on SaaS, IT services, software development, NDAs, and IP assignment. Checks the contract against Danish mandatory rules, including the ban on no-hire clauses, the B2B payment-term cap, the Copyright Act's transfer rules, and the Contracts Act's unfair-terms rule. Use when a contract names Danish law or Danish courts, or when the user asks how Danish law affects a clause.
---

# Danish contract law

This skill reviews and drafts B2B contracts under Danish law for a SaaS or software business. It works in English and quotes Danish statutes in Danish.

This skill was written by an AI assistant from the official statute texts on retsinformation.dk, checked on 16 October 2026. No Danish lawyer has reviewed it. Treat its output as preparation for a lawyer, not as legal advice. For a contract that matters, have a Danish advokat confirm the findings before signing.

## Rules that apply to every task

1. **Cite only what you verified.** Every statement about Danish law must cite a statute and section from `references/mandatory-rules.md`, or a provision you fetched from the official source during this task. If you can't cite it, say it's unverified.
2. **Check the current text before relying on a section.** The references record what was in force on 16 October 2026. For any section that decides a finding, fetch the current text as described in `references/sources.md`. If the register shows a newer consolidated act or an amendment to that section, use the new text and say so.
3. **Separate law from practice.** Statements marked "practice note" in the references come from general knowledge of Danish practice, not from a statute. Label them that way in your output.
4. **Know the scope.** This skill covers B2B contracts. If one party is a consumer, say so and flag that consumer rules apply, starting with Aftaleloven §§ 38 a to 38 d. Employment contracts, real estate, and public procurement are out of scope.
5. **Never invent a case, a section number, or an amount.** If the answer depends on case law you can't fetch, say that and recommend a Danish lawyer.

## Choose the task

| The user wants | Do this |
| --- | --- |
| A quick verdict on a contract | Run the triage below and stop. |
| A full review | Run the full review below. |
| A clause or a full contract drafted | Run the drafting steps below. |
| An answer to one question | Answer from `references/mandatory-rules.md`, with the citation, then stop. |

If the request is unclear, ask which of these the user wants before you start.

## Triage

1. Confirm the contract is B2B and under Danish law. Check the governing-law and jurisdiction clauses. If Danish law doesn't apply, say so and stop.
2. Read `references/mandatory-rules.md`.
3. Scan the contract for the red flags listed at the top of `references/clause-checklist.md`.
4. Give a verdict of GREEN, YELLOW, or RED, with one line per finding and its citation. RED means a clause is likely void or the contract misses something the law requires. YELLOW means a clause is risky or unclear. GREEN means you found no issue on the checklist.

## Full review

1. Do the triage steps.
2. Identify the contract type: SaaS subscription, software development, IT services or consulting, NDA, IP assignment, or data processing agreement.
3. Go through every section of `references/clause-checklist.md` that applies to that type.
4. For each finding, give the clause reference, the problem, the Danish rule with its citation, the risk for the user's side, and a suggested fix.
5. List the sections you verified against the current official text, and the ones you didn't.
6. End with the three changes that matter most.

## Drafting

1. Ask for the contract type, which side the user is on, the parties, the services, the fees, and the contract language.
2. Read `references/mandatory-rules.md` and `references/clause-checklist.md`.
3. Draft clauses that comply with the mandatory rules. In particular:
   - Don't include a no-hire or non-solicitation clause covering the other party's employees. Lov om ansættelsesklausuler § 3 makes it void, unless the business-transfer exception in § 4 applies.
   - For software or other copyright works made by a contractor, include an explicit assignment that lists the uses, the right to modify, and the right to transfer onward. Ophavsretsloven §§ 53 and 56 read transfers narrowly, and § 59 only gives the employer software made by its own employees.
   - Keep B2B payment terms at 30 days from the invoice or less, unless the creditor expressly accepts a longer term. See renteloven § 3 a.
4. Mark every assumption and open question in the draft as `[TO CONFIRM: ...]`.
5. Add a note at the top that a Danish lawyer should review the draft before use.

## Output

- Write in English unless the user asks for Danish. Quote statute text in Danish, then translate it.
- Cite statutes by short name and section, for example "Aftaleloven § 36". Use the full identifiers from `references/sources.md` in a sources list at the end.
- Keep the disclaimer from the top of this skill in every review and draft.
