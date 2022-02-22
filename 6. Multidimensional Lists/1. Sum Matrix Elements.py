
rows , cols = [int(x) for x in input().split(", ")]

matrix = []
sums = 0
for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    sums += sum(lines)
    matrix.append(lines)
print(sums)
print(matrix)
