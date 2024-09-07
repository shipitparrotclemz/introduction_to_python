"""
Create a list [1, 2..., 100]

Way 1:
1. Create an empty list
2. Use a for-loop + range, to iterate from 1 to 100
3. for each item in the for-loop append it to the list
"""

my_list: list[int] = [] # [1, 2, 3]
for num in range(1, 101):   # 3
    my_list.append(num)
print(my_list)