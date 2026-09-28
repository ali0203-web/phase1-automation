#!/bin/bash
# RFQ Campaign Daily Scheduler
# Runs at 08:00 Dubai Time (04:00 UTC)

LOG_FILE="/Users/aliasgarfatepurwala/Claude-Data-Vault/rfq_scheduler.log"

# Record execution
echo "[$(date '+%Y-%m-%d %H:%M:%S')] RFQ Campaign Scheduler triggered" >> "$LOG_FILE"

# Change to data vault directory
cd /Users/aliasgarfatepurwala/Claude-Data-Vault

# Load environment
export $(cat ~/.env | xargs)

# Execute RFQ campaign
/usr/bin/python3 /Users/aliasgarfatepurwala/Claude-Data-Vault/rfq_campaign_execution.py >> "$LOG_FILE" 2>&1

# Log completion
echo "[$(date '+%Y-%m-%d %H:%M:%S')] RFQ Campaign execution completed" >> "$LOG_FILE"
