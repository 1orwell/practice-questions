def caeser(message, shift):
    orders = list(map(ord, message))
    print(orders)
    new_orders = list(map(lambda x: x+shift, orders))
    for i, val in enumerate(new_orders):
        if val>122:
            new_orders[i] = val-26
    return list(map(chr, new_orders))

# need to fix issue with spaces
print(caeser("abcd xyz", 4))
