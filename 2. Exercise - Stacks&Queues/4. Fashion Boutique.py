
clothes = list(input().split())

rack = int(input())
rack_count = 0
counter = 0
while len(clothes) != 0:
    n = int(clothes.pop())
    counter += n
    if len(clothes) == 1:
        rack_count += 1
    elif counter > rack:
        clothes.append(n)
        rack_count += 1
        counter = 0
    elif counter == rack:
        rack_count += 1
        counter = 0

print(rack_count)

