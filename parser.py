def parser(tokens):
    ast = []
    
    i = 0
    
    while i < len(tokens):
        if tokens[i+4][0] == "PLUS":
            variable_node = {"node_type" : "VariableDeclaration",
                         "var_type" : tokens[i][1],
                         "name" : tokens[i+1][1],
                         "value" : {"node_type" : "BinaryExpression",
                                    "left" : tokens[i+3][1],
                                    "operator" : tokens[i+4][1],
                                    "right" : tokens[i+5][1]
                                    }
                         }
            i += 7
        
        else:
            variable_node = {"node_type" : "VariableDeclaration",
                         "var_type" : tokens[i][1],
                         "name" : tokens[i+1][1],
                         "value" : tokens[i+3][1]
                         }
            i += 5
        ast.append(variable_node)
        
    return ast