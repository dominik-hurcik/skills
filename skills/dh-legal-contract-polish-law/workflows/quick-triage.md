# Workflow: quick triage (GREEN / YELLOW / RED)

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

**Purpose:** a fast classification of a contract, NDA, or annex in 5 to 10 minutes, to help decide *"sign", "send for analysis", or "reject without negotiating"*. Complements `full-review.md`, which is deeper and takes longer.

**Inspiration:** the Anthropic Contract Review skill (`anthropics/claude-for-legal`), adapted to Polish B2B IT.

**Triggers:** *"can I sign this"*, *"a quick look"*, *"triage"*, *"how bad is it"*, *"look at it in 5 minutes"*, *"an NDA to sign"*, *"a simple contract, can you assess it?"*.

**Caveat:** triage is a **first filter**, not a full analysis. Send every YELLOW or RED contract for a full analysis (`full-review.md`) before signing. GREEN means no red flags in the usual areas. It does *not* mean the contract is *perfect*.

## Three categories

### 🟢 GREEN: standard, can be signed as is

The contract matches KTZR patterns or the typical B2B IT market. No red flags in the usual areas. It can be signed after sending the client a short note: *"OK, you can sign."*

**Criteria (all must be met):**

- The parties are clearly identified (KRS, NIP, representation).
- The subject is specific and within the client's line of business.
- A liability cap exists and is in the usual range (usually 12 months of fees × 1 to 3).
- Intentional fault and gross negligence aren't excluded (consistent with art. 473 § 2 KC).
- Payment terms are standard (30 or 45 days from the invoice).
- A dispute resolution method exists (Polish courts, or agreed arbitration).
- Confidentiality clauses are proportionate (duration and scope).
- For an IT contract, the fields of exploitation are listed and fit the subject (art. 41 ust. 2 PrAut).

### 🟡 YELLOW: needs analysis before signing

The contract has clauses that depart from typical KTZR or market patterns. It isn't obviously "bad", but it needs a deliberate decision by the client, and possibly negotiation.

**YELLOW signals (any one of these):**

