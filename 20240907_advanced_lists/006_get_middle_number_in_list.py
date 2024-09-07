my_list: list[int] = [num**2 for num in range(1,101)]

"""
get the middle number in the list

my_list is already sorted, so no need to sort
"""

# hint: get the middle index, assign it to middle_index: int

# hint: use the middle_index to get the middle item from my_list
# my_list[some_number]
# [0, 1, 2, 3, 4, 5, 6, 7]
#
length_of_list: int = len(my_list)
print(length_of_list)
right_index: int = length_of_list // 2
print(right_index)
left_index: int = right_index - 1
print(left_index)
left_index_of_list: int = my_list[left_index]
print(left_index_of_list)
right_index_of_list: int = my_list[right_index]
print(right_index_of_list)