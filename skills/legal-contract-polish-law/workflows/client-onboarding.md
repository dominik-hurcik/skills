# Workflow: client onboarding (cold start)

> _Global rules: `references/core-rules.md` (R1 citing · R2 gate · R3 roles · R4 profile · R5 format)._

**Purpose:** a quick, structured interview with a new client (10 to 15 minutes) that produces a *client profile* the agent uses in later work on their matters. The profile helps put recommendations in context. Without it, the agent works on a *generic B2B* basis, which usually gives worse results than the client's real profile.

**Inspiration:** the *cold-start interview* in Anthropic's `claude-for-legal` (commercial-legal, employment-legal), adapted to the Polish B2B IT and SME market.

**Triggers:** a new client of the firm, *"onboarding"*, *"client profile"*, *"first conversation with a client"*, *"set up the agent for a specific client"*, *"save the client's preferences"*.

**Output:** a file `profile/klient-[working-name].md` in the user's private folder (gitignored, never committed to a public repo). The profile is a *living document* that is updated as the work goes on.

**Caveat:** the interview is informative and operational for the firm's work. It doesn't replace legal advice on the client's specific matters. The profile puts recommendations in context. It doesn't generate legal decisions automatically.

Ask the interview questions in the language the user works in with the client. The examples below are in English.

## Interview structure (10 to 15 minutes)

The interview has 6 sections of 1 to 3 minutes each. The questions can come in any order. What matters is having material for every profile section at the end.

### Section 1: the client's business (2 to 3 minutes)

Questions:

1. *"What does your company do commercially?"* (sector, business model)
2. *"What stage is the company at?"* (pre-seed, seed, series A+, mature, corporation)
3. *"What's the scale?"* (headcount, annual revenue, number of counterparties)
4. *"Do you operate locally, regionally, nationally, or internationally?"*
5. *"Are there regulatory constraints in your industry?"* (KSC/NIS2, special GDPR rules, MiFID, MAR, health, energy, education)

**What it means for the agent:** the sector and stage set the default tone of voice (formal or partner-like), the level of detail (a startup wants it short, a corporation wants documentation), and the regulatory context.

### Section 2: typical matters and counterparties (2 to 3 minutes)

Questions:

