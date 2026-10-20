# Responsive, adapt, and harden

Two jobs live here. Adapting moves a design to a new context, such as a phone or a print page. Hardening makes it hold up against real users, bad networks, and unusual content.

## Adapt to a new context

Adapting is not scaling. Rethink the experience for the new context. Start with these questions:

- What was the design made for? What did it assume about screen size, mouse, speed, and time?
- What does the new context look like? Device, input (touch, mouse, keyboard), screen size, connection, and how the person is using it: on the go, or at a desk?
- What no longer fits, what no longer works, and what would feel wrong there?

Adapt for the web only here. For native iOS and Android screens, use the platform's own guidance.

**Phone:**

- One column, stacked content, and full-width controls.
- Navigation at the bottom or in a menu, with a short path back.
- Bottom sheets in place of dropdowns when a choice needs space.
- Touch targets of at least 44 by 44 pixels, with more space between them.
- Hide secondary content behind a disclosure or tab, and keep the main content first.
- Body text at 16px or larger.

**Tablet:**

- Two columns where they help: a list and its detail, or main content and a side panel.
- Support both touch and pointer input.
- Handle both portrait and landscape.

**Desktop:**

- Use the extra width for comparison and overview. Do not just stretch a phone layout.
- Support keyboard and pointer hover, and do not rely on hover alone for anything important.

**Print or email:** keep the content and the order. Remove interactive parts. Email needs simple layouts and inline styles, because many clients strip out modern CSS.

## Layout techniques

- Write mobile-first styles, then add layers for larger sizes.
- Set breakpoints where the content breaks, not at device sizes.
- Detect input method as well as screen size. A large touch screen is still a touch screen.
- Respect device safe areas, such as notches and home indicators.
- Serve images at several sizes with `srcset`. Use `picture` when the crop should change with the screen.
- Test on real devices. Browser dev tools do not show everything.

## Harden against real use

Test with inputs that a perfect demo never shows:

- **Text:** very long names, very short values, empty fields, emoji, accented letters, and right-to-left text.
- **Numbers:** millions and billions, and negative or zero values.
- **Lists:** no items, one item, and more than 1,000 items.
- **Errors:** offline, slow network, timeouts, server errors (400 to 500), expired sessions, missing permissions, and rate limits.
- **Concurrency:** two people or two tabs changing the same thing.

Then fix what breaks:

- **Overflow:** let containers grow with their content. Use `min-width: 0` on flex and grid children that hold text. Use `overflow-wrap: break-word` for long strings. Use line clamps for long titles, with the full text available on demand.
- **Fluid type:** use `clamp()` for sizes that scale with the screen. Keep body text at 16px.
- **Translation length:** plan for about 30 to 40 percent more text than English. German is often the longest.
- **Direction:** use logical CSS properties such as `margin-inline-start` and `padding-inline`, so the layout flips for right-to-left text.
- **Dates and numbers:** use the `Intl` API for dates, numbers, and currency. Do not format them by hand.
- **Plurals:** use the project's i18n library. Do not write `item + 's'`.
- **Forms:** validate on input and on submit. Keep the user's entries when an error occurs. Set input font size to 16px or more on iOS, or the page zooms when a field is focused.
- **Loading and errors:** show a skeleton or spinner for slow loads, a retry for failed requests, and a clear message for every error. Never leave a blank screen.
- **Performance:** debounce search input, paginate or virtualize long lists, and cancel requests the user no longer needs.
- **Accessibility under stress:** the layout still works at 200% zoom and with long translations.

## Verify

- The layout holds at phone, tablet, and desktop widths.
- Touch targets meet the size guideline.
- No horizontal scrolling at narrow widths.
- Long, empty, and unusual content does not break the layout.
- Each error case shows a clear message and a way out.
- Text stays readable at 200% zoom.
- Then do the final pass in [polish.md](polish.md).
