---
name: writing-drunk-grandma
disable-model-invocation: true
description: Rewrite text so a tipsy grandma with no technical background understands it on the first read. Use when the user asks to make something simple, plain, or "grandma-proof", before writing or sending a chat answer, doc, email, or release note.
---

# Drunk grandma test

Before you write or send text, rewrite it until a slightly tipsy grandma with no background in the topic would understand it on the first read. Simplify the words, never the facts.

## Steps

1. Find the one thing she must take away. Say it first, in 12 words or fewer.
2. Swap every technical word, acronym, and brand name for an everyday word. If a term must stay, explain it with something from her kitchen, garden, or TV. For example, "a cache is like keeping the milk on the table instead of walking to the shop each time."
3. Write one idea per sentence, with 15 words or fewer per sentence.
4. Use numbers she can picture, such as "about 2 minutes" or "costs about as much as a coffee".
5. Tell her why it matters to her: what changes, what she has to do, or that she doesn't have to do anything.
6. Keep it short: at most 5 short paragraphs or bullets.
7. Read it back as her. Wherever she'd ask "what does that mean, dear?", rewrite that part.

## Rules

- Keep every fact, number, warning, and deadline that matters. If simplifying would make something untrue, keep the true version and explain it more slowly.
- Never simplify code, commands, file paths, or exact values. Show them as they are, and explain around them.
- Be kind, not condescending. No baby talk, no "simply" or "just", and no jokes about her drinking.
- Follow the writing rules in AGENTS.md.

## Output

Give the rewritten text only. If you left something out, add one line at the end that says what and why.

## Example

**Before:**

> The deploy failed because the CI pipeline's integration tests timed out against the staging DB after the migration added a non-concurrent index, which locked the table.

**After:**

> The update didn't go live. Nothing is broken for anyone.
>
> Before an update goes live, a robot runs checks on a practice copy of the website. One check took too long and gave up.
>
> It got stuck because we were reorganising a big list of data, a bit like re-sorting a whole recipe box. While that happened, nobody else could open the box.
>
> We'll sort the box in a gentler way and try again. You don't need to do anything.
