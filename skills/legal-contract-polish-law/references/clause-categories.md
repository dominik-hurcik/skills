# Contract clause categories: an analytical taxonomy

**Status:** a KTZR analytical model that helps with drafting and diagnosing clauses. Inspired by *Adams, A Manual of Style for Contract Drafting* (5th ed., ABA 2023), *"categories of contract language"*, adapted to the Polish legal system.

**Purpose:** give the agent and the KTZR lawyer a taxonomy of 7 main clause categories (plus 2 auxiliary ones: intention and recommendation), so every clause in a contract can be classified deliberately. Mixing categories in one clause is a common source of ambiguity.

**Caveat:** the taxonomy is analytical, not normative. It doesn't replace doctrine or case law. In a specific case, the category of a clause can itself be disputed. The taxonomy serves the drafter, not the court.

Example clauses are in Polish, because the contracts are.

## TL;DR

1. **One clause, one category.** If a clause tries to do more than one thing (for example it obliges and permits at once), it should probably be split in two.
2. **A category that doesn't fit the content creates ambiguity.** The clause *„Strony zobowiązują się, że termin biegnie od dnia zawarcia"* (the Parties undertake that the period runs from signing) mixes an obligation with a policy. A period isn't an obligation. It's a calculation rule.
3. **Choosing the category starts with a question:** *do I mean (a) a duty to do something, (b) a right to something, (c) a ban on something, (d) a rule with no obliged party, (e) a statement of fact, (f) an act performed by the contract itself, or (g) a condition?*
4. **Polish obligation syntax** has its own pattern. See rule 2 in `drafting-style.md` (layer 2): *„[Strona] zobowiązuje się do [czynności w bezokoliczniku]"*. The taxonomy adds the other categories.

## Seven clause categories

### 1. Obligation (a duty to perform)

**Construction:** *„[Strona] zobowiązuje się do [czynności]"* / *„[Strona] [czyni X]"*

**Example:**
> *„Wykonawca zobowiązuje się do wystawienia faktury w terminie 7 dni od dnia uznania rachunku."*

**Features:**
- An identifiable obliged party (who?)
- A specific act to perform (what?)
- Usually with a deadline (when?)
- Non-performance is a breach, leading to liability (art. 471 KC) or a contractual penalty

**Anti-pattern:** using an obligation where a policy is enough. *„Strony zobowiązują się, że umowa wchodzi w życie z dniem podpisania"* (the Parties undertake that the contract enters into force on signing) isn't an obligation. It's a policy: the date of entry into force needs no undertaking.

### 2. Right (an entitlement to do something)

**Construction:** *„[Strona] ma prawo do [X]"* / *„[Strona] może [X]"*

**Example:**
> *„Wykonawca ma prawo do wstrzymania świadczenia Usług w razie opóźnienia w zapłacie wynagrodzenia powyżej 30 dni."*

**Features:**
- An identifiable entitled party
- A specific right
- Exercising the right usually isn't a breach
- Often tied to a condition that activates the right

**Anti-pattern:** *„Wykonawca może zobowiązać się do [X]"* (the Contractor may undertake to X) mixes a right with an obligation. Either the Contractor undertakes (an obligation) or has the right (a right), not both.

### 3. Prohibition (a duty to refrain)

**Construction:** *„[Stronie] nie wolno [X]"* / *„[Strona] zobowiązuje się nie czynić [X]"* / *„[Strona] zobowiązuje się powstrzymać od [X]"*

**Example:**
> *„Zamawiający zobowiązuje się powstrzymać od jakichkolwiek wypowiedzi mogących naruszyć dobre imię Wykonawcy."*

**Features:**
- A negative obligation (a duty not to act)
- Breach means doing the prohibited act
- Often secured by a contractual penalty (art. 483 KC)

**Anti-pattern:** *„Zamawiający nie powinien udostępniać Materiałów"*. *„Nie powinien"* (should not) isn't a prohibition. It's a recommendation, and enforcing it is unclear. Better: *„Zamawiający zobowiązuje się nie udostępniać Materiałów"*.

