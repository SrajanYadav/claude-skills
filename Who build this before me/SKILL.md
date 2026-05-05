---
name: who-built-this-before-me
description: Check whether a project, tool, library, or product idea has already been built before the user invests time in it. Find existing solutions, extract standard patterns, benchmark the user's angle against prior art, and deliver a clear verdict (build / fork / contribute / use existing / investigate why it failed). Use this skill whenever the user describes something they're thinking of building, making, shipping, launching, or coding — especially phrases like "I want to build…", "I'm thinking of making…", "should I build X…", "is there already a…", "my idea is…", or when the user is scoping a new side project, startup, library, or tool. Trigger even if the user doesn't explicitly ask for prior art research — if they're about to build something, they should check first.
---

# who-built-this-before-me

Before the user burns a weekend (or a quarter) building something, find out whether it already exists. Most ideas have been tried. Some are solved well, some are solved badly, some failed for instructive reasons, and a few are genuinely open. This skill figures out which bucket the user's idea falls into and tells them plainly.

## Core loop

1. **Restate the idea in one sentence.** Strip the pitch down to: what it does, who it's for, what constraint makes it distinctive (if any). Show this back to the user and confirm before searching. If the idea is too vague to search (i.e. the framing matches an entire tool category), ask exactly **one** clarifying question. You may include up to 3 example dimensions as prompts, but no more — this is a question, not a questionnaire.
2. **Generate vocabulary before searching.** Before running any query, write down 6–10 different framings of the idea from distinct vantage points. The user's framing is one lens; other builders, academics, and infrastructure people use different words for the same thing. Cover at minimum:
   - The builder's framing (the user's own words)
   - The user-of-the-tool framing (what someone searching for this would type)
   - The academic or research framing (if applicable)
   - The infrastructure / implementation framing
   - The adjacent-community framing (the next-door discipline that likely solved this first)

   Write the list out explicitly. Map each search query to a framing. This prevents the failure mode where 5 queries all hit the same semantic neighborhood.
3. **Search where builders actually publish.** Run 3–6 targeted queries across the right registries, covering distinct framings from step 2:
   - Code: GitHub, GitLab, PyPI, npm, crates.io, Hugging Face (for ML)
   - Products: Product Hunt, Hacker News ("Show HN"), relevant subreddits
   - Writing: engineering blog posts, papers (arXiv, Google Scholar) when relevant
   - Domain-specific high-signal venues: model release notes and system cards for AI/ML tools, SEC filings for fintech, RFCs and standards bodies for protocols, regulator guidance for compliance.

   Keep queries short. Don't run one generic query and stop.
4. **Trace one layer down on every direct match.** When a project's docs mention another tool as a dependency, bridge, or "official harness for X" — that other tool is often the real incumbent. For each direct match, ask: what does this project delegate to? What does it wrap? Follow those pointers with a dedicated query.
5. **Cluster the findings into four buckets.**
   - **Direct matches** — same problem, same approach
   - **Adjacent solutions** — same problem, different approach
   - **Partial solutions** — solves a subset of the problem
   - **Abandoned / stale** — existed, now dead (note the last commit date and why it died)
6. **Extract standard patterns.** Across the matches, what shows up repeatedly? Common architecture, libraries, design decisions, naming conventions, pricing models.
7. **Benchmark the user's angle.** In one honest paragraph, compare the user's specific framing against what exists. Name the real differentiator — or admit there isn't one.
8. **Deliver a verdict.** Pick one:
   - **Build it** — genuine gap; differentiation is clear and defensible
   - **Fork/extend** — closest existing project + specifically what to add
   - **Contribute** — the feature belongs upstream in an existing project
   - **Use existing** — already solved well; name the best option(s)
   - **Investigate first** — someone tried and failed; understand why before spending time

## Output format

Always produce a short markdown report with these exact sections:

```markdown
# Prior art check: [idea in ≤8 words]

## The idea, restated
[One sentence.]

## The landscape
[Table with columns: Name | Link | Status | Relevance | Bucket]
[Rows grouped by bucket: direct matches, adjacent, partial, abandoned. Max 3 rows per bucket.]

## Standard patterns
[3–6 bullets describing what's common across the matches.]

## Differentiator analysis
[One paragraph. What's genuinely different about the user's framing, if anything. Honest.]

## Verdict: [Build it / Fork X / Contribute to Y / Use Z / Investigate first]
[One paragraph explaining the verdict and the concrete next step.]
```

## Search strategy

Vary vocabulary across queries. Bad: run the same query five times. Good: try multiple framings — the user's words, the implementer's words, the researcher's words, the adjacent community's words.

Prefer primary sources (repos, Show HN threads, project homepages) over aggregator articles.

## What to avoid

- **Don't invent competitors.** If search comes up empty after real effort, say so and explain where you looked.
- **Don't pad the verdict.** Pick one. The user can push back.
- **Don't stop at the first match.** One existing tool means you have a baseline, not a dead end.
- **Don't be diplomatic to spare feelings.** The user asked for a reality check. Give it.

## Budget

Aim for ≤10 total search queries. Stop earlier only if the landscape is clear after 3–4 queries *and* at least one followed a dependency lead. If still not confident after 10, say so and list what you found.
