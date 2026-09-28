#!/bin/bash
cd "/Users/aliasgarfatepurwala/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/trading-agents"

# Try linking with echo to select first project
echo "1" | railway project link 2>/dev/null || true

# Get the current linked project
echo ""
echo "Checking linked project..."
railway status 2>&1 | head -5
