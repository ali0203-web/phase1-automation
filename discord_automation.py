#!/usr/bin/env python3
"""
Discord Automation Bot - Community Hub for AI Systems Engineer Curriculum
Handles auto-responses, member management, engagement tracking, and analytics
"""

import discord
from discord.ext import commands, tasks
import json
import os
from datetime import datetime
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DISCORD_CLIENT_ID = os.getenv('DISCORD_CLIENT_ID')

# Activity log file
ACTIVITY_LOG_FILE = '/tmp/discord_activity.json'

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Response templates for auto-responses
CURRICULUM_RESPONSE = """
🎓 **AI Systems Engineer Curriculum Overview**

📚 **14-Week Program:**
- Week 1-2: Foundation (Python, ML basics)
- Week 3-4: Advanced concepts
- Week 5-6: Project implementation
- Week 7-14: Production systems & career path

💰 **Career Progression:** $80K → $600K+

✨ **14 Production Projects** covering:
- Machine Learning systems
- Data pipelines
- Cloud deployment
- Real-world applications

👉 **Get Started:** Check pinned messages for resources!
"""

CAREER_RESPONSE = """
💼 **Career Progression Path**

🚀 **Starting Point:** $80K-$120K
- Entry-level AI engineer roles
- Strong foundational knowledge
- Industry-ready projects

📈 **Mid-Level:** $200K-$300K
- Senior engineer positions
- Team leadership
- Specialized domain expertise

🌟 **Senior Level:** $400K-$600K+
- Principal engineer roles
- AI/ML strategy
- Technical leadership

📊 **What Accelerates Growth:**
1. Complete production projects ✅
2. Open-source contributions
3. Speaking/writing about work
4. Building in public
5. Network in AI community

💡 **Our curriculum is designed to accelerate every step!**
"""

HELP_RESPONSE = """
🆘 **Getting Started Guide**

**Step 1: Join Our Community**
- You're already here! 🎉

**Step 2: Introduce Yourself**
- Post in #introductions channel
- Share your goals & interests

**Step 3: Access Curriculum**
- Check #resources for links
- See pinned messages for setup
- Join study groups

**Step 4: Start Learning**
- Follow the 14-week path
- Complete projects
- Engage with community

**Step 5: Share Progress**
- Post your wins in #wins channel
- Help others in #questions
- Build your portfolio

📞 **Need Help?**
- Ask in #questions or #help
- Mention @moderators if urgent
"""

# Initialize activity log
def init_activity_log():
    """Initialize activity log file if it doesn't exist"""
    if not os.path.exists(ACTIVITY_LOG_FILE):
        initial_data = {
            "started_at": datetime.now().isoformat(),
            "members_joined": 0,
            "messages_logged": 0,
            "engagement_score": 0,
            "activity_by_hour": {},
            "top_active_users": {},
            "last_updated": datetime.now().isoformat()
        }
        with open(ACTIVITY_LOG_FILE, 'w') as f:
            json.dump(initial_data, f, indent=2)

def log_activity(activity_type, user=None, content=None, channel=None):
    """Log activities to JSON file for analytics"""
    try:
        if os.path.exists(ACTIVITY_LOG_FILE):
            with open(ACTIVITY_LOG_FILE, 'r') as f:
                data = json.load(f)
        else:
            init_activity_log()
            with open(ACTIVITY_LOG_FILE, 'r') as f:
                data = json.load(f)

        now = datetime.now()
        hour_key = now.strftime("%Y-%m-%d %H:00")

        # Update hourly activity
        if hour_key not in data["activity_by_hour"]:
            data["activity_by_hour"][hour_key] = 0
        data["activity_by_hour"][hour_key] += 1

        # Track user activity
        if user:
            user_key = str(user)
            if user_key not in data["top_active_users"]:
                data["top_active_users"][user_key] = 0
            data["top_active_users"][user_key] += 1

        # Log activity type
        data["messages_logged"] = data.get("messages_logged", 0) + 1
        data["last_updated"] = now.isoformat()

        with open(ACTIVITY_LOG_FILE, 'w') as f:
            json.dump(data, f, indent=2)

        logger.info(f"Activity logged: {activity_type} by {user}")
    except Exception as e:
        logger.error(f"Error logging activity: {e}")

