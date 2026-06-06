# C2Py_Transpiler

A beginner-friendly C-to-Python transpiler written in Python.

This project is part of my compiler development journey. The goal is to learn how real compilers work by building one from scratch, step by step.

Instead of translating the entire C language, this project starts with a very small subset of C and gradually adds new features in each version.

**Current Version: **v3**

---

## Features

### Supported Data Types

* `int`
* `char`

### Supported Statements

* Variable declarations with initialization
* Multiple variable declarations
* Binary addition expressions

### Supported Operators

* `+`

Example:

```c
int age = 20;
char grade = 'A';

int sum = 5 + 3;
```

Generated Python:

```python
age = 20
grade = 'A'
sum = 5 + 3
```

---

## File-Based Transpilation

The transpiler:

1. Reads C source code from `input.c`
2. Tokenizes the source code
3. Builds an Abstract Syntax Tree (AST)
4. Generates equivalent Python code
5. Writes the result to `output.py`

---

## Compiler Pipeline

```text
input.c (source code)
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
output.py
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
├── output.py
│
└── README.md
```

---

## Example

### Input (input.c)

```c
int a = 1;
int b = 2;

char c = 'C';
char d = 'D';

int sum = 5 + 3;
int total = 10 + 4;
```

### Generated Output (output.py)

```python
a = 1
b = 2

c = 'C'
d = 'D'

sum = 5 + 3
total = 10 + 4
```

---

## Version History

### v1

Features:

* Integer declarations
* Character declarations
* Integer literals
* Character literals
* Lexer implementation
* Parser implementation
* AST generation
* Python code generation

---

### v2

New Features:

* Multiple variable declarations
* Read source code from `input.c`
* Generate Python output files
* Ignore preprocessor directives such as `#include`
* Improved AST handling

---

### v3

New Features:

* Binary expression support
* Addition operator (`+`)
* BinaryExpression AST nodes
* Python code generation for arithmetic expressions

Example:

```c
int result = 5 + 3;
```

Output:

```python
result = 5 + 3
```

---

## Current Limitations

Currently supported:

* int declarations
* char declarations
* integer literals
* character literals
* multiple declarations
* addition expressions

Not yet supported:

* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Parentheses
* Strings
* Functions
* Loops
* Conditionals
* Arrays
* Structs
* Pointers

---

## Learning Objectives

This project is being built to learn:

* Lexical Analysis
* Parsing
* Abstract Syntax Trees (ASTs)
* Expression Parsing
* Code Generation
* Compiler Architecture
* Language Design
* Python Implementation Techniques

---

## Contributing

Suggestions, bug reports, and pull requests are welcome.

If you are learning compilers too, feel free to fork the project and experiment with new features.

---

## Author

Built as a personal transpiler-learning project.

GitHub: https://github.com/AryaXVer7


