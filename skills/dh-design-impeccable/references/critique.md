# Critique

Use this to review a design and report what works, what does not, and what to fix first. The output is a written review, not a set of edits, unless the user asks for edits.

## Setup

1. Resolve the target to a file path or a URL. Prefer a source file when both point to the same screen, because URLs and ports change more often than files.
2. Read the brief or the project's design notes, if any. Know the surface's mode: Persuade, Operate, Read, or Experience.
3. Look at the surface at desktop and mobile widths. Check the main path and the states: empty, loading, error, and full content.
4. Review it yourself in one pass. Keep your first impression separate from the checklist, so the checklist does not bias that first read.

## Questions to answer

- **First impression:** What does the visitor notice in the first few seconds? Is that the right thing?
- **Specificity:** Does this look made for this product, or could it belong to any product in the category? Name one element that could not be copied to another product.
- **Hierarchy:** Is the primary action or message obvious? Do secondary items support it instead of competing?
- **Clarity:** Can a first-time user tell what to do next without help?
- **Consistency:** Do repeated parts look and behave the same?
- **Cognitive load:** Does the visitor have to hold too much in mind at once: too many choices, hidden navigation, jargon, or a context switch to finish a task?

## Score the heuristics

Score each of Nielsen's ten usability heuristics from 0 to 4. Use 0 to 4 honestly. A 4 means excellent. Most real interfaces score 20 to 32 out of 40.

1. Visibility of system status
2. Match between the system and the real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

Mark a heuristic `n/a` only when it truly cannot apply. On Persuade and Experience surfaces, heuristics 7 and 10 often do not apply. If you mark any `n/a`, the maximum drops to 4 times the number you scored. Report the percentage too.

| Score | Rating |
| --- | --- |
| 36 to 40 | Excellent. Minor polish only. |
| 28 to 35 | Good. Fix the weak areas. |
| 20 to 27 | Acceptable. Significant work needed. |
| 12 to 19 | Poor. Core experience needs an overhaul. |
| 0 to 11 | Critical. Redesign before release. |

## Rate each issue

| Priority | Name | Meaning | Action |
| --- | --- | --- | --- |
| P0 | Blocking | Stops the task | Fix now |
| P1 | Major | Causes real confusion or difficulty | Fix before release |
| P2 | Minor | Annoying, with a workaround | Fix in the next pass |
| P3 | Polish | Little real impact | Fix if time allows |

If you are not sure between two levels, ask: would a user contact support about this? If yes, it is at least P1.

## Test with personas

Walk the main path as each relevant person. Pick the three or four that fit the product.

- **Impatient power user:** wants shortcuts and speed. Can they skip the slow parts?
- **First-time visitor:** knows nothing about the product. Can they understand it and act?
- **Visitor who relies on assistive tech or zoom:** can they use the keyboard, read the labels, and zoom to 200% without breaking the layout?
- **Stress tester:** enters long names, empty fields, odd characters, and bad network conditions. What breaks?
- **Distracted mobile user:** on a small screen, with interruptions. Can they finish quickly with one thumb?

## Report

Write the report in this order:

1. The overall verdict in one or two sentences.
2. What works. Be specific, and name the elements.
3. Priority issues, sorted by P0 to P3. For each one: what happens, why it matters, and the fix.
4. Persona red flags, if any.
5. Minor observations.
6. The heuristic table and score.
7. One or two focused questions for the user, if answers would change the next step.

Put the questions last. Do not write anything after them. If you ask no questions, say so in one line.
