"""
## Challenge 3: Modifying Elements in a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Change the value of the 'city' key in my_dict to 'San Francisco'
- Print my_dict
"""
my_dict: dict[str, str | int] = {"name": "Alice", "age": 25, "city": "New York"}
my_dict["city"] = "San Francisco"
print(my_dict)
