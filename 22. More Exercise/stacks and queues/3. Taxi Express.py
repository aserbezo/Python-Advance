from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for  x in input().split(", ")]

total_time = 0

while customers and taxis:
    cu_time = customers.popleft()

    taxi_time = taxis.pop()

    if cu_time <= taxi_time:
        total_time += cu_time
        continue
    customers.appendleft(cu_time)

if not  customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
