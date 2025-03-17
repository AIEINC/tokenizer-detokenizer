import json
import os
import subprocess

# Define test cases
test_cases = {
    "Python": {
        "input_file": "test_python.py",
        "source_code": "import os\ndef hello():\n    print('Hello, World!')\nif True:\n    hello()",
        "expected_tokens": ["I001", "F001", "C001", "IO001"]
    },
    "JavaScript": {
        "input_file": "test_javascript.js",
        "source_code": "function hello() {\n    console.log('Hello, World!');\n}\nhello();",
        "expected_tokens": ["F001", "IO001"]
    },
    "Go": {
        "input_file": "test_go.go",
        "source_code": "package main\nimport 'fmt'\nfunc main() {\n    fmt.Println('Hello, World!')\n}",
        "expected_tokens": ["I001", "F001", "IO001"]
    }
}

def run_tokenizer_test():
    for lang, test_data in test_cases.items():
        print(f"\n🔹 Testing {lang} Tokenization...\n")
        with open(test_data["input_file"], "w") as f:
            f.write(test_data["source_code"])
        process = subprocess.run(["python", "tokenizer.py"], input="tokenize\n" + lang + "\n" + test_data["input_file"] + "\n", text=True, capture_output=True)
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
