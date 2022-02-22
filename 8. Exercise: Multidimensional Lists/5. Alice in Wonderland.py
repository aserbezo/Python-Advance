def get_next_position(direction,row, col):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


def is_outside(row: int, col: int, s: int):
    return row < 0 or col < 0 or row >= s or col >= s


n = int(input())
wonderland = []
alice_row, alice_col = 0, 0
tea_sum = 0

for row in range(n):
    row = input().split()
    wonderland.append(row)
    for col in range(n):
        if row[col] == 'A':
            alice_row = row
            alice_col = col

while True:
    direction = input()

    if not wonderland[alice_row][alice_col] == '*':
        wonderland[alice_row][alice_col] = '*'

    alice_row, alice_col = get_next_position(direction, alice_row, alice_col)

    if is_outside(alice_row, alice_col, n) or wonderland[alice_row][alice_col] == 'R':
        wonderland[alice_row][alice_col] = '*'
        print("Alice didn't make it to the tea party.")
        break

    if wonderland[alice_row][alice_col] not in ".*":
        tea_sum += int(wonderland[alice_row][alice_col])

    if tea_sum >= 10:
        wonderland[alice_row][alice_col] = '*'
        print("She did it! She went to the party.")
        break

for row in wonderland:
    print(*row, sep=' ')
