from sys import maxsize
jobs = [int(x) for x in input().split(", ")]
index = int(input())


clock_cycles = 0
while True:
    min_num = min(jobs)
    if jobs.index(min_num) == index:
        clock_cycles += min_num
        break
    clock_cycles += min_num
    jobs[jobs.index(min_num)] = maxsize


print(clock_cycles)
