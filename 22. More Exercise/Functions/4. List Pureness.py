from collections import deque


def best_list_pureness(*args):
    numbers, rotations = args
    numbers = deque(numbers)
    dict_pure = {}
    for k in range(rotations):
        if k == len(numbers):
            break
        pure = sum([i * n for i, n in enumerate(numbers)])
        if pure not in dict_pure:
            dict_pure[pure] = k
        numbers.rotate()
    return f"Best pureness {max(dict_pure)} after {dict_pure[max(dict_pure)]} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
