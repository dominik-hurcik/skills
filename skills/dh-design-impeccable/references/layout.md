# Layout

Layout turns product priority into reading order, grouping, rhythm, and usable space. Find the structural problem before you move boxes around.

## Choose the mode

- **Persuade and Experience:** asymmetric or loose composition is fine when the design calls for it.
- **Operate and Read:** predictable structure, stable density, and simple linear flow help people. Keep them.

Layout changes stay inside the current visual identity. A new identity belongs in [new-work.md](new-work.md).

## Assess first

Check the layout at a few real states and sizes. Answer each question from the rendered page or the code:

- **Reading order:** Blur the details. Can you still find the main element, the supporting element, and the main groups, in that order?
- **Grouping:** Are related items close together? Are separate groups clearly apart? Or do boxes and borders do work the spacing should do?
- **Rhythm:** Do tight and loose spacing create a clear pattern? Or is one value repeated until everything looks equally important?
- **Structure:** Do the cards, columns, or sections really hold equal content? Or were they repeated by default?
- **Density:** Is the amount of information per area right for how often people use it?
- **Adaptation:** What reorders, collapses, wraps, or scrolls at narrow and wide sizes? Does the source order match the visual order?
- **Extremes:** Long text, empty states, overlays, sticky elements, and small touch targets.

## Set the structure

Before you edit, decide:

- the main reading or task path;
- what belongs together and what must separate;
- which element leads and which supports it;
- the density and spacing rhythm;
- how the structure changes at different widths and with long content.

Choose the simplest structure that shows those relationships.

## Apply

- Group by meaning first. Use spacing before you add containers or decoration.
- Create rhythm with deliberate contrast between tight and loose spacing.
- Use a spacing scale with named steps, not one-off values. A 4px base usually gives the middle steps that an 8px-only scale misses.
- Let hierarchy follow product priority, not the defaults of the framework.
- Keep different content visually distinct without boxing every group.
- Make responsive changes structural: reorder, collapse, or reveal based on what matters most at that size.
- Use `gap` for spacing between siblings when it says the relationship more clearly than margins on children.
- Keep touch targets usable even when the visible mark is small. Aim for 44 by 44 pixels.
- Use depth (shadow, elevation, layering) only to show state or hierarchy.
- Make optical adjustments only after you look at the rendered result.

Variety is not a goal. Repetition helps people recognize things. Break the pattern only when the content or its priority changes.

## Verify

- The main, secondary, and group order still reads at every supported size.
- The task path stays clear at every size.
- Related content groups together. Unrelated content does not blur together.
- Spacing creates a deliberate rhythm.
- Density fits how often people use the screen.
- Long text, empty states, other languages, zoom, and live content do not break the structure.
- Keyboard and screen reader order match the visual order.
- Then do the final pass in [polish.md](polish.md).
