from collections import deque


pizza_orders = deque([int(x) for x in input().split(", ") if 0 < int(x) < 11])
employee = [int(x) for x in input().split(", ")]
is_finish = False
total_pizza_count = 0
while pizza_orders and employee:
    while pizza_orders[0] > employee[-1]:
        total_pizza_count += employee[-1]
        pizza_orders[0] = pizza_orders[0] - employee[-1]
        employee.pop()
        if not pizza_orders or not employee:
            is_finish =True
            break
    if is_finish:
        break
    total_pizza_count += pizza_orders.popleft()
    employee.pop()

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_count}")
    print(f"Employees: {', '.join([str(x) for x in employee])}")
