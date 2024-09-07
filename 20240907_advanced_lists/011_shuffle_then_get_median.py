"""
generate a list

[1, 2, 3... 99]

shuffle it

then, you sort it

then you find median of it
"""
import random

my_list: list[int] = [num for num in range(1, 100)]
random.shuffle(my_list)
my_list.sort()
length_of_list: int = len(my_list)
index_of_list: int = length_of_list // 2
item_of_list: int = my_list[index_of_list]
print(item_of_list)