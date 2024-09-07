"""
Create a list containing 100 items

my_list: list[int] = [...]
"""

my_list: list[int] = []
for num in range(1, 101):
    my_list.append(num)
print(my_list)
