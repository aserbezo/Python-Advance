n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

primary_diagonal = []
secondary_diagonal = []
for idx in range(n):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][n - 1 - idx])

prime = sum(primary_diagonal)
second = sum(secondary_diagonal)
print(f"{abs(prime - second )}")
