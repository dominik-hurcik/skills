# Color

Color shows hierarchy, meaning, and atmosphere. Keep the brand colors and semantic conventions the project already has. Do not replace the visual identity under the name of "adding color."

## Choose the mode

- **Persuade and Experience:** color can carry the voice and fill large areas when the design calls for it.
- **Operate and Read:** color mainly shows actions, selection, status, navigation, and the reading hierarchy. Use it sparingly so the accent stands out.

## Audit before you choose

Read the design notes, tokens, assets, current themes, and sample screens. Note:

- which colors are confirmed brand commitments;
- the current roles for surfaces, text, actions, and status;
- places where grayscale hides hierarchy or state;
- contrast failures and places where color alone carries meaning;
- light and dark theme needs, and any data charts;
- whether the task asks for more color or a new identity. For a new identity, use [new-work.md](new-work.md).

## Choose a strategy

Decide the mood, the main relationship between colors, the contrast range, and how much color to use. The strategy can be restrained or immersive. Follow the brief, not a fixed percentage rule.

Build palettes from roles, not from a bag of swatches:

- canvas and raised surfaces;
- primary and secondary text;
- action, focus, and selection;
- borders and dividers;
- success, warning, error, and information;
- data categories, when charts need them.

Use the project's color format. For a new web palette, OKLCH is a good choice because you can adjust lightness and chroma in a predictable way. Pick hue from the product's meaning and the visual direction, not from default associations.

## Apply

- Let the strongest color own one clear area or role. Do not scatter small accents everywhere.
- Keep the primary action easy to find. Do not spend its color on decoration.
- Tint neutral grays toward the brand hue only when it creates cohesion. Plain gray is fine when it suits the design.
- Derive secondary text from the foreground or surface hue, not from a washed-out generic gray.
- Keep status meanings consistent. Follow platform or domain conventions where they exist, instead of forcing fixed hues.
- In charts, separate categories by lightness, shape, labels, or pattern, not by color alone.
- In dark mode, design surface levels and contrast on purpose. Do not invert the light theme.
- If the project has a token system, define primitive values and semantic tokens. Switching themes should remap the semantic roles.

Color that does not relate to hierarchy, state, content, or the visual identity is decoration, not a color strategy.

## Contrast

Check computed colors for each pair of foreground and background:

| Content | Minimum (WCAG AA) |
| --- | --- |
| Body text | 4.5:1 |
| Large text | 3:1 |
| Controls, icons, focus rings | 3:1 |

Check hover, focus, overlays, text over images, disabled content, and both themes. Information shown only by color also needs text, shape, an icon, or position. Check for color blindness.

When you build a lightness ramp in OKLCH, reduce chroma near white and black. Keep chroma high only where it works. Prefer solid colors over stacked transparent layers, because transparency makes contrast depend on what sits behind.

## Verify

- Each color has a clear role or a clear purpose in the visual identity.
- Attention lands on the intended action, content, or state.
- The palette works in quiet, dense, interactive, error, and empty states.
- Light and dark themes are each designed, not one copied from the other.
- Contrast and non-color cues pass in every relevant state.
- The palette looks like this product, not like a generic colorful theme.
- Then do the final pass in [polish.md](polish.md).
