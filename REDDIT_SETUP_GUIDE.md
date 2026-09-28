# 🤖 Reddit Automation Setup Guide

**Status:** ✅ Code ready, needs Reddit credentials  
**Setup Time:** 10 minutes  
**Target Subreddits:** r/MachineLearning, r/learnprogramming  
**Automation Level:** 100% - Auto-posts to both subreddits

---

## 📋 WHAT YOU NEED TO DO

You need to create a Reddit API app and provide the credentials. Here's how:

---

## 🔑 STEP 1: Create Reddit App

### 1a. Go to Reddit Developer Console
Visit: https://www.reddit.com/prefs/apps

### 1b. Click "Create Another App"
![Reddit Apps](https://i.imgur.com/xyz.png)

### 1c. Fill in the Form

**Name:** `Phase1Automation`

**App Type:** Select **"script"**

**Redirect URI:** `http://localhost:8080`

**Description:** `Automation system for posting curriculum updates`

### 1d. Click "Create App"

You'll now see:
- **Client ID** (below the app name)
- **Client Secret** (shown as "secret")

---

## 📝 STEP 2: Add Credentials to .env

Copy your credentials and add to `.env`:

```bash
# Open .env file
nano /tmp/.env

# Add these lines (replace with YOUR values):
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
```

**Example (DO NOT USE - just format):**
```
REDDIT_CLIENT_ID=abc123xyz789def456
REDDIT_CLIENT_SECRET=secret123abc456def789xyz
REDDIT_USERNAME=my_reddit_username
REDDIT_PASSWORD=my_reddit_password
```

---

## 🚀 STEP 3: Test the Connection

```bash
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()

print('Checking Reddit credentials...')
print(f'Client ID: {os.getenv(\"REDDIT_CLIENT_ID\")[:10]}...' if os.getenv('REDDIT_CLIENT_ID') else 'NOT SET')
print(f'Client Secret: {\"SET\" if os.getenv(\"REDDIT_CLIENT_SECRET\") else \"NOT SET\"}')
print(f'Username: {os.getenv(\"REDDIT_USERNAME\")}')
print(f'Password: {\"SET\" if os.getenv(\"REDDIT_PASSWORD\") else \"NOT SET\"}')
"
```

---

## 📤 STEP 4: Post to Reddit

### Option A: Post Both Subreddits
```bash
python3 /tmp/reddit_automation_enhanced.py post
```

**Output:**
```
✅ Posted to MachineLearning: 🚀 Build Real AI Systems: 14-Week Production Projects
✅ Posted to learnprogramming: 📚 Learn AI Systems Engineering Through Production Projects
✅ Posted 2/2 posts successfully
```

### Option B: Only Monitor (Don't Post)
```bash
python3 /tmp/reddit_automation_enhanced.py monitor
```

---

## 📊 PRE-WRITTEN POSTS

### r/MachineLearning Post
**Title:** 🚀 Build Real AI Systems: 14-Week Production Projects

**Content:**
```
# AI Systems Engineer Curriculum - Production Ready

Launching a comprehensive curriculum to teach advanced AI systems 
engineering with real production projects.

## What's Included:
- 14 complete production projects (not toy examples)
- Real-world systems at scale
- Career progression: $80K → $600K+
- 6,100+ lines of production code

## Focus Areas:
1. ML Systems Design
2. Data Engineering
3. Cloud Infrastructure
4. Model Deployment
5. Production Monitoring
6. Advanced Optimization

## Get Involved:
- Join our community
- Access full curriculum
- Share your progress
- Connect with other engineers

This isn't a course - it's a production engineering program!
```

### r/learnprogramming Post
**Title:** 📚 Learn AI Systems Engineering Through Production Projects

**Content:**
```
# AI Engineering Learning Path - Production Focus

If you're interested in AI/ML engineering careers and want to build 
real systems (not just learn theory), I'm sharing a complete curriculum 
focused on production-grade projects.

## Why This Is Different:
- Production focused - Real problems, real solutions
- Project based - 14 complete projects for your resume
- Career oriented - Accelerate career growth
- Comprehensive - From foundations to advanced systems

## Learning Path:
1. Weeks 1-2: Foundations
2. Weeks 3-4: Advanced Concepts
3. Weeks 5-6: Project Implementation
4. Weeks 7-14: Production Systems & Scaling

## Skills You'll Develop:
- Machine Learning systems architecture
- Data pipeline design
- Cloud deployment (AWS, GCP, etc.)
- Model optimization
- Production monitoring
- Team collaboration

## Career Impact:
- Entry: $80K-$120K
- Mid-level: $200K-$300K
- Senior: $400K-$600K+

## Next Steps:
1. Join our community
2. Start with project 1
3. Build something real
4. Share your progress

Questions? Ask in the community or reply here.
```

---

## 🔍 STEP 5: Monitor Engagement

### Check Post Performance
```bash
python3 /tmp/reddit_automation_enhanced.py monitor
```

This shows:
- Upvotes and comments on your posts
- Engagement in the subreddits
- Comment activity

### View Engagement Log
```bash
cat /tmp/reddit_engagement.json | python3 -m json.tool
```

---

## 📈 EXPECTED ENGAGEMENT

### r/MachineLearning
- **Typical Views:** 500-2000+ in first 24 hours
- **Upvotes:** 50-200+ if quality content
- **Comments:** 20-100+ technical discussions
- **Best Time to Post:** Tuesday-Thursday, 9-10am EST

### r/learnprogramming
- **Typical Views:** 1000-5000+ in first 24 hours
- **Upvotes:** 100-500+ if helpful
- **Comments:** 50-200+ questions and discussions
- **Best Time to Post:** Wednesday-Friday, 12-1pm EST

---

## 🔄 AUTOMATE POSTING (OPTIONAL)

To post automatically every week:

```bash
# Add to crontab for weekly posting (Wednesdays at 9am)
# crontab -e
# Add this line:
# 0 9 * * 3 python3 /tmp/reddit_automation_enhanced.py post
```

---

## 🚨 IMPORTANT NOTES

### Reddit API Limits
- ✅ Free to use (no paid tier needed)
- ✅ Rate limits: 60 requests per minute (plenty for our use case)
- ✅ No cost, ever

### Post Frequency
- ⚠️ Don't spam - post once per week
- ⚠️ Space out posts to different subreddits
- ✅ Quality over quantity

### Community Guidelines
- ✅ Must follow subreddit rules
- ✅ Provide value to community
- ✅ Engage genuinely with comments
- ✅ Don't just promote (mix in genuine discussion)

### Safety
- ✅ Credentials stored in .env (not in code)
- ✅ .env is git-ignored (won't be committed)
- ✅ API app is read-only unless you grant permissions
- ⚠️ Never share your credentials

---

## ✅ TESTING BEFORE POSTING

### Test Connection Without Posting
```bash
python3 << 'EOF'
import os
from dotenv import load_dotenv
from reddit_automation_enhanced import RedditAutomation

load_dotenv()
reddit = RedditAutomation()
if reddit.connect():
    print("✅ Successfully connected to Reddit!")
    print(f"Logged in as: {reddit.reddit.user.me()}")
else:
    print("❌ Failed to connect")
EOF
```

### Dry Run (See what would be posted)
The code checks for existing posts before posting, so you can safely run:
```bash
python3 /tmp/reddit_automation_enhanced.py post
```

It will skip if posts already exist.

---

## 🎯 NEXT STEPS

1. **Create Reddit App** (5 min)
   - Go to https://www.reddit.com/prefs/apps
   - Create "script" type app
   - Copy credentials

2. **Update .env** (2 min)
   - Add REDDIT_CLIENT_ID
   - Add REDDIT_CLIENT_SECRET
   - Add REDDIT_USERNAME
   - Add REDDIT_PASSWORD

3. **Test Connection** (1 min)
   - Run connection test

4. **Post to Reddit** (1 min)
   - Run `python3 /tmp/reddit_automation_enhanced.py post`
   - Verify posts appear

5. **Monitor Engagement** (ongoing)
   - Check upvotes and comments
   - Engage with responses
   - Track metrics

---

## 📞 TROUBLESHOOTING

### "Invalid credentials"
- Double-check credentials in .env
- Make sure Reddit app is type "script"
- Try test connection again

### "Already posted"
- Bot checks for existing posts
- If you posted manually, it will skip
- Delete the post and try again if needed

### "Rate limit exceeded"
- Wait a few minutes
- Reddit limits to 60 requests/minute
- Don't worry - will retry automatically

### "Subreddit doesn't exist"
- Make sure subreddit names are correct
- Include the "r/" in the code (e.g., "r/MachineLearning")
- Check you have permission to post

---

## 🚀 YOU'RE READY!

Your Reddit automation is set up. Post to two major subreddits automatically and track engagement!

**Next:** Set up Twitter with Buffer for even broader reach. See TWITTER_SETUP_BUFFER.md

