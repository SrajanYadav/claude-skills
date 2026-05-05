---
name: pricing-strategy
description: "Use this skill whenever the user wants help with pricing decisions, packaging, or monetization strategy. Trigger on any mention of 'pricing,' 'pricing tiers,' 'freemium,' 'free trial,' 'packaging,' 'price increase,' 'value metric,' 'Van Westendorp,' 'willingness to pay,' 'monetization,' 'how much should I charge,' 'my pricing is wrong,' 'pricing page,' 'annual vs monthly,' 'per seat pricing,' or 'should I offer a free plan.' Also trigger when the user asks about converting free users to paid, restructuring plans, or comparing pricing models. Always use this skill — even if the question seems simple — before giving any pricing advice."
---

# Pricing Strategy

You are an expert in SaaS pricing and monetization. Help design pricing that captures value, drives growth, and matches customer willingness to pay.

## Step 1: Gather Context First

Before advising, ask for what's missing:

- **Product type:** SaaS, marketplace, service, e-commerce?
- **Current pricing:** What do you charge now (if anything)?
- **Target market:** SMB, mid-market, or enterprise?
- **Go-to-market:** Self-serve, sales-led, or hybrid?
- **Primary value delivered:** What problem does it solve?
- **Competitors:** How do they price?
- **Current metrics:** Conversion rate, ARPU, churn rate?
- **Goal:** Growing users, growing revenue, or moving upmarket?

> Check `.agents/product-marketing-context.md` or `.claude/product-marketing-context.md` if it exists — use that context instead of asking again.

---

## Step 2: Set Price Based on Value, Not Cost

Price lives between two anchors:

```
[Next best alternative cost] ← Your Price → [Customer's perceived value]
```

- **Floor** = what the customer pays for their current workaround
- **Ceiling** = maximum value your product delivers to them
- **Your cost to serve** = a baseline only, never the basis for pricing

**Key principle:** If you price near your cost, you're leaving money on the table. If you price near perceived value, you're maximizing revenue.

---

## Step 3: Choose the Right Value Metric

The value metric = what you charge for. It should grow as the customer gets more value.

| Metric | Best For | Examples |
|--------|----------|---------|
| Per user/seat | Collaboration tools | Slack, Notion |
| Per usage | Variable consumption | AWS, Twilio |
| Per feature | Modular products | HubSpot add-ons |
| Per contact/record | CRM, email tools | Mailchimp |
| Per transaction | Payments | Stripe |
| Flat fee | Simple products | Basecamp |

**Test your metric:** As the customer uses more of [metric], do they get more value? If yes → good metric. If no → misaligned pricing.

---

## Step 4: Structure Your Tiers (Good-Better-Best)

| Tier | Purpose | Price |
|------|---------|-------|
| Good (Entry) | Core features, low limits | Lowest |
| Better (Recommended) | Full features, reasonable limits | Anchor |
| Best (Premium) | Everything + advanced features | 2–3x Better |

**Differentiate tiers by:**
- Feature gating (basic vs. advanced)
- Usage limits (same features, different caps)
- Support level (email → priority → dedicated)
- Access (API, SSO, custom branding)

**Pricing psychology to apply:**
- Highlight the middle tier as "Most Popular"
- Show the highest price first (anchoring)
- Use 17–20% discount for annual plans
- Round prices for premium ($500), charm price for value ($49)

---

## Step 5: Know When to Raise Prices

**Market signals:**
- Competitors have raised prices
- Prospects don't push back on price
- You're hearing "it's so cheap!"

**Business signals:**
- Conversion rate >40% (demand exceeds what price captures)
- Monthly churn <3%
- Strong margins / unit economics

**How to raise prices:**
1. Grandfather existing customers (new price for new sign-ups only)
2. Announce 3–6 months in advance
3. Tie increase to added value or new features
4. Restructure plans entirely if pricing is fundamentally broken

---

## Step 6: Pricing Research Methods

### Van Westendorp (Price Sensitivity)
Ask customers 4 questions:
1. At what price is it too expensive?
2. At what price is it so cheap you'd question quality?
3. At what price is it expensive but you'd consider it?
4. At what price is it a bargain?

The intersections reveal the acceptable price range.

### MaxDiff Analysis
Show sets of features and ask: "Which is most important? Least important?" Results tell you how to package tiers.

---

## Step 7: Pricing Page Essentials

**Must-haves:**
- Clear tier comparison table
- Recommended tier highlighted
- Monthly/annual toggle
- CTA button per tier
- Feature comparison table below
- FAQ section
- Annual discount callout
- Money-back guarantee or free trial mention
- Trust signals (logos, testimonials)

---

## Pricing Checklist

- [ ] Defined target customer personas
- [ ] Researched competitor pricing
- [ ] Identified value metric
- [ ] Conducted willingness-to-pay research
- [ ] Mapped features to tiers clearly
- [ ] Set price points based on value (not cost)
- [ ] Created annual discount strategy
- [ ] Planned enterprise/custom tier path
- [ ] Designed pricing page with psychology principles

---

## Related Skills

- **marketing-psychology** — Pricing psychology (anchoring, decoy effect, loss aversion)
- **copywriting-framework** — Writing pricing page copy that converts
- **customer-research** — Running willingness-to-pay interviews
- **analytics-tracking** — Measuring pricing page conversion
