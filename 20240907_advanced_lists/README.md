# 20240907 - Advanced Lists

## Concept 1: Sorting a List

1. `my_list.sort()` -> sorts list in-place, ascending-ly

2. `my_sorted_list = sorted(my_list)` -> it creates a new sorted copy, ascendingly

## Concept 2: Recap, accessing item in a list by index

```python3
my_list: list[int] = [1, 3, 5, 7, 9]
#              index  0  1  2  3  4
# to get 5, you use index 2
five: int = my_list[2]
```

## Concept 3: Find median of a sorted list

```python3
my_list: list[int] = [9, 7, 1, 3, 5]
# you can't take 1 as the median
# the median is a better way of finding the average
# we agar know the answer should be 5

# to get the median:
```

1. To get the median of a list of numbers, it involves two steps
- sort it ascendingly
- get the middle item in the sorted

```python3
my_list: list[int] = [9, 7, 1, 3, 5]
my_sorted_list: list[int] = sorted(my_list)     # [1, 3, 5, 7, 9]
median_index: int = len(my_sorted_list) // 2    # 5 / 2 = 2.5 -> 2
median: int = my_list[median_index]             # 5 
```

## Concept 4: Binary Searching an item in a sorted list

```python3
import random

my_numbers: list[int] = [i for i in range(1, 1000001)]  # 1,000,000 items
random.shuffle(my_numbers)  # randomly shuffle the list in-place

# now, we want to find the index which contains this item
number_of_checks: int = 0
item_to_find: int = 500000
answer: int = -1
for index, item in enumerate(my_numbers):   # iterates both index, and item in my_numbers
    if item == item_to_find:
        answer = index
        break
    number_of_checks += 1

print(answer)       # this is the index which this exists at
print(my_numbers[answer])   # 500000
print(f"number of checks we had to use: {number_of_checks}")    # this is very slow, can take up to even 1M checks
```