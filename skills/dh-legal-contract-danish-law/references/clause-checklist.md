# Clause checklist for Danish B2B contracts

Use this list in triage and full reviews. Each item names the rule in `mandatory-rules.md` that it relies on.

## Red flags, check these first

| Red flag | Why | Rule |
| --- | --- | --- |
| Either party promises not to hire or approach the other's employees | Void, unless it's tied to business-transfer negotiations | Lov om ansættelsesklausuler §§ 3 and 4 |
| Payment term over 30 days in a B2B contract, without the creditor's express acceptance | The longer term doesn't bind the creditor | Renteloven § 3 a |
| Clause excluding late interest between businesses | Void | Renteloven § 1, stk. 4 |
| Acceptance or testing period over 30 days, without the creditor's express acceptance | Not binding on the creditor | Renteloven § 3 d |
| Software or content made by a contractor with no written IP assignment, or an assignment that doesn't name the uses | The customer may get narrower rights than expected | Ophavsretsloven §§ 53, 56, and 59 |
| Clause that lengthens the limitation period in advance | Not binding on the debtor | Forældelsesloven § 26, stk. 1 |
| Clause that removes a software user's backup right or right to study the program | Void | Ophavsretsloven § 36, stk. 3 |
| Liability cap, penalty, or termination right that is extreme for the deal | A court can adjust it | Aftaleloven § 36 |
| The other party is a consumer | Consumer rules apply. Out of scope. | Aftaleloven §§ 38 a to 38 d |

## SaaS subscription

- **Scope and service levels.** The contract defines the service, the availability target, how availability is measured, and the remedy when the target is missed, such as service credits.
- **Payment.** The payment term is 30 days or less, or the supplier expressly accepted a longer term (Renteloven § 3 a). Price changes need notice and a way to leave.
- **Licence to the customer.** It states who may use the service, for what purpose, and any limits on users or volume.
- **Customer data.** The customer owns its data. The supplier processes personal data only under a data processing agreement. Load the `dh-legal-contract-dpa` skill for that agreement.
- **Liability.** A cap exists and fits the deal value, and the excluded loss types are clear. See the practice note on gross negligence before relying on the cap.
- **Term and exit.** The contract covers notice periods, termination for breach, and how data is returned or deleted at the end.
- **Governing law and disputes.** It names Danish law and a court or arbitration body.

## Software development or IT services

- **IP assignment.** If the customer should own the result, the contract assigns copyright explicitly. It covers all uses, modification, onward transfer, and sublicensing (Ophavsretsloven §§ 53 and 56). Note that § 59 doesn't cover contractors.
- **Pre-existing and open-source components.** The supplier keeps its pre-existing tools and grants a licence to them. Open-source licences are listed, and their terms are compatible with the customer's plans.
- **Acceptance.** The test period is 30 days or less, or the creditor expressly accepted a longer one (Renteloven § 3 d). The contract says what happens if the customer doesn't test.
- **Staffing.** Remove any no-hire or non-solicitation clause (Lov om ansættelsesklausuler § 3).
- **Delay and defects.** The remedies are clear. Any penalty is proportionate to the deal (Aftaleloven § 36).

## NDA

- **Definition.** Confidential information is defined, with the usual exceptions: already public, already known, independently developed, or disclosure required by law.
- **Duration.** The confidentiality obligation has a fixed duration, or a clear reason why it continues.
- **Penalty.** Any fixed penalty is proportionate (Aftaleloven § 36).
- **No hidden no-hire clause.** NDAs often include one. Remove it (Lov om ansættelsesklausuler § 3).

## IP assignment agreement

- **Uses.** It lists all uses being transferred, and says "all present and future uses" if that is the intent (Ophavsretsloven § 53, stk. 3).
- **Modification and onward transfer.** It grants the right to modify and adapt, and the right to transfer and sublicense (§ 56).
- **Moral rights.** It respects the author's right to be named and to object to derogatory treatment, which can't be fully waived (§ 3). Read § 3 in the current text before advising.
- **Payment.** It states whether the price covers the assignment.

## Questions to ask the user

- Which side are you on?
- Is the other party a business or a consumer?
- Has anyone on your side expressly accepted a payment term over 30 days?
- Who writes the code or content: your employees, the other party's employees, or contractors?
