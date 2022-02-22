def numbers_searching(*args):
    min_numbers = min(args)
    max_numbers = max(args)
    missing = None
    duplicate = set()

    for num in range(min_numbers, max_numbers + 1):
        if num not in args:
             missing = num
        if args.count(num) > 1:
            duplicate.add(num)

    return [missing, list(sorted(duplicate))]





print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
