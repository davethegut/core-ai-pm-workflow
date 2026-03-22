# One-Pager Examples

Three formats for different purposes. Each should fit on a single page (or screen).

---

## 1. Concept One-Pager

> Use when proposing a new idea, capability, or strategic direction. The goal is to communicate the vision and get buy-in to explore further.

### AI-Powered Meeting Summarizer

Our team spends roughly 15 hours per week in meetings, yet the insights from those conversations are scattered across personal notes, chat threads, and memory. Action items are lost. Decisions are undocumented. New team members have no way to get context on past discussions. The cost is not just inefficiency — it is institutional amnesia.

We propose building an AI-powered meeting summarizer that automatically generates structured notes from any recorded meeting. The system would produce a decision log, an action-item list with owners and due dates, and a searchable transcript — all delivered to the team's workspace within minutes of a meeting ending. Users would be able to ask follow-up questions against the transcript ("What did we decide about the timeline?") and receive precise, cited answers.

This capability would fundamentally change how our organization captures and retrieves knowledge. Early experiments with a prototype showed a 40% reduction in follow-up clarification messages and near-universal satisfaction from pilot users. The technology is mature enough to ship a reliable v1 within one quarter, and the underlying model can be extended to support async voice messages and Slack huddles in future iterations.

---

## 2. Problem/Solution One-Pager

> Use when proposing an enhancement to an existing product. Structured format helps reviewers quickly assess scope and feasibility.

### Dashboard Export Enhancement

**Background**

Users can currently create dashboards with up to 50 panels, combining charts, tables, and text. Dashboards are the primary way teams share analytical insights with stakeholders who do not use the product directly.

**Problem**

The existing export function only supports PNG screenshots, which lose interactivity and render poorly at high panel counts. In the last quarter, 340 support tickets cited export quality issues. User interviews revealed that 60% of dashboard creators manually recreate their dashboards in slide decks because the export is unusable for executive reporting.

**Requirements**

- Export dashboards to PDF with configurable page layout (portrait/landscape, panels per page)
- Support scheduled exports delivered via email on a daily/weekly cadence
- Preserve table data fidelity — export tables as real tables, not images
- Provide a "presentation mode" optimized for screen sharing

**Non-Goals**

- Real-time collaborative editing of exported documents (future consideration)
- Export to editable slide formats like PPTX (high complexity, low incremental value over PDF)
- Custom branding/theming beyond what the dashboard already supports

---

## 3. Decision One-Pager

> Use when the team faces a fork in the road and needs to align on a path. Present options honestly; make a recommendation.

### Build vs. Buy: Notification System

**Decision**

We need a notification system that supports in-app, email, and push channels with user-configurable preferences. Two viable paths exist: build in-house or integrate a third-party service.

**Recommendation**

Buy — integrate with a managed notification service (e.g., a vendor like Courier, Knock, or Novu).

**Options**

| | Build In-House | Buy / Integrate |
|---|---|---|
| Time to v1 | 3-4 months | 4-6 weeks |
| Ongoing cost | ~1 engineer maintaining | ~$800/month at current scale |
| Flexibility | Full control | Constrained to vendor capabilities |
| Channel support | Must build each channel | All major channels included |
| Reliability | Must build retry/failover logic | Included with SLA |

**Tradeoffs**

Building gives us full control and avoids vendor lock-in, but diverts engineering from core product work for at least a quarter. Buying gets us to market faster and shifts operational burden, but introduces a dependency and a recurring cost that scales with usage.

**Kill Criteria**

Revisit this decision if: (a) vendor costs exceed $3,000/month, (b) we need a notification channel the vendor does not support, or (c) vendor reliability drops below 99.9% over any 30-day window.
