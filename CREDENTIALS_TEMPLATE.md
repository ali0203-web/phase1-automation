# 🔐 CREDENTIALS SETUP TEMPLATE
**Complete Guide to Gathering All Required API Keys**

---

## 📋 Instructions

1. **Go through each service below**
2. **Follow the setup instructions** for each one
3. **Copy the generated credentials** to the corresponding section
4. **Keep this file secure** - it contains sensitive information
5. **Use these values** when adding secrets to Railway (Step 5 in deployment guide)

---

## 1️⃣ OPENROUTER (Claude API)

### Setup Instructions
1. Go to: https://openrouter.io/keys
2. Sign up or log in with GitHub
3. Click "Create Key"
4. Name it: `automation-suite-production`
5. Copy the API key

### Your Credentials
```
OPENROUTER_API_KEY = sk-or-[COPY_HERE]
OPENROUTER_MODEL = claude-3-sonnet-20240229
```

### Verification
```bash
curl https://openrouter.io/api/v1/models \
  -H "Authorization: Bearer sk-or-[YOUR_KEY]"
```

---

## 2️⃣ LINKEDIN OAUTH

### Setup Instructions
1. Go to: https://www.linkedin.com/developers/apps
2. Click "Create app"
3. Fill in:
   - App name: `Automation Suite`
   - LinkedIn Page: (select or create)
   - App logo: (upload)
   - Legal agreement: Accept
4. Click "Create app"
5. Go to "Auth" tab
6. Set Authorized redirect URLs:
   ```
   https://api.domain.com/oauth/linkedin
   https://localhost:3000/oauth/linkedin
   ```
7. Copy Client ID and Client Secret

### Your Credentials
```
LINKEDIN_CLIENT_ID = [COPY_HERE]
LINKEDIN_CLIENT_SECRET = [COPY_HERE]
LINKEDIN_REDIRECT_URI = https://api.domain.com/oauth/linkedin
```

### Permissions Needed
- ✓ w_member_social (Post on behalf of member)
- ✓ r_liteprofile (Read member profile)
- ✓ r_emailaddress (Read email address)

### Verification
```bash
curl -X POST https://www.linkedin.com/oauth/v2/accessToken \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=[CLIENT_ID]&client_secret=[CLIENT_SECRET]"
```

---

## 3️⃣ DISCORD BOT

### Setup Instructions
1. Go to: https://discord.com/developers/applications
2. Click "New Application"
3. Name: `Automation Suite Bot`
4. Accept Terms
5. Go to "Bot" section
6. Click "Add Bot"
7. Under "TOKEN", click "Copy"
8. Copy the Bot Token
9. Go to "OAuth2" → "URL Generator"
10. Select Scopes:
    - `bot`
11. Select Permissions:
    - `Send Messages`
    - `Read Messages/View Channels`
    - `Manage Messages`
    - `Embed Links`
    - `Read Message History`
12. Copy the generated URL and invite bot to your server
13. Go to "OAuth2" → "General"
14. Copy Client ID

### Your Credentials
```
DISCORD_BOT_TOKEN = [COPY_HERE]
DISCORD_CLIENT_ID = [COPY_HERE]
DISCORD_CLIENT_SECRET = [COPY_HERE]
DISCORD_GUILD_ID = [YOUR_GUILD_ID]
```

### Find Guild ID
1. Enable Developer Mode in Discord (User Settings → Advanced → Developer Mode)
2. Right-click your server name
3. Click "Copy Server ID"
4. That's your GUILD_ID

### Verification
```bash
curl https://discord.com/api/v10/users/@me \
  -H "Authorization: Bot [BOT_TOKEN]"
```

---

## 4️⃣ AIRTABLE

### Setup Instructions
1. Go to: https://airtable.com/app
2. Create a new base called: `Automation Suite`
3. Create a table called: `LinkedIn_Content`
4. Add columns:
   - `Content` (Long text)
   - `Scheduled_Date` (Date)
   - `Status` (Single select: Draft/Scheduled/Published)
   - `LinkedIn_URL` (URL)
   - `Engagement_Rate` (Number)
5. Go to: https://airtable.com/account/tokens
6. Click "Create token"
7. Set scope: `data.records:read`, `data.records:write`
8. Set workspace access: Your workspace
9. Copy the token
10. Get Base ID: Open your base, URL is `https://airtable.com/[BASE_ID]/...`

### Your Credentials
```
AIRTABLE_API_KEY = [COPY_HERE]
AIRTABLE_BASE_ID = [COPY_HERE]
AIRTABLE_TABLE = LinkedIn_Content
```

