# Tokenization-Based Auto-Code Generation System

## Overview
This program is a **universal auto-code generation engine** that allows users to **create complete software programs** by utilizing **tokenization, spreadsheets, and multi-language code assembly**.

It is designed to work within **Termux, Linux, and cloud environments**, and it enables **AI-assisted program creation** by mapping different programming languages into **a unified tokenized format**.

---

## 🚀 Features
✅ **Multi-Language Tokenization & Detokenization** (Python, Go, JavaScript, C++, Rust, PHP, Swift)  
✅ **Spreadsheet-Driven Auto-Code Generation**  
✅ **Auto-Code Assembly (Multi-Language Software Creation)**  
✅ **Cloud Backup & GitHub Auto-Sync**  
✅ **Secure Keystore & Cryptographic Fingerprinting**  
✅ **Termux-Compatible for On-the-Go Development**  

---

## 📌 How It Works

### 1️⃣ Tokenization Process
- **Reads a source code file** (e.g., Python, JavaScript, etc.).
- **Identifies common keywords, functions, and structures**.
- **Replaces them with short tokens** for **compressed representation**.
- **Saves tokenized output as JSON**.

### 2️⃣ Spreadsheet-Based Auto-Code Generation
- Users **define a program’s functionality in a spreadsheet**.
- The spreadsheet **maps required features to tokenized components**.
- The engine **assembles code automatically** from tokenized language data.

### 3️⃣ Auto-Code Assembly (Multi-Language Support)
- **Reads spreadsheet design** and **fetches required tokens**.
- **De-tokenizes into complete, working source code**.
- **Supports single or multi-language software development**.

---

## 📌 Example: Tokenization

### 🚀 Original Python Code
```python
import os

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

print(read_file("data.txt"))
```

### 🎯 Tokenized Version
```json
{
    "tokens": ["I001", "F001", "L001", "IO01"]
}
```

### 🔄 De-Tokenized Version
```python
import os

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

print(read_file("data.txt"))
```

---

## 📌 Spreadsheet Format for Auto-Code Generation
| **Component**  | **Type**      | **Functionality** | **Language** | **Token Reference** |
|---------------|--------------|------------------|--------------|--------------------|
| User Input   | UI Element   | Accepts user text | Python, JS   | `INPUT01` |
| Database     | Storage      | Saves user data   | MySQL, PostgreSQL | `DB01` |
| Processing   | Function     | Computes result   | Python       | `F001` |
| Output       | UI Element   | Displays results  | HTML, JS     | `OUTPUT01` |

---

## 📌 NEGBT Prompt for Spreadsheet Creation

This AI prompt will allow **GPT models** to generate structured **spreadsheets** that serve as blueprints for the **Auto-Code program**.

### **Prompt for AI**
```
You are an advanced AI that assists in generating structured **spreadsheet-based program blueprints** for an **AI-powered code generation system**.
Generate a **CSV/Excel spreadsheet** that outlines the program structure based on user input.
Each row should represent a **functional component of the program** and map it to **predefined tokens** that the Auto-Code engine will recognize.

Example Output:
| Component | Type | Functionality | Language | Token Reference |
|-----------|------|--------------|----------|-----------------|
| API Endpoint | Backend API | Handle user requests | Python Flask | `API01` |
| Database Model | Storage | Store user data | MySQL | `DB01` |
| Authentication | Security | User login/logout | Python JWT | `AUTH01` |
| Response | Output | Send JSON responses | Python | `OUTPUT01` |

Output the spreadsheet in CSV or Excel format.
```
---

## 📌 How to Use
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/AIEINC/tokenizer-detokenizer.git
cd tokenizer-detokenizer
```

2️⃣ **Run Tokenization or De-Tokenization**
```bash
python tokenizer.py
```

3️⃣ **Use a Spreadsheet to Generate a Full Program**
- Create a **spreadsheet (CSV/Excel)** following the provided format.
- Run the Auto-Code program to generate working source code.

4️⃣ **Push Changes to GitHub**
```bash
git add .
git commit -m "Updated tokenization and auto-code generation system"
git push origin main
```

---

## 📌 Summary
🚀 **Write software using AI & tokenization**  
🚀 **Supports multiple programming languages**  
🚀 **Runs in Termux, Linux, and cloud environments**  
🚀 **Generates fully working programs from a spreadsheet**  
🚀 **Automatically stores & updates code in GitHub and cloud storage**  

---

## 📌 Future Enhancements
- ✅ **Add AI-powered program suggestions**  
- ✅ **Expand to support AI-driven unit testing**  
- ✅ **Integrate GPT for more advanced code generation**  
