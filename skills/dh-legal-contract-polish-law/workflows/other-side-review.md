# Workflow: review from the other side's perspective (devil's advocate)

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

A workflow that simulates **the other side's lawyer** reading a draft contract or settlement. Goal: find everything the other side could use against our client, *before* the document goes out.

**Triggers (when to run it):**
- "review from the other side"
- "what can they challenge"
- "how will the other side read this"
- "the counterparty's perspective"
- "red team"
- "devil's advocate"
- "audit from the opponent's view"
- "attacks on the contract"
- "check how the other side could use this"

**When to run it proactively:** always before sending a settlement, a demand for payment, a counter-proposal, or a contract in a high-stakes negotiation. It's the final check before a document leaves the firm.

---

## Step 0: the firm's memory

If a firm memory tool is available, check whether the firm has earlier information about the counterparty or its negotiating style.

1. `list_categories()`: if the memory is empty, skip the rest of this step and go to Step 1.
2. If it isn't empty:
   - `recall("counterparty name")`: history of cooperation, earlier positions
   - `recall("negotiations")`: documented tactics of the other side
   - `recall("precedents")`: how similar matters ended

Show the hits as context for the opponent persona:

```
📋 Firm memory: counterparty history:
[entries on the counterparty and its negotiation history; they shape the opponent persona in Step 1]
```

If there are no hits, or no memory tool, **skip this section** and go to Step 1.

---

## Step 1: establish the sides and the context

Before reading "from the other side":

1. **Identify our client:** whom do we represent in this contract? (Contractor? Client? Landlord? Beneficiary?)
2. **Identify the other side:** who reads our contract across the table?
3. **Establish the context:** is there an open dispute? A negotiation of new cooperation? An implementing contract in an ongoing relationship?
4. **Establish the profile of the other side's lawyer:** a large corporate firm (looks for fine print)? A small general practice (looks for the obvious)? A defensive in-house lawyer? A business owner with no lawyer (looks for "why should I pay this much")?

The result of this step is **the opponent persona**. In Step 2 you step into their shoes.

---

## Step 2: six categories of attack

Read the contract point by point from the opponent's perspective, looking for each of **six categories**.

### Category 1: unfavourable concessions

Passages where **our side accidentally concedes** a fact or legal position that favours the other side.

**Check questions:**
- Does the contract contain a statement that confirms the other side's claims or rights more broadly than we need?
- Does the preamble contain findings of fact that could arm the other side in a future dispute?
- Do references to earlier contracts or rules "switch on" clauses that hurt our client?
- Do we use words like „potwierdzają", „uznają", „zgodnie z" (confirm, acknowledge, in accordance with) about disputed matters?

**Warning signs:**
- *„Strony zgodnie potwierdzają, że…"* (the Parties jointly confirm that…) about a disputed fact
- *„kierując się treścią [poprzedniej umowy]"* (following the content of [the earlier contract]): switches on the earlier contract's clauses through a back door
- *„Strony nie mają wobec siebie żadnych roszczeń"* (the Parties have no claims against each other): can be used against us if there's a claim we don't know about
- *„Wszystko, co przekazane do dnia podpisania, stanowi własność…"* (everything handed over before signing belongs to…): a broad transfer

**How the anti-pattern works:**
A preamble with a reference like *„kierując się treścią [wcześniejszej umowy]"* gives the other side an argument that specific clauses of the expired contract (for example on transfer of copyright) still applied after the written contract expired. The classic fix: remove the reference to the whole content, or narrow it to *„operacyjnych zasad wykonywania świadczeń"* (the operational rules for performing the services), without touching substantive clauses.

### Category 2: interpretive ambiguities

Words or constructions that let the opponent **read a clause another way** in their favour.

