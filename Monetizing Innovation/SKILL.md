---
name: monetizing-innovation
description: "Designs products around price using the 9 rules from Ramanujam and Tacke. Use this skill whenever the user is: designing a new product or feature, validating pricing for SaaS/B2B/B2C launches, choosing between subscription/usage/freemium/dynamic models, diagnosing why a product launch failed or is underperforming, fixing post-launch sales below plan, hearing 'let's price it later' from their team, trying to configure Good/Better/Best tiers, figuring out what to charge and how to charge it, or doing WTP (willingness-to-pay) research. Also trigger when user mentions: feature shock, minivation, hidden gem, undead product, price integrity, bundling, monetization model, willingness to pay, value communication, or behavioral pricing. Not for pure commodities or cost-plus regulated environments."
---

# Monetizing Innovation

> "Design the product around the price." — Ramanujam & Tacke

## Core Principle

**72% of new products fail** because pricing is decided LAST. The fix: treat price as an input to product design, not an output.

| Old Paradigm | New Paradigm |
|---|---|
| Design → Build → Market → Price | Price & Market → Design → Build |

Only ~5% of business cases include real WTP data. Fix this first.

> ⚠️ The 72% figure comes from Simon-Kucher's own client survey (the book's authors are principals there). Treat as directionally correct, not independently verified.

---

## Step 0: Diagnose the Failure Type First

Before prescribing anything, identify which failure type applies.

| Failure | Definition | Tell-Tale Signs |
|---|---|---|
| **Feature Shock** | Too many features → confusing, overpriced | Can't articulate value; price slashed post-launch |
| **Minivation** | Right product, priced too low | Sales hits target easily; channel maxes margin; sellouts |
| **Hidden Gem** | Great idea never properly launched | Mid-level execs kill it; sold as deal sweetener |
| **Undead** | Wrong answer, or no question asked | Sales avoids it; pet project of senior leadership |

**Real examples:** Amazon Fire Phone = Feature Shock ($170M write-down). Audi Q7 = Minivation (missed €210M/yr). Kodak digital camera 1974 = Hidden Gem. Segway = Undead.

→ Full case studies: see [references/cases.md](references/cases.md)

---

## The 9 Rules (Quick Reference)

| # | Rule | One-Line Summary |
|---|---|---|
| 1 | **WTP Talk Early** | Have it before design freezes — not weeks before launch |
| 2 | **Needs-Based Segmentation** | Segment by value/WTP, not demographics |
| 3 | **Configuration & Bundling** | Leaders/Fillers/Killers + Good/Better/Best with FENCES |
| 4 | **How You Charge > What You Charge** | Pick the right monetization model |
| 5 | **Pricing Strategy** | Maximization / Penetration / Skimming — pick one |
| 6 | **Living Business Case** | Link Price–Value–Volume–Cost; update at every milestone |
| 7 | **Value Communication** | Sell benefits, not features. Use MOCA matrix |
| 8 | **Behavioral Pricing** | 6 tactics: compromise, anchoring, signals, razor-blade, pennies-a-day, thresholds |
| 9 | **Maintain Price Integrity** | Don't cut after launch. Try 3 non-price actions first |

→ Full detail on all 9 rules: see [references/frameworks.md](references/frameworks.md)

---

## Critical Frameworks (At-a-Glance)

### Leaders / Fillers / Killers

| Type | Definition | Action |
|---|---|---|
| **Leader** | Drives buying decision, high WTP | Always include |
| **Filler** | Nice-to-have | Use to fill gaps |
| **Killer** | Blows the deal if forced to pay | Remove or sell à la carte |

**Killer test:** Valued by <20% of customers AND not valued at all by >20%. Segment-dependent (heated seats = Leader in Norway, Killer in Mumbai).

### Good / Better / Best Distribution

| Distribution | Diagnosis |
|---|---|
| ≤25% Good, ~70% Better+Best, ≥10% Best | Healthy |
| >50% picking Good | Trip-wire: strip features from Good tier |
| Best <10% | Premium tier underpowered |

**Fences are mandatory.** Without visible, defensible differences between tiers, G/B/B cannibalizes itself. Fence test: Can a customer see in 10 seconds what's missing from Good?

### The 5 Monetization Models

| Model | When to Use | Example |
|---|---|---|
| **Subscription** | Continual usage; lock out competitors | Netflix, Adobe |
| **Dynamic Pricing** | Volatile demand or constrained supply | Uber, airlines |
| **Auctions** | Seller's market, constrained inventory | Google AdWords |
| **Pay-As-You-Go / Alt Metric** | Usage tracks value | Michelin (per mile), GE engines |
| **Freemium** | Near-zero production AND fixed cost | LinkedIn, Dropbox |

⚠️ **Freemium warning:** Fails for 90% of companies. Software conversion typically <10%. Don't use if your cost-to-serve the free tier is meaningful.

Models are mix-and-matchable (Costco = subscription + per-product).

### The 6 Behavioral Pricing Tactics

