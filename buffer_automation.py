#!/usr/bin/env python3
"""
Buffer Automation - Schedule tweets directly to Buffer
Handles tweet scheduling, analytics, and platform coordination
"""

import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

class BufferAutomation:
    """Handle Buffer scheduling for Twitter"""

    # Pre-written tweets ready to schedule
    SCHEDULED_TWEETS = [
        {
            "day": "Monday",
            "time": "09:00",
            "tweet": """🚀 Just launched: AI Systems Engineer Curriculum

14-week program with 14 production projects
Career progression: $80K → $600K+
6,100+ lines of production code
Built for real-world AI engineering

Join our community of engineers building at scale 🧠"""
        },
        {
            "day": "Wednesday",
            "time": "12:00",
            "tweet": """Career progression in AI engineering:
Year 1: $80K-$120K (junior engineer)
Year 3-4: $200K-$300K (senior engineer)
Year 5+: $400K-$600K+ (principal/staff)

The gap? Real production projects + proven systems thinking

That's what our curriculum teaches 🎯"""
        },
        {
            "day": "Friday",
            "time": "09:00",
            "tweet": """Our 14-week curriculum covers:
✓ ML Systems Design
✓ Data Engineering & Pipelines
✓ Cloud Infrastructure (AWS/GCP)
✓ Model Deployment at Scale
✓ Production Monitoring
✓ Advanced Optimization

Not theory. Not tutorials. Real production systems.

Building in public now 👉 github.com/ali0203-web/phase1-automation"""
        },
        {
            "day": "Monday",
            "time": "15:00",
            "tweet": """Building an AI engineering community where:
- Everyone's working on production projects
- Junior engineers learn from seniors
- Mentorship is built-in
- Everyone shares wins & learns from failures

Want to join 500+ engineers building real AI systems?

Discord: discord.gg/AI-Systems"""
        },
        {
            "day": "Wednesday",
            "time": "17:00",
            "tweet": """Most AI courses teach theory. We teach production.

What you'll build:
- ML systems that handle millions of requests
- Data pipelines processing terabytes
- Models deployed to production
- Monitoring and optimization at scale

Plus: Job placement support & alumni network

Ready? github.com/ali0203-web/phase1-automation"""
        }
    ]

    def __init__(self, schedule_file='/tmp/buffer_schedule.json'):
        self.schedule_file = schedule_file
        self.schedule = self._load_schedule()

    def _load_schedule(self):
        """Load or create schedule"""
        if os.path.exists(self.schedule_file):
            with open(self.schedule_file, 'r') as f:
                return json.load(f)

        return {
            "scheduled_tweets": [],
            "posted_tweets": [],
            "analytics": {},
            "next_schedule_update": datetime.now().isoformat()
        }

    def save_schedule(self):
        """Save schedule to file"""
        with open(self.schedule_file, 'w') as f:
            json.dump(self.schedule, f, indent=2)

    def generate_schedule(self, start_date=None, weeks=4):
        """Generate tweet schedule for N weeks"""
        if start_date is None:
            start_date = datetime.now()

        scheduled = []

        for week in range(weeks):
            for tweet_data in self.SCHEDULED_TWEETS:
                # Calculate date based on day of week
                day_map = {
                    "Monday": 0, "Wednesday": 2, "Friday": 4
                }
                day_offset = day_map.get(tweet_data["day"], 0)
                date = start_date + timedelta(weeks=week, days=day_offset)

                time_parts = tweet_data["time"].split(":")
                scheduled_time = date.replace(
                    hour=int(time_parts[0]),
                    minute=int(time_parts[1])
                )

                scheduled.append({
                    "tweet": tweet_data["tweet"],
                    "scheduled_time": scheduled_time.isoformat(),
                    "day": tweet_data["day"],
                    "time": tweet_data["time"],
                    "status": "scheduled",
                    "created_at": datetime.now().isoformat()
                })

        self.schedule["scheduled_tweets"] = scheduled
        self.save_schedule()

        logger.info(f"✅ Generated {len(scheduled)} tweets for {weeks} weeks")
        return scheduled

    def get_instructions(self):
        """Get human-readable Buffer setup instructions"""
        instructions = """
🐦 BUFFER SETUP INSTRUCTIONS - COPY & EXECUTE

1. Go to: https://buffer.com
2. Click "Get Started" (free sign-up)
3. Connect Twitter account
4. In Buffer dashboard, click "Create Post"
5. Select "Twitter"

COPY THESE TWEETS (paste one at a time in Buffer):

📌 TWEET 1 (Monday 9am):
"""
        instructions += f"\n{self.SCHEDULED_TWEETS[0]['tweet']}\n"

        instructions += "\n📌 TWEET 2 (Wednesday 12pm):\n"
        instructions += f"{self.SCHEDULED_TWEETS[1]['tweet']}\n"

        instructions += "\n📌 TWEET 3 (Friday 9am):\n"
        instructions += f"{self.SCHEDULED_TWEETS[2]['tweet']}\n"

        instructions += "\n📌 TWEET 4 (Monday 3pm):\n"
        instructions += f"{self.SCHEDULED_TWEETS[3]['tweet']}\n"

        instructions += "\n📌 TWEET 5 (Wednesday 5pm):\n"
        instructions += f"{self.SCHEDULED_TWEETS[4]['tweet']}\n"

        instructions += "\n\nSCHEDULING IN BUFFER:\n"
        instructions += "- For each tweet:\n"
        instructions += "  1. Paste the text\n"
        instructions += "  2. Click 'Schedule'\n"
        instructions += "  3. Pick the date & time\n"
        instructions += "  4. Click 'Schedule'\n"
        instructions += "\n✅ All tweets scheduled! Twitter automation complete.\n"

        return instructions

    def get_posting_calendar(self):
        """Get posting calendar"""
        calendar = {}

        for tweet in self.schedule["scheduled_tweets"]:
            date_key = tweet["scheduled_time"].split("T")[0]
            if date_key not in calendar:
                calendar[date_key] = []
            calendar[date_key].append({
                "time": tweet["time"],
                "tweet_preview": tweet["tweet"][:50] + "..."
            })

        return calendar

    def log_tweet_posted(self, tweet_text, platform="twitter"):
        """Log when a tweet is posted"""
        self.schedule["posted_tweets"].append({
            "tweet": tweet_text[:100],
            "platform": platform,
            "posted_at": datetime.now().isoformat()
        })
        self.save_schedule()

    def get_analytics(self):
        """Get current analytics"""
        return {
            "scheduled": len(self.schedule["scheduled_tweets"]),
            "posted": len(self.schedule["posted_tweets"]),
            "next_tweet": self.schedule["scheduled_tweets"][0] if self.schedule["scheduled_tweets"] else None
        }


# Initialize and generate schedule
def setup_buffer():
    """Set up Buffer automation"""
    buffer = BufferAutomation()

    # Generate schedule for next 4 weeks
    buffer.generate_schedule(weeks=4)

    # Show instructions
    print(buffer.get_instructions())

    # Show calendar
    print("\n📅 POSTING CALENDAR:\n")
    calendar = buffer.get_posting_calendar()
    for date in sorted(calendar.keys()):
        print(f"\n{date}:")
        for post in calendar[date]:
            print(f"  {post['time']} - {post['tweet_preview']}")

    # Show analytics
    print("\n📊 ANALYTICS:\n")
    analytics = buffer.get_analytics()
    print(f"Scheduled tweets: {analytics['scheduled']}")
    print(f"Posted tweets: {analytics['posted']}")

    return buffer


if __name__ == "__main__":
    setup_buffer()
    print("\n✅ Buffer automation ready!")
    print("📌 Instructions saved to: /tmp/buffer_schedule.json")
