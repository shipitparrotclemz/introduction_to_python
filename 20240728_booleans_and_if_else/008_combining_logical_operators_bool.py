"""
Challenge 8: Combining Logical Operators

Define three boolean objects True, False, and True and
assign their values to variables named bool1, bool2, and bool3 respectively

Define a boolean object that checks if either bool1 or bool2 is True,
and bool3 is False using the or, and operators and assign it to a variable

named result
Print result
python3 008_combining_logical_operators_bool.py
True
"""

bool1: bool = True
bool2: bool = False
bool3: bool = True

# new concept: use or, to return True, if left or right hand side is True

# bool1 or bool2 -> True or False -> or will return True
# True and bool3 is False
# True and False
# False
result: bool = (bool1 or bool2) and not bool3

print(result)
