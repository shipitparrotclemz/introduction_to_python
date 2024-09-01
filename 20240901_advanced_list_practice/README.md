# Advanced List Practice

## Date: 2024-09-01

## Q1: Find the median of an even or odd length list (assumed sorted ascendingly)

##### Test Case 1:

Given an even length list, take the average of the two items in the center

```python3
my_list: list[int] = [1, 2, 3, 4]
```

The two items in your center will be 2 and 3

The median is `(2 + 3) / 2 = 2.5`

##### Test Case 2:

Given an odd lenfgth list, take the center item as the median

```python3
my_list: list[int] = [1, 2, 3]
```

The median is `2`

## Q2: Create your own random list

Concept 1: `random.randint(start, end)` to generate a number from start to end, inclusive

```python3
import random

my_int: int = random.randint(0, 10)   # generate a number from 0 to 10 inclusive
```

Way 1: normal for-loop

```python3
import random

my_list: list[int] = []

for i in range(1, 11):
    my_list.append(random.randint(1, 10))   # randomly insert a number from 1 to 10

print(my_list)
```

Way 2: List comprehension

```python3
import random

my_list: list[int] = [random.randint(1, 10) for i in range(1, 11)]

print(my_list)
```


## Q3: Find median of an unsorted list (can be even length can be odd length)

```python3
my_list: list[int] = [4, 2, 1, 3]
```

Concept: To sort a list, you have two ways

Way 1: `.sort()` to sort a list in place

```python3
my_list: list[int] = [4, 2, 1, 3]
my_list.sort()
print(my_list)  # [1, 2, 3, 4]
```

Way 2: `sorted(my_list)` to give back a new copy of the list but sorted

```python3
my_list: list[int] = [4, 2, 1, 3]
sorted_list: list[int] = sorted(my_list)
print(my_list)  # [1, 2, 3, 4]
```

## Q4: Finding two numbers that add to a target number

```python3
my_list: list[int] 
```