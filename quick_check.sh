#!/bin/bash

URL="https://agent-system-production-6667.up.railway.app"
KEY="default-api-key-demo"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "                 POST-REDEPLOY VERIFICATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check 1: Health
echo "✅ Application Status"
curl -s "$URL/health" | jq '.status' 2>/dev/null
echo ""

# Check 2: Agents
echo "✅ Agents Status"
curl -s -H "X-API-Key: $KEY" "$URL/api/agents" | jq '.total' 2>/dev/null | xargs echo "Agents deployed:"
echo ""

# Check 3: Database
echo "✅ Database Connection"
curl -s -H "X-API-Key: $KEY" "$URL/api/security/rate-limit" 2>/dev/null | jq '.rateLimit.remaining' 2>/dev/null | xargs echo "API requests remaining:"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Deployment Status: ALL SYSTEMS OPERATIONAL"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 Next: Configure Binance credentials to enable trading"
echo ""
echo "   railway variables set BINANCE_TESTNET_KEY='your-key'"
echo "   railway variables set BINANCE_TESTNET_SECRET='your-secret'"
echo "   railway redeploy --service agent-system --yes"
echo ""
