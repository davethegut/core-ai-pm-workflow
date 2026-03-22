---
name: doc-writer
description: Write product documents in any standard format — Concept one-pager, Problem/Solution one-pager, Decision one-pager, PRFAQ, PRD/Structured Epic, Vision Epic, or GitHub Issue. Use when creating one-pagers, feature briefs, decision docs, PRFAQs, press releases, PRDs, epics, or product specs.
---

# Document Writer

Write product documents in any standard PM format. Infer the right format from the request — don't ask the user to pick one.

## When to Use

- "Write a one-pager for ..."
- "Help me write up ..."
- "Create a brief for ..."
- "Write a decision doc for ..."
- "Write a PRFAQ for ..."
- "Create a PRD for ..."
- "Write an epic for ..."
- "Write a vision epic for ..."
- "Help me scope an epic for ..."
- "Open an issue for ..."
- "Create a GitHub issue for ..."
- "File an issue for ..."

## Seven Formats

### 1. Concept One-Pager
**Use for:** New capabilities, vision pieces, platform investments, strategic initiatives, things that don't exist yet

**Format:** Narrative (2-3 tight paragraphs)

**Structure:**
- **Paragraph 1 - Vision:** Current state problem → Desired future state → Key benefits
- **Paragraph 2 - How:** Concrete approach → User experience → Outcomes for teams

**Characteristics:**
- Reads as a story, not a checklist
- Problem-first framing
- Outcome-focused (what teams/users can DO)
- No fluff — no timelines, metrics tables, or boilerplate

### 2. Problem/Solution One-Pager
**Use for:** Enhancements to existing features, fixing gaps, improving workflows

**Format:** Structured sections

**Structure:**
- **Background & Context:** How things work today
- **Problem:** User problem + business problem (both perspectives)
- **Requirements:** Given/When/Then user stories for initial phase
- **Things we DON'T need:** Explicit scope boundaries (prevents scope creep)

**Characteristics:**
- Concrete examples (actual code, queries, UI descriptions)
- Testable acceptance criteria
- Explicit non-goals
- Technical context for engineers

### 3. Decision One-Pager
**Use for:** Choosing between real alternatives, committing resources, resolving forks in strategy or product direction

**Format:** Structured, opinionated

**Structure:**
- **Decision:** One-sentence statement of what is being decided
- **Recommendation:** Clear POV and rationale
- **Options Considered:** Real alternatives (including "do nothing" if relevant)
- **Decision Criteria:** The few dimensions that actually matter
- **Tradeoffs & Risks:** Second-order and long-term impacts
- **What Must Be True:** Assumptions and dependencies
- **Kill / Revisit Criteria:** How we know if this decision was wrong

**Characteristics:**
- Optimized for speed and clarity, not exploration
- Explicitly chooses, not just analyzes
- Avoids re-litigating background or strategy

### 4. PRFAQ
**Use for:** Validating big bets before committing resources, aligning stakeholders on vision and value for a launch

**Format:** Press release + FAQ

**Structure:**
- **Press Release:** Headline, Subheadline, Summary, Problem, Value, Customer Experience, Leadership Quote, Customer Testimonials, Call to Action
- **External FAQs:** Customer-facing, concise (what, why, how, pricing)
- **Internal FAQs:** Comprehensive (strategy, competition, KPIs, risks, rollout, dependencies)

**Characteristics:**
- Problem and Value paragraphs mirror each other
- Customer Experience section leaves room for design
- Internal FAQs thorough enough to answer any stakeholder question

**Template:** Follow `templates/prfaq-template.md` for structure.

### 5. PRD / Structured Epic
**Use for:** Full product specs with problem statement, goals, scope, detailed requirements, success criteria. Also for engineering-ready GitHub epics with work streams and child issues.

**Format:** Structured document with work streams, design decisions, and dependency graphs

**Structure:**
- **Background:** What exists today and what gap motivates this work
- **User Story / Problem Statement:** As a [role], I want [X] so that [Y]
- **The Solution:** High-level approach with UX before/after and "How It Works" steps
- **Architecture:** Mermaid diagrams showing component relationships
- **Goals & Non-Goals:** What success looks like and explicit scope boundaries
- **Work Streams:** Decomposed into streams with task checklists
- **Child Issues:** Table of sub-issues with what each delivers
- **Key Design Decisions:** Non-obvious choices with rationale and tradeoffs
- **Success Criteria:** Measurable metric/target table plus acceptance checklist
- **Technical Requirements:** Framework, dependencies, platform prerequisites
- **Related Epics:** Cross-references with relationship types and dependency graph
- **Stakeholders:** PM, Eng, Design, QA

