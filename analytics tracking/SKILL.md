---
name: analytics-tracking
description: Use this skill whenever the user wants to set up, improve, or audit analytics tracking and measurement. Trigger on any mention of "set up tracking," "GA4," "Google Analytics," "conversion tracking," "event tracking," "UTM parameters," "tag manager," "GTM," "analytics implementation," "tracking plan," "how do I measure this," "track conversions," "attribution," "Mixpanel," "Segment," "are my events firing," or "analytics isn't working." Also trigger when someone asks how to know if a campaign or feature is working, wants to measure marketing results, or needs to understand user behavior data. Always use this skill before giving any analytics advice — even for seemingly simple questions like "how do I track signups" or "what events should I set up."
---

# Analytics Tracking

You are an expert in analytics implementation and measurement. Your goal is to help set up tracking that provides actionable insights for marketing and product decisions.

## Initial Assessment

Before implementing anything, understand:

1. **Business Context** — What decisions will this data inform? What are key conversions?
2. **Current State** — What tracking already exists? What tools are in use?
3. **Technical Context** — What's the tech stack? Any privacy/compliance requirements?

> Check if a product marketing context file exists at `.agents/product-marketing-context.md` or `.claude/product-marketing-context.md`. If it does, read it first and skip questions already answered there.

---

## Core Principles

- **Track for decisions, not data** — Every event should inform a specific action or decision. Avoid vanity metrics.
- **Start with questions** — Work backwards from what you need to know to what you need to track.
- **Name things consistently** — Establish naming conventions before implementing. Document everything.
- **Maintain data quality** — Clean data beats more data. Validate your setup before going live.

---

## Event Naming Convention

**Format: Object-Action (lowercase, underscores)**

```
signup_completed
button_clicked
form_submitted
checkout_payment_completed
cta_hero_clicked
```

**Rules:**
- Lowercase with underscores only
- Be specific: `cta_hero_clicked` not `button_clicked`
- Put context in properties, not in the event name
- No spaces or special characters
- Document every naming decision

---

## Essential Events to Track

### Marketing Site

| Event | Key Properties |
|-------|----------------|
| `cta_clicked` | button_text, location |
| `form_submitted` | form_type |
| `signup_completed` | method, source |
| `demo_requested` | — |

### Product / App

| Event | Key Properties |
|-------|----------------|
| `onboarding_step_completed` | step_number, step_name |
| `feature_used` | feature_name |
| `purchase_completed` | plan, value |
| `subscription_cancelled` | reason |

---

## Standard Event Properties

| Category | Properties |
|----------|------------|
| Page | page_title, page_location, page_referrer |
| User | user_id, user_type, account_id, plan_type |
| Campaign | source, medium, campaign, content, term |
| Product | product_id, product_name, category, price |

**Rules for properties:**
- Use consistent names across all events
- Never include PII (names, emails, phone numbers)
- Don't duplicate properties that are tracked automatically

---

## GA4 Quick Setup

1. Create a GA4 property and data stream
2. Install `gtag.js` or connect via Google Tag Manager (GTM)
3. Enable Enhanced Measurement in GA4 settings
4. Configure your custom events
5. Mark key events as Conversions in Admin

**Custom event example:**
```javascript
gtag('event', 'signup_completed', {
  'method': 'email',
  'plan': 'free'
});
```

---

## Google Tag Manager (GTM) Basics

| Component | What it does |
|-----------|--------------|
| Tags | The code that runs (GA4, pixels, etc.) |
| Triggers | When that code fires (page view, click, etc.) |
| Variables | Dynamic values (click text, data layer values) |

**Data Layer push example:**
```javascript
dataLayer.push({
  'event': 'form_submitted',
  'form_name': 'contact',
  'form_location': 'footer'
});
```

---

## UTM Parameter Guide

| Parameter | Purpose | Example |
|-----------|---------|---------|
| utm_source | Where traffic comes from | google, newsletter |
| utm_medium | Type of marketing | cpc, email, social |
| utm_campaign | Campaign name | spring_sale |
| utm_content | Differentiate ad versions | hero_cta |
| utm_term | Paid search keyword | running+shoes |

**Naming rules:**
- Always lowercase
- Use underscores or hyphens — pick one and stick with it
- Be specific: `blog_footer_cta` not `cta1`
- Track all UTMs in a shared spreadsheet

---

## Debugging & Validation

**Tools to use:**

| Tool | Use For |
|------|---------|
| GA4 DebugView | Real-time event monitoring |
| GTM Preview Mode | Test triggers before publishing |
| Tag Assistant (Chrome) | Verify tags are loading |
| dataLayer Inspector | Inspect data layer values |

**Validation checklist before going live:**
- [ ] Events fire on the correct triggers
- [ ] Property values populate correctly
- [ ] No duplicate events firing
- [ ] Works on mobile and across browsers
- [ ] Conversions are being recorded
- [ ] No PII leaking into event properties

**Common issues:**

| Problem | What to check |
|---------|---------------|
| Events not firing | Trigger configuration, GTM loaded correctly |
| Wrong property values | Variable path, data layer structure |
| Duplicate events | Multiple GTM containers, trigger firing twice |

---

## Privacy & Compliance

- Cookie consent is required in EU, UK, and Canada — implement before collecting data
- Never send PII through analytics properties
- Set data retention limits in GA4 Admin
- Enable IP anonymization
- Use Google Consent Mode to pause tracking until user consents
- Only collect what you actually use

---

## Tracking Plan Template

Use this format to document your tracking setup:

```markdown
# [Site/Product] Tracking Plan

## Overview
- Tools: GA4, GTM
- Last updated: [Date]

## Events

| Event Name | Description | Properties | Trigger |
|------------|-------------|------------|---------|
| signup_completed | User completes signup | method, plan | Success page load |

## Conversions

| Conversion | Event | Counting Method |
|------------|-------|-----------------|
| Signup | signup_completed | Once per session |

## Custom Dimensions

| Name | Scope | Parameter |
|------|-------|-----------|
| user_type | User | user_type |
```

---

## Questions to Ask Before Starting

1. What analytics tools are you using (GA4, Mixpanel, Amplitude, etc.)?
2. What key user actions do you want to track?
3. What business decisions will this data inform?
4. Who will implement — dev team or marketing via GTM?
5. Are there privacy or consent requirements (GDPR, etc.)?
6. What's already being tracked today?

---

## Tool Reference

| Tool | Best For |
|------|----------|
| GA4 | Web analytics, Google Ads ecosystem |
| Mixpanel | Product analytics, event-based tracking |
| Amplitude | Product analytics, cohort analysis |
| PostHog | Open-source analytics + session replay |
| Segment | Routing data to multiple tools (CDP) |

---

## Related Skills

- **ab-test-setup** — For measuring A/B experiments
- **seo-audit** — For organic traffic analysis
- **page-cro** — For conversion optimization (uses analytics data)
- **revops** — For pipeline metrics, CRM tracking, revenue attribution
