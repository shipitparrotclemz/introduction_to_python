my_list: list[int] = [num for num in range(1, 101)]
length_of_list: int = len(my_list)
num_of_index: int = length_of_list // 100
index_sevenfive: int = num_of_index * 75 - 1
item_of_list: int = my_list[index_sevenfive]
print(item_of_list)
