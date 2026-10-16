# KTZR format checklist

Ten points to check before generating or returning any document. A quick filter for `legal-design.md` and `drafting-style.md`. The points apply to the Polish contract text.

---

## Checklist

| # | Rule | Test |
|---|--------|------|
| 1 | **Quotation marks** | Polish „…" only. Not English "…" or «any others». |
| 2 | **No dashes** | No em or en dashes in contract text. Definitions use „oznacza". Asides use commas. A hyphen only in numeric ranges such as „5-10 dni". |
| 3 | **Amounts and penalties** | In figures and in words: `18.000,00 zł (słownie: osiemnaście tysięcy złotych)` |
| 4 | **Numbering** | §/ust./pkt consistent across the whole document. Clause lists: a) b) c). Point lists: 1) 2) 3). |
| 5 | **Definitions** | Every capitalised term is defined in § Definicje or at first use. |
| 6 | **Internal cross-references** | Every „§ X ust. Y" leads to an existing provision. Check after numbering is final. |
| 7 | **No Latin in clauses** | `lucrum cessans`, `dolus`, `ex contractu`: only in analysis, never in clause text. |
| 8 | **Deadlines** | Dates as `dd.mm.rrrr`. Periods as `7 dni` / `7 Dni Roboczych`, not „tydzień" (a week) or „niezwłocznie". |
| 9 | **Consistent party names** | One name throughout: „Wykonawca" everywhere, not „Zleceniobiorca" in places. |
| 10 | **Quoted provisions** | Every article N of act X: first `verify_article()` (if the MCP server is active), otherwise `[UNVERIFIED]`. |

---

## When to run it

- Before every output from `contract-generator.md` (STEP 5, QA)
- Before every output from `terms-generator.md`
- After `fix-clause.md`, before returning the corrected passage
- Optionally after `risk-audit.md`, to check the cited provisions (point 10)

## Red flags: fix at once before output

```
❌ "niezwłocznie"                       → replace: "w terminie 3 dni roboczych" (or another number)
❌ straight quotes "..."                → replace: „..."
❌ em dash or en dash                   → replace: „oznacza" in definitions, a comma elsewhere
❌ capitalised term without definition  → add a definition, or lower-case it
❌ § 5 ust. 3 (doesn't exist)           → fix the cross-reference
❌ art. X of act Y without verify_article → add [UNVERIFIED] or call the MCP server
```
