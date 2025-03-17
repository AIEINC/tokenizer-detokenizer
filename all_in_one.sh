#!/bin/bash

# Define repository directory
REPO_DIR="/data/data/com.termux/files/home/tokenizer-detokenizer"
GITHUB_USERNAME="AIEINC"
GITHUB_REPO_URL="https://github.com/AIEINC/tokenizer-detokenizer.git"
LOG_FILE="$HOME/all_in_one_log.txt"

echo "🚀 Starting full setup, testing, and update process..." | tee -a $LOG_FILE

# Ensure required packages are installed
pkg install -y git python nano termux-api openjdk-17 rclone
pip install pandas openpyxl

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

# Step 1: Run the required file creation script to ensure all files exist
echo "🔄 Running file creation script..." | tee -a $LOG_FILE
cat <<EOL > create_required_files.sh
#!/bin/bash
LANGUAGES=("python" "javascript" "go" "cpp" "rust" "php" "swift")

# Create necessary files
for lang in "\${LANGUAGES[@]}"; do
    touch "tokenized_output_\${lang}.json"
    touch "detokenized_output_\${lang}.\${lang}"
    touch "generated_code_\${lang}.\${lang}"
done

# Create a sample spreadsheet for auto-code generation
cat <<CSV > auto_code_blueprint.csv
Language,Component,Token
Python,Print Statement,IO001
JavaScript,Print Statement,IO001
Go,Function Declaration,F001
C++,Loop Structure,L001
Rust,Variable Declaration,V001
PHP,Class Definition,O001
Swift,Return Statement,RT001
CSV

echo "✅ All required files have been created!"
EOL

chmod +x create_required_files.sh
./create_required_files.sh

# Step 2: Run automated tests
echo "🔄 Running automated tests..." | tee -a $LOG_FILE
cat <<EOL > test_tokenizer.py
import json
import os
import subprocess

# Define test cases
test_cases = {
    "Python": {
        "input_file": "test_python.py",
        "source_code": "import os\\ndef hello():\\n    print('Hello, World!')\\nif True:\\n    hello()",
        "expected_tokens": ["I001", "F001", "C001", "IO001"]
    },
    "JavaScript": {
        "input_file": "test_javascript.js",
        "source_code": "function hello() {\\n    console.log('Hello, World!');\\n}\\nhello();",
        "expected_tokens": ["F001", "IO001"]
    },
    "Go": {
        "input_file": "test_go.go",
        "source_code": "package main\\nimport 'fmt'\\nfunc main() {\\n    fmt.Println('Hello, World!')\\n}",
        "expected_tokens": ["I001", "F001", "IO001"]
    }
}

def run_tokenizer_test():
    for lang, test_data in test_cases.items():
        print(f"\\n🔹 Testing {lang} Tokenization...\\n")
        with open(test_data["input_file"], "w") as f:
            f.write(test_data["source_code"])
        process = subprocess.run(["python", "tokenizer.py"], input="tokenize\\n" + lang + "\\n" + test_data["input_file"] + "\\n", text=True, capture_output=True)
        tokenized_file = f"tokenized_output_{lang.lower()}.json"
        if not os.path.exists(tokenized_file):
            print(f"❌ Tokenized output not found for {lang}!")
            continue
        with open(tokenized_file, "r") as f:
            tokenized_data = json.load(f)
        if tokenized_data["tokens"] == test_data["expected_tokens"]:
            print(f"✅ Tokenization for {lang} passed!")
        else:
            print(f"❌ Tokenization for {lang} failed! Expected: {test_data['expected_tokens']}, Got: {tokenized_data['tokens']}")
run_tokenizer_test()
EOL

python test_tokenizer.py

# Step 3: Add all files to Git tracking
echo "🔄 Adding all updated files to Git tracking..." | tee -a $LOG_FILE
git add tokenizer.py
git add test_tokenizer.py
git add tokenized_output_*.json
git add detokenized_output_*
git add generated_code_*
git add auto_code_blueprint.csv
git add create_required_files.sh
git add update.sh
git add all_in_one.sh

# Step 4: Commit and push changes
echo "🔄 Committing all updates..." | tee -a $LOG_FILE
git commit -m "Finalized full update with setup, testing, and GitHub integration"
git push origin main

echo "✅ Update complete! Check repository: $GITHUB_REPO_URL"
