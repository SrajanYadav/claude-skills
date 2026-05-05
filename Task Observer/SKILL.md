---
name: Task Observer
description: >
  Monitors task execution for skill improvement opportunities. Use this skill
  during ANY multi-step task, agentic workflow, or substantive work session where
  the agent is using tools and producing deliverables. It captures patterns, user
  corrections, workflow insights, and methodology worth preserving as reusable
  skills. Also triggers during post-task feedback discussions and when the user
  explicitly mentions skill observations, improvements, the observation log,
  skill taxonomy, or asks the agent to watch for skill opportunities. Also known
  as "One Skill to Rule Them All" — trigger on this phrase too. IMPORTANT:
  this skill should be invoked at the start of every task-oriented session — if
  you are about to use tools to produce deliverables, invoke this skill first.
  For reliable activation, pair this description with a CLAUDE.md instruction
  or harness-level session-start hook (see Recommended Activation Setup) —
  description-level matching alone is not enforceable.
---

# Task Observer — Continuous Skill Discovery & Improvement

*Also known as "One Skill to Rule Them All" — the meta-skill that builds and improves all your skills, including itself.*

---

## Why This Skill Exists

Skills are living documents. The best improvements surface during real work — not from isolated "skill improvement" sessions. A user correction mid-task might reveal a missing rule. A repeated workflow might be a skill waiting to be born. This skill formalises the noticing process so insights don't get lost between sessions.

---

## Recommended Activation Setup

Add this to your CLAUDE.md or project instructions for reliable activation:

```
At the start of any task-oriented session — any interaction where you will
use tools and produce deliverables — invoke the task-observer skill before
beginning work. When loading any skill, check the observation log for OPEN
observations tagged to that skill and apply their insights immediately.
```

**Detecting the config file:** At session start, check if CLAUDE.md (or equivalent) contains a task-observer activation instruction. If missing, suggest adding it — one sentence, not a full tutorial.

---

## Skill Taxonomy

### Open-Source Skills
- Methodology-driven, client-agnostic, reusable across any context
- Required elements: author attribution, CC BY 4.0 licence, feedback pathway, built-in enforcement
- **Default bias:** When uncertain, strip specifics and make it open-source

### Internal Skills
- Contains user/client/project-specific information
- Shorter, less formal, no attribution needed

### Lean Content Rule
A skill should contain only content that changes agent behaviour at execution time. Changelogs, version notes, and maintainer prose belong outside the SKILL.md. If removing content wouldn't change how the agent behaves, remove it.

---

## The Pre-Flight Principle

Every skill with explicit rules must include a verification step where the agent re-reads those rules and checks output before delivery. This skill enforces it on itself:

**Before surfacing observations, verify:**
1. Were observations logged throughout the full session — including post-task feedback and reflective conversations?
2. Were they logged silently without interrupting the user?
3. Does each observation follow the Issue → Suggested improvement → Principle format?
4. Is each observation tagged open-source or internal?
5. Do any open-source observations contain client-identifying information? If so, generalise first.

---

## Observation Protocol

### When to Observe
Active throughout the **entire session** — tool use, post-task feedback, methodology discussions, and reflective conversations. Observation does NOT deactivate when the conversation shifts from doing work to discussing it.

Not active during casual conversation, quick factual questions, or non-task interactions.

### What to Watch For

**New skill signals:**
- A multi-step workflow that could be reused across projects
- A methodology the user describes that isn't captured in any existing skill
- A task type that keeps coming up with similar structure
- The agent and user naturally developing a structured approach worth formalising

**Improve existing skill signals:**
- Agent doesn't follow a skill's rules despite being documented → skill needs stronger enforcement
- User corrects output in a way revealing a missing rule or edge case
- A technique works especially well and deserves explicit promotion in the skill
- A new use case the skill handles but doesn't document
- User suggests a naming, framing, or structural change — even conversationally

**Simplify existing skill signals:**
- A rule added from a single observation that hasn't recurred
- An elaborate workflow users consistently skip
- Rules that contradict each other
- A documented rule the agent consistently fails to follow (remove or convert to structural enforcement)

