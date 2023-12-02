"""
Practice 1:
Create an empty list
- use for loop to add 3 items "item" into it
"""

# my_list: list[str] = []
#
# for i in range(3):  # i = 0, i = 1, i = 2
#     my_list.append("item")
#
# print(my_list)
#
# """
# Practice 2:
# Create a non-empty list containing "item 1", "item 2", "item 3"
# add item 4 5 6 with for loop and append
# """
# my_another_list: list[str] = ["item 1", "item 2", "item 3"]
#
# for i in range(4,7): # 4, 5, 6 (start, end exclusive)
#     my_item: str = "item " + str(i)
#     my_another_list.append(my_item)
# print(my_another_list)


"""
Practice 3

2 approaches for this
we will do the first approach

item 1, item 3, item 5... item 9

if True:
    do_something
"""

# my_list: list[str] = []
#
# for i in range(1, 10, 2):
#     my_list.append("item " + str(i))
# print(my_list)

my_list: list[str] = []
for i in range(1, 10):
    if i % 2 == 1:  # if remainder of i / 2 is 1 (odd), add to my_list
        my_list.append("Item " + str(i))
print(my_list)

# print(10 / 2)   # 5.0
# print(10 % 2)   # 0
# print(9 / 2)    # 4.5
# print(9 % 2)    # 1