# Craft floor

Read this after the direction is set, then build without listing the checks out loud. A pinned brief or an established visual identity overrides anything here. Your own habits do not.

## Verify the built result

Each item is a check on the rendered page. Run them together in one review of the render, not one at a time.

- **Contrast:** body and placeholder text at least 4.5:1. Large text at least 3:1. On colored surfaces, derive secondary text from that hue or the foreground color, not from plain gray.
- **Depth:** shadows have a vertical or horizontal offset and a soft blur. A shadow with zero offset and a colored glow is decoration.
- **Spacing:** tight inside groups, generous between groups, and more space above a heading than below it. Read the computed values.
- **Type:** body text at 65 to 75 characters per line. Display text at most 6rem. Letter-spacing no tighter than -0.04em. Headings balanced. Scale and weight steps easy to see. Run the real copy at every breakpoint and fix anything that overflows.
- **Motion:** one authored moment, not scattered effects. Not the same entrance on every section. Ease out from a state that is already visible. See [motion.md](motion.md).
- **States:** hover, focus, disabled, loading, error, and empty. Real content, working controls, responsive layout, and keyboard focus.
- **Browser defaults:** text selection, the caret, scrollbars, focus rings, and table numerals ship with browser defaults that belong to no design. Style them from the palette. Models skip this step most often, and it is the fastest way to spot a page that was assembled rather than designed.
- **Copy:** the product's own language. Buttons name their action. Errors name the problem and the way out. See [copy.md](copy.md).
- **Coverage:** every requirement in the brief is present and easy to find within a few seconds.

## Avoid these defaults

These are common patterns, not bans. A brief can earn any of them. If you reach for one only because it is familiar, you have not made a decision. Replace the element instead of softening it.

Page structure:

- Identical cards with an icon, a heading, and a line of text as the main layout. Cards are a lazy container, and nested cards almost always look wrong.
- The hero metric template: a big number, a small label, a few supporting stats, and an accent color.
- A small label (eyebrow) above every heading. Delete it and let the heading carry the weight.
- Section numbers like 01, 02, 03, unless the order itself matters to the reader.
- A modal for a task that needs no interruption and no protected focus.

Surface habits:

- Gradient text. Use weight or size for emphasis.
- Glass and blur as decoration rather than a specific effect.
- A colored left or right border thicker than 1px on cards, list items, callouts, or alerts.
- Hard offset shadows with no blur, unless the visual world is built on them.
- Sparklines, progress rings, and rounded boxes with soft shadows that stand in for real content.
- Monospace type used only to look technical. Use it for code, data, and measurements.
- A system display font (Impact, Arial Black, the platform sans) as the voice of a designed page. Choose a face with character that fits the world.
- Emoji or Unicode symbols standing in for icons. Use one drawn icon set with one stroke weight.
- Geometric shapes that approximate the edge of a photo subject. Cut the real edge from the image or leave the effect out.
- Light or dark theme chosen by product category. Choose it from the real use: who uses it, where, and in what light.
- The usual default faces (Inter, Fraunces, Playfair Display, Space Grotesk, IBM Plex, and similar). Pick faces for the world the design is building.
- The common AI look: a warm cream background, a high-contrast serif display face, and a terracotta accent. Also near-black with one neon accent and glowing edges. Treat either as a starting guess to challenge, not a plan.

Defaults that tend to look cheap:

- Letter-spacing tighter than -0.04em. Often -0.02 to -0.03em reads better.
- Border and shadow used together on one card. Pick one elevation method. Keep card corners around 12 to 16px, and use pill shapes for small controls.
- Sketchy hand-drawn SVG scenes or grain textures in place of real illustration. Use real art or none. Crisp vector diagrams and animated linework are fine.
- Stripe or grid backgrounds with no real canvas or map behind them.

The craft floor sets the minimum. It does not pick the direction. When every check passes, put the effort into the chosen direction. When you are torn between a safe version and a committed one, commit.
