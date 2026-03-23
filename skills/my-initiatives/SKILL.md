---
name: my-initiatives
description: Track and surface your GitHub issues and initiatives across multiple repositories. Use when the user asks about epics, team issues, PM action items, or wants to sync GitHub tasks.
---

# My Initiatives Skill

## Purpose

Track and surface your GitHub issues and initiatives across multiple repositories. Syncs issue status from GitHub into a local task file and presents a categorized, prioritized view of your active work.

## Trigger

User says: "my initiatives", "show my issues", "sync initiatives", "what am I tracking", "initiative status"

## Setup

### Configuration

Create a configuration file at `skills/my-initiatives/config.yaml`. This file should be gitignored since it contains your specific setup.

An example is provided at `skills/my-initiatives/config.example.yaml`.

#### Config Schema

```yaml
# skills/my-initiatives/config.yaml

github_username: "your-username"

repos:
  - name: "org/repo-name"
    labels:
      team: "Team:YourTeam"
      epic: "Epic"
      pm_action: "pm-action"
    categories:
      "Feature A": ["feature-a", "Feature A"]
      "Feature B": ["feature-b"]

  - name: "org/another-repo"
    labels:
      team: "Team:YourTeam"
      epic: "Epic"
      pm_action: "pm-action"
    categories:
      "Platform Work": ["platform", "infra"]
      "Feature A": ["feature-a"]

task_file: "tasks/ACTIVE.md"
```

#### Config Reference

| Field | Type | Required | Description |
|---|---|---|---|
| `github_username` | string | yes | Your GitHub username for filtering assignments |
| `repos` | list | yes | Repositories to track |
| `repos[].name` | string | yes | Repo in `org/repo` format |
| `repos[].labels.team` | string | no | Label identifying your team's issues |
| `repos[].labels.epic` | string | no | Label identifying epics |
| `repos[].labels.pm_action` | string | no | Label flagging issues needing PM action |
| `repos[].categories` | object | no | Map of category name to list of matching labels |
| `task_file` | string | yes | Path to the local markdown file for synced initiatives |

## Workflow

### Step 1: Load Configuration

Read `skills/my-initiatives/config.yaml`. If it does not exist, prompt the user:

> "No initiatives config found. Would you like me to set one up? I'll need your GitHub username and the repos you track."

Walk the user through interactive setup if they agree.

### Step 2: Fetch Issues from GitHub (use subagents)

Spawn a subagent per repo to fetch issues in parallel using `gh` CLI.

For each configured repo, run queries like:

```bash
# Issues assigned to you
gh issue list --repo org/repo-name --assignee your-username --state open --json number,title,labels,state,updatedAt,url --limit 100

# Issues with your team label
gh issue list --repo org/repo-name --label "Team:YourTeam" --state open --json number,title,labels,state,updatedAt,url --limit 100

# Issues needing PM action
gh issue list --repo org/repo-name --label "pm-action" --state open --json number,title,labels,state,updatedAt,url --limit 50

# Epics
gh issue list --repo org/repo-name --label "Epic" --state open --json number,title,labels,state,updatedAt,url --limit 50
```

### Step 3: Categorize and Deduplicate

For each issue:
1. Match against configured categories by checking the issue's labels against the category label lists
2. If an issue matches multiple categories, use the first match
3. If no category matches, place in "Uncategorized"
4. Deduplicate issues that appear in multiple queries

### Step 4: Identify PM Action Items

Flag issues that need your attention:
- Issues with the `pm_action` label
- Issues assigned to you that were updated in the last 48 hours
- Epics with no recent activity (stale for 14+ days)
- Issues with new comments since you last synced

### Step 5: Generate Report

Present the categorized view:

```markdown
## My Initiatives — [Date]

### Needs Action (X issues)

| # | Title | Repo | Category | Last Updated | Why |
|---|---|---|---|---|---|
| #123 | Add widget support | org/repo | Feature A | 2 days ago | pm-action label |
| #456 | Q2 roadmap epic | org/repo | Platform | 15 days ago | Stale epic |

### By Category

#### Feature A (X issues)
- [#123 Add widget support](url) — `pm-action` `in-progress` — updated 2d ago
- [#124 Widget API design](url) — `in-review` — updated 5d ago

#### Feature B (X issues)
- [#200 New onboarding flow](url) — `epic` `in-progress` — updated 1d ago

#### Platform Work (X issues)
- [#300 Migrate to new API](url) — `in-progress` — updated 3d ago

#### Uncategorized (X issues)
- [#400 Bug: login redirect](url) — `bug` — updated 1d ago

### Summary
- **Total open issues:** X
- **Needing PM action:** X
- **Epics:** X (Y active, Z stale)
- **Updated in last 7 days:** X
```

### Step 6: Sync to Task File

If `task_file` is configured, update the specified file with the current initiative state. Preserve any manual notes or annotations the user has added.

The sync should:
- Add new issues not already in the file
- Update status of existing issues
- Mark issues that were closed since last sync
- Never delete manual notes the user added

### Step 7: Offer Follow-ups

After presenting:
- "Want me to open any of these issues in the browser?"
- "Should I update your task file?"
- "Want to filter by a specific category?"
- "Should I check for recently closed issues too?"

## Interactive Configuration

If the user says "configure initiatives" or "set up my initiatives", walk them through:

1. **What is your GitHub username?**
2. **What repos do you track?** (org/repo format, one at a time)
3. For each repo:
   - What label identifies your team's issues?
   - What label marks epics?
   - What label flags PM action items?
   - What categories do you use, and what labels map to each?
4. **Where should I sync the initiative list?** (default: `tasks/ACTIVE.md`)
5. Generate the `config.yaml` file

## Files

| File | Purpose | Git Status |
|---|---|---|
| `skills/my-initiatives/SKILL.md` | This file — skill definition | Tracked |
| `skills/my-initiatives/config.example.yaml` | Example config for reference | Tracked |
| `skills/my-initiatives/config.yaml` | Your actual config (contains your repos/labels) | **Gitignored** |

## Tips

- Run this daily alongside your morning standup for a complete picture.
- Use the `pm-action` label convention across repos so the skill can surface what needs your attention.
- Keep categories aligned with your roadmap themes for easy reporting.
- If you track issues across many repos, the parallel subagent approach keeps this fast even with 5-10 repos.
- Combine with `gh issue view <number> --repo org/repo` to drill into any specific issue from the report.
