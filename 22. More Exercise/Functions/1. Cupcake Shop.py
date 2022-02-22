def stock_availability(*args):
    stock = args[0]
    command = args[1]
    if command == "delivery":
        for i in args[2:]:
            stock.append(i)
    elif command == "sell":
        if len(args) == 2:
            stock.pop(0)
        elif len(args) > 2:
            if str(args[2]).isdigit():
                param = args[2]
                for i in range(param):
                    if stock:
                        stock.pop(0)
            else:
                lst = args[2:]
                for item in lst:
                    for i in range(len(stock)):
                        if stock[i] == item:
                            stock[i] == ""
    return [x for x in stock if x != '']


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