class DiscordAutomation(commands.Cog):
    """Main Discord automation cog"""

    def __init__(self, bot):
        self.bot = bot
        self.engagement_tracker.start()

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when bot connects to Discord"""
        logger.info(f'✅ Bot logged in as {self.bot.user}')
        await self.bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="AI Systems Engineer Curriculum | !help for info"
        ))
        init_activity_log()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Welcome new members"""
        logger.info(f"New member joined: {member}")

        try:
            # Send welcome DM
            await member.send(f"""
👋 **Welcome to the AI Systems Engineer Community!**

Hey {member.name}! Excited to have you here.

This is a community dedicated to learning advanced AI/ML systems engineering with a path from $80K → $600K+.

**Quick Start:**
1. Check #introductions and say hi! 👋
2. Read #resources for curriculum details
3. Browse #questions if you have any
4. Join our study groups!

Feel free to reach out anytime. Let's build amazing things together! 🚀
            """)
        except Exception as e:
            logger.error(f"Could not send welcome DM to {member}: {e}")

        # Log activity
        log_activity("member_join", user=member.name)

    @commands.Cog.listener()
    async def on_message(self, message):
        """Handle incoming messages for auto-responses"""
        if message.author == self.bot.user:
            return

        # Log all messages
        log_activity("message", user=message.author, content=message.content[:50], channel=message.channel.name)

        # Auto-response triggers
        content_lower = message.content.lower()

        # Curriculum questions
        if any(word in content_lower for word in ['curriculum', 'course', 'program', 'learn', 'start']):
            if 'curriculum' in content_lower or 'course' in content_lower or 'program' in content_lower:
                await message.reply(CURRICULUM_RESPONSE, mention_author=True)
                return

        # Career questions
        if any(word in content_lower for word in ['career', 'salary', 'job', 'money', 'income', '$', 'money']):
            await message.reply(CAREER_RESPONSE, mention_author=True)
            return

        # Help/Getting started
        if any(word in content_lower for word in ['help', 'how', 'start', 'beginning', 'new', 'tutorial']):
            await message.reply(HELP_RESPONSE, mention_author=True)
            return

        await self.bot.process_commands(message)

    @tasks.loop(hours=1)
    async def engagement_tracker(self):
        """Track engagement metrics hourly"""
        try:
            total_members = 0
            total_messages = 0

            for guild in self.bot.guilds:
                total_members += guild.member_count

                # Log metrics
                log_activity("engagement_check", user="system")

            logger.info(f"Engagement tracked: {total_members} members")
        except Exception as e:
            logger.error(f"Error in engagement tracker: {e}")

    @engagement_tracker.before_loop
    async def before_engagement_tracker(self):
        """Wait until bot is ready before starting tracker"""
        await self.bot.wait_until_ready()

    @commands.command(name='stats')
    async def show_stats(self, ctx):
        """Show community statistics (!stats)"""
        try:
            if os.path.exists(ACTIVITY_LOG_FILE):
                with open(ACTIVITY_LOG_FILE, 'r') as f:
                    data = json.load(f)

                guild = ctx.guild
                embed = discord.Embed(title="📊 Community Statistics", color=discord.Color.blue())
                embed.add_field(name="Total Members", value=str(guild.member_count), inline=False)
                embed.add_field(name="Messages Logged", value=str(data.get('messages_logged', 0)), inline=False)
                embed.add_field(name="Last Updated", value=data.get('last_updated', 'Never'), inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send("📊 No stats available yet. Check back soon!")
        except Exception as e:
            logger.error(f"Error showing stats: {e}")
            await ctx.send(f"Error retrieving stats: {e}")

    @commands.command(name='announce')
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *, message):
        """Post announcement to channel (!announce <message>)"""
        try:
            embed = discord.Embed(
                title="📢 Community Announcement",
                description=message,
                color=discord.Color.gold()
            )
            embed.set_footer(text=f"Posted by {ctx.author}")

            await ctx.send(embed=embed)
            log_activity("announcement", user=ctx.author, content=message)
        except Exception as e:
            logger.error(f"Error posting announcement: {e}")
            await ctx.send(f"Error posting announcement: {e}")

# Set up bot
async def setup_bot():
    """Initialize bot with cogs"""
    await bot.add_cog(DiscordAutomation(bot))

# Main execution
async def main():
    """Run the bot"""
    init_activity_log()
    await setup_bot()
    await bot.start(DISCORD_BOT_TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
