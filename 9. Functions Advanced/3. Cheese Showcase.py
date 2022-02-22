def sorting_cheeses(**cheeses_dict):
    result = ""
    cheeses_dict = sorted(cheeses_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for tuple_ in cheeses_dict:
        result += tuple_[0] + "\n"
        quantity_list = sorted(tuple_[1], reverse=True)
        result += "\n".join(map(str, quantity_list))
        result += "\n"
    result = result.strip()

    return  result



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
