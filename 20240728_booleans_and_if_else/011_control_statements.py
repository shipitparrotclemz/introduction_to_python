"""
Problem Statement:
Friends are losing weight

But we need to call out culprits who ate mala today

Define 4 bools
elson_fucked_up: bool = True
clement_fucked_up: bool = True
gabriel_fucked_up: bool = True
weixuan_fucked_up: bool = True

If elson fucked up:
    print("Elson fucked up")
If clement fucked up:
    print("Clement fucked up")
If gabriel fucked up:
    print("Gabriel fucked up")
If weixuan fucked up:
    print("Wei Xuan fucked up")

If elson and clement fucked up
    print("Elson and Clement fucked up")
If elson and weixuan and gabriel fucked up
    print("Elson and Weixuan and Gabriel fucked up")
If elson and clement and gabriel and weixuan fucked up
    print("All fucked up")

New: Creating a new data structure: list[str]
"""

elson_fucked_up: bool = False
clement_fucked_up: bool = True
gabriel_fucked_up: bool = True
weixuan_fucked_up: bool = True
# contain the names for those who fucked up
list_of_fuck_ups: list[str] = []

# if <bool>:
# if <bool> is True, then execute this
if elson_fucked_up:
    # new concept: use .append() on the list, to add a new item to the list
    list_of_fuck_ups.append("Elson")  # list_of_fuck_ups = ["Elson"]
if clement_fucked_up:
    list_of_fuck_ups.append("Clement")
if gabriel_fucked_up:
    list_of_fuck_ups.append("Gabriel")
if weixuan_fucked_up:
    list_of_fuck_ups.append("Weixuan")

if len(list_of_fuck_ups) == 4:  # True
    print("All fucked up")
# elif will be called if the above statement was not executed
elif len(list_of_fuck_ups) > 0:
    # NEW CONCEPT: you can put items between strings in a list with .join
    # <string_to_put_between_items>.join(list_of_string)
    # weixuan and aaron
    my_string = " and ".join(list_of_fuck_ups)
    print(my_string + " fucked up")
