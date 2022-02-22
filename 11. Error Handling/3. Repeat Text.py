text = input()
while True:
    try:
        number_rep = int(input())
        break
    except ValueError:
        print("Variable times must be an integer")
string = ""
for _ in range(number_rep):
    string += text



print(string)
