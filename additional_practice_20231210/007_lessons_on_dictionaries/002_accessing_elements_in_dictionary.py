"""
## Challenge 2: Accessing Elements in a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Access and print the value associated with the 'age' key in my_dict
"""
my_dict: dict[str, str | int] = {"name": "Alice", "age": 25, "city": "New York"}
age: int | str = my_dict["age"]
print(age)
