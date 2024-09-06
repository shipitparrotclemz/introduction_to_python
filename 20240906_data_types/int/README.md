# 20240906 - Data Types

Python has 4 main scalar data types (0-D data types)

## 1. `int` -> whole numbers

### 1.1 Defining an integer

```python3
# <variable_name> -> my_int
# <type_hint> -> int
# = -> assignment operator
# 10 -> your int itself (object)
# <variable_name>: <type_hint> = <object>
my_int: int = 10
```

### 1.2 `+` -> operator to add two integers together

```python3
one: int = 1
two: int = 2
# + operator must have two integers sandwiched between them
three: int = one + two
print(three)    # 3
```

### 1.3 `-` -> to delete an integer from another

```python3
one: int = 1
two: int = 2
minus_one: int = one - two
print(minus_one)    # -1
```

### 1.4 `*` -> multiply two integers

```python3
two: int = 2
three: int = 3
six: int = two * three
print(six)  # 6
```

### 1.5 `/` -> divide two integers

NEW: `/` gives back a `float`

```python3
one: int = 1
two: int = 2
half: float = one / two # 0.5
print(float)    # 0.5
```

### 1.6 `//` -> floor division, divide and take lower full number

```python3
one: int = 1
two: int = 2
zero: int = one // two  # 0.5 -> 0
print(zero) # 0
```

### 1.7 `%` -> modulo, takes the remainder after dividing

```python3
one: int = 1
two: int = 2
remainder: int = one % two  # 1
print(remainder)    # 1
```

Tip: The modulo operator is commonly used to check if an integer is even or odd

```python3
my_integer: int = 9
is_even: bool = my_integer % 2 == 0 # 1 == 0 = False

my_integer: int = 10
is_even: bool = my_integer % 2 == 0 # 0 == 0 = True
```

## 2. `float`

## 3. `str`

## 4. `bool`