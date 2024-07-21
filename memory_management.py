# this already creates an integer object
# instance of a class
"""
to prove that this is already an int object
we print the type of 10
if we see any keyword related to "class" and "int"
this hints that this is an object of type int
"""
print(type(10))
"""
my_int: int = 10

what is my_int then?
it is definitely not the int object since the right hand side is already the object

A: my_int is really a pointer
pointer is a variable that contains the address of where 10 is stored in memory

0x123

Q: When will python free up the memory used by int object 10?

1. when python program (or process) terminates
2. when no other pointers point to object 10

Concept: Pass by reference (memory address of an object)
"""

my_int: int = 10
my_int_two: int = my_int