**Characteristics:**
- Comprehensive enough for engineering to build from
- Success criteria are measurable (metric + target)
- Key design decisions explain the "why", not just the "what"
- Non-goals are explicit to prevent scope creep
- Mermaid diagrams for architecture and cross-epic dependencies

**Template:** Follow `templates/structured-epic-template.md` for structure.

### 6. Vision Epic
**Use for:** Early-stage direction-setting, new initiative areas, vision alignment before detailed scoping

**Format:** Narrative with structured support sections

**Structure:**
- **Background:** Current state and landscape context
- **What's Changing:** The catalyst — new capability, market shift, strategic decision
- **Vision:** Desired future state, concrete enough to be actionable
- **Examples:** Screenshots, prototypes, mockups showing feasibility or direction
- **Focus Areas:** Bulleted list of initial capabilities to build
- **User Stories:** 1-2 line user stories
- **Related Issues & Stakeholders**

**Characteristics:**
- Narrative-driven — reads as a story, not a checklist
- Visual — includes prototypes or screenshots when available
- Open for design exploration — sets direction without over-specifying
- Links to sub-issues for trackability

**Template:** Follow `templates/vision-epic-template.md` for structure.

### 7. GitHub Issue
**Use for:** Publishing any of the above formats directly as a GitHub issue instead of saving locally. The document format inference still applies for structuring the issue body.

