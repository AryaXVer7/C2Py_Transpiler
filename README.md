# C2Py_Transpiler_Version_1

A beginner-friendly C to Python transpiler written in Python.

This project is part of my compiler development journey. The goal is to learn how real compilers work by building one from scratch, step by step.

Instead of translating the entire C language, this project starts with a very small subset of C and gradually adds new features in each version.

Current version: **v1**

---

## Features

### Supported Data Types

- `int`
- `char`

### Supported Statements

Variable declarations with initialization.

Example:

```c
int age = 20;
char grade = 'A';
```

Generated Python:

```python
age = 20
grade = 'A'
```

---

## Compiler Pipeline

The transpiler follows the basic structure used in real compilers:

```text
Source Code
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
Python Code
```

---

## Project Structure

```text
C2Py-Compiler/
│
├── lexer.py
├── parser.py
├── codeGenerator.py
├── main.py
│
├── README.md
└── .gitignore
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

### Input

```c
int age = 20;
```

### Tokens

```python
[
    ('INT', 'int'),
    ('IDENTIFIER', 'age'),
    ('EQUALS', '='),
    ('NUMBER', '20'),
    ('SEMICOLON', ';')
]
```

### AST

```python
{
    "node_type": "VariableDeclaration",
    "var_type": "int",
    "name": "age",
    "value": "20"
}
```

### Generated Python

```python
age = 20
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AryaXVer7/C2Py_Transpiler_Version_0.1.git
```

Move into the project directory:

```bash
cd C2Py_Transpiler_Version_0.1
```

Run:

```bash
python main.py
```

---

## Current Limitations

This project currently supports only:

- Single variable declarations
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

## Sample Output

Input:

```c
char alphabet = 'A';
```

Output:

```python
alphabet = A
```
---

## Contributing

Suggestions, bug reports, and pull requests are welcome.

If you are learning compilers too, feel free to fork the project and experiment with new features.

---

## Author

Built as a personal compiler-learning project.

GitHub: https://github.com/AryaXVer7
