from  collections import deque

def math_operations(*args,**kwargs):
    nums = deque(args)

    while nums:
        kwargs["a"] += nums.popleft()
        if not nums:
            break

        kwargs["s"] -= nums.popleft()
        if not nums:
            break

        divisor = nums.popleft()
        if divisor != 0:
            kwargs["d"] /= divisor

        if not nums:
            break

        kwargs["m"] *= nums.popleft()

    return kwargs




print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
