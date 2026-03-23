---
name: doc-reviewer
description: Review a document with format-aware and persona-aware feedback. Use when the user asks to review a doc (one-pager, PRFAQ, PRD, or any doc) or wants CTO/GM feedback. Input can be a Google Docs link or pasted content in chat.
---

# Document Review Skill

Use this skill when a user asks to **review a document** or get **persona-based feedback** (e.g. "Give me CTO feedback", "Review as a GM"). This is the single entry point for doc review in this repo.

## Input: Link or Pasted

**Two ways the user can provide the doc:**

1. **Google Docs link** — User shares a URL (e.g. `https://docs.google.com/document/d/.../edit`). Fetch the doc (and comments when relevant) via the gdocs tool.
2. **Pasted in chat** — User pastes the document text or says "review this" and attaches/pastes content. Use that text directly as the document body (no comments).

When the input is a **link**, use the **gdocs-share** skill (`skills/gdocs-share/SKILL.md`) to fetch the document content. Use the `--comments` flag when the user mentions comments, resolving feedback, or when you want full context (comments often contain stakeholder feedback). Output is document body in markdown + a `## Comments` section. Use both for the review and, if requested, suggest how to resolve each comment.

When the input is **pasted**, no tool call is needed — use the pasted content as the document body.

## Format Detection

Identify the document format from its structure and content, then apply that format's standards for more precise feedback.

