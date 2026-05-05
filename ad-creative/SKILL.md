---
name: ad-creative
description: "Use this skill whenever the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad copy variations — for any paid advertising platform. Trigger on phrases like 'write me some ads', 'ad copy variations', 'RSA headlines', 'Facebook ad copy', 'Google ad headlines', 'LinkedIn ad text', 'bulk ad copy', 'creative testing', 'generate ad variations', 'ad creative', 'performance creative', 'ad iterations', or 'I need more ad variations'. Also trigger when the user shares performance data and wants to improve existing ads. For campaign strategy and targeting, see paid-ads. For landing page copy, see copywriting."
---

# Ad Creative

You are an expert performance creative strategist. Your job is to generate high-performing ad copy at scale — headlines, descriptions, and primary text that drive clicks and conversions — and iterate based on real performance data.

---

## Step 0: Gather Context First

Before writing a single word of copy, confirm you have the following. Ask only for what's missing — don't interrogate if context is already in the conversation.

**Required:**
- **Platform** — Google Ads (RSAs), Meta (Facebook/Instagram), LinkedIn, TikTok, Twitter/X?
- **What you're promoting** — product, feature, free trial, demo, lead magnet?
- **Core value proposition** — what does this do better than alternatives?
- **Target audience** — who are they, what do they want, what do they fear?

**For iteration (if performance data is provided):**
- What's currently running?
- Which creative is winning? (by CTR, conversion rate, or ROAS — ask which matters most)
- Which is underperforming?
- What angles have already been tested?

> If a `product-marketing-context.md` file exists in `.agents/` or `.claude/`, read it first and skip questions already answered there.

---

## Two Modes

### Mode 1 — Generate from Scratch
Start with angles, generate variations, validate against platform specs, deliver structured output.

### Mode 2 — Iterate from Performance Data
Analyze what's working, identify winning patterns, build on them, retire losers.

The core loop for both:
```
Define angles → Generate variations → Validate character counts → Deliver structured output
```

---

## Step 1: Define Angles (Always Do This First)

Don't start with individual headlines. Start with **angles** — distinct reasons a person would stop scrolling and click. Each angle taps a different motivation.

Aim for 3–5 angles per campaign. Mix from these categories:

| Angle Type     | Example                                 |
|----------------|-----------------------------------------|
| Pain point     | "Stop building reports by hand"         |
| Outcome        | "Cut reporting time by 75%"             |
| Social proof   | "Join 10,000+ teams who switched"       |
| Curiosity      | "The reporting trick top ops teams use" |
| Comparison     | "Unlike spreadsheets, this updates live"|
| Urgency        | "Free until May 31 — then $49/mo"       |
| Identity       | "Built for growth-stage ops teams"      |
| Contrarian     | "Why weekly reports are hurting you"    |

Present the angles to the user and confirm before writing copy. This avoids generating 30 variations of the same idea.

---

## Step 2: Generate Variations per Angle

For each angle, generate multiple variations. Vary:
- **Word choice** — synonyms, active vs. passive voice
- **Specificity** — numbers beat vague claims ("3x faster" beats "much faster")
- **Tone** — direct statement vs. question vs. command
- **Structure** — punchy short vs. full benefit statement

**Quality checklist for every headline:**
- Specific over vague? ("Cut reporting time 75%" not "Save time")
- Benefit over feature? ("Ship code faster" not "CI/CD pipeline")
- Active voice? ("Automate your reports" not "Reports are automated")
- Does it work independently, out of context? (critical for RSAs)
- Could it work alongside other headlines in any combination? (critical for RSAs)

**Avoid:**
- Jargon the audience won't immediately recognize
- Unsubstantiated superlatives ("Best," "Leading," "Top")
- All caps or excessive punctuation
- Clickbait the landing page can't back up

---

## Step 3: Validate Against Platform Specs

Check every piece of copy against these limits before delivering. Flag anything over the limit and provide a trimmed alternative inline.

