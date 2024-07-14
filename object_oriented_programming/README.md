# Object Oriented Programming
Way of writing code, to defining object, and blue-prints (class) to create objects

## Concept 1: Object, like an object in real world, represents one thing in code
- Objects are analogous to objects in the real world
- You can have multiple objects of a given class type

## Concept 2: Classes as blue-prints to create an Object

Example of a class / blue-print of an object

```python3
class Cat:
    """
    Blueprint of a cat, that defines it's behaviour
    """
    def __init__(self, name: str, age: int, color: str, weight: int) -> None:
        # __init__ is a special function called, when creating a cat
        # this function is called a constructor
        self.name: str = name       # attribute 1
        self.age: int = age         # attribute 2
        self.color: str = color     # attribute 3
        self.weight: int = weight
```

### Concept 2.1: Classes define attributes of an object
- A cat has a name (str), age (int), color (str)
- These name, age and colors, we have a name for that; they are attributes

### Concept 2.2: Methods, as functions under classes.
- A cat can meow, jump up staircase, jump down staircase, eat food
- These behaviours are represented by functions in a class.
- Functions in a class has a special name; methods
- A class is a blue-print that defines the behaviour (functions) and attributes of the cat

### Concept 2.3: You can create multiple objects

We do so by calling the constructor

We call the constructor by writing the name of the class

```python3
<NameOfClass>(input1, input2, input3)
```

Example:

```python3
# When you call the Cat like a function, you are creating a cat by calling def __init__
cat_one: Cat = Cat(name="Aaron", age=32, color="black", weight=100)
cat_two: Cat = Cat(name="Clement", age=29, color="black", weight=100)
```

Surprise! You have always been using classes! In pandas, we use the DataFrame class, to create data frames.

```python3
import pandas as pd
from typing import Any

class DataFrame:
    def __init__(self, input: list[dict[str, Any]]) -> None:
        pass

# you are really calling DataFrame's __init__ function to create a dataframe
df: pd.DataFrame = pd.DataFrame([{"name": "Aaron"}])
```