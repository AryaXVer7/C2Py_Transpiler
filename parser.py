def parser(token):
    ast = []
    
    i = 0
    
    while i < len(token):
        variable_node = {"node_type" : "VariableDeclaration",
                "var_type" : token[i][1],
                "name" : token[i+1][1],
                "value" : token[i+3][1]
            }
        ast.append(variable_node)
        i += 5
        
    return ast