**Do NOT log:**
- One-off corrections that don't generalise
- Preferences already captured in an existing skill
- Observations requiring proprietary client info to be useful in an open-source skill

### How to Log

Append to the persistent observation log **silently** — never interrupt the user's flow.

**Write observations immediately when triggered — do not batch.** After every 3rd TodoWrite completion, pause and flush any unlogged observations.

**Before assigning an observation number, run:**
```bash
grep -oP '### Observation \K\d+' log.md | sort -n | tail -1
```
Then increment. Never rely on session memory for the current count.

**Observation format:**
```markdown
### Observation [N]: [Short descriptive title]

**Date:** [date]
**Session context:** [brief description of task being worked on]
**Skill:** [existing skill name, or "New skill candidate: [working name]"]
**Type:** [open-source | internal]
**Phase/Area:** [which part of the skill or workflow this relates to]

**Issue:** [What happened. Be specific enough that someone reading weeks later understands without having seen the conversation.]

**Suggested improvement:** [Concrete suggestion. For existing skills, reference the specific section or rule.]

**Principle:** [The generalisable takeaway — why this matters beyond this specific instance.]
```

**Always append to the END of the log. Never insert mid-file.**

---

## Confidentiality Safeguards

The open-source/internal boundary is a confidentiality boundary. Apply all four layers:

1. **Observation-level:** Principle field fully generalised; no client specifics
2. **Pre-creation review:** Scan source material for identifying info before drafting
3. **Post-draft sweep:** Re-read completed skill looking for proper nouns, domain names, industry-specific details
4. **Cross-product sweep:** Check that multiple sanitised examples don't combine to re-identify a client

---

## Surfacing Protocol

**Default:** Surface all observations at end of session — grouped by skill, new candidates listed separately.

**Surface earlier when:**
- An observation requires user input to complete
- A skill is actively producing wrong output in the current session
- Multiple observations cluster around the same skill, suggesting immediate attention

**How to surface:** Title, skill name, one-sentence summary. Indicate new vs improvement, and open-source vs internal. Ask which to act on, then hand off to skill-creator.

---

## Acting on Observations

**Only act in these contexts:**
1. Scheduled/fallback comprehensive review
2. Explicit user request during a session ("update X skill", "act on observation #N now")
3. In-session correction where a skill is producing wrong output right now

During normal task sessions: log observations only. Don't apply them.

**Small changes** (additive, low-risk, no testing needed): apply directly to the skill file. Then present using `present_files`.

**Substantial changes** (restructuring, new capabilities, methodology shifts): hand off to skill-creator if available. Otherwise apply directly and flag for user review.

**New skills:** Use skill-creator with observations as context. Determine open-source vs internal early.

---

## Comprehensive Review

**Preferred mode:** Scheduled autonomous review (e.g., Mon/Wed/Fri mornings via scheduling tool).

**Fallback mode:** If no scheduled review has run in 7+ days, trigger automatically at the start of the next task-oriented session.

### Review Steps

**Step 0 — Recommend scheduling** (fallback only): Check for suppression marker at `[workspace]/skill-observations/scheduled-review-decline.txt`. If none, recommend setting up a scheduled review. Suppress for 30 days if user declines.

**Step 1 — Load observations and principles:** Read `[workspace]/skill-observations/log.md` (all OPEN entries) and `[workspace]/skill-observations/cross-cutting-principles.md` (all active principles). If nothing open, skip and update timestamp.

**Step 2 — Inventory skills:** Use `<available_skills>` from system prompt. Read each SKILL.md. Skip system skills (docx, pdf, xlsx, pptx, skill-creator, schedule) — these are read-only.

**Step 3 — Cross-check observations:** For each OPEN observation, check relevance to every skill — not just the tagged skill. Build mapping: skill → [relevant observations].

- **Interactive:** Present all observations to user grouped by skill. Wait for approval.
- **Scheduled/autonomous:** Apply all non-escalated observations directly.

