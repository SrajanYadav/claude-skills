---
name: Content Writer
description: |
  Phased content generation system (Discuss→Plan→Execute→Verify→Ship) that produces
  human-sounding blog articles, LinkedIn/Twitter/Instagram/Facebook posts, emails,
  landing pages, sales funnels, case studies, and SEO metadata. Uses copywriting
  frameworks (AIDA, PAS, BAB, LEMA, CONVERT). Requires a brand voice profile before
  generating content. Integrated with claude-seo and humanizer for quality checks.

  Use this skill when the user:
  - Runs commands: /writer:discuss, /writer:plan, /writer:execute, /writer:verify,
    /writer:ship, /writer:profile-create, /writer:next, /writer:update
  - Asks to write, draft, or generate ANY content (blog, post, email, page, copy)
  - Says "help me write", "write a post", "draft a blog", "create an email"
  - Wants to build or manage a brand voice profile
  - Mentions content strategy, content calendar, or multi-platform content packages
  Always use this skill — even for simple requests like "write me a LinkedIn post."
---

# Content Writer v2.0

Professional content generation system that produces blog articles, social media posts, email content, web pages, landing pages, sales funnels, case studies, product descriptions, and SEO metadata that sound like a specific human wrote them — not like AI. Integrated with claude-seo for SEO optimization and humanizer for anti-AI auditing.

---

## Update Check System

**IMPORTANT:** Before processing any user command, check for updates:

1. Read `~/.claude/skills/content-writer/.version` to get installed version
2. Check npm registry: `npm view claude-content-writer version`
3. Compare versions
4. If update available and not shown this session:
   - Display update notification
   - Mark as shown for this session (store in memory: `updateNotificationShown = true`)
5. Continue with user's command

**Update Notification Format:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📦 Content Writer Update Available
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Current: v{current_version}
  Latest:  v{latest_version}

  Run /writer:update to upgrade and see what's new.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Session Tracking:**
- Only show notification once per Claude Code session
- Reset when Claude Code restarts
- Skip check if already shown in current session

---

## System Overview

Content Writer v2.0 uses a **GSD-style phased workflow** inspired by Get Shit Done methodology. Instead of generating content in one step, it follows a structured process that ensures quality, SEO optimization, and human-like voice.

### The Five Phases

1. **Discuss** — Gather requirements, clarify decisions, identify gray areas
2. **Plan** — Research approach, select framework, create execution plan
3. **Execute** — Generate content following the plan and best practices
4. **Verify** — Run SEO check (claude-seo) and anti-AI audit (humanizer)
5. **Ship** — Save to file, present to user with publishing notes

### Why Phased Workflow?

- **Higher Quality** — Each phase has a specific purpose and deliverables
- **Better SEO** — Integrated optimization throughout the process
- **More Human** — Anti-AI audit catches patterns you might miss
- **Professional** — Matches proven development methodologies
- **Transparent** — Clear progress and decision points

---

## Core Commands

### Phased Workflow Commands

**`/writer:discuss [topic]`**
Start a new content project. Gathers requirements, clarifies decisions, identifies content type and framework.

**`/writer:plan`**
Research and plan the content. Selects framework, creates outline, defines SEO strategy.

**`/writer:execute`**
Generate the content following the plan. Applies selected framework and best practices.

**`/writer:verify`**
Quality check. Runs SEO optimization (claude-seo) and anti-AI audit (humanizer).

**`/writer:ship`**
Finalize and save. Generates markdown file with metadata and publishing notes.

**`/writer:next`**
Auto-advance to the next phase. Detects current phase and runs the next step automatically.

### Profile Management Commands

**`/writer:profile-create`**
Create a new writer profile with URL scanning and comprehensive questionnaire.

**`/writer:profile-view`**
View current writer profile and all stored information.

**`/writer:profile-edit`**
Edit existing writer profile, products, CTAs, or case studies.

**`/writer:profile-delete`**
Delete writer profile and all associated data.

### Quick Commands

**`/writer:help`**
Show available commands and current workflow status.

**`/writer:status`**
Show current phase, profile status, and next steps.

**`/writer:update`**
Check for updates and upgrade to the latest version. Shows changelog preview before updating.

---

## Profile-First Enforcement

**CRITICAL:** Content Writer v2.0 requires a writer profile before generating any content.

### Profile Check Flow

