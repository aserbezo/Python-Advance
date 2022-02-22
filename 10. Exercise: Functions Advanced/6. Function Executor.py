



def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for funck_ref, funch_params in args:
        funk_result = funck_ref(*funch_params)
        result.append(funk_result)

    return result



print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
