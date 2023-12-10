"""
## Challenge 7: Checking Key Existence in a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Check if the key 'age' is present in my_dict and print the result
"""
my_dict: dict[str, str | int] = {"name": "Alice", "age": 25, "city": "New York"}
age_in_my_dict: bool = "age" in my_dict
print(age_in_my_dict)
