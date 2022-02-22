def fill_the_box(heigh,lenght,width, *args):
    volume = heigh * lenght * width
    cubs_left = 0
    for el in args:
        if el == "Finish":
            break
        if el > volume:
            el -= volume
            cubs_left += el
            volume = 0
        else:
            volume -= el

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."

    else:
        return f"No more free space! You have {cubs_left} more cubes."





print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
