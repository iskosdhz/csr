#!/bin/bash
# CSR Repository Update Automation

echo "🔒 CSR Repository Update"
echo "========================"

# Update from GitHub
echo "📥 Pulling latest changes..."
git pull origin main

# Update Termux packages
echo "📦 Updating system packages..."
pkg update -y && pkg upgrade -y

# Update Python packages
echo "🐍 Updating Python packages..."
pip install --upgrade pip
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U

echo "✅ CSR update completed!"


