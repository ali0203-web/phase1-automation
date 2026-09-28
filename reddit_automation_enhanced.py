#!/usr/bin/env python3
"""
Reddit Automation Enhanced - Post, Monitor, and Track Engagement
Posts to r/MachineLearning and r/learnprogramming automatically
"""

import praw
import json
import os
from datetime import datetime
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class RedditAutomation:
    """Handle Reddit automation for multi-subreddit posting and monitoring"""

    def __init__(self):
        self.client_id = os.getenv('REDDIT_CLIENT_ID')
        self.client_secret = os.getenv('REDDIT_CLIENT_SECRET')
        self.username = os.getenv('REDDIT_USERNAME')
        self.password = os.getenv('REDDIT_PASSWORD')
        self.user_agent = 'Phase1-Automation/1.0 by ali0203-web'

        self.reddit = None
        self.engagement_log_file = '/tmp/reddit_engagement.json'
        self._init_engagement_log()

    def connect(self):
        """Connect to Reddit API"""
        try:
            if not all([self.client_id, self.client_secret, self.username, self.password]):
                logger.error("Missing Reddit credentials in environment")
                return False

            self.reddit = praw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent,
                username=self.username,
                password=self.password
            )

            # Test connection
            self.reddit.user.me()
            logger.info("✅ Successfully connected to Reddit")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to connect to Reddit: {e}")
            return False

    def _init_engagement_log(self):
        """Initialize engagement log"""
        if not os.path.exists(self.engagement_log_file):
            data = {
                "started_at": datetime.now().isoformat(),
                "posts": [],
                "total_karma_gained": 0,
                "top_posts": [],
                "subreddit_stats": {}
            }
            with open(self.engagement_log_file, 'w') as f:
                json.dump(data, f, indent=2)

    def post_to_subreddit(self, subreddit_name, title, content):
        """Post to a specific subreddit"""
        if not self.reddit:
            logger.error("Not connected to Reddit")
            return False

        try:
            subreddit = self.reddit.subreddit(subreddit_name)

            # Check if already posted
            for submission in subreddit.new(limit=50):
                if submission.title.lower() == title.lower():
                    logger.info(f"Post already exists in {subreddit_name}: {title}")
                    return False

            # Post the submission
            submission = subreddit.submit(title=title, selftext=content)
            logger.info(f"✅ Posted to {subreddit_name}: {title}")

            # Log activity
            self._log_post(subreddit_name, title, submission.url)
            return True
        except Exception as e:
            logger.error(f"❌ Failed to post to {subreddit_name}: {e}")
            return False

    def monitor_subreddit(self, subreddit_name, limit=10):
        """Monitor a subreddit for engagement"""
        if not self.reddit:
            logger.error("Not connected to Reddit")
            return []

        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            engagement_data = []

            for submission in subreddit.new(limit=limit):
                data = {
                    "title": submission.title,
                    "score": submission.score,
                    "comments": submission.num_comments,
                    "url": submission.url,
                    "created_at": datetime.fromtimestamp(submission.created_utc).isoformat(),
                    "ratio": submission.upvote_ratio
                }
                engagement_data.append(data)

            logger.info(f"Monitored {len(engagement_data)} posts in {subreddit_name}")
            return engagement_data
        except Exception as e:
            logger.error(f"Failed to monitor {subreddit_name}: {e}")
            return []

    def track_comment_activity(self, subreddit_name, limit=20):
        """Track comments on posts in subreddit"""
        if not self.reddit:
            return []

        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            comments_data = []

            for submission in subreddit.new(limit=limit):
                submission.comments.replace_more(limit=0)
                for comment in submission.comments.list()[:5]:
                    comments_data.append({
                        "post_title": submission.title,
                        "comment_author": comment.author.name if comment.author else "[deleted]",
                        "comment_score": comment.score,
                        "comment_text": comment.body[:100]
                    })

            logger.info(f"Tracked {len(comments_data)} comments in {subreddit_name}")
            return comments_data
        except Exception as e:
            logger.error(f"Failed to track comments: {e}")
            return []

    def _log_post(self, subreddit, title, url):
        """Log post to engagement file"""
        try:
            with open(self.engagement_log_file, 'r') as f:
                data = json.load(f)

            post_entry = {
                "timestamp": datetime.now().isoformat(),
                "subreddit": subreddit,
                "title": title,
                "url": url
            }

            data["posts"].append(post_entry)

            # Update subreddit stats
            if subreddit not in data["subreddit_stats"]:
                data["subreddit_stats"][subreddit] = {"posts": 0, "karma": 0}
            data["subreddit_stats"][subreddit]["posts"] += 1

            with open(self.engagement_log_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to log post: {e}")

    def get_engagement_stats(self):
        """Get engagement statistics"""
        if not os.path.exists(self.engagement_log_file):
            return {}

        with open(self.engagement_log_file, 'r') as f:
            return json.load(f)


# Pre-written posts ready to post
REDDIT_POSTS = {
    "r/MachineLearning": {
        "title": "🚀 Build Real AI Systems: 14-Week Production Projects",
        "content": """
# AI Systems Engineer Curriculum - Production Ready

Launching a comprehensive curriculum to teach advanced AI systems engineering with real production projects.

## What's Included:
- **14 complete production projects** (not toy examples)
- **Real-world systems** at scale
- **Career progression**: $80K → $600K+
- **6,100+ lines** of production code
- **Advanced topics**: ML systems, data pipelines, deployment, scaling

## Focus Areas:
1. ML Systems Design
2. Data Engineering
3. Cloud Infrastructure
4. Model Deployment
5. Production Monitoring
6. Advanced Optimization

## Current Status:
✅ All projects built and tested
✅ Comprehensive curriculum complete
✅ Community launching now

## Get Involved:
- Join our community for support
- Access full curriculum
- Share your progress
- Connect with other engineers

This isn't a course - it's a production engineering program designed to get you from junior engineer to senior/principal level.

Feedback and questions welcome! 🚀
        """
    },
    "r/learnprogramming": {
        "title": "📚 Learn AI Systems Engineering Through Production Projects",
        "content": """
# AI Engineering Learning Path - Production Focus

If you're interested in AI/ML engineering careers and want to build real systems (not just learn theory), I'm sharing a complete curriculum focused on production-grade projects.

## Why This Is Different:
- **Production focused** - Real problems, real solutions
- **Project based** - 14 complete projects you can put on resume
- **Career oriented** - Designed to accelerate career growth
- **Comprehensive** - From foundations to advanced systems

## Learning Path:
1. **Weeks 1-2**: Foundations
2. **Weeks 3-4**: Advanced Concepts
3. **Weeks 5-6**: Project Implementation
4. **Weeks 7-14**: Production Systems & Scaling

## Skills You'll Develop:
- Machine Learning systems architecture
- Data pipeline design
- Cloud deployment (AWS, GCP, etc.)
- Model optimization
- Production monitoring
- Team collaboration

## Career Impact:
Students typically see:
- **Entry**: $80K-$120K
- **Mid-level**: $200K-$300K
- **Senior**: $400K-$600K+

## Next Steps:
1. Join our community (link in comments)
2. Start with project 1
3. Build something real
4. Share your progress

Questions? Ask in the community or reply here.

Good luck! 🚀
        """
    }
}


def post_to_reddit():
    """Post all pre-written posts to Reddit"""
    reddit = RedditAutomation()

    if not reddit.connect():
        logger.error("Could not connect to Reddit. Check credentials in .env")
        return False

    success_count = 0
    for subreddit, post_data in REDDIT_POSTS.items():
        if reddit.post_to_subreddit(
            subreddit.replace("r/", ""),
            post_data["title"],
            post_data["content"]
        ):
            success_count += 1

    logger.info(f"✅ Posted {success_count}/{len(REDDIT_POSTS)} posts successfully")
    return success_count == len(REDDIT_POSTS)


def monitor_reddit():
    """Monitor Reddit engagement"""
    reddit = RedditAutomation()

    if not reddit.connect():
        return False

    for subreddit in ["MachineLearning", "learnprogramming"]:
        logger.info(f"\n📊 Monitoring r/{subreddit}...")

        # Monitor engagement
        engagement = reddit.monitor_subreddit(subreddit)
        if engagement:
            logger.info(f"Top posts: {engagement[0]['title'][:50]}...")

        # Track comments
        comments = reddit.track_comment_activity(subreddit)
        logger.info(f"Found {len(comments)} recent comments")

    # Get stats
    stats = reddit.get_engagement_stats()
    logger.info(f"\nStats: {json.dumps(stats, indent=2)}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "post":
            post_to_reddit()
        elif sys.argv[1] == "monitor":
            monitor_reddit()
    else:
        print("Usage: python3 reddit_automation_enhanced.py [post|monitor]")
        print("  post    - Post all pre-written posts to Reddit")
        print("  monitor - Monitor subreddit engagement")
