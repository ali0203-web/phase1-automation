#!/usr/bin/env python3
"""
Phase 2 Infrastructure - CMS, Advanced Analytics, Community Manager, Email Automation
Handles content management, detailed analytics, and community nurturing
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

class ContentManagementSystem:
    """Manage content across all platforms"""

    def __init__(self, content_file='/tmp/cms_content.json'):
        self.content_file = content_file
        self.content = self._load_content()

    def _load_content(self):
        """Load content from file"""
        if os.path.exists(self.content_file):
            with open(self.content_file, 'r') as f:
                return json.load(f)

        return {
            "blog_posts": [],
            "video_scripts": [],
            "social_posts": [],
            "email_templates": [],
            "project_descriptions": []
        }

    def save_content(self):
        """Save content to file"""
        with open(self.content_file, 'w') as f:
            json.dump(self.content, f, indent=2)

    def add_blog_post(self, title, content, category, tags):
        """Add blog post to CMS"""
        post = {
            "id": len(self.content["blog_posts"]),
            "title": title,
            "content": content,
            "category": category,
            "tags": tags,
            "created_at": datetime.now().isoformat(),
            "status": "draft"
        }
        self.content["blog_posts"].append(post)
        self.save_content()
        return post

    def add_video_script(self, title, script, project, duration):
        """Add video script"""
        video = {
            "id": len(self.content["video_scripts"]),
            "title": title,
            "script": script,
            "project": project,
            "duration_minutes": duration,
            "created_at": datetime.now().isoformat(),
            "status": "draft"
        }
        self.content["video_scripts"].append(video)
        self.save_content()
        return video

    def add_social_post(self, platform, content, schedule_time, images=None):
        """Add social media post"""
        post = {
            "id": len(self.content["social_posts"]),
            "platform": platform,
            "content": content,
            "images": images or [],
            "scheduled_time": schedule_time,
            "created_at": datetime.now().isoformat(),
            "status": "scheduled"
        }
        self.content["social_posts"].append(post)
        self.save_content()
        return post

    def get_content_calendar(self, days=7):
        """Get content calendar for next N days"""
        calendar = defaultdict(list)
        today = datetime.now().date()

        for post in self.content["social_posts"]:
            scheduled = datetime.fromisoformat(post["scheduled_time"]).date()
            days_ahead = (scheduled - today).days

            if 0 <= days_ahead < days:
                calendar[str(scheduled)].append(post)

        return dict(calendar)


class AdvancedAnalytics:
    """Advanced analytics and reporting"""

    def __init__(self, analytics_file='/tmp/advanced_analytics.json'):
        self.analytics_file = analytics_file
        self.data = self._load_analytics()

    def _load_analytics(self):
        """Load analytics data"""
        if os.path.exists(self.analytics_file):
            with open(self.analytics_file, 'r') as f:
                return json.load(f)

        return {
            "daily_metrics": {},
            "user_segments": {},
            "trends": {},
            "cohorts": {}
        }

    def save_analytics(self):
        """Save analytics"""
        with open(self.analytics_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def record_daily_metrics(self, platform, metrics_dict):
        """Record daily metrics"""
        today = datetime.now().date().isoformat()

        if today not in self.data["daily_metrics"]:
            self.data["daily_metrics"][today] = {}

        self.data["daily_metrics"][today][platform] = metrics_dict
        self.save_analytics()

    def segment_users(self, user_id, segment_type, characteristics):
        """Segment users for targeting"""
        if segment_type not in self.data["user_segments"]:
            self.data["user_segments"][segment_type] = []

        self.data["user_segments"][segment_type].append({
            "user_id": user_id,
            "characteristics": characteristics,
            "joined_at": datetime.now().isoformat()
        })
        self.save_analytics()

    def identify_trends(self, topic, data_points):
        """Identify trends in data"""
        if topic not in self.data["trends"]:
            self.data["trends"][topic] = []

        trend = {
            "data": data_points,
            "direction": self._calculate_direction(data_points),
            "strength": self._calculate_strength(data_points),
            "identified_at": datetime.now().isoformat()
        }

        self.data["trends"][topic].append(trend)
        self.save_analytics()
        return trend

    def _calculate_direction(self, data_points):
        """Calculate trend direction"""
        if len(data_points) < 2:
            return "unknown"

        if data_points[-1] > data_points[0]:
            return "upward"
        elif data_points[-1] < data_points[0]:
            return "downward"
        else:
            return "flat"

    def _calculate_strength(self, data_points):
        """Calculate trend strength"""
        if len(data_points) < 2:
            return 0

        change = abs(data_points[-1] - data_points[0])
        avg = sum(data_points) / len(data_points)

        if avg == 0:
            return 0

        return min(10, (change / avg) * 5)

    def get_cohort_analysis(self, cohort_date):
        """Analyze cohort performance"""
        cohort_key = cohort_date.isoformat()

        return {
            "cohort_date": cohort_key,
            "retention": self._calculate_retention(cohort_key),
            "engagement": self._calculate_engagement(cohort_key),
            "growth": self._calculate_growth(cohort_key)
        }

    def _calculate_retention(self, cohort_key):
        """Calculate retention rate"""
        return 0.85  # Placeholder

    def _calculate_engagement(self, cohort_key):
        """Calculate engagement rate"""
        return 0.72  # Placeholder

    def _calculate_growth(self, cohort_key):
        """Calculate growth rate"""
        return 0.15  # Placeholder


class CommunityManager:
    """Manage community engagement and member relationships"""

    def __init__(self, members_file='/tmp/community_members.json'):
        self.members_file = members_file
        self.members = self._load_members()

    def _load_members(self):
        """Load community members"""
        if os.path.exists(self.members_file):
            with open(self.members_file, 'r') as f:
                return json.load(f)

        return {
            "early_adopters": [],
            "active_members": [],
            "contributors": [],
            "mentors": []
        }

    def save_members(self):
        """Save members data"""
        with open(self.members_file, 'w') as f:
            json.dump(self.members, f, indent=2)

    def identify_early_adopters(self, user, engagement_score):
        """Identify and track early adopters"""
        if engagement_score > 8:
            early_adopter = {
                "user_id": user,
                "engagement_score": engagement_score,
                "identified_at": datetime.now().isoformat(),
                "referral_count": 0
            }
            self.members["early_adopters"].append(early_adopter)
            self.save_members()
            return early_adopter

    def track_engagement_history(self, user, action, platform):
        """Track member engagement history"""
        for member_type in self.members.values():
            for member in member_type:
                if member.get("user_id") == user:
                    if "engagement_history" not in member:
                        member["engagement_history"] = []

                    member["engagement_history"].append({
                        "action": action,
                        "platform": platform,
                        "timestamp": datetime.now().isoformat()
                    })

                    self.save_members()
                    return True

        return False

    def promote_to_contributor(self, user):
        """Promote active member to contributor"""
        for member in self.members["active_members"]:
            if member.get("user_id") == user:
                self.members["contributors"].append(member)
                self.members["active_members"].remove(member)
                self.save_members()
                return True
        return False

    def promote_to_mentor(self, user):
        """Promote contributor to mentor"""
        for member in self.members["contributors"]:
            if member.get("user_id") == user:
                self.members["mentors"].append(member)
                self.members["contributors"].remove(member)
                self.save_members()
                return True
        return False

    def get_community_overview(self):
        """Get overview of community structure"""
        return {
            "early_adopters": len(self.members["early_adopters"]),
            "active_members": len(self.members["active_members"]),
            "contributors": len(self.members["contributors"]),
            "mentors": len(self.members["mentors"]),
            "total_members": sum(len(v) for v in self.members.values())
        }


class EmailAutomationNursery:
    """Manage email campaigns and subscriber nurturing"""

    def __init__(self, subscribers_file='/tmp/email_subscribers.json'):
        self.subscribers_file = subscribers_file
        self.subscribers = self._load_subscribers()

    def _load_subscribers(self):
        """Load email subscribers"""
        if os.path.exists(self.subscribers_file):
            with open(self.subscribers_file, 'r') as f:
                return json.load(f)

        return {
            "total": 0,
            "by_stage": {
                "awareness": [],
                "consideration": [],
                "decision": [],
                "loyal": []
            },
            "campaigns": []
        }

    def save_subscribers(self):
        """Save subscribers data"""
        with open(self.subscribers_file, 'w') as f:
            json.dump(self.subscribers, f, indent=2)

    def add_subscriber(self, email, name=None, stage="awareness"):
        """Add email subscriber"""
        subscriber = {
            "email": email,
            "name": name,
            "stage": stage,
            "subscribed_at": datetime.now().isoformat(),
            "emails_received": 0,
            "engagement_score": 0
        }

        if stage in self.subscribers["by_stage"]:
            self.subscribers["by_stage"][stage].append(subscriber)
            self.subscribers["total"] += 1
            self.save_subscribers()
            return subscriber

    def send_welcome_email(self, email):
        """Queue welcome email"""
        return {
            "template": "welcome",
            "to": email,
            "subject": "Welcome to AI Systems Engineer Curriculum",
            "scheduled_at": datetime.now().isoformat()
        }

    def send_weekly_digest(self):
        """Generate weekly digest"""
        today = datetime.now().date()
        last_week = today - timedelta(days=7)

        return {
            "template": "weekly_digest",
            "subject": f"Weekly Update - {today}",
            "content_focus": ["recent_posts", "top_contributors", "trending_projects"],
            "scheduled_for": str(today)
        }

    def nurture_lead(self, email, stage):
        """Nurture lead through sales funnel"""
        campaigns = {
            "awareness": {
                "subject": "Start Your AI Engineering Journey",
                "content": "Intro to curriculum and career path"
            },
            "consideration": {
                "subject": "How Our Students Landed $400K+ Jobs",
                "content": "Success stories and project portfolio"
            },
            "decision": {
                "subject": "Join 500+ Engineers Building AI Systems",
                "content": "Enrollment and early adopter benefits"
            }
        }

        if stage in campaigns:
            campaign = campaigns[stage]
            campaign["to"] = email
            campaign["scheduled_at"] = datetime.now().isoformat()

            self.subscribers["campaigns"].append(campaign)
            self.save_subscribers()
            return campaign


# Export classes
__all__ = [
    'ContentManagementSystem',
    'AdvancedAnalytics',
    'CommunityManager',
    'EmailAutomationNursery'
]

if __name__ == "__main__":
    # Example usage

    # Content Management
    cms = ContentManagementSystem()
    cms.add_blog_post("Getting Started", "Tutorial content", "tutorial", ["beginner", "python"])
    print("✅ Blog post added")

    # Analytics
    analytics = AdvancedAnalytics()
    analytics.record_daily_metrics("discord", {"members": 45, "messages": 120})
    print("✅ Daily metrics recorded")

    # Community
    community = CommunityManager()
    overview = community.get_community_overview()
    print(f"✅ Community Overview: {json.dumps(overview, indent=2)}")

    # Email
    email = EmailAutomationNursery()
    email.add_subscriber("user@example.com", "Alex")
    print("✅ Subscriber added")
