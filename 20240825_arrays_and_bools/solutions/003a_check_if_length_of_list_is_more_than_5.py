"""
Create a list with 6 int

my_list: list[int] = [1,2,3,4,5,6]

Get the length of the list

if the length of the list is more than 5:
    print("The list contains more than 5 items!")
else:
    print("the list contains 5 or less items")
"""

my_list: list[int] = [1, 2, 3, 4, 5]
length_of_list: int = len(my_list)

if length_of_list > 5:
    print("The list contains more than 5 items!")
else:
    print("The list contains 5 or less items")
