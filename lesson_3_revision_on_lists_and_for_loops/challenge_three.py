"""
Challenge 3 Accessing an item by index in a List:

my_list: list[str] = ["Item 1", "Item 2", "Item 3"]
                        ^           ^       ^
                        0           1       2

Concept: Indexes (starts from 0 to length of list - 1)
- Index is an int that refers to an item in position
"Item 1" has an index of 0

Concept: We can access an item in a list by index
my_string: str = my_list[0] # "Item 1"
my_string_two: str = my_list[1] # "Item 2"
my_string_three: str = my_list[2] # "Item 3"
"""

"""
Challenge 3

Define a list[str] with 3 cakes

Tip: you can't put commas and spaces in variable names
"""
my_cakes: list[str] = ["Cheese Cake", "Wei Xuan's Cheese Cake", "Vivian's Favourite Cheese Cake"]
wei_xuan_cheese_cake: str = my_cakes[1]
print(my_cakes[1])
