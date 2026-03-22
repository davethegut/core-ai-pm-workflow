# CLAUDE.md

This file configures Claude Code (and Cursor) when working in this repository.

## What This Repo Is

**The Core AI PM Workflow** — a ready-made toolkit of AI-powered skills that help Product Managers win back hours every week. Clone it, configure it, start using it.

## Skills

This repo ships 10 skills. Each skill is a self-contained prompt + process in `skills/<name>/SKILL.md`.

| Skill | What it does | Trigger |
|-------|-------------|---------|
| **calendar** | Shows today's meetings from Google Calendar | "what's on my calendar" |
| **gdocs-share** | Read, write, and sync Google Docs | "read this Google Doc" |
| **deep-dive** | Research any GitHub repo → polished HTML doc | "deep dive into [topic] in [repo]" |
| **competitor-research** | Research competitors → structured analysis | "research [competitor]" |
| **doc-writer** | Write product docs (7 formats) | "write a one-pager for..." |
| **doc-reviewer** | Review docs with CTO/GM persona feedback | "review this doc as a CTO" |
| **html-reference-page** | Generate styled, self-contained HTML pages | "create a reference page for..." |
| **presentation** | Generate HTML slide decks | "create a presentation about..." |
| **morning-standup** | Daily standup with configurable metrics | "run my morning standup" |
| **my-initiatives** | Track your GitHub issues and sync to tasks | "show my team's epics" |

## Directory Structure

```
skills/           → All 10 skills (SKILL.md files + supporting templates)
journey/          → Guided walkthrough (start here if you're new)
templates/        → Document templates (PRD, PRFAQ, one-pager, epic)
output/           → Where generated artifacts go (gitignored)
tools/            → Python scripts (calendar, Google Docs)
tasks/            → Your task tracking (ACTIVE.md, GOALS.md)
data/             → Persistent data (competitor profiles, configs)
```

## Getting Started

1. Read `journey/01-setup.md` for installation and configuration
2. Follow the journey docs in order, or jump to any skill that interests you
3. Each skill has a `SKILL.md` with trigger phrases, process, and examples

## Conventions

- **Output goes to `output/`** — all generated docs, HTML pages, presentations, and research
- **Config goes to `data/`** — competitor profiles, metric configs, personal settings
- **Tasks go to `tasks/`** — your ACTIVE.md, GOALS.md, BACKLOG.md
- **Templates are in `templates/`** — doc format templates shared across skills

## Tool Prerequisites

| Tool | Required For | Install |
|------|-------------|---------|
| `gh` CLI | deep-dive, my-initiatives | `brew install gh && gh auth login` |
| Python 3.9+ | calendar, gdocs-share | Usually pre-installed on macOS |
| Google OAuth | calendar, gdocs-share | Configured on first run (browser opens automatically) |

## How Skills Work

Each skill in `skills/<name>/SKILL.md` contains:
- **Frontmatter** with name, description, and trigger phrases
- **Process** — step-by-step instructions the AI follows
- **Templates** — referenced files for consistent output
- **Examples** — sample prompts that activate the skill

When you say something that matches a skill's trigger (e.g., "write a one-pager"), the AI reads the skill file and follows its process. You don't need to remember exact commands — just describe what you want naturally.

## Compatibility

This toolkit works with:
- **Claude Code** — Skills go in `.claude/skills/` (symlinked during setup)
- **Cursor** — Skills go in `.cursor/skills/` (symlinked during setup)

The journey setup guide covers configuration for both.
