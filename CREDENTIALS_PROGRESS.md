# 🎯 CREDENTIALS GATHERING - INTERACTIVE PROGRESS TRACKER
**Follow this step-by-step. Check off each as you complete it.**

---

## 📊 OVERALL PROGRESS

**Status:** 0/10 Credentials Gathered  
**Estimated Time:** ~30 minutes total  
**Current Step:** Getting Started

```
□ OpenRouter       [████░░░░░░] 0%
□ LinkedIn OAuth   [████░░░░░░] 0%
□ Discord Bot      [████░░░░░░] 0%
□ Airtable         [████░░░░░░] 0%
□ Binance Sandbox  [████░░░░░░] 0%
□ Supabase         [████░░░░░░] 0%
□ Slack Webhooks   [████░░░░░░] 0%
□ Discord Webhook  [████░░░░░░] 0%
□ Database Pwd     [████░░░░░░] 0%
□ Verification     [████░░░░░░] 0%
```

---

## STEP 1️⃣ : OPENROUTER (2 minutes)

### ✅ Your Task
- [ ] Go to: https://openrouter.io/keys
- [ ] Sign up with GitHub (if needed)
- [ ] Click "Create Key"
- [ ] Name it: `automation-suite-production`
- [ ] Copy the API key starting with `sk-or-`

### 📝 When Complete, Paste Here:
```
OPENROUTER_API_KEY = sk-or-[PASTE_YOUR_KEY_HERE]
```

### ✓ How to Verify
Open terminal and run:
```bash
curl https://openrouter.io/api/v1/models \
  -H "Authorization: Bearer sk-or-[YOUR_KEY]" | grep -i claude
```

Should show Claude models in response.

### Status
- [ ] **STEP 1 COMPLETE** (move to Step 2)

---

## STEP 2️⃣ : LINKEDIN OAUTH (5 minutes)

### ✅ Your Task
- [ ] Go to: https://www.linkedin.com/developers/apps
- [ ] Click "Create app"
- [ ] App name: `Automation Suite`
- [ ] LinkedIn Page: (select existing or create new)
- [ ] Upload a logo (can be simple image)
- [ ] Accept terms and click "Create app"
- [ ] Go to "Auth" tab
- [ ] Add Redirect URLs:
  - `https://api.domain.com/oauth/linkedin`
  - `https://localhost:3000/oauth/linkedin`
- [ ] Copy "Client ID" and "Client Secret"

### 📝 When Complete, Paste Here:
```
LINKEDIN_CLIENT_ID = [PASTE_HERE]
LINKEDIN_CLIENT_SECRET = [PASTE_HERE]
LINKEDIN_REDIRECT_URI = https://api.domain.com/oauth/linkedin
```

### ✓ How to Verify
Both values should be alphanumeric strings (Client ID longer, Secret even longer).

### Status
- [ ] **STEP 2 COMPLETE** (move to Step 3)

---

## STEP 3️⃣ : DISCORD BOT (5 minutes)

### ✅ Your Task
- [ ] Go to: https://discord.com/developers/applications
- [ ] Click "New Application"
- [ ] Name: `Automation Suite Bot`
- [ ] Accept Terms
- [ ] Click "Bot" in left sidebar
- [ ] Click "Add Bot"
- [ ] Under TOKEN, click "Copy"
- [ ] Save the Bot Token
- [ ] Go to "OAuth2" → "URL Generator"
- [ ] Check "bot" under Scopes
- [ ] Check permissions:
  - `Send Messages`
  - `Read Messages/View Channels`
  - `Manage Messages`
  - `Embed Links`
  - `Read Message History`
- [ ] Copy the generated URL
- [ ] Paste in browser to invite bot to your server
- [ ] Go back to "OAuth2" → "General"
- [ ] Copy "Client ID"

### 📝 When Complete, Paste Here:
```
DISCORD_BOT_TOKEN = [PASTE_BOT_TOKEN_HERE]
DISCORD_CLIENT_ID = [PASTE_CLIENT_ID_HERE]
DISCORD_CLIENT_SECRET = [WILL_FILL_IF_NEEDED]
DISCORD_GUILD_ID = [WE'LL_GET_THIS_NEXT]
```

### 📍 Get Your Guild ID
- [ ] Enable Developer Mode in Discord (Settings → Advanced → Developer Mode)
- [ ] Right-click your server name
- [ ] Click "Copy Server ID"
- [ ] Paste below:

```
DISCORD_GUILD_ID = [PASTE_SERVER_ID_HERE]
```

### ✓ How to Verify
Bot Token should start with `MTA` or `MT`. Should be very long string (100+ chars).

### Status
- [ ] **STEP 3 COMPLETE** (move to Step 4)

---

## STEP 4️⃣ : AIRTABLE (5 minutes)

### ✅ Your Task - Create Base
- [ ] Go to: https://airtable.com/app
- [ ] Click "Add a base"
- [ ] Name: `Automation Suite`
- [ ] Create a table called: `LinkedIn_Content`
- [ ] Add columns (click "+" icon):
  1. `Content` → Type: Long text
  2. `Scheduled_Date` → Type: Date
  3. `Status` → Type: Single select (options: Draft, Scheduled, Published)
  4. `LinkedIn_URL` → Type: URL
  5. `Engagement_Rate` → Type: Number

