# ako kletkata e v matricata trqbva da proverim dali v kletkata ne e kon suzdava oshte edna pomohstna  fnckia is_knight
def is_knight(row,col,matrix):
    return matrix[row][col] == "K"

# pomoshtna funcia is_inside da proverim dali  dadenata kletka e validna
def is_inside(row,col,size):
    return 0 <= row < size and 0 <= col < size

# vsihki vuzmojni kletki za prowevka na dvijenieto na kon
def get_attacked_counter(row,col,matrix):
    result = 0
    # row , col
    # row -2 , col -1
    if is_inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2,col - 1, matrix):
        result += 1
    # row -2, col +1
    if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2,col + 1, matrix):
        result += 1
    # row -1,col -2
    if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1,col - 2, matrix):
        result += 1
    # row -1 , col +2
    if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1,col + 2, matrix):
        result += 1
    # row + 2, col -1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2,col - 1, matrix):
        result += 1
    # row + 2 , col + 1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2,col + 1, matrix):
        result += 1
    # row + 1 , col - 2
    if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1,col - 2, matrix):
        result += 1
    # row + 1 , col + 2
    if is_inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1,col + 2, matrix):
        result += 1

    return result




size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    table = {}

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "0":
                continue
            counter = get_attacked_counter(row,col,matrix)
            # tupple go izpolzvame kato kluch
            if counter:
                table[(row,col)] = counter

    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for coords , count in table.items():
        if count > best_counter:
            best_counter = count
            knight_row = coords[0]
            knight_col = coords[1]




    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)
