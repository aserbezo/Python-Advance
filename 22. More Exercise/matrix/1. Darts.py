def is_inside(size, row, col):
    return 0 <= row < size and 0 <= col < size


def check_score(matrix, row, col):
    if is_inside(len(matrix), row, col):
        return matrix[row][col]
    return 0


def calculate_points(ma, row, col):
    counts = 0
    poss = matrix[row][col]
    # top
    counts += int(ma[0][col])
    # left
    counts += int(ma[row][0])
    # right
    counts += int(ma[row][6])
    # bottom
    counts += int(ma[6][col])

    return counts


player_one, player_two = [x for x in input().split(", ")]
dashboard = 7
matrix = []
for _ in range(dashboard):
    matrix.append([x for x in input().split()])

first_player_points = 501
second_player_points = 501
throw = 0
first_player_trow = 0
second_player_trow = 0
while True:
    coordinates = eval(input())
    row = coordinates[0]
    col = coordinates[1]
    throw += 1
    if throw % 2 == 1:
        first_player_trow += 1
    else:
        second_player_trow += 1

    check = check_score(matrix, row, col)
    if check == "B":
        if throw % 2 == 1:
            print(f"{player_one} won the game with {first_player_trow} throws!")
            break
        else:
            print(f"{player_two} won the game with {second_player_trow} throws!")
            break
    elif check == "D":
        points = calculate_points(matrix, row, col) * 2
    elif check == "T":
        points = calculate_points(matrix, row, col) * 3
    else:
        points = int(check)
    if throw % 2 == 1:
        first_player_points -= points
        if first_player_points <= 0:
            print(f"{player_one} won the game with {first_player_trow} throws!")
            break
    else:
        second_player_points -= points
        if second_player_points <= 0:
            print(f"{player_two} won the game with {second_player_trow} throws!")
            break
