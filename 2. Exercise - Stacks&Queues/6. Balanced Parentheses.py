# parentheses = input()
# check = []
# pairs = {
#     '(': ')',
#     '{': '}',
#     '[': ']',
# }
# valid = True
#
# for el in parentheses:
#     if el in '([{':
#         check.append(el)
#     if check:
#         current_element = check[-1]
#         if el in ')}]':
#             if current_element == check[-1]:
#                 if pairs[current_element] == el:
#                     check.pop()
#                 else:
#                     valid = False
#                     break
#     else:
#         valid = False
#         break
#
# if valid:
#     print('YES')
# else:
#     print('NO')

cheked = input()

check_pairs = ["{}", "[]", "()"]
brackets = []
valid = True

for char in cheked:

    if char in "{[(":
        brackets.append(char)
    else:
        if not brackets:
            valid = False
            break
        else:
            balanced = brackets.pop() + char
            if balanced in check_pairs:
                continue
            else:
                valid = False
                break

if valid and not brackets:
    print("YES")
else:
    print("NO")
