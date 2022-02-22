def even_odd(*args):
    command = args[-1]
    parity = 0 if command == "even" else 1
    return [x for x in args[0:len(args) - 1] if x  % 2 == parity]




print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
