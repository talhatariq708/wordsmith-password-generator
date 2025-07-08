#!/bin/bash

echo "📦 Installing Wordsmith..."

# Clone repo to user home
git clone https://github.com/talhatariq708/wordsmith-password-generator.git ~/wordsmith

# Add to shell (bash or zsh)
if [ -n "$ZSH_VERSION" ]; then
    PROFILE="$HOME/.zshrc"
else
    PROFILE="$HOME/.bashrc"
fi

# Add run + update aliases
echo "alias wordsmith='python3 ~/wordsmith/main.py'" >> $PROFILE
echo "alias wordsmith-update='cd ~/wordsmith && git pull && echo 🔄 Wordsmith Updated!'" >> $PROFILE

# Reload shell
source $PROFILE

echo "✅ Wordsmith installed!"
echo "👉 Run it: wordsmith"
echo "🔄 Update it anytime: wordsmith-update"
