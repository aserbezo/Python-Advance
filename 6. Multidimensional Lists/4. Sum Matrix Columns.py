rows_count , colums_count = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows_count):
    row = [int(x) for x in input().split()]
    matrix.append(row)

result = []

for colums_index in range(colums_count):
    column_sum = 0
    for row_index in range(rows_count):
        column_sum += matrix[row_index][colums_index]
    result.append(column_sum)

[print(x) for x in result]