### Verification
```bash
curl https://api.airtable.com/v0/[BASE_ID]/LinkedIn_Content \
  -H "Authorization: Bearer [API_KEY]"
```

---

## 5️⃣ BINANCE (SANDBOX)

### Setup Instructions
1. Go to: https://testnet.binance.vision
2. Sign up with email
3. Go to: https://testnet.binance.vision/key/api
4. Click "Create API Key"
5. Label: `automation-suite-trading`
6. Restrictions: Spot/Margin Trading
7. Copy API Key and Secret Key
8. **IMPORTANT:** Use testnet URL, not production

### Your Credentials
```
BINANCE_API_KEY = [COPY_TESTNET_KEY_HERE]
BINANCE_API_SECRET = [COPY_TESTNET_SECRET_HERE]
BINANCE_TESTNET = true
BINANCE_BASE_URL = https://testnet.binance.vision
```

### Sandbox Capital
- Default: $10,000 USDT
- Can request more at testnet dashboard

### Verification
```bash
curl https://testnet.binance.vision/api/v3/account \
  -H "X-MBX-APIKEY: [API_KEY]"
```

---

## 6️⃣ SUPABASE

### Setup Instructions
1. Go to: https://supabase.com
2. Click "Start your project"
3. Sign up with GitHub
4. Click "New Project"
5. Fill in:
   - Project name: `automation-suite`
   - Database password: (generate secure password)
   - Region: (closest to your location)
6. Wait for provisioning (~2 minutes)
7. Go to "Project Settings" → "API"
8. Copy:
   - Project URL
   - anon public key (API Key)
9. Get Project ID from URL: `https://[PROJECT_ID].supabase.co`

### Your Credentials
```
SUPABASE_PROJECT_ID = [COPY_HERE]
SUPABASE_API_KEY = [COPY_ANON_KEY_HERE]
SUPABASE_URL = https://[PROJECT_ID].supabase.co
SUPABASE_POSTGRES_PASSWORD = [YOUR_DB_PASSWORD]
```

### Create Tables
```sql
-- Run in Supabase SQL Editor
CREATE TABLE IF NOT EXISTS analytics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  metric_name VARCHAR NOT NULL,
  value NUMERIC NOT NULL,
  timestamp TIMESTAMP DEFAULT NOW(),
  source VARCHAR
);

CREATE TABLE IF NOT EXISTS trades (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  symbol VARCHAR NOT NULL,
  quantity NUMERIC NOT NULL,
  entry_price NUMERIC NOT NULL,
  exit_price NUMERIC,
  pnl NUMERIC,
  timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS integrations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  service VARCHAR NOT NULL,
  status VARCHAR DEFAULT 'active',
  last_sync TIMESTAMP,
  next_sync TIMESTAMP
);
```

### Verification
```bash
curl -X GET https://[PROJECT_ID].supabase.co/rest/v1/analytics \
  -H "apikey: [API_KEY]" \
  -H "Authorization: Bearer [API_KEY]"
```

---

## 7️⃣ SLACK (WEBHOOKS)

### Setup Instructions
1. Go to: https://api.slack.com/apps
2. Click "Create New App"
3. Select "From scratch"
4. App name: `Automation Suite`
5. Pick a workspace
6. Go to "Incoming Webhooks"
7. Click "Add New Webhook to Workspace"
8. Select channel: `#automation-alerts`
9. Copy the Webhook URL
10. For monitoring channel, repeat for `#monitoring`

### Your Credentials
```
SLACK_WEBHOOK = https://hooks.slack.com/services/T.../B.../X...
SLACK_CHANNEL = #automation-alerts
```

### Verification
```bash
curl -X POST [SLACK_WEBHOOK] \
  -H 'Content-type: application/json' \
  -d '{"text":"Test message from automation suite"}'
```

---

## 8️⃣ DISCORD WEBHOOK (MONITORING)

### Setup Instructions
1. In your Discord server
2. Right-click `#monitoring` channel
3. Select "Edit Channel"
4. Go to "Integrations" → "Webhooks"
5. Click "New Webhook"
6. Name: `Automation Suite`
7. Click "Copy Webhook URL"

### Your Credentials
```
DISCORD_WEBHOOK = https://discordapp.com/api/webhooks/[ID]/[TOKEN]
```

### Verification
```bash
curl -X POST [DISCORD_WEBHOOK] \
  -H 'Content-type: application/json' \
  -d '{"content":"Test message from automation suite"}'
```

---

## 9️⃣ DATABASE CREDENTIALS

### Generate Secure Passwords
```bash
# Generate a random password
openssl rand -base64 32

# Example output (use this format)
# L4kP9mN2xR8qW5vB3tY7uI6oP1sD4fG8=
```

