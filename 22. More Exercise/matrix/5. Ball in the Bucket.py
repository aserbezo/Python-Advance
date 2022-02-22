def sum_column(ma, col):
    points = 0
    for row_idx in range(len(ma)):
        if ma[row_idx][col] != "B":
            points += int(ma[row_idx][col])
    return points

n = 6
throws_count = 3
# for this bellow the comprehenshion
# matrix = []
# for _ in range(n):
#     matrix.append(input().split())

matrix = [input().split() for _ in range(n)]
total_points = 0
for _ in range(throws_count):
    # row,col = [int(x) for x in eval(input())]

    data = input()
    data = data[1:len(data) - 1].split(", ")
    row = int(data[0])
    col = int(data[1])
# ako e izvun index sa shte vlezne v except statment
    try:
        if matrix[row][col] == "B":
           # ussing a fucntion
           #total_points += sum_column(matrix, col)
           total_points += sum([int(matrix[row_idx][col])for row_idx in range(n) if matrix[row_idx][col].isdigit()])
           matrix[row][col] = "0"
    except IndexError:
        continue

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
elif 100 <= total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")

