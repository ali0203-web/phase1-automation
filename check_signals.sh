#!/bin/bash

URL="https://agent-system-production-6667.up.railway.app"
KEY="default-api-key-demo"

echo "╔════════════════════════════════════════════════════════════╗"
echo "║              CHECKING TRADING SIGNALS                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Get signals
SIGNALS=$(curl -s -H "X-API-Key: $KEY" "$URL/api/signals" 2>/dev/null)

# Count signals
SIGNAL_COUNT=$(echo "$SIGNALS" | jq '.signals | length' 2>/dev/null)

if [ -z "$SIGNAL_COUNT" ] || [ "$SIGNAL_COUNT" = "null" ]; then
  SIGNAL_COUNT=0
fi

echo "📊 Signal Status"
echo "─────────────────────────────────────────────────────────────"
echo "Total Signals Generated: $SIGNAL_COUNT"
echo ""

if [ "$SIGNAL_COUNT" -gt 0 ]; then
  echo "✅ SIGNALS DETECTED - System is generating trading signals!"
  echo ""
  echo "📋 Recent Signals:"
  echo "$SIGNALS" | jq '.signals[0:5] | .[] | {agent: .agent_name, symbol: .symbol, type: .signal_type, confidence: .confidence}' 2>/dev/null
else
  echo "⏳ Waiting for first signals..."
  echo ""
  echo "Agents execute on 5-15 minute schedules."
  echo "Signals should appear within the next few minutes."
  echo ""
  echo "Check again in 1-2 minutes:"
  echo "  curl -H 'X-API-Key: default-api-key-demo' \\"
  echo "    $URL/api/signals | jq '.signals | length'"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Checking metrics and agent status...                     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check metrics
METRICS=$(curl -s -H "X-API-Key: $KEY" "$URL/api/metrics" 2>/dev/null)
TOTAL_TRADES=$(echo "$METRICS" | jq '.agentMetrics | length' 2>/dev/null)

echo "📈 Agent Metrics"
echo "─────────────────────────────────────────────────────────────"
echo "Agents with Data: $TOTAL_TRADES"
echo ""

# Check health
HEALTH=$(curl -s "$URL/health" | jq '.status')
echo "🏥 System Health: $HEALTH"
echo ""

# Rate limit
RATE=$(curl -s -H "X-API-Key: $KEY" "$URL/api/security/rate-limit" 2>/dev/null | jq '.rateLimit')
REMAINING=$(echo "$RATE" | jq '.remaining')
echo "🔐 API Rate Limit: $REMAINING/100 requests remaining"
echo ""

echo "╔════════════════════════════════════════════════════════════╗"
if [ "$SIGNAL_COUNT" -gt 0 ]; then
  echo "║  ✅ SIGNALS LIVE - SYSTEM TRADING ACTIVELY              ║"
else
  echo "║  ⏳ INITIALIZING - FIRST SIGNALS COMING SOON            ║"
fi
echo "╚════════════════════════════════════════════════════════════╝"

