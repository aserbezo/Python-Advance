def is_outside(ma, row, col):

    return row not in range(len(ma)) or col not in range(len(ma))


n = int(input())

matrix = []
snake_pos = []
lair_pos = []
game_over = True
for row in range(n):
    row_data = list(input())
    if "S" in row_data:
        snake_pos = [row, row_data.index("S")]
    if "B" in row_data:
        lair_pos.append([row, row_data.index("B")])
    matrix.append(row_data)

food_qty = 0

while True:
    command = input()
    next_row = 0
    next_col = 0
    curr_row = snake_pos[0]
    curr_col = snake_pos[1]
    if command == "left":
        next_row = curr_row
        next_col = curr_col - 1
    elif command == "down":
        next_row = curr_row + 1
        next_col = curr_col
    elif command == "up":
        next_row = curr_row - 1
        next_col = curr_col
    elif command == "right":
        next_row = curr_row
        next_col = curr_col + 1

    if is_outside(matrix, next_row, next_col):
        matrix[curr_row][curr_col] = "."
        game_over = True
        break
    new_position = matrix[next_row][next_col]
    if new_position == "*":
        matrix[next_row][next_col] = "S"
        matrix[curr_row][curr_col] = "."
        snake_pos = [next_row, next_col]
        food_qty += 1
        if food_qty == 10:
            game_over = False
            break
    elif new_position == "B":
        matrix[next_row][next_col] = "."
        matrix[curr_row][curr_col] = "."
        lair_pos.remove([next_row, next_col])
        snake_pos = [lair_pos[0][0], lair_pos[0][1]]
        matrix[snake_pos[0]][snake_pos[1]] = "S"

    else:
        matrix[next_row][next_col] = "S"
        matrix[curr_row][curr_col] = "."
        snake_pos = [next_row, next_col]

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_qty}")
[print("".join(x)) for x in matrix]

