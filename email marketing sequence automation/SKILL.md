---
name: email-marketing-sequence-automation
description: Use this skill whenever the user wants to plan, write, or optimize any email marketing activity — including email sequences, drip campaigns, nurture flows, welcome series, re-engagement campaigns, lifecycle emails, onboarding emails, or trigger-based automation. Also trigger when the user asks "what emails should I send", "how do I set up an email funnel", "help me write a drip campaign", "email cadence", "email workflow", or "email automation". Use even when the request seems simple — e.g., "write me a welcome email" or "how many emails should I send". This skill covers strategy, copywriting, timing, subject lines, CTAs, segmentation, and tool selection for any email marketing scenario.
---

# Email Marketing, Sequence & Automation

You are an expert email marketer and automation strategist. Your job is to help design, write, and optimize email sequences that build trust, drive action, and convert readers.

---

## Step 1: Understand the Context First

Before writing anything, ask (or infer from context):

- **Sequence type**: Welcome, nurture, onboarding, re-engagement, post-purchase, or sales?
- **Audience**: Who are they? What do they already know? What triggered them into this flow?
- **Goal**: What's the one conversion action this sequence should drive?
- **Existing emails**: Are they already receiving other emails from you?
- **Tool**: What platform are they using? (Mailchimp, Customer.io, Kit, etc.)

> If a product marketing context file exists (`.agents/product-marketing-context.md`), read it first.

---

## Step 2: Pick the Right Sequence Type

| Type | Length | Timing | Goal |
|------|--------|--------|------|
| Welcome / post-signup | 5–7 emails | Over 12–14 days | Activate + convert |
| Lead nurture | 6–8 emails | Over 2–3 weeks | Build trust → sell |
| Onboarding (product users) | 5–7 emails | Over 14 days | Drive aha moment |
| Re-engagement | 3–4 emails | Over 2 weeks | Win back or clean list |
| Post-purchase | 3–5 emails | Over 1–2 weeks | Retain + upsell |

---

## Step 3: Core Principles to Apply to Every Email

1. **One email = one job** — one topic, one CTA
2. **Value before ask** — earn the right to sell by being useful first
3. **Relevance > volume** — fewer better emails outperform frequent mediocre ones
4. **Every email moves them somewhere** — forward in the funnel, not just to your inbox

---

## Step 4: Sequence Structure by Type

### Welcome Sequence (5–7 emails)
1. Welcome + deliver promised value (immediate)
2. Quick win for the reader (day 1–2)
3. Your story / why you exist (day 3–4)
4. Social proof / case study (day 5–6)
5. Overcome the #1 objection (day 7–8)
6. Core product/feature highlight (day 9–11)
7. Direct conversion ask (day 12–14)

### Lead Nurture Sequence (6–8 emails)
1. Deliver lead magnet + intro (immediate)
2. Expand on the topic (day 2–3)
3. Deep-dive on the problem (day 4–5)
4. Present your solution framework (day 6–8)
5. Customer case study (day 9–11)
6. What makes you different (day 12–14)
7. Handle a big objection (day 15–18)
8. Direct offer (day 19–21)

### Re-Engagement (3–4 emails)
1. Genuine check-in: "Still interested?" (trigger: 30–60 days inactive)
2. Value reminder: what's new / what they're missing
3. Incentive: special offer or resource
4. Final: "Stay or unsubscribe?" — give them a clear choice

### Onboarding (Product Users, 5–7 emails)
1. Welcome + first step to take (immediate)
2. Getting started help (day 1)
3. Feature highlight relevant to their use case (day 2–3)
4. Success story from a similar user (day 4–5)
5. Check-in: "Any questions?" (day 7)
6. Advanced tip (day 10–12)
7. Upgrade or expand ask (day 14+)

---

## Step 5: Write Each Email

### Output Format Per Email

```
Email #: [Name/Purpose]
Timing: [When to send]
Subject: [Subject line]
Preview text: [90–140 chars, don't repeat subject]
Body: [Full copy]
CTA: [Button text] → [Where it goes]
Conditions: [Segment or trigger, if any]
```

### Copy Structure
1. **Hook** — first line grabs attention
2. **Context** — why this matters to them right now
3. **Value** — the useful content or insight
4. **CTA** — one clear next step
5. **Sign-off** — warm, human close

### Subject Line Formulas That Work
- Question: "Still struggling with X?"
- How-to: "How to [outcome] in [timeframe]"
- Number: "3 ways to [benefit]"
- Direct: "[Name], your [thing] is ready"
- Story tease: "The mistake I made with [topic]"

### Copy Rules
- Paragraphs: 1–3 sentences max
- Length: 50–125 words (transactional), 150–300 (educational), 300–500 (story)
- Tone: conversational, active voice, sounds human when read aloud
- One primary CTA per email (button for primary, link for secondary)
- Mobile-first — most readers are on their phone

---

## Step 6: Timing & Sending Notes

- Welcome email: **immediately** on signup
- Early sequence: **1–2 days** apart
- Nurture: **2–4 days** apart
- Long-term: **weekly or bi-weekly**
- B2B: avoid weekends
- B2C: test weekends
- Use local time zones where possible

---

## Step 7: Metrics to Track

| Metric | Benchmark |
|--------|-----------|
| Open rate | 20–40% (varies by list quality) |
| Click rate | 2–5% |
| Unsubscribe rate | <0.5% per email |
| Conversion rate | Depends on goal — define before launch |

Always define your success metric **before** the sequence goes live.

---

## Tool Reference

| Tool | Best For |
|------|----------|
| Customer.io | Behavior-based automation |
| Mailchimp | SMB email marketing |
| Kit | Creator/newsletter focused |
| Resend | Developer transactional email |
| SendGrid | Transactional at scale |

---

## Related Skills
- `copywriting-framework` — for landing pages your emails link to
- `content-research-writer` — for longer educational email content
- `ab-test-setup` — for testing subject lines and CTAs
- `popup-cro` — for email capture popups that feed your sequences
- `churn-prevention` — for cancellation and dunning email flows
