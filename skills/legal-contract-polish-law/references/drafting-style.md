# KTZR drafting style

The contract drafting rules used at KTZR. The file has two layers:

1. **Lawyer's craft.** General rules of the trade, independent of any firm. If the layers conflict, this layer wins.
2. **KTZR style.** Specific syntax and terminology patterns taken from **KTZR's internal bank of model clauses**.

**Always load this file** when you generate or edit clauses. These rules rank below the KTZR golden rules and the essentialia negotii requirements.

The contracts are in Polish, so every example clause below is Polish. Explanations are in English. Text marked ❌ is an anti-pattern, and text marked ✅ is the pattern to use.

---

# LAYER 1: LAWYER'S CRAFT

These are general rules of the trade that every competent lawyer follows. **Always apply them**, whatever the contract type or firm.

## W1. Clarity and specificity: who, what, when, how

Every clause that imposes an obligation must answer four questions:

- **WHO:** which party (by its defined name, not a pronoun)
- **WHAT:** which specific act (an operative verb, not a generality)
- **WHEN:** by when (a date or a number of days, not „niezwłocznie" on its own)
- **HOW:** in what form, manner, or channel (in writing, by email, through system X, using the template in Annex Y)

**Anti-pattern (an empty clause):**
> *„Strony zobowiązują się do współpracy w zakresie świadczenia usług."*

It doesn't say who provides what (both parties to each other?), what exactly (which services?), when (from when to when?), or how (on what terms?). It's a statement of fact, not a binding rule.

**Pattern (an enforceable clause):**
> *„Wykonawca świadczy na rzecz Zamawiającego usługi w zakresie określonym w Załączniku nr 1, w terminach wskazanych w Harmonogramie (Załącznik nr 2), z wykorzystaniem narzędzi i metodyki opisanych w § 4 ust. 2-4."*

## W2. Leave no room for over-interpretation

Choose clarity over elegance.

- **Repeat the subject** instead of using a referring pronoun:
  - ❌ *„Wykonawca dostarczy raport. Ten zostanie zweryfikowany w terminie 7 dni od jego doręczenia."* What does „ten" refer to: the report or the contractor?
  - ✅ *„Wykonawca dostarczy Raport. Zamawiający dokona weryfikacji Raportu w terminie 7 dni od dnia doręczenia Raportu."*

- **Make deadlines concrete.** „Niezwłocznie" (without undue delay) on its own isn't a deadline:
  - ❌ *„Strona powiadomi drugą Stronę niezwłocznie."*
  - ✅ *„Strona powiadomi drugą Stronę niezwłocznie, nie później niż w terminie 3 Dni Roboczych od dnia powzięcia informacji."*

- **Avoid „odpowiednio", „stosownie", and „w miarę możliwości"** (accordingly, as appropriate, where possible). They invite disputes about meaning. If you must allow flexibility, say **how much and who decides**:
  - ❌ *„Wykonawca dostosuje zakres usług odpowiednio do potrzeb Zamawiającego."*
  - ✅ *„Wykonawca dostosuje zakres usług do potrzeb Zamawiającego określonych w Zamówieniu, którego zmiana wymaga formy pisemnej pod rygorem nieważności."*

- **Avoid „z należytą starannością" (with due care) without detail.** It's the statutory standard (art. 355 KC), and repeating it adds nothing. To raise the bar, write *„z najwyższą starannością wymaganą od profesjonalisty w zakresie [X]"*.

- **Closed or open lists: decide.** *„w szczególności"* (in particular) opens the list, so it's illustrative. Without that phrase, the list is exhaustive. Make this choice on purpose.

### W2.1. Ambiguity and vagueness: two different tools

Adams (*MSCD*) and Garner distinguish:

- **Ambiguity:** several *precisely defined* meanings. The clause can be read two or more ways. **Usually a drafting error.**
- **Vagueness:** one meaning with *blurred edges*. The clause leaves the assessment to the specific case. **Sometimes a deliberate tool for flexibility.**

**Example of ambiguity:**
> ❌ *„Wykonawca dostarczy raport w terminie tygodnia."*

What does *„w terminie tygodnia"* (within a week) mean? A week from signing, or from the request? A calendar week or working days? **Two or more precise meanings mean ambiguity.** Fix it by naming the date or the trigger event.

**Example of vagueness:**
> ⚖️ *„Wykonawca podejmie rozsądne starania w celu uzyskania zgody…"*

*„Rozsądne starania"* (reasonable efforts) has one meaning, a duty to make efforts, but its limits are decided *after the fact* in context. **Choose it on purpose** when:

- you can't foresee every scenario in advance,
- the parties don't want to commit to *best efforts* (an absolute standard) or to *commercially reasonable efforts* (a higher standard), or
- there isn't enough data to be specific at signing.

**Operating rule:**
- **Ambiguity:** always resolve it (W2: leave no room for over-interpretation).
- **Vagueness:** use it deliberately. When you write *„rozsądny"*, *„uzasadniony"*, or *„w stosownym terminie"* (reasonable, justified, in due time), ask yourself: *do I really want flexibility, or do I just not want to be specific?* If it's the second, be specific.

**Useful additions:**
- With a vague standard, add *context that narrows it*, for example *„rozsądny termin uwzględniający charakter Świadczenia oraz dotychczasową praktykę współpracy w danym kwartale"*. It's still vague, but a court has more to work with.
- Alternatively, pair the vague standard with a *right to demand detail*, for example *„Strony uzgodnią szczegóły terminu na piśmie nie później niż w terminie 14 dni od dnia podpisania."*

### W2.2. Cross-references: prefer specific over general

Anti-pattern: *„powyższy"*, *„wyżej wymieniony"*, *„powyżej opisany"*, *„powyższego punktu"*, *„poniższego ustępu"* (the above, the aforementioned, the paragraph below). These forms:

- break when clauses are renumbered (after a move, „powyższy" no longer points where it did),
- are imprecise (which „above"?), and
- make the reader look back and count.

**Pattern:** always refer by a specific paragraph, section, or point number.

| Anti-pattern | Pattern |
|---|---|
| *„zgodnie z powyższym punktem"* | *„zgodnie z pkt 2)"* |
| *„wskazana w wyżej wymienionym ustępie kwota"* | *„kwota wskazana w ust. 1"* |
| *„opisany powyżej termin"* | *„termin określony w § 3 ust. 2"* |
| *„zaspokojonymi zgodnie z powyższym"* | *„zaspokojonymi zgodnie z pkt 2)"* |

**Side benefit.** A structural change (moving or adding a section) needs updated cross-references. With specific numbers that's a mechanical find-and-replace. With „powyższy" you must analyse every occurrence by hand.

**Exception.** A collective reference to *„powyższych ustępów"* is acceptable (for example *„Z przyczyn opisanych w ust. 1-3 powyżej Strony uzgadniają, że…"*) when the scope is unambiguous and covers all earlier sections of the paragraph. Simpler still: *„z przyczyn opisanych w ust. 1-3"*.

## W3. Industry terms: always defined

If the contract uses a term outside general legal language, **it must have a definition in § Definicje**. No exceptions.

This covers:
- **IT technical terms:** API, CI/CD, SLA, uptime, repository, branch, deploy, production or staging environment, source code, technical documentation, implementation, integration, single sign-on.
- **Business-specific terms:** Klient (in a commission agreement, *who* counts as a Client for commission), Projekt, Współpraca, Usługa Wsparcia, Maintenance, Wsparcie Techniczne.
- **Abbreviations and acronyms:** OC, RODO, SKD, GUS, SIP, ERP. Even if "everyone knows what it means", the contract must define it.
- **Metrics and indicators:** uptime of 99.9%, RPO, RTO, response time, repair time, each with a specific measurement method.

**Verification rule.** After writing a clause, go through it word by word. Every word that **isn't** from general or standard legal vocabulary needs a definition. If it has none, add a definition or rewrite the clause without that word.

**Anti-pattern:**
> *„Wykonawca świadczy usługi maintenance serwerów Zamawiającego."*

„Maintenance" is an undefined industry term. What does it cover? Patching, monitoring, backups? Only reacting to incidents, or proactive work too? In which hours? With what SLA?

**Pattern:**
> *„Wykonawca świadczy na rzecz Zamawiającego Usługi Utrzymania, obejmujące: (a) monitoring dostępności serwerów; (b) aplikację łatek bezpieczeństwa w terminie 7 dni od ich publikacji przez producenta; (c) backup danych w trybie określonym w § 5; (d) reakcję na zgłoszenia incydentów zgodnie z SLA (Załącznik nr 3). Definicję Usług Utrzymania zawiera § 1 ust. 8."*

### W3.1. Describe by features instead of adding undefined concepts

This complements W3. When a **concept** tries to sneak into the contract (for example *„indywidualna licencja dostępu"*, *„standardowy poziom usług"*, *„rozsądny okres"*, *„kursant aktywny"*) and you don't plan to add a formal definition, **describe it by its features** instead.

**Anti-pattern:**
> ❌ *„obejmuje wyłącznie odpłatne udostępnianie Materiałów słuchaczom… w ramach **indywidualnych licencji dostępu** w serwisach…"*

*„Indywidualne licencje dostępu"* (individual access licences) sounds sensible but has no definition. The other side can read it broadly: *"an individual licence is any separate subscription, so a corporate package for 50 trainees is 50 individual licences."*

**Pattern (described by features):**
> ✅ *„obejmuje wyłącznie odpłatne udostępnianie Materiałów w serwisach…, każdorazowo na rzecz indywidualnie zarejestrowanego słuchacza kursu zawodowego prowadzonego przez Zamawiającego, na podstawie odrębnej opłaty wniesionej za dostęp tego słuchacza;"*

Three specific defining features, each an **independent test for breach**:

- *„indywidualnie zarejestrowanego słuchacza"*: each person has their own account,
- *„kursu prowadzonego przez Zamawiającego"*: a direct relationship, not through intermediaries,
- *„odrębnej opłaty wniesionej za dostęp tego słuchacza"*: a fee tied to that specific access.

With the pattern, the other side must meet three independent criteria together. With the anti-pattern, it has one concept to interpret.

**Operating rule.** If a concept has no definition in § Definicje, rewrite the clause by features. Don't leave the concept in "hoping" it's clear.

### W3.2. Balancing the scope in scope clauses

In settlements and agreements that end a dispute, you often have to define the **scope of permitted use** (of what, by whom, where, how). There's a tension between:

- **too broad a description** (for example *„dotychczasowa praktyka Stron"*, *„standardowy zakres"*, *„zgodnie z dotychczasowymi zasadami"*: the parties' practice so far, the standard scope, the rules applied so far). An anti-pattern, see W8 anti-pattern 3.
- **too narrow a description** (for example a precise operating model: *„1 słuchacz = 1 opłata = 1 dostęp"*). It can block the other side's legitimate business models and make signing harder.

**Balancing pattern:**
- **Narrow the context tightly** (to whom, within which activity, which product): *„Słuchaczom kursów zawodowych prowadzonych przez Zamawiającego ([nazwa instytucji])"*.
- **Leave the commercial model flexible** (subscription, package, one-off purchase: all fine, as long as they stay within the context).

The result: the other side has operational freedom in its commercial model, but the context limits it firmly.

## W4. Party names: by legal type of relationship

**Choose the pair of party names from the dominant legal type of the contract.** This isn't a style preference. It follows from the structure of the Civil Code (KC) and special statutes.

| Contract type | Legal basis | Pair of party names |
|---|---|---|
| Contract for a specific work (umowa o dzieło) | art. 627 KC | **Zamawiający / Wykonawca** (common usage; KC says "przyjmujący zamówienie") |
| Mandate contract (umowa zlecenia) | art. 734 KC | **Zleceniodawca / Zleceniobiorca** (common usage; KC says "dający zlecenie / przyjmujący zlecenie") |
| Contract for services | art. 750 KC with art. 734 | as for a mandate, or **Usługodawca / Usługobiorca** |
| Sale | art. 535 KC | **Sprzedawca / Kupujący** |
| Lease (najem) | art. 659 KC | **Wynajmujący / Najemca** |
| Lease with right to profits (dzierżawa) | art. 693 KC | **Wydzierżawiający / Dzierżawca** |
| Construction works | art. 647 KC | **Wykonawca / Inwestor** |
| Copyright licence | art. 41 et seq. PrAut | **Licencjodawca / Licencjobiorca** |
| Transfer of copyright | art. 41 PrAut | **Zbywca / Nabywca** (or **Autor / Nabywca**) |
| Assignment of receivables (cesja) | art. 509 KC | **Cedent / Cesjonariusz** |
| Loan | art. 720 KC | **Pożyczkodawca / Pożyczkobiorca** |
| Gift | art. 888 KC | **Darczyńca / Obdarowany** |
| Commission (komis) | art. 765 KC | **Komitent / Komisant** |
| Carriage | art. 774 KC | **Wysyłający / Przewoźnik** or **Zamawiający / Przewoźnik** |
| Forwarding (spedycja) | art. 794 KC | **Dający zlecenie / Spedytor** |
| Settlement (ugoda) | art. 917 KC | the names of the parties to the dispute; no statutory pair |
| NDA (an innominate contract) | art. 353¹ KC | **Strona Ujawniająca / Strona Otrzymująca** (if one-way: **Ujawniający / Odbiorca**) |

### Mixed contracts: by the dominant relationship

When a contract combines several types (for example IT body leasing = services + transfer of copyright + NDA), pick the names from the **dominant legal type**. Don't switch names at each transition.

**Example, IT body leasing:**
- Dominant type: contract for services (art. 750 KC). It frames the whole cooperation, and copyright follows from the services.
- Pair of names: **Usługodawca / Usługobiorca** (or Zleceniodawca / Zleceniobiorca), kept in the IP and confidentiality paragraphs too.
- **Don't switch** to "Zbywca / Nabywca" in the paragraph on transfer of rights. That would put a third pair of names into one contract and blur its structure.

**Example, IT implementation contract (fixed price + maintenance):**
- Dominant type: contract for a specific work (art. 627 KC) with elements of ongoing services.
- Pair of names: **Zamawiający / Wykonawca**. For the service part (maintenance after go-live), you can add a definition: "Wykonawca świadczy również Usługi Utrzymania na zasadach określonych w § X".

**Example, assignment combined with a settlement:**
- Dominant type: depends on context. If the assignment is a tool for settling the dispute, the settlement dominates, so use the dispute parties' names. If the contract is *primarily* an assignment with settlement elements, use **Cedent / Cesjonariusz**.

**Operating conclusion.** Before you write any clauses, **map the dominant legal type** in the essentialia negotii and derive the pair of names from it. Keep those names **throughout the contract**, not only in the paragraph closest to that type.

### Category names for unique roles

When one party's role is distinctive enough that a generic "X-dawca / X-biorca" pair blurs the picture, use a **category name**:
- **Specjalista** (the person providing services in body leasing, separate from the contract parties but named in clauses)
- **Partner** (a commission-based business intermediary)
- **Klient** (defined: *who* counts as a Client for commission)
- **Przewoźnik / Spedytor / Komisant** (if that is the essence of the relationship)

This doesn't replace the pair of parties. It adds to it. In body leasing you have **Usługodawca / Usługobiorca**, and **Specjalista** is a defined third party, not a party to the contract.

## W5. Define once, refer many times

Each rule has one place in the contract. If the penalty clause is in § 8, don't repeat it in § 12. Refer to it instead: *„zgodnie z § 8 ust. 2"*, *„zastrzeżonych w § 8"*, *„o których stanowi § 8"*.

**Order of work:** first define the concept or regulate the institution, then refer to that definition or rule. A repeated definition is an error, a repeated rule is an error, and a repeated obligation is an error.

**Anti-patterns to remove at once:**
- The same term defined twice in different places.
- An obligation clause moved to another paragraph with a small wording change.
- A severability clause appearing twice (once in the final provisions, once in "additional clauses").
- „Powyższe nie wyłącza" (the above doesn't exclude) plus a repeated rule from another paragraph, instead of a short cross-reference.
- The same contractual penalty set out both in the confidentiality paragraph and in the sanctions paragraph. There should be one, with references from elsewhere.

**Practical check.** After drafting, go through each paragraph and ask *"does the same content appear anywhere else?"* If it does, delete the duplicate and replace it with a cross-reference.

## W6. Use statutory references sparingly

A reference to a statute in a contract clause has a **specific legal function**, not a decorative one. Loading a contract with „zgodnie z KC", „w rozumieniu art. X PrAut", „stosownie do art. Y KP" **obscures and legally weakens the contract**. It doesn't strengthen it.

### When to refer to a statute: YES

1. **To adjust liability or a standard**, when you tighten or relax the statutory regime:
   - *„Strony wyłączają odpowiedzialność za szkody pośrednie (lucrum cessans), z zastrzeżeniem art. 473 § 2 KC"*. The reference makes sense here, because it marks the limit of a permitted exclusion (intentional fault).
   - *„Wykonawca świadczy usługi z najwyższą starannością wymaganą od profesjonalisty w zakresie [X], wykraczającą poza standard z art. 355 § 1 KC"*. It signals a deliberate raising of the standard.

2. **To define statutory concepts**, when you use a term defined in a statute and want to avoid repeating its definition:
   - *„Utwór": utwór w rozumieniu art. 1 ustawy z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych*
   - *„Tajemnica przedsiębiorstwa": informacje w rozumieniu art. 11 ust. 2 ustawy o zwalczaniu nieuczciwej konkurencji*

3. **To exclude or include a regime explicitly**, when you want no doubt about the legal basis:
   - *„Umowa nie kreuje stosunku pracy w rozumieniu art. 22 § 1 Kodeksu pracy"*. Key for IT body leasing.
   - *„Niniejsza umowa stanowi umowę o świadczenie usług w rozumieniu art. 750 KC w zw. z 734"*. When the classification matters for tax or litigation.

4. **Fields of exploitation for copyright.** Art. 41 ust. 2 PrAut requires the fields to be listed expressly, so a reference to art. 50 and 74 PrAut can be useful for the catalogue.

5. **The form of a legal act**, when you rely on a specific basis:
   - *„Zmiany Umowy wymagają formy pisemnej pod rygorem nieważności (art. 77 § 1 KC)"*

### When not to refer to a statute: NO

1. **When the clause regulates the matter itself.** The reference is decoration:
   - ❌ *„Strony rozliczą się zgodnie z postanowieniami niniejszej umowy oraz przepisami KC"*
   - ✅ *„Strony rozliczą się zgodnie z postanowieniami niniejszej umowy"*

2. **When the reference points to a general statutory rule that you don't change.** It repeats what applies by law anyway:
   - ❌ *„Wykonawca zobowiązuje się do wykonania umowy z należytą starannością zgodnie z art. 355 § 1 KC"*
   - ✅ *„Wykonawca zobowiązuje się do wykonania umowy z należytą starannością"* (art. 355 § 1 KC applies anyway)

3. **In obligation structures**, when the legal basis is obvious from context:
   - ❌ *„Strony zawierają umowę o świadczenie usług na podstawie art. 750 KC w zw. z 734 KC, mocą której Usługodawca świadczy usługi…"*
   - ✅ *„Usługodawca zobowiązuje się do świadczenia na rzecz Usługobiorcy usług…"* (the legal type follows from the content, not the preamble)

4. **In the final provisions.** The common „w sprawach nieuregulowanych stosuje się KC" (matters not covered are governed by the Civil Code) is empty, because that is the law anyway:
   - ❌ *„W sprawach nieuregulowanych niniejszą Umową zastosowanie mają przepisy Kodeksu cywilnego oraz inne właściwe przepisy prawa polskiego"*
   - ✅ Leave the clause out, or, if there's an international element, limit it to: *„Umowa podlega prawu polskiemu"*

5. **When the reference signals uncertainty**, as if the author wanted to "cover" themselves. It does more harm than good:
   - ❌ *„Wykonawca odpowiada za szkody na zasadach ogólnych KC"*: unclear; better to set the scope of liability.
   - ✅ *„Wykonawca odpowiada do wysokości 12-krotności miesięcznego wynagrodzenia z wyłączeniem szkód pośrednich, z zastrzeżeniem przypadków winy umyślnej"*

### Drafting test before adding a statutory reference

Ask yourself:

> *"Without this reference, does the clause mean something different, or the same?"*

If **the same**, the reference is decoration, so delete it. If **something different** (you modify a regime, define a statutory concept, or exclude a presumption), keep it, because it does a job.

**Operating conclusion.** When generating and editing clauses, **don't add references to KC, PrAut, KP, or KSH "automatically"** to strengthen the tone. Use a reference only when it does one of the five jobs above (W6, "YES"). When in doubt, **leave it out**.

## W7. Don't duplicate default rules of the Civil Code

Clauses that only repeat what already applies by law add nothing. They lengthen the text, and sometimes weaken it: if the clause restates the Code inaccurately, a court reads it against the party relying on it.

### Typical clauses that usually go

- **Severability clause** („nieważność postanowienia nie wpływa na ważność pozostałych"). It follows from art. 58 § 3 KC. Include it only if you add an active duty to replace the provision („Strony zastąpią…"), which goes beyond KC.
- **„W sprawach nieuregulowanych zastosowanie ma KC".** The default. With an international element, *„Umowa podlega prawu polskiemu"* is enough (see W6, NO, point 4).
- **„Strony zobowiązują się do współpracy w dobrej wierze"** (cooperate in good faith). Art. 354 § 1 KC requires this of every party by law.
- **„Strony zawierają umowę ze świadomością jej treści i skutków prawnych"** (the parties understand the contract). Awareness is presumed from signing. The clause doesn't close the routes in art. 82 to 86 KC, or art. 918 KC for a settlement (avoiding the effects of an error).
- **„Wykonawca odpowiada na zasadach ogólnych KC".** Changes nothing (art. 471 KC applies anyway). Either modify the regime explicitly or write nothing.
- **„Forma pisemna wymagana"** (written form required) without saying the consequence. It enforces nothing. Be specific: *„pod rygorem nieważności"* (on pain of invalidity, art. 73 § 1 KC) or *„dla celów dowodowych"* (for evidence, art. 74 KC).

### When to keep them anyway

- A foreign or English-speaking partner expects boilerplate: include it, but briefly.
- The clause genuinely refines a default rule within freedom of contract.
- The clause creates an extra duty beyond KC (for example a severability clause with an active duty to renegotiate).
- The clause signals a deliberate exclusion of the statutory regime (you modify it rather than repeat it).

### KTZR preference

At the firm we **deliberately leave out clauses that only repeat KC**. We keep only those that modify the statutory regime or regulate something the statute doesn't. This applies to § Postanowienia końcowe (final provisions) too. We often limit it to the legal classification of the contract (for example art. 917 KC for a settlement), the form of amendments, governing law and jurisdiction, and the number of copies. The severability clause and "awareness" declarations usually go.

## W8. Don't revive clauses of expired contracts through a back door

When the preamble of a settlement or new contract describes the parties' earlier relationship (especially an expired written contract), **watch for phrases that accidentally "switch on" clauses of the earlier contract** in the current relationship.

### Anti-pattern: „kierując się treścią [poprzedniej umowy]"

A phrase like:
> *„po wygaśnięciu [poprzedniej Umowy] Strony kontynuowały współpracę bez zachowania formy pisemnej, **jednak kierując się treścią w zakresie praw i obowiązków Stron**"*

(continued cooperating informally, *but following its content as to the parties' rights and duties*) **opens a door** for the other side. In a later dispute it can rely on a clause of the expired contract (for example § 9 on transfer of copyright, a penalty clause, or non-solicitation) and argue that *"the parties followed that contract's content, so this clause applied too"*.

**How the damage happens.** You literally confirm, in the preamble of the new contract, that the clauses of the earlier (formally expired) contract applied in the disputed period, without the client knowing this concession matters for the dispute.

### Operating rule

In the preambles of settlements and new contracts, **describe facts, not legal regimes**, for the period after the earlier contract expired. Three safe variants, from strongest to weakest:

1. **Silence about the regime:** *„po wygaśnięciu [poprzedniej umowy] Strony kontynuowały współpracę bez zachowania formy pisemnej."* Full stop.
2. **Operational detail:** *„…w odniesieniu do operacyjnych zasad wykonywania świadczeń"*. It points to *how* (division of work, billing model) without reaching for the legal *what* (copyright, penalties, non-solicitation).
3. **Express exclusion (when you want to exclude it outright):** *„…bez przyjęcia w całości postanowień [poprzedniej umowy] jako podstawy dalszych zobowiązań."* The strongest, but confrontational, and it may draw objections from the other side.

### Related phrases to avoid

- *„zgodnie z dotychczasową praktyką wynikającą z [poprzedniej umowy]"*: as above.
- *„kontynuowali stosunek na dotychczasowych zasadach"*: ambiguous; which rules?
- *„zgodnie z postanowieniami [poprzedniej umowy], które w odpowiednim zakresie znajdują dalsze zastosowanie"*: switches on the back door directly.

### Anti-pattern 2: direct references to sections of the expired contract in substantive clauses

W8 covers not only the **preamble** but also substantive clauses (scope, remuneration, obligations). The anti-pattern can return through specific references:

> ❌ *„obejmuje wyłącznie odpłatne udostępnianie Materiałów… w formule odpłatnej emisji zgodnej **z dotychczasową praktyką Stron oraz § 1 [wygasłej Umowy]**;"*

Two problems in one sentence:

1. **„§ 1 [wygasłej Umowy]".** It literally switches on a specific clause of the expired contract. Even if § 1 is neutral (the subject matter), the reference signals that the earlier contract is still "in play", which opens the way to relying on other clauses (for example the copyright section).
2. **„dotychczasową praktyką Stron".** See anti-pattern 3 below.

**Operating rule.** In substantive clauses, state the scope **on its own terms and descriptively**. Don't refer to sections of the expired contract, even if they seem neutral. Exception: specific rates or parameters (for example *„według stawek z § [X] [poprzedniej Umowy]"*), where the reference replaces writing out the numbers without switching on a legal regime.

### Anti-pattern 3: „dotychczasowa praktyka Stron" (the parties' practice so far)

> ❌ *„zgodnie z dotychczasową praktyką Stron"* / *„na zasadach dotychczas stosowanych"* / *„w sposób przyjęty pomiędzy Stronami"*

**Why it's dangerous, especially in an open dispute.** You can't be 100% sure what the other side did with the subject matter (for example audiovisual material) **outside the client's knowledge**. They may have shared it more widely, run campaigns, or shared it with partners. Once you write *„dotychczasowa praktyka"* into a new contract or settlement, it becomes **the permitted limit**. In a dispute, the other side can produce correspondence about distribution to partners and argue: *"that was the practice so far, so it's covered by the consent."*

**Operating rule.** Define the scope of permitted use **on its own terms**, through specific features (to whom, where, in which model), not by reference to an unknown or undefined status quo. This matters most when:

- a dispute between the Parties is ongoing or ending,
- one Party had operational control over the subject matter (for example recordings, data, or documentation) and the client doesn't fully know how it was used, or
- the new contract is meant to end the earlier relationship (a settlement or termination agreement).

### Drafting test

Before sending a draft, ask yourself: **"could the other side's lawyer use this phrase to pull a harmful clause out of the expired contract?"** If yes, delete or rephrase it.

See also: `workflows/other-side-review.md` (category 1, unfavourable confirmations).

---

# LAYER 2: KTZR STYLE (from the clause bank)

The specific syntax and terminology patterns used by KTZR. They come from analysing clauses in many types of civil-law contracts, in particular B2B contracts in the IT and SME sectors, service contracts, operational cooperation agreements, dispute-ending agreements, licence agreements, assignments, and premises allocation.

**Visual layer (typography, borders, layout):** see the separate file `legal-design.md`. The default KTZR typography is **Arial 11.5 pt** with **light borders under paragraph titles** (`color: 808080`, `size: 6`). Use it in every document leaving the firm.

## Operating rules (what to use, what to avoid)

### 1. Conditional constructions

**Use:**
- ✅ **„W przypadku"** (in the event of): *„W przypadku naruszenia zakazu non-solicitation Usługobiorca zapłaci karę umowną…"*
- ✅ **„W razie"** (in case of): *„W razie jakiejkolwiek wątpliwości co do charakteru danej informacji…"*

**DON'T use:**
- ❌ **„Jeżeli"** (if): doesn't appear in any KTZR clause.
- ❌ **„Gdy"** (when): doesn't appear.
- ❌ **„O ile"** (provided that): doesn't appear.

> Conclusion: the condition that opens a clause takes the form **„W przypadku [zdarzenia], [strona] [czyni X]"**. It's the basic syntax pattern for conditional clauses at KTZR.

### 2. Obligation construction

**Pattern:** `[Strona] zobowiązuje się do [czynności w bezokoliczniku]` (the Party undertakes to [verb]).

Examples from the bank:
> Usługodawca zobowiązuje się **do świadczenia** na rzecz Usługobiorcy usług informatycznych za pośrednictwem Specjalistów…
>
> Zleceniobiorca zobowiązuje się **do bieżącej weryfikacji** otrzymywanych od Zleceniodawcy dokumentów…
>
> Zleceniobiorca zobowiązuje się **do składania** sprawozdania ze swej działalności.

**Short variant** (when both parties undertake reciprocally): `[Strona A] zleca, a [Strona B] zobowiązuje się do…`

The subject **always comes first in the sentence**, never in the middle:
- ✅ „Usługodawca zobowiązuje się do…"
- ❌ „Do obowiązków Usługodawcy należy…"

### 3. Declaration construction

**Pattern for preambles and context declarations:**

> Strony zgodnie oświadczają, że:
> (i) [oświadczenie 1];
> (ii) [oświadczenie 2];
> (iii) [oświadczenie 3].

**Simpler variant** (one statement): `Strony [zgodnie] oświadczają/postanawiają/ustalają/potwierdzają, że [...]`

### 4. Definitions

**Pattern: „oznacza" (means).**

> „Specjalista" oznacza osobę fizyczną prowadzącą działalność gospodarczą lub współpracującą z Usługodawcą na podstawie umowy cywilnoprawnej, delegowaną, wskazaną lub „skojarzoną" do świadczenia Usług na rzecz Usługobiorcy; Specjalista nie jest pracownikiem ani Usługodawcy, ani Usługobiorcy.

> „Timesheet" oznacza miesięczną ewidencję czasu świadczonych Usług, zatwierdzaną przez obie Strony, której wzór stanowi Załącznik nr 2.

> „Utwór" oznacza każdy rezultat pracy Specjalisty stanowiący utwór w rozumieniu ustawy z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych, w tym kod źródłowy, dokumentację techniczną i oprogramowanie.

> „Informacje Poufne" oznaczają wszelkie informacje techniczne, technologiczne, handlowe, finansowe, prawne i organizacyjne posiadające wartość gospodarczą, przekazane przez Stronę Ujawniającą, niezależnie od formy przekazu oraz niezależnie od tego, czy zostały wyraźnie oznaczone jako poufne.

**Elements of the pattern:**
- Polish typographic quotation marks **„..."** (low opening, high closing). Never straight `"..."`.
- The definition follows the quoted term with **„oznacza"** (or „oznaczają" for a plural term).
- Within one definition, separate sub-definitions with a **semicolon**, optionally followed by a negative closing sentence („Specjalista nie jest pracownikiem ani…").
- References to statutes: **„w rozumieniu ustawy z dnia [data] o [tytuł]"**, the full name with the date, not an abbreviation.

**Note on dashes.** KTZR's original style put a long dash between the quoted term and its definition. This repo's rules ban em and en dashes, so use „oznacza" for every definition. Don't add dashes to contract text.

### 5. Lists

**Default KTZR pattern: Arabic numerals with a bracket, `1) 2) 3)`.** This is the preferred form in the firm's current practice.

> Przedmiotem Ugody jest: 1) rozstrzygnięcie polubowne w przedmiocie roszczeń zgłoszonych w Wezwaniu; 2) udzielenie przez Wykonawcę odpłatnej, ograniczonej czasowo zgody na korzystanie z wizerunku; 3) określenie obowiązków Zamawiającego po zakończeniu okresu.

> Zgoda: 1) obejmuje wyłącznie udostępnianie Materiałów słuchaczom kursów…; 2) nie obejmuje publikacji Materiałów na innych platformach…; 3) nie obejmuje udostępniania Materiałów osobom trzecim.