### ✅ Your Task - Get Credentials
- [ ] Go to: https://airtable.com/account/tokens
- [ ] Click "Create token"
- [ ] Name: `automation-suite-prod`
- [ ] Set scopes: `data.records:read`, `data.records:write`
- [ ] Set workspace access: Your workspace
- [ ] Click "Create token"
- [ ] Copy the token

### 📍 Get Base ID
- [ ] Open your Automation Suite base
- [ ] Look at URL: `https://airtable.com/[BASE_ID]/...`
- [ ] Copy the BASE_ID part

### 📝 When Complete, Paste Here:
```
AIRTABLE_API_KEY = [PASTE_TOKEN_HERE]
AIRTABLE_BASE_ID = [PASTE_BASE_ID_HERE]
AIRTABLE_TABLE = LinkedIn_Content
```

### ✓ How to Verify
Go to terminal and run:
```bash
curl https://api.airtable.com/v0/[BASE_ID] \
  -H "Authorization: Bearer [API_KEY]"
```

Should return your bases (200 OK response).

### Status
- [ ] **STEP 4 COMPLETE** (move to Step 5)

---

## STEP 5️⃣ : BINANCE SANDBOX (3 minutes)

### ⚠️ IMPORTANT: USE TESTNET, NOT PRODUCTION

### ✅ Your Task
- [ ] Go to: https://testnet.binance.vision
- [ ] Sign up with email
- [ ] Verify email
- [ ] Go to: https://testnet.binance.vision/key/api
- [ ] Click "Create API Key"
- [ ] Label: `automation-suite-trading`
- [ ] Restrictions: Spot/Margin Trading
- [ ] Click "Create"
- [ ] Copy "API Key"
- [ ] Copy "Secret Key"

### 📝 When Complete, Paste Here:
```
BINANCE_API_KEY = [PASTE_TESTNET_API_KEY]
BINANCE_API_SECRET = [PASTE_TESTNET_SECRET]
BINANCE_TESTNET = true
BINANCE_BASE_URL = https://testnet.binance.vision
```

### 💰 Check Testnet Balance
- [ ] Log into testnet.binance.vision
- [ ] Go to Wallet
- [ ] Should see $10,000 USDT (free testnet funds)
- [ ] If not, request more from faucet

### ✓ How to Verify
Go to terminal and run:
```bash
curl -X GET "https://testnet.binance.vision/api/v3/account" \
  -H "X-MBX-APIKEY: [API_KEY]"
```

Should return your account balance (~$10,000).

### Status
- [ ] **STEP 5 COMPLETE** (move to Step 6)

---

## STEP 6️⃣ : SUPABASE (5 minutes)

### ✅ Your Task - Create Project
- [ ] Go to: https://supabase.com
- [ ] Click "Start your project"
- [ ] Sign up with GitHub
- [ ] Click "New Project"
- [ ] Organization: (your account)
- [ ] Name: `automation-suite`
- [ ] Database password: (click Generate, save it)
- [ ] Region: (pick closest to you)
- [ ] Click "Create new project"
- [ ] Wait for provisioning (~2 minutes)

### ✅ Your Task - Get Credentials
- [ ] Go to "Project Settings" → "API"
- [ ] Copy "Project URL"
- [ ] Copy "anon public" key (under Service Role Key section)

### 📍 Get Project ID
- [ ] Look at Project URL: `https://[PROJECT_ID].supabase.co`
- [ ] Copy the PROJECT_ID part

### 📝 When Complete, Paste Here:
```
SUPABASE_PROJECT_ID = [PASTE_PROJECT_ID]
SUPABASE_API_KEY = [PASTE_ANON_KEY]
SUPABASE_URL = https://[PROJECT_ID].supabase.co
```

### ✅ Optional: Create Tables
- [ ] In Supabase, go to "SQL Editor"
- [ ] Create new query
- [ ] Copy & paste this:

```sql
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

- [ ] Click "Run"
- [ ] Should see "Success" messages

### ✓ How to Verify
Go to terminal and run:
```bash
curl -X GET "https://[PROJECT_ID].supabase.co/rest/v1/analytics" \
  -H "apikey: [API_KEY]" \
  -H "Authorization: Bearer [API_KEY]"
```

Should return empty array `[]` or error (both mean it's working).

### Status
- [ ] **STEP 6 COMPLETE** (move to Step 7)

---

## STEP 7️⃣ : SLACK WEBHOOKS (3 minutes)

### ✅ Your Task
- [ ] Go to: https://api.slack.com/apps
- [ ] Click "Create New App"
- [ ] Select "From scratch"
- [ ] App name: `Automation Suite`
- [ ] Pick your workspace
- [ ] Click "Create App"
- [ ] Go to "Incoming Webhooks" in left sidebar
- [ ] Click "Add New Webhook to Workspace"
- [ ] Select channel: `#automation-alerts` (or create it)
- [ ] Click "Allow"
- [ ] Copy the Webhook URL

