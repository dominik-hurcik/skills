# Clause checklist for Slovak B2B contracts

Use this list in triage and full reviews. Each item names the rule in `mandatory-rules.md` that it relies on.

## Red flags, check these first

| Red flag | Why | Rule |
| --- | --- | --- |
| A clause "assigns" or "transfers" copyright or software rights | Economic rights can't be transferred, so the clause may fail. Rewrite it as a licence. | Autorský zákon § 20, ods. 2 |
| Licence with no stated manner of use, territory, or duration | Defaults are narrow: uses needed for the purpose, Slovakia only, and at most one year | Autorský zákon §§ 66, 67, and 68 |
| Customer needs exclusivity, but the licence isn't stated as exclusive or isn't in writing | The licence is non-exclusive by default, and an exclusive licence needs writing | Autorský zákon § 65, ods. 3, and § 70 |
| Licensee must sublicense or assign, but the author's consent isn't in the contract | Not allowed without prior consent | Autorský zákon § 72 |
| A party waives damages in advance, or excludes all liability | Void | ObZ § 386, ods. 1 |
| Plain liability cap | Disputed under § 386. See the practice note. | ObZ §§ 379 and 386 |
| Clause that shortens or excludes the limitation period | The limitation sections are mandatory | ObZ §§ 263 and 397 |
| Very high contractual penalty | A court can reduce it | ObZ § 301 |
| Payment, late-interest, or collection-fee term that is grossly unfair to the creditor | Void | ObZ § 369d |
| Missing business name, seat, legal form, IČO, or register details | Required on business documents | ObZ § 3a |
| The other party is a consumer, or the Commercial Code doesn't apply | Civil Code and consumer rules apply. Out of scope. | ObZ §§ 261 and 262 |

## SaaS subscription

- **Applicable code.** Both parties are entrepreneurs acting in business, so the Commercial Code applies (§ 261), or they chose it in writing (§ 262).
- **Scope and service levels.** The contract defines the service, the availability target, how availability is measured, and the remedy when the target is missed. A service credit drafted as a contractual penalty is enforceable without fault (§ 300), but can be reduced if disproportionate (§ 301).
- **Licence to use the software.** The contract states the manner of use, the scope, the territory, and the duration (Autorský zákon §§ 65 to 68). Otherwise the narrow defaults apply.
- **Payment and late payment.** The due date is clear. If no interest rate is agreed, the statutory rate applies (§ 369, ods. 2, and Nariadenie 21/2013).
- **Customer data.** The supplier processes personal data only under a data processing agreement. Load the `dh-legal-contract-dpa` skill for that agreement.
- **Liability.** No advance waiver (§ 386). Any limit follows the practice note on liability caps.
- **Force majeure.** The clause is consistent with the statutory test in § 374, or says expressly how it differs.
- **Term and exit.** The contract covers notice periods, withdrawal for breach, and how data is returned or deleted at the end.
- **Form.** If the parties want written form for amendments, the contract says so (§ 272, ods. 2).

## Software development (zmluva o dielo) or IT services

- **Licence, not assignment.** The customer gets a licence that is exclusive, in writing, worldwide, unlimited in time, covers all manners of use, and includes modification, sublicensing, and assignment (Autorský zákon §§ 20, 65, 70, and 72). § 91, ods. 4 helps the customer, but don't rely on it alone.
- **Supplier's people.** The supplier warrants that it holds the rights from its employees (§ 90) and from any freelancers it uses.
- **Pre-existing and open-source components.** The supplier licenses its pre-existing tools separately. Open-source licences are listed, and their terms fit the customer's plans.
- **Acceptance.** The test procedure and deadlines are clear.
- **Penalties for delay.** Common in Slovakia. Keep them proportionate (§ 301).

## NDA

- **Definition.** Confidential information is defined, with the usual exceptions.
- **Protection.** The NDA supports the "suitable protection" condition for trade secrets (ObZ § 17, ods. 1).
- **Penalty.** Any fixed penalty is proportionate (§ 301).
- **Duration.** The confidentiality obligation has a fixed duration, or a clear reason why it continues.

## Licence agreement (licenčná zmluva)

- **Required content.** It covers the manner of use, scope, duration, and fee (Autorský zákon § 65, ods. 1).
- **Exclusivity.** It says whether the licence is exclusive (§ 70). An exclusive licence is in writing (§ 65, ods. 3).
- **Sublicensing and assignment.** It grants the licensee's right to sublicense and to assign, as the author's prior consent (§ 72).
- **Unknown uses.** It doesn't try to license uses that aren't known when the contract is signed (§ 66, ods. 2).

## Questions to ask the user

- Which side are you on?
- Is the other party an entrepreneur acting in business, or a consumer?
- Does the customer need exclusive rights to the software or content?
- Who writes the code: the supplier's employees, freelancers, or both?
