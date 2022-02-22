# Read an input with a name and add it to a queue until "End"
# If you receive "Paid", print every customer and empty the queue
# When you receive "End" print the remaining people in the format: "{count} people remaining.

from collections import deque

queue = deque()

while True:
    command = input()
    if command == "Paid":
        while len(queue):
            print(queue.popleft())
    elif command == "End":
        print(f"{len(queue)} people remaining. ")
        break
    else:
        queue.append(command)

