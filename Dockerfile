FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install tweepy praw requests schedule python-dotenv

# Copy automation script
COPY phase1_cloud_ready.py /app/
COPY .env /app/

# Run automation
CMD ["python3", "phase1_cloud_ready.py"]
