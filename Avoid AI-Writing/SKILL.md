---
name: avoid-ai-writing
description: >
  Audit and rewrite content to remove AI writing patterns ("AI-isms"). Use this skill whenever
  the user asks to "remove AI-isms," "clean up AI writing," "edit writing for AI patterns,"
  "audit writing for AI tells," "make this sound less like AI," "humanize this text," or
  "make this sound more human." Also trigger when the user shares a piece of writing and asks
  for an edit, review, or polish pass — especially for LinkedIn posts, blog articles, emails,
  or any professional content. Supports a detect-only mode that flags patterns without rewriting.
  When in doubt, use this skill — AI-ism removal improves almost any written content.
version: 3.3.1
license: MIT
compatibility: Any AI coding assistant that supports agentskills.io SKILL.md format. No external tools or APIs required.
metadata:
  author: Conor Bronsdon
  tags: writing editing voice quality humanize
---

# Avoid AI Writing — Audit & Rewrite

You are editing content to remove AI writing patterns ("AI-isms") that make text sound machine-generated.

---

## Modes

**`rewrite`** (default) — Flag AI-isms and rewrite the text to fix them.

**`detect`** — Flag AI-isms only. No rewriting. Use when:
- The writer wants to see what's flagged and decide what to fix themselves
- Patterns might be intentional
- You're auditing text you don't want altered
- The user says "detect," "flag only," "audit only," "just flag," "scan," or "what AI patterns are in this"

Default to **rewrite** if not specified.

---

## Output Format

### Rewrite mode
Return four sections:
1. **Issues found** — bulleted list of every AI-ism, with the offending text quoted
2. **Rewritten version** — full rewrite; preserve original structure, intent, and technical details
3. **What changed** — brief summary of major edits and why
4. **Second-pass audit** — re-read the rewrite, catch anything that survived, fix inline, note what changed. If clean, say so.

### Detect mode
Return two sections:
1. **Issues found** — bulleted list grouped by severity (P0, P1, P2), with offending text quoted
2. **Assessment** — for each flag, note whether it's a clear problem or a judgment call

---

## Context Profiles

Auto-detect from content cues, or apply when user specifies. Rules not listed apply at full strength.

| Signal | Inferred context |
|--------|-----------------|
| Under 300 words + hashtags/mentions | `linkedin` |
| Code blocks, API refs, technical architecture | `technical-blog` |
| Salutation + investor/fundraising language | `investor-email` |
| Step-by-step instructions, README structure | `docs` |
| No strong signals | `blog` (default — all rules apply) |

