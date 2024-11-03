# concept: list comprehension
my_sorted_list: list[int] = [num for num in range(1, 20001)]

# 75th percentile: 75 -> is at index 74, your list starts from 0

# concept: how to use len
length_of_list: int = len(my_sorted_list)

# concept: how to use // floor division
indexes_for_each_percentile: int = length_of_list // 100  # 100 // 100 = 1

# concept: how to use * and -
index_at_75: int = indexes_for_each_percentile * 75 - 1  # 1 * 75 - 1 = 74

# concept: how to get item at an index
number_at_75 = my_sorted_list[index_at_75]
print(number_at_75)
