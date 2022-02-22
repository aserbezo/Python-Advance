import math
size = int(input())

matrix = []
p_row = 0
p_col = 0
coins = 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'P':
            p_row = row
            p_col = col


def next_position(command, row, col, size):
    if command == 'left':
        return row, col - 1
    elif command == 'right':
        return row, col + 1
    elif command == 'up':
        return row - 1, col
    elif command == 'down':
        return row + 1, col


path = [[p_row, p_col]]

while coins < 100:

    command = input()
    if command in ['left', 'right', 'up', 'down']:
        next_row, next_col = next_position(command, p_row, p_col, size)
    else:
        continue

    if next_row < 0:
        next_row = size + next_row
    if next_col < 0:
        next_col = size + next_col
    if next_row == size:
        next_row = 0
    if next_col == size:
        next_col = 0

    if matrix[next_row][next_col] == 'X':
        path.append([next_row, next_col])
        break
    else:
        coins += int(matrix[next_row][next_col])

    matrix[p_row][p_col] = 0

    matrix[next_row][next_col] = 'P'

    p_row, p_col = next_row, next_col
    path.append([p_row, p_col])

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {math.floor(coins/2)} coins.")
print('Your path:')
for i in path:
    print(i)
