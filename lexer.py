def tokenizer(source):
	create_tokens = source.replace(";", " ;").replace("=", " = ").split()

	Tokens = []

	for token in create_tokens:
		if token == "int":
			Tokens.append(("INT", token))

		elif token == "char":
			Tokens.append(("CHAR", token))

		elif token == "=":
			Tokens.append(("EQUALS", token))

		elif token == ";":
			Tokens.append(("SEMICOLON", token))

		elif token.isdigit():
			Tokens.append(("NUMBER", token))

		elif len(token) == 3 and token[0] == "'" and token[2] == "'":
			Tokens.append(("CHAR_LITERAL", token[1]))

		else:
			Tokens.append(("IDENTIFIER", token))

	return Tokens