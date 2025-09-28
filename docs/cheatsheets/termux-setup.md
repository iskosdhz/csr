# 🐧 Termux Setup for Cybersecurity

## Essential Packages
```bash
# Update system
pkg update && pkg upgrade

# Basic tools
pkg install git python nodejs ruby nano vim

# Security tools
pkg install unstable-repo
pkg install metasploit nmap hydra sqlmap

# Networking
pkg install curl wget netcat-openbsd tcpdump

# Development
pkg install clang make cmake binutils

# Edit ~/.bashrc
alias msf='msfconsole'
alias nmap='nmap --script-updatedb' 
alias py='python'
alias l='ls -la'
alias uu='pkg update && pkg upgrade'

export PS1='iskos@\h:➜ "


### **Step 7: Setup Git dan Push**

