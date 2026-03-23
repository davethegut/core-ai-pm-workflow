---
name: gdocs-share
description: Read, write, and sync Google Docs. Use when the user asks to fetch a Google Doc, push content to a Doc, or keep a local file in sync with a Doc.
---

# Google Docs Reader / Writer / Sync

Interact with Google Docs programmatically. Supports three modes: read (fetch doc content), write (push content to a doc), and sync (bidirectional keep-in-sync).

## Trigger phrases

- "read this Google Doc", "fetch the doc", "pull the doc content"
- "push this to a Google Doc", "write to the doc", "update the doc"
- "sync this file with a Google Doc", "keep the doc in sync"

## Prerequisites

- Python 3.9+ with venv
- A Google Docs API OAuth client (see setup below)
- On first run, a browser window will open for Google OAuth consent (one-time)

## Setup

This skill requires Python scripts to interact with the Google Docs API. If you haven't set them up yet:

1. **Create a project directory** for your Google Docs tools (e.g., `tools/gdocs/` in your workspace)
2. **Install dependencies:**
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```
3. **Create scripts** for each mode (read, write, sync) that authenticate via OAuth and interact with the Docs API
4. **Enable the Google Docs API** at https://console.cloud.google.com/apis/library/docs.googleapis.com
5. Store OAuth tokens at `~/.ai-pm-workflow/gdocs_credentials.json`

## Modes

### Mode 1: Read a Google Doc

Fetch the full content of a Google Doc by URL or document ID.

**Options:**
- `--format markdown` — Convert to Markdown (default)
- `--format plain` — Plain text, no formatting
- `--format html` — Raw HTML export
- `--comments` — Include document comments (useful for review workflows)
- `--output output/doc-name.md` — Save to file instead of stdout

### Mode 2: Write / push to a Google Doc

Push local content to an existing Google Doc (replaces body content).

**Options:**
- `--input <file>` — Local file to push (required)
- `--append` — Append to the doc instead of replacing content
- `--title "New Title"` — Update the document title

### Mode 3: Sync (bidirectional)

Keep a local file in sync with a Google Doc. Detects which side changed and syncs accordingly.

**Options:**
- `--local <file>` — Local file path (required)
- `--direction pull` — Force pull from Google Doc to local
- `--direction push` — Force push from local to Google Doc
- `--direction auto` — Auto-detect which side changed (default)

## Bidirectional workflows

### Pull a doc, edit locally, push back

1. **Read** the doc to a local file
2. Edit the local file (or have the AI edit it)
3. Optionally run the doc-reviewer skill (`skills/doc-reviewer/SKILL.md`) for feedback
4. **Push** changes back to the Google Doc

### Continuous sync during editing

Use the sync mode with `--direction auto` to keep local and remote in sync during an editing session.

## First-time authentication

If the OAuth token does not exist, the script will open a browser for Google OAuth. The user must:
1. Sign in with their Google account
2. Grant access to Google Docs (read and write)
3. Token is saved automatically and auto-refreshes

## After fetching

When reading a Google Doc:
- Display a brief summary of the document (title, length, last modified if available)
- Show the content in the requested format
- If the user asks for review or feedback, hand off to the doc-reviewer skill (`skills/doc-reviewer/SKILL.md`)

## Troubleshooting

- **"Missing dependency"** — Make sure you activated the venv before running
- **Browser opens on every run** — Token may be corrupted. Delete `~/.ai-pm-workflow/gdocs_credentials.json` and re-authenticate.
- **"Access denied"** — Enable the Google Docs API at https://console.cloud.google.com/apis/library/docs.googleapis.com
- **"File not found"** — Ensure the document ID or URL is correct and your Google account has access to the document.
- **Push overwrites content** — By default, the write script replaces the doc body. Use `--append` to add content instead.
- **Sync conflicts** — If both local and remote changed, the sync tool will warn and ask which direction to prefer. Use `--direction pull` or `--direction push` to force.
