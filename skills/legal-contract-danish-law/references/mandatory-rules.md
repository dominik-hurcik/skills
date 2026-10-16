# Danish rules that shape B2B contracts

Each rule below was read in the official text on 16 October 2026. See `sources.md` for the versions. Statute quotes are in Danish, followed by an English summary. Items marked "practice note" are not statute text and were not verified.

## Contract formation and unfair terms (Aftaleloven)

- **§ 1.** Offers and acceptances bind the party that makes them. "Tilbud og svar på tilbud er bindende for afgiveren."
- **§ 6, stk. 1.** An acceptance that adds to, limits, or qualifies the offer counts as a rejection plus a new offer. This matters when both sides attach their own terms.
- **§ 33.** A party can't rely on a declaration if doing so would be against "almindelig hæderlighed" (ordinary honesty), given what it knew when it received the declaration.
- **§ 36, stk. 1.** "En aftale kan ændres eller tilsidesættes helt eller delvis, hvis det vil være urimeligt eller i strid med redelig handlemåde at gøre den gældende." A court can amend or set aside a term that would be unreasonable to enforce. This applies between businesses too, not only to consumers.
- **§ 36, stk. 2.** The court weighs the circumstances at signing, the content of the contract, and later events.
- **§§ 38 a to 38 d.** Extra protection when the other party is a consumer. Unclear non-negotiated terms are read in the consumer's favour (§ 38 b). Out of scope for this skill, but flag them if a consumer is involved.

Use in reviews. A one-sided liability cap, penalty, or termination right isn't void by itself in a B2B contract, but a court can adjust it under § 36. Flag terms that are extreme for the deal.

## No-hire and non-solicitation clauses (Lov om ansættelsesklausuler)

- **§ 1, stk. 2, nr. 4.** A "jobklausul" is an agreement that an employer makes with other businesses to prevent or limit an employee's chances of getting a job at another business.
- **§ 3.** "En arbejdsgiver kan ikke gyldigt indgå aftaler om jobklausuler." An employer can't validly agree to a job clause.
- **§ 4.** The only exception is during negotiations about a business transfer. The clause can last at most 6 months, and it can't cover employees who have worked at the transferring business for 3 months or less.

Use in reviews. A clause in a SaaS, consulting, or outsourcing contract where either party promises not to hire, or not to approach, the other party's employees is void under Danish law, unless § 4 applies. Mark it RED and recommend deleting it. Don't redraft it into a softer no-hire version, because that is still a job clause.

The same act limits non-compete and customer clauses between an employer and its own employee (§§ 5 to 11). Those clauses need written information, a minimum of 6 months' employment, compensation, and a maximum length of 12 months. They belong in employment contracts, which this skill doesn't cover.

## Payment terms and late interest (Renteloven)

- **§ 3, stk. 1.** Interest runs from the due date if the contract fixes one.
- **§ 3 a.** Between businesses, the agreed payment term can't be longer than 30 days from the payment request, unless the creditor expressly accepted a longer term and the longer term isn't unreasonable to the creditor.
- **§ 3 d.** An acceptance or inspection procedure can't take longer than 30 days after delivery, unless the creditor expressly accepted a longer procedure and it isn't unreasonable to the creditor.
- **§ 5, stk. 1.** Late interest is the reference rate plus 8 percentage points a year. The reference rate is Nationalbanken's official lending rate on 1 January and 1 July.
- **§ 1, stk. 4.** Between businesses, the creditor's right to late interest from the due date can't be excluded by contract.
- **§ 9 a, stk. 3.** Between businesses, the creditor can claim a fixed compensation amount for collection costs. A contract can't exclude this right.

Use in reviews. If you're the supplier, a customer's 60-day or 90-day payment term only binds you if you expressly accepted it. If you're the customer, don't rely on a term longer than 30 days unless the supplier expressly accepted it. A clause excluding late interest between businesses is void.

## Limitation periods (Forældelsesloven)

- **§ 3, stk. 1.** The general limitation period is 3 years.
- **§ 2, stk. 3.** For a claim from breach of contract, the period starts at the time of the breach.
- **§ 3, stk. 2.** If the creditor didn't know about the claim or the debtor, the period starts when the creditor knew or should have known.
- **§ 3, stk. 3, nr. 4.** In any case, most claims expire 10 years after the start date.
- **§ 26, stk. 1.** "Loven kan ikke ved forudgående aftale fraviges til skade for skyldneren." An advance agreement can't change the rules to the debtor's detriment. So a B2B contract can't lengthen the periods in advance. A shorter period, which hurts the creditor, isn't blocked by § 26, stk. 1, but a court can still review it under Aftaleloven § 36.

The register lists amendments to this act from 2018 and 2023 that were not read here. Fetch the current text before relying on these sections.

## Copyright and software (Ophavsretsloven)

- **§ 53, stk. 1.** The author can transfer the rights wholly or partly, subject to the moral rights in § 3.
- **§ 53, stk. 3.** If the author transferred the right to use the work in a certain way, the transfer doesn't cover other ways. Courts read transfers narrowly.
- **§ 53, stk. 4.** The default rules in §§ 54 to 59 can be changed by contract, unless a section says otherwise.
- **§ 56, stk. 1.** A transfer doesn't let the acquirer change the work, unless the change is customary or obviously assumed.
- **§ 56, stk. 2.** A transfer doesn't let the acquirer transfer the rights onward, unless that is customary or obviously assumed.
- **§ 59.** "Ophavsretten til et edb-program, der er frembragt af en arbejdstager under udførelsen af dennes arbejde eller efter arbejdsgiverens anvisninger, overgår til arbejdsgiveren." Copyright in software made by an employee in the course of work passes to the employer. This rule covers employees only, not contractors or agencies.
- **§ 36, stk. 1 and stk. 3.** A lawful user of a program may make copies and changes needed to use it, including fixing errors, make a backup copy, and study the program while running it. A contract can't remove the backup right or the right to study the program.

Use in drafting. When you buy software development from a contractor, write an explicit assignment that covers all present and future uses, the right to modify and adapt, and the right to transfer and sublicense. Without it, §§ 53 and 56 leave rights with the contractor.

## Practice notes, not verified

Confirm these with a Danish lawyer before relying on them:

- Danish courts generally don't let a party rely on a limitation of liability for damage it caused by gross negligence or intent.
- Danish contract law doesn't require written form for most B2B contracts. Electronic signatures, including MitID, are commonly used.
- Danish law has no general rule that the other side must give "consideration" for a promise to bind.
