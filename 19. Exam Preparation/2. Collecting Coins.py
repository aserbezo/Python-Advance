def calculate_pos(matrix , row, col):
    if row < 0 :
        row = len(matrix) - 1
    if col < 0:
        col = len(matrix) - 1
    if row >= len(matrix):
        row = 0
    if col >= len(matrix):
        col = 0

    return row,col

n = int(input())

matrix = []

player_pos = []
# here we are finding the position for the PLyaer
for row_ind in range(n):
   row_data = input().split()
   if "P" in row_data:
       player_pos = [row_ind, row_data.index("P")]
   matrix.append(row_data)

player_path = []

coins = 0
is_winner = True
player_path.append(player_pos)
while coins < 100:
    command = input()
    curr_row , curr_col = player_pos
    if command == "up":
        row,col = calculate_pos(matrix, curr_row - 1, curr_col)
    elif command == "down":
         row,col = calculate_pos(matrix, curr_row + 1, curr_col)
    elif command == "right":
         row,col = calculate_pos(matrix, curr_row , curr_col + 1)
    elif command == "left":
         row,col = calculate_pos(matrix, curr_row, curr_col - 1)

    matrix[curr_row][curr_col] = "0"
    if matrix[row][col] == "X":
        player_path.append([row,col])
        is_winner = False
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break
    coins += int(matrix[row][col])
    matrix[row][col] = "P"
    player_pos = [row, col]
    player_path.append(player_pos)

if is_winner:
    print(f"You won! You've collected {coins} coins.")
print(f"Your path:")
[print(x) for x in player_path]

