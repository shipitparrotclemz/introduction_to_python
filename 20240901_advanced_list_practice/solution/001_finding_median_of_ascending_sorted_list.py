# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#              ^  ^
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#              ^
# Union only for python 3.9 and below
from typing import Union

my_list: list[int] = [i for i in range(1, 10)]

length_of_list: int = len(my_list)  # 10
list_is_even: bool = length_of_list % 2 == 0

# simplicity: assume list is guaranteed to have at least 1 number

median: int | float # | is a shortcut for Union, available from python3.10

if list_is_even:
    # solution for even length is here
    center_right_index: int = length_of_list // 2   # index 5, points at 6
    center_left_index: int = center_right_index - 1 # index 4, points at 5
    center_right: int = my_list[center_right_index] # my_list[5], 6
    center_left: int = my_list[center_left_index]   # my_list[4], 5
    median = (center_right + center_left) / 2
else:
    # solution for odd length is here
    center_index: int = length_of_list // 2  # 9 // 2 = 4.5 -> 4
    median = my_list[center_index]

# Test Case 1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# median = 5.5
# Test Case 2: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# median = 5
print(median)