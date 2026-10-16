# Official sources

The official source for Slovak legislation is Slov-Lex, run by the Ministry of Justice of the Slovak Republic. Each act has a page at `https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/<year>/<number>/`.

## How to fetch the current text

The Slov-Lex page is rendered by JavaScript, so a plain page fetch returns no text. Fetch a consolidated PDF instead:

```text
https://static.slov-lex.sk/pdf/SK/ZZ/<year>/<number>/ZZ_<year>_<number>_<YYYYMMDD>.pdf
```

`<YYYYMMDD>` is the date the version took effect. The first line of the PDF confirms it ("Časová verzia predpisu účinná od"). To find the newest version date, search the web for the act number plus "slov-lex účinné od", then fetch the PDF for that date. If your fetch tool can't read the compressed PDF, save it and extract the text with a PDF library, such as `pypdf` in Python.

Older static HTML versions also exist at `https://static.slov-lex.sk/static/SK/ZZ/<year>/<number>/<YYYYMMDD>.html`.

## Acts this skill relies on

Checked on 16 October 2026.

| Short name | Full title | Version read | Address |
| --- | --- | --- | --- |
| ObZ | Zákon č. 513/1991 Zb., Obchodný zákonník | Version effective from 17 August 2026 | `ZZ/1991/513` |
| Autorský zákon | Zákon č. 185/2015 Z. z., Autorský zákon | Version effective from 1 September 2026 | `ZZ/2015/185` |
| Nariadenie 21/2013 | Nariadenie vlády č. 21/2013 Z. z., the government regulation that sets the late-interest rate and the flat collection fee under the Commercial Code | Version effective from 1 January 2015, the latest listed | `ZZ/2013/21` |

## Other relevant acts, not checked here

Fetch and read these before citing them:

- Zákon č. 40/1964 Zb., Občiansky zákonník (Civil Code). It applies to consumers and to relationships outside the Commercial Code. It also contains the work contract (zmluva o dielo) that Autorský zákon § 91 refers to.
- Zákon č. 18/2018 Z. z. on personal data protection, which supplements the GDPR.
- Zákon č. 22/2004 Z. z. on electronic commerce.
- Zákon č. 244/2002 Z. z. on arbitration.
