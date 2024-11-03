"""
## Challenge 8: Union of Sets
- Define two sets set1 containing integers 1, 2, 3 and set2 containing integers 3, 4, 5
- Find the union of set1 and set2 and print the result
"""

set1: set[int] = {1, 2, 3}
set2: set[int] = {3, 4, 5}
union_of_set1_and_set_2: set[int] = set1.union(set2)
print(union_of_set1_and_set_2)
