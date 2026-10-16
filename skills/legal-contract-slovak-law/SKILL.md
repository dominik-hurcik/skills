---
name: legal-contract-slovak-law
disable-model-invocation: true
description: Review, triage, or draft B2B contracts governed by Slovak law, focused on SaaS, IT services, software development, NDAs, and software licences. Checks the contract against Slovak mandatory rules, including the ban on waiving damages in advance, court reduction of contractual penalties, the 4-year limitation period, and the rule that copyright can only be licensed, never assigned. Use when a contract names Slovak law or Slovak courts, or when the user asks how Slovak law affects a clause.
---

# Slovak contract law

This skill reviews and drafts B2B contracts under Slovak law for a SaaS or software business. It works in English and quotes Slovak statutes in Slovak.

This skill was written by an AI assistant from the official statute texts on slov-lex.sk, checked on 16 October 2026. No Slovak lawyer has reviewed it. Treat its output as preparation for a lawyer, not as legal advice. For a contract that matters, have a Slovak advokát confirm the findings before signing.

## Rules that apply to every task

1. **Cite only what you verified.** Every statement about Slovak law must cite a statute and section from `references/mandatory-rules.md`, or a provision you fetched from the official source during this task. If you can't cite it, say it's unverified.
2. **Check the current text before relying on a section.** The references record the versions in force on 16 October 2026. For any section that decides a finding, fetch the current version as described in `references/sources.md`. If a newer version changes that section, use the new text and say so.
3. **Separate law from practice.** Statements marked "practice note" in the references come from general knowledge of Slovak practice, not from a statute. Label them that way in your output.
4. **Know the scope.** This skill covers B2B contracts under the Commercial Code (Obchodný zákonník). If one party is a consumer, or the relationship falls under the Civil Code (Občiansky zákonník), say so and flag that this skill's rules may not apply. Employment contracts, real estate, and public procurement are out of scope.
5. **Never invent a case, a section number, or an amount.** If the answer depends on case law you can't fetch, say that and recommend a Slovak lawyer.

## Choose the task

| The user wants | Do this |
| --- | --- |
| A quick verdict on a contract | Run the triage below and stop. |
| A full review | Run the full review below. |
| A clause or a full contract drafted | Run the drafting steps below. |
| An answer to one question | Answer from `references/mandatory-rules.md`, with the citation, then stop. |

If the request is unclear, ask which of these the user wants before you start.

## Triage

1. Confirm the contract is B2B and under Slovak law. Check the governing-law and jurisdiction clauses. Check whether the Commercial Code applies (§ 261), or whether the parties chose it in writing (§ 262). If Slovak law doesn't apply, say so and stop.
2. Read `references/mandatory-rules.md`.
3. Scan the contract for the red flags listed at the top of `references/clause-checklist.md`.
4. Give a verdict of GREEN, YELLOW, or RED, with one line per finding and its citation. RED means a clause is likely void or the contract misses something the law requires. YELLOW means a clause is risky or unclear. GREEN means you found no issue on the checklist.

## Full review

1. Do the triage steps.
2. Identify the contract type: SaaS subscription, software development (zmluva o dielo), IT services, NDA, licence agreement (licenčná zmluva), or data processing agreement.
3. Go through every section of `references/clause-checklist.md` that applies to that type.
4. For each finding, give the clause reference, the problem, the Slovak rule with its citation, the risk for the user's side, and a suggested fix.
5. List the sections you verified against the current official text, and the ones you didn't.
6. End with the three changes that matter most.

## Drafting

1. Ask for the contract type, which side the user is on, the parties, the services, the fees, and the contract language.
2. Read `references/mandatory-rules.md` and `references/clause-checklist.md`.
3. Draft clauses that comply with the mandatory rules. In particular:
   - Never draft an "assignment" or "transfer" of copyright. Slovak law doesn't allow it (Autorský zákon § 20, ods. 2). Draft a licence instead, and state the manner of use, scope, territory, duration, and fee (§ 65). Make it exclusive and in writing if the customer needs exclusivity (§ 65, ods. 3), and grant sublicensing and assignment rights expressly (§ 72).
   - Don't draft a clause where a party waives its right to damages in advance (Obchodný zákonník § 386, ods. 1). Read the practice note on liability caps before drafting a cap.
   - Don't shorten or remove the limitation period. Those sections are mandatory (§ 263, ods. 1).
   - Put the party details that § 3a requires in the contract header.
4. Mark every assumption and open question in the draft as `[TO CONFIRM: ...]`.
5. Add a note at the top that a Slovak lawyer should review the draft before use.

## Output

- Write in English unless the user asks for Slovak. Quote statute text in Slovak, then translate it.
- Cite statutes by short name and section, for example "ObZ § 386". Use the full identifiers from `references/sources.md` in a sources list at the end.
- Keep the disclaimer from the top of this skill in every review and draft.
