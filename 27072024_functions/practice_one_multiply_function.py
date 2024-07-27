"""
Practice: Create our first function that takes in two numbers

and return the product
"""

# def <function_name>(<input_one_name>: <type_hint>, <input_two_name>: <type_hint>) -> int:
def multiply(a: int, b: int) -> int:
    # return at the back of the function <output>
    return a * b


product: int = multiply(10, 10)
print(product)
product = multiply(20, 20)
print(product)


