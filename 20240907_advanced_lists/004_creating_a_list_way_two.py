"""
create a list with list-comprehension

but

[2, 4, 6..., 200]

hint

[num * 2 for num in range(1, 101]
"""

my_list: list[int] = [num * 2 for num in range(1, 101)]
print(my_list)
