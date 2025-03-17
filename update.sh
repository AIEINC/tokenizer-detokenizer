#!/bin/bash

# Define repository directory
REPO_DIR="/data/data/com.termux/files/home/tokenizer-detokenizer"
GITHUB_USERNAME="AIEINC"
GITHUB_REPO_URL="https://github.com/AIEINC/tokenizer-detokenizer.git"
LOG_FILE="$HOME/update_log.txt"

echo "🚀 Starting full update process for tokenizer-detokenizer..." | tee -a $LOG_FILE

# Ensure Git is installed
pkg install -y git

# Navigate to the repository
if [ -d "$REPO_DIR" ]; then
    echo "📂 Repository found. Pulling latest changes..." | tee -a $LOG_FILE
    cd "$REPO_DIR" || exit
    git pull origin main
else
    echo "🛠️ Cloning GitHub repository to $REPO_DIR..." | tee -a $LOG_FILE
    git clone "$GITHUB_REPO_URL" "$REPO_DIR"
    cd "$REPO_DIR" || exit
fi

# Ensure tokenizer.py exists
if [ ! -f "$REPO_DIR/tokenizer.py" ]; then
    echo "❌ tokenizer.py not found in $REPO_DIR. Exiting." | tee -a $LOG_FILE
    exit 1
fi

# Run the required file creation script to ensure all files exist
echo "🔄 Running file creation script to generate missing files..." | tee -a $LOG_FILE
if [ -f "$REPO_DIR/create_required_files.sh" ]; then
    chmod +x "$REPO_DIR/create_required_files.sh"
    "$REPO_DIR/create_required_files.sh"
else
    echo "❌ create_required_files.sh not found. Please ensure it exists in the repository." | tee -a $LOG_FILE
    exit 1
fi

# Add all required files to Git tracking
echo "🔄 Adding all updated files to Git tracking..." | tee -a $LOG_FILE
git add tokenizer.py
git add tokenized_output_*.json
git add detokenized_output_*
git add generated_code_*
git add auto_code_blueprint.csv
git add create_required_files.sh
git add update.sh

# Commit and push changes
echo "🔄 Committing all updates..." | tee -a $LOG_FILE
git commit -m "Finalized update: Multi-language support, spreadsheet integration, and tokenization enhancements"
git push origin main

echo "✅ Update complete! Check repository: $GITHUB_REPO_URL"
