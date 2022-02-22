
file = open("numbers.txt" ,"r")
sum_num = 0
for line in file:
    sum_num += int(line)

print(sum_num)

