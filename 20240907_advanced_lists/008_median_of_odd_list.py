"""
Create an odd-length list with list comprehension

[1, 2, ... 99]

median of odd length list is the item at the center

median index = 49
median = 50

get the median of the list
"""

my_list: list[int] = [num for num in range(1, 100)]
length_of_list: int = len(my_list)
index_of_list: int = length_of_list // 2
item_of_list: int = my_list[index_of_list]
print(item_of_list)
