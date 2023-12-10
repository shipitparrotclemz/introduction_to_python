"""
## Challenge 6: Finding a substring in a string
- Define a string object "Python is powerful!" and assign its value to a variable named my_str
- Define a substring "power" to check its presence in my_str
- Define a boolean object to store whether the substring exists in my_str using the in operator
- Print the result
"""
my_str: str = "Python is powerful!"
my_substring: str = "power"
exists: bool = my_substring in my_str
print(exists)
