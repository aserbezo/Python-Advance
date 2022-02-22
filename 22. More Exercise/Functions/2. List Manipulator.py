def list_manipulator(lists, *args):
    lists = lists
    first_com, secomd_com, *numbers = args

    if first_com == "add":
        if secomd_com == "beginning":
            return numbers + lists
        elif secomd_com == "end":
            return lists + numbers
    elif first_com == "remove":
        if secomd_com == "beginning":
            if numbers:
                return lists[numbers[0]:]
            else:
                return lists[1:]
        elif secomd_com == "end":
            if numbers:
                return lists[: - numbers[0]]
            else:
                return lists[:-1]



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
