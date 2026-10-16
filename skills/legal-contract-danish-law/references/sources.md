# Official sources

The official source for Danish legislation is Retsinformation, run by Civilstyrelsen. Each act has an ELI address of the form `https://www.retsinformation.dk/eli/lta/<year>/<number>`.

## How to fetch the current text

The HTML page at an ELI address is rendered by JavaScript, so a plain page fetch returns no text. Fetch the PDF instead:

```text
https://www.retsinformation.dk/eli/lta/<year>/<number>/pdf
```

The PDF is compressed. If your fetch tool can't read it, save it and extract the text with a PDF library, such as `pypdf` in Python. A PDF printed from Retsinformation shows the status ("Gældende" or "Historisk") and lists later amendments ("Senere ændringer til forskriften") on its first page.

To check whether a newer consolidated act exists, search for the act's name on retsinformation.dk, or search the web for the act name plus "retsinformation gældende".

## Acts this skill relies on

Checked on 16 October 2026.

| Short name | Full title | Version | ELI |
| --- | --- | --- | --- |
| Aftaleloven | Lov om aftaler og andre retshandler på formuerettens område | LBK nr. 193 af 2. marts 2016 | `eli/lta/2016/193` |
| Lov om ansættelsesklausuler | Lov om ansættelsesklausuler | LOV nr. 1565 af 15. december 2015 | `eli/lta/2015/1565` |
| Renteloven | Lov om renter og andre forhold ved forsinket betaling | LBK nr. 459 af 13. maj 2014 | `eli/lta/2014/459` |
| Forældelsesloven | Lov om forældelse af fordringer | LBK nr. 1238 af 9. november 2015, later amended by LOV nr. 140 of 2018 and LOV nr. 1553 of 2023 | `eli/lta/2015/1238` |
| Ophavsretsloven | Lov om ophavsret | LBK nr. 1093 af 20. august 2023, amended by LOV nr. 676 af 11. juni 2024 | `eli/lta/2023/1093` |
| Købeloven | Lov om køb | LBK nr. 1853 af 24. september 2021. Not text-checked here. It covers sales of goods, not SaaS. | `eli/lta/2021/1853` |

The sections quoted in `mandatory-rules.md` come from these versions. The later amendments to Forældelsesloven and Ophavsretsloven were not read section by section. Fetch the current text before relying on those two acts.

## Other relevant acts, not checked here

Fetch and read these before citing them:

- Databeskyttelsesloven, the Danish act that supplements the GDPR.
- Lov om forretningshemmeligheder, the Trade Secrets Act.
- Markedsføringsloven, the Marketing Practices Act.
- Voldgiftsloven, the Arbitration Act.
- Forbrugeraftaleloven, the Consumer Contracts Act, for any consumer side.
