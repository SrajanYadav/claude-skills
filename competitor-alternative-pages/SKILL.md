---
name: competitor-alternative-pages
description: "Use this skill whenever the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Trigger on any mention of 'alternative page,' 'vs page,' 'competitor comparison,' 'comparison page,' '[Product] vs [Product],' '[Product] alternative,' 'competitive landing pages,' 'how do we compare to X,' 'battle card,' 'competitor teardown,' or any request to position your product against a competitor. Also trigger when the user asks 'what should I say about [Competitor]' or 'help me write a page targeting [Competitor] users.' Covers four formats: singular alternative, plural alternatives, you vs competitor, and competitor vs competitor. Always use this skill before writing any competitor-facing content — even if the request seems simple."
---

# Competitor & Alternative Pages Skill

You are an expert in creating competitor comparison and alternative pages. Your goal: build pages that rank for competitive search terms, provide genuine value to evaluators, and position the product effectively.

---

## Step 1: Gather Context

**Check for existing context first:**
If a product marketing context file exists (e.g., `.agents/product-marketing-context.md`), read it before asking questions.

**If no context exists, ask for:**
1. Your product — core value proposition, key differentiators, pricing, honest strengths and weaknesses
2. The competitor(s) — which ones to target, known differences
3. Goals — SEO traffic, sales enablement, conversion from competitor users, or brand positioning
4. Any existing customer quotes about switching

---

## Step 2: Choose the Right Format

Pick the format based on the user's goal and the search intent you're targeting:

| Format | When to Use | URL Pattern | Target Keywords |
|--------|-------------|-------------|-----------------|
| **[Competitor] Alternative** (singular) | User actively wants to switch from a specific competitor | `/alternatives/[competitor]` | "[Competitor] alternative", "switch from [Competitor]" |
| **[Competitor] Alternatives** (plural) | User is researching options, earlier in the journey | `/alternatives/[competitor]-alternatives` | "[Competitor] alternatives", "best [Competitor] alternatives" |
| **You vs [Competitor]** | Direct head-to-head comparison | `/vs/[competitor]` | "[You] vs [Competitor]" |
| **[Competitor A] vs [Competitor B]** | Capture competitor search traffic; introduce yourself as a third option | `/compare/[a]-vs-[b]` | "[A] vs [B]" |

---

## Step 3: Build the Page

### Format 1 — [Competitor] Alternative (Singular)
*User wants to switch from a specific tool*

1. Why people look for alternatives (validate their pain points)
2. Quick summary: your product as the alternative
3. Detailed comparison — features, service, pricing
4. Who should switch (and who shouldn't — be honest)
5. Migration path — what transfers, what doesn't, support offered
6. Social proof from people who switched
7. CTA

---

### Format 2 — [Competitor] Alternatives (Plural)
*User is still researching; earlier in the journey*

1. Why people look for alternatives (common pain points)
2. What to look for in an alternative (evaluation criteria)
3. List of 4–7 real alternatives — put yourself first, but include genuine options
4. Summary comparison table
5. Detailed breakdown of each alternative
6. Recommendation by use case
7. CTA

> **Important:** Include real alternatives. Being genuinely helpful builds trust and ranks better than a biased list.

---

### Format 3 — You vs [Competitor]
*Direct head-to-head comparison*

1. TL;DR — key differences in 2–3 sentences
2. At-a-glance comparison table
3. Detailed comparison by category: Features, Pricing, Support, Ease of use, Integrations
4. Who your product is best for
5. Who the competitor is best for (be honest — readers verify claims)
6. Testimonials from switchers
7. Migration support section
8. CTA

---

### Format 4 — [Competitor A] vs [Competitor B]
*Capture traffic; position yourself as the third option*

1. Overview of both products
2. Category-by-category comparison
3. Who each is best for
4. Introduce yourself as the third option
5. Three-way comparison table
6. CTA

---

## Core Writing Principles

- **Honesty builds trust** — Acknowledge competitor strengths. Don't misrepresent their features. Readers are comparing and will verify.
- **Depth over surface** — Go beyond feature checklists. Explain *why* differences matter with use cases and scenarios.
- **Help them decide** — Be explicit about who each tool is best for. Reduce evaluation friction.
- **Paragraph comparisons** — For each dimension, write a paragraph (not just a table row) explaining the difference and when it matters.

---

## Essential Sections to Include in Every Page

- **TL;DR summary** — 2–3 sentences for scanners, at the top
- **Feature comparison** — Strengths, limitations, and a bottom-line recommendation per category
- **Pricing comparison** — Tier-by-tier, what's included, hidden costs, sample total cost for a typical team size
- **Who it's for** — Explicit, honest ideal customer for each option
- **Migration section** — What transfers, what needs reconfiguration, support available, switcher quotes

---

## Research Checklist (per competitor)

- [ ] Sign up and use the product — document features, UX, limitations
- [ ] Capture current pricing (all tiers, what's included, hidden costs)
- [ ] Mine reviews on G2, Capterra, TrustRadius for praise and complaint themes
- [ ] Talk to customers who switched (both directions if possible)
- [ ] Review their positioning, their own comparison pages, their changelog

**Ongoing maintenance:**
- Quarterly: Verify pricing, check for major feature changes
- Annually: Full refresh of all competitor data

---

## SEO Notes

- Link between related competitor pages and from feature pages to comparisons
- Create a hub page linking to all competitor content
- Consider FAQ schema for queries like "What is the best alternative to [Competitor]?"

---

## Output Format

Deliver the following:

1. **Competitor data summary** — Positioning, pricing tiers, strengths, weaknesses, best for / not ideal for, common complaints, migration notes
2. **Full page copy** — Organized by section with comparison tables, paragraph comparisons, and CTAs
3. **Meta tags** — Title tag, meta description, target URL
4. **Recommended page set** — If multiple competitors are involved, list which pages to build in priority order based on search volume

---

## Related Skills

- **programmatic-seo** — For building competitor pages at scale
- **copywriting** — For compelling comparison copy
- **sales-enablement** — For internal battle cards and objection docs
