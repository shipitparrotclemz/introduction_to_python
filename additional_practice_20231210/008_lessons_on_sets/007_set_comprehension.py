"""
## Challenge 7: Set Comprehension
- Implement a set comprehension to create a set of squares of numbers from 1 to 5
- Print the set
"""

my_set: set[int] = {i**2 for i in range(1, 6)}
print(my_set)
