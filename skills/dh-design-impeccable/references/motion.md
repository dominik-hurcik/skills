# Motion

Use motion to show state, relationships, and hierarchy, or to create one deliberate moment the design has earned. Motion that only decorates is wasted effort and a cost to the user.

## Choose the mode

- **Persuade and Experience:** motion can carry the voice. One rehearsed sequence usually beats many small reveals.
- **Operate and Read:** motion supports feedback, state, and continuity. Keep routine transitions fast. Do not make people wait through page-load effects.

## Find the job

Look at the existing motion, the interaction states, the target devices, and the performance budget. Add motion only where it:

- confirms an action;
- makes a state change or a spatial relationship clear;
- keeps continuity across navigation or a layout change;
- draws attention to a moment that matters;
- expresses the visual identity.

Do not animate something just because it is on the page.

## Plan the motion

Write a short plan before you build:

- **Focal moment:** the one sequence worth authoring, if any. It should come from this product and this surface.
- **Continuity:** the state or layout changes that need explanation.
- **Feedback:** the controls and results that need acknowledgment.
- **Budget:** which effects are expensive, and how often they run.

A generic fade-and-rise, a hover lift, a parallax layer, or a scroll reveal on every section is not a plan.

## Pick the right property

Transform and opacity are safe, but they are not the only tools. Choose the property for what the motion should communicate:

- **Continuity and relationship:** shared-element moves, view transitions, or deliberate movement through space.
- **Focus and depth:** limited blur, filter, backdrop, or shadow changes.
- **Reveal:** masks, clip paths, or cropping.
- **Material and energy:** color shifts, gradient movement, or texture, when the visual identity supports them.
- **Feedback:** the smallest change that makes cause and result obvious.

Do not stack several techniques for spectacle. One strong idea, carried through the focal sequence, is usually enough.

A staggered list entrance is right when a list appears as a list. Cap the total delay. Do not stagger every section on the page.

## Timing

| Duration | Use |
| --- | --- |
| 100 to 150 ms | Immediate feedback |
| 150 to 300 ms | Routine state change |
| 300 to 500 ms | Layout, overlay, or view transition |
| 500 to 800 ms | A deliberate focal entrance |

Exits are faster than entrances. For confident arrivals, use an ease-out curve such as `cubic-bezier(0.16, 1, 0.3, 1)`. Avoid bounce and elastic easing unless the design calls for them. Feedback that lags feels like a slow app.

## Build it

- Use CSS transitions and keyframes for simple state changes and short sequences.
- Use the Web Animations API or the project's existing motion library when you need to interrupt, sequence, or drive values.
- Use view transitions or shared-element techniques when continuity between two states is the point.
- Use scroll-linked motion only when the scroll position itself means something. Give it a fallback.
- Do not add a dependency for an effect the current stack can handle cleanly.

Keep content visible in its default state, so a failed script does not hide the page. Avoid animating width, height, top, left, and margins. Use transforms or grid techniques instead. Limit blur, filter, shadow, and canvas work to small areas. Use `will-change` only while an animation runs. Test on real target devices. Transforms are not automatically fast.

## Accessibility

Respect the user's motion preference. Every animation needs a reduced-motion path that keeps the meaning. Reduce or remove movement through space. Keep fades, color changes, and state changes that carry information. Reduced motion means fewer and gentler animations, not no feedback at all.

Stop any looping animation that is not essential when it leaves the screen or the tab is hidden. Do not autoplay sound.

## Verify

- The focal motion is specific to this product and surface.
- Each supporting animation explains feedback, state, or relationship.
- Interrupted and repeated use behave correctly.
- Desktop, mobile, and keyboard use still work.
- With reduced motion on, the page keeps its feedback and state changes.
- Costly effects stay smooth on target devices.
- Removing an animation would lose meaning or character, not just decoration.
- Then do the final pass in [polish.md](polish.md).
