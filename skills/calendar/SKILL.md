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
- On first run, a browser window will open for Google OAuth consent (one-time, calendar read-only)

## Setup

```bash
cd tools/calendar && python3 -m venv .venv && source .venv/bin/activate && pip install google-auth google-auth-oauthlib google-api-python-client
```

## Flows

### Flow 1: Today's events
```bash
cd tools/calendar && source .venv/bin/activate && python3 calendar_reader.py
```

### Flow 2: Specific date
```bash
cd tools/calendar && source .venv/bin/activate && python3 calendar_reader.py --date YYYY-MM-DD
```

### Flow 3: Upcoming events (multi-day)
```bash
cd tools/calendar && source .venv/bin/activate && python3 calendar_reader.py --days 7
```

### Flow 4: JSON output
Append `--json` to any command above for machine-readable JSON.

## First-time authentication

If `~/.ai-pm-workflow/calendar_credentials.json` does not exist, the script will open a browser for Google OAuth. The user must:
1. Sign in with their Google account
2. Grant **read-only** access to calendar events
3. Token is saved automatically and auto-refreshes

## After fetching

Present the calendar data as a concise summary:
- Group events by time
- Highlight meetings with external attendees
- Include Meet/Zoom links when present
- Note any conflicts (overlapping times)

## File locations

| File | Purpose |
|------|---------|
| `tools/calendar/calendar_reader.py` | CLI tool — fetches and formats events |
| `tools/calendar/config.py` | OAuth config, scopes, credential helpers |
| `~/.ai-pm-workflow/calendar_credentials.json` | OAuth token (auto-created) |

## Troubleshooting

- **"Missing dependency"** — Activate the venv: `cd tools/calendar && source .venv/bin/activate`
- **Browser opens on every run** — Token may be corrupted. Delete `~/.ai-pm-workflow/calendar_credentials.json` and re-authenticate.
- **"Access denied"** — Enable the Calendar API at https://console.cloud.google.com/apis/library/calendar-json.googleapis.com
