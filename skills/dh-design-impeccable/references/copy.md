# Copy

Words are part of the interface. Good copy tells people what is happening, what they can do next, and how to recover from a problem. Use the product's own language.

## Audit the words

Read every label, button, message, heading, and empty state. For each one, ask:

- Does it say what happens, not how the system works?
- Would a first-time user understand it without help?
- Does the same thing have the same name everywhere?
- Is it shorter than it needs to be? Cut anything that repeats the heading.
- Is it sentence case, with no decorative capitals or emoji?

## Write by job

**Buttons and links:** name the action. "Save changes" or "Create project" works. "Submit" or "OK" does not say what happens. Links name the destination.

**Forms:** label every field in plain words. Put help text where it helps, before the field, not only after an error. Mark required fields clearly.

**Errors:** say what went wrong, in plain words, and what to do next. "That email is already registered. Sign in, or use another address." Do not blame the user, and do not show codes or stack traces as the message.

**Permissions:** say what the person cannot do, why, and who can change it.

**Loading:** say what is happening when the wait is longer than a moment. "Saving your draft" is better than a spinner with no words.

**Empty states:** say what the space is for and give one clear next step. Do not just say "Nothing here."

**Success:** confirm what changed, briefly. "Your changes are live" is enough.

**Help text:** keep it short. Explain the decision the person must make, not the internals of the feature.

## Voice and accessibility

- Use plain words. Prefer "use" to "utilize," "help" to "facilitate," and "if" to "in the event that."
- Use active voice. Name the actor when you can.
- Keep one term for one thing across the product.
- Write for screen readers too. Labels should make sense when read out of context.
- Keep translations in mind. Short, complete sentences translate more reliably than clever phrases.
- Do not joke about errors or money. Be warm, but clear first.

## Verify

- Every control names its action.
- Every error names the problem and the way out.
- Every empty and loading state says what is happening or what to do.
- The same term means the same thing everywhere.
- No claim appears that the product cannot back up. Do not invent numbers, testimonials, or guarantees.
- Then do the final pass in [polish.md](polish.md).
