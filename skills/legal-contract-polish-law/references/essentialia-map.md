# Essentialia negotii: mapping contract types

Before any work on a contract, **always map the essentialia first**. Don't generate a single paragraph until they're mapped.

## Five elements every contract needs

1. **CONTRACT TYPE:** which legal relationship does it govern? (B2B, NDA, implementation, transfer of rights, lease, supply, and so on)
2. **PARTIES:** who with whom (full names, legal forms, roles such as Zleceniodawca/Wykonawca or Zamawiający/Dostawca)
3. **SUBJECT:** what exactly the contract covers (a service, a licence, a transfer of rights, a work, goods)
4. **REMUNERATION:** how much, how, when (amount or rate, model, due date, currency, invoice)
5. **TERM:** for how long (fixed or indefinite term, dates, notice periods)

---

## Mapping by type: what must be there

### IT body leasing (B2B)

**Legal type:** a contract for services (art. 750 KC with art. 734 et seq.) between businesses.

**Critical elements:**
- **Express exclusion of an employment relationship** (art. 22 § 1 KP): „Umowa nie kreuje stosunku pracy" (the contract doesn't create employment).
- **The Specialist (Specjalista) as an independent business** (B2B) or a person on a civil-law contract.
- **The Specialist's autonomy** in choosing methods and tools (key to defending against reclassification as employment).
- **Billing model:** T&M based on a timesheet that gets approved (with deemed acceptance after, for example, 5 working days).
- **NDA for Specialists:** a duty to sign separate NDAs before starting.
- **Transfer of copyright:** in the Works created as part of the Services, with the timing and the fields of exploitation.

**Term:** usually indefinite, with 1 to 3 months' notice. A framework agreement plus orders.

---

### NDA (non-disclosure agreement)

**Legal type:** an innominate contract (freedom of contract, art. 353¹ KC), usually one-way or mutual.

**Critical elements:**
- **Definition of Confidential Information:** broad, with confidentiality presumed in case of doubt.
- **Purpose of disclosure:** stated expressly (a project, negotiations, cooperation).
- **Duration:** during and after (typically 3 to 10 years; trade secrets indefinitely).
- **Exceptions:** information that is public, known earlier, independently developed, or disclosed at an authority's request.
- **Breach procedure:** notification within 24 to 72 hours, cooperation in limiting the effects.
- **Contractual penalty:** a specific amount per breach, plus additional compensation.
- **Reservation:** signing the NDA doesn't oblige anyone to sign the main contract.

**Term:** a set period from signing, plus a period after the end.

---

### IT implementation contract (fixed price)

**Legal type:** a contract for a specific work (umowa o dzieło, art. 627 KC) with service elements, or a mixed contract.

**Critical elements:**
- **Specification** as an annex (ideally a detailed SOW).
- **Milestones** with acceptance protocols (partial and final).
- **Acceptance procedure:** deadlines for reporting defects, and a classification of defects (critical, significant, cosmetic).
- **Warranty:** period, scope, exclusions (configuration changes, environment changes).
- **Transfer of copyright:** with the moment of transfer (usually after payment).
- **Anti-copyleft clause:** the contractor guarantees there are no GPL or AGPL components.
- **Repository handover:** the procedure for handing over source code and documentation.

**Term:** fixed by an end date, or by reaching the last milestone.

---

### SaaS or software licence

**Legal type:** a licence agreement (art. 41 et seq. PrAut) plus a contract for services (maintenance).

**Critical elements:**
- **Fields of exploitation** for the licence, listed expressly.
- **Nature of the licence:** non-exclusive or exclusive, territorial or worldwide, sublicensable or not.
- **SLA:** availability (uptime %), response times, repair times.
- **Maintenance and support:** what's included and what's paid extra.
- **Customer data:** ownership, where it's processed, GDPR, export at the end.
- **Termination and exit:** notice period, data migration procedure.

---

### Accounting services contract

**Legal type:** a contract for services (art. 750 KC), regulated by the Accounting Act.

**Critical elements:**
- **The provider's qualifications:** entry on the register or a certificate, and valid liability insurance (OC).
- **Scope of services:** full or simplified accounting, HR, payroll, tax advice (separately).
- **The client's obligations:** delivering documents on time and complete.
- **Liability for damage:** with a reference to the liability insurance policy.
- **Professional secrecy:** a reference to art. 4a of the Tax Advisory Act or the Accounting Act.

---

### Copyright transfer agreement

**Legal type:** a dispositive contract (art. 41 et seq. PrAut).

**Critical elements:**
- **Fields of exploitation:** listed expressly (art. 41 ust. 2 PrAut: a field not listed isn't transferred).
- **Remuneration:** stated expressly (a free transfer needs a clear statement).
- **Moment of transfer:** stated expressly (signing, payment, or acceptance).
- **Derivative rights:** whether the acquirer may adapt, modify, and create derivative works.
- **Moral rights:** the author's undertaking not to exercise them (they can't be transferred, only not exercised).
- **Clean-IP warranties:** the transferor guarantees it holds the full rights exclusively.
- **Anti-copyleft clause:** for software.

---

### Settlement (ugoda)

**Legal type:** a settlement (art. 917 KC).

**Critical elements:**
- **The disputed situation:** a description of what it covers, with specifics (invoice numbers, dates, amounts).
- **Mutual concessions:** expressly on both sides (without them it isn't a settlement).
- **Waiver of claims:** to what extent, and of what.
- **Deadline and manner of performing** the settlement's obligations.
- **A settlement-specific fallback clause:** what happens if a party doesn't perform.

---

### Assignment of receivables (cesja)

**Legal type:** assignment of a receivable (art. 509 et seq. KC).

**Critical elements:**
- **The receivable, precisely identified:** legal basis, debtor, amount, due date.
- **Price for the assignment**, or none (a free assignment).
- **The assignor's statement about the receivable:** it exists, is unencumbered, and isn't subject to a ban on assignment.
- **Notifying the debtor:** who, when, in what form (after notification, the debtor can't pay the assignor).
- **The assignor's liability:** for the receivable existing (always), and for the debtor's solvency (only if expressly agreed, art. 516 KC).

---

## After mapping the essentialia

Show the user the mapping in a clear format:

```
ESSENTIALIA NEGOTII
- Type: [...]
- Parties: [...]
- Subject: [...]
- Remuneration: [...]
- Term: [...]

CRITICAL ELEMENTS FOR THIS CONTRACT TYPE:
- [...]
- [...]
```

Then **ask the user to confirm or correct it** before you continue.
