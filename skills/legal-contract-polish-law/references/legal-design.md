# Legal design at KTZR

**Source:** legal design standards developed by the firm, based on the literature (Hagan, Haapio, Passera) and the WorldCC Contract Design Pattern Library. Adapted to the firm's profile (B2B IT, not consumer, not startups).

**Purpose:** decide **which legal design elements KTZR adopts** and which are outside its profile. It isn't about "decorating contracts". It's about selected techniques that improve readability while keeping the professional tone of a legal document.

## TL;DR

1. **Legal design ≠ decoration.** It's a method of designing documents for their real user (a business client), not for another lawyer.
2. **WorldCC Pattern Library** (https://contract-design.worldcc.foundation): open source, 10 pattern families. The main operational source.
3. **KTZR adopts 5 families fully** (Layout, Navigation, Emphasis, Organizing, Tone of voice), **3 selectively** (Summarizing, Layering, Visuals, only when they really help), and **drops or keeps 2 internal** (Reviewing, and Explainers in normative text).
4. **Default KTZR typography:** Arial 11.5 pt for the body, light borders under paragraph titles, justified body text. Times New Roman only when the client explicitly asks for a "classic" look.
5. **5 questions for every contract** decide whether to add a key-terms table, a table of contents, a timeline, or an explainer box.
6. **Anti-patterns are always out:** comic contracts, coloured diagrams in normative text, icons replacing text, emoji.
7. **The KTZR "light legal design" standard** = a classic legal structure + selected visual elements that improve readability, without breaking the professional tone.

## Default KTZR typography

Use these settings **in every document leaving the firm**, unless the client asks for another standard.

### Font

| Element | Font | Size | Weight |
|---|---|---|---|
| Body text | Arial | 11.5 pt | Regular |
| Document title (POROZUMIENIE, UMOWA, and so on) | Arial | 16-18 pt | Bold |
| Subtitle (legal classification) | Arial | 12 pt | Bold |
| Paragraph titles (§ X. Name) | Arial | 12 pt | Bold |
| Numbering of letter or number lists | Arial | 11.5 pt | Regular |

**Exception:** if the client explicitly asks for a "classic" look (Times New Roman), use Times New Roman 12 pt, with the same structure and borders.

### Borders

| Element | Border | Colour | Size |
|---|---|---|---|
| Under a paragraph title (§ X. Name) | bottom | `808080` (mid grey) | 0.75-1 pt |
| Under the document title | bottom | `808080` | 1 pt |
| Tables („Kluczowe warunki", summaries) | all | `CCCCCC` (light grey) | 0.5 pt |

Principle: **subtle and monochrome**. Never use colours outside greyscale in the body of a contract. Colours only in supporting tables, and only if the client explicitly ordered fuller legal design.

### Layout

- Margins: 2.5 cm on all sides (1 inch is also fine).
- Justified body text: yes, for most paragraphs. Centred only for titles and section headings.
- Spacing: 6 pt after each paragraph. Line spacing 1.25.
- Lists: hanging indent for (a)(b)(c) and for numbered 1./2./3. lists.

## The 10 WorldCC pattern families, filtered for KTZR

A map of all the families in the Passera and Haapio library, with the KTZR decision for each.

| Family | What it does | KTZR decision | What it means for us |
|---|---|---|---|
| **Emphasis** | Highlights key information | ✅ adopt | Bold for amounts, dates, deadlines, and account numbers. **A bottom border** under paragraph titles. Italics for definitions in typographic quotes „..." |
| **Layout** | Arranges content for readability | ✅ adopt | White space, short paragraphs, hanging indents. Arial 11.5 pt, 2.5 cm margins |
| **Navigation** | Helps people find things | ✅ adopt | A table of contents for contracts over 5 pages (auto-generated). **Live cross-references** instead of typed ones |
| **Organizing** | Structures content logically | ✅ adopt | Clauses in the chronological order of the relationship, not alphabetically. Definitions first, final provisions last |
| **Tone of voice** | Words, tone, perception | ✅ adopt | Plain Polish, active voice, short sentences (W1/W2 of the KTZR style) |
| **Summarizing** | Summarises | ⚖️ selectively | A „Kluczowe warunki" (key terms) table at the start. Only for contracts over 3 pages, or when a business client reads it |
| **Layering** | Puts what matters on top | ⚖️ selectively | Move technical and operational clauses to annexes so the body stays readable |
| **Visuals** | Images that aid understanding | ⚖️ selectively | A timeline for phased projects (IT implementation, milestones). A RACI table for division of responsibility. A swimlane for multi-party processes. **Only when they really explain the structure** |
| **Explainers** | Explains what clauses mean | ⚠️ with care | „Wyjaśnienie" (explanation) boxes only for unusually counter-intuitive clauses (liability cap, intentional fault, indemnity), when the client signals they don't understand |
| **Reviewing** | Checks completeness | 🏠 internal | Checklists for our team (`workflows/`). We don't put them in outgoing documents |

## 5 questions for every contract

Before sending a contract to the client or counterparty:

1. **Is the contract over 3 pages?** Yes → add a table of contents (Word: `Insert → Table of Contents`).
2. **Does it contain key parameters a business client would want to see at once?** Yes → a „Kluczowe warunki" table at the start (parties, subject, remuneration, term, main obligations).
3. **Does it describe a multi-stage process?** Yes → consider a timeline (phase 1 → 2 → 3) or a swimlane (who does what, when).
4. **Does it contain technically complex clauses the reader probably won't understand?** Yes → a short explainer box next to them (at most 2 to 3 sentences in plain Polish).
5. **Are the cross-references live (clickable) in Word?** No → change them to hyperlinks, because static text like „§ 5 ust. 2" becomes an error after renumbering.

If the answer to questions 1 to 4 is "no", the contract stays in the **classic KTZR style** (Arial 11.5, a bottom border under each §, no extra visual elements).

## Specific techniques, step by step

### A. „Kluczowe warunki" table (Summarizing)

**When:** contracts over 3 pages, every settlement, IT implementation contracts, framework agreements with many orders.

**Where:** right under the document title, before or after the parties' details, depending on convention.

**Structure (minimal, 2 columns):**

```
| Strony                  | Wykonawca: [Nazwa] / Zamawiający: [Nazwa]   |
| Przedmiot               | [Krótko, 1 zdanie]                          |
| Wynagrodzenie           | [Kwota / mechanizm rozliczenia]             |
| Czas trwania            | [Daty lub okres]                            |
| Najważniejsze terminy   | [Np. terminy płatności, data wygaśnięcia]   |
| Sąd właściwy            | [Miejscowość]                               |
```

**Nature:** informative, not normative. The paragraphs are what bind. If someone asks, we can add the clause „Tabela ma charakter wyłącznie informacyjny" (the table is for information only) to the final provisions, but we don't by default, because it's unnecessary and obvious.

### B. Table of contents (Navigation)

**When:** contracts over 5 pages.

**How:** Word → `Insert → Table of Contents` → pick an automatic template and set the font to Arial 11.5. The paragraph titles must use *Heading 2* (or a matching style).

### C. Process timeline (Visuals)

**When:** contracts for multi-phase projects (IT implementation, construction, migration). For a settlement with 3 instalments it *isn't worth it*: a table of instalments is enough.

**How:**
- Word: `Insert → SmartArt → Process` → a horizontal template with 3 to 7 stages.
- Each stage = a short name (1 to 3 words) + a date or milestone.
- No icons, monochrome (greys, or one accent colour matching the client's branding).

### D. Swimlane (Visuals)

**When:** multi-stage processes involving more than 2 parties (for example IT body leasing: Zamawiający / Usługodawca / Specjalista).

**How:** SmartArt → a diagram with rows for the parties and columns for the phases, with flow arrows between rows.

### E. Explainer box (Explainers)

**When:** rarely, only when a clause is technically complex and the client explicitly signals they don't understand it.

**Structure:**
```
┌─────────────────────────────────────────────┐
│ Wyjaśnienie (charakter informacyjny):       │
│ [2-3 zdania plain Polish, co klauzula       │
│ oznacza w praktyce]                         │
└─────────────────────────────────────────────┘
```

**Nature:** informative, not normative. Keep the box visually separate from the clause (for example a 1×1 table with a light border, in 10.5 pt italics).

### F. Bottom border under paragraph titles (Emphasis + Layout)

**Purpose:** a subtle separation of title and body that makes the document easier to scan.

**Implementation (Word):**
- Select the paragraph with the title (§ X. Name).
- `Paragraph → Borders → Bottom Border` → colour `808080`, width 0.75 pt.
- Alternatively, in the style definition: `pBdr → bottom`.

**Implementation (docx-js):**
```javascript
new Paragraph({
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "808080", space: 4 } },
  children: [new TextRun({ text: "§ X. Tytuł", bold: true })]
})
```

## Anti-patterns: what we avoid

- **Comic contracts** (cartoon illustrations replacing the text). Used in South Africa for workers who can't read. Not our profile.
- **Coloured diagrams in normative text.** It looks like a presentation, not a legal document.
- **Icons instead of text in clauses.** An icon can be an accent in a key-terms table (if the client requires it), but it never replaces normative text.
- **Emoji:** in no document leaving the firm.
- **Too much bold:** if everything is emphasised, nothing is. Keep bold for amounts, dates, and key obligations.
- **Two different fonts in one document** (except cases like Arial for the body and Courier for code in a technical annex). Stick to one.
- **Table borders darker than the text:** it looks like graph paper. Always light grey (`CCCCCC` or lighter).

## When to use "light legal design"

By default KTZR works in **"classic-clean"** mode: no key-terms table and no timelines, but with our default typography (Arial 11.5 + bottom border + plain Polish).

Switch to **"light legal design"** when **at least one** of these is true:

- The contract is over 5 pages and the reader is a business person (not the other side's lawyer).
- The contract describes a multi-stage process with milestones.
- The client explicitly asks for legal design or a "user-friendly" document.
- Teams will use the contract operationally (it won't just be signed and filed).

**"Full legal design"** (colours, icons, infographics): **we don't do it at KTZR**. If the client needs it, we refer them to specialised design-focused firms.

## Doctrinal and operational sources

### Operational (pattern libraries)

- **WorldCC Contract Design Pattern Library:** https://contract-design.worldcc.foundation (Stefania Passera, Helena Haapio). Open source, 10 pattern families with examples from Shell, Airbus, Juro, and others.
- **Open Law Lab:** https://www.openlawlab.com (Margaret Hagan). Blog and resources.
- **Stanford Legal Design Lab:** https://www.legaltechdesign.com.

### Doctrinal (publications)

- **Hagan, M.** (2020), "Legal Design as a Thing: A Theory of Change and a Set of Methods to Craft a Human-Centered Legal System", *Design Issues* 36(3).
- **Hagan, M.**, *Law by Design*: https://www.lawbydesign.co (online, open).
- **Haapio, H. & Passera, S.** (2021), "Contracts as interfaces: Exploring visual representation patterns in contract design", in: *Legal Informatics*, Cambridge University Press, pp. 213-238.
- **Haapio, H. & Hagan, M.** (2016), "Design Patterns for Contracts", *Proceedings of the 19th International Legal Informatics Symposium IRIS 2016*. SSRN: 2747280.
- **Corrales Compagnucci, M., Haapio, H., Hagan, M. & Doherty, M.** (eds.) (2021), *Legal Design*, Edward Elgar Publishing.

## Links within the skill

- `drafting-style.md`: W1 to W8 (lawyer's craft) and the KTZR style. The default KTZR typography (Arial 11.5 + borders) extends layer 2.
- `golden-rules.md`: the KTZR golden rules (1 and 12). Legal design doesn't change these rules.
- `clause-bank/`: clause patterns. The visual layer is *independent* of clause content. It's how we *present* clauses, not *what* we write in them.
