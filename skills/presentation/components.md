# Slide Component Library

Reference for all available slide types in the presentation template. Each component shows the HTML snippet, when to use it, and what to customize.

All slides follow the same outer structure:

```html
<div class="slide" data-slide="N">
  <div class="slide-content">
    <!-- Component HTML goes here -->
  </div>
</div>
```

The first slide in the deck must include the `active` class: `class="slide active"`.

---

## 1. Title Slide

Hero opening slide. Use as the first slide in every deck.

```html
<div class="slide active" data-slide="1">
  <div class="slide-content" style="text-align: center;">
    <h1><span class="gradient-text">Your Presentation Title</span></h1>
    <p class="lead">A one-line description of what this deck covers and why it matters.</p>
    <div class="tags">
      <span class="tag">Strategy</span>
      <span class="tag purple">Q2 2025</span>
      <span class="tag teal">Security</span>
    </div>
  </div>
</div>
```

**When to use:** Always the first slide. Sets the context for the entire presentation.

**Customize:**
- The `<h1>` text. Wrap key words in `<span class="gradient-text">` for the blue-to-purple gradient effect, or use plain text.
- The `.lead` paragraph -- keep it to one or two sentences.
- Tags: add, remove, or change colors. Available tag colors: default (blue), `purple`, `teal`, `pink`, `yellow`.

---

## 2. Stat Cards

Big numbers in a grid. Use to lead with quantitative impact.

```html
<div class="slide" data-slide="2">
  <div class="slide-content">
    <h2>Key Metrics</h2>
    <div class="card-grid-3">
      <div class="card">
        <div class="stat-value">47%</div>
        <div class="stat-label">Reduction in mean time to respond</div>
      </div>
      <div class="card">
        <div class="stat-value purple">3.2x</div>
        <div class="stat-label">Increase in analyst throughput</div>
      </div>
      <div class="card">
        <div class="stat-value teal">$1.4M</div>
        <div class="stat-label">Annual cost savings per customer</div>
      </div>
    </div>
  </div>
</div>
```

**When to use:** After the title or problem statement to anchor the audience with data. Works well for KPIs, adoption numbers, cost savings, and performance benchmarks.

**Customize:**
- Grid class: `card-grid-2`, `card-grid-3`, or `card-grid-4` depending on how many cards you need.
- Stat value colors: default (blue), `purple`, `teal`, `pink`, `yellow`.
- Keep labels short (one line preferred).

---

## 3. Content Slide

Standard informational slide with a heading and bullet points or paragraphs.

```html
<div class="slide" data-slide="3">
  <div class="slide-content">
    <h2>Problem Statement</h2>
    <ul>
      <li><strong>Alert fatigue:</strong> SOC analysts face 11,000+ alerts per day with limited context.</li>
      <li><strong>Manual triage:</strong> Average investigation time is 45 minutes per alert.</li>
      <li><strong>Staffing gaps:</strong> 3.4 million unfilled cybersecurity positions globally.</li>
    </ul>
    <p>These challenges compound as attack surfaces expand with cloud adoption and remote work.</p>
  </div>
</div>
```

**When to use:** The workhorse slide. Use for problem statements, feature descriptions, requirements, explanations, and any narrative content.

**Customize:**
- Use `<ul>` for unordered lists, `<ol>` for ordered lists.
- Bold key terms with `<strong>` at the start of each bullet for scanability.
- Mix paragraphs and lists as needed. Keep total content to 4-6 bullet points max.

---

## 4. Before/After Slide

Two-column comparison layout for showing the contrast between current state and proposed state.

