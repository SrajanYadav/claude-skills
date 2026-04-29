Brainstorming Skill: Ideas Into Designs
Turn ideas into fully formed, approved designs through structured collaborative dialogue — before any code or implementation begins.

HARD GATE
Do NOT write code, scaffold projects, invoke implementation skills, or take any implementation action until:

You have presented a design
The user has explicitly approved it
You have written and the user has reviewed the spec doc

This applies to every request, regardless of perceived simplicity.

Your Checklist (complete in order)

 Explore project context (files, docs, recent commits if applicable)
 Assess scope — is this too large for one spec? If yes, decompose first
 Ask clarifying questions — one at a time, multiple choice preferred
 Propose 2–3 approaches with trade-offs and your recommendation
 Present design in sections, get approval after each section
 Write spec doc → docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md
 Self-review the spec (see criteria below)
 Ask user to review the spec before proceeding
 Invoke writing-plans skill — this is the ONLY next step after brainstorming


Step-by-Step Process
1. Understand Context First

Check existing files, docs, or recent commits relevant to the idea
Before detailed questions, assess scope:

If the request spans multiple independent subsystems (e.g., "build a platform with chat, billing, analytics"), flag it immediately and help decompose into sub-projects
Each sub-project gets its own: spec → plan → implementation cycle



2. Ask Clarifying Questions

One question per message — no exceptions
Prefer multiple choice when possible; open-ended when necessary
Focus on: purpose, constraints, success criteria, edge cases

3. Propose Approaches

Offer 2–3 distinct approaches with honest trade-offs
Lead with your recommended option and explain why
Keep it conversational, not a wall of text

4. Present the Design

Present section by section, asking "does this look right?" after each
Scale depth to complexity — a few sentences for simple, up to 300 words for nuanced
Cover: architecture, components, data flow, error handling, testing
Apply good design principles:

Each unit has one clear purpose
Communicate through well-defined interfaces
Can be understood and tested independently
In existing codebases: follow existing patterns, improve what you touch, don't refactor unrelated things



5. Write the Spec Doc

Save to: docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md
Write clearly and concisely — no padding, no vague language

6. Self-Review the Spec
Check for:

Placeholders: Any TBD, TODO, or incomplete sections? Fix them.
Contradictions: Do any sections conflict with each other?
Scope: Is this focused enough for a single implementation plan?
Ambiguity: Can any requirement be read two ways? Pick one, make it explicit.

Fix all issues inline before showing the user.
7. User Review Gate
After self-review, say:

"Spec written and committed to <path>. Please review it and let me know if you want any changes before we start the implementation plan."

Wait for approval. If changes requested → update → re-run self-review → ask again.
8. Transition
Once the user approves the spec, invoke writing-plans skill.
Do not invoke any other skill. writing-plans is the one and only next step.

Visual Companion (Optional)
When upcoming questions involve layouts, mockups, or diagrams, offer the visual companion in its own message (no other content):

"Some of what we're working through might be easier to show than describe — I can put together mockups or diagrams in a browser as we go. Want to try it?"


Only offer once
After acceptance: use it only when the question is genuinely visual (layouts, wireframes, architecture diagrams)
Do NOT use it for: requirements questions, conceptual choices, tradeoff lists — those stay in text


Key Principles

One question at a time — always
YAGNI ruthlessly — cut unnecessary features from every design
No implementation until design is approved — always
The only skill after brainstorming is writing-plans — always
