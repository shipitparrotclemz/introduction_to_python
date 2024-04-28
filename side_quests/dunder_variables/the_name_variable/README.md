# The __main__ variable

## Concept 1:
- Python has special reserved variables and functions
- Ignore functions for now :D lets focus on reserved variables
- __main__

```python
if __name__ == "__main__":
    print("Elson gorgor")
```

Q: Hey, we see this `if __name__ == "__main__"` alot, the fuck is this?

A: __name__ is a special reserved variable that tells us if the current file is the entry point of a python program.

If the python script is executed directly in a file

The __name__ variable will default to "__main__"

TLDR: (Too long don't wanna read)

`if __name__ == "__main__":` -> If this file is executed directly

