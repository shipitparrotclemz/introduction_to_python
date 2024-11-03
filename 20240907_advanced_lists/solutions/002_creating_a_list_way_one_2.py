"""
1. create a list
2. use a for loop + range
3. instead of appending just the num from range
append num * 2
"""

my_list: list[int] = []
for num in range(1, 101):
    multiplied_by_two: int = num * 2
    my_list.append(multiplied_by_two)
print(my_list)
