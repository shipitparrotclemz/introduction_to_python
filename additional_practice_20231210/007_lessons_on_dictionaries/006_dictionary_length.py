"""
## Challenge 6: Dictionary Length
- Define a dictionary my_dict containing keys 'a', 'b', 'c', 'd' with corresponding values 1, 2, 3, 4
- Calculate and print the length of my_dict
"""

my_dict: dict[str, int] = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
length_of_dict: int = len(my_dict)
print(length_of_dict)
