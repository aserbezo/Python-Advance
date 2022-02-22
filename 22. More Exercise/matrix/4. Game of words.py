# function to check if imdex is in the matrix
def is_valid(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix)


# function for finding a player  in the Matrix
def find_player_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "P":
                return row, col


word = input()
size = int(input())
field = [[el for el in input()] for _ in range(size)]

player_pos = find_player_position(field)

number_of_commands = int(input())

for command in range(number_of_commands):
    next_player_pos = []
    row = player_pos[0]
    col = player_pos[1]
    command = input()
    if command == "up":
        next_player_pos = [row - 1,col]
    elif command == "down":
        next_player_pos = [row + 1,col]
    elif command == "left":
        next_player_pos = [row,col - 1]
    elif command == "right":
        next_player_pos = [row,col + 1]
    if is_valid(field, next_player_pos):
        if field[next_player_pos[0]][next_player_pos[1]] == "-":
           field[next_player_pos[0]][next_player_pos[1]] = "P"
           field[player_pos[0]][player_pos[1]] = "-"
           player_pos = next_player_pos
        else:
             word = word + field[next_player_pos[0]][next_player_pos[1]]
             field[player_pos[0]][player_pos[1]] = "-"
             field[next_player_pos[0]][next_player_pos[1]] = "P"
             player_pos = next_player_pos
    else:
        if len(word) > 0:
           word = word[:-1]

print(word)
print(*[''.join(el) for el in field], sep='\n')
