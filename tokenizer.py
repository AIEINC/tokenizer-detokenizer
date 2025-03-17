import json
import re
import sys
import pandas as pd
import requests
import os

# IP owned by Joseph Lacroix

# Token Map for Multiple Languages
token_map = {
    "Python": {"import": "I001", "def": "F001", "for": "L001", "print": "IO01", "if": "C001", "var": "V001"},
    "Go": {"import": "I001", "func": "F001", "for": "L001", "fmt.Println": "IO01", "if": "C001", "var": "V001"},
    "JavaScript": {"import": "I001", "function": "F001", "for": "L001", "console.log": "IO01", "if": "C001", "let": "V001"},
    "C++": {"#include": "I001", "int main()": "F001", "for": "L001", "std::cout": "IO01", "if": "C001", "int": "V001"},
    "Rust": {"use": "I001", "fn main()": "F001", "for": "L001", "println!": "IO01", "if": "C001", "let": "V001"},
    "PHP": {"<?php": "I001", "function": "F001", "for": "L001", "echo": "IO01", "if": "C001", "$var": "V001"},
    "Swift": {"import": "I001", "func": "F001", "for": "L001", "print": "IO01", "if": "C001", "var": "V001"}
}

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

def generate_code_from_spreadsheet(file_path):
    df = pd.read_excel(file_path)
    code_output = ""

    for index, row in df.iterrows():
        language = row["Language"]
        component = row["Component"]
        token = row["Token"]

        if language in reverse_token_map and token in reverse_token_map[language]:
            code_output += reverse_token_map[language][token] + "\n"
        else:
            code_output += f"# UNKNOWN TOKEN: {token}\n"

    with open("generated_program.txt", "w") as f:
        f.write(code_output)

    print("✅ Code generated from spreadsheet and saved to generated_program.txt")

def upload_to_cloud(filename):
    print("🌐 Uploading file to Google Drive...")
    os.system(f"rclone copy {filename} gdrive:/Tokenizer-Backup/")
    print("✅ File successfully uploaded.")

def save_tokenized_output(tokens, output_file):
    with open(output_file, "w") as f:
        json.dump({"tokens": tokens}, f, indent=4)
    print(f"Tokenized output saved to {output_file}")
    upload_to_cloud(output_file)

def save_detokenized_output(detokenized_code, output_file):
    with open(output_file, "w") as f:
        f.write(detokenized_code)
    print(f"Detokenized code saved to {output_file}")
    upload_to_cloud(output_file)

def main():
    mode = input("Enter mode (tokenize/detokenize/spreadsheet): ").strip().lower()

    if mode == "spreadsheet":
        file_path = input("Enter the path to the spreadsheet file: ")
        generate_code_from_spreadsheet(file_path)
        return

    language = input("Enter programming language: ").strip()

    if mode == "tokenize":
        file_path = input("Enter the path to the source code file: ")
        with open(file_path, "r") as f:
            source_code = f.read()
        tokens = tokenize_code(source_code, language)
        save_tokenized_output(tokens, "tokenized_output.json")

    elif mode == "detokenize":
        file_path = input("Enter the path to the tokenized JSON file: ")
        with open(file_path, "r") as f:
            token_data = json.load(f)
        detokenized_code = detokenize_code(token_data.get("tokens", []), language)
        save_detokenized_output(detokenized_code, f"detokenized_output.{language.lower()}")

if __name__ == "__main__":
    main()
