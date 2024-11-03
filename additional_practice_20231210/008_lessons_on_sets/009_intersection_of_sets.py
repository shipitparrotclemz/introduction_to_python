"""
## Challenge 9: Intersection of Sets
- Define two sets set1 containing integers 1, 2, 3 and set2 containing integers 3, 4, 5
- Find the intersection of set1 and set2 and print the result
"""

set1: set[int] = {1, 2, 3}
set2: set[int] = {3, 4, 5}
intersection_of_sets: set[int] = set1.intersection(set2)
print(intersection_of_sets)