**Alternative: letters (a) (b) (c).** Acceptable in older archived clauses, and in references to statutory provisions (for example *„art. 6 ust. 1 lit. a RODO"*, where we keep the statutory form).

> …na polach eksploatacji: (a) utrwalanie i zwielokrotnianie; (b) wprowadzanie do pamięci komputera oraz sieci…
> *(old pattern, acceptable when quoting a clause from an existing contract)*

**Roman numerals (i) (ii) (iii):** used only for context declarations after „Strony zgodnie oświadczają, że:".

**Consistency within a document.** Within one contract, use **one numbering system** for lists at the same level. Don't mix `1) 2) 3)` with `(a) (b) (c)` within one paragraph. When renumbering, mixing causes errors such as *„zgodnie z lit. (b)"* when it should be *„zgodnie z pkt 2)"*.

**Separator between items:** a semicolon (`;`), with a full stop only after the last item.

**Internal references:** always use the form that matches the chosen system. For `1) 2) 3)` items, refer to *„pkt 1)"* (not *„lit. 1)"* or *„ust. 1)"*). For letters `(a) (b) (c)`, refer to *„lit. (a)"*.

### 6. References to statutes and to parts of the contract

**To statutes: full name the first time, short form afterwards.**

> …w rozumieniu **art. 22 § 1 Kodeksu pracy**…
> …w rozumieniu **art. 11 ust. 2 Ustawy o zwalczaniu nieuczciwej konkurencji**…
> …w rozumieniu **ustawy z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych**…
> …przetwarzania danych osobowych zgodnie z **art. 28 RODO**…