```html
<div class="slide" data-slide="4">
  <div class="slide-content">
    <h2>Investigation Workflow</h2>
    <div class="comparison-grid">
      <div class="before">
        <div class="label">Before</div>
        <h3>Manual Triage</h3>
        <ul>
          <li>Analyst manually reviews each alert</li>
          <li>Pivots across 4-5 tools for context</li>
          <li>45 min average per investigation</li>
          <li>High analyst burnout</li>
        </ul>
      </div>
      <div class="after">
        <div class="label">After</div>
        <h3>AI-Assisted Triage</h3>
        <ul>
          <li>AI auto-groups correlated alerts</li>
          <li>Context enriched in a single view</li>
          <li>5 min average per investigation</li>
          <li>Analyst focuses on decisions, not data gathering</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

**When to use:** Product demos, ROI justifications, workflow improvements, competitive comparisons. Any time you need to show a clear transformation.

**Customize:**
- Column headers (`.label` and `h3`). You can change "Before/After" to "Current/Proposed", "Without/With", etc.
- Content in each column can be lists, paragraphs, or stat values.
- Before column has a pink top border; After has teal.

---

## 5. Quote Slide

Large pull quote with attribution. Creates a visual pause and emphasis.

```html
<div class="slide" data-slide="5">
  <div class="slide-content">
    <blockquote class="quote">
      "This platform cut our triage time from hours to minutes. Our team can finally focus on the work that actually matters."
    </blockquote>
    <div class="attribution">
      <strong>Sarah Chen</strong>, Director of Security Operations &mdash; Acme Corp
    </div>
  </div>
</div>
```

**When to use:** Customer testimonials, analyst quotes, executive endorsements, industry analyst findings. Place after data slides to add a human element.

**Customize:**
- Quote text. Keep it to 1-3 sentences for readability at presentation size.
- Attribution line with name, title, and organization.
- The left border is blue by default. Override with inline style if needed: `style="border-left-color: var(--teal)"`.

---

## 6. Table Slide

Data table for structured comparisons, feature matrices, or planning grids.

```html
<div class="slide" data-slide="6">
  <div class="slide-content">
    <h2>Feature Comparison</h2>
    <table>
      <thead>
        <tr>
          <th>Capability</th>
          <th>Your Product</th>
          <th>Competitor A</th>
          <th>Competitor B</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Alert Grouping</strong></td>
          <td>AI-driven, real-time</td>
          <td>Rule-based only</td>
          <td>Manual</td>
        </tr>
        <tr>
          <td><strong>Investigation Context</strong></td>
          <td>Full entity timeline</td>
          <td>Limited enrichment</td>
          <td>Separate tool required</td>
        </tr>
        <tr>
          <td><strong>Response Automation</strong></td>
          <td>Built-in workflows</td>
          <td>SOAR integration needed</td>
          <td>Basic playbooks</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

**When to use:** Feature comparisons, pricing tiers, roadmap timelines, requirement matrices, risk assessments. Keep tables to 4-5 rows max for readability.

**Customize:**
- Number of columns and rows. Bold the first column for row labels.
- Header row is styled automatically. Rows highlight on hover.

---

## 7. Architecture / Diagram Slide

Visual layout using placeholder boxes and CSS arrows. For showing system architecture, data flow, or process steps.

```html
<div class="slide" data-slide="7">
  <div class="slide-content">
    <h2>Architecture Overview</h2>
    <div class="diagram">
      <div class="diagram-box">
        <h3>Data Sources</h3>
        <p>Endpoints, Cloud, Network</p>
      </div>
      <div class="diagram-arrow">&#8594;</div>
      <div class="diagram-box highlight">
        <h3>Core Platform</h3>
        <p>Detection & Analytics</p>
      </div>
      <div class="diagram-arrow">&#8594;</div>
      <div class="diagram-box">
        <h3>AI Engine</h3>
        <p>AI Triage & Response</p>
      </div>
      <div class="diagram-arrow">&#8594;</div>
      <div class="diagram-box">
        <h3>SOC Analyst</h3>
        <p>Decision & Action</p>
      </div>
    </div>
    <p style="text-align: center; margin-top: 1.5rem;">Data flows left to right through the detection and response pipeline.</p>
  </div>
</div>
```

**When to use:** System architecture, data flow pipelines, integration diagrams, process chains. Keep to 3-5 boxes for clarity.

