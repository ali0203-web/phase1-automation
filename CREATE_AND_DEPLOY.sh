#!/bin/bash

# AUTOMATED GITHUB REPO CREATION + RENDER DEPLOYMENT SCRIPT
# Run this script to complete the full deployment

set -e

echo "🚀 AUTONOMOUS DEPLOYMENT SCRIPT"
echo "======================================"
echo ""

# Step 1: Create GitHub repo via web (user will need to authorize)
echo "STEP 1: Creating GitHub Repository..."
echo "Opening https://github.com/new in browser..."
echo ""
echo "Manual steps:"
echo "1. Repository name: phase1-automation"
echo "2. Description: Phase 1 Social Media Automation - Docker + Cloud Ready"
echo "3. Visibility: Public"
echo "4. Click: Create repository"
echo ""
read -p "Press ENTER once you've created the repo..."

# Step 2: Push code
echo ""
echo "STEP 2: Pushing code to GitHub..."
cd /tmp
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/aliasgarfatepurwala/phase1-automation.git
git branch -M main
git push -u origin main

echo "✅ Code pushed!"
echo ""

# Step 3: Deploy to Render
echo "STEP 3: Deploying to Render..."
echo "Opening https://render.com/new-web-service in browser..."
echo ""
echo "Manual steps:"
echo "1. Sign up/In with GitHub"
echo "2. Authorize Render"
echo "3. Select phase1-automation repo"
echo "4. Click: Create Web Service"
echo "5. Wait for green 'Live' status"
echo ""
read -p "Press ENTER once deployment is Live on Render..."

echo ""
echo "======================================"
echo "✅ DEPLOYMENT COMPLETE!"
echo "======================================"
echo ""
echo "Your automation is now running 24/7 on Render!"
echo ""
