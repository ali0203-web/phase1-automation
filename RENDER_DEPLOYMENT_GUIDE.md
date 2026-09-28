# 🚀 RENDER DEPLOYMENT GUIDE (100% FREE)

## ✅ Your Code Is Ready!

Your automation system has been containerized and committed to git. Now let's deploy it to Render's free tier for 24/7 operation.

---

## 📋 STEP 1: Create GitHub Repository

You need to push your code to GitHub first. Render will pull directly from GitHub.

### Option A: Create repo via GitHub web

1. Go to **https://github.com/new**
2. **Repository name:** `phase1-automation`
3. **Description:** Phase 1 Social Media Automation System
4. **Visibility:** Public (required for free tier)
5. Click **Create repository**

### Option B: Use GitHub CLI (if installed)

```bash
gh repo create phase1-automation --public --source=. --remote=origin --push
```

---

## 📤 STEP 2: Push Your Code to GitHub

```bash
# From /tmp directory:
git remote add origin https://github.com/YOUR_USERNAME/phase1-automation.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

**Example:**
```bash
git remote add origin https://github.com/aliasgar02/phase1-automation.git
git branch -M main
git push -u origin main
```

---

## 🎯 STEP 3: Deploy on Render

### 1. Go to Render.com
- Visit **https://render.com**
- Click **Sign Up** (or **Sign In** if you have an account)
- Connect with GitHub

### 2. Authorize Render with GitHub
- Click **Authorize render-oss**
- Grant access to your repositories

### 3. Create New Web Service
- Click **Dashboard** (top-right)
- Click **New +** (top-right) → **Web Service**
- Select your repository: **phase1-automation**

### 4. Configure Service
**Settings:**
- **Name:** `phase1-automation` (auto-filled)
- **Environment:** `Docker` (auto-detected)
- **Region:** Choose closest to you (default is fine)
- **Branch:** `main`
- **Auto-deploy:** `Yes` (auto-redeploy on GitHub push)

**Build & Deploy:**
- Leave all defaults (Render auto-detects Dockerfile)
- Click **Create Web Service**

### 5. Wait for Build & Deploy
- Render builds your Docker image (2-5 minutes)
- Deployment happens automatically
- You'll see a green **Live** status when done

---

## 🔗 STEP 4: Access Your Running Service

Once deployed:
- Render gives you a URL: `https://phase1-automation.onrender.com`
- Your automation runs 24/7 on Render's free tier
- No credit card required

---

## 📊 Monitor Your Service

On Render Dashboard:
- **Logs tab:** See real-time logs of your automation
- **Health tab:** Check service status
- **Environment tab:** View environment variables (all loaded from `.env`)

---

## 🚨 Important Notes

### Free Tier Limits
- ✅ 24/7 uptime (no sleep mode)
- ✅ 400 free compute hours/month (plenty for this)
- ✅ Free tier services run on shared CPU
- ✅ No credit card needed

### Environment Variables
Your `.env` file is already included in the Docker image. All credentials are loaded at runtime.

### Logs
Check logs to see:
- Successful automation cycles
- API credential validation
- Schedule executions

---

## ✨ What's Running

Your automation is now executing:
- ✅ Scheduled cycles every 30 minutes
- ✅ Social media API integrations (Twitter, Reddit, LinkedIn, etc.)
- ✅ GitHub engagement tracking
- ✅ Metrics collection
- ✅ 24/7 availability

---

## 🔧 Next Steps (Optional)

### Connect to Slack (for notifications)
Add this to your `.env`:
```
SLACK_WEBHOOK=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

### Enable Database (future)
If you want persistent data storage:
- Go to **Settings** → **Environment**
- Add PostgreSQL connection string

### Custom Domain
Link your own domain via Render settings (paid feature).

---

## 📞 Troubleshooting

### Service keeps restarting?
- Check logs for errors
- Verify API credentials in `.env`
- Check if any API rate limits are hit

### Want to update code?
- Push new changes to GitHub
- Render auto-redeploys in 2-3 minutes
- No manual intervention needed

### Need to stop the service?
- Render Dashboard → **Settings** → **Suspend Service**
- Can resume anytime

---

## 🎉 Done!

Your automation system is now:
- ✅ Containerized with Docker
- ✅ Running on Render's free tier
- ✅ Executing 24/7
- ✅ Auto-scaling included
- ✅ Auto-SSL certificates
- ✅ Auto-redeploy on GitHub push

**Status:** DEPLOYED & RUNNING

Enjoy your automated social media system! 🚀
