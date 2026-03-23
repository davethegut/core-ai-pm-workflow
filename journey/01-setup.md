# Step 1: Setup

Get your toolkit configured and ready to use.

## Prerequisites

Before starting, make sure you have:

- **Claude Code** or **Cursor** installed
- **GitHub CLI** (`gh`) — [Install guide](https://cli.github.com/)
- **Python 3.9+** — usually pre-installed on macOS

## 1. Clone and Open

```bash
git clone https://github.com/YOUR_USERNAME/core-ai-pm-workflow.git
cd core-ai-pm-workflow
```

Open in your tool of choice:

```bash
# Claude Code
claude

# Cursor
cursor .
```

## 2. Authenticate GitHub CLI

```bash
gh auth login
gh auth status  # Verify it worked
```

This enables the **deep-dive**, **my-initiatives**, and **doc-writer** (GitHub issue creation) skills.

## 3. Set Up Google OAuth (Optional)

If you want to use the **calendar** and **gdocs-share** skills, you'll need Google OAuth. This requires a Google Cloud project with the Calendar API and Google Docs API enabled.

### Create a Google Cloud project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the **Google Calendar API** and **Google Docs API**
4. Create OAuth 2.0 credentials (Desktop application type)
5. Download the credentials JSON file

### Configure credentials

Store your OAuth client credentials in a central location:

```bash
mkdir -p ~/.ai-pm-workflow
# Copy your OAuth client JSON to ~/.ai-pm-workflow/client_secret.json
```

The first time you use either skill, a browser window will open for you to authorize access. After that, tokens are stored locally at `~/.ai-pm-workflow/` and auto-refresh.

See `skills/calendar/SKILL.md` and `skills/gdocs-share/SKILL.md` for detailed setup instructions for each skill.

## 4. Configure Your AI Tool

### Claude Code

Skills are automatically picked up from the `skills/` directory via CLAUDE.md. No additional configuration needed.

### Cursor

Create symlinks so Cursor finds the skills:

```bash
mkdir -p .cursor/skills
ln -s ../../skills/* .cursor/skills/
```

## 5. Create Your Output Directories

```bash
mkdir -p output/{html,presentations,one-pagers,prfaqs,prds,deep-dives,competitor-research}
mkdir -p tasks
mkdir -p data/competitors/profiles
```

## 6. Verify It Works

Try these commands with your AI assistant:

```
"What skills do I have available?"
"Write a concept one-pager for a new feature idea"
```

If both work, you're ready. Head to [Step 2: Read](02-read.md).

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `gh: command not found` | Install GitHub CLI: `brew install gh` |
| `python3: command not found` | Install Python: `brew install python` |
| Google OAuth fails | Check that APIs are enabled in Google Cloud Console |
| Skills not recognized | Make sure CLAUDE.md is in the repo root |
