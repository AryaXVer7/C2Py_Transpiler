def parser(tokens):
	ast = {"node_type" : "VariableDeclaration",
		   "var_type" : tokens[0][1],
		   "name" : tokens[1][1],
		   "value" : tokens[3][1]
	}
	return ast