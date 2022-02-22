
n = int(input())
# ako definirame prazen set izpozlvame set()
cars = set()
for _ in range(n):
    direction , car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if cars:
    print('\n'.join(cars))
else:
    print("Parking Lot is Empty")
