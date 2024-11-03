"""
Task 1:

Create a list with 5 numbers

[5, 2, 6, 1, 3]

sort it in-place

hint: use .sort()

you should get

[1, 2, 3, 5, 6]
"""

my_list: list[int] = [5, 2, 6, 1, 3]
my_sorted_list: list[int] = sorted(my_list)
print(my_sorted_list)
print(my_list)
