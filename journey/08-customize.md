# Step 8: Customize — Make It Yours

The core skills work out of the box. These two require your configuration to be truly useful.

## Skills Used

- **Morning Standup** — Daily metric check-in
- **My Initiatives** — GitHub issue tracking

---

## Exercise 1: Configure Your Morning Standup

Say:

```
"Help me configure my morning standup metrics"
```

The AI will ask:
1. What's your role? (PM, Engineering Lead, Executive)
2. What product areas do you focus on?
3. What questions do you want answered every morning?

Then it creates a `metrics.yaml` config file with your personalized metrics.

### Example metrics you might configure:

| Role | Example metrics |
|------|----------------|
| **PM** | Feature adoption milestones, conversion rates, usage trends |
| **Engineering Lead** | Health scores, error rates, deployment success |
| **Executive** | Growth KPIs, customer health, platform snapshot |

### Run it daily:

```
"Run my morning standup"
```

You get a red/yellow/green report of what needs your attention.

### Bring your own data source

The standup works with any SQL-compatible data source. Configure your query runner in the metrics.yaml:

```yaml
alerts:
  - name: "Feature Adoption"
    priority: high
    query: |
      SELECT COUNT(DISTINCT user_id) AS users
      FROM your_table
      WHERE date = CURRENT_DATE - 1
        AND feature_used = 'your_feature'
    milestone: "> 5000"
    target: 5000
```

---

## Exercise 2: Configure Your Initiative Tracker

Say:

```
"Help me set up my initiative tracker"
```

The AI will ask:
1. Your GitHub username
2. Which repos to track
3. What labels to filter by
4. How to categorize your issues

Then it creates a `config.yaml` for the my-initiatives skill.

### Sync your tasks:

```
"Sync my tasks from GitHub"
```

This pulls your assigned issues and organizes them into your `tasks/ACTIVE.md` file.

### Browse your team's work:

```
"Show my team's epics"
"What needs PM input?"
"What's in the current release?"
```

---

## Exercise 3: Add Your Own Skill

Want to add a workflow specific to your team? Create a new skill:

```bash
mkdir skills/my-custom-skill
```

Create `skills/my-custom-skill/SKILL.md` with this structure:

```markdown
---
name: my-custom-skill
description: What this skill does. When to trigger it.
---

# My Custom Skill

## When to Use
- "trigger phrase one"
- "trigger phrase two"

## Process
1. Step one
2. Step two
3. Step three
```

The AI will pick it up automatically on next conversation.

---

## You're Done

You now have:
- 10 working skills
- A daily standup configured for your role
- GitHub issues synced to your task list
- The ability to add your own skills

The workflow is:
1. **Morning:** Run standup, check calendar, sync GitHub tasks
2. **During the day:** Research, write, review, present — as needed
3. **Ship:** Push to Google Docs or GitHub when ready

Welcome to the Core AI PM Workflow.
