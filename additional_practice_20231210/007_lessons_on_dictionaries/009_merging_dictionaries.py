"""
## Challenge 9: Merging Dictionaries
- Define two dictionaries dict1 containing keys 'a', 'b' with values 1, 2 and dict2 containing keys 'c', 'd' with values 3, 4
- Merge dict2 into dict1 and print the updated dict1
"""
dict1: dict[str, int] = {"a": 1, "b": 2}
dict2: dict[str, int] = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)
