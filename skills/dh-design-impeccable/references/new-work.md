# New visual work

Use this for a new surface, a new page, or a replacement visual identity. It is not needed for small edits inside an established design.

## 1. Decide what is already true

Read the existing design notes, representative code, tokens, components, and assets. Then pick one case:

- **Redesign:** keep the product's facts, content, function, and constraints. Replace the old look. Treat the old look as evidence of what the product is, not as the rule for what it must become.
- **Established identity:** the project already has a coherent look, even without a design doc. Inherit it and document it. Do not invent a replacement.
- **Incomplete brand:** keep the confirmed assets and recognizable traits. Expand the system with the user for this surface.
- **No visual authority:** create a new identity with the user.

A new section or component inside an existing surface inherits that surface's identity. Never turn a small addition into a new identity project.

## 2. Ask the questions that change the work

Ask two or three focused questions before you build. Skip anything already settled in the notes.

- **Persuade:** Who must act? What should they believe? What proof, content, or assets make that belief credible?
- **Operate:** What task does the user complete? What information matters? Which states come up often?
- **Read:** What question is the reader trying to answer? What is the source material? How do readers find their way?
- **Experience:** What leads? How does a visitor explore? Which interaction or transition matters most?

For every mode, ask what success looks like, what must stay untouched, and what would make a polished result feel wrong. Do not ask for CSS values or style labels.

## 3. Find the world

Name three things in one sentence each:

- the product's distinctive mechanism, the thing it does that others do not;
- the audience's real situation: where they are, what they are doing, what light and time pressure they face;
- the first surface's job: what this page or screen must prove.

Then list five to seven concrete visual worlds the audience already knows well. These can be real artifacts, places, print or screen traditions, or rituals. For each one, note why it fits, its main colors and type, and the one visual signature that makes it recognizable.

Also name the usual look for this kind of page and its opposite. Both are defaults. Do not pick either by reflex.

## 4. Commit to one direction

Choose one direction and carry it through fully. A safer mix of two directions usually looks like neither.

Before you build, write a short direction note with these parts:

- **Thesis:** the one idea this surface owns.
- **First viewport:** what the visitor sees first, and whether it shows the mechanism rather than a generic header.
- **Visitor path:** the steps from arrival to the main action.
- **Signature interaction:** the one motion or behavior the surface is known for.
- **Risk:** what could look wrong, and how you will check it.

Keep the note under about 150 words. Save it with the project's other design notes if it has a place for them. Do not put it in code, comments, or anything shipped to the browser.

## 5. Choose color and type from the world

Pick a color strategy first:

- **Restrained:** tinted neutrals with one accent. Common for tools people use every day.
- **Committed:** one saturated color covers much of the surface.
- **Full palette:** three or four named roles.
- **Drenched:** the surface is the color.

Persuade and Experience surfaces can take bold choices. Operate and Read surfaces should keep color for jobs such as actions, status, and selection.

Choose type faces the way you choose objects from the world. Operate and Read surfaces work well with system fonts or sturdy UI faces. Persuade and Experience surfaces need faces with a point of view. Avoid the usual default faces unless the world calls for them.

## 6. Build with full commitment

- Build the chosen direction. Do not build a safer version of it.
- Rebuild nav, buttons, inputs, and links in the direction's style. A stock component inside a committed design weakens it.
- Use real product content. Give the page real names, entries, and copy. Do not fill gaps with gradients, generic icon tiles, or stock blobs.
- Use real photos only when the brief needs them. Find the actual subject, not the category. Check that every image URL loads.
- Make the first viewport show the thesis at full size. The memory test: if a visitor left after one screen, what would they describe an hour later? If the answer is a mood, the direction is not clear yet.
- Use motion once, with purpose. See [motion.md](motion.md).

## 7. Check and finish

- View the surface at every size it ships at, including the first viewport at common desktop widths.
- Turn off or finish entrance animations before you judge the layout. A hidden element looks missing.
- Run the checks in [craft-floor.md](craft-floor.md).
- Then do the final pass in [polish.md](polish.md).
- Update the project's design notes if the identity is new or changed. Write the notes from the finished build, not from the plan.