1. *"Which contract types do you deal with most often?"* (NDA, body leasing, implementations, licences, SaaS, distribution, agency, employment, B2B)
2. *"Who are your typical counterparties?"* (sector, scale: large enterprises, mid-size B2B, small businesses, consumers)
3. *"Are there counterparties you work with regularly?"* (and what they're like: *"usually aggressive"*, *"usually reasonable"*, *"always try to slip in X"*)
4. *"Do you have your own contract template, or do you usually work on the other side's?"*

**What it means for the agent:** it can suggest clause types typical for the client's industry. Knowing *who sits across the table* helps choose the contract's tone (aggressive or conciliatory).

### Section 3: risk preferences (2 to 3 minutes)

Questions:

1. *"How would you describe your tolerance for legal risk?"* (conservative, balanced, aggressive)
2. *"Have you had court or arbitration disputes?"* (which, with what result)
3. *"Do you have a policy on typical risk clauses?"* Liability cap, indemnity, contractual penalties, non-compete.
4. *"Are there clauses you never accept?"* (deal breakers)
5. *"Are there clauses you always insist on in your contracts?"* (must-haves)

**What it means for the agent:** the client's appetite for risk shapes the recommendations. A *conservative* client gets stricter protective clauses. An *aggressive* client gets contracts with elements of negotiating pressure.

### Section 4: escalation and decisions (1 to 2 minutes)

Questions:

1. *"Who decides on contracts on your side?"* (CEO, CFO, Head of Legal, founder)
2. *"Above what threshold does a matter need the decision-maker?"* (an amount, impact on the business, time)
3. *"Who should be kept in the loop on matters about your company?"* (besides the main contact, for example the accountant on tax questions, the IT manager on implementations)
4. *"Which firms or advisers do you work with in other areas?"* (if relevant, for example a notary for real estate, a tax adviser)

**What it means for the agent:** it can flag that a matter needs escalation to the decision-maker or a consultation with another adviser, and it knows whom to cite as *"as agreed with person X"*.

### Section 5: communication style and format (1 to 2 minutes)

Questions:

1. *"What communication style do you expect from the firm?"* (formal, partner-like, or partner-like with formality on important matters)
2. *"Do you prefer written communication (email, DMS) or spoken (phone, video)"* for day-to-day matters?
3. *"What format do you expect for documents?"* Word (.docx), PDF, or both; a classic look (Times New Roman) or a more modern one (Arial); preferences on contract typography.
4. *"Do you use legal design (key-terms tables, a table of contents, diagrams)?"* See `references/legal-design.md`.
5. *"Do you want technical explanations (clauses with commentary), or clean contracts with no meta-commentary?"*

**What it means for the agent:** it adapts generated documents to the client's typography and communication preferences. An *old-school* client gets Times 12. A *modern* client gets Arial 11.5 with legal design.

### Section 6: specific clauses and contexts (1 to 2 minutes)

Questions:

1. *"Do you have your own clause templates you want to use?"* (for example your own confidentiality, GDPR, or liability clause)
2. *"Are there areas with an internal policy you won't negotiate?"* (for example *"our MFN clause always applies"*)
3. *"Are there technology or industry areas the agent should know about?"* (for example *"we always work with open source, so IP clauses must account for copyleft licences"*)
4. *"Are there areas you never get involved in?"* (for example *"we never take contracts with the gambling, military, or crypto sectors"*)

**What it means for the agent:** the client's *hard rules* are not up for debate. The agent applies them without questioning them. *Soft preferences* can be negotiated in specific matters.

## Output: client profile structure

After the interview, the agent writes the file `profile/klient-[name].md` (private, never published) with this structure:

```markdown
# Client profile: [Name]

**Status:** working version after onboarding on [date]
**Updated:** [date of last update]

## Section 1: Business profile
- Sector: [...]
- Scale: [...]
- Stage: [...]
- Reach: [...]
- Regulatory constraints: [...]

## Section 2: Typical matters and counterparties
- Most frequent contract types: [...]
- Typical counterparties: [...]
- Regular relationships (and what they're like): [...]
- Own template or theirs: [...]

## Section 3: Risk profile
- Tolerance: [conservative / balanced / aggressive]
- Dispute history: [...]
- Policies on typical clauses:
  - Liability cap: [...]
  - Indemnity: [...]
  - Contractual penalties: [...]
  - Non-compete: [...]
- Deal breakers: [...]
- Must-haves: [...]

## Section 4: Escalation
- Decision-maker: [...]
- Escalation threshold: [...]
- Stakeholders to inform: [...]
- Other advisers: [...]

## Section 5: Communication and format
- Style: [...]
- Day-to-day channel: [...]
- Document format: [...]
- Legal design: [yes / no / only for X]
- Comments in documents: [yes / no]

## Section 6: Specific clauses and contexts
- Own templates: [...]
- Hard rules: [...]
- Technology or industry contexts: [...]
- Excluded industries: [...]

## Matter history (updated over time)
- [date], [short description of the matter], [result / status]

## Additional notes
[ad hoc notes after conversations]
```

## Operating rule: how to use the profile

1. **Before every new matter**, the agent reads the client profile to put its recommendations in context.
2. **After every significant matter**, the agent or the lawyer handling it updates *Matter history*. Over time the profile gets richer.
3. **Every 6 to 12 months**, review the profile with the client (a short 15 to 20 minute check-in). Preferences can change as the company grows.

## Operating rule: when to run onboarding

- ✅ A new client of the firm (the first 1 or 2 matters)
- ✅ An existing client whose matters haven't been handled with the agent before
- ✅ A significant change at the client (new management, a new funding round, a new business model)
- ❌ A regular client with a current profile (updated within the last 12 months)

## Links within the skill

- `references/golden-rules.md`: the KTZR golden rules, unchanged whatever the client profile
- `references/drafting-style.md`: the KTZR style, unchanged; the client profile adjusts its *intensity* (for example whether we use legal design)
- `references/legal-design.md`: choosing *"classic-clean"* or *"light legal design"* depends on the client profile (section 5)
- `workflows/quick-triage.md`: triage can take the client profile into account (RED signals for a conservative client may be YELLOW for an aggressive one)
- `workflows/full-review.md`: a full analysis always takes the client profile into account

## Final caveat

The client profile is *a working tool for the firm*, not a commitment to the client. Decisions on specific matters are always made in the context of the current situation, whatever general preferences the profile records. The profile makes the work easier. It doesn't replace it.
