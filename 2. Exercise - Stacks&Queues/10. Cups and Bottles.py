
from collections import deque

cups = deque([int(el) for el in input().split()])

bottles_as_stack = [int(el) for el in input().split()]

wasted_water = 0
while bottles_as_stack:
    current_litters = bottles_as_stack[-1]
    if not  cups:
        print(f"Bottles: {' '.join([str(el) for el in bottles_as_stack])}")
        print(f"Wasted litters of water: {wasted_water}")
    # here we remove filled cup
    if cups[0] < current_litters:
        wasted_water += (bottles_as_stack.pop() - cups.popleft())

    else:
        while cups[0] > current_litters:
            cups[0] -= current_litters
            bottles_as_stack.pop()
            current_litters = bottles_as_stack.pop()
        wasted_water += current_litters

print()
