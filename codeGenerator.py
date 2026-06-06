def generate(ast):
    output = []
    
    for node in ast:
        if isinstance(node["value"], dict):
            line = f"{node['name']} = {node['value']['left']} {node['value']['operator']} {node['value']['right']}"
            
        else:
            line = f"{node['name']} = {node['value']}"
            
        output.append(line)
        
    return "\n".join(output)