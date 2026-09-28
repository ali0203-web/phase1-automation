# 🚀 STEP-BY-STEP DEPLOYMENT GUIDE
**All 4 Systems Live in ~10 Minutes**

---

## 📋 PRE-DEPLOYMENT CHECKLIST

Before starting, ensure you have:

- [ ] Railway account (https://railway.app)
- [ ] Binance account with API keys (sandbox)
- [ ] Discord bot created with token
- [ ] LinkedIn OAuth app configured
- [ ] OpenRouter API key
- [ ] Airtable API key
- [ ] Supabase project URL
- [ ] Railway CLI installed (`npm install -g @railway/cli`)
- [ ] Slack webhook URL (for alerts)

---

## STEP 1: Install Railway CLI

```bash
# Install Railway Command Line Interface
npm install -g @railway/cli

# Verify installation
railway --version
```

**Expected output:** `Railway CLI v3.x.x` or later

---

## STEP 2: Authenticate with Railway

```bash
# Login to Railway
railway login

# This will open a browser window to authenticate
# Accept the authorization
# Return to terminal
```

**Expected output:** `✓ Successfully logged in`

---

## STEP 3: Create Railway Project

```bash
# Create new project for automation suite
railway init

# When prompted, enter:
# Project name: automation-suite
# Description: Full automation deployment (4 systems)
```

**Expected output:** `✓ Project created successfully`

---

## STEP 4: Set Up Environment Variables

Copy and save all your API credentials. You'll need:

```bash
# 1. OpenRouter
OPENROUTER_API_KEY=sk-or-[YOUR_KEY]
OPENROUTER_MODEL=claude-3-sonnet-20240229

# 2. LinkedIn
LINKEDIN_CLIENT_ID=[YOUR_CLIENT_ID]
LINKEDIN_CLIENT_SECRET=[YOUR_CLIENT_SECRET]
LINKEDIN_REDIRECT_URI=https://api.domain.com/oauth/linkedin

# 3. Airtable
AIRTABLE_API_KEY=[YOUR_API_KEY]
AIRTABLE_BASE_ID=[YOUR_BASE_ID]

# 4. Discord
DISCORD_BOT_TOKEN=[YOUR_BOT_TOKEN]
DISCORD_CLIENT_ID=[YOUR_CLIENT_ID]
DISCORD_CLIENT_SECRET=[YOUR_CLIENT_SECRET]
DISCORD_GUILD_ID=[YOUR_GUILD_ID]

# 5. Binance
BINANCE_API_KEY=[YOUR_SANDBOX_KEY]
BINANCE_API_SECRET=[YOUR_SANDBOX_SECRET]

# 6. Supabase
SUPABASE_PROJECT_ID=[YOUR_PROJECT_ID]
SUPABASE_API_KEY=[YOUR_API_KEY]
SUPABASE_URL=https://[PROJECT_ID].supabase.co

# 7. Slack
SLACK_WEBHOOK=[YOUR_WEBHOOK_URL]

# 8. Discord Webhook (for monitoring)
DISCORD_WEBHOOK=[YOUR_WEBHOOK_URL]
```

---

## STEP 5: Add Secrets to Railway

```bash
# Add each secret to Railway project
# Format: railway variable add NAME value

# LinkedIn
railway variable add LINKEDIN_CLIENT_ID [YOUR_CLIENT_ID]
railway variable add LINKEDIN_CLIENT_SECRET [YOUR_CLIENT_SECRET]
railway variable add LINKEDIN_REDIRECT_URI https://api.domain.com/oauth/linkedin

# OpenRouter
railway variable add OPENROUTER_API_KEY sk-or-[YOUR_KEY]
railway variable add OPENROUTER_MODEL claude-3-sonnet-20240229

# Airtable
railway variable add AIRTABLE_API_KEY [YOUR_API_KEY]
railway variable add AIRTABLE_BASE_ID [YOUR_BASE_ID]
railway variable add AIRTABLE_TABLE LinkedIn_Content

# Discord
railway variable add DISCORD_BOT_TOKEN [YOUR_BOT_TOKEN]
railway variable add DISCORD_CLIENT_ID [YOUR_CLIENT_ID]
railway variable add DISCORD_CLIENT_SECRET [YOUR_CLIENT_SECRET]
railway variable add DISCORD_GUILD_ID [YOUR_GUILD_ID]

# Binance
railway variable add BINANCE_API_KEY [YOUR_SANDBOX_KEY]
railway variable add BINANCE_API_SECRET [YOUR_SANDBOX_SECRET]
railway variable add BINANCE_TESTNET true

# Supabase
railway variable add SUPABASE_PROJECT_ID [YOUR_PROJECT_ID]
railway variable add SUPABASE_API_KEY [YOUR_API_KEY]
railway variable add SUPABASE_URL https://[PROJECT_ID].supabase.co

# Slack
railway variable add SLACK_WEBHOOK [YOUR_WEBHOOK_URL]
railway variable add DISCORD_WEBHOOK [YOUR_WEBHOOK_URL]

# Database
railway variable add DB_HOST postgres.railway.internal
railway variable add DB_NAME automation_db
railway variable add DB_USER postgres
railway variable add DB_PASSWORD [GENERATE_RANDOM]

# Environment
railway variable add NODE_ENV production
railway variable add PYTHON_ENV production
railway variable add LOG_LEVEL info
```

**Verify all variables added:**
```bash
railway variable ls
```

---

## STEP 6: Deploy Configuration File

```bash
# Copy the railway.yml to your project root
cp /tmp/railway.yml ./railway.yml

# Verify the file
cat railway.yml
```

**Expected:** File contains all 4 service definitions

---

## STEP 7: Deploy All 4 Services

### Option A: Automatic Deployment (Recommended)

```bash
# Deploy using the orchestration script
bash /tmp/DEPLOY_ALL_PARALLEL.sh
```

This will automatically:
1. Build all 4 service images
2. Deploy in parallel
3. Run health checks
4. Verify all endpoints
5. Display final status

**Expected output:**
```
╔════════════════════════════════════════════╗
║    🎯 ALL 4 SYSTEMS DEPLOYED SUCCESSFULLY 🎯  ║
╚════════════════════════════════════════════╝

✓ LinkedIn Automation → LIVE
✓ Discord Bot → LIVE
✓ Trading Agent → LIVE
✓ Supabase Real-time → LIVE
```

### Option B: Manual Deployment

If you prefer step-by-step:

```bash
# 1. Deploy LinkedIn Service
railway service create linkedin-automation
railway environment add production
railway deploy --service linkedin-automation

# 2. Deploy Discord Bot
railway service create discord-bot
railway deploy --service discord-bot

# 3. Deploy Trading Agent
railway service create trading-agent
railway deploy --service trading-agent

# 4. Deploy Supabase Real-time
railway service create supabase-realtime
railway deploy --service supabase-realtime

# Monitor all deployments
railway status
```

---

## STEP 8: Verify Deployment Status

```bash
# Check overall project status
railway status

# Expected output should show all 4 services as "RUNNING"
```

### Individual Service Health Checks

```bash
# LinkedIn Automation
curl https://api.domain.com/linkedin/health

# Discord Bot
curl https://api.domain.com/discord/health

# Trading Agent
curl https://api.domain.com/trading/health

# Supabase Real-time
curl https://[PROJECT].supabase.co/health
```

**Expected response:** `{"status":"ok"}` or HTTP 200

---

## STEP 9: Enable Monitoring & Alerts

```bash
# View logs in real-time
railway logs --service linkedin-automation
railway logs --service discord-bot
railway logs --service trading-agent
railway logs --service supabase-realtime

# Set up alert thresholds (in Railway dashboard)
# 1. Go to https://railway.app
# 2. Select automation-suite project
# 3. Settings → Alerts
# 4. Configure thresholds for:
#    - CPU >70%
#    - Memory >80%
#    - Error rate >5%
```

---

## STEP 10: Configure Custom Domain (Optional)

```bash
# Point your domain to Railway
# In Railway dashboard:
# 1. Project → Settings → Domains
# 2. Add custom domain: api.domain.com
# 3. Configure DNS CNAME record

# After DNS propagates:
railway domain add api.domain.com
```

---

## STEP 11: Verify All Endpoints are Live

```bash
# LinkedIn
curl -X GET https://api.domain.com/linkedin/health

# Discord
curl -X GET https://api.domain.com/discord/health

# Trading
curl -X GET https://api.domain.com/trading/health

# Supabase
curl -X GET https://[PROJECT].supabase.co/health

# All should return 200 OK
```

---

## STEP 12: Test Core Functionality

### LinkedIn Automation
```bash
# Test OAuth flow
curl -X GET https://api.domain.com/oauth/linkedin

# Test webhook
curl -X POST https://api.domain.com/linkedin/webhook \
  -H "Content-Type: application/json" \
  -d '{"test":"true"}'
```

### Discord Bot
```bash
# Verify bot is online
curl -X GET https://api.domain.com/discord/status

# Test command
curl -X POST https://api.domain.com/interactions \
  -H "Content-Type: application/json" \
  -d '{"type":1,"data":{"name":"ping"}}'
```

### Trading Agent
```bash
# Check market connection
curl -X GET https://api.domain.com/trading/health

# Get trading status
curl -X GET https://api.domain.com/trading/status
```

### Supabase Real-time
```bash
# Check database connection
curl -X GET https://[PROJECT].supabase.co/rest/v1/ \
  -H "apikey: [SUPABASE_API_KEY]"

# Verify WebSocket
wscat -c wss://[PROJECT].supabase.co/realtime/v1
```

---

## STEP 13: Configure Slack Notifications

```bash
# Test Slack webhook
curl -X POST $SLACK_WEBHOOK \
  -H 'Content-type: application/json' \
  -d '{
    "text":"Automation Suite Deployment Complete ✅",
    "blocks":[{
      "type":"section",
      "text":{"type":"mrkdwn","text":"*All 4 Systems Live*\n• LinkedIn: ✅\n• Discord: ✅\n• Trading: ✅\n• Supabase: ✅"}
    }]
  }'
```

---

## STEP 14: Set Up Monitoring Dashboard

```bash
# Create monitoring endpoint
curl -X POST https://api.domain.com/dashboard/setup \
  -H "Content-Type: application/json" \
  -d '{
    "services":["linkedin","discord","trading","supabase"],
    "metrics":["cpu","memory","latency","errors"],
    "alerts":["email","slack","discord"]
  }'

# Access dashboard
# Dashboard: https://api.domain.com/dashboard
# Metrics: https://api.domain.com/dashboard/metrics
# Alerts: https://api.domain.com/dashboard/alerts
```

---

## STEP 15: Enable Auto-Rebalancing (Trading Agent)

```bash
# Configure daily rebalancing at 08:00 Dubai time
railway variable add REBALANCE_TIME "08:00"
railway variable add REBALANCE_TIMEZONE "Asia/Dubai"

# Redeploy trading agent
railway redeploy --service trading-agent
```

---

## ✅ DEPLOYMENT COMPLETE

Once all steps are done:

```bash
# Final verification
railway status

# View live logs
railway logs

# Check all endpoints
railway logs --all
```

---

## 🎯 Post-Deployment Checklist

- [ ] All 4 services showing "RUNNING" status
- [ ] All health check endpoints returning 200 OK
- [ ] Slack/Discord alerts working
- [ ] Monitoring dashboard accessible
- [ ] LinkedIn OAuth authenticated
- [ ] Discord bot responding to commands
- [ ] Trading agent generating signals
- [ ] Supabase syncing data in real-time
- [ ] Email notifications configured
- [ ] Database backups enabled

---

## 📊 Expected Timeline

| Step | Duration | Action |
|------|----------|--------|
| 1-5 | 5 min | Setup & credentials |
| 6-7 | 3 min | Deploy services |
| 8-10 | 2 min | Verify status |
| 11-15 | 5 min | Configure monitoring |
| **TOTAL** | **~15 min** | **All systems live** |

---

## 🆘 Troubleshooting

### Service not starting
```bash
# Check logs
railway logs --service [SERVICE_NAME]

# Verify environment variables
railway variable ls

# Redeploy
railway redeploy --service [SERVICE_NAME]
```

### Health check failing
```bash
# Check service status
railway status

# Restart service
railway restart --service [SERVICE_NAME]

# View detailed logs
railway logs --service [SERVICE_NAME] --tail 100
```

### Connection errors
```bash
# Verify secrets are set
railway variable ls

# Test connectivity
curl -v https://api.domain.com/[SERVICE]/health

# Check Railway network
railway network status
```

### Slow deployment
- Clear Railway cache: `railway cache clear`
- Rebuild services: `railway redeploy --all --force`
- Check Railway status: https://status.railway.app

---

## 📞 Support

**After deployment:**
- Monitor: https://api.domain.com/dashboard
- Logs: `railway logs --tail 100`
- Status: `railway status`
- Alerts: Check #automation-alerts in Slack

---

## 🎉 Success Indicators

Your deployment is successful when:

1. ✅ All 4 services show "RUNNING" on Railway dashboard
2. ✅ All health endpoints return 200 OK
3. ✅ Slack receives deployment confirmation alert
4. ✅ Dashboard shows live metrics from all services
5. ✅ Trading agent shows "Ready to trade" status
6. ✅ Discord bot online in guild
7. ✅ LinkedIn OAuth authenticated
8. ✅ Supabase syncing real-time data

**When all are green, you're done! 🚀**

---

*Generated: September 28, 2026 | Authority: Full Deployment Guide*
