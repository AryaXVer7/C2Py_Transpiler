def generate(ast):
    output = []
    
    for node in ast:
        output.append(f"{node['name']} = {node['value']}")
        
    return "\n".join(output)