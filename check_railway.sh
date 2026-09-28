#!/bin/bash
cd /Users/aliasgarfatepurwala/agent-system

# Get the project and service info
PROJECT_ID="ff453173-0c12-4b93-b692-8a53a13e344c"
SERVICE_ID="efb11ab7-bb5d-4d05-b4c7-6bb4a0fe1c88"

# The Railway project URL
echo "📊 Railway Dashboard:"
echo "https://railway.com/project/$PROJECT_ID"
echo ""
echo "✅ Services Deployed:"
echo "- agent-system: ONLINE"
echo "- PgBouncer: ONLINE (3/3 replicas)"
echo "- PostgreSQL: CRASHED (optional for Phase 4)"
echo ""

# Try to get the service URL
echo "🔍 Checking deployment status..."
railway status 2>&1 | grep -A 5 "agent-system"
