"""
Define a list of 10 items

["Elson", "Gabriel", "Aaron", "Xuan", "Zheng Yang", "Clement", "Weiyan", "Vivienne", "Eugene", "Ariel"]

Get the center index of the list: 5

Hint: use len(my_list) to get length of list

Hint: use // to get the floor division of a number

a floor division is the number after division, rounded down

9 // 2 = 4.5 -> 4
"""

my_list_of_names: list[str] = [
    "Elson",
    "Gabriel",
    "Aaron",
    "Xuan",
    "Zheng Yang",
    "Eugene",
    "Ariel",
    "Clement",
    "Vivienne",
    "Weiyan"
]
center_index: int = len(my_list_of_names) // 2
print(center_index)