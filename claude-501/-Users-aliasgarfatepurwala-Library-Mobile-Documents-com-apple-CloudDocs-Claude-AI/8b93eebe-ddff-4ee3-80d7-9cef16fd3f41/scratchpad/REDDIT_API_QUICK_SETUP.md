# Reddit API Credentials - 2 Minute Setup

## Fastest Way to Get Client ID & Secret

### Step 1: Go to Reddit (30 seconds)
1. Go to: https://www.reddit.com/prefs/apps
2. Scroll to bottom → Click **"Create Application"**

### Step 2: Fill Form (1 minute)
Fill in:
- **name:** `Trading OS Bot` (or any name)
- **App type:** Select **"Script"** (for personal use/backend)
- **description:** `Trading automation`
- **about url:** `http://localhost:3000` (can be blank)
- **redirect uri:** `http://localhost:3000/auth/callback`

Click **"Create app"**

### Step 3: Copy Credentials (30 seconds)
You'll see a card with:

```
CLIENT ID (under the app name, looks like):
abcd1234efgh5678

SECRET (click "show"):
your_secret_key_here_very_long_string
```

Copy both.

### Step 4: Add to .env
```bash
REDDIT_CLIENT_ID=abcd1234efgh5678
REDDIT_CLIENT_SECRET=your_secret_key_here_very_long_string
```

**Done in ~2-3 minutes total.**

---

## Why I Can't Do This Myself

- Reddit OAuth requires **browser login** to reddit.com/prefs/apps
- No way for me to authenticate as you
- No existing Reddit API token in the system
- I cannot perform the click-to-create action

This is a one-time human step that takes 2 minutes max.
