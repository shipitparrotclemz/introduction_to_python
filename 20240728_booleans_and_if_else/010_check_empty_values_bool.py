"""
Challenge 10: Checking for Empty Values
Define an empty list [] and assign it to a variable named empty_list

Define a boolean object that checks if empty_list is empty using the
not operator and assign it to a variable named is_empty

Print is_empty
python3 010_check_empty_values_bool.py
True
"""

# New Concept:
# In python, we have this new data structure called a list
# a list is like an egg tray
# Creating a list:
# <variable_name>: list[<type_the_list_contains>] = []

empty_list: list[str] = []
# New Concept: if you put the `not` keyword in front of a data structure like list
# it will return True, if the data structure is empty
is_empty: bool = not empty_list  # False
# False
print(is_empty)
