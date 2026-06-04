# C2Py_Transpiler

A beginner-friendly C to Python transpiler written in Python.

This project is part of my compiler development journey. The goal is to learn how real compilers work by building one from scratch, step by step.

Instead of translating the entire C language, this project starts with a very small subset of C and gradually adds new features in each version.

Current version: **v2**

---

## Features

### Supported Data Types

- `int`
- `char`

### Supported Statements

Variable declarations with initialization.
Multiple variable declarations

Example:

```c
int age = 20;
char grade = 'A';
```

Generated Python:

```python
age = 20
grade = A
```

### File-Based Transpilation

The transpiler:

1. Reads C source code from `input.c`
2. Tokenizes the source code
3. Builds an Abstract Syntax Tree (AST)
4. Generates equivalent Python code
5. Writes the result to `python_code.py`

---
## Compiler Pipeline

The transpiler follows the basic structure used in real compilers:

```text
inout.c (source_code)
     │
     ▼
   Lexer
     │
     ▼
  Tokens
     │
     ▼
   Parser
     │
     ▼
    AST
     │
     ▼
Code Generator
     │
     ▼
python_code.py (output file)
```

---

## Project Structure

```text
C2Py_Transpiler/
│
├── lexer.py
├── parser.py
├── codeGenerator.py
├── main.py
│
├── input.c
├── python_code.py
│
└── README.md
```

### lexer.py

Converts source code into tokens.

Input:

```c
char grade = 'A';
```

Output:

```python
[
    ('CHAR', 'char'),
    ('IDENTIFIER', 'grade'),
    ('EQUALS', '='),
    ('CHAR_LITERAL', 'A'),
    ('SEMICOLON', ';')
]
```

---

### parser.py

Converts tokens into an Abstract Syntax Tree (AST).

Output:

```python
{
    "node_type": "VariableDeclaration",
    "var_type": "char",
    "name": "grade",
    "value": "A"
}
```

---

### codeGenerator.py

Converts the AST into Python code.

Output:

```python
grade = A
```

---

## Example

### Input (input.c)

```c
int a = 1;
int b = 2;
char c = 'C';
char d = 'D';
```

### Generated Output (python_code.py)

```python
a = 1
b = 2
c = C
d = D
```
---

## Installation

Clone the repository:

```bash
git clone https://github.com/AryaXVer7/C2Py_Transpiler.git
```

Move into the project directory:

```bash
cd C2Py_Transpiler
```

Run:

```bash
python main.py
```

---

## Current Limitations

This project currently supports only:

- Multiple variable declarations
- Integer literals
- Character literals
- `int`
- `char`

The following are **not supported yet**:

- Arithmetic expressions
- Strings
- Multiple declarations
- Functions
- Loops
- Conditionals
- Arrays
- Structs
- Pointers

---

## Learning Objectives

This project is being built to learn:

- Lexical Analysis
- Parsing
- Abstract Syntax Trees (ASTs)
- Code Generation
- Compiler Architecture
- Language Design
- Python Implementation Techniques

---

## Contributing

Suggestions, bug reports, and pull requests are welcome.

If you are learning compilers too, feel free to fork the project and experiment with new features.

---

## Author

Built as a personal transpiler-learning project.

GitHub: https://github.com/AryaXVer7

