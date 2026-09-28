#!/bin/bash
BASE_URL="https://agent-system-production-6667.up.railway.app"

echo "=== API ENDPOINT TESTS ==="
echo ""

echo "1. HEALTH CHECK"
echo "GET $BASE_URL/api/health"
curl -s "$BASE_URL/api/health" | jq . 2>/dev/null || curl -s "$BASE_URL/api/health"
echo ""
echo ""

echo "2. ALL AGENTS"
echo "GET $BASE_URL/api/agents"
curl -s "$BASE_URL/api/agents" | jq '.agents | length' 2>/dev/null || echo "Failed to parse"
echo ""
echo ""

echo "3. AGENT DETAILS (First agent)"
echo "GET $BASE_URL/api/agents"
FIRST_AGENT=$(curl -s "$BASE_URL/api/agents" | jq -r '.agents[0].id' 2>/dev/null)
if [ ! -z "$FIRST_AGENT" ]; then
  echo "Testing agent: $FIRST_AGENT"
  curl -s "$BASE_URL/api/agents/$FIRST_AGENT" | jq . 2>/dev/null || curl -s "$BASE_URL/api/agents/$FIRST_AGENT"
else
  echo "Could not get agent list"
fi
echo ""
echo ""

echo "4. SIGNALS"
echo "GET $BASE_URL/api/signals"
curl -s "$BASE_URL/api/signals" | jq '.signals | length' 2>/dev/null || echo "Failed to parse"
echo ""
echo ""

echo "5. METRICS"
echo "GET $BASE_URL/api/metrics"
curl -s "$BASE_URL/api/metrics" | jq '.metrics | length' 2>/dev/null || echo "Failed to parse"
echo ""
echo ""

echo "6. DAILY METRICS"
echo "GET $BASE_URL/api/metrics/daily"
curl -s "$BASE_URL/api/metrics/daily" | jq . 2>/dev/null || echo "Failed to parse"
echo ""
echo ""

echo "7. PERFORMANCE (Top/Worst)"
echo "GET $BASE_URL/api/performance"
curl -s "$BASE_URL/api/performance" | jq . 2>/dev/null || echo "Failed to parse"
echo ""
echo ""

echo "8. DASHBOARD AGENTS"
echo "GET $BASE_URL/api/dashboard/agents"
curl -s "$BASE_URL/api/dashboard/agents" | jq '.agents | length' 2>/dev/null || echo "Failed to parse"
echo ""
echo ""

echo "9. DASHBOARD SIGNALS"
echo "GET $BASE_URL/api/dashboard/signals"
curl -s "$BASE_URL/api/dashboard/signals" | jq '.signals | length' 2>/dev/null || echo "Failed to parse"
echo ""
echo ""

echo "10. DASHBOARD SUMMARY"
echo "GET $BASE_URL/api/dashboard/summary"
curl -s "$BASE_URL/api/dashboard/summary" | jq '.summary | length' 2>/dev/null || echo "Failed to parse"
echo ""