See [Step 4b: GitHub Issue Output](#step-4b-github-issue-output) for the full workflow.

## Inference Logic

Infer the format from the user's request — don't ask them which format they want.

**Signals for Concept One-Pager:**
- "new", "vision", "idea", "concept", "initiative", "strategy"
- Describing something that doesn't exist yet
- Platform or infrastructure work
- Cross-cutting capabilities
- No specific existing feature referenced

**Signals for Problem/Solution One-Pager:**
- References an existing product feature or capability
- "fix", "gap", "doesn't work", "can't", "enhancement", "improvement", "support for"
- Describes something broken or incomplete
- Improving an existing workflow
- Specific technical constraints or edge cases

**Signals for Decision One-Pager:**
- "decide", "choose", "pick", "tradeoff", "option", "alternative", "which approach", "fork", "escalate"
- Presenting multiple real alternatives
- Asking for commitment on direction or resources
- Resolving disagreement or ambiguity in strategy

**Signals for PRFAQ:**
- "PRFAQ", "PR/FAQ", "press release", "launch announcement"
- Validating a big bet or major initiative
- Aligning stakeholders on vision before committing resources

**Signals for PRD / Structured Epic:**
- "PRD", "product requirements", "spec", "requirements document", "product spec"
- "epic", "write an epic", "structured epic", "engineering spec"
- Needs detailed requirements for engineering
- Work needs to be decomposed into work streams and child issues
- Full product spec with scope, acceptance criteria, and success metrics

**Signals for Vision Epic:**
- "vision epic", "direction", "initiative epic"
- Early-stage exploration before detailed scoping
- Setting direction for a new capability area
- Aligning stakeholders on "what" and "why" before engineering specs
- Prototype or mockup exists but detailed requirements don't

**Signals for GitHub Issue output:**
- "issue", "GitHub issue", "open an issue", "file an issue", "PR", "create an issue"
- These signal the user wants the document published as a GitHub issue, not saved as a local file
- The document format inference (epic, one-pager, etc.) still applies for structuring the issue body
- **You must ask the user which repo to target before creating the issue.** Never auto-select a repo.

**If unclear:** Default to Decision if the request frames multiple options or asks for a choice. Default to Problem/Solution if a specific feature is mentioned. Default to Concept if it's more abstract. Default to Structured Epic if the user says "epic" or "PRD". Default to Vision Epic if early-stage or direction-setting. If still unclear, ask one clarifying question: "Are you looking to explore a new idea, improve something existing, make a decision, validate a big bet, write a full spec, or set direction for a new initiative?"

## Process

### Step 1: Understand the Request
- What are they trying to communicate?
- What's the user/customer problem?
- What's the business context or motivation?
- Infer the format from the signals above.

### Step 2: Gather What You Need

**For Concept One-Pagers, understand:**
1. What's broken or missing today? (current state)
2. What does the ideal future look like? (vision)
3. How will we get there? (approach)
4. Who benefits and how? (outcomes)

**For Problem/Solution One-Pagers, understand:**
1. How does the feature work today? (context)
2. What can't users do? What's the pain? (user problem)
3. Why does this matter to the business? (business problem)
4. What does "done" look like? (requirements)
5. What are we explicitly NOT doing? (scope)

**For Decision One-Pagers, understand:**
1. What exactly is being decided? (decision)
2. What are the real alternatives, including "do nothing"? (options)
3. What criteria matter most? (decision criteria)
4. What are the second-order effects and risks? (tradeoffs)
5. What assumptions must hold? (dependencies)
6. How will we know if we were wrong? (kill/revisit criteria)

**For PRFAQs, understand:**
1. What are we launching? Feature/product name and what it does
2. Who is the target customer? Specific segment or persona
3. What problem does it solve? Customer pain point (not self-inflicted)
4. What value does it create? Outcome for the customer
5. How will customers use it? End-to-end experience
6. What's the strategic context? Why this, why now

**For PRDs / Structured Epics, understand:**
1. What problem are we solving and why now? (problem statement)
2. What does success look like? (goals)
3. What are we explicitly not doing? (non-goals)
4. What scenarios must the product support? (use cases)
5. What are the detailed requirements? (functional and non-functional)
6. How will we measure success? (KPIs and success criteria)
7. What are the work streams and sub-tasks? (decomposition)
8. What non-obvious decisions have been made and why? (design decisions)
9. What are the technical dependencies? (platform requirements)
10. What related epics does this connect to? (dependency graph)

**For Vision Epics, understand:**
1. What exists today and what's the landscape? (background)
2. What's changed that creates the opportunity? (catalyst)
3. What does the future state look like? (vision)
4. Are there prototypes, mockups, or screenshots? (evidence)
5. What are the initial focus areas? (scope)
6. Who are the key stakeholders? (ownership)

Ask clarifying questions if the user hasn't provided enough context. Be conversational.

### Step 3: Write the Document

Read the appropriate template first (from `templates/` in the repo root), then write.

Write in a clear, direct voice. Follow the structure for the inferred format.

**Writing principles:**
- Lead with customer problems, not features
- Be specific — use real examples, actual syntax, concrete scenarios
- Keep it tight — if a sentence doesn't add value, cut it
- Make it testable — requirements should be verifiable

### Step 4: Save and Iterate

Save the document to the appropriate output directory:
- One-pagers: `output/one-pagers/[descriptive-name].md`
- PRFAQs: `output/prfaqs/[feature-name]-prfaq.md`
- PRDs / Structured Epics: `output/prds/[feature-name]-prd.md`
- Vision Epics: `output/prds/[feature-name]-vision.md`

Ask if they want to refine any section.

### Step 4b: GitHub Issue Output

When the user asks to "open an issue", "file an issue", or "create a PR" instead of saving locally:

1. **Always ask which repo.** Before creating anything, ask: "Which repo should this go to?" Wait for the user to specify (e.g., `org/repo-name`). **Never auto-select a repo** based on content, existing issues, or workspace context.
2. **Format the issue body** using the same structured format as the inferred document type (e.g., structured epic template for epics, problem/solution structure for enhancements).
3. **Match the repo's conventions.** Check a few recent issues in the target repo to match title format and labels.
4. **Create the issue** using `gh issue create --repo <user-specified-repo>`.
5. **Return the issue URL** so the user can review it.

If the user provides the repo in their initial request (e.g., "open an issue on org/repo for ..."), skip the confirmation and proceed directly.

### Step 5: Offer Review

After drafting, offer persona-based review:

- "Want me to review this from a GM perspective before finalizing? Or a CTO review focused on simplicity and feature fit?"

If review is requested, the **doc-reviewer** skill handles it with format-aware, persona-aware feedback.

## Templates and Examples

| Format | Template |
|--------|----------|
| PRFAQ | `templates/prfaq-template.md` |
| One-pagers | `templates/one-pager-examples.md` |
| PRD / Structured Epic | `templates/structured-epic-template.md` |
| Vision Epic | `templates/vision-epic-template.md` |

## Example Prompts

- "Write a one pager for [feature]"
- "I need a one pager about [topic]"
- "Help me write up [initiative]"
- "Create a brief for [capability]"
- "Write a decision one-pager for [topic]"
- "Help me decide between [A] and [B]"
- "Write a PRFAQ for [feature]"
- "Create a PR/FAQ for [initiative]"
- "Help me write a press release for [capability]"
- "Write a PRD for [feature]"
- "Create a product spec for [capability]"
- "I need a requirements doc for [project]"
- "Write an epic for [feature]"
- "Create a structured epic for [initiative]"
- "Write a vision epic for [new capability]"
- "Help me scope an epic for [project]"
- "Open an issue for [feature]"
- "Create a GitHub issue for [initiative]"
- "File an issue on org/repo for [feature]"
