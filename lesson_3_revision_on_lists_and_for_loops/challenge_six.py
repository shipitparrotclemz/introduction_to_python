"""
Challenge 6 is just Challenge 5 with for-loops and range
"""

my_list: list[int] = [1, 2, 3, 4, 5]

"""
Q: What is len?
len is a magic wand that gives the length of a list
"""
# length_of_list: int = len(my_list)
# print(length_of_list, type(length_of_list))
for index in range(len(my_list)):  # 0 to length of list - 1, or 0 to 4
    my_list[index] = my_list[index] * 2
print(my_list)
