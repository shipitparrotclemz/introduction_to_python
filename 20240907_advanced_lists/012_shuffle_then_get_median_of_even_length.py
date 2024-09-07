"""
Now 1, 2.. to 100

shuffle it

sort it

then get median

but, your median is (item at index 49 + item at index 50) / 2
"""
import random

my_list: list[int] = [num for num in range(1, 101)]
random.shuffle(my_list)
my_list.sort()
length_of_list: int = len(my_list)
right_index: int = length_of_list // 2
left_index: int = right_index - 1
right_item: int = my_list[right_index]
left_item: int = my_list[left_index]
median_of_list: float = (right_item + left_item) / 2
print(median_of_list)