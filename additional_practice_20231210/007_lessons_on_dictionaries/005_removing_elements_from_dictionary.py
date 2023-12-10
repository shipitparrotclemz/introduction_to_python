"""
## Challenge 5: Removing Elements from a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Remove the key-value pair 'age': 25 from my_dict
- Print my_dict
"""
my_dict: dict[str, str | int] = {"name": "Alice", "age": 25, "city": "New York"}
my_dict.pop("age")
print(my_dict)