1. **Compromise effect** — Always offer 3 tiers; people avoid extremes
2. **Anchoring** — Add a decoy; The Economist test lifted bundle pick rate from 32% → 84%
3. **Price signals quality** — Ariely placebo: $2.50 pill = 85% pain relief; $0.10 same pill = 61%
4. **Razor / razor blades** — Low upfront preferred even if 12-month total is identical
5. **Pennies-a-day** — $9.99/mo converts very differently from $120/yr
6. **Psychological thresholds** — $69.99 works; $71 drops acceptance >20%

---

## Decision Trees

### "Is my product likely to fail?"

```
Can I clearly state the customer BENEFIT (not features)?
├─ NO  → Likely Feature Shock
└─ YES → Has WTP been validated with real customers?
         ├─ NO  → Could be Undead or Minivation
         └─ YES → Did C-suite engage personally?
                  ├─ NO  → Likely Hidden Gem
                  └─ YES → On the right track
```

### "Which monetization model?"

```
Is value tied to usage volume?
├─ YES → Alternative Metric (Michelin model)
└─ NO  → Is demand volatile or supply constrained?
         ├─ YES → Dynamic Pricing
         └─ NO  → Is production cost near zero?
                  ├─ YES → Freemium (only if free users still profitable)
                  └─ NO  → Subscription or per-unit
```

### "Should I cut the price?"

```
Sales below plan?
└─ YES → Root cause identified?
         ├─ NO  → Diagnose first (usually NOT a price problem)
         └─ YES → Is it pricing-specific?
                  ├─ NO  → Fix the actual problem
                  └─ YES → Tried 3 non-price actions first?
                           ├─ NO  → Try: advertise more / add value / upgrade customer
                           └─ YES → War-game competitor reaction
                                    └─ Worse off after their counter? → Don't cut
```

---

## The BECAUSE Test

Every pricing decision must end with a "because" traceable to customer data.

**Bad:** "We priced at $99 to be competitive."

**Good:** "We priced at $99 BECAUSE 60% of segment B said $100 was the threshold above which they'd reconsider, and our value advantage justifies the high end."

**Template:**
```
We priced [tier] at $[X] BECAUSE [N]% of [segment] customers told us
[specific WTP/threshold data point], AND [secondary data on competitive
position or upgrade willingness].
```

If you can't fill in this template, you don't have a pricing strategy — you have a guess.

---

## Key Numbers to Remember

| Number | Rule |
|---|---|
| 72% | New products fail |
| 80% | Companies wait until pre-launch to set price |
| 5% | Business cases include real WTP data |
| 3–4 | Ideal starting number of segments |
| <10% | Threshold to call something a "Killer" feature |
| ≤25% / ~70% / ≥10% | G/B/B healthy split (Good / Better+Best / Best) |
| 50% | Trip-wire: more than this picking Good = problem |
| 3 | Non-price actions required before any price cut |
| 25% | Of WTP interview questions should be "Why?" |

---

## Startup / Solo Founder Lite Path

The full 9-rule process assumes a cross-functional team and survey budget. If you don't have that:

1. **Talk to 10 customers about the problem** — what are they doing today and what does it cost them?
2. **Ask directly:** "What would you pay?" and "What's the most you'd pay?" Weight the middle responses; ignore anchoring-low instinct answers.
3. **Test 3 price points:** low (everyone says yes), medium (most say yes), high (some say yes). Pick for the right segment, not maximum close rate.
4. **One clean offer for v1** — skip G/B/B until you know which features people actually use.
5. **Launch at medium price; iterate on actual conversion data** — win/loss patterns teach more than any survey at this stage.

> Skip conjoint analysis, Van Westendorp, and Gabor-Granger until you have 200+ respondents.

---

## WTP Research Caveat

Stated WTP ≠ Revealed WTP. Customers predict their own behavior poorly in interviews.

**Always validate with:**
- Paid pilots (not free betas — skin in the game changes answers)
- Pre-orders or letters of intent
- Live A/B price tests
- Money-back guarantees while testing

Treat WTP research as a strong prior, not a fact.

---

## Quick Launch Checklist

- [ ] WTP conversations held with real customers (≥10)
- [ ] Segmented by needs/value/WTP — not demographics
- [ ] Leaders, Fillers, Killers identified
- [ ] G/B/B configured with visible FENCES
- [ ] Monetization model chosen explicitly
- [ ] Pricing strategy documented (max / penetration / skimming)
- [ ] Living business case links Price / Value / Volume / Cost
- [ ] Messaging tested on benefits, not features
- [ ] Behavioral tactics considered
- [ ] Team prepared to hold price post-launch

**The acid test:** Ask anyone "Why this price?" If the answer is "cost-plus" or "what competitors charge" — failure is likely coming.

---

## Reference Files

- **[references/frameworks.md](references/frameworks.md)** — Full detail on all 9 rules, sub-frameworks, WTP question methods, bundling insights, post-launch tips
- **[references/cases.md](references/cases.md)** — Detailed case studies: Porsche, Gillette India, LinkedIn, Dräger, Uber, Apple Watch, BMW 7 Series, and all failure exemplars
- **[references/examples.md](references/examples.md)** — Worked examples: bundling math, BECAUSE test templates, MOCA matrix, value-selling spreadsheet, behavioral pricing experiments
