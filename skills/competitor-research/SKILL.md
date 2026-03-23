---
name: competitor-research
description: Run structured competitor research using web searches, GitHub analysis, and parallel subagent workflows. Use when comparing vendors, analyzing competitor features, or answering "How does X do Y?"
---

# Competitor Research Skill

## Purpose

Run structured competitor research using web searches, GitHub analysis, and parallel subagent workflows. Produces actionable competitive intelligence profiles and feature comparisons.

## Trigger

User says: "research competitor X", "competitive analysis of X", "compare us to X", "competitor deep-dive on X"

## Workflow

### Step 1: Identify Target

Parse the user's request to determine:
- **Target competitor(s)** — one or more companies/products
- **Focus area** — overall product, specific feature, pricing, positioning, or all
- **Depth** — quick scan (5 min) or deep dive (15+ min)

If ambiguous, ask:
> "Should I do a quick scan or a full deep-dive? And is there a specific feature area you want me to focus on?"

### Step 2: Parallel Research (use subagents)

Spawn parallel subagents for each research track. This keeps the main context clean and allows simultaneous investigation.

#### Subagent A: Web Research
- Search for recent product announcements, blog posts, and press releases
- Search for analyst reports or reviews mentioning the competitor
- Search for pricing pages and packaging changes
- Search for customer reviews on G2, Gartner Peer Insights, or similar

#### Subagent B: GitHub / Open-Source Analysis
- If the competitor has public repos, analyze:
  - Repository activity (commits, contributors, stars, forks)
  - Recent releases and changelogs
  - Open issues and feature requests (what are users asking for?)
  - Technology stack and architecture patterns
- Use `gh` CLI for structured queries:
  ```bash
  gh repo view <org/repo> --json description,stargazerCount,forkCount,updatedAt
  gh release list --repo <org/repo> --limit 5
  gh issue list --repo <org/repo> --label "feature-request" --limit 20
  ```

#### Subagent C: Feature Deep-Dive (if requested)
- Compare specific capabilities side-by-side
- Look for documentation, API references, integration lists
- Identify gaps, advantages, and unique differentiators

### Step 3: Synthesize Profile

Combine subagent results into a structured competitor profile.

#### Profile Template

```markdown
# Competitor Profile: [Company Name]

**Last Updated:** [Date]
**Researcher:** AI-assisted

## Overview
- **Product:** [Product name and one-line description]
- **Target Market:** [Who they sell to]
- **Positioning:** [How they position themselves]
- **Pricing Model:** [Pricing approach — per-seat, usage-based, tier-based, etc.]

## Recent Activity
- [Bullet list of notable recent announcements, releases, or moves]

## Strengths
- [What they do well — be specific]

## Weaknesses
- [Where they fall short — cite evidence]

## Feature Comparison
| Capability | Us | [Competitor] | Notes |
|---|---|---|---|
| [Feature 1] | [Status] | [Status] | [Context] |
| [Feature 2] | [Status] | [Status] | [Context] |

## Open-Source / Community Signals
- GitHub stars: [count]
- Recent release cadence: [frequency]
- Top feature requests: [list]

## Key Takeaways
1. [Most important insight]
2. [Second most important insight]
3. [Actionable recommendation]
```

### Step 4: Save Output

- **Profile:** Save to `data/competitors/profiles/<competitor-slug>.md`
- **Full research report:** Save to `output/competitor-research/<competitor-slug>-<YYYY-MM-DD>.md`
- If a profile already exists, update it and note what changed

### Step 5: Present Summary

Return a concise summary to the user:
- 3-5 bullet key findings
- Any surprises or notable changes since last research
- Recommended actions or areas to watch
- Path to the full report file

## Output Locations

| Artifact | Path |
|---|---|
| Competitor profiles | `data/competitors/profiles/<slug>.md` |
| Research reports | `output/competitor-research/<slug>-<date>.md` |

## Configuration

No configuration file required. This skill works out of the box with web search and `gh` CLI.

Optional: maintain a `data/competitors/watchlist.yaml` to track competitors you research regularly:

```yaml
competitors:
  - name: "Competitor A"
    slug: "competitor-a"
    repos:
      - "org/main-repo"
    last_researched: "2025-01-15"
    focus_areas:
      - "feature-x"
      - "pricing"
  - name: "Competitor B"
    slug: "competitor-b"
    repos: []
    last_researched: "2025-02-01"
    focus_areas:
      - "integrations"
```

## Examples

**Quick scan:**
> "Research competitor Acme Corp — quick scan on their latest release"

**Deep dive:**
> "Do a full competitive deep-dive on Acme Corp, focusing on their AI capabilities and pricing"

**Comparison:**
> "Compare our workflow automation to what Acme Corp and Beta Inc offer"

## Tips

- Run this periodically (monthly or quarterly) for key competitors to keep profiles fresh.
- Combine with your standup or initiative skills to surface competitive context alongside your own metrics.
- For public companies, earnings calls and investor presentations are rich sources — ask the skill to search for those specifically.
