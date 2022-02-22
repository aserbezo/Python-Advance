
# numbers = (map(float,input().split()))
#
# result = {}
#
# for num in numbers:
#     if num not in result:
#         result[num] = 0
#
#     result[num] += 1
#
# [print(f"{key} - {value} times") for key, value in result.items()]

nums = (float(el) for el in input().split())
occ ={}
for num in nums:
    if num not in occ:
        occ[num] = 0
    occ[num] += 1

for key,value in occ.items():
    print(f"{key} - {value} times")

