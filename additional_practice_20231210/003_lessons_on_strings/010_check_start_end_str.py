"""
## Challenge 10: Checking Start and End of a String
- Define a string object "Python is amazing" and assign its value to a variable named my_str
- Check if my_str starts with "Python" and assign the result to a boolean variable named starts_with_python
- Check if my_str ends with "amazing" and assign the result to a boolean variable named ends_with_amazing
- Print both starts_with_python and ends_with_amazing
"""
my_str: str = "Python is amazing"
starts_with_python: bool = my_str.startswith("Python")
ends_with_amazing: bool = my_str.endswith("amazing")
print(starts_with_python)
print(ends_with_amazing)