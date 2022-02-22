def get_magic_triangle(args):
    result = []
    x = [1]
    y = [0]
    for _ in range(args):
        result.append(x)
        x = [i+j for i, j in zip(x+y, y+x)]
    return result


print(get_magic_triangle(5))
