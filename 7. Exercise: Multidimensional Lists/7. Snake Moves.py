

rows,cols = [int(x) for x in input().split()]

word = input()

idx = 0

matrix = []

for row in range(rows):
    row_element = []
    for col in range(cols):
        row_element.append(word[idx % len(word)])
        idx += 1
    if row % 2 == 0:
        print(*row_element, sep="")
    else:
        print(*reversed(row_element), sep="")
