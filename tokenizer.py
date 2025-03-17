import json
import re
import sys

# IP owned by Joseph Lacroix

# Token Map for Multiple Languages
token_map = {
    "Python": {
        "import": "I001",
        "def": "F001",
        "for": "L001",
        "print": "IO01",
        "if": "C001",
        "var": "V001"
    },
    "Go": {
        "import": "I001",
        "func": "F001",
        "for": "L001",
        "fmt.Println": "IO01",
        "if": "C001",
        "var": "V001"
    },
    "JavaScript": {
        "import": "I001",
        "function": "F001",
        "for": "L001",
        "console.log": "IO01",
        "if": "C001",
        "let": "V001"
    }
}

# Reverse Token Map for Detokenization
reverse_token_map = {lang: {v: k for k, v in token_map[lang].items()} for lang in token_map}

def tokenize_code(source_code, language):
    if language not in token_map:
        print(f"Unsupported language: {language}")
        return []

    lines = source_code.split("\n")
    tokenized_code = []

    for line in lines:
        line = line.strip()
        for keyword, token in token_map[language].items():
            if re.match(f"^{keyword}\b", line):
                tokenized_code.append(token)
                break

    return tokenized_code

def detokenize_code(token_list, language):
    if language not in reverse_token_map:
        print(f"Unsupported language: {language}")
        return ""

    detokenized_code = []
    for token in token_list:
        if token in reverse_token_map[language]:
            detokenized_code.append(reverse_token_map[language][token])
        else:
            detokenized_code.append("# UNKNOWN TOKEN")
    return "\n".join(detokenized_code)

def save_tokenized_output(tokens, output_file):
    with open(output_file, "w") as f:
        json.dump({"tokens": tokens}, f, indent=4)
    print(f"Tokenized output saved to {output_file}")

def save_detokenized_output(detokenized_code, output_file):
    with open(output_file, "w") as f:
        f.write(detokenized_code)
    print(f"Detokenized code saved to {output_file}")

def main():
    mode = input("Enter mode (tokenize/detokenize): ").strip().lower()
    language = input("Enter programming language (Python/Go/JavaScript): ").strip()

    if mode == "tokenize":
        file_path = input("Enter the path to the source code file: ")
        try:
            with open(file_path, "r") as f:
                source_code = f.read()
        except Exception as e:
            print(f"Error reading the source code file: {e}")
            sys.exit(1)

        tokens = tokenize_code(source_code, language)
        print("\nTokenized Code:", tokens)

        output_file = "tokenized_output.json"
        save_tokenized_output(tokens, output_file)

    elif mode == "detokenize":
        file_path = input("Enter the path to the tokenized JSON file: ")
        try:
            with open(file_path, "r") as f:
                token_data = json.load(f)
                tokens = token_data.get("tokens", [])
        except Exception as e:
            print(f"Error reading the tokenized file: {e}")
            sys.exit(1)

        detokenized_code = detokenize_code(tokens, language)
        print("\nDetokenized Code:")
        print(detokenized_code)

        output_file = f"detokenized_output.{language.lower()}"
        save_detokenized_output(detokenized_code, output_file)
    else:
        print("Invalid mode selected.")
        sys.exit(1)

if __name__ == "__main__":
    main()
