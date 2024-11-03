"""
## Challenge 8: Combining Logical Operators
- Define three boolean objects True, False, and True and
assign their values to variables named bool1, bool2, and bool3 respectively
- Define a boolean object that checks if either bool1 or bool2 is True, and bool3 is False using the or, and operators and assign it to a variable named result
- Print result
"""

bool1: bool = True
bool2: bool = False
bool3: bool = True
# result: bool = bool1 or bool2 and bool3 is False
result: bool = bool1 is True or bool2 is True and bool3 is False
"""
Q: Is this a valid alternative answer?
bool1 is True or bool2 is True or bool3 is True
                                ^^^^^^^^^^^^^^^

a: Lets check it out by creating our own test cases
and checking if the above answer passes the test case

Input, Expected, Output
TC1: False, True, False -> True => True (Passed)
TC2: False, False, True -> False => True (Failed)
TC3: False, True, False -> True
TC4: False, False, False -> False
"""
print(result)
