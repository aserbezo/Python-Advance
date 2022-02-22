from collections import deque

water_liters = int(input())

name = input()
line = deque()
while name != "Start":
    line.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        required_liters = int(command)
        name = line.popleft()
        if water_liters >= required_liters:
            water_liters -= required_liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    else:
        # _,  ne izpolzvana promenliva
        _, litters_to_fill = command.split()
        litters_to_fill = int(litters_to_fill)
        water_liters += litters_to_fill
    command = input()
print(f"{water_liters} liters left")
