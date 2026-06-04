from lexer import tokenizer
from parser import parser
from codeGenerator import generate

with open("input.c", "r") as file:
    source_code = file.read()
    
lines = source_code.splitlines()

filtered_code = []

for line in lines:
    if not line.startswith("#"):
        filtered_code.append(line)

source_code = "\n".join(filtered_code)

Token_Created = tokenizer(source_code)
ast = parser(Token_Created)
python_code_generate = generate(ast)

with open("python_code.py", "w") as file:
    file.write(python_code_generate)

print("Python file generated as python_code.py")