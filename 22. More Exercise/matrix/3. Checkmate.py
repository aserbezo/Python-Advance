
n = 8
chess_board = []

for row in range(n):
    row_data = input().split(" ")
    if "K" in row_data:
        row_k ,col_k = row, row_data.index("K")
    chess_board.append(row_data)

directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
hit_queens = []

for i in range(1,n + 1):
    out_direction = []
    for el in directions:
        nex_row, nex_col = el
        qu_row = nex_row * i + row_k
        qu_col = nex_col * i + col_k
        if 0 <= qu_row < n and 0 <= qu_col < n:
            if chess_board[qu_row][qu_col] == "Q":
                hit_queens.append([qu_row, qu_col])
                out_direction.append([nex_row, nex_col])

        else:
            out_direction.append([nex_row,nex_col])
    for dir in out_direction:
        directions.remove(dir)

    if not directions:
        break

if hit_queens:
    print(*hit_queens,sep="\n")
else:
    print("The king is safe!")
