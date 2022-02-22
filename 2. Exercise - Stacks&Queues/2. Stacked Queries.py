

stack = []

number = int(input())

for i in range(number):
    number_check = input().split()
    if number_check[0] == "1":
        stack.append(int(number_check[1]))
    elif number_check[0] == "2":
        if len(stack) == 0:
            continue
        stack.pop()
    elif number_check[0] == "3":
        print(max(stack))
    elif number_check[0] == "4":
        print(min(stack))

stack.reverse()
print(*stack, sep=", ")
