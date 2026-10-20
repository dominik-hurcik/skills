# Typography

Type carries information, hierarchy, and voice. Improve it inside the existing visual identity. Replace the font families only when the user asked for a new identity, and then use [new-work.md](new-work.md).

## Choose the mode

- **Persuade and Experience:** display type can carry the voice. Use strong contrast in size and weight, and let headings scale with the space available.
- **Operate and Read:** stability, scanning, and measure come first. One well-tuned family with a fixed set of roles is often the right answer.

## Review the current type

Check:

- **Families and weights:** which ones are in use, and whether each one has a job. Remove any family that does not earn its place.
- **Hierarchy:** can a reader tell headings, body text, labels, metadata, and data apart at a glance? Adjacent sizes or weights that are too close fail this test.
- **Scale:** is there a deliberate set of sizes, or a pile of arbitrary values? Repeated roles should look identical everywhere.
- **Reading:** body text at 45 to 75 characters per line. Line height, paragraph rhythm, and tracking should fit the actual face.
- **Stress:** long headings, longer translations, zoom, narrow containers, missing weights, and fallback fonts.
- **Loading:** only the fonts and weights in use are loaded. Fallback fonts match the metrics of the web font, so text does not jump. No invisible text while a font loads.

## Set the system

Before you edit, decide:

- which roles the interface needs;
- how far apart those roles should be in size, weight, and tone;
- the reading measure and density;
- which existing faces are authoritative;
- any performance, language, or accessibility limits.

Use the fewest roles and families that make the hierarchy clear. Name roles by purpose, such as "section heading" or "caption," not by value, such as "18px."

## Apply

- Use 16px as the normal body size on the web unless a dense layout or a user setting calls for something else.
- Keep prose between 45 and 75 characters per line. Wider lines need more leading.
- Light text on a dark background usually needs a little more line height, a little more letter-spacing, and sometimes one step more weight.
- Tune line height to the face, its width, the language, and the contrast. No single ratio fits all.
- Use tabular numerals in tables and figures that people compare.
- Use paragraph spacing or a first-line indent for paragraph breaks, not both.
- Preserve browser zoom, user font settings, and platform text scaling.
- Do not use decorative type where it hurts comprehension. Do not add a second family unless it has a role no other family can do.

## Line breaks

- Set `text-wrap: balance` on headings and short centered text. Set `text-wrap: pretty` on body text. Browsers that ignore these keep their default wrap, which is fine.
- If a single word sits alone on the last line of a narrow column, edit the copy or widen the column.
- Use a hard line break only between phrases, and check it at every width. A break that lands in the middle of a phrase on a phone is worse than the default.
- An uneven break can be intentional, such as a one-word headline for emphasis. Make it deliberate, and keep it rare.

## Verify

- Primary, secondary, body, and metadata text are easy to tell apart without reading the copy.
- Long text stays comfortable in the relevant widths and languages.
- The type fits the product and its visual identity.
- Loading causes no jumping text and no invisible text.
- Zoom, text scaling, focus states, and contrast all still work.
- Then do the final pass in [polish.md](polish.md).
