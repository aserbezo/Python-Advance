
def operate(sigh,*args):
    if sigh in ("+", "-"):
        result = 0

    else:
        result = 1

    if sigh == "+":
        for el in args:
            result += el
    elif sigh == "-":
        for el in args:
            result -= el

    elif sigh == "*":
        for el in args:
            result *= el

    elif sigh == "/":
        for el in args:
            if el == 0:
                continue
            else:
                result /= el

    return result

print(operate("+", 1, 2, 3))
