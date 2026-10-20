# Audit

Use this for technical quality checks: accessibility, performance, theming, responsive behavior, and implementation quality. Each area gets a score from 0 to 4. Then list the specific findings.

Check the rendered page and the code. Test in a browser when one is available. If you cannot test, say which checks were code-only.

## 1. Accessibility

Check for:

- **Contrast:** body text below 4.5:1, or large text below 3:1. Check every state, including hover, focus, disabled, and placeholder text.
- **Motion:** a `prefers-reduced-motion` path that keeps meaningful feedback and state change. Flag a blanket rule that kills all motion, flashing above safe rates, and motion that moves focus or hides reading content.
- **Labels and ARIA:** interactive elements have roles, names, and states. Form inputs have labels. Required fields are marked.
- **Keyboard:** every control reachable, focus visible, tab order matches the visual order, no keyboard traps.
- **Semantics:** a sensible heading order, landmarks, real buttons and links instead of clickable divs.
- **Images:** meaningful alt text, and empty alt for decorative images.
- **Errors:** messages say what went wrong and how to fix it, linked to the field.

Score 0: fails basic WCAG A. 1: major gaps. 2: partial effort, real gaps. 3: meets AA with minor gaps. 4: meets AA fully and approaches AAA.

## 2. Performance

Check for:

- Layout thrashing: reading and writing layout values in a loop.
- Animating layout properties such as width, height, top, left, or margins instead of transforms and opacity.
- Blur, filter, or shadow effects that drop frames.
- Images without lazy loading or with oversized files.
- `will-change` left on at rest. Use it only during a known animation.
- Unused imports and dependencies, and extra re-renders.

Score 0: severe problems across the page. 1: major problems, such as no lazy loading and costly animations. 2: some optimization, gaps remain. 3: mostly optimized, small gains left. 4: fast on target devices.

## 3. Theming

Check for:

- Hard-coded colors instead of tokens.
- Dark mode missing, or dark mode with weak contrast.
- Tokens used in the wrong role, or mixed token types.
- Values that do not update when the theme changes.

Score 0: no theme system. 1: mostly hard-coded. 2: tokens exist but are used unevenly. 3: tokens used with minor exceptions. 4: complete token system, and dark mode works well.

## 4. Responsive behavior

Check for:

- Fixed widths that break on small screens.
- Touch targets smaller than 44 by 44 pixels.
- Custom sliders or drag areas that fail on touch, block page scroll, or get stuck after an interrupted drag.
- Horizontal scrolling at narrow widths.
- Layouts that break at 200% text size.
- Missing breakpoints for tablet or mobile.

Score 0: desktop only. 1: major breakage. 2: works on mobile with rough edges. 3: responsive, with small overflow or target issues. 4: fluid at every width, with proper touch targets.

## 5. Implementation integrity

Check for:

- The same shortcut repeated across the code, such as copied inline styles or duplicated components.
- Drift from the project's design system.
- Decorative content that adds nothing, or fake data shown as real.
- Layouts that could belong to any product in the category.

Confirm each finding in context before you report it.

## Report

1. Overall score, as a total out of 20, with the rating.
2. Each area's score with one line of evidence.
3. Findings grouped by severity: blocking, major, minor, and polish.
4. Patterns that repeat across the code.
5. What is already good.
6. The fixes, in priority order. Do not apply them unless the user asked for changes.