Pattern: `art. X [§ Y] [ust. Z] [name of the act in the nominative]`. Leave out „ustawy z dnia" for widely known acts (Kodeks pracy, Kodeks cywilny, RODO). Give the full date for less known acts.

**To parts of the contract:**

> …Załącznik nr 2.
> …roszczeń opisanych **w § 1**…
> …wykonania **ust. 1 i 2**…
> …**art. 6 ust. 1 lit. a**…

**DON'T use** „o którym mowa w" (referred to in). It doesn't appear in the bank. The pattern is **„opisanych w § X"** / **„wskazanych w § X"** / **„określonych w § X"**.

### 7. Linking phrases

**Use often:**
- ✅ **„w rozumieniu"** (within the meaning of): for references to statutory definitions
- ✅ **„w szczególności"** (in particular): for open lists, when the list is illustrative
- ✅ **„w zakresie"** (in respect of): to set a field of action
- ✅ **„niezależnie od"** (regardless of): to exclude limits
- ✅ **„nie później niż"** (no later than): for final deadlines
- ✅ **„zgodnie z"** (in accordance with): for procedural references

**DON'T use:**
- ❌ **„z wyłączeniem"** (excluding): 0 occurrences
- ❌ **„z wyjątkiem"** (except): 0 occurrences
- ❌ **„bez uszczerbku dla"** (without prejudice to): 0 occurrences, an Anglo-Saxon import
- ❌ **„z zastrzeżeniem"** (subject to): 1 occurrence, marginal

