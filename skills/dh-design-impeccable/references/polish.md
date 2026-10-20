# Polish

Use this for the final pass before something ships. Polish refines the design. It does not redesign it. Keep the current visual identity, copy, and behavior, and change only what falls outside the quality bar.

If the concept itself is wrong, say so. Recommend a redesign with [new-work.md](new-work.md) instead of slipping a new look in here.

## 1. Learn the system

Read the design notes, tokens, shared components, and neighboring screens. If there is no formal system, follow the project's own conventions.

Sort each problem into one of four types before you fix it:

- **Missing token:** the system needs a reusable value.
- **One-off implementation:** a shared component or pattern should replace it.
- **Conceptual mismatch:** the flow or hierarchy differs from similar areas of the product.
- **Local defect:** the implementation is incomplete or inconsistent.

Fix each problem at the narrowest level that solves it. Ask only when a system rule that matters cannot be inferred.

## 2. Gather evidence

Use the feature yourself at desktop and mobile widths. Walk through the main path, the edge cases, and every state: empty, loading, error, success, disabled, and permission-limited.

Use realistic content. Try long names, long translations, and empty data.

## 3. Triage

Fix in this order:

1. Broken or blocked tasks, data loss, misleading status, and paths a screen reader or keyboard cannot use.
2. Missing loading, empty, error, success, disabled, and permission states.
3. Flow, hierarchy, responsive, and system drift.
4. Visual and motion inconsistencies.
5. Code and asset cleanup.

Do not perfect one corner while the rest stays below the quality bar.

## 4. Polish the whole path

**Flow and hierarchy**

- Match the terms, save behavior, and navigation that neighboring screens use.
- Make the main task and current state obvious without making everything the same weight.
- Connect arrival, transitions, empty states, and recovery paths.

**Layout and type**

- Align to the project's grid and spacing scale. Check optical alignment too, not only the math.
- Group related items closely and separate groups clearly. See [layout.md](layout.md).
- Fix text that wraps badly, overflows, or runs too long. See [typography.md](typography.md).

**Color and imagery**

- Check contrast in every state and both themes. See [color.md](color.md).
- Make sure images are the right size, load fast, and have alt text.
- Make icons one consistent set in one stroke weight.

**Interaction and state**

- Give every control a clear hover, focus, active, and disabled state.
- Check keyboard use end to end.
- Keep motion to the one or two moments that matter. See [motion.md](motion.md).

**Content and code**

- Tighten labels and messages. See [copy.md](copy.md).
- Remove dead code, unused styles, and leftover placeholder text.
- Check that the layout still works at small and large text sizes.

## 5. Verify and finish

- Run the checks in [craft-floor.md](craft-floor.md) on the rendered result.
- Re-check every state from step 2, not only the ones you changed.
- Report what you fixed, what you could not verify, and any issue you left for later with its reason.

Claim only what you saw. Say "the empty state now shows a next step," not "everything is polished."
