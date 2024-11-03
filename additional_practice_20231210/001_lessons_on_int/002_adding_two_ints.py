"""
Challenge 2:
- Define a first integer object `10` and assign it's address to a variable named `first_int`
- Define a second integer object `10` and assign it's address to a variable named `second_int`
- Define a third integer object as the sum of `first_int` and `second_int` with the `+` operator
  - Assign it's address to a variable named `third_int`

The statement below does two things
- It creates `10` as an object, and saves it on our machine, at an address e.g 0x123
- It creates first_int as a variable, storing the address of where `10` is created (0x123)
"""

first_int: int = 10

"""
Same for second_int
"""
second_int: int = 10

"""
Right hand side: Create a third `int` object storing the sum of the first two `int` (10 + 10)
Left hand side: create `third_int` as a variable storing the address of where `20` is created
"""
third_int: int = first_int + second_int
print(third_int)
