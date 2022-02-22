def start_spring(**kwargs):
    output = {}
    output_string = ''
    for k, v in kwargs.items():
        if v not in output:
            output[v] = [k]
        else:
            output[v].append(k)
    for k, v in sorted(output.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        output_string += f'{k}:\n'
        for i in sorted(v):
            output_string += f'-{i}\n'
    return output_string

