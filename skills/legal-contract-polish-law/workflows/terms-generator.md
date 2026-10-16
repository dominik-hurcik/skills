# Workflow: terms of service generator (cold start → interview → skeleton → text)

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

> **R3, NON-LAWYER:** extra signals for terms of service: "I have to publish terms of service", "I own an online shop", "I want to launch a shop".

An interactive generator for terms of service (regulamin) for electronic services, under the Polish Act on Providing Services by Electronic Means (u.ś.u.d.e.) and the DSA. The workflow **always starts with 3 diagnostic questions** to choose the right track. Then it interviews the user one question at a time, shows a skeleton for approval, and only then generates the full text.

Ask the questions in English. The terms of service themselves are drafted in Polish, unless the user asks for another language.

## Three tracks

| Track | When | Paragraphs | Interview questions |
|---|---|---|---|
| **General** | B2B, a professional service, no shop and no SaaS | ~10 | 4 |
| **SaaS** | B2B or B2C, a platform or app, subscription, SLA | ~18 | 7 |
| **E-commerce** | B2C or mixed, a shop, goods or digital content | ~22 | 9 |

---

## STAGE 0: cold start (diagnosis: 3 questions)

**Don't ask everything at once.** Ask each question separately and wait for the answer.

### Diagnostic question 1/3

> Before we start, a few questions so I pick the right track.
>
> **Who will the main users of your terms be?**
> a) Only companies or businesses (B2B)
> b) Consumers: private individuals (B2C)
> c) Mixed: both businesses and consumers

### Diagnostic question 2/3

After the answer, ask:

> **What is the service covered by the terms mainly about?**
> a) Selling products or goods online (an online shop)
> b) Access to a platform or a web or mobile app (SaaS, marketplace, portal)
> c) Hosting, servers, domains, email
> d) Professional services, intermediation, or online advice
> e) Other (describe)

### Diagnostic question 3/3

After the answer, ask:

> **What's the payment model?**
> a) Subscription (monthly or yearly)
> b) One-off purchase or a fee per transaction
> c) Commission or success fee
> d) Free or freemium

### Choosing the track

After the 3 answers, announce the track:

```
Based on your answers, I'm choosing the [NAME] track,
because [one sentence of reasoning].

Next I'll ask you [N] detailed questions. Shall we go?
```

**Selection rules:**
- B2C + shop, goods, or digital content → **E-commerce**
- B2C + platform or app → **E-commerce** (the Consumer Rights Act, u.p.k., applies to platforms)
- Mixed + shop → **E-commerce** (the consumer is the weaker party, so apply the higher standard)
- Mixed + platform or app (not a shop) → **SaaS** ⚠️ The platform has consumer users. Add a right-of-withdrawal paragraph to SaaS (art. 27 u.p.k., for contracts concluded online) and an ODR section in the final provisions.
- B2B + shop or sale of goods → **E-commerce** ⚠️ Skip § 10 Right of withdrawal and § 11 Exceptions. They don't apply in B2B. Keep the Civil Code warranty for defects (art. 556 et seq. KC) without consumer clauses.
- B2B + platform, SaaS, hosting, or domains → **SaaS**
- B2B + professional services, intermediation, or other → **General**
- B2C + hosting, domains, or email → **SaaS** ⚠️ Add a right-of-withdrawal paragraph (art. 27 u.p.k.) and an ODR section in the final provisions. A consumer buying hosting has the full protection of u.p.k.
- Mixed + hosting or domains → **SaaS** ⚠️ As above.
- In doubt → ask directly instead of guessing.

**STOP. Wait for confirmation ("go", "yes", or a correction to the track).**

---

## STAGE 1A: interview, General track (4 questions)

Ask one at a time and wait for each answer.

**Q1.** The full name of your company or business, and its registered seat?

**Q2.** What's the service or website covered by the terms called? What is it about? Describe it in one sentence.

**Q3.** What are the user's main obligations and prohibitions? (for example no spamming, no reselling, no fake accounts)

**Q4.** How do you handle payments? When does the user pay, and how? Subscription, one-off, or a free service?

After the last answer → **STAGE 2A**.