If you need to express an exclusion, **rephrase the sentence** instead of looking for a qualifying phrase. For example, instead of *„X, z wyłączeniem przypadków określonych w § 5"*, write *„X. Powyższe nie dotyczy przypadków określonych w § 5."*

### 8. Party names: how KTZR applies the craft

> **The governing rule is W4 above:** choose the pair of party names from the dominant legal type of the relationship, not by style. This section shows what that looks like in actual KTZR practice.

Pairs from the clause bank (illustrations of the rule, not the rule itself):

| KTZR contract type | Pair used | Follows from |
|---|---|---|
| IT body leasing | **Usługodawca / Usługobiorca** | Contract for services (art. 750 KC) |
| Accounting services | **Zleceniodawca / Zleceniobiorca** | Contract for services (art. 750 KC with art. 734) |
| NDA | **Strona Ujawniająca / Strona Otrzymująca** | Innominate contract (art. 353¹ KC); functional names |
| Assignment | **Cedent / Cesjonariusz** | Assignment of receivables (art. 509 KC) |
| Commission-based cooperation (B2B) | **Zleceniodawca / Partner** | Services plus the intermediary's unique role |
| Framework carriage agreement | **Zamawiający / Przewoźnik** | Contract of carriage (art. 774 KC) |
| Licence and advisory agreement | **Licencjodawca / Licencjobiorca** | Parties with unique roles; category names |