- An **unusual** liability cap (for example only 50% of annual fees, which is low; or 5× annual fees, which is high but acceptable in some industries).
- **Broad liability exclusions** (*„za szkody pośrednie, lucrum cessans"*: for indirect damage and lost profits). Check the context; usually acceptable in commercial contracts.
- A **non-compete** or **non-solicitation** clause. Check the compensation, duration, and scope. In Poland these are hard to enforce without compensation; applying art. 101¹ KP by analogy to B2B is disputed.
- A **transfer of copyright** *„do wszystkich utworów powstałych w toku współpracy"* (to all works created during the cooperation) without listing the fields of exploitation. Without specifics the clause is ineffective (art. 41 ust. 2 PrAut), but the client may not know this.
- A **foreign dispute forum** (for example a foreign court, or arbitration in another jurisdiction). Needs the client's agreement.
- An **audit clause** or a *right of inspection* for the other side. Check the scope.
- **GDPR (RODO):** no data processing agreement, although the contract involves processing personal data (art. 28 RODO). A signal to add one.
- Remuneration **dependent on external factors** (KPIs, the client's financial results, a success fee). The metrics need defining.
- **Contract change** clauses (for example *„Zamawiający może jednostronnie zmienić zakres Usług"*: the client may change the scope unilaterally). A typical imbalance, worth negotiating.

### 🔴 RED: don't sign without serious negotiation

The contract has blocking clauses, or clauses that create significant risk. It shouldn't be signed without negotiation.

**RED signals (any one of these):**

- **No liability cap**, or a grossly low cap (for example *„do kwoty 1 PLN"*). A party with no protection against the consequences.
- **Exclusion of liability for intentional fault:** void under art. 473 § 2 KC, but it shows the other side drafted aggressively.
- A **one-sided indemnity** (*„Wykonawca zwolni Zamawiającego z wszelkich roszczeń osób trzecich"*: the contractor indemnifies against all third-party claims) with no reciprocity and no amount or time limits.
- **Assignment of the contract** without one party's consent (usually without the contractor's consent, which is bad for our client).
- An **MFN (most-favoured nation)** clause, or a lowest-price clause. It obliges giving the other side the best terms on the market, and is often impossible to enforce in practice.
- A **non-compete** without compensation and with a broad time and territory (for example *„5 lat, na terenie EU, w branży IT"*: 5 years, the EU, the IT sector).
- A **full transfer of copyright** *„do wszystkich utworów, które kiedykolwiek powstaną"* (to all works ever created) in an open-ended contract. Needs specifics.
- **No termination clause**, or termination for one side only.
- A **dispute forum that excludes Polish law** with no business reason.
- **GDPR (RODO):** the other side demands access to personal data of our client's employees with no legal basis.
- **Contractual penalties** grossly high relative to the contract value (for example *„kara umowna 500% wynagrodzenia za każde naruszenie"*: 500% of fees per breach). A court can reduce it under art. 484 § 2 KC, but it signals aggression.
- An **automatic renewal clause** without express consent (*„umowa przedłuża się o kolejny rok, chyba że strona złoży wypowiedzenie 6 miesięcy przed terminem"*: renews for a year unless notice is given 6 months ahead).

## Triage procedure

### Step 1: completeness check (1 to 2 minutes)

- Does the contract have a date, place, parties, and representation?
- Does it have all the *essentialia negotii* (type of relationship, subject, remuneration, term)?
- Are the annexes attached?

Any missing element makes it **YELLOW automatically** (fill the gap, then repeat the triage).

### Step 2: scan the risk areas (3 to 5 minutes)

Go through the GREEN, YELLOW, and RED criteria in turn. The first RED flag makes the contract RED. No RED but any YELLOW makes it YELLOW. Neither makes it GREEN.

**Areas to scan, in order:**

1. Liability (cap, exclusions, intentional fault)
2. Copyright (transfer, fields of exploitation)
3. Confidentiality and NDA (duration, scope)
4. Termination and exit
5. Contractual penalties
6. GDPR (data processing agreement, transfers to third countries)
7. Assignment of the contract
8. Dispute resolution
9. Contract change clauses (asymmetry)
10. Remuneration and payment terms

### Step 3: triage note (1 to 2 minutes)

**Output format:**

```
TRIAGE: 🟢/🟡/🔴

Category: [GREEN / YELLOW / RED]

Significant clauses:
- § X: [short description of the signal]
- § Y: [short description of the signal]
- ...

Recommendation:
[GREEN] Can be signed. Optional note: [short remark].
[YELLOW] Needs analysis before signing. Points to discuss: [list].
[RED] Don't sign without negotiation. Blocking points: [list].
```

### Step 4 (YELLOW and RED only): hand over to a full analysis

YELLOW and RED leave the matter open. The next step is `full-review.md` or `risk-audit.md`. Triage doesn't replace a full analysis. It's a first filter.

## Operating rule: when to use triage

- ✅ Standard NDAs (mutual or one-way) from typical counterparties
- ✅ Technical annexes (billing, SLA changes, adding a module)
- ✅ Simple service contracts up to PLN 50,000 a year
- ✅ A first filter when many contracts arrive for review
- ✅ The client's decision *"should we even read this further, or reject it?"*

**When NOT to use triage (go straight to a full analysis):**

- Contracts worth over PLN 250,000 a year
- Contracts with a merger, acquisition, or investment element
- Employment contracts, and B2B equivalents with elements of control (risk of reclassification)
- Contracts that affect the client's capital structure
- Any case where the client signals *"this matters to us, check it carefully"*

## Links within the skill

- `workflows/full-review.md`: the next step for YELLOW and RED
- `workflows/risk-audit.md`: a deeper risk analysis for YELLOW
- `references/golden-rules.md`: the golden rules as a filter for GREEN, YELLOW, and RED
- `references/clause-bank/INDEX.md`: reference to typical KTZR clauses (for comparison)

## Final caveat

Triage is an operational tool for legal work, not a market product or advisory service. A triage result doesn't replace a full legal analysis. In every matter, the final decision to sign belongs to the client, after consulting the lawyer handling the matter.
