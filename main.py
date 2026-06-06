from lexer import tokenizer
from parser import parser
from codeGenerator import generate

with open("input.c", "r") as file:
    source_code = file.read()
    
lines = source_code.splitlines()

filtered_lines = []

for line in lines:
    if not line.startswith("#"):
        filtered_lines.append(line)
        
source_code = "\n".join(filtered_lines)

Tokens = tokenizer(source_code)
ast = parser(Tokens)
python_code = generate(ast)

with open("output.py", "w") as file:
    file.write(python_code)

print("python file generated as output.py")