### 4. Policy (a rule with no obliged party)

**Construction:** *„[X] wynosi [Y]"* / *„[X] biegnie od [Y]"* / *„[X] stanowi [Y]"* / *„[X] jest [Y]"* (X amounts to, runs from, constitutes, is Y)

**Example:**
> *„Termin płatności wynosi 30 dni od dnia doręczenia faktury."*
> *„Okres Przejściowy biegnie od dnia zawarcia Porozumienia do dnia 31 grudnia [roku] r."*

**Features:**
- No identifiable obliged party
- A statement of a calculation, factual, or definitional rule
- Applies to the whole contract or to a specific paragraph

**Anti-pattern:** phrasing a policy as an obligation. *„Strony zobowiązują się, że termin płatności wynosi 30 dni"* is clumsy, because "being 30 days" needs no undertaking. Just write *„Termin płatności wynosi 30 dni"*.

### 5. Representation (a statement of fact)

**Construction:** *„[Strona] oświadcza, że [X]"* / *„Strony zgodnie oświadczają, że [X]"* / *„[Strona] potwierdza, że [X]"*

**Example:**
> *„Wykonawca oświadcza, że posiada pełne prawa autorskie majątkowe do Utworów oraz że ich przeniesienie na Zamawiającego nie narusza praw osób trzecich."*

**Features:**
- A statement of a factual or legal state of affairs
- If it's untrue, the party is liable for the assurance (art. 471 KC, and possibly art. 84 to 86 KC, avoiding a declaration made under error)
- Often tied to an indemnity (see `clause-bank/10-kary-umowne.md` and `knowledge-base/07-indemnifikacja-kary-umowne.md`)

**Anti-pattern:** mixing a representation with an obligation. *„Wykonawca oświadcza, że będzie wystawiał faktury"* (represents that it will issue invoices). A future act isn't a "fact" to represent. It should be an obligation: *„Wykonawca zobowiązuje się do wystawiania faktur"*.

### 6. Performative act (a legal effect by the contract itself)

**Construction:** *„[Strona] niniejszym [przenosi / udziela / zwalnia / wyraża zgodę / wypowiada]"* (hereby transfers, grants, releases, consents, terminates)

**Example:**
> *„Wykonawca niniejszym przenosi na Zamawiającego autorskie prawa majątkowe do Utworów na polach eksploatacji wymienionych w § 5."*
> *„Wykonawca niniejszym wyraża zgodę na rozpowszechnianie jego wizerunku w Okresie Przejściowym."*

**Features:**
- The legal effect arises from the contract itself (a transfer of rights, a consent, a release from debt)
- Key word: *„niniejszym"* (hereby), or none when the context is clear
- Once signed, the act is done. It needs no separate performance.
- Adams calls this the *"language of performance"*

**Anti-pattern:** using an obligation where the act itself is enough. *„Wykonawca zobowiązuje się do przeniesienia praw autorskich"* (undertakes to transfer the copyright) requires a separate, later act of transfer. Better: *„Wykonawca niniejszym przenosi prawa autorskie"*, with immediate effect.

### 7. Condition (a triggering event)