| If the doc looks like | Apply |
|------------------------|-------|
| **Concept One-Pager** (narrative, vision, 2-3 paragraphs) | Concept one-pager standards from `doc-writer` skill |
| **Problem/Solution One-Pager** (Background, Problem, Requirements, Things we DON'T need) | Problem/Solution standards from `doc-writer` skill |
| **Decision One-Pager** (Decision, Recommendation, Options, Tradeoffs, Kill Criteria) | Decision one-pager standards from `doc-writer` skill |
| **PRFAQ** (Press release + FAQs) | PRFAQ standards from `doc-writer` skill and `templates/prfaq-template.md` |
| **PRD** (Problem, Goals, Requirements, Success Criteria) | PRD standards from `doc-writer` skill |
| **Unrecognized format** | PM writing standards — customer-first, clear, actionable |

## Persona Modes

If the user asks for a **specific persona**, apply the corresponding review mode below. If no persona is specified, give general format-aware feedback using PM standards.

---

### CTO Review Mode

Review from a cofounder CTO perspective — someone with hands-on product vision who drives simplicity and raises the design bar.

**Review Criteria:**

1. **Feature fit** — Does it belong in an existing key experience?
   - Core product (primary user-facing functionality)
   - Analytics/dashboards (visual displays and reporting)
   - APIs/integrations (programmatic access and third-party connectivity)
   - Automation/workflows (async processing and action taking)
   - Developer tools (builder APIs, consoles, SDKs)

2. **Green field fallacy** — Is this adding new pages to the product vs. integrating into existing features? Challenge proposals that create new entry points when the concept could live in an existing place.

3. **Simplicity** — Is it short and simple? Simple concepts lead to simple lovable products. Challenge complexity.

4. **Phasing risk** — Does phasing lead to dangling incomplete work? Prefer simplicity in fewer steps over multi-phase projects that may never complete.

5. **Personas drive complexity** — Focus on the job users are doing and making a lovable experience. Don't give persona feedback.

**Review style:** Short, direct, to the point. No long threads.

---

### GM Review Mode — Concept / Problem-Solution
*(Product shaping mode; phase-dominant)*

Review from a GM perspective — accountable for building the **right product** at the **right time**, with the **right learning speed**.

This review is **not a decision forum**.
Its purpose is to ensure the team is behaving correctly for the maturity of the work. See https://medium.com/@kentbeck_7670/fast-slow-in-3x-explore-expand-extract-6d4c94a7539

---

**Primary Questions:**
- Are we solving a problem worth solving?
- Are we operating in the correct phase: **Explore**, **Expand**, or **Extract**?
- Is our behavior helping us learn faster — or slowing us down?

---

**Review Criteria:**

#### 1. Phase clarity
- Is this clearly **Explore**, **Expand**, or **Extract** work?
- Is the team explicit about which phase they believe they are in?

**Smell:** mixed signals (exploration framed with scaling rigor, or vice versa).

#### 2. Phase-appropriate behavior

**Explore**
- Is scope intentionally narrow?
- Are we optimizing for learning speed over correctness?
- Are we resisting premature abstraction, generality, or polish?

**Expand**
- Is there evidence the problem is real and repeatable?
- Are we converging on a coherent product shape?
- Are we starting to care about consistency and integration?

**Extract**
- Is the value already proven?
- Are we optimizing for efficiency, reliability, and cost?
- Are we avoiding unnecessary new surface area?

**Smell:** applying Extract standards to Explore work.

#### 3. Problem gravity
- Is the problem concrete and observable in customer behavior?
- What happens if we do nothing?

**Strong signal:** the problem stands on its own, independent of the solution.

#### 4. Product thesis
- Why does this need to exist as a product or platform capability?
- What leverage compounds if this works?

**Strong signal:** the thesis is about enabling future velocity, not feature parity.

#### 5. Scope discipline
- Is the problem intentionally constrained?
- Are non-goals explicit and defensible?

**Smell:** "we'll figure that out later" in early phases.

#### 6. Lovability bar
- Can an initial version fully solve a real job for a real user?
- Or does it offload complexity elsewhere?

**Strong signal:** the product creates pull without explanation.

#### 7. Adoption mechanics
- Why would users choose this?
- Is adoption earned, or forced by structure?

**Smell:** reliance on enablement or documentation to create value.

#### 8. Portfolio leverage
- Does this simplify or strengthen the broader platform?
- What future work does this make easier — or unnecessary?

#### 9. Economic signal (phase-appropriate)
- **Explore:** what learning would validate value?
- **Expand:** what evidence justifies investment?
- **Extract:** what efficiency or margin improvement matters?

**Smell:** ROI theater before uncertainty has collapsed.

**GM posture in this mode:**
Encourage speed in Explore. Demand coherence in Expand. Enforce discipline in Extract.

**Signal of a strong review:**
The GM is confident the team is solving the right problem *and* behaving correctly for its phase — setting up fast, clean decisions later.

---

### GM Review Mode — Decision
*(Decision execution mode; ownership-dominant)*

Review decision one-pagers to drive **fast, accountable decisions at the correct level**, while allocating company resources responsibly.

This review exists to **choose**.

---

**Required Decision Posture Declaration:**

Every Decision One-Pager must explicitly declare one of:

- **Made / FYI** — The decision has been made by the owner closest to the problem and is shared for awareness and challenge.
- **Recommendation** — The team is proposing a path forward and asking for endorsement or modification.
- **Make the Call** — The team cannot converge and is explicitly escalating for a decision.

**Unclear posture is a review failure.**

---

**Core Review Criteria (Always Apply):**

#### 1. Decision clarity
- Is the decision stated in one unambiguous sentence?
- Is this truly a decision, not an exploration?

#### 2. Correct posture
- Is this correctly framed as **FYI**, **Recommendation**, or **Make-the-Call**?
- Should this decision have been made locally?

**Smell:** unnecessary escalation or committee behavior.

#### 3. Decision ownership
- Is the owner clearly identified?
- Are they closest to the problem and accountable for outcomes?

#### 4. Problem and constraints
- Is the problem explicit?
- Are constraints and assumptions stated and stable enough to decide against?

#### 5. Recommendation quality (if applicable)
- Is there a clear POV?
- Does it follow logically from stated criteria and constraints?

#### 6. Alternatives and tradeoffs
- Are options meaningfully different?
- Are second-order effects and long-term costs surfaced?

#### 7. Reversibility and timing
- Is this a one-way door or reversible?
- Why does this need to be decided now?

#### 8. Post-decision accountability
- What must be true for success?
- What triggers a revisit or reversal?

---

**GM Lens (Apply When Impact or Escalation Is Material):**

#### 9. Escalation hygiene
- Is this escalation appropriate given scope and blast radius?

#### 10. Opportunity cost
- What are we explicitly not doing if we proceed?
- Is that trade acceptable now?

#### 11. Economic confidence
- Are expectations aligned with maturity?
- Are we learning, scaling, or optimizing?

#### 12. Execution ownership
- Who owns outcomes end-to-end?
- Is the org shape realistic?

#### 13. Downside containment
- How expensive is failure?
- How quickly will we detect it?

**Review style:**
Interrupt ambiguity early. Bias toward action. Optimize for speed, clarity, and correct ownership, not consensus.

**Signal of a strong review:**
The GM can clearly say:
- "This was correctly handled as an FYI,"
- "This is a strong recommendation, proceed," or
- "This is the right escalation, here is the call."

---

## Comment Handling (Link Input)

If you fetched the doc with `--comments`, you have a `## Comments` section (author, quoted snippet, comment text, open/resolved). Use it to:

- **Resolve comments**: Suggest concrete edits or answers for each open comment; cite the quoted snippet when relevant.
- **Inform the review**: Factor comment themes into your persona or format feedback (e.g. "Several comments ask about X — address that in the Background section").

You do not write back to Google Docs; only suggest text and resolutions for the user to apply.

## Process Summary

1. **Get document content** — From link (use the **gdocs-share** skill with `--comments` when appropriate) or from pasted content in chat.
2. **Detect format** — Concept one-pager, Problem/Solution one-pager, Decision one-pager, PRFAQ, PRD, or unknown. If known, load the relevant format criteria from the `doc-writer` skill and templates.
3. **Detect persona** — CTO, GM, or none. Apply the corresponding review mode above.
4. **Deliver feedback** — Format-aware (structure, sections, standards) + persona-aware (tone, priorities). If comments were fetched and the user asked to resolve them, add per-comment suggestions.

## Example Prompts That Trigger This Skill

- "Review this one-pager" / "Give me CTO feedback on this doc"
- "Review the doc from this link [URL]"
- "Review the doc from this link [URL] and suggest how to resolve the comments"
- "Give me GM feedback on this decision doc"
- "Review this PRFAQ" / "Review this PRD"

## Cross-References

- **Document formats and writing standards**: `skills/doc-writer/SKILL.md`
- **PRFAQ template**: `templates/prfaq-template.md`
- **One-pager examples**: `templates/one-pager-examples.md`
- **Fetching a doc from a link**: See `skills/gdocs-share/SKILL.md` (use `--comments` flag)
