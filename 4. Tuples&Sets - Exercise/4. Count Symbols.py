line = input()
chars_count = {}

for ch in line:
    if ch in chars_count:
        chars_count[ch] += 1
    else:
        chars_count[ch] = 1

for key, value in sorted(chars_count.items()):
    print(f"{key}: {value} time/s")