**Construction:** *„W przypadku [zdarzenia], [strona] [czyni X]"* / *„Jeżeli [zdarzenie], [skutek]"* (the KTZR style prefers *„W przypadku"*, see layer 2, rule 1)

**Example:**
> *„W przypadku opóźnienia w zapłacie którejkolwiek z rat o więcej niż 7 dni od terminu jej wymagalności Porozumienie wygasa w części, w jakiej nie zostało wykonane do dnia upływu tego terminu."*

**Features:**
- A condition precedent (the effect arises when it's met) or subsequent (the effect ends when it's met): art. 89 to 94 KC
- Linked to another category. The condition activates an obligation, a right, a prohibition, or a policy.
- A complex construction by nature, so inconsistencies are easy (see `clause-bank/16-ugody.md`, the anti-pattern on duplicated sanction mechanisms)

**Anti-pattern:** hiding a condition inside an obligation. *„Wykonawca zobowiązuje się do wstrzymania Usług, jeżeli Zamawiający opóźni się z zapłatą o 30 dni"* is really a condition plus a right (the Contractor *may* suspend, not *must*). Better: *„W przypadku opóźnienia w zapłacie powyżej 30 dni Wykonawca ma prawo wstrzymać świadczenie Usług"*.

## Auxiliary categories (used less often)

### Intention

**Construction:** *„Strony zamierzają, że [X]"* / *„Intencją Stron jest, aby [X]"* (the Parties intend that X)

Used mainly in the preamble, or in clauses with an uncertain legal effect (for example *„Strony zamierzają, aby Wykonawca pozostawał niezależnym przedsiębiorcą, a nie pracownikiem Zamawiającego"* in a B2B contract). An intention isn't binding, but it helps interpretation.

### Recommendation

**Construction:** *„[Strona] powinna [X]"* / *„zalecane jest [X]"* (should, it is recommended)

Rarely used at KTZR. It's self-contradictory: if something is only recommended, the contract gives no right to enforce it. It may appear in technical annexes as *"best practices"*.

## Operating rule: how to use the taxonomy when drafting

Before writing a clause, ask yourself four questions:

1. **What do I want this clause to achieve?** (the intended effect)
2. **Which category best captures that effect?** (obligation, right, prohibition, policy, representation, performative act, condition)
3. **Am I trying to do more than one thing in one clause?** If so, split it into two or more.
4. **Does the syntax match the category?** (*„zobowiązuje się"* for an obligation, *„ma prawo"* for a right, *„niniejszym"* for a performative act, *„W przypadku"* for a condition; see the table below)

| Category | Opening pattern |
|---|---|
| Obligation | *Strona zobowiązuje się do…* |
| Right | *Strona ma prawo do… / może…* |
| Prohibition | *Stronie nie wolno… / Strona zobowiązuje się nie czynić…* |
| Policy | *X wynosi / biegnie / stanowi / jest…* |
| Representation | *Strona oświadcza, że…* |
| Performative act | *Strona niniejszym przenosi / udziela / wyraża zgodę…* |
| Condition | *W przypadku [X]… / W razie [X]…* |

## Operating rule: diagnosing ambiguity

When a clause reads *oddly*, or the other side raises interpretive objections, the taxonomy helps you find *why*:

- **Mixed categories** in one sentence: the most common cause
- **The wrong category for the effect** (for example an obligation where a policy belongs): a court struggles to interpret it
- **No category at all:** the clause is just an observation, with no legal effect

## Links within the skill

- `references/drafting-style.md`: layer 2 describes the syntax patterns for obligations (an extension of this taxonomy)
- `references/drafting-style.md`: layer 2, rule 1 (conditional constructions, *„W przypadku"*)
- `references/golden-rules.md`: golden rule 12 (§ 1 = Subject of the Contract, a map of the clause categories in later paragraphs)
- `workflows/risk-audit.md`: the clause category as a filter in audits
- `workflows/fix-clause.md`: diagnosis through the taxonomy when fixing clauses

## Doctrinal sources

- **Adams, Kenneth A.**, *A Manual of Style for Contract Drafting*, 5th ed., American Bar Association 2023. The concept of *"categories of contract language"* (chap. 2 to 3)
- **Garner, Bryan A.**, *Guidelines for Drafting and Editing Contracts*, West Academic Publishing 2019. A complementary approach with a focus on plain language
- **Wronkowska, Sławomira; Zieliński, Maciej**, *Komentarz do Zasad techniki prawodawczej*, Wydawnictwo Sejmowe 2004. Polish standards for drafting legislation (applied by analogy to contracts)
- *Rozporządzenie Prezesa Rady Ministrów z 20 czerwca 2002 r. w sprawie „Zasad techniki prawodawczej"* (Dz.U. 2016 poz. 283 t.j.): the formal Polish drafting standard
