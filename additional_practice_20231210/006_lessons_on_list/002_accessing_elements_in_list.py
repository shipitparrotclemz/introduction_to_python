"""
## Challenge 2: Accessing Elements in a List
- Define a list object my_list containing integers 10, 20, 30, 40, 50
- Access and print the third element of my_list

Introduce the concept of an index -> the address of every item in the list

<list_variable>[<index>] -> index = 2

my_list[2]
"""

my_list: list[int] = [10, 20, 30, 40, 50]
third_element: int = my_list[2]
print(third_element)
