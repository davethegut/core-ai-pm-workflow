---
name: calendar
description: Fetch and display calendar events from Google Calendar. Read-only access. Use when the user asks about meetings, schedule, or calendar.
---

# Google Calendar Reader

Fetch and display today's meetings from Google Calendar. Read-only access.

## Trigger phrases

- "what meetings do I have", "show my calendar", "today's schedule"
- "what's on my calendar", "calendar for today", "upcoming meetings"

## Prerequisites

- Python 3.9+ with venv
- A Google Calendar API OAuth client (see setup below)
- On first run, a browser window will open for Google OAuth consent (one-time, calendar read-only)

## Setup

This skill requires a small Python script to fetch calendar events via the Google Calendar API. If you haven't set one up yet:

1. **Create a project directory** for your calendar tool (e.g., `tools/calendar/` in your workspace)
2. **Install dependencies:**
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```
3. **Create a script** that authenticates via OAuth and fetches events from the Calendar API. The script should:
   - Accept optional `--date YYYY-MM-DD` and `--days N` flags
   - Support `--json` output for machine-readable results
   - Store OAuth tokens at `~/.ai-pm-workflow/calendar_credentials.json`
4. **Enable the Calendar API** at https://console.cloud.google.com/apis/library/calendar-json.googleapis.com

## Flows

### Flow 1: Today's events
Run your calendar script with no arguments to fetch today's events.

### Flow 2: Specific date
Run with `--date YYYY-MM-DD` to fetch events for a specific day.

### Flow 3: Upcoming events (multi-day)
Run with `--days 7` to fetch the next 7 days of events.

### Flow 4: JSON output
Append `--json` to any command above for machine-readable JSON.

## First-time authentication

If the OAuth token does not exist, the script will open a browser for Google OAuth. The user must:
1. Sign in with their Google account
2. Grant **read-only** access to calendar events
3. Token is saved automatically and auto-refreshes

## After fetching

Present the calendar data as a concise summary:
- Group events by time
- Highlight meetings with external attendees
- Include Meet/Zoom links when present
- Note any conflicts (overlapping times)

## Troubleshooting

- **"Missing dependency"** — Make sure you activated the venv before running
- **Browser opens on every run** — Token may be corrupted. Delete `~/.ai-pm-workflow/calendar_credentials.json` and re-authenticate.
- **"Access denied"** — Enable the Calendar API at https://console.cloud.google.com/apis/library/calendar-json.googleapis.com