---

## STAGE 1B: interview, SaaS track (7 questions)

Ask one at a time and wait for each answer.

**Q1.** The full company name, and the name of the platform or app?

**Q2.** What subscription model? Which plans are available, by name, and what do they include? Is there a free trial?

**Q3.** Do you offer an SLA, a guaranteed availability (uptime)? If so, what percentage, and what happens if it's missed?

**Q4.** The acceptable use policy (AUP): what are users not allowed to do on the platform? (typically spam, scraping, illegal content, API abuse)

**Q5.** Do you process users' personal data: account data, logs, or customer data that users upload? Do you need a data processing agreement (DPA, art. 28 RODO)?

**Q6.** Does the platform include AI features, generative or analytical? If so, describe them briefly.

**Q7.** Can users upload content to the platform (UGC: posts, files, images, data)? Is the platform moderated?

After the last answer → **STAGE 2B**.

---

## STAGE 1C: interview, E-commerce track (9 questions)

Ask one at a time and wait for each answer.

**Q1.** The full name of the shop or website, and the seller's registered seat?

**Q2.** What do you sell: physical products, digital content (files, online access), services, or a mix?

**Q3.** Which payment methods do you accept? (card, BLIK, bank transfer, PayPal, other)

**Q4.** Which delivery methods, and roughly how long does fulfilment take? (courier, parcel locker, email for digital content)

**Q5.** Returns policy: do you apply the statutory 14 days to withdraw (art. 27 u.p.k.), or offer a longer period?

