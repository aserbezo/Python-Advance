
# proverka dali sme izvun matricata
def is_inside(row, col, size ):
    return 0 <= row < size and 0 <= col < size


def get_neighbour(row , col , matrix):
    size = len(matrix)
    neighb = []
    # vsichki susedi po teoriq
    # row - 1, col
    if is_inside(row -1, col, size) and matrix[row - 1][col] > 0:
        neighb.append([row - 1, col])
    # row + 1 , col
    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighb.append([row + 1, col])
    # row , col - 1
    if is_inside(row , col - 1, size) and matrix[row][col - 1] > 0:
        neighb.append([row , col -1])
    # row , col + 1
    if is_inside(row , col + 1, size) and matrix[row][col + 1] > 0:
        neighb.append([row , col +1])
    # row - 1, col - 1
    if is_inside(row -1 , col - 1, size) and matrix[row-1][col - 1] > 0:
        neighb.append([row - 1 , col -1])
    # row -1 , col + 1
    if is_inside(row -1, col + 1, size) and matrix[row-1][col + 1] > 0:
        neighb.append([row - 1, col + 1])
    # row + 1 , col - 1
    if is_inside(row +  1, col - 1, size) and matrix[row+1][col - 1] > 0:
        neighb.append([row + 1 , col -1])
    # row + 1 , col + 1
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighb.append([row + 1 , col +1])

    return neighb


n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])


bombs = input().split()


for bomb_coords in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb_coords.split(",")]
    if matrix[bomb_row][bomb_col] <= 0 :
        continue

    bomp_power = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0
    for row, col in get_neighbour(bomb_row,bomb_col,matrix):
        matrix[row][col] -= bomp_power

alive_cels = 0
alive_cels_sum = 0


for row in matrix:
    for el in row:
        if el > 0:
            alive_cels += 1
            alive_cels_sum += el


print(f"Alive cells: {alive_cels}")
print(f"Sum: {alive_cels_sum}")
for row in matrix:
    print(*row, sep = " ")



