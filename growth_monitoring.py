#!/usr/bin/env python3
"""
Growth Monitoring & Analytics Dashboard
Real-time tracking of all platforms and community engagement
"""

import json
import os
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GrowthMonitor:
    """Monitor and track growth across all platforms"""

    def __init__(self, metrics_file='/tmp/growth_metrics.json'):
        self.metrics_file = metrics_file
        self.data = self._load_metrics()

    def _load_metrics(self):
        """Load metrics"""
        if os.path.exists(self.metrics_file):
            with open(self.metrics_file, 'r') as f:
                return json.load(f)

        return {
            "started_at": datetime.now().isoformat(),
            "platforms": {
                "discord": {"members": 0, "messages": 0, "active_users": 0},
                "twitter": {"followers": 0, "impressions": 0, "engagements": 0},
                "reddit": {"karma": 0, "posts": 0, "comments": 0},
                "github": {"stars": 0, "discussions": 0, "forks": 0},
                "youtube": {"subscribers": 0, "views": 0, "watch_time": 0},
                "linkedin": {"followers": 0, "posts": 0, "engagements": 0},
                "email": {"subscribers": 0, "open_rate": 0},
                "hashnode": {"followers": 0, "articles": 0, "views": 0},
                "tiktok": {"followers": 0, "views": 0, "shares": 0},
                "bluesky": {"followers": 0, "posts": 0}
            },
            "daily_metrics": {},
            "growth_trends": {},
            "engagement_score": 0,
            "community_health": "starting",
            "last_updated": datetime.now().isoformat()
        }

    def save_metrics(self):
        """Save metrics"""
        self.data["last_updated"] = datetime.now().isoformat()
        with open(self.metrics_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def update_platform(self, platform, metrics_dict):
        """Update metrics for a platform"""
        if platform in self.data["platforms"]:
            self.data["platforms"][platform].update(metrics_dict)
            self.save_metrics()
            logger.info(f"✅ Updated {platform}: {metrics_dict}")

    def calculate_total_reach(self):
        """Calculate total reach across all platforms"""
        total = 0
        for platform, metrics in self.data["platforms"].items():
            # Calculate based on followers and engagement
            followers = metrics.get("followers", 0) or metrics.get("members", 0) or metrics.get("subscribers", 0) or 0
            engagement = metrics.get("engagements", 0) or metrics.get("comments", 0) or 0

            total += followers + engagement

        return total

    def calculate_engagement_rate(self):
        """Calculate overall engagement rate"""
        total_reach = self.calculate_total_reach()
        if total_reach == 0:
            return 0

        total_engagements = 0
        for platform, metrics in self.data["platforms"].items():
            total_engagements += metrics.get("engagements", 0) or metrics.get("comments", 0) or 0

        rate = (total_engagements / total_reach * 100) if total_reach > 0 else 0
        return min(100, rate)

    def calculate_community_health(self):
        """Calculate community health score"""
        total_reach = self.calculate_total_reach()
        engagement_rate = self.calculate_engagement_rate()

        # Health based on reach and engagement
        if total_reach > 10000 and engagement_rate > 5:
            health = "excellent"
        elif total_reach > 5000 and engagement_rate > 3:
            health = "good"
        elif total_reach > 1000 and engagement_rate > 1:
            health = "growing"
        else:
            health = "early_stage"

        self.data["community_health"] = health
        self.save_metrics()
        return health

    def get_daily_summary(self):
        """Get daily summary"""
        today = datetime.now().date().isoformat()

        summary = {
            "date": today,
            "total_reach": self.calculate_total_reach(),
            "engagement_rate": round(self.calculate_engagement_rate(), 2),
            "community_health": self.calculate_community_health(),
            "platforms": self.data["platforms"],
            "timestamp": datetime.now().isoformat()
        }

        # Store in daily metrics
        self.data["daily_metrics"][today] = summary
        self.save_metrics()

        return summary

    def get_growth_report(self, days=7):
        """Get growth report for N days"""
        daily_summaries = list(self.data["daily_metrics"].values())[-days:]

        if len(daily_summaries) < 2:
            return {"status": "insufficient_data"}

        first_day = daily_summaries[0]
        last_day = daily_summaries[-1]

        growth = {
            "period_days": days,
            "start_date": first_day.get("date"),
            "end_date": last_day.get("date"),
            "total_reach_start": first_day.get("total_reach", 0),
            "total_reach_end": last_day.get("total_reach", 0),
            "reach_growth": last_day.get("total_reach", 0) - first_day.get("total_reach", 0),
            "engagement_rate_start": first_day.get("engagement_rate", 0),
            "engagement_rate_end": last_day.get("engagement_rate", 0),
            "health_trajectory": last_day.get("community_health")
        }

        return growth

    def print_dashboard(self):
        """Print a formatted dashboard"""
        print("\n" + "="*60)
        print("📊 GROWTH MONITORING DASHBOARD")
        print("="*60)

        summary = self.get_daily_summary()

        print(f"\n📈 Total Reach: {summary['total_reach']:,}")
        print(f"💬 Engagement Rate: {summary['engagement_rate']}%")
        print(f"🏥 Community Health: {summary['community_health'].upper()}")

        print("\n📱 Platform Breakdown:")
        for platform, metrics in summary["platforms"].items():
            reach = metrics.get("followers") or metrics.get("members") or metrics.get("subscribers") or 0
            engagement = metrics.get("engagements") or metrics.get("comments") or 0
            print(f"  {platform:12} | Reach: {reach:6,} | Engagement: {engagement:6,}")

        print("\n" + "="*60 + "\n")


class EngagementAutomation:
    """Automate community engagement"""

    ENGAGEMENT_TEMPLATES = {
        "welcome_discord": """Welcome to the AI Systems Engineer Community! 🎉

👋 Hi {name}! Excited to have you here.

**Quick Start:**
1. Introduce yourself in #introductions
2. Check #resources for curriculum details
3. Ask questions in #questions
4. Share your progress in #wins

Let's build amazing AI systems together! 🚀""",

        "answer_curriculum": """Great question! 📚

Our 14-week curriculum covers:
✓ ML Systems Design
✓ Data Engineering & Pipelines
✓ Cloud Infrastructure (AWS/GCP)
✓ Model Deployment at Scale
✓ Production Monitoring
✓ Advanced Optimization

Real production projects, real career progression ($80K → $600K+).

Check #resources for the full curriculum. Let me know if you have other questions!""",

        "answer_career": """Excellent question! 💼

**Career Progression in AI Engineering:**
- Year 1: $80K-$120K (junior engineer)
- Year 3-4: $200K-$300K (senior engineer)
- Year 5+: $400K-$600K+ (principal/staff)

The gap? **Real production experience.** That's what our curriculum teaches.

Want to accelerate your career? Start with Project 1 in the curriculum.
Discord: [invite link]""",

        "highlight_project": """🎯 Project Highlight: {project_name}

{description}

**Key Learning:** {learning}

**Skills:** {skills}

**What you build:** {deliverable}

Students completing this project see significant career acceleration.
Next project: {next_project}""",

        "weekly_digest": """📰 Weekly Community Update

**This Week:**
- {stat1}
- {stat2}
- {stat3}

**Top Questions Answered:**
1. {question1}
2. {question2}

**Student Wins:**
🎉 {win1}
🎉 {win2}

**Coming Next:**
- {event1}
- {event2}

Join us! Discord: [link]"""
    }

    def __init__(self, engagement_log='/tmp/engagement_log.json'):
        self.log_file = engagement_log
        self.log = self._load_log()

    def _load_log(self):
        """Load engagement log"""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return json.load(f)

        return {"engagements": [], "total_interactions": 0}

    def save_log(self):
        """Save engagement log"""
        with open(self.log_file, 'w') as f:
            json.dump(self.log, f, indent=2)

    def log_engagement(self, engagement_type, user, platform, content_preview):
        """Log an engagement"""
        engagement = {
            "type": engagement_type,
            "user": user,
            "platform": platform,
            "content": content_preview[:100],
            "timestamp": datetime.now().isoformat()
        }

        self.log["engagements"].append(engagement)
        self.log["total_interactions"] += 1
        self.save_log()

        logger.info(f"✅ Logged {engagement_type} from {user} on {platform}")

    def get_response_template(self, question_type):
        """Get appropriate response template"""
        if "curriculum" in question_type.lower():
            return self.ENGAGEMENT_TEMPLATES["answer_curriculum"]
        elif "career" in question_type.lower():
            return self.ENGAGEMENT_TEMPLATES["answer_career"]
        else:
            return "Thanks for the question! Let me help you with that."


if __name__ == "__main__":
    # Initialize monitors
    monitor = GrowthMonitor()
    engagement = EngagementAutomation()

    # Show dashboard
    monitor.print_dashboard()

    # Get growth report
    print("📊 Growth Report (Last 7 Days):")
    report = monitor.get_growth_report(7)
    print(json.dumps(report, indent=2))

    print("\n✅ Monitoring system ready!")
    print("📌 Data saved to: /tmp/growth_metrics.json")