### 📝 When Complete, Paste Here:
```
SLACK_WEBHOOK = https://hooks.slack.com/services/T.../B.../X...
SLACK_CHANNEL = #automation-alerts
```

### ✓ How to Verify
Go to terminal and run:
```bash
curl -X POST https://hooks.slack.com/services/T.../B.../X... \
  -H 'Content-type: application/json' \
  -d '{"text":"Test from credentials setup"}'
```

Should see message appear in your Slack channel.

### Status
- [ ] **STEP 7 COMPLETE** (move to Step 8)

---

## STEP 8️⃣ : DISCORD WEBHOOK (2 minutes)

### ✅ Your Task
- [ ] In Discord, create a channel: `#monitoring`
- [ ] Right-click `#monitoring`
- [ ] Click "Edit Channel"
- [ ] Go to "Integrations" tab
- [ ] Click "Webhooks"
- [ ] Click "New Webhook"
- [ ] Name: `Automation Suite`
- [ ] Click "Copy Webhook URL"

### 📝 When Complete, Paste Here:
```
DISCORD_WEBHOOK = https://discordapp.com/api/webhooks/[ID]/[TOKEN]
```

### ✓ How to Verify
Go to terminal and run:
```bash
curl -X POST https://discordapp.com/api/webhooks/[ID]/[TOKEN] \
  -H 'Content-type: application/json' \
  -d '{"content":"Test from credentials setup"}'
```

Should see message appear in your Discord monitoring channel.

### Status
- [ ] **STEP 8 COMPLETE** (move to Step 9)

---

## STEP 9️⃣ : GENERATE DATABASE PASSWORD (1 minute)

### ✅ Your Task
Generate a secure random password:

```bash
openssl rand -base64 32
```

Copy the output. Example:
```
L4kP9mN2xR8qW5vB3tY7uI6oP1sD4fG8hJ2kL5mN8oP1qR4sT7uV0wX3yZ6aB9cD2e=
```

### 📝 When Complete, Paste Here:
```
DB_PASSWORD = [PASTE_GENERATED_PASSWORD]
```

### Status
- [ ] **STEP 9 COMPLETE** (move to Step 10)

---

## STEP 🔟 : VERIFICATION CHECK (2 minutes)

### ✅ All Credentials Gathered?

Check all completed:
- [ ] OPENROUTER_API_KEY
- [ ] LINKEDIN_CLIENT_ID & SECRET
- [ ] DISCORD_BOT_TOKEN & CLIENT_ID & GUILD_ID
- [ ] AIRTABLE_API_KEY & BASE_ID
- [ ] BINANCE_API_KEY & SECRET
- [ ] SUPABASE_PROJECT_ID & API_KEY
- [ ] SLACK_WEBHOOK
- [ ] DISCORD_WEBHOOK
- [ ] DB_PASSWORD

### 📋 Final Checklist Summary

Copy & fill this out:

```
✓ CREDENTIALS GATHERED - COMPLETE SUMMARY

OPENROUTER:
  API_KEY: sk-or-[✓]

LINKEDIN:
  CLIENT_ID: [✓]
  CLIENT_SECRET: [✓]
  REDIRECT_URI: https://api.domain.com/oauth/linkedin [✓]

DISCORD BOT:
  BOT_TOKEN: [✓]
  CLIENT_ID: [✓]
  GUILD_ID: [✓]

AIRTABLE:
  API_KEY: [✓]
  BASE_ID: [✓]
  TABLE: LinkedIn_Content [✓]

BINANCE:
  API_KEY: [✓]
  API_SECRET: [✓]
  TESTNET: true [✓]

SUPABASE:
  PROJECT_ID: [✓]
  API_KEY: [✓]
  URL: https://[PROJECT_ID].supabase.co [✓]

SLACK:
  WEBHOOK: [✓]
  CHANNEL: #automation-alerts [✓]

DISCORD:
  WEBHOOK: [✓]

DATABASE:
  PASSWORD: [✓]

STATUS: ✅ ALL CREDENTIALS READY FOR DEPLOYMENT
```

### Status
- [ ] **ALL STEPS COMPLETE** → Ready for Deployment Guide Step 5

---

## 🎯 NEXT STEPS

Once all credentials are gathered:

1. ✅ You are here → Credentials gathered
2. → Open Deployment Guide (/tmp/DEPLOYMENT_GUIDE.md)
3. → Follow Step 5: "Add Secrets to Railway"
4. → Paste credentials using the commands provided
5. → Complete Steps 6-7: Deploy all 4 services
6. → Verify systems live (Steps 8-15)

---

## ⏱️ PROGRESS SUMMARY

- **Time to gather credentials:** ~30 minutes
- **Current status:** 0/10 complete
- **Next action:** Start with Step 1 (OpenRouter)

**Let's go! 🚀**

---

*This is YOUR progress tracker. Keep this open as you gather each credential.*
