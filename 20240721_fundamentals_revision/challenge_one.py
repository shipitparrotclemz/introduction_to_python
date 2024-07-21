# input() is a function. it is a reusable piece of code that can be called
# it's built-in, you only have to use it, by calling () on the function name
# input() blocks the python script, till it receives an input
# returns back a string

# Challenge 1: Use this function, and print the output from the user
# Concept 1: input() -> allows you to suspend the script to take in an input from the user
# this input can be assigned to a variable (of type string)
# Concept 2: Concatenating strings with the + operator
# Concept 3: Reinforce your str syntax. You have to be comfortable with "", ''
my_input: str = input()
print("my_input: " + my_input)

# Concept 4: How to convert a string into an int
print("type of input")
print(type(my_input))
my_int_input: int = int(my_input)
# Concept 5: type() is a function that lets you check the type of an input
print("type of int input")
print(type(my_int_input))