**Q6.** Do you sell digital content not supplied on a physical medium, such as PDF files, online courses, or app access? (This affects art. 38 pkt 13 u.p.k.: the right of withdrawal ends once the service is performed with the consumer's consent.)

**Q7.** Do any of your products fall under exceptions to the right of withdrawal, such as sealed recordings, perishable goods, or goods made to the consumer's specification?

**Q8.** Do you take orders from EU countries outside Poland? (This affects VAT OSS and cross-border rules.)

**Q9.** Preferred complaints channel: email, a form, or something else? Which response deadline do you want to state?

> ⚠️ **Checking Q9:** in B2C, the stated deadline for answering a complaint shouldn't exceed 14 calendar days. A longer deadline means the complaint is deemed accepted by law (art. 7a u.p.k.); for claims about goods not conforming to the contract, see art. 43d ust. 1 u.p.k. If the user gives a deadline longer than 14 days, explain the risk and propose 14 days. Convert working days or weeks to calendar days before comparing (a week = 7 calendar days; 1 working day ≈ 1.4 calendar days).

After the last answer → **STAGE 2C**.

---

## STAGE 2A: skeleton, General track

**Open:** `references/clause-bank/20-regulamin-usdde-aup.md`, `references/clause-bank/INDEX.md`

Show the proposed structure (write the paragraph titles in the language of the terms):

```
TERMS SKELETON: General track (~10 §)

§ 1.  Definitions: key terms, the parties' names
§ 2.  General provisions: nature of the terms, acceptance, technical requirements
§ 3.  Scope of the service: what it includes and what it doesn't
§ 4.  User obligations and prohibitions: the list from Q3
§ 5.  Fees and payments: [model from Q4]
§ 6.  Provider's liability: cap, exclusions
§ 7.  Complaints: procedure (form, details, deadline)
§ 8.  Termination and account suspension
§ 9.  Personal data protection: art. 13 RODO, legal basis for processing
§ 10. Final provisions: governing law, court, changes to the terms
```

**STOP. Ask:** "Do you accept this structure? Anything to add or remove?"

---

## STAGE 2B: skeleton, SaaS track

**Open:** `references/clause-bank/20-regulamin-usdde-aup.md`, `references/knowledge-base/13-regulamin-usdde-hosting-ai.md`, `references/clause-bank/INDEX.md`

Show the proposed structure. Include paragraphs marked [if...] only when they apply:

```
TERMS SKELETON: SaaS track (~18 §)

§ 1.  Definitions: Platform, Subscription Plan, SLA, AUP, Account, User
§ 2.  Conclusion of the contract: moment of registration, activation email, age or legal status
§ 3.  Scope of the service: description of the Platform, modules, production vs test environment
§ 4.  Subscription plans: [names from Q2], scope, upgrades and downgrades
§ 5.  AUP: prohibited uses [list from Q4]
§ 6.  User account: password, security, responsibility for the account
§ 7.  Fees and payments: prepaid, VAT invoices, consequences of non-payment
§ 8.  SLA: availability [% from Q3], response times, Critical / Significant / Cosmetic defects [if Q3 answered]
§ 9.  Personal data and processing: art. 13 RODO + DPA under art. 28 [if Q5 = yes]
§ 10. Intellectual property: the platform belongs to the provider; user data belongs to the user
§ 11. User content (UGC): licence, moderation, notice and action [if Q7 = yes]
§ 12. AI modules: scope, exclusions of liability for output [if Q6 = yes]
§ 13. Liability: cap (the last 12 months of subscription fees), exclusion of indirect damage
§ 14. Suspension and deletion of the account: grounds, wind-down, data export
§ 15. Termination: by either party, notice periods
§ 16. Changes to the terms: procedure, advance notice, non-acceptance
§ 17. Complaints: procedure, [___] working days
§ 18. Final provisions: Polish law, court, severability clause
```

**STOP. Ask:** "Do you accept this structure? Which §§ marked [if...] apply to your platform? Anything to add or remove?"

---

## STAGE 2C: skeleton, E-commerce track

**Open:** `references/clause-bank/20-regulamin-usdde-aup.md`, `references/clause-bank/INDEX.md`

Show the proposed structure. Include paragraphs marked [if...] only when they apply:

```
TERMS SKELETON: E-commerce track (~22 §)

§ 1.  Seller details: art. 8 ust. 3 u.ś.u.d.e.: business name, address, NIP, email, phone
§ 2.  Definitions: Shop, Goods, Digital Content, Consumer, Account, Order
§ 3.  Rules for using the Shop: technical requirements, prohibitions
§ 4.  Registration and Account [if the shop has accounts]
§ 5.  Placing Orders: procedure, the moment the sale contract is concluded
§ 6.  Prices and Payments: methods [from Q3], currency, due date
§ 7.  Delivery: methods [from Q4], costs, timing, risk of loss of goods
§ 8.  Fulfilment: confirmation, cancellation, goods unavailable
§ 9.  Digital Content: supply, moment of performance, the consumer's consent to immediate performance [if Q2/Q6]
§ 10. Right of Withdrawal: 14 days (art. 27 u.p.k.), form, refund
§ 11. Exceptions to the Right of Withdrawal: [list from Q7 + art. 38 u.p.k.] [if applicable]
§ 12. Warranty for defects: liability for non-conforming goods (art. 43a-43g u.p.k. for B2C; art. 556 et seq. KC for B2B)
§ 13. Complaints: procedure [from Q9], deadline, what a complaint must contain
§ 14. Guarantee: who gives it, duration, scope [if applicable]
§ 15. Ratings and Reviews [if the shop has a review system]
§ 16. Personal Data Protection: art. 13 RODO, purpose and basis of processing
§ 17. Cookies and tracking
§ 18. Liability: the seller's limits (not applicable to a consumer's warranty claims)
§ 19. Cross-border orders, VAT, governing law for EU consumers [if Q8 = yes]
§ 20. Out-of-court Dispute Resolution: ODR (https://commission.europa.eu/consumers/odr), UOKiK
§ 21. Changes to the Terms: procedure, effect on orders placed before the change
§ 22. Final Provisions: Polish law, court, severability clause
```

**STOP. Ask:** "Do you accept this structure? Which §§ marked [if...] apply to your shop? Anything to add or remove?"

---

## STAGE 3: generate the terms

**Open:** `references/drafting-style.md`, `references/clause-bank/20-regulamin-usdde-aup.md`, and the other files from `references/clause-bank/` that `INDEX.md` points to

Using the approved skeleton, generate the terms paragraph by paragraph.

### Writing rules

1. **Clauses from the KTZR bank.** The main source is `20-regulamin-usdde-aup.md`. Add from other files via `INDEX.md`. Don't invent clauses outside the bank.

2. **Fit the interview.** The provider's and service's actual names, not placeholders. The actual plans, deadlines, and payment methods from the answers. Leave `[___]` fields **only where the user didn't give the data**.

3. **KTZR style**, per `drafting-style.md`. Capitalised defined terms. Numbered sections. Cross-references as „§ X ust. Y". Formal legal language, not marketing.

4. **The art. 8 u.ś.u.d.e. minimum.** Every set of terms must include:
   - the provider's details (business name, address, NIP, email, phone)
   - the types and scope of electronic services
   - the conditions of providing them (technical requirements)
   - the conditions for concluding and terminating the contract
   - the complaints procedure

5. **E-commerce track, consumers.** Every clause about the consumer must comply with the Act of 30 May 2014 on consumer rights. Clauses that limit consumer rights are ineffective by law, so don't include them.

### Output format

```
REGULAMIN [NAZWA USŁUGI / SKLEPU]
Obowiązuje od: [date; leave blank if not given]
Wersja: 1.0

§ 1. [TITLE]

1. [Text of the first section]
2. [Text of the second section]

§ 2. [TITLE]

1. [Text]
[...]

---
Kontakt: [details from the interview]
```

After generating everything → **STAGE 4 (QA)**.

**STOP. Ask:** "Do you want me to run the QA on the terms now?"

---

## STAGE 4: verification (QA)

Check the terms for:

1. **The u.ś.u.d.e. minimum:** is art. 8 ust. 3 pkt 1-4 met: (a) the provider's details (business name, address, NIP, email, phone); (b) technical requirements; (c) a ban on supplying unlawful content; (d) conditions for concluding and terminating the contract; (e) the complaints procedure
2. **Definitions:** every capitalised term is defined in § Definitions
3. **Cross-references:** every „§ X ust. Y" leads to an existing provision
4. **`[___]` fields:** no unintended blanks left
5. **Consumers (E-commerce, and SaaS with B2C):** no clauses contrary to u.p.k. or art. 385¹ KC
6. **Terminology:** one name for each party throughout
7. **Withdrawal form (E-commerce B2C):** the right-of-withdrawal paragraph includes the model form, or refers to the form in Annex 2 to u.p.k. (art. 30 u.p.k.)
8. **Information duties (E-commerce and SaaS B2C):** the terms, or a named place on the website, cover the art. 12 u.p.k. minimum (seller details, total price, duration, right of withdrawal, interoperability of digital content)
9. **B2C complaints (SaaS with B2C, E-commerce):** the deadline in § Complaints must be in **calendar** days, not working days. Art. 7a u.p.k. caps it at 14 calendar days (a longer deadline means the complaint is deemed accepted). Convert: 1 week = 7 calendar days; 1 working day ≠ 1 calendar day.

Before the final version, the gate. Show these questions and **wait for an answer**:

```
⛔ Before the final terms, please confirm:
1. Have the entity's details (name, NIP, address, KRS) been checked against the source?
2. Have the quoted provisions been checked (verify_article or manually)?
3. Is the platform or shop B2C, or B2B only? (changes the scope of u.p.k. duties)
4. Has a lawyer seen the draft?
→ "yes, generate" / or say what to fix
```

Generate only after confirmation. Without confirmation, put `[DRAFT, FOR REVIEW]` above the terms.

Exception: "express mode" or "do it without asking" → generate with `[DRAFT, FOR REVIEW]` at the start and end.

Return the QA as a ✅ / ⚠️ / ❌ list, then the final terms:

```
## TERMS VERIFICATION

✅ The art. 8 u.ś.u.d.e. minimum is met (§ 1, § 7, § 17)
⚠️ [any warning]
❌ [any error: describe what was fixed]

---

## FINAL TERMS

[clean text, with no comments inside it]
```

---

## Iteration: REDRAFT

If the user wants to change a passage after generation:

1. Identify the paragraph and the change.
2. Take the right clause from the bank (if needed).
3. Apply the change, and check it didn't break cross-references, definitions, or numbering.
4. Return **the WHOLE terms again**, not just the changed passage.
