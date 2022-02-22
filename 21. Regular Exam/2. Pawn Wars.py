
n = 8
chess_board = []
row_dict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
for row in range(n):
    row_data = input().split(" ")
    if "w" in row_data:
        white_row_pos, white_col_pos = row, row_data.index("w")
    elif "b" in row_data:
        black_row_pos, black_col_pos = row, row_data.index("b")
    chess_board.append(row_data)

for _ in range(n):
    if white_row_pos == 0:
        letter = white_col_pos
        row_pos = 8 - white_row_pos
        if letter in row_dict.keys():
           letter = (row_dict[letter])
        print(f"Game over! White pawn is promoted to a queen at {letter + str(row_pos)}.")
        break
    try:
        if chess_board[white_row_pos - 1][white_col_pos - 1] == "b":
            last_post = [white_row_pos - 1, white_col_pos - 1]
            letter = last_post[1]
            row_pos = 8 - white_row_pos
            if letter in row_dict.keys():
                letter = (row_dict[letter])
            print(f"Game over! White win, capture on {letter + str(row_pos)}.")
            break
        elif chess_board[white_row_pos - 1][white_col_pos + 1] == "b":
            last_post = chess_board[white_row_pos - 1][white_col_pos - 1]
            letter = last_post[1]
            row_pos = 8 - white_row_pos
            if letter in row_dict.keys():
                letter = (row_dict[letter])
            print(f"Game over! White win, capture on {letter + str(row_pos)}.")
            break
        elif chess_board[white_row_pos + 1][white_col_pos - 1] == "b":
            last_post = chess_board[white_row_pos - 1][white_col_pos - 1]
            letter = last_post[1]
            row_pos = 8 - white_row_pos
            if letter in row_dict.keys():
                letter = (row_dict[letter])
            print(f"Game over! White win, capture on {letter + str(row_pos)}.")
            break
        elif chess_board[white_row_pos + 1][white_col_pos + 1] == "b":
            last_post = chess_board[white_row_pos - 1][white_col_pos - 1]
            letter = last_post[1]
            row_pos = 8 - white_row_pos
            if letter in row_dict.keys():
                letter = (row_dict[letter])
            print(f"Game over! White win, capture on {letter + str(row_pos)}.")
            break
        else:
            new_white_row = white_row_pos - 1
            chess_board[white_row_pos][white_col_pos] = "-"
            white_row_pos = new_white_row
            chess_board[new_white_row][white_col_pos] = "w"
        if black_row_pos == 8:
            print("Game over! Black pawn is promoted to a queen at b8.")
            break
        if chess_board[black_row_pos - 1][black_col_pos - 1] == "b":
            last_post = chess_board[black_row_pos - 1][black_col_pos - 1]
            print(f"Game over! Black win, capture on a3.")
            break
        elif chess_board[black_row_pos - 1][black_col_pos + 1] == "b":
            last_post = chess_board[black_row_pos - 1][black_col_pos - 1]
            print(f"Game over! Black win, capture on a3.")
            break
        elif chess_board[black_row_pos + 1][black_col_pos - 1] == "b":
            last_post = chess_board[black_row_pos - 1][black_col_pos - 1]
            print(f"Game over! Black win, capture on a3.")
            break
        elif chess_board[black_row_pos + 1][black_col_pos + 1] == "b":
            last_post = chess_board[black_row_pos - 1][black_col_pos - 1]
            print(f"Game over! Black win, capture on a3.")
            break
        else:
            new_black_row = black_col_pos + 1
            chess_board[black_row_pos][black_col_pos] = "-"
            black_row_pos = new_black_row
            chess_board[black_row_pos][black_col_pos] = "b"

    except IndexError:
        continue


#
# rows, cols = 8, 8
#
# board = []
# white = ''
# black = ''
# winner = False
#
# for row in range(rows):
#     line = [el for el in input().split(' ')]
#     board.append(line)
#     if 'w' in line:
#         white = [row,line.index('w')]
#     if 'b' in line:
#         black = [row, line.index('b')]
#
# coor_board = []
#
# for row in range(8):
#     coor_board.append([f'' for el in range(8)])
#     for col in range(8):
#         coor_board[row][col] = f'{chr(97+col)}{8-row}'
#
# while not winner:
#     if white[0]-black[0]==1:
#         if white[1]-black[1]==1 or black[1]-white[1]==1:
#             winner = True
#             print(f'Game over! White win, capture on {coor_board[black[0]][black[1]]}.')
#             break
#     white[0]-=1
#     if white[0]==0:
#         winner = True
#         print(f'Game over! White pawn is promoted to a queen at {coor_board[white[0]][white[1]]}.')
#         break
#     if black[0]-white[0]==-1:
#         if black[1]-white[1]==1 or white[1]-black[1]==1:
#             winner = True
#             print(f'Game over! Black win, capture on {coor_board[white[0]][white[1]]}.')
#             break
#     black[0]+=1
#     if black[0]==7:
#         winner = True
#         print(f'Game over! Black pawn is promoted to a queen at {coor_board[black[0]][black[1]]}.')
#         break
