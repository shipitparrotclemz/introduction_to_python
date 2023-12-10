"""
## Challenge 9: Pass Statement
- Implement a function my_function that prints "This is a placeholder function"
- Implement a second function my_nothing_function that does nothing
    - Use the pass statement to define the function without implementing any code
- Call both functions
"""

def my_function() -> None:
    print("This is a placeholder function")

def my_nothing_function() -> None:
    pass

my_function()
my_nothing_function()