**Pattern for the generator:**
1. First map the **dominant legal type** of the relationship (essentialia, step 1).
2. Take the matching pair of names from the table in W4.
3. If one party has a clearly unique category role (Specjalista, Partner, Klient, Przewoźnik), add that name to the pair.
4. Keep the pair **throughout the contract**, even though individual paragraphs cover different parts of the relationship.

**KTZR anti-patterns:**
- ❌ Reaching for "Wykonawca / Zamawiający" by default, whatever the contract type. Those names come from public procurement and construction contracts. They aren't the default for every IT contract.
- ❌ Changing the pair mid-contract (for example "Usługodawca / Usługobiorca" in §§ 1 to 5 and "Zbywca / Nabywca" in § 6 on transfer of rights). One contract, one main pair.
- ❌ Mixing the common and the literal statutory form ("Zleceniobiorca" in one section and "Przyjmujący zlecenie" in another for the same party). Pick one and use it consistently.

### 9. Clause length and structure

**KTZR statistics:** the average clause is **215 characters and 1.4 sentences**. The median is 213 characters.

- A short clause (1 sentence, 1 idea) is the dominant pattern.
- A medium clause (2 to 3 sentences) is used for obligations with consequences.
- A long clause (over 400 characters) only for declarations about the nature of the contract or for complex definitions.

