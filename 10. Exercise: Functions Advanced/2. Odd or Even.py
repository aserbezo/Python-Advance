command = input()
numbers = [int(x) for x  in input().split()]



parity = 0 if command == "Even" else 1
result = sum([x for x in numbers if x % 2 == parity]) * len(numbers)
print(result)

# if command == "Even":
#     even = sum([x for x in numbers if x % 2 == 0]) * len(numbers)
#     print(even)
# else:
#     odd = sum([x for x in numbers if x % 2 == 1]) * len(numbers)
#     print(odd)
