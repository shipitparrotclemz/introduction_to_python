"""
Create

[1, 4, 9, 16, 25... 10000]

hint:

to square a number

num**2, if num = 2, num**2 = 4
"""

my_list: list[int] = [num**2 for num in range(1, 101)]
print(my_list)