**Profile tolerance matrix** (skip = don't audit; relaxed = allow minor instances; strict = zero tolerance; extra strict = flag even borderline):

| Rule | linkedin | blog | technical-blog | investor-email | docs | casual |
|------|----------|------|----------------|----------------|------|--------|
| Em dashes | relaxed | strict | strict | strict | relaxed | skip |
| Bold overuse | relaxed | strict | strict | strict | relaxed | skip |
| Emoji in headers | relaxed (1-2 end-of-line OK) | strict | strict | strict | skip | skip |
| Excessive bullets | skip | strict | relaxed | strict | skip | skip |
| Hedging | strict | strict | relaxed | strict | relaxed | skip |
| Word table | strict | strict | partial* | strict | relaxed | P0 only |
| Promotional language | relaxed | strict | strict | extra strict | strict | skip |
| Significance inflation | strict | strict | strict | extra strict | relaxed | skip |
| Generic conclusions | skip | strict | strict | extra strict | skip | skip |

*Technical-blog exceptions (don't flag): `robust`, `comprehensive`, `seamless`, `ecosystem`, `leverage` (platform/API context), `facilitate`, `underpin`, `streamline`. Still flag: `delve`, `tapestry`, `beacon`, `embark`, `testament to`, `game-changer`, `harness`.

---

## Severity Tiers

### P0 — Credibility killers (fix immediately)
- Cutoff disclaimers ("As of my last update," "I don't have access to real-time data")
- Chatbot artifacts ("I hope this helps!", "Great question!", "Certainly!", "Feel free to reach out")
- Vague attributions ("Experts believe," "Studies show," "Research suggests" — without naming the source)
- Significance inflation on routine events

### P1 — Obvious AI smell (fix before publishing)
- Tier 1 word-list violations (see below)
- Template/slot-fill phrases
- "Let's explore / Let's take a look / Let's dive in" openers
- Synonym cycling within a paragraph
- Formulaic openings ("In the rapidly evolving world of...")
- Bold overuse
- Em dash frequency above 1 per 1,000 words

### P2 — Stylistic polish (fix when time allows)
- Generic conclusions ("The future looks bright," "Only time will tell")
- Compulsive rule of three
- Uniform paragraph length
- Copula avoidance (serves as, features, boasts, presents)
- Transition phrases (Moreover, Furthermore, Additionally)

---

## What to Remove or Fix

### Formatting
- **Em dashes (— and --)**: Replace with commas, periods, parentheses, or two sentences. Target: zero. Hard max: 1 per 1,000 words. Applies to headings too.
- **Bold overuse**: Strip bold from most phrases. Max one bolded phrase per major section — or restructure the sentence to lead with the important thing instead.
- **Emoji in headers**: Remove entirely (exception: social posts, one or two at end of line only).
- **Excessive bullets**: Convert to prose. Bullets only for genuinely list-like content (feature comparisons, step-by-step instructions, parameters).

### Sentence Structure
- **"It's not X — it's Y"**: Rewrite as a direct positive statement. Max one per piece.
- **Hollow intensifiers**: Cut `genuine`, `real` (as in "a real improvement"), `truly`, `quite frankly`, `to be honest`, `let's be clear`, `it's worth noting that`.
- **Vague endorsement**: Cut `worth reading`, `worth paying attention to`, `worth exploring`, `worth your time`. Say *why* instead.
- **Hedging**: Cut `perhaps`, `could potentially`, `it's important to note that`, `to be clear`. Make the point directly.
- **Missing bridge sentences**: Each paragraph should connect to the last. If paragraphs could be rearranged without the reader noticing, add connective tissue.
- **Compulsive rule of three**: Vary groupings. Max one "adjective, adjective, and adjective" triad per piece.

### Transition Phrases to Remove
- "Moreover" / "Furthermore" / "Additionally" → restructure, or use "and," "also," "on top of that"
- "In today's [X]" / "In an era where" → cut or state specific context
- "It's worth noting that" / "Notably" → just state the fact
- "Here's what's interesting" / "Here's what caught my eye" → let the content signal its own importance
- "In conclusion" / "In summary" / "To summarize" → your conclusion should be obvious
- "When it comes to" → talk about the thing directly
- "At the end of the day" → cut
- "That said" / "That being said" → cut or use "but," "yet," or "however" (not all three)

### Structural Issues
- **Uniform paragraph length**: Vary deliberately. Include 1–2 sentence paragraphs alongside longer ones.
- **Formulaic openings**: Lead with the news or insight. Context comes second.
- **Suspiciously clean grammar**: Keep deliberate fragments, sentences starting with "And" or "But," comma splices for effect — if the natural voice uses them, keep them.
- **Excessive structure**: More than 3 headings in under 300 words is AI scaffolding. Merge or use prose transitions. Formulaic headers ("Overview," "Key Points," "Summary") — use headers that tell the reader something specific.

### Copula Avoidance
AI avoids "is" and "has" and substitutes: `serves as`, `features`, `boasts`, `presents`, `represents`. Default to "is" or "has" unless a more specific verb genuinely adds meaning.

### Synonym Cycling
AI rotates synonyms to avoid repetition: "developers… engineers… practitioners… builders." Human writers repeat the clearest word. If the same noun appears three times and it's right, keep all three.

### Vague Attributions
"Experts believe," "Studies show," "Research suggests" — without naming who. Either cite a specific source or drop the attribution and state the claim directly.

### Significance Inflation
Phrases like "marking a pivotal moment in the evolution of..." inflate routine events. State what happened. Let the reader judge significance. If the sentence works after deleting the inflation clause, delete it.

### Novelty Inflation
AI treats established concepts as if the speaker invented them: "He introduced a term," "a failure mode nobody's naming," "the insight everyone's missing." Describe what the person *did with* the concept, not that they discovered it. If unsure whether something is novel, assume it isn't.

### Emotional Flatline
"What surprised me most," "I was fascinated to discover," "What struck me was" — claiming emotions as structural crutch without earning them. If the thing is genuinely surprising, the reader should feel it from the content. If you claim an emotion, the writing around it should earn it. Otherwise cut the claim and present the thing directly.

### False Concession Structure
"While X is impressive, Y remains a challenge" — sounds balanced without weighing anything. Both halves are vague. Either make the concession specific or pick a side and argue it.

### Sycophantic Tone
"Great question!", "Excellent point!", "You're absolutely right!" — remove entirely.

### Acknowledgment Loops
"You're asking about," "To answer your question," "That's a great question. The..." — AI restates the prompt before answering. Just answer.

### Confidence Calibration Phrases
"It's worth noting that," "Interestingly," "Surprisingly," "Importantly," "Significantly," "Notably," "Certainly," "Undoubtedly" — AI signals how the reader should feel instead of letting the fact speak. Flag by density (3+ in 500 words = problem).

### Filler Phrases
- "It is important to note that" → just state it
- "In terms of" → rewrite
- "The reality is that" → cut or state the claim
- "In order to" → "to"
- "Due to the fact that" → "because"

### Promotional / Brochure Language
"Nestled within the breathtaking foothills," "a vibrant hub of innovation," "a thriving ecosystem." Replace with plain description. Numbers beat adjectives.

### Formulaic Challenges
"Despite challenges, [subject] continues to thrive." Name the actual challenge and the actual response, or cut.

### "Let's" Constructions
"Let's explore," "Let's take a look," "Let's break this down" — false-collaborative openers that delay the point. Just start with the point.

### Rhetorical Question Openers
"But what does this mean for developers?" / "So why should you care?" — if you know the answer, just say it. Rhetorical questions are earned by strong setup, not dropped as section transitions.

### Parenthetical Hedging
"(and, increasingly, Z)" / "(or, more precisely, Y)" — if the aside matters, give it its own sentence. If it doesn't, cut it.

### Reasoning Chain Artifacts
"Let me think step by step," "Breaking this down," "Step 1:," "Here's my thought process" — scaffolding leaking into prose. State the conclusion, then the evidence.

### Numbered List Inflation
"Three key takeaways" / "Five things to know" — only use when the content genuinely has that many discrete, parallel items.

### Generic Conclusions
"The future looks bright," "Only time will tell," "One thing is certain," "As we move forward" — cut. If the piece needs a closing thought, make it specific to the argument.

### Chatbot Artifacts
"I hope this helps!", "Certainly!", "Absolutely!", "Feel free to reach out," "Let me know if you need anything else," "In this article, we will explore…," "Let's dive in!" — remove entirely.

### Notability Name-Dropping
"Cited in The New York Times, BBC, Financial Times, and The Hindu" — if a source matters, use it with context. One specific reference beats four name-drops.

### Inline-Header Lists
Bullet items starting with a bold header that repeats itself: "**Performance:** Performance improved by..." — strip the bold header and write the point directly.

### Title Case Headings
Use sentence case for subheadings. Title case only for the main title.

### False Ranges
"From the Big Bang to dark matter," "from ancient civilizations to modern startups" — sweeping but empty. List actual topics or pick the one that matters.

### Superficial -ing Analyses
"Symbolizing the region's commitment to progress, reflecting decades of investment, and showcasing a new era..." — these say nothing. Replace with specific facts or cut.

---

## Word Lists

### Tier 1 — Always replace

| Replace | With |
|---|---|
| delve / delve into | explore, dig into, look at |
| landscape (metaphor) | field, space, industry, world |
| tapestry | describe the actual complexity |
| realm | area, field, domain |
| paradigm | model, approach, framework |
| embark | start, begin |
| beacon | rewrite entirely |
| testament to | shows, proves, demonstrates |
| robust | strong, reliable, solid |
| comprehensive | thorough, complete, full |
| cutting-edge | latest, newest, advanced |
| leverage (verb) | use |
| pivotal | important, key, critical |
| underscores | highlights, shows |
| meticulous / meticulously | careful, detailed, precise |
| seamless / seamlessly | smooth, easy, without friction |
| game-changer / game-changing | describe what specifically changed and why |
| utilize | use |
| watershed moment | turning point, shift |
| marking a pivotal moment | state what happened |
| the future looks bright | cut — say something specific or nothing |
| only time will tell | cut — say something specific or nothing |
| nestled | is located, sits, is in |
| vibrant | describe what makes it active, or cut |
| thriving | growing, active (or cite a number) |
| showcasing | showing, demonstrating (or cut the clause) |
| deep dive / dive into | look at, examine, explore |
| unpack / unpacking | explain, break down, walk through |
| bustling | busy, active |
| intricate / intricacies | complex, detailed (or name the specific complexity) |
| complexities | name the actual complexities, or use "problems" / "details" |
| ever-evolving | changing, growing (or describe how) |
| enduring | lasting, long-running |
| daunting | hard, difficult, challenging |
| holistic / holistically | complete, full, whole |
| actionable | practical, useful, concrete |
| impactful | effective, significant (or describe the impact) |
| learnings | lessons, findings, takeaways |
| thought leader / thought leadership | expert, authority |
| best practices | what works, proven methods, standard approach |
| at its core | cut — just state the thing |
| synergy / synergies | describe the actual combined effect |
| interplay | relationship, connection, interaction |
| in order to | to |
| due to the fact that | because |
| serves as | is |
| features (verb) | has, includes |
| boasts | has |
| presents (inflated) | is, shows, gives |
| commence | start, begin |
| ascertain | find out, determine, learn |
| endeavor | effort, attempt, try |
| keen (as intensifier) | interested, eager, enthusiastic (or cut) |
| symphony (metaphor) | describe the actual coordination |
| embrace (metaphor) | adopt, accept, use, switch to |
| hit differently / hits different | describe how, or cut |

### Tier 2 — Flag when 2+ appear in the same paragraph

| Replace | With |
|---|---|
| harness | use, take advantage of |
| navigate / navigating | work through, handle, deal with |
| foster | encourage, support, build |
| elevate | improve, raise, strengthen |
| unleash | release, enable, unlock |
| streamline | simplify, speed up |
| empower | enable, let, allow |
| bolster | support, strengthen, back up |
| spearhead | lead, drive, run |
| resonate / resonates with | connect with, appeal to, matter to |
| revolutionize | change, transform, reshape |
| facilitate / facilitates | enable, help, allow, run |
| underpin | support, form the basis of |
| nuanced | specific, subtle, detailed (or name the actual nuance) |
| crucial | important, key, necessary |
| multifaceted | describe the actual facets, or cut |
| ecosystem (metaphor) | system, community, network, market |
| myriad | many, numerous (or give a number) |
| plethora | many, a lot of (or give a number) |
| encompass | include, cover, span |
| catalyze | start, trigger, accelerate |
| reimagine | rethink, redesign, rebuild |
| galvanize | motivate, rally, push |
| augment | add to, expand, supplement |
| cultivate | build, develop, grow |
| illuminate | clarify, explain, show |
| elucidate | explain, clarify, spell out |
| juxtapose | compare, contrast, set side by side |
| paradigm-shifting | describe what actually shifted |
| transformative / transformation | describe what changed and how |
| cornerstone | foundation, basis, key part |
| paramount | most important, top priority |
| poised (to) | ready, set, about to |
| burgeoning | growing, emerging (or cite a number) |
| nascent | new, early-stage, emerging |
| quintessential | typical, classic, defining |
| overarching | main, central, broad |
| underpinning / underpinnings | basis, foundation, what supports |

### Tier 3 — Flag only at high density (3%+ of total words)

| Word | What to do |
|---|---|
| significant / significantly | Replace some with specifics: numbers, comparisons, examples |
| innovative / innovation | Describe what's actually new |
| effective / effectively | Say how or cite a metric |
| dynamic / dynamics | Name the actual forces or changes |
| scalable / scalability | Describe what scales and to what |
| compelling | Say why it compels |
| unprecedented | Name the precedent it breaks, or cut |
| exceptional / exceptionally | Cite what makes it an exception |
| remarkable / remarkably | Say what's worth remarking on |
| sophisticated | Describe the sophistication |
| instrumental | Say what role it played |
| world-class / state-of-the-art / best-in-class | Cite a benchmark or comparison |

---

## Rhythm and Uniformity

**Structure is the #1 detection signal.** Structural regularity is harder to mask than swapping flagged words. If you fix every Tier 1 word but leave the rhythm untouched, the text still reads as AI.

- **Sentence length uniformity**: Mix short punchy sentences (3–8 words) with longer ones (20+). Fragments work. Questions break the monotony.
- **Paragraph length uniformity**: Some paragraphs should be one sentence. Some should be longer. Vary deliberately.
- **Read-aloud test**: If the text sounds like it could be read by text-to-speech without sounding weird, it's too uniform.
- **Missing first-person perspective**: If the piece is supposed to have a voice, the absence of "I think" or a stated preference is itself an AI tell.
- **Over-polishing warning**: Don't sand away all personality. Natural disfluency, idiosyncratic word choices, and uneven pacing keep text out of the "AI-generated" bucket. This skill should make writing sound more human, not less.

---

## When to Rewrite from Scratch

If the text has **all three**: 5+ Tier 1 vocabulary hits, 3+ distinct pattern categories triggered, and uniform sentence/paragraph length — patching won't fix it. The structure itself is AI-generated. Advise a full rewrite: state the core point in one sentence, then rebuild from there.

---

## Tone Calibration

Five principles for human-sounding rewrites:
1. **Vary sentence length** — mix short with long. Fragments are fine.
2. **Be concrete** — replace vague claims with numbers, names, dates, or examples.
3. **Have a voice** — where appropriate, use first person, state preferences, show reactions.
4. **Cut the neutrality** — humans have opinions. If the piece takes a position, take it.
5. **Earn your emphasis** — don't tell the reader something is interesting. Make it interesting.

If the original writing is already strong, say so and make only the necessary cuts. The replacement table provides defaults, not mandates — if a flagged word is clearly right in context, keep it.

---

## Self-Reference Escape Hatch

When writing *about* AI writing patterns, quoted examples are exempt. Text inside quotation marks, code blocks, or explicitly marked as illustrative ("for example, AI might write...") should not be rewritten. Only flag patterns in the author's own prose.
