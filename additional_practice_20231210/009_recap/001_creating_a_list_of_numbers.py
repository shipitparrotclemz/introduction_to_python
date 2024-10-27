"""
Challenge 1:

Create a list[int] of numbers from 5 to 15

Concepts:
- list and list.append()
- range(start, end); end is exclusive
"""

my_list: list[int] = []
for i in range(5,16):
    my_list.append(i)
print(my_list)