```
User: "/writer:discuss blog post about X"
↓
System: Check for profile in memory
↓
Profile exists? NO
↓
"No writer profile found. Let's create one first."
"A profile ensures your content has consistent voice and quality."
↓
Run /writer:profile-create
↓
After completion → Return to original request
```

### Why Profile-First?

- **Consistent Voice** — Every piece sounds like you
- **Better Quality** — No generic AI content
- **Professional Workflow** — Proper setup before execution
- **Richer Context** — More information = better content

---

## Profile Creation Workflow

### Step 1: URL Scanning (Optional but Recommended)

```
Let's create your writer profile! This helps me write content that sounds like YOU.

First, do you have any URLs I can analyze to detect your tone and voice?
(Blog posts, articles, social media posts, etc.)

You can provide:
• Multiple URLs (the more, the better)
• Or skip this step and I'll build your profile from scratch

Paste URLs below (one per line) or type "skip":
```

**If URLs provided:**
1. Fetch each URL
2. Analyze for:
   - Sentence structure (length, complexity, variety)
   - Vocabulary (technical vs. casual, jargon usage)
   - Tone markers (formal/informal, serious/playful)
   - Personality indicators (humor, anecdotes, opinions)
   - Formatting preferences (paragraph length, lists, emphasis)
3. Generate tone profile and confirm:
```
Based on your content, I detected:
• Tone: [Direct, conversational, data-driven]
• Sentence style: [Mix of short punchy sentences and longer explanatory ones]
• Vocabulary: [Technical but accessible, minimal jargon]
• Personality: [Confident, slightly irreverent, uses specific examples]
• Formatting: [Short paragraphs, frequent subheadings, bullet points]

Does this sound right? (yes/no/adjust)
```

### Step 2: Comprehensive Brand Questionnaire

Walk through each section one at a time, interactively.