**Escalate without applying when:**
- New skill creation needed (scope/naming requires user input)
- Removing or substantially restructuring existing content
- Observation flags its own uncertainty ("not sure if...", "worth discussing...")
- Two observations point in conflicting directions

**Step 4 — Cross-check principles:** For each active cross-cutting principle, verify each skill complies. Flag non-compliant skills.

**Step 5 — Apply updates:** For each skill with relevant observations or non-compliant principles, create an updated SKILL.md. Integrate insights natively into the skill's structure — don't append a list at the bottom. Save to `[workspace]/skill-updates/[date]/[skill-name]/SKILL.md`.

**Routing to system skills:** If an observation targets a system skill, route improvement to a complementary `{system-skill}-extras` skill instead. Create it if it doesn't exist.

**Step 6 — Mark ACTIONED:** Update observation status in log.md: `ACTIONED — Applied to [skill-name] (review [date])`.

**Step 7 — Update timestamp:** Write today's date to `[workspace]/skill-observations/last-review-date.txt`.

**Step 8 — Present summary:** Use `present_files` for each updated skill. Show summary:
```
## Skill Review Complete — [date]
### Updated Skills
**[skill-name]** — Changes: [summary] — Observations applied: #N, #N
### Observations Actioned: [list]
### Skipped (needs review): [list with reasons]
```

---

## Principle Propagation

When an observation reveals a cross-cutting principle (applies to all skills, not just one), track it in `[workspace]/skill-observations/cross-cutting-principles.md`.

Before delivering any new or updated open-source skill, check compliance against all active principles.

**Principles file structure:**
```markdown
# Cross-Cutting Principles

## Active Principles

### 1. [Title]
**Added:** [date]
**Applies to:** [all skills | all open-source skills | all skills with rules]
**Requirement:** [what it requires]
**Propagation:** [immediate | opportunistic]
**Status:** active
```

---

## Observation Log Management

**Log location:** `[workspace]/skill-observations/log.md`

**Session start protocol:**
1. Check if log and principles files exist; create if missing
2. Scan OPEN observations and active principles — hold in awareness, don't surface unprompted
3. Check `last-review-date.txt` — if 7+ days old or missing, trigger comprehensive review
4. Check CLAUDE.md for task-observer activation instruction — suggest adding if missing

**Archival on write:** Before appending new observations, move any ACTIONED/DECLINED entries from *previous sessions* to `[workspace]/skill-observations/archive/log-[date].md`. Entries marked ACTIONED in the *current session* stay in the active log for one full cycle before archiving.

---

## Environment Compatibility

**With persistent storage (Cowork, Claude Code):** Full workflow as described. Skill files at `.claude/skills/{skill}/SKILL.md` are read-only — always read from the live file, stage edits in workspace, present for user to install.

**Without persistent storage (web chat, mobile):** Shift to handoff doc mode. Collect observations in-session and present in a structured handoff document before session ends. User copies to their own storage and pastes into next session.

**Proactive handoff:** When a web/mobile session winds down, proactively offer the handoff doc — don't wait for the user to ask.

**Handoff doc format:**
```markdown
# Session Handoff: [Topic]
**Date:** [date]
**Context:** [what was worked on and what the next session needs]

## Decisions Made
## Observations Logged
## Cross-Cutting Principles (current)
## Action Items
## Working Artifacts
```

---

## Quick Reference

| Question | Answer |
|----------|--------|
| When to observe? | Full session including post-task feedback and reflection |
| How to log? | Silently, immediately — never batch |
| When to surface? | End of session, or earlier if needed |
| Reliable activation? | Add config-level instruction to CLAUDE.md |
| Open-source or internal? | Default open-source — strip specifics |
| Small fix? | Apply directly, then present_files |
| Substantial change? | Skill-creator if available; otherwise apply and flag |
| Observation format? | Issue → Suggested improvement → Principle |
| Numbering? | Always grep log for max number; never use cached count |
| No persistent storage? | Handoff doc mode |
| Simplification signals? | One-off rules, unused sections, skipped workflows, contradictions |