**DON'T write** "monster" clauses with 5 or more nested conditional sentences. If a clause grows past 350 characters, **split it into separate sections**.

### 10. Latin and archaisms

**Latin in contract clauses: ZERO.**

Across all 92 KTZR clauses there isn't a single occurrence of:
- "essentialia negotii"
- "lucrum cessans"
- "dolus" / "culpa"
- "ex contractu" / "ex delicto" / "ex lege"

**Operating conclusion.** At KTZR, Latin lives in **legal commentary, analysis, and internal discussion**, NOT in the contract text signed with the client. To express "essentialia negotii" in a contract, write it in Polish: „elementy konieczne umowy". For "lucrum cessans", write „utracone korzyści".

### 11. Negations and exclusion clauses

**Pattern that opens a negation: „Żadna ze Stron nie…"** (neither Party…) (2 occurrences):

> Żadna ze Stron nie [jest uprawniona/zobowiązana/może...]

**Pattern that excludes a regime:**

> Udostępnienie lokalu Zleceniobiorcy na mocy niniejszego Przydziału **nie jest** umową najmu ani dzierżawy w rozumieniu przepisów Kodeksu cywilnego ani nie podlega przepisom ustawy z dnia 21 czerwca 2001 r. o ochronie praw lokatorów.

> Umowa **nie kreuje** stosunku pracy w rozumieniu art. 22 § 1 Kodeksu pracy.

