from lexer import tokenizer
from parser import parser
from codeGenerator import generate

source_code = "char alphabet = 'A';"

token = tokenizer(source_code)
parser = parser(token)
generate = generate(parser)

print(f"Python Code: {generate}")