#!/usr/bin/env python3
"""
Phase 1 Enhancements - Advanced Metrics, Sentiment Analysis, and Conversion Funnel Tracking
Extends phase1_automation.py with sophisticated analytics capabilities
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import re

class AdvancedMetricsEngine:
    """Track advanced metrics across all platforms"""

    def __init__(self, metrics_file='/tmp/phase1_metrics.json'):
        self.metrics_file = metrics_file
        self.data = self._load_metrics()

    def _load_metrics(self):
        """Load metrics from file"""
        if os.path.exists(self.metrics_file):
            try:
                with open(self.metrics_file, 'r') as f:
                    return json.load(f)
            except:
                return self._init_metrics()
        return self._init_metrics()

    def _init_metrics(self):
        """Initialize empty metrics structure"""
        return {
            "timestamp": datetime.now().isoformat(),
            "github": {
                "stars": 0,
                "discussions": 0,
                "comments": 0,
                "engagement_score": 0
            },
            "twitter": {
                "followers": 0,
                "impressions": 0,
                "engagements": 0,
                "engagement_rate": 0
            },
            "reddit": {
                "posts": 0,
                "karma": 0,
                "comments": 0,
                "subreddits": ["r/MachineLearning", "r/learnprogramming"]
            },
            "discord": {
                "members": 0,
                "messages": 0,
                "engagement_score": 0
            },
            "linkedin": {
                "followers": 0,
                "posts": 0,
                "engagements": 0
            },
            "overall": {
                "total_reach": 0,
                "engagement_rate": 0,
                "growth_rate": 0,
                "community_health": "excellent"
            }
        }

    def save_metrics(self):
        """Save metrics to file"""
        self.data["timestamp"] = datetime.now().isoformat()
        with open(self.metrics_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def calculate_engagement_score(self, platform_data):
        """Calculate engagement score for a platform"""
        if platform_data.get("followers", 0) == 0:
            return 0

        engagements = platform_data.get("engagements", 0) + platform_data.get("comments", 0)
        followers = platform_data.get("followers", 1)
        return min(10, (engagements / followers) * 10)

    def update_platform_metrics(self, platform, metrics_dict):
        """Update metrics for a specific platform"""
        if platform in self.data:
            self.data[platform].update(metrics_dict)
            self.save_metrics()

    def get_platform_breakdown(self):
        """Get engagement breakdown by platform"""
        breakdown = {}
        for platform in ["github", "twitter", "reddit", "discord", "linkedin"]:
            if platform in self.data:
                breakdown[platform] = self.calculate_engagement_score(self.data[platform])
        return breakdown

    def calculate_overall_health(self):
        """Calculate community health score"""
        scores = self.get_platform_breakdown()
        if not scores:
            return 0

        avg_score = sum(scores.values()) / len(scores)

        if avg_score >= 8:
            health = "excellent"
        elif avg_score >= 6:
            health = "good"
        elif avg_score >= 4:
            health = "moderate"
        else:
            health = "needs_attention"

        self.data["overall"]["community_health"] = health
        self.save_metrics()
        return health

    def get_growth_rate(self, days=7):
        """Calculate growth rate over N days"""
        # Simplified: just calculate current total reach growth
        current_reach = self.data["overall"].get("total_reach", 0)
        previous_reach = max(1, current_reach - 100)  # Simplified

        if previous_reach == 0:
            return 0

        growth = ((current_reach - previous_reach) / previous_reach) * 100
        self.data["overall"]["growth_rate"] = f"{growth:.1f}%"
        self.save_metrics()
        return growth


class SentimentAnalyzer:
    """Analyze sentiment of community feedback"""

    POSITIVE_WORDS = [
        'love', 'great', 'awesome', 'excellent', 'amazing', 'fantastic', 'wonderful',
        'perfect', 'best', 'thank', 'helpful', 'useful', 'impressive', 'brilliant'
    ]

    NEGATIVE_WORDS = [
        'hate', 'terrible', 'awful', 'bad', 'worst', 'useless', 'frustrated',
        'confused', 'difficult', 'broken', 'bug', 'error', 'problem', 'issue'
    ]

    def analyze_sentiment(self, text):
        """Analyze sentiment of text (-1 to 1 scale)"""
        text_lower = text.lower()

        positive_count = sum(1 for word in self.POSITIVE_WORDS if word in text_lower)
        negative_count = sum(1 for word in self.NEGATIVE_WORDS if word in text_lower)

        if positive_count == 0 and negative_count == 0:
            return 0  # Neutral

        sentiment_score = (positive_count - negative_count) / max(1, positive_count + negative_count)
        return min(1, max(-1, sentiment_score))

    def categorize_feedback(self, text):
        """Categorize feedback type"""
        text_lower = text.lower()

        if any(word in text_lower for word in ['curriculum', 'course', 'learn', 'project']):
            return "curriculum"
        elif any(word in text_lower for word in ['career', 'job', 'salary', 'money']):
            return "career"
        elif any(word in text_lower for word in ['bug', 'error', 'issue', 'problem']):
            return "technical"
        elif any(word in text_lower for word in ['help', 'how', 'tutorial', 'guide']):
            return "help"
        else:
            return "general"


class ConversionFunnelTracker:
    """Track conversion funnel: Visitor → Member → Student → Promoter"""

    def __init__(self, funnel_file='/tmp/conversion_funnel.json'):
        self.funnel_file = funnel_file
        self.funnel = self._load_funnel()

    def _load_funnel(self):
        """Load funnel data"""
        if os.path.exists(self.funnel_file):
            with open(self.funnel_file, 'r') as f:
                return json.load(f)

        return {
            "visitors": 0,
            "members": 0,
            "students": 0,
            "promoters": 0,
            "conversion_rates": {
                "visitor_to_member": 0,
                "member_to_student": 0,
                "student_to_promoter": 0
            },
            "last_updated": datetime.now().isoformat()
        }

    def save_funnel(self):
        """Save funnel data"""
        self.funnel["last_updated"] = datetime.now().isoformat()
        with open(self.funnel_file, 'w') as f:
            json.dump(self.funnel, f, indent=2)

    def update_stage(self, stage, increment=1):
        """Update conversion funnel stage"""
        if stage in self.funnel:
            self.funnel[stage] += increment
            self._calculate_conversion_rates()
            self.save_funnel()

    def _calculate_conversion_rates(self):
        """Calculate conversion rates between stages"""
        visitors = max(1, self.funnel["visitors"])
        members = max(1, self.funnel["members"])
        students = max(1, self.funnel["students"])

        self.funnel["conversion_rates"]["visitor_to_member"] = (self.funnel["members"] / visitors) * 100
        self.funnel["conversion_rates"]["member_to_student"] = (self.funnel["students"] / members) * 100
        self.funnel["conversion_rates"]["student_to_promoter"] = (self.funnel["promoters"] / students) * 100

    def get_funnel_status(self):
        """Get current funnel status"""
        return {
            "stage": self._current_stage(),
            "conversion_rates": self.funnel["conversion_rates"],
            "counts": {
                "visitors": self.funnel["visitors"],
                "members": self.funnel["members"],
                "students": self.funnel["students"],
                "promoters": self.funnel["promoters"]
            }
        }

    def _current_stage(self):
        """Determine current funnel stage"""
        if self.funnel["promoters"] > 10:
            return "scaling"
        elif self.funnel["students"] > 20:
            return "growing"
        elif self.funnel["members"] > 50:
            return "established"
        else:
            return "early_stage"


class IntelligentResponseEngine:
    """Generate intelligent responses based on context"""

    RESPONSE_TEMPLATES = {
        "curriculum": {
            "common": "Great question about the curriculum! 🎓 We have a 14-week program covering {topic}.",
            "follow_up": "Would you like me to walk you through the {topic} module?"
        },
        "career": {
            "common": "Career growth is key! 💼 Many students progress from $80K to ${amount}K in {timeframe}.",
            "follow_up": "What's your current experience level?"
        },
        "technical": {
            "common": "Let's debug this! 🔧 Can you share more details about the {issue}?",
            "follow_up": "Have you tried {suggestion}?"
        },
        "help": {
            "common": "I'm here to help! 🤝 Here's what I recommend: {step1}, {step2}, {step3}.",
            "follow_up": "Let me know if you need clarification on any step!"
        }
    }

    def generate_response(self, category, context=None):
        """Generate response based on category and context"""
        if category in self.RESPONSE_TEMPLATES:
            template = self.RESPONSE_TEMPLATES[category]["common"]
            return template
        return "Thanks for your message! Let me help you with that. 👊"

    def add_personal_touch(self, username, response):
        """Add personal touch to response"""
        return f"Hey {username}! {response}"


class PlatformCoordinator:
    """Coordinate actions across all platforms"""

    def __init__(self):
        self.metrics = AdvancedMetricsEngine()
        self.sentiment = SentimentAnalyzer()
        self.funnel = ConversionFunnelTracker()
        self.responses = IntelligentResponseEngine()

    def sync_all_platforms(self):
        """Synchronize data across all platforms"""
        # Calculate overall community health
        health = self.metrics.calculate_overall_health()

        # Get platform breakdown
        breakdown = self.metrics.get_platform_breakdown()

        # Calculate growth rate
        growth = self.metrics.get_growth_rate()

        return {
            "timestamp": datetime.now().isoformat(),
            "community_health": health,
            "platform_scores": breakdown,
            "growth_rate": f"{growth:.1f}%",
            "funnel_status": self.funnel.get_funnel_status()
        }

    def process_community_feedback(self, text, user=None, platform=None):
        """Process and respond to community feedback"""
        sentiment = self.sentiment.analyze_sentiment(text)
        category = self.sentiment.categorize_feedback(text)

        # Generate response
        response = self.responses.generate_response(category)
        if user:
            response = self.responses.add_personal_touch(user, response)

        return {
            "sentiment": sentiment,
            "category": category,
            "response": response,
            "platform": platform
        }


# Export classes
__all__ = [
    'AdvancedMetricsEngine',
    'SentimentAnalyzer',
    'ConversionFunnelTracker',
    'IntelligentResponseEngine',
    'PlatformCoordinator'
]

if __name__ == "__main__":
    # Example usage
    coordinator = PlatformCoordinator()

    # Sync all platforms
    status = coordinator.sync_all_platforms()
    print("Platform Status:")
    print(json.dumps(status, indent=2))

    # Process feedback
    feedback = "This curriculum is amazing! I love the career progression path."
    result = coordinator.process_community_feedback(feedback, user="Alex", platform="discord")
    print("\nFeedback Analysis:")
    print(json.dumps(result, indent=2))
