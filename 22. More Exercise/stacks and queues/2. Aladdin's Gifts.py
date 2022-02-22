from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}
while materials and magic_level:
    material = materials[-1]
    magic = magic_level[0]
    result = material + magic
    if result < 100:
        if result % 2 == 0:
            material = material * 2
            magic = magic * 3
            result = material + magic
        else:
            result = result * 2
    elif result > 499:
        result = result / 2

    if 100 <= result <= 199:
        gifts["Gemstone"] += 1
        materials.pop()
        magic_level.popleft()
    elif 200 <= result <= 299:
        gifts["Porcelain Sculpture"] += 1
        materials.pop()
        magic_level.popleft()
    elif 300 <= result <= 399:
        gifts["Gold"] += 1
        materials.pop()
        magic_level.popleft()
    elif 400 <= result <= 499:
        gifts["Diamond Jewellery"] += 1
        materials.pop()
        magic_level.popleft()
    else:
        materials.pop()
        magic_level.popleft()

if gifts["Gemstone"] and gifts["Porcelain Sculpture"] > 0 or gifts["Gold"] and gifts["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key , value in sorted(gifts.items()):
    if value > 0:
        print(f"{key}: {value}")
