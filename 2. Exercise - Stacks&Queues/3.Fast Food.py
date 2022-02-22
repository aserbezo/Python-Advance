from collections import deque


quantity_of_food = int(input())
orders_quantity = deque(input().split())
integer_map = map(int,orders_quantity)
integer_list = list(integer_map)
max_order = max(integer_list)
for order in range(len(orders_quantity)):
    order = int(orders_quantity[0])
    if quantity_of_food - order >= 0:
        orders = orders_quantity.popleft()
        quantity_of_food -= int(orders)
    else:
        print(max_order)
        print(f"Orders left: {' '.join(orders_quantity)}")
        break
if len(orders_quantity) == 0:
    print(max_order)
    print("Orders complete")
