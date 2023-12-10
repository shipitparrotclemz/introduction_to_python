"""
## Challenge 10: Difference of Sets
- Define two sets set1 containing integers 1, 2, 3 and set2 containing integers 3, 4, 5
- Find the difference between set1 and set2 and print the result
"""
set1: set[int] = {1, 2, 3}
set2: set[int] = {3, 4, 5}
difference_in_set_1_and_2: set[int] = set1 - set2
print(difference_in_set_1_and_2)
