"""
## Challenge 8: Accessing Keys and Values in a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Print all the keys and values present in my_dict
"""
my_dict: dict[str, str | int] = {"name": "Alice", "age": 25, "city": "New York"}
my_dict_keys: list[str] = list(my_dict.keys())
my_dict_values: list[str | int] = list(my_dict.values())
print(my_dict_keys)
print(my_dict_values)
