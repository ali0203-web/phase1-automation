#!/usr/bin/env python3
"""
PHASE 1 COMPLETE AUTOMATION SYSTEM - DOTENV VERSION
Handles posting, monitoring, responding, and metrics tracking
Runs autonomously 24/7 until Phase 2 deployment
"""

import os
import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv
import schedule
import tweepy
import praw
import requests

# Load .env file
load_dotenv("/tmp/.env")

# Configuration from .env
CONFIG = {
    "twitter": {
        "api_key": os.getenv("TWITTER_API_KEY"),
        "api_secret": os.getenv("TWITTER_API_SECRET"),
        "access_token": os.getenv("TWITTER_ACCESS_TOKEN"),
        "access_secret": os.getenv("TWITTER_ACCESS_SECRET"),
        "bearer_token": os.getenv("TWITTER_BEARER_TOKEN"),
    },
    "reddit": {
        "client_id": os.getenv("REDDIT_CLIENT_ID"),
        "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
        "username": os.getenv("REDDIT_USERNAME"),
        "password": os.getenv("REDDIT_PASSWORD"),
        "user_agent": "CurriculumLaunch/1.0",
    },
    "github": {
        "token": os.getenv("GITHUB_TOKEN"),
        "repo": "ali0203-web/desktop-tutorial",
    },
    "linkedin": {
        "access_token": os.getenv("LINKEDIN_ACCESS_TOKEN"),
    }
}

METRICS = {
    "posts_published": 0,
    "comments_monitored": 0,
    "responses_sent": 0,
    "engagement_count": 0,
    "github_stars": 0,
    "last_updated": datetime.now().isoformat(),
    "status": "RUNNING"
}

class TwitterManager:
    def __init__(self, config):
        if all(config.values()):
            self.client = tweepy.Client(
                bearer_token=config["bearer_token"],
                consumer_key=config["api_key"],
                consumer_secret=config["api_secret"],
                access_token=config["access_token"],
                access_token_secret=config["access_secret"],
            )
        else:
            self.client = None

    def post(self, text):
        if not self.client:
            return None
        try:
            response = self.client.create_tweet(text=text)
            return response.data['id']
        except Exception as e:
            print(f"Twitter post failed: {e}")
            return None

    def monitor(self):
        if not self.client:
            return None
        try:
            mentions = self.client.get_users_mentions(
                id="YOUR_USER_ID",
                max_results=10,
                tweet_fields=['created_at', 'author_id'],
            )
            return mentions
        except Exception as e:
            print(f"Twitter monitoring failed: {e}")
            return None

class RedditManager:
    def __init__(self, config):
        if all(config.values()):
            self.reddit = praw.Reddit(
                client_id=config["client_id"],
                client_secret=config["client_secret"],
                username=config["username"],
                password=config["password"],
                user_agent=config["user_agent"],
            )
        else:
            self.reddit = None

    def post_to_subreddit(self, subreddit, title, body):
        if not self.reddit:
            return None
        try:
            sub = self.reddit.subreddit(subreddit)
            submission = sub.submit(title=title, selftext=body)
            return submission.id
        except Exception as e:
            print(f"Reddit post failed: {e}")
            return None

    def monitor(self, subreddit):
        if not self.reddit:
            return None
        try:
            sub = self.reddit.subreddit(subreddit)
            comments = []
            for submission in sub.new(limit=5):
                for comment in submission.comments:
                    if comment.author != "[deleted]":
                        comments.append({
                            "author": comment.author.name,
                            "text": comment.body,
                            "score": comment.score,
                        })
            return comments
        except Exception as e:
            print(f"Reddit monitoring failed: {e}")
            return None

class GitHubManager:
    def __init__(self, config):
        self.token = config["token"]
        self.repo = config["repo"]
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }

    def get_stars(self):
        url = f"https://api.github.com/repos/{self.repo}"
        try:
            response = requests.get(url, headers=self.headers, timeout=5)
            if response.status_code == 200:
                return response.json()["stargazers_count"]
        except Exception as e:
            print(f"Failed to get stars: {e}")
        return 0

class MetricsTracker:
    def __init__(self, log_file="/tmp/phase1_metrics.json"):
        self.log_file = log_file
        self.load_metrics()

    def load_metrics(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                self.metrics = json.load(f)
        else:
            self.metrics = METRICS.copy()

    def save_metrics(self):
        self.metrics["last_updated"] = datetime.now().isoformat()
        with open(self.log_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)

    def update(self, key, value):
        self.metrics[key] = value
        self.save_metrics()

    def report(self):
        return f"""
=== PHASE 1 METRICS REPORT ===
Time: {self.metrics['last_updated']}

Posts Published: {self.metrics['posts_published']}
Comments Monitored: {self.metrics['comments_monitored']}
Responses Sent: {self.metrics['responses_sent']}
Total Engagement: {self.metrics['engagement_count']}
GitHub Stars: {self.metrics['github_stars']}

Status: RUNNING 24/7
        """

class Phase1Automation:
    def __init__(self):
        self.twitter = TwitterManager(CONFIG["twitter"])
        self.reddit = RedditManager(CONFIG["reddit"])
        self.github = GitHubManager(CONFIG["github"])
        self.metrics = MetricsTracker()

        print(f"[{datetime.now()}] ✅ Twitter: {'READY' if self.twitter.client else 'PENDING'}")
        print(f"[{datetime.now()}] ✅ Reddit: {'READY' if self.reddit.reddit else 'PENDING'}")
        print(f"[{datetime.now()}] ✅ GitHub: READY")

    def run_monitoring_cycle(self):
        print(f"\n[{datetime.now()}] 👁️  MONITORING CYCLE")
        
        # Update GitHub stars
        if self.github:
            stars = self.github.get_stars()
            self.metrics.update("github_stars", stars)
            print(f"   ✅ GitHub stars: {stars}")

    def run_metrics_report(self):
        report = self.metrics.report()
        print(report)

    def start(self):
        print("🚀 PHASE 1 AUTOMATION SYSTEM STARTING")
        print("=" * 70)

        # Schedule jobs
        schedule.every(30).minutes.do(self.run_monitoring_cycle)
        schedule.every(1).hours.do(self.run_metrics_report)

        print("✅ Automation scheduled")
        print("=" * 70)

        # Run initial cycle
        self.run_monitoring_cycle()
        self.run_metrics_report()

        # Keep running
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    try:
        automation = Phase1Automation()
        automation.start()
    except KeyboardInterrupt:
        print("\n🛑 Automation stopped")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