#### Section 1/10 — Brand Identity
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Brand Identity (1/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What's your name and title?
   (This appears as the byline on all content)

2. What's your company/brand name?

3. Company website/domain?

4. Tagline or mission statement? (optional)

5. What does your company do? (1-2 sentences, in your words)
```

#### Section 2/10 — Industry & Market
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Industry & Market (2/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What industry/niche are you in?
   Examples: SaaS, E-commerce, Healthcare, Consulting, etc.

2. Who are your main competitors? (List 2-3 companies)

3. What makes you different from competitors?
   (Your unique positioning)
```

#### Section 3/10 — Target Audience
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Target Audience (3/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Who is your primary audience?
   Be specific: "startup founders", "marketing directors at mid-market SaaS",
   "small business owners in healthcare", etc.

2. What are their main pain points? (What problems do they face?)

3. What are their goals? (What do they want to achieve?)

4. What objections might they have? (Why might they hesitate?)
```

#### Section 4/10 — Voice & Tone
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Voice & Tone (4/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[If URL scanning was done, show detected tone and ask for confirmation]

1. Pick 3-5 adjectives that describe your ideal writing voice:

   Select from these options (or provide your own):
   1. Direct          7. Provocative      13. Witty
   2. Warm            8. Authoritative    14. Humble
   3. Irreverent      9. Data-driven      15. Technical
   4. Conversational  10. Storytelling    16. Casual
   5. Professional    11. Empathetic      17. Bold
   6. Confident       12. Educational     18. Other: _____

2. Are there voices or writers you admire?
   (Blogs, newsletters, authors — helps calibrate)

3. Anything you specifically want to AVOID?
   Examples: Corporate jargon, emojis, exclamation marks, overly casual, etc.
```

#### Section 5/10 — Content Strategy
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Content Strategy (5/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What types of content do you create? (Select all that apply)
   1. Blog articles        9. Landing pages
   2. LinkedIn posts       10. Web pages
   3. Twitter/X posts      11. Product pages
   4. Instagram captions   12. Sales funnels
   5. Facebook posts       13. Case studies
   6. Email newsletters    14. Testimonials
   7. Email campaigns      15. Product descriptions
   8. Email sequences      16. Other: _____

2. What are your main content themes/pillars?
   (3-5 topics you write about regularly)

3. What's your primary content goal?
   1. Brand awareness (TOFU)     4. Thought leadership
   2. Lead generation (MOFU)     5. Community building
   3. Customer conversion (BOFU) 6. Other: _____

4. Preferred article length?
   1. Short (800-1,200 words)     3. Long (2,500+ words)
   2. Medium (1,500-2,000 words)  4. Varies by topic
```

#### Section 6/10 — Products & Services
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Products & Services (6/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

List your main products/services (I'll reference these naturally in content):

For each, provide:
• Name
• Brief description (1 sentence)
• Target customer
• Key benefit
• Price range (optional)

Add first product/service:
```

After each entry: `✓ Added: [Product Name] — Add another? (yes/no)`

#### Section 7/10 — Case Studies
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Case Studies (7/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Do you have case studies or success stories I can reference?

For each, provide:
• Client/project name (or "Anonymous" if NDA)
• Challenge/problem
• Solution/approach
• Results/outcomes (with metrics if possible)
• Can I mention this publicly? (yes/no/anonymized)

Add first case study (or type "skip"):
```

#### Section 8/10 — CTAs
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CTAs (8/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What actions do you want readers to take?

Common CTAs:
• Book a call/demo
• Download a resource
• Subscribe to newsletter
• Follow on social media
• Visit website
• Contact for consultation

For each CTA, provide:
• Platform (blog, LinkedIn, Twitter, etc. or "all")
• CTA text
• URL (if applicable)

Add first CTA:
```

#### Section 9/10 — Publishing Workflow
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Publishing Workflow (9/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Where do you publish content? (Select all that apply)
   1. Company blog     5. Instagram
   2. Medium           6. Facebook
   3. LinkedIn         7. Email newsletter
   4. Twitter/X        8. Other: _____

2. Do you have a content approval process?
   1. No approval needed (I publish directly)
   2. Self-review before publishing
   3. Team review required
   4. Other: _____

3. Preferred output format?
   1. Markdown    3. HTML
   2. Plain text  4. Platform-specific format
```

#### Section 10/10 — SEO Strategy
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SEO Strategy (10/10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Do you have target keywords or topics?
   (List 5-10 keywords/phrases you want to rank for)

2. SEO priority level?
   1. High (SEO is critical)
   2. Medium (SEO matters but not primary)
   3. Low (Focus on quality over SEO)

3. Any SEO constraints?
   (Word count requirements, keyword density, etc.)
```

### Step 3: Profile Confirmation

Show full summary of all 10 sections. Ask: `Does this look correct? (yes/edit/cancel)`

### Step 4: Save Profile

On confirmation:
1. Save to memory: `[Content Writer] Writer Profile`
2. Save to file: `content-writer-output/profile/PROFILE.md`
3. Save products to: `content-writer-output/profile/PRODUCTS.md`
4. Save CTAs to: `content-writer-output/profile/CTAS.md`
5. Save case studies to: `content-writer-output/profile/CASE-STUDIES.md`

```
✓ Profile saved successfully!

Your profile is stored in:
• Memory (for quick access)
• Files (for version control)

Location: content-writer-output/profile/

You're all set! Let's create some content.
To get started: /writer:discuss "your topic here"
```

---

## Phase 1: Discuss (Requirements Gathering)

**Command:** `/writer:discuss [topic]`

**Goal:** Understand what to write and why. Gather all necessary information before planning.

### Workflow

**Step 1: Profile Check**
```
Check memory for [Content Writer] Writer Profile
↓
Profile exists? NO → Run /writer:profile-create first, then return here
↓
Profile exists? YES → Continue
```

**Step 2: Gather Requirements (conversationally, not as a form)**

1. **Topic & Angle**
   - What's the main topic?
   - What's your specific angle or perspective?
   - Any specific points you want to cover?

2. **Content Type** — What platform is this for?
   1. Blog article
   2. LinkedIn post
   3. Facebook post
   4. Instagram caption
   5. Twitter/X (single tweet)
   6. Twitter/X (thread)
   7. Email newsletter
   8. SEO metadata
   9. Content package (multiple platforms)

3. **Audience & Goal**
   - Who's the primary audience for this piece?
   - What do you want them to do after reading?
   - What stage of awareness? (Unaware / Problem-aware / Solution-aware / Product-aware)

4. **Framework Selection** — Suggest one based on content type + goal, confirm with user:
   - **AIDA** (Attention-Interest-Desire-Action) — Sales pages, landing pages
   - **PAS** (Problem-Agitate-Solution) — Problem-focused content
   - **BAB** (Before-After-Bridge) — Transformation stories, case studies
   - **LEMA** (Logic-Explicitness-Memorability-Actionability) — Thought leadership
   - **4-Point** (Hook-Effortless-Flow-Polish) — Long-form articles
   - **CONVERT** (Clarity-Outcome-Narrative-Value-Engagement-Relevance-Trigger) — Conversion-focused

   Say: "I recommend [Framework] for this. Sound good, or prefer a different approach?"

5. **Length & Format**
   - Desired length? (Or use profile default)
   - Any specific formatting requirements?

6. **Research Needs**
   - Any URLs I should analyze for inspiration?
   - Specific data, stats, or sources to include?

7. **CTAs & Next Steps**
   - Which CTA from profile, or a new one?
   - Any specific links or resources to include?

**Step 3: Summarize & Confirm**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Content Brief
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Topic:      [Topic and angle]
Platform:   [Content type]
Framework:  [Selected framework]
Audience:   [Target audience]
Goal:       [Primary objective]
Length:     [Target word count]
CTA:        [Call-to-action]

Key Points:
• [Point 1]
• [Point 2]
• [Point 3]

Ready to plan? (yes/edit)
```

**Step 4:** Save to memory: `[Content Writer] Current Project - Discussion`

```
✓ Discussion complete!
Next: /writer:plan
(Or use /writer:next to auto-advance)
```

---

## Phase 2: Plan (Research & Strategy)

**Command:** `/writer:plan`

**Goal:** Research the topic, create detailed outline, define SEO strategy.

### Workflow

**Step 1:** Load `[Content Writer] Current Project - Discussion`. If missing → "Please run /writer:discuss first."

**Step 2: Research (if URLs provided in Discuss)**
1. Fetch each URL
2. Extract key insights, data points, angles
3. Identify gaps or opportunities
4. Note what to avoid (don't copy)

**Step 3: Framework Application — Create Detailed Structure**

**For AIDA:**
```
1. Attention (Headline + Hook)
   - Compelling headline
   - Opening that grabs immediately

2. Interest (Build engagement)
   - Relevant benefits or pain points
   - Specific examples

3. Desire (Create want)
   - Show transformation
   - Social proof
   - Address objections

4. Action (Clear CTA)
   - Specific next step
   - Remove friction
```

**For PAS:**
```
1. Problem (Identify pain)
   - State the problem clearly
   - Make it relatable

2. Agitate (Make it urgent)
   - Show cost of inaction
   - Amplify the pain

3. Solution (Present answer)
   - Introduce your solution
   - Show how it solves the problem
   - Clear CTA
```

**For BAB:**
```
1. Before (Current state)
   - Paint picture of life with problem
   - Be specific and relatable

2. After (Desired state)
   - Show the transformation
   - Make it tangible

3. Bridge (How to get there)
   - Explain your solution
   - Show the path
   - Clear CTA
```

**For LEMA:**
```
1. Logic (Natural flow)
   - Organize ideas logically
   - Answers follow questions

2. Explicitness (Be specific)
   - Concrete examples
   - No vague language

3. Memorability (Make it stick)
   - Analogies, stories
   - Coined terms

4. Actionability (Clear steps)
   - What to do next
   - Pathway to results
```

**For 4-Point:**
```
1. Hook Attention Early
   - Compelling headline
   - Strong intro

2. Make It Effortless to Read
   - Subheadings every 300-400 words
   - Short paragraphs
   - Bullet points

3. Maintain Narrative Flow
   - Smooth transitions
   - Logical progression

4. Polish Ruthlessly
   - Cut fluff
   - Strengthen CTA
```

**For CONVERT:**
```
1. Clarity — Simple, easy to understand
2. Outcome — Show end result
3. Narrative — Tell a story
4. Value — Demonstrate value prop
5. Engagement — Interactive elements
6. Relevance — Speak to audience
7. Trigger — Strong CTA
```

**Step 4: SEO Strategy** (for blog articles and long-form content)
1. Identify primary keyword
2. List secondary keywords
3. Plan keyword placement (natural, not stuffed)
4. Define meta title (50-60 chars) and meta description (150-160 chars)
5. Plan internal/external links
6. Identify related topics to cover

**Step 5: Outline Creation**

Create detailed outline with:
- Section headings
- Key points per section
- Examples/data to include
- Where to place CTAs
- Estimated word count per section

**Step 6: Present Plan**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Content Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Framework: [Selected framework]

Structure:
[Detailed outline with sections, key points, examples]

SEO Strategy:
• Primary keyword: [keyword]
• Secondary keywords: [list]
• Meta title: [title]
• Meta description: [description]

Estimated length: [word count]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ready to execute? (yes/edit)
```

**Step 7:** Save to memory: `[Content Writer] Current Project - Plan`

```
✓ Plan complete!
Next: /writer:execute
(Or use /writer:next to auto-advance)
```

---

## Phase 3: Execute (Content Generation)

**Command:** `/writer:execute`

**Goal:** Write the content following the plan, applying best practices and brand voice.

### Workflow

**Step 1:** Load `[Content Writer] Current Project - Plan` AND `[Content Writer] Writer Profile`. If either missing → "Please complete previous phases first."

**Step 2: Voice Calibration**

If profile has blog URL:
1. Fetch 1-2 recent articles
2. Analyze sentence patterns
3. Note vocabulary choices
4. Identify personality markers
5. Calibrate generation style to match

**Step 3: Generate Content — Follow plan section by section**

**Writing Principles:**
1. **Active voice** — "We built" not "It was built"
2. **Be specific** — concrete examples, numbers, names
3. **Show, don't tell** — use stories and scenarios
4. **Vary sentence length** — mix short punchy with longer explanatory
5. **Use transitions** — connect ideas smoothly
6. **Include proof** — data, quotes, case studies
7. **Address objections** — anticipate and answer questions
8. **Natural keyword use** — SEO without stuffing

**Anti-AI Principles (CRITICAL):**

Avoid these AI tells in all content:
- Overused words: leverage, seamless, robust, pivotal, delve, realm, transformative, navigate
- Rule of three everywhere
- Parallel list structures
- Em dash overuse (—)
- Throat-clearing openers: "In today's digital landscape...", "In the ever-evolving world of..."
- Generic conclusions: "In conclusion, it's clear that...", "As we've seen..."
- Vague attributions: "Studies show...", "Research suggests..." (without citing actual sources)
- Forced symmetry and over-structuring

**Platform-Specific Formatting:**

**Blog Articles:**
- H2 every 300-400 words
- Paragraphs: 2-3 sentences max
- Bullet points for lists only
- Bold for emphasis, not decoration
- Note image/visual placement

**LinkedIn Posts:**
- Line breaks every 2-3 lines
- Bold for section headers
- 1,400-1,800 characters
- Note: "Add link in first comment"

**Twitter/X:**
- Single tweets: 240-280 characters
- Threads: 5-12 tweets, numbered (1/n)
- One idea per tweet
- No external links in body

**Instagram:**
- First 125 characters critical (above fold)
- Strategic line breaks and emojis
- 3-5 hashtags
- "Link in bio" for CTA

**Facebook:**
- 100-250 characters for reach
- Conversational tone
- Ask questions to drive engagement
- Link in first comment

**Step 4: Apply Framework Throughout**

Ensure content strictly follows selected framework:
- AIDA: Attention → Interest → Desire → Action
- PAS: Problem → Agitate → Solution
- BAB: Before → After → Bridge
- LEMA: Logic → Explicitness → Memorability → Actionability
- 4-Point: Hook → Effortless → Flow → Polish
- CONVERT: All 7 elements present

**Step 5: CTA Placement**
- Blog: mid-content + end
- LinkedIn / Twitter / Facebook: end only
- Instagram: caption end

**Step 6: Generate Metadata** (for blog articles)
- Meta title (50-60 chars)
- Meta description (150-160 chars)
- URL slug (lowercase, hyphens, no special chars)
- Image alt text suggestions

**Step 7: Present Draft**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Content Draft
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Full content here]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Stats:
• Word count: [count]
• Reading time: [minutes]
• Framework: [framework used]

Ready to verify? (yes/edit)
```

**Step 8:** Save to memory: `[Content Writer] Current Project - Draft`

```
✓ Content generated!
Next: /writer:verify
(Or use /writer:next to auto-advance)
```

---

## Phase 4: Verify (Quality Check)

**Command:** `/writer:verify`

**Goal:** Run SEO optimization and anti-AI audit to ensure quality.

### Workflow

**Step 1:** Load `[Content Writer] Current Project - Draft`. If missing → "Please run /writer:execute first."

### SEO Check (claude-seo Integration)

```
Check for claude-seo skill
↓
Available? YES → Run full SEO analysis
Available? NO  → Skip with warning, provide basic SEO checklist
```

If available, analyze: keyword optimization, meta tags quality, content structure, internal/external links, readability score, technical SEO elements.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SEO Analysis (claude-seo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Keyword optimization: [score/10]
✓ Meta tags:            [score/10]
✓ Structure:            [score/10]
✓ Readability:          [score/10]

Recommendations:
• [Recommendation 1]
• [Recommendation 2]
• [Recommendation 3]

Apply recommendations? (yes/no/manual)
```

### Anti-AI Audit (humanizer Integration)

```
Check for humanizer skill
↓
Available? YES → Run full audit
Available? NO  → Skip with warning, provide manual checklist
```

If available, check for: AI vocabulary, parallel structures, rule-of-three overuse, em dash frequency, generic phrases, vague attributions, throat-clearing openers.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Anti-AI Audit (humanizer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detected AI patterns:
• [Pattern 1]: [count] instances
• [Pattern 2]: [count] instances
• [Pattern 3]: [count] instances

Suggestions:
• [Suggestion 1]
• [Suggestion 2]
• [Suggestion 3]

Apply fixes? (yes/no/manual)
```

### Graceful Degradation

If dependencies missing:
```
⚠ Note: claude-seo not available. SEO check skipped.
⚠ Note: humanizer not available. Anti-AI audit skipped.

Content will still be generated, but without automated quality checks.
Consider installing dependencies for full functionality.
```

### Manual Quality Checklist (always present)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Quality Checklist
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Content Quality:
☐ Achieves stated goal
☐ Follows selected framework
☐ Maintains brand voice
☐ Includes specific examples
☐ No AI writing patterns

Technical Quality:
☐ No spelling/grammar errors
☐ Proper formatting for platform
☐ Links/CTAs correct

Persuasion Quality:
☐ Clear value proposition
☐ Addresses objections
☐ Includes social proof
☐ Strong CTA

All good? (yes/needs-work)
```

If user requests changes: apply fixes, re-run verification.

**Step 2:** Save to memory: `[Content Writer] Current Project - Verified`

```
✓ Verification complete!
Next: /writer:ship
(Or use /writer:next to auto-advance)
```

---

## Phase 5: Ship (Finalize & Deliver)

**Command:** `/writer:ship`

**Goal:** Save content to file, generate metadata, present with publishing notes.

### Workflow

**Step 1:** Load `[Content Writer] Current Project - Verified`. If missing → "Please complete verification first."

### Smart Output Location Detection

```
Check if running in Claude Code:
↓
In Claude Code? YES → ./content-writer-output/[type]/[filename].md
In Claude Code? NO  → /mnt/user-data/outputs/content-writer/[type]/[filename].md
```

### Directory Structure

```
content-writer-output/
├── profile/
│   ├── PROFILE.md
│   ├── PRODUCTS.md
│   ├── CTAS.md
│   └── CASE-STUDIES.md
├── blog/
├── linkedin/
├── facebook/
├── instagram/
├── twitter/
├── email/
├── landing-pages/
├── seo/
├── research/
└── packages/
    └── 001-package-name/
        ├── blog.md
        ├── linkedin.md
        ├── newsletter.md
        └── PACKAGE.md
```

### Filename Format

Format: `{number}-{slug}.md` — Example: `001-why-saas-onboarding-fails.md`
- **Number:** Auto-increment based on existing files in directory
- **Slug:** Generated from title (lowercase, hyphens, no special chars)

### File Frontmatter

```markdown
---
title: [Title]
platform: [Platform]
framework: [Framework used]
word_count: [Count]
created: [Date]
author: [From profile]
status: draft
seo:
  meta_title: [Meta title]
  meta_description: [Meta description]
  keywords: [Keywords]
---

[Content here]
```

### Save to File

1. Create directory if doesn't exist
2. Write content with frontmatter metadata
3. Save to both file and memory

### Publishing Notes (Platform-Specific)

**For Blog:**
```
• Upload to CMS
• Add featured image
• Set category/tags
• Schedule or publish
• Share on social media
```

**For LinkedIn:**
```
• Copy content to LinkedIn
• Add link in first comment: [URL]
• Tag relevant people/companies
• Best time to post: [Based on profile]
• Engage with comments for first hour
```

**For Twitter:**
```
• Post as thread (numbered 1/[n])
• Add link in final tweet
• Pin thread if important
• Best time to post: [Based on profile]
• Engage with replies
```

**For Instagram:**
```
• Prepare visual content first
• Copy caption (check character count)
• Add hashtags in caption or first comment
• Update "link in bio"
• Best time to post: [Based on profile]
```

**For Facebook:**
```
• Post content
• Add link in first comment
• Ask a question to drive engagement
• Best time to post: [Based on profile]
```

**For Email:**
```
• Import into email platform (Mailchimp, ConvertKit, etc.)
• Set subject line and preview text from metadata
• Test on mobile before sending
• Schedule for optimal send time
• Monitor open and click rates
```

### Delivery Message

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Content Shipped! ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File saved: [Full path to file]

Stats:
• Platform:      [Platform]
• Framework:     [Framework]
• Word count:    [Count]
• Reading time:  [Minutes]
• SEO Score:     [Score]/10 (claude-seo)
• Human Score:   [Score]/10 (humanizer)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Publishing Notes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Platform-specific publishing notes]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ready to create more content? Use /writer:discuss to start a new project!
```

### Clean Up

After shipping, delete from memory:
- `[Content Writer] Current Project - Discussion`
- `[Content Writer] Current Project - Plan`
- `[Content Writer] Current Project - Draft`
- `[Content Writer] Current Project - Verified`

Keep profile and assets in memory permanently.

---

## Auto-Advance Command

**`/writer:next`** — Detect current phase and run the next one automatically.

```
No project?                → "No active project. Use /writer:discuss to start."
Has Discussion, no Plan?   → Run /writer:plan
Has Plan, no Draft?        → Run /writer:execute
Has Draft, no Verified?    → Run /writer:verify
Has Verified?              → Run /writer:ship
```

Usage:
```
/writer:discuss "blog post about X"
/writer:next   → runs /writer:plan
/writer:next   → runs /writer:execute
/writer:next   → runs /writer:verify
/writer:next   → runs /writer:ship
```

---

## Dual Storage System

### Memory Storage (Runtime)
- Fast access during generation
- Persists across sessions
- Used for profile lookups and project state

### File Storage (Permanent)
- Version control friendly
- Shareable and portable
- Organized directory structure with metadata

### Sync Mechanism

**On Save:** Write to file first → update memory → verify both succeeded

**On Load:** Check memory first → fall back to file if missing → sync memory from file if needed

---

## Skill Integration

### claude-seo
- **When available:** Full SEO analysis in verify phase, keyword optimization, meta tag check, technical SEO recommendations
- **When unavailable:** Skip with warning, provide basic SEO checklist, continue workflow

### humanizer
- **When available:** Full anti-AI pattern detection, specific fix suggestions, human score calculation
- **When unavailable:** Skip with warning, provide manual checklist, continue workflow

### Graceful Degradation
Both dependencies optional. Content generation continues without them; quality checks become manual.

---

## Status & Help Commands

### `/writer:status`
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Content Writer Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Profile:         ✓ [Name] ([Company])
Active Project:  [Topic] ([Platform])
Current Phase:   [Phase name]
Next Step:       /writer:[command]

Dependencies:
• claude-seo:  ✓ Available / ✗ Not found
• humanizer:   ✓ Available / ✗ Not found

Output Location: [Path]
```

### `/writer:help`
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Content Writer v2.0 — Commands
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phased Workflow:
/writer:discuss [topic]  — Start new project
/writer:plan             — Research and plan
/writer:execute          — Generate content
/writer:verify           — Quality check (SEO + anti-AI)
/writer:ship             — Save and deliver
/writer:next             — Auto-advance to next phase

Profile Management:
/writer:profile-create   — Create new profile
/writer:profile-view     — View current profile
/writer:profile-edit     — Edit profile
/writer:profile-delete   — Delete profile

Utilities:
/writer:status           — Show current status
/writer:update           — Check for and install updates
/writer:help             — Show this help

Quick Start:
1. Create profile: /writer:profile-create
2. Start project:  /writer:discuss "your topic"
3. Auto-advance:   /writer:next (repeat until shipped)
```

---

## Update Command Workflow

When user runs `/writer:update`:

**Step 1: Check Version**
```bash
cat ~/.claude/skills/content-writer/.version
npm view claude-content-writer version
```

**Step 2: Compare & Display**

If update available:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Content Writer Update Available
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Current: v{current_version}
  Latest:  v{latest_version}

  Changelog Preview:
  {show relevant changelog entries}

  Update now? (y/n)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If already latest:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Content Writer is Up to Date
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Current version: v{current_version}
  Latest version:  v{current_version}

  You're running the latest version!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Step 3: Execute Update** (if confirmed)
```bash
npm install -g claude-content-writer@latest
```

**Step 4: Confirm Success**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Content Writer Updated Successfully!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Updated: v{old_version} → v{new_version}

  What's New:
  {show changelog entries}

  Full changelog: ~/.claude/skills/content-writer/CHANGELOG.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Copywriting Frameworks — Quick Reference

| Framework | Best For | Structure |
|-----------|----------|-----------|
| AIDA | Sales pages, landing pages | Attention → Interest → Desire → Action |
| PAS | Pain-point content | Problem → Agitate → Solution |
| BAB | Case studies, transformations | Before → After → Bridge |
| LEMA | Thought leadership | Logic → Explicitness → Memorability → Actionability |
| 4-Point | Long-form blog articles | Hook → Effortless → Flow → Polish |
| CONVERT | Conversion-focused content | Clarity → Outcome → Narrative → Value → Engagement → Relevance → Trigger |

---

## Reference Files

Loaded automatically when needed during content generation:

- `references/content-frameworks.md` — All copywriting frameworks and best practices
- `references/anti-ai-checklist.md` — Complete anti-AI writing audit
- `references/content-packages.md` — Multi-platform content package workflows
- `references/twitter-conventions.md` — Twitter/X specific guidelines
- `references/facebook-conventions.md` — Facebook specific guidelines
- `references/instagram-conventions.md` — Instagram specific guidelines
- `references/seo-meta-conventions.md` — SEO and metadata best practices
- `references/research-workflow.md` — Content research methodology
- `references/profile-management.md` — Profile system documentation

---

## Best Practices

**For Users:**
1. Take time with profile creation — richer profile = better content
2. Provide multiple URLs — more examples = better tone detection
3. Use the phased workflow — don't skip steps, each adds value
4. Review verify phase carefully — this is where quality is ensured
5. Trust the process — the workflow is designed for consistent quality

**For Content Generation:**
1. Always check for profile first — no content without profile
2. Load all reference files — use the frameworks and conventions
3. Apply anti-AI principles — avoid the common tells at all times
4. Use specific examples — no vague language ever
5. Follow platform conventions — each platform has unique requirements
6. Integrate SEO naturally — don't stuff keywords
7. Save incrementally — don't lose work between phases

---

## Troubleshooting

**"No profile found"**
→ Run `/writer:profile-create` first

**"Dependencies not available"**
→ Install claude-seo and humanizer (auto-installed with package)

**"Current directory not writable"**
→ Check permissions or use the standard output location

**"Phase out of order"**
→ Use `/writer:status` to see current phase, then run appropriate command

**"Content doesn't sound like me"**
→ Run `/writer:profile-edit` and add more URLs and voice examples

---

## Content Types Supported

- Blog articles (short 800–1,200 / medium 1,500–2,000 / long 2,500+)
- LinkedIn posts
- Twitter/X posts and threads
- Instagram captions
- Facebook posts
- Email newsletters, campaigns, and drip sequences
- Landing pages, web pages, and product pages
- Sales funnels
- Case studies and testimonials
- Product descriptions
- SEO metadata (title, description, URL slug)
- Content packages (multi-platform output from one brief)

---

## Version History

**v2.0.0** (2026-03-31)
- Complete rewrite with GSD-style phased workflow
- Enhanced profile creation with URL scanning and 10-section questionnaire
- Integrated claude-seo and humanizer with graceful degradation
- Smart output location detection (Claude Code vs standard)
- Dual storage system (memory + files)
- Best-in-class content frameworks (AIDA, PAS, BAB, LEMA, 4-Point, CONVERT)
- Profile-first enforcement
- Update check system on every command

**v1.2.0** (Previous)
- Basic content generation
- Simple profile system
- Memory-only storage

---

**Last Updated:** 2026-03-31
**Version:** 2.0.0
