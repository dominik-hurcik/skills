# Workflow: risk audit (standalone)

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

A standalone audit of the legal and business risks in a contract. Narrower than a full analysis. It focuses **only on risks**, without the essentialia, the completeness checklist, or the internal logic.

Use this workflow when the user says: "check the risks", "audit", "what's dangerous here", "what am I exposed to", "check for traps".

---

## Step 0: the firm's memory

If a firm memory tool is available, check it before the analysis. It may hold earlier notes about this matter or counterparty.

1. `list_categories()`: if the memory is empty, skip the rest of this step and go to Step 1.
2. If it isn't empty:
   - `recall("counterparty name")`: if the name appears in the contract
   - `recall("contract type")`: for example "NDA", "body leasing", "SaaS"
   - `recall("key risks")`: for example "liability cap", "non-solicitation"

Show the hits briefly (at most 5 entries):

```
📋 Firm memory: context for this matter:
[entry 1]
[entry 2]
...
```

If there are no hits, or no memory tool, **skip this section without telling the user** and go to Step 1.

---

## Step 1: identify the risks

Read the contract with an eye on the typical risk areas. Open `references/golden-rules.md` as the lens through which you read it.

**Quoting legislation (R1):** `verify_article()` before every cited article, or `[UNVERIFIED]` without the MCP server. A wrong article number in the report is a substantive error. **Never give court case numbers from memory.** To rely on case law, describe the holding without a case number, or mark it `[CASE NUMBER UNVERIFIED]`.

### Typical risk areas to check

**Liability and penalties:**
- No liability cap
- Unlimited lost profits (utracone korzyści)
- An attempt to exclude intentional fault (void, art. 473 § 2 KC)
- Contractual penalties out of proportion to the breach
- No compensation for a non-compete (without it, the clause may be ineffective or breach good morals)

**Copyright (in IT contracts):**
- Fields of exploitation not listed (without them there's no dispositive effect, art. 41 ust. 2 PrAut)
- No anti-copyleft clause (risk of acquiring GPL or AGPL software)
- No clean-IP warranty from the transferor
- Unclear moment of transfer of rights

**Definitions and logic:**
- Terms used without a definition
- Definitions that contradict each other
- Definitions used inconsistently with the text

**Representation:**
- The signatory's authority isn't stated (KRS, power of attorney)
- Incomplete party details (no KRS or NIP)

**Termination and exit:**
- No termination clause (art. 746 KC allows termination at any time, but without rules on notice and effects a party risks a damages claim)
- No exit procedure (return of materials and data, settling work in progress)
- Asymmetric termination (only one side can terminate)

**GDPR (RODO):**
- Processing entrusted without an art. 28 RODO agreement
- No list of sub-processors
- No procedure for returning or deleting data

**Legal title and reclassification:**
- In body leasing: no express exclusion of art. 22 § 1 KP, and no autonomy for the Specialist (risk of reclassification as employment)
- In a contract for a specific work (umowa o dzieło): no defined result (risk of reclassification as a mandate contract, with social security (ZUS) consequences)

**Confidentiality:**
- No period after the contract ends
- No exceptions (public information, independently developed)
- No contractual penalty (hard to enforce)

**Disputes:**
- An inconvenient court (foreign jurisdiction with no reason)
- Foreign law (needless complication for a Polish contract)
- An arbitration clause that doesn't name the tribunal

---

## Step 2: classify the risks

Give each identified risk a level:

| Level | Criteria |
|---|---|
| 🔴 **CRITICAL** | Can lead to: invalidity of the contract or part of it; unlimited liability; loss of copyright; enforcement against the client on an unexpected scale; administrative sanctions |
| 🟠 **HIGH** | Significant financial risk (over 10% of the contract value) or operational risk; hard to fix after signing; needs immediate negotiation |
| 🟡 **MEDIUM** | Worth fixing; possible interpretation problems; specific clauses may be ineffective |
| 🟢 **LOW** | Minor inaccuracies; style suggestions; improvements |

---

## Step 3: output format

```
## RISK AUDIT: [contract or project name]

### 🔴 CRITICAL RISKS

#### 1. [Short risk title]: § X ust. Y
**Description:** [specifically what's wrong and why it's risky]
**Consequence:** [what can happen: enforcement, invalidity, a penalty, loss of rights]
**Recommendation:** [a specific fix]
**Clause from the bank:** `references/clause-bank/XX-yyy.md`

#### 2. [...]

### 🟠 HIGH RISKS

#### 1. [...]

### 🟡 MEDIUM RISKS

#### 1. [...]

### 🟢 LOW RISKS

#### 1. [...]

---

## SAFETY SCORE: XX/100

[2 to 3 sentences on what drove the score]

**Verdict:** [SIGN with minor fixes / NEGOTIATE / REWORK THOROUGHLY / DON'T SIGN]

---

*This analysis is supporting material and doesn't replace the assessment of the radca prawny handling the matter.*
```

---

## Safety score scale

| Points | Description | Verdict |
|---|---|---|
| 85-100 | Very good; minor improvements | SIGN with minor fixes |
| 70-84 | Good; a few areas to negotiate | NEGOTIATE (1 to 3 🟠 risks) |
| 50-69 | Mixed; significant risks | NEGOTIATE (several 🟠 or one 🔴) |
| 30-49 | Weak; a thorough rework is needed | REWORK THOROUGHLY |
| 0-29 | Dangerous; don't sign in its current form | DON'T SIGN |

Each 🔴 takes off about 15 to 20 points, each 🟠 about 5 to 10, each 🟡 about 1 to 3, and each 🟢 about 0.5.

---

## Choosing clauses from the bank to fix the risks

After the audit, propose **specific clauses from the bank** to fix the most serious risks. Format:

```
### KTZR bank clauses to add

🔴 RISK 1 (unlimited liability)
→ Use: `references/clause-bank/11-odpowiedzialnosc.md`, the variant with a cap of 12 months' fees

🔴 RISK 2 (no anti-copyleft clause)
→ Use: `references/clause-bank/08-prawa-autorskie-ip.md` (the variant with clean-IP warranties)

🟠 RISK 3 (no confidentiality period after the contract)
→ Use: `references/clause-bank/09-poufnosc.md`, the layered confidentiality periods (10 years / indefinitely for trade secrets)
```

Don't paste the full clause text here (unless the user asks). Show **where to find them**.

---

**STOP. Present the report and ask:** "Do you want me to generate corrected clauses for any of these risks?"
