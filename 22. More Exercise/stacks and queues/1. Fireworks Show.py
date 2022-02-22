from collections import deque


def is_firework(craft):
    for count in craft.values():
        if count < 3:
            return False
    return True


fireworks_effect = deque([int(x) for x in input().split(", ") if int(x) > 0])
explosive_power = [int(x) for x in input().split(", ") if int(x) > 0]

firework_crafted = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while fireworks_effect and explosive_power:

    firework = fireworks_effect[0]
    explosive = explosive_power[-1]
    result = firework + explosive
    if result % 3 == 0 and result % 5 == 0:
        firework_crafted["Crossette Fireworks"] += 1
        fireworks_effect.popleft()
        explosive_power.pop()
    elif result % 3 == 0:
        firework_crafted["Palm Fireworks"] += 1
        fireworks_effect.popleft()
        explosive_power.pop()
    elif result % 5 == 0:
        firework_crafted["Willow Fireworks"] += 1
        fireworks_effect.popleft()
        explosive_power.pop()
    else:
        firework = fireworks_effect.popleft() - 1
        fireworks_effect.append(firework)

    if is_firework(firework_crafted):
        break

if is_firework(firework_crafted):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effect)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for key, value in firework_crafted.items():
    print(f"{key}: {value}")
