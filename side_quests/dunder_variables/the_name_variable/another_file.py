def multiply(a: int, b: int) -> int:
    return a * b

# this is the __name__ variable belonging to
# another_file.py
# print(f"another_file: __name__: {__name__}")


"""
We can be careless and put dangerous code
to be executed in a file

And when we import that file, we can accidentally
run it

Concept:
Becareful to place the code meant to be executed
only if the file is run directly
under 

if __name__ == "__main__"
"""
if __name__ == "__main__":
    print("Clement send 20k to Kim Jong Un")
