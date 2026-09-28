#!/bin/bash

# Production URL
PROD_URL="https://agent-system-production-6667.up.railway.app"
API_KEY="default-api-key-demo"

echo "========================================"
echo "Production Endpoint Verification"
echo "========================================"
echo ""
echo "Testing: $PROD_URL"
echo ""

# Test 1: Health Check (no auth required)
echo "1️⃣  Health Check (GET /health)"
echo "---"
curl -s -w "\nHTTP Status: %{http_code}\n" "$PROD_URL/health" | head -20
echo ""

# Test 2: API Agents List (requires auth)
echo "2️⃣  List Agents (GET /api/agents)"
echo "---"
curl -s -w "\nHTTP Status: %{http_code}\n" \
  -H "X-API-Key: $API_KEY" \
  "$PROD_URL/api/agents" | jq '.total, .agents | length' 2>/dev/null || echo "Failed or invalid response"
echo ""

# Test 3: Rate Limit Status
echo "3️⃣  Rate Limit Status (GET /api/security/rate-limit)"
echo "---"
curl -s -w "\nHTTP Status: %{http_code}\n" \
  -H "X-API-Key: $API_KEY" \
  "$PROD_URL/api/security/rate-limit" | jq '.rateLimit' 2>/dev/null || echo "Failed or invalid response"
echo ""

# Test 4: Alert Status
echo "4️⃣  Alert Status (GET /api/alerts/status)"
echo "---"
curl -s -w "\nHTTP Status: %{http_code}\n" \
  -H "X-API-Key: $API_KEY" \
  "$PROD_URL/api/alerts/status" | jq '.alerts' 2>/dev/null || echo "Failed or invalid response"
echo ""

# Test 5: Security Info
echo "5️⃣  Security Info (GET /api/security/info)"
echo "---"
curl -s -w "\nHTTP Status: %{http_code}\n" \
  -H "X-API-Key: $API_KEY" \
  "$PROD_URL/api/security/info" | jq '.authentication, .rateLimit' 2>/dev/null || echo "Failed or invalid response"
echo ""

echo "========================================"
echo "Verification Complete"
echo "========================================"