### Your Credentials
```
DB_HOST = postgres.railway.internal
DB_NAME = automation_db
DB_USER = postgres
DB_PASSWORD = [GENERATE_SECURE_PASSWORD]
```

---

## 🔟 ENVIRONMENT CONFIGURATION

### Standard Settings
```
NODE_ENV = production
PYTHON_ENV = production
LOG_LEVEL = info
REBALANCE_TIME = 08:00
REBALANCE_TIMEZONE = Asia/Dubai
```

---

## 📋 COMPLETE CREDENTIALS CHECKLIST

Copy this section and fill it in as you gather credentials:

```
OPENROUTER_API_KEY = [ ]
OPENROUTER_MODEL = [ ]

LINKEDIN_CLIENT_ID = [ ]
LINKEDIN_CLIENT_SECRET = [ ]
LINKEDIN_REDIRECT_URI = [ ]

AIRTABLE_API_KEY = [ ]
AIRTABLE_BASE_ID = [ ]
AIRTABLE_TABLE = [ ]

DISCORD_BOT_TOKEN = [ ]
DISCORD_CLIENT_ID = [ ]
DISCORD_CLIENT_SECRET = [ ]
DISCORD_GUILD_ID = [ ]

BINANCE_API_KEY = [ ]
BINANCE_API_SECRET = [ ]
BINANCE_TESTNET = [ ]

SUPABASE_PROJECT_ID = [ ]
SUPABASE_API_KEY = [ ]
SUPABASE_URL = [ ]

SLACK_WEBHOOK = [ ]
SLACK_CHANNEL = [ ]

DISCORD_WEBHOOK = [ ]

DB_HOST = [ ]
DB_NAME = [ ]
DB_USER = [ ]
DB_PASSWORD = [ ]

NODE_ENV = [ ]
PYTHON_ENV = [ ]
LOG_LEVEL = [ ]

REBALANCE_TIME = [ ]
REBALANCE_TIMEZONE = [ ]
```

---

## ⏱️ ESTIMATED TIME

| Service | Setup Time | Notes |
|---------|-----------|-------|
| OpenRouter | 2 min | Just copy key |
| LinkedIn | 5 min | Create app |
| Discord | 5 min | Create bot & add to server |
| Airtable | 5 min | Create base & table |
| Binance | 3 min | Testnet account |
| Supabase | 5 min | Create project |
| Slack | 3 min | Create webhooks |
| Discord Webhook | 2 min | Add to channel |
| **TOTAL** | **~30 min** | **All credentials ready** |

---

## 🔒 Security Best Practices

- ✅ Never commit this file to git
- ✅ Use `.gitignore` to exclude credentials
- ✅ Rotate keys regularly
- ✅ Use separate keys for dev/prod
- ✅ Store in password manager
- ✅ Use Railway secrets, not `.env` files
- ✅ Limit API key permissions to what's needed
- ✅ Audit access logs regularly

---

## ✅ Verification Commands

Test all credentials at once:

```bash
#!/bin/bash

echo "Testing OpenRouter..."
curl -s https://openrouter.io/api/v1/models \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" | head -c 50

echo -e "\n\nTesting Airtable..."
curl -s https://api.airtable.com/v0/meta/bases \
  -H "Authorization: Bearer $AIRTABLE_API_KEY" | head -c 50

echo -e "\n\nTesting Discord..."
curl -s https://discord.com/api/v10/users/@me \
  -H "Authorization: Bot $DISCORD_BOT_TOKEN" | head -c 50

echo -e "\n\nTesting Slack..."
curl -s -X POST $SLACK_WEBHOOK \
  -H 'Content-type: application/json' \
  -d '{"text":"Credentials verified ✅"}'

echo -e "\n\nAll tests complete!"
```

---

## 📞 Support

**Stuck getting a credential?**

- OpenRouter: https://openrouter.io/docs/api
- LinkedIn: https://docs.microsoft.com/en-us/linkedin/shared/authentication/authentication
- Discord: https://discord.com/developers/docs/getting-started
- Airtable: https://airtable.com/developers/web/api/introduction
- Binance: https://binance-docs.github.io/apidocs/spot/en/
- Supabase: https://supabase.com/docs/guides/getting-started
- Slack: https://api.slack.com/messaging/webhooks

---

## 🎯 Next Steps

1. **Fill in credentials above** ← You are here
2. **Copy to secure location** (password manager, 1Password, Vault)
3. **Follow Deployment Guide** (Step 5: Add secrets to Railway)
4. **Run deployment script** (Steps 6-7)
5. **Verify systems live** (Steps 8-15)

---

*Generated: September 28, 2026 | Security Priority: HIGH*
