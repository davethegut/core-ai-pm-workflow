---
name: morning-standup
description: Generate a daily standup report with key metrics, status indicators, and actionable highlights. Use when the user asks to run standup, check metrics, or wants a morning check-in on key indicators.
---

# Morning Standup Skill

## Purpose

Generate a daily standup report with key metrics, status indicators, and actionable highlights. This is a **template-based skill** — you configure your own data sources, metrics, and thresholds, and the skill produces a consistent red/yellow/green report each morning.

> **This skill works with any SQL-compatible data source (BigQuery, PostgreSQL, Snowflake, etc.) — configure your query runner in the setup step.**

## Trigger

User says: "standup", "morning standup", "daily metrics", "how are my numbers"

## Setup

### Step 1: Configure Your Query Runner

The skill needs a way to execute SQL queries against your data source. Set the `query_runner` field in your config to the command that runs a SQL query and returns results.

Examples:
```yaml
# BigQuery (using bq CLI)
query_runner: "bq query --use_legacy_sql=false --format=json"

# BigQuery (using a custom Python script)
query_runner: "python3 my_query_runner.py -y"

# PostgreSQL
query_runner: "psql -h myhost -d mydb -c"

# Snowflake
query_runner: "snowsql -q"
```

### Step 2: Define Your Metrics

Create a configuration file at `skills/morning-standup/metrics.yaml` (this file should be gitignored since it contains your specific setup).

An example configuration is provided at `skills/morning-standup/metrics.example.yaml`.

### Configuration Schema

```yaml
# skills/morning-standup/metrics.yaml

query_runner: "python3 my_query_runner.py --execute"

role: "Product Manager"  # Used to tailor report framing

metrics:
  - name: "Daily Active Users"
    slug: "dau"
    type: "threshold"          # threshold | milestone | trend
    query: |
      SELECT COUNT(DISTINCT user_id) AS value
      FROM usage_events
      WHERE event_date = CURRENT_DATE - 1
    threshold:
      green: ">= 1000"
      yellow: ">= 500"
      red: "< 500"
    compare_to: "previous_period"  # previous_period | fixed_target | none
    compare_query: |
      SELECT COUNT(DISTINCT user_id) AS value
      FROM usage_events
      WHERE event_date = CURRENT_DATE - 8
    alert_if: "red"

  - name: "Feature Adoption Rate"
    slug: "feature-adoption"
    type: "milestone"
    query: |
      SELECT
        ROUND(100.0 * COUNT(DISTINCT CASE WHEN used_feature THEN user_id END)
        / COUNT(DISTINCT user_id), 1) AS value
      FROM user_activity
      WHERE event_date >= CURRENT_DATE - 7
    milestones:
      - label: "10% adoption"
        target: 10
      - label: "25% adoption"
        target: 25
      - label: "50% adoption"
        target: 50
    alert_if: "below_next_milestone"

  - name: "Weekly Active Users"
    slug: "wau"
    type: "trend"
    query: |
      SELECT event_week, COUNT(DISTINCT user_id) AS value
      FROM usage_events
      WHERE event_date >= CURRENT_DATE - 56
      GROUP BY event_week
      ORDER BY event_week
    trend:
      direction: "up"        # up | down — which direction is good
      alert_if: "3_week_decline"

sections:
  - title: "Growth Metrics"
    metrics: ["dau", "wau"]
  - title: "Adoption Metrics"
    metrics: ["feature-adoption"]
```

### Metric Schema Reference

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Human-readable metric name |
| `slug` | string | yes | Unique identifier |
| `type` | enum | yes | `threshold`, `milestone`, or `trend` |
| `query` | string | yes | SQL query returning a `value` column |
| `threshold` | object | if type=threshold | `green`, `yellow`, `red` conditions |
| `compare_to` | string | no | `previous_period`, `fixed_target`, or `none` |
| `compare_query` | string | no | SQL for the comparison value |
| `alert_if` | string | no | When to flag this metric (e.g., `red`, `below_next_milestone`, `3_week_decline`) |
| `milestones` | list | if type=milestone | Ordered list of `{label, target}` |
| `trend.direction` | string | if type=trend | `up` or `down` — which way is good |

## Workflow

### Step 1: Load Configuration

Read `skills/morning-standup/metrics.yaml`. If it does not exist, prompt the user:

> "No metrics config found. Would you like me to create one from the example template? You'll need to fill in your SQL queries and thresholds."

If the user agrees, copy `metrics.example.yaml` to `metrics.yaml` and open it for editing.

### Step 2: Execute Queries (use subagents)

Spawn a subagent to run all SQL queries in parallel using the configured `query_runner`. For each metric:
1. Run the primary query
2. Run the comparison query (if configured)
3. Evaluate thresholds / milestones / trends
4. Assign status: GREEN, YELLOW, or RED

### Step 3: Generate Report

Produce a standup report in this format:

```
## Morning Standup — [Date]

### [Section Title]

| Metric | Value | Status | vs. Prior | Notes |
|---|---|---|---|---|
| Daily Active Users | 1,234 | GREEN | +12% WoW | Steady growth |
| Weekly Active Users | 5,678 | YELLOW | -3% WoW | Slight dip — monitor |

### [Section Title]

| Metric | Value | Status | vs. Prior | Notes |
|---|---|---|---|---|
| Feature Adoption | 18.2% | GREEN | Next milestone: 25% | On track |

---

### Alerts
- YELLOW: Weekly Active Users declined 3% week-over-week
- Watch: Feature Adoption approaching 25% milestone (18.2%)

### Suggested Actions
- Investigate WAU dip — check if related to a specific cohort or region
- Plan push for 25% adoption milestone
```

### Step 4: Present and Offer Follow-ups

After presenting the report, offer:
- "Want me to dig into any of these metrics?"
- "Should I update your task file with action items?"
- "Want to compare against a different time period?"

## Interactive Configuration

If the user says "configure standup" or "set up standup metrics", walk them through:

1. **What data source do you use?** (BigQuery, PostgreSQL, Snowflake, other)
2. **What metrics do you track daily?** (list them)
3. For each metric:
   - What SQL query produces the value?
   - What are the green/yellow/red thresholds?
   - What should you compare against? (last week, last month, fixed target)
4. **How should metrics be grouped in the report?** (sections)
5. Generate the `metrics.yaml` file

## Files

| File | Purpose | Git Status |
|---|---|---|
| `skills/morning-standup/SKILL.md` | This file — skill definition | Tracked |
| `skills/morning-standup/metrics.example.yaml` | Example config for reference | Tracked |
| `skills/morning-standup/metrics.yaml` | Your actual config (contains your queries) | **Gitignored** |

## Tips

- Start simple with 3-5 metrics, then expand as you build the habit.
- Set thresholds conservatively at first — too many red alerts causes alert fatigue.
- The `compare_to: previous_period` pattern works well for spotting week-over-week changes.
- Combine this with the `my-initiatives` skill to get both metrics and initiative status in one morning review.
