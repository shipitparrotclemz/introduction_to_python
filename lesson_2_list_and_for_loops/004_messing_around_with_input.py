# my_drink: str = input("What drink do you want?\n")     # magic wand will pause python here,
#                             # till the user give an input
# print(f"Serving you {my_drink}")

"""
Q: What if i define a list of 3 items
and i use a for loop to iterate all items

in every loop
instead of printing out each item
i do input() instead

what will the code's behaviour be?
"""

my_list: list[str] = ["weixuan", "aaron"]

for name in my_list:  # 2 times
    my_input: str = input()
    my_list.append(my_input)

print(my_list)  # 4