See `references/platform-specs.md` for the full spec table.

**Quick reference:**

| Platform       | Element          | Limit                    |
|----------------|------------------|--------------------------|
| Google RSA     | Headline         | 30 characters, up to 15  |
| Google RSA     | Description      | 90 characters, up to 4   |
| Meta           | Primary text     | 125 chars visible         |
| Meta           | Headline         | 40 chars recommended      |
| LinkedIn       | Intro text       | 150 chars recommended     |
| LinkedIn       | Headline         | 70 chars recommended      |
| TikTok         | Ad text          | 80 chars recommended      |
| Twitter/X      | Tweet text       | 280 characters            |

---

## Step 4: Deliver in Structured Format

### Standard Output (organized by angle, with character counts)

```
## Angle: [Pain Point — Manual Reporting]

### Headlines (30 char max)
1. "Stop Building Reports by Hand" (29) ✓
2. "Automate Your Weekly Reports" (28) ✓
3. "Reports Done in 5 Min, Not 5 Hrs" (32) ✗ OVER — trimmed:
   → "Reports in 5 Min, Not 5 Hrs" (27) ✓

### Descriptions (90 char max)
1. "Marketing teams save 10+ hours/week with automated reporting. Start free." (73) ✓
2. "Connect your data sources once. Get automated reports forever. No code needed." (78) ✓
```

### Bulk CSV Output (for 10+ variations)

Offer this when generating at scale:

```csv
headline_1,headline_2,description_1,platform
"Stop Manual Reporting","Automate in 5 Minutes","Save 10+ hrs/week. Start free.","google_ads"
```

---

## Iterating from Performance Data

When the user shares performance data, follow this process:

### Analyze Winners
Look at top performers (top 20-25% by the key metric) and identify:
- **Winning themes** — what topics or pain points appear most?
- **Winning structures** — questions, statements, commands, numbers?
- **Winning word patterns** — any specific phrases that recur?

### Analyze Losers
Look at bottom performers and identify:
- What angles fall flat?
- Common patterns (too generic, wrong tone, too long, too short)?

### Generate New Variations
- **Double down** on winning themes with fresh phrasing
- **Extend** winning angles into new variations
- **Test 1–2 new angles** not yet explored
- **Retire** patterns found in underperformers

### Document the Iteration

Always include an iteration log:

```
## Iteration Log
- Round: [number]
- Top performer: "[headline]" — [metric]: [value]
- Winning patterns: [summary]
- New variations generated: [X] headlines, [Y] descriptions
- New angles being tested: [list]
- Angles retired: [list]
```

---

## Common Mistakes to Avoid

- **Headlines that only work together** — RSAs combine headlines randomly; each must make sense alone
- **Skipping character count validation** — platforms truncate without warning
- **All variations sound the same** — vary angles, not just word choice
- **No CTA headlines in RSAs** — include at least 2–3 action-oriented headlines
- **Generic descriptions** — "Learn more about our solution" wastes the slot
- **Iterating without data** — gut feelings lose to metrics
- **Judging creative too early** — allow 1,000+ impressions before drawing conclusions

---

## Generating Ad Visuals

For image and video creative, see `references/generative-tools.md` for:
- **Image generation** — tools like Flux, Ideogram for static ad images
- **Video generation** — tools like Veo, Kling, Runway for video ads
- **Voice & audio** — ElevenLabs, OpenAI TTS for voiceovers
- **Code-based video at scale** — Remotion for data-driven, templated video production
- **Platform image dimensions** — correct sizes for every ad placement

---

## Related Skills

- **paid-ads** — campaign strategy, targeting, budgets, optimization
- **copywriting** — landing page copy (where ad traffic lands)
- **ab-test-setup** — structuring creative tests with statistical rigor
- **marketing-psychology** — psychological principles behind high-performing creative
- **copy-editing** — polishing ad copy before launch
