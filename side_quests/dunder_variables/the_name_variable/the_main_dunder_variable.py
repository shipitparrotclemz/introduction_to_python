"""
Concept 1:
Let's print out the special reserved __name__ variable
And run this program directly

When we run a program directly, this __name__ variable will default to "__main__"
"""

# this is the __name__ variable belonging to
# the_main_dunder_variable.py
print(f"the_main_dunder_variable: __name__: {__name__}")

"""
Q: How to run a program indirectly leh?
A: When you import another python file, in the main file

When you import another file, in a main file, it will run that file from top to bottom
Each file has it's own __name__ variable
"""

from another_file import multiply
