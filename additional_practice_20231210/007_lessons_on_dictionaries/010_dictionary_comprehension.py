"""
## Challenge 10: Dictionary Comprehension
- Implement a dictionary comprehension to create a dictionary of squares of numbers from 1 to 5
- Print the dictionary
"""

my_dict: dict[int, int] = {i: i**2 for i in range(1, 6)}
print(my_dict)