**Check questions:**
- Do we use „odpowiednio", „stosownie", „w miarę możliwości", „rozsądny", „uzasadniony" (accordingly, as appropriate, where possible, reasonable, justified) without detail?
- Are cut-off dates unambiguous („do dnia X włącznie / wyłącznie": up to and including, or excluding, day X)?
- Do referring pronouns („ten", „te", „powyższy") point clearly to one source?
- Are amounts described as gross, net, with VAT, or without VAT, and is that consistent throughout?
- Are conditional events described specifically ("if X" vs "if circumstances arise")?

**Warning signs:**
- *„w terminie odpowiednim do okoliczności"* (within a period appropriate to the circumstances): always disputed
- *„koszty zostaną pokryte"* (costs will be covered): by whom, to what extent, on what basis?
- *„świadczenie zostanie wykonane"* (the service will be performed): passive voice with no actor

### Category 3: evidentiary gaps

Missing provisions the other side could use in litigation.

**Check questions:**
- Is the moment of payment clearly fixed? (Credit to the account, or debit?)
- Is the mechanism for service of notices described? (Email or letter, to which address?)
- Are there evidentiary clauses („oświadczenia stron stanowią pełny dowód": the parties' statements are full evidence)?
- Does the contract require specific forms (written, documentary), and do they serve as evidence?
- Are there mechanisms to confirm performance (reports, statements)?

**Warning signs:**
- No deadline for raising objections (silence may be taken as acceptance)
- No acceptance mechanism (in implementation contracts, without it there's no basis for payment)
- No addresses for notices (the defaults from the parties' details may differ)

### Category 4: internal contradictions

Logical holes that let the other side **read selectively**.

**Check questions:**
- Is every paragraph consistent with the preamble?
- Do mutually dependent clauses (conditional consent + expiry + satisfaction) form a closed loop?
- Does "claims are exhausted" in one clause clash with "a duty to pay" in another?
- Are internal cross-references („§ X ust. Y") still correct after all edits?

**Warning sign (classic):** a clause saying the contract expires "in full", while obligations are left in place after expiry. It needs reworking into "expires in the part not yet performed".

### Category 5: calculation and date errors

Specifics: numbers, deadlines, dates.

**Check questions:**
- Do the instalments add up to the total?
- Are the payment dates compatible (for example a third instalment on 31.07 and the consent expiring on 31.07: a collision!)?
- Do the figures and the words for amounts match (*„50 000 zł (słownie: pięćdziesiąt tysięcy złotych)"*)?
- Does „do dnia X" mean up to and including X, or excluding it?
- From which date does interest run (the date of the demand? the due date?)?

**Warning signs:**
- The sum of the parts ≠ the declared total
- Cut-off dates that collide with no explanation
- No amount in words for the main sum

### Category 6: exit ramps

Clauses the other side can use to **withdraw** from the contract or slow down performance.

**Check questions:**
- Are force majeure clauses too broad?
- Are the "important reasons" for termination specific or open-ended?
- Are avoidance mechanisms (for example art. 918 KC for settlements) limited where they could hurt?
- Are the termination clauses symmetric, and do we want them to be?
- Are there provisions like "until the condition is met" that give the other side unlimited delay?

**Warning signs:**
- „Strony mogą rozwiązać umowę z ważnych powodów" (the Parties may terminate for important reasons) without a closed list
- No deadlines for dealing with objections
- A right to withdraw quietly without penalties

---

## Step 3: generate the report

After all six categories, generate **the other side's perspective report** with this structure:

```
## Opponent persona
[Briefly: who reads it, their motivations, their tools]

## Weaknesses found

### P1: critical (must be fixed before sending)
1. [Location: § X ust. Y] [Weakness] → [The other side's attack] → [Recommendation]
2. ...

### P2: significant (recommended to fix)
1. ...

### P3: minor (to consider)
1. ...

## Questions for the client before sending
[If some points need the client's business decision before the fix]

## Overall risk assessment
[1 to 3 sentences: how the other side's view affects our negotiating position]
```

**Priorities:**
- **P1:** a weakness the opponent will very likely exploit. It could significantly weaken our position in a dispute. Always fix it.
- **P2:** a weakness that could be exploited in aggressive negotiation, but needs a specialist. Fixing it is recommended, though not blocking.
- **P3:** a theoretical weakness, unlikely to be exploited, but "nice to have" fixed.

---

## Step 4: iterate with the client

Some P1 and P2 items may need **a business decision by the client**, not just a legal one (for example *"do you accept the risk of a symmetric non-disparagement clause in exchange for signing faster?"*).

After the fixes, **run the workflow again** (steps 1 to 3). Iterate until only accepted P2 and P3 items remain and the client knowingly accepts them.

## Step 5: final check before sending

**A lesson from practice:** after several rounds of fixes, the client may **forget to apply** the final decisions (for example a change from gross to net, or a typo fix in a cross-reference). The workflow isn't finished until you've verified that every agreed change is actually in the document.

**Final checklist** (just before sending):

1. **Are all agreed changes in the document?**
   - Compare against the list of agreed changes (the P1 and P2 items approved in the iterations).
   - Watch especially for **small value changes** (gross or net, amounts, dates). They're easy to miss.
2. **Are internal cross-references still correct after all edits?**
   - Every *„zgodnie z § X ust. Y pkt Z)"*: check it still points to the right passage after renumbering.
   - Especially after adding or removing sections, later references may point to the wrong number.
3. **Is list numbering consistent?**
   - After switching from `(a)(b)(c)` to `1)2)3)`, check that references use *„pkt"* and not *„podpunkt"* or *„lit."* (see `drafting-style.md`, layer 2, rule 5).
4. **Are there duplicated mechanisms?**
   - See `references/clause-bank/16-ugody.md`, the anti-pattern on duplicated sanction mechanisms.
   - One mechanism, one paragraph. If two paragraphs govern the same effect, one should go.
5. **Are grammatical cases consistent when lists are joined?** (Polish grammar)
   - *„wraz z X oraz Y"*: X and Y must be in the same case (instrumental), not mixed with the genitive.
   - *„dochodzenia X, Y oraz Z"*: all in the genitive.
6. **Typos in bolding or placeholders?**
   - Split bolding (*„**5 000** **zł**"* instead of *„**5 000 zł**"*), a side effect of repeated Word edits. Merge it.
   - Placeholders for dates and places: consistent (5 dots or 4? one style throughout).
7. **Do party names in the clauses match the parties' details at the top?**
   - After many iterations, variants appear (*„Wykonawca"* / *„Zleceniobiorca"* / *„Strona"*). Everything should match the definition in the parties' details.

**Operating rule:** the final check is always done by **someone other** than the author of the final version (or by the agent, if the client works alone). A fresh pair of eyes catches what the author no longer sees.

---

## Workflow anti-patterns

- **Don't confuse this with the risk audit** (`risk-audit.md`). The risk audit looks *from our perspective*: what threatens us when performing the contract. This review looks *from the opponent's perspective*: what the opponent can find in it against us. They complement each other. They aren't interchangeable.
- **Don't limit yourself to legal language.** The other side's lawyer may have other specialisations (civil law, tax, IP). Think broadly.
- **Don't treat a clause as "safe" just because it's standard.** Standard clauses have the most case law, so the most known attacks.
- **Don't forget the tone.** Sometimes the weakness is the tone (for example an aggressive phrase in a settlement invites a hard counter instead of a quick signature).

---

## Links within the skill

- `workflows/risk-audit.md`: the complementary workflow (our client's perspective)
- `workflows/full-review.md`: a wider analysis (essentialia + consistency + risks + the other side)
- `references/golden-rules.md`: the KTZR golden rules (the overriding context)
- `references/knowledge-base/`: doctrinal knowledge to justify attacks and defences

---

## Example of use (schematic)

The example shows the structure of the process, not a specific matter. Each context (contract type, industry, the parties' roles) produces a different set of weaknesses and attacks, but the logic of the steps stays the same.

**A typical sequence:**

1. **Input:** a draft contract or settlement, freshly drafted by one side's lawyer, ready to send.
2. **The other side's persona:** a lawyer with a clear motivation (minimise obligations, keep as many rights as possible, extract information from the preamble).
3. **Mapping weaknesses:** for each clause, ask the questions from categories 1 to 6 (concessions, ambiguities, evidentiary gaps, internal contradictions, calculation and date errors, exit ramps).
4. **Classification:** give each weakness a priority: **P1** (must be fixed before sending), **P2** (recommended), or **P3** (knowingly accepted).
5. **Results table:** location → weakness → possible attack → recommendation → priority.

**Worth keeping in mind:**

- Sometimes a P3 weakness is a deliberate compromise (for example an asymmetric non-disparagement clause in a settlement, when our client has less public exposure).
- Sometimes a P1 weakness comes from a simple wording slip („brutto" applied to two payment items with different VAT regimes).
- Sometimes a P1 weakness comes from a real gap in the structure (a logical contradiction: withdrawing a consent that was never formally given).

The workflow works the same way for settlements that end disputes, IT implementation contracts, body leasing, NDAs, and exit agreements. The substance of the check questions changes. The structure of the process doesn't.
