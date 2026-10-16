# Workflow: practice setup

A one-time interview that generates `practice-profile.md`: a permanent configuration of the practice that every workflow reads. Run by the administrator (the partner or owner of the practice, or an assistant they authorise).

**When to run it:**
- When first deploying the skill in a practice
- After a change in the practice's profile, specialisation, or standards
- When several people in an organisation use the skill and need a consistent configuration

**Time:** 15 to 20 minutes. Answer specifically. The more precise the answers, the better the skill fits your practice.

**Output:** a finished `practice-profile.md` to save in the skill's root folder. The repo's `.gitignore` excludes this file, so it never reaches a public repository.

---

## How to run the interview

- Ask one section at a time. Wait for the answers after each section, then continue.
- Don't ask for client data, case numbers, or any personal data.
- If the administrator answers "standard" or "typical", use market defaults for a Polish B2B IT practice.
- Use the answers to build `practice-profile.md`. Don't keep them in session memory.

---

## SECTION 1/5: practice profile

**Questions:**

1. **Main contract types:** which contract types make up over 80% of the practice's work? (for example IT body leasing, NDA, SaaS, ERP implementations, transfer of copyright, settlements, B2B employment-style contracts)

2. **Representation:** whom does the practice represent most often?
   - The client or buyer of services (Zamawiający)
   - The contractor or supplier (Wykonawca)
   - Both (depends on the matter)

3. **Market:** the practice's client profile:
   - B2B, B2C, or mixed
   - Domestic or international (if international, which jurisdictions?)
   - Client size: SMEs, corporations, startups, or mixed

4. **Industries:** beyond IT, any other industries? (for example fintech, medtech, e-commerce, real estate)

**STOP and wait for the answers to Section 1.**

---

## SECTION 2/5: risk thresholds

**Questions:**

1. **The practice's style:** how would you describe its approach to risk?
   - **Conservative:** always starts from maximum protection and negotiates every departure from the standard
   - **Moderate:** the standard B2B market; negotiates risks above a threshold
   - **Aggressive:** focused on closing the deal; accepts higher risks when the client decides knowingly

2. **Absolute RED:** what always blocks a contract without negotiation? Examples (tick and add your own):
   - [ ] No liability cap, or a cap below X months of fees
   - [ ] An attempt to exclude intentional fault (art. 473 § 2 KC)
   - [ ] No fields of exploitation in a transfer of copyright
   - [ ] Foreign jurisdiction with no reason
   - [ ] Other: ___

3. **Full analysis vs triage threshold:** above what contract value do you always do a full analysis (not triage)?

**STOP and wait for the answers to Section 2.**

---

## SECTION 3/5: default negotiating positions

**Questions:**

1. **Liability cap:** which cap does the practice recommend as the starting point in negotiations?
   - For example "12 months of net fees", "the contract value", or "depends on the contract value"

2. **Confidentiality:** the practice's standard confidentiality period after the contract ends?
   - For example "3 years for ordinary information, indefinitely for trade secrets"

3. **GDPR:** the practice's default position:
   - We represent the controller (the party entrusting processing)
   - We represent the processor (the party receiving the data)
   - Both

4. **Dispute resolution:** preferred forum?
   - Common courts (at which party's seat?)
   - Arbitration (which arbitration court?)
   - Depends on the value and the parties

5. **Contractual penalties:** does the practice propose penalties in every contract as standard, or only when the client asks?

**STOP and wait for the answers to Section 3.**

---

## SECTION 4/5: style and format

**Questions:**

1. **Legal design:** which output format do you prefer?
   - **Classic:** a traditional legal format, without tables and boxes (Times New Roman)
   - **Light legal design:** Arial, key-terms tables, subtle emphasis (the KTZR standard)

2. **How formal the skill's answers should be:** how should the skill address you?
   - Formal, impersonal
   - Semi-formal
   - Operational: directly, like a fellow lawyer

3. **Working language** for the skill's answers:
   - English (the default in this repo)
   - Polish
   - Both
   Contract text is drafted in the contract's own language whatever you choose here.

4. **Format of analysis reports:** what must always be in a report, and what don't you want?

**STOP and wait for the answers to Section 4.**

---

## SECTION 5/5: exclusions

**Questions:**

1. **Matter types the practice does NOT handle:** for example employment law, litigation, criminal matters, pre-seed startups

2. **Client types the practice does NOT serve:** for example consumers, foreign clients without a Polish structure, regulated industries (banks, insurers)

3. **Anything else** the skill should know about the practice that we didn't ask?

**STOP and wait for the answers to Section 5.**

---

## Generating practice-profile.md

After collecting the answers to all 5 sections, generate the file in the format below. Fill in values from the answers. For a missing answer, use the default given in the brackets.

When generating, replace `[TODAY]` with today's date as DD.MM.YYYY, `[list from answers]` with the specific list from the answers, and `[answer]` with the chosen option or the user's text.

```markdown
# practice-profile.md
# Practice configuration: private file (excluded by .gitignore)
# Generated by: workflows/practice-setup.md
# Date: [TODAY]

## Practice profile

Main contract types: [list from answers / default: IT body leasing, NDA, SaaS, implementations]
Representation: [Client / Contractor / Both]
Market: [domestic B2B / international B2B / mixed]
Client size: [SMEs / corporations / mixed]
Industries: [list]

## Risk thresholds

Style: [Conservative / Moderate / Aggressive / default: Moderate]
Full analysis threshold: [amount in PLN / default: PLN 100,000 a year]

Absolute RED (always block without negotiation):
- [list from answers]
- [default: no cap, exclusion of intentional fault, no fields of exploitation for IP]

## Default negotiating positions

Liability cap (starting point): [answer / default: 12 months of net fees]
Confidentiality period after the end: [answer / default: 3 years for ordinary information, indefinitely for trade secrets]
GDPR position: [Controller / Processor / Both]
Dispute forum: [answer / default: the court for our client's registered seat]
Contractual penalties: [as standard / at the client's request]

## Style and format

Legal design: [Classic / Light legal design / default: Light legal design]
Formality: [Formal / Semi-formal / Operational / default: Operational]
Working language: [EN / PL / both / default: EN]
Report format: [notes from answers]

## Exclusions

Matter types outside the profile: [list from answers]
Client types outside the profile: [list from answers]
Additional notes: [answer to Section 5, question 3]
```

---

## After generating: instructions for the administrator

```
1. Save the generated block above as practice-profile.md
   (in the skill's root folder, next to SKILL.md).

2. The repo's .gitignore excludes this file, so it never reaches a public repository.

3. From now on, every workflow reads practice-profile.md at the start of the session
   and adapts to your practice's profile.

4. To update the profile, run this workflow again, or edit practice-profile.md by hand.
```
