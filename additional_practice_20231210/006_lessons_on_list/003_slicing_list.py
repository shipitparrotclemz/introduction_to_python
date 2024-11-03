"""
## Challenge 3: Slicing a List
- Define a list object my_list containing integers 1 through 10
- Slice and print elements from index 2 to 5 from my_list

[<start>:<end>]
<end> is excluded
"""

my_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_two: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

sliced_list: list[int] = my_list[2:6]
slice_list_two: list[float] = my_list_two[2:6]
print(sliced_list)
print(slice_list_two)