Construction: `[act/document] nie jest/nie kreuje/nie podlega [...] w rozumieniu [...]`. In Polish, short, with a reference to the legal basis.

### 12. Preambles with historical context

**Pattern „ZWAŻYWSZY, ŻE: A. … B. … C. …"** (WHEREAS, in capitals, then letters):

> ZWAŻYWSZY, ŻE:
> A. Licencjodawca jest organizacją posiadającą specjalistyczną wiedzę…
> B. Licencjobiorca jest podmiotem zainteresowanym…
> C. …
> D. Licencjobiorca jest zainteresowany uzyskaniem licencji…

Use it when the contract needs grounding in earlier relations or facts, or an explanation of the parties' intent. Simple contracts (simple B2B, NDA, assignment) don't need a preamble.

### 13. Negative definitions that exclude

**Pattern: „X w rozumieniu Umowy [JEST/NIE jest] Y. [Y nie jest:] [list]"**

> Klientem w rozumieniu niniejszej Umowy Ramowej jest podmiot, z którym Zleceniodawca zawrze Umowę Inwestycyjną za pośrednictwem usług świadczonych przez Partnera. Klientem nie jest: podmiot z którym Zleceniodawca nawiązał współpracę lub kontakt przed otrzymaniem informacji o tym podmiocie od Partnera.

A definitional pattern of "affirmation plus negation by list". Very useful in commission, exit, and non-solicitation clauses.

### 14. Typography

