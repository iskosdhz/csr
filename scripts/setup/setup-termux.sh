#!/bin/bash
# CSR Professional Setup Script for Termux

set -e  # Exit on error

echo "🔒 CSR Professional Setup"
echo "========================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running in Termux
if [ ! -d "$PREFIX" ]; then
    error "This script is designed for Termux only!"
    exit 1
fi

log "Starting CSR professional setup..."

# Update and upgrade system
log "Updating system packages..."
pkg update -y && pkg upgrade -y

# Install essential packages
log "Installing essential packages..."
pkg install -y \
    git python nodejs ruby \
    nano vim tree curl wget \
    clang make cmake binutils

# Install security tools
log "Installing security tools..."
pkg install -y \
    unstable-repo \
    metasploit nmap hydra sqlmap \
    tshark tcpdump netcat-openbsd

# Install Python packages
log "Installing Python packages..."
pip install --upgrade pip
pip install \
    requests beautifulsoup4 \
    scapy pycryptodome

# Setup Git configuration
log "Configuring Git..."
git config --global user.name "iskos"
git config --global user.email "iskos532@gmail.com"
git config --global init.defaultBranch main

# Create CSR directories structure
log "Creating CSR directory structure..."
mkdir -p \
    ~/csr/{docs,tools,notes,labs,progress,scripts} \
    ~/csr/tools/{scanners,analyzers,utilities} \
    ~/csr/notes/{linux,networking,web-security} \
    ~/csr/labs/{tryhackme,hackthebox,practice} \
    ~/csr/scripts/{python,bash,automation}

# Setup bashrc for CSR
log "Setting up custom bashrc..."
cat >> ~/.bashrc << 'EOF'

# ==================== CSR CUSTOM CONFIG ====================
export CSR_HOME="$HOME/csr"
export PATH="$CSR_HOME/scripts:$PATH"

# CSR Aliases
alias csr-cd="cd \$CSR_HOME"
alias csr-update="cd \$CSR_HOME && git pull"
alias csr-scan="python3 \$CSR_HOME/tools/scanners/port-scanner.py"
alias csr-lab="cd \$CSR_HOME/labs"

# Security Tools Aliases
alias msf="msfconsole"
alias nmap="nmap --script-updatedb"
alias pysec="python3"

echo "🔒 CSR Environment Loaded! Use 'csr-cd' to navigate."
# ==================== END CSR CONFIG ====================
EOF

# Make scripts executable
log "Making scripts executable..."
find ~/csr/scripts -name "*.sh" -exec chmod +x {} \;
find ~/csr/scripts -name "*.py" -exec chmod +x {} \;

# Create initial progress file
log "Creating progress tracker..."
cat > ~/csr/progress/current-status.json << 'EOF'
{
    "current_phase": "foundation",
    "current_module": "linux-basics",
    "progress_percentage": 85,
    "last_updated": "$(date -I)",
    "next_goals": [
        "Complete networking module",
        "Start Python for security",
        "Setup first lab environment"
    ]
}
EOF

log "CSR professional setup completed successfully!"
echo ""
echo "🎯 Next steps:"
echo "1. Run: source ~/.bashrc"
echo "2. Navigate: csr-cd"
echo "3. Explore the CSR structure"
echo "4. Start with: cat docs/learning-path.md"
echo ""
echo "🔒 Happy learning!"
