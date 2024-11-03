"""
instead of [1, 2, 3..., 100]

[2, 4, 6, ... 200]
"""

my_list: list[int] = []
for num in range(1, 101):
    my_list.append(num * 2)
print(my_list)
