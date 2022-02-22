from statistics import mean
# count = int(input())
# students = {}
#
# for _ in range(count):
#     line = tuple(input().split())
#     student,grade = line
#     if student not in students:
#         students[student] = []
#     students[student].append(float(grade))
#
#
#
# for key ,value in students.items():
#     print(f"{key} -> {''.join(str(value))}")
#


n = int(input())

grades = {}

for _ in range(n):
    name,grade_as_string =input().split()
    grade = float(grade_as_string)
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for data in grades.items():
    print(f"{data[0]} -> {' '.join(f'{el:.2f}' for el in data[1])} (avg: {mean(data[1]):.2f}) ")
