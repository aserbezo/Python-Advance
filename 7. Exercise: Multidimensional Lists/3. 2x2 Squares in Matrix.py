rows , column = [int(x) for x  in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

count = 0
# posledniq red ne go iskame da go dokasvame , zashtoto gi proverqva po kvadratcheta 2x2 , inacche shte ima error
for row in range(rows - 1):
    for col in range(column - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            count += 1

print(count)