**Customize:**
- Number of boxes and arrow direction. Use `&#8594;` for right arrows, `&#8595;` for down arrows.
- Add `.highlight` class to the key box (gives it a blue border).
- Each box can contain an `h3` and a short `p`. Keep text minimal.

---

## 8. Callout Slide

Big callout box for key takeaways, strategic statements, or important announcements.

```html
<div class="slide" data-slide="8">
  <div class="slide-content">
    <div class="callout">
      <h2>The Bottom Line</h2>
      <p>Our AI engine reduces mean time to respond by 47% while handling 3x the alert volume — enabling teams to do more with less.</p>
    </div>
  </div>
</div>
```

**When to use:** After a section of supporting slides to drive home the key message. Good for executive summaries, strategic recommendations, and section transitions.

**Customize:**
- Heading and body text. Keep body to 1-2 sentences for maximum impact.
- The callout has a subtle gradient background (blue-to-purple). Override with inline styles for different emphasis.

---

## 9. Timeline Slide

Vertical timeline for roadmaps, milestones, historical progression, or phased plans.

```html
<div class="slide" data-slide="9">
  <div class="slide-content">
    <h2>Roadmap</h2>
    <div class="timeline">
      <div class="timeline-item">
        <div class="date">Q1 2025</div>
        <h3>Foundation</h3>
        <p>Launch core AI engine with automated alert grouping and intelligent triage.</p>
      </div>
      <div class="timeline-item">
        <div class="date">Q2 2025</div>
        <h3>Intelligence Layer</h3>
        <p>Add threat intelligence enrichment and entity risk scoring.</p>
      </div>
      <div class="timeline-item">
        <div class="date">Q3 2025</div>
        <h3>Automation</h3>
        <p>Ship response workflows and one-click remediation actions.</p>
      </div>
      <div class="timeline-item">
        <div class="date">Q4 2025</div>
        <h3>Scale</h3>
        <p>Agent builder for custom investigation playbooks and partner integrations.</p>
      </div>
    </div>
  </div>
</div>
```

**When to use:** Product roadmaps, project milestones, historical timelines, phased rollout plans. Keep to 3-5 items.

**Customize:**
- Date labels, headings, and descriptions for each milestone.
- The timeline has a gradient line (blue-to-purple) on the left with dot markers.

---

## 10. CTA / Closing Slide

Final slide with action items, next steps, and contact information.

```html
<div class="slide" data-slide="10">
  <div class="slide-content" style="text-align: center;">
    <h1>Next Steps</h1>
    <p class="lead">Ready to transform your SOC? Here is how to get started.</p>
    <div class="cta-actions" style="justify-content: center;">
      <a href="#" class="cta-btn primary">Schedule a Demo</a>
      <a href="#" class="cta-btn secondary">View Documentation</a>
    </div>
    <div style="margin-top: 3rem; color: var(--text-secondary); font-size: 0.95rem;">
      <p><strong>Your Name</strong> &mdash; your.email@company.com</p>
      <p style="margin-top: 0.5rem;">Questions? Reach out anytime.</p>
    </div>
  </div>
</div>
```

**When to use:** Always the last slide. Summarize the ask, provide clear next steps, and include contact information.

**Customize:**
- Heading: "Next Steps", "Get Started", "Thank You", or whatever fits.
- CTA buttons: `.primary` for the main action, `.secondary` for alternatives. Update `href` with real links.
- Contact section with name, email, and optional closing message.

---

## Combining Components

A typical deck structure:

| Slide | Component | Purpose |
|-------|-----------|---------|
| 1 | Title Slide | Set context |
| 2 | Content Slide | Problem statement |
| 3 | Stat Cards | Quantify the problem |
| 4 | Before/After | Show the transformation |
| 5 | Architecture | How it works |
| 6 | Timeline | Roadmap / phases |
| 7 | Quote | Customer proof point |
| 8 | Table | Feature comparison |
| 9 | Callout | Key takeaway |
| 10 | CTA / Closing | Next steps |

Adapt the order and selection to your audience. Executive audiences prefer fewer slides with bigger numbers. Technical audiences want more architecture and table slides.
