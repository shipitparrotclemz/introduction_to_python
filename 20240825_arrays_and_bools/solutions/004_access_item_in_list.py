"""
Create a list containing 7 names

my_list: list[str] = ["Gabriel", "Aaron", "Clement", "Xuan", "Vivienne", "Elson", "Eugene"]

Get Elson from list, print it

Hint: to get index of an item in a list

my_list.index("Elson")

Hint: index of items start from zero

Hint: to get item from list by index

To get Gabriel

my_list[0]
"""

my_list: list[str] = [
    "Gabriel",
    "Aaron",
    "Clement",
    "Xuan",
    "Vivienne",
    "Elson",
    "Eugene",
]
elson_index: int = my_list.index("Elson")
print(my_list[elson_index])
