import json
import pandas as pd
import re
import os

# Token mappings for multiple languages
token_maps = {
    "Python": {
        "import": "I001", "def": "F001", "for": "L001", "while": "L002",
        "if": "C001", "elif": "C002", "else": "C003", "print": "IO001",
        "return": "RT001", "try": "E001", "except": "E002", "raise": "E003",
        "class": "O001", "self": "O002", "with": "R001", "open": "FS001",
        "read": "FS002", "write": "FS003", "append": "FS004", "int": "DT001",
        "float": "DT002", "str": "DT003", "list": "DT004", "dict": "DT005"
    },
    "JavaScript": {
        "function": "F001", "console.log": "IO001", "if": "C001", "else": "C003",
        "for": "L001", "while": "L002", "return": "RT001", "try": "E001",
        "catch": "E002", "throw": "E003", "class": "O001", "this": "O002",
        "let": "V001", "const": "V002", "var": "V003"
    },
    "Go": {
        "package": "I001", "func": "F001", "for": "L001", "if": "C001",
        "else": "C003", "return": "RT001", "defer": "R001", "import": "I002",
        "struct": "O001", "var": "V001", "const": "V002"
    },
    "C++": {
        "#include": "I001", "int main()": "F001", "std::cout": "IO001",
        "if": "C001", "else": "C003", "for": "L001", "while": "L002",
        "return": "RT001", "try": "E001", "catch": "E002", "throw": "E003",
        "class": "O001", "this": "O002", "int": "DT001", "float": "DT002",
        "string": "DT003", "vector": "DT004", "map": "DT005"
    }
}

# Reverse mapping for de-tokenization
reverse_token_maps = {lang: {v: k for k, v in token_map.items()} for lang, token_map in token_maps.items()}

def tokenize_code(source_code, language):
    """
    Converts source code into a tokenized format based on language.
    """
    if language not in token_maps:
        print(f"❌ Unsupported language: {language}")
        return []

    token_map = token_maps[language]
    lines = source_code.split("\n")
    tokenized_code = []

    for line in lines:
        line = line.strip()
        for keyword, token in token_map.items():
            if re.match(f"^{keyword}\\b", line):
                tokenized_code.append(token)
                break
        else:
            tokenized_code.append(line)  # Keep unknown lines as is

    return tokenized_code

def detokenize_code(token_list, language):
    """
    Converts tokenized code back into readable source code based on language.
    """
    if language not in reverse_token_maps:
        print(f"❌ Unsupported language: {language}")
        return ""

    detokenized_code = []
    
    for token in token_list:
        if token in reverse_token_maps[language]:
            detokenized_code.append(reverse_token_maps[language][token])
        else:
            detokenized_code.append(token)  # Keep unknown tokens as is
    
    return "\n".join(detokenized_code)

def generate_code_from_spreadsheet(file_path):
    """
    Reads a spreadsheet, extracts function definitions and mappings, 
    tokenizes them, and converts them into structured multi-language code.
    """
    df = pd.read_excel(file_path)
    generated_files = {}

    for index, row in df.iterrows():
        language = row.get("Language", "Python")  # Default to Python
        component = row.get("Component", "")
        token = row.get("Token", "")

        if language not in reverse_token_maps:
            continue

        if token in reverse_token_maps[language]:
            code_line = reverse_token_maps[language][token]
        else:
            code_line = f"# UNKNOWN TOKEN: {token}"

        if language not in generated_files:
            generated_files[language] = []

        generated_files[language].append(code_line)

    for lang, code_lines in generated_files.items():
        output_file = f"generated_code_{lang.lower()}.{lang.lower()}"
        with open(output_file, "w") as f:
            f.write("\n".join(code_lines))

        print(f"✅ Code for {lang} saved as {output_file}")

if __name__ == "__main__":
    mode = input("Enter mode (tokenize/detokenize/spreadsheet): ").strip().lower()

    if mode == "spreadsheet":
        file_path = input("Enter the path to the spreadsheet file: ")
        generate_code_from_spreadsheet(file_path)
    elif mode == "tokenize":
        language = input("Enter programming language: ").strip()
        file_path = input("Enter the path to the source code file: ")
        with open(file_path, "r") as f:
            source_code = f.read()
        tokens = tokenize_code(source_code, language)
        with open(f"tokenized_output_{language}.json", "w") as f:
            json.dump({"tokens": tokens}, f, indent=4)
        print(f"✅ Tokenized output saved as tokenized_output_{language}.json")
    elif mode == "detokenize":
        language = input("Enter programming language: ").strip()
        file_path = input("Enter the path to the tokenized JSON file: ")
        with open(file_path, "r") as f:
            token_data = json.load(f)
        detokenized_code = detokenize_code(token_data.get("tokens", []), language)
        with open(f"detokenized_output_{language}.{language.lower()}", "w") as f:
            f.write(detokenized_code)
        print(f"✅ De-tokenized output saved as detokenized_output_{language}.{language.lower()}")