- **Quotation marks:** always Polish typographic `„..."` (low opening, high closing).
- **Dashes:** don't use em or en dashes in contract text. Use „oznacza" in definitions, commas for asides, and a hyphen only in numeric ranges (for example „5-10 dni").
- **Semicolon (;):** to separate list items and sub-definitions.
- **Colon (:):** to open a list after „co następuje", „Strony oświadczają, że:", or „Przedmiotem Umowy jest:".
- **Capital S for the Parties:** „Strony", „Strona". Always capitalised, because it's a contractual definition.
- **Capitals for defined terms:** always (for example „Umowa", „Specjalista", „Utwór", „Informacje Poufne", „Załącznik nr X").

### 15. Model paragraph openings

**Top 3 openings in the KTZR bank** (most often repeated):

1. **„Zleceniobiorca ponosi pełną odpowiedzialność za…"** (3 times): liability paragraphs
2. **„[Strona] zobowiązuje się do…"** (4 times in total): obligation paragraphs
3. **„Żadna ze Stron nie…"** (2 times): paragraphs on mutual restrictions

**Less frequent openings:**
- „Strony zgodnie oświadczają, że:": preambles and clauses on the nature of the contract
- „Umowa ma charakter…": clauses that classify the contract type
- „Zawarcie niniejszej Umowy nie stanowi…": clauses that exclude effects
- „Niniejsza umowa ramowa określa…": preambles of framework agreements

### 16. Form of legal acts in electronic dealings

**Hierarchy of forms. Apply it deliberately:**

| Term | Basis | What it means | Requirement |
|---|---|---|---|
| **forma pisemna** (written form) | art. 78 KC | handwritten signature | a handwritten signature |
| **forma elektroniczna** (electronic form) | art. 78¹ KC | equivalent to written form | a qualified electronic signature (KPE) |
| **forma dokumentowa** (documentary form) | art. 77² KC | a document plus identification of the person | no signature; an email, or a system log with confirmation |
| **postać elektroniczna** (electronic format) | none | the medium or format (PDF, email body) | none; describes the medium only |
| **droga elektroniczna** (by electronic means) | art. 2 pkt 5 u.ś.u.d.e. | the transmission channel | none; a communication channel only |
| **a click with no trace** | none | a factual act | outside KC |

**Operating rule: never use „drogą elektroniczną" as a standalone form clause.**

❌ *„wypowiedzenie złożone drogą elektroniczną"* (notice given by electronic means). Ambiguous: „droga elektroniczna" is a channel (u.ś.u.d.e.), not a form under KC, and a reader may confuse it with electronic form (KPE).

✅ Always name the channel:

| Intent | Correct wording |
|---|---|
| Plain email | *„wiadomością e-mail na adres [___]"* |
| Panel or system | *„za pośrednictwem panelu Konta (system generuje potwierdzenie e-mail)"* |
| Email or letter | *„wiadomością e-mail na adres [___] albo w formie pisemnej na adres siedziby"* |

Use *„drogą elektroniczną"* only where the Act on Providing Services by Electronic Means (u.ś.u.d.e.) uses the term directly, because there it's a technical term, not a form clause.

**„Forma dokumentowa" and clicks:**
- A click alone is a factual act, not a declaration *in the form of a document* (art. 77³ KC).
- A click plus an automatic confirmation email is documentary form (the email is the medium).
- A click plus a system log identifying the user is probably documentary form.
- Accepting terms with a checkbox is enough for u.ś.u.d.e. (art. 8), whatever its classification under KC.

### 17. Definitions: how to define correctly in terms of service

**No tautology:**

❌ *„Serwis" oznacza serwis internetowy dostępny pod adresem…*
This defines the term by itself.

✅ *„Serwis" oznacza platformę dostępną za pośrednictwem sieci Internet pod adresem [___], za pośrednictwem której Usługodawca świadczy Usługi.*
A functional description that doesn't repeat the defined word.

**Platform or service: always add access through the Internet.** The phrase *„dostępny za pośrednictwem sieci Internet"* specifies the access medium, and it matters for classification as a service provided by electronic means under u.ś.u.d.e.

**Service recipient: tie it to an act, not to accepting the terms:**

❌ *podmiot, który zawarł umowę na podstawie niniejszego Regulaminu*
„Na podstawie Regulaminu" doesn't describe a legal relationship. The terms are a standard form, not a legal basis.

✅ *podmiot, który zawarł Umowę ramową przez rejestrację Konta i akceptację Regulaminu*
A specific act of entering the relationship (registering, or placing an order).

**Journal of Laws, consolidated text.** At the first reference to a less known act, or when the wording of the consolidated text matters, add *t.j. Dz. U. z [rok] r. poz. [numer] ze zm.* This applies in particular to u.ś.u.d.e., u.p.k., and the act on the protection of tenants' rights.

---

## How to use this file

**Hierarchy.** If rules conflict, apply them in this order:
1. **KTZR golden rules** (`golden-rules.md`)
2. **Essentialia negotii requirements** for the contract type (`essentialia-map.md`)
3. **Layer 1, lawyer's craft** (sections W1 to W8 in this file), because it's general craft that applies to every contract
4. **Layer 2, KTZR style** (sections 1 to 17 in this file), the firm's specific patterns

**How to work with it:**

1. **Before writing a clause:** map the contract's legal type. Take the pair of party names from W4. Reserve **§ Definicje** for all industry and technical terms that will appear.

2. **While writing:** check as you go. Does the clause answer WHO, WHAT, WHEN, HOW (W1)? Is every technical word defined (W3)? Do pronouns create ambiguity (W2)?

3. **After writing:** go through the clause word by word:
   - Every industry word: is it defined in § Definicje?
   - Every deadline: is it specific („nie później niż w terminie X dni", not „niezwłocznie" alone)?
   - Every „odpowiednio", „stosownie", or „w miarę możliwości": delete or make precise?
   - Conditional construction: „W przypadku" or „W razie" (not „Jeżeli")?
   - Pair of party names: consistent with the dominant legal type?
   - Lists: `1) 2) 3)` by default (the KTZR pattern); `(a)(b)(c)` only when the client requires it, or in a mixed contract with an external document?
   - Quotation marks: typographic `„..."`?

4. **Anti-patterns to fix at once**, wherever you find them in generated text:
   - „Jeżeli…, to…" → rewrite as „W przypadku…, [strona]…"
   - „niezwłocznie" without a number → add „nie później niż w terminie X dni/godzin"
   - „odpowiednio" / „stosownie" → make the scope precise
   - „z wyłączeniem" / „bez uszczerbku dla" → rephrase
   - Latin („essentialia negotii", „lucrum cessans") in clause text → Polish
   - The pair „Wykonawca/Zamawiający" in a services contract (for example IT body leasing) → per W4, for example „Usługodawca/Usługobiorca"
   - Straight quotes `"..."` → Polish typographic `„..."`
   - An industry or technical term (API, SLA, maintenance, CI/CD, uptime, deployment) without a definition in § Definicje → add a definition or rewrite the clause
   - „Wykonawca dostarczy raport. Ten zostanie zweryfikowany…" (referring pronouns) → repeat the subject
   - **The same rule in two places in the contract** (W5) → keep one place, and put a reference („zgodnie z § X") in the other
   - **A reference to KC, PrAut, or KP with no legal function** (for example „zgodnie z art. 355 § 1 KC" for the general standard of care, or „w sprawach nieuregulowanych stosuje się KC" in the final provisions) (W6) → delete or rephrase
   - **„Strony zawierają umowę na podstawie art. 750 KC…"** in the preamble or § Przedmiot. The reference is unnecessary, because the type follows from the content (W6) → delete the reference
   - **„drogą elektroniczną"** as a form clause for a declaration (notice, complaint, demand) → always a specific channel: „wiadomością e-mail na adres [___]" or „za pośrednictwem panelu Konta" (section 16)
   - **„w formie elektronicznej"** for a plain email or click → art. 78¹ KC requires a KPE; use „wiadomością e-mail na adres [___]" or „w postaci elektronicznej" (section 16)
   - **A tautological definition** (for example „Serwis" oznacza serwis internetowy…) → rewrite as a functional description without the defined word (section 17)
   - **„Usługobiorca" defined by accepting the Terms** without the act of entering the relationship → tie it to registration or placing an order (section 17)
   - **„Licencja na przetwarzanie danych"** (a licence to process data) → no such construction exists; personal data → DPA (art. 28 RODO); protected content → a declaration of rights to the content (see `clause-bank/20-regulamin-usdde-aup.md`)
   - **An em or en dash** anywhere in the contract text → replace it per section 14

---

## Future iterations

Layer 2 (KTZR style) is a starting point, taken from the clause bank across the contract types the firm handles. **It should grow** as new contract types are added to the bank. Each new contract brings:
- New party names, if unique. Add them to the table in section 8.
- Possibly new syntax patterns, if they repeat systematically.
- New preamble constructions, if specific to the contract type.

Layer 1 (lawyer's craft) is stable. It holds general craft rules, independent of how many contracts are in the bank. Add to it only rules the agent turns out to skip systematically (for example "after writing a remuneration clause, always check that you gave the currency"). Such a check then becomes a permanent rule of the craft here.

When you extend the skill, run new clauses through the same analysis and extend layer 2.
