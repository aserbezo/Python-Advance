from collections import deque as dq

pizza_orders = dq([int(i) for i in input().split(', ')])
employees = [int(i) for i in input().split(', ')]
total_pizza = 0
while pizza_orders and employees:
    order = pizza_orders[0]
    employee = employees[-1]
    if order > 10:
        pizza_orders.popleft()
        continue
    elif order <= 0:
        pizza_orders.popleft()
        continue
    if order <= employee:
        pizza_orders.popleft()
        total_pizza += order
    else:
        pizza_orders[0] = order - employee
        total_pizza += employee

    employees.pop()

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join(str(i) for i in employees)}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(i) for i in pizza_orders)}")
