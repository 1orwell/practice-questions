def caeser(message, shift):
    orders = list(map(ord, message))
    new_orders = list(map(lambda x: x+shift, orders))
    #make loop back if go past z
    for i, val in enumerate(new_orders):
        if val>122:
            new_orders[i] = val-26
    return list(map(chr, new_orders))

def caeser2(message, shift):
    #create string of all lowercase ascii characters from a to z
    letters = string.ascii_lowercase
    #e.g. letters[3:] = def...z
    # e.g. letters[:3] = ab
    # creates new string, e.g. def...zabc
    mask = letters[shift:] + letters[:shift]
    # matches each value in letters to the corresponding value in mask
    trantab = str.maketrans(letters, mask)
    # applies above translation to the message
    return message.translate(trantab)

# need to fix issue with spaces
print(caeser("abcd xyz", 4))
