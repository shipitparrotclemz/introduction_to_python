# Duplicate Integer

Question Link:
- https://neetcode.io/problems/duplicate-integer

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

```txt
Input: nums = [1, 2, 3, 3]

Output: true
```

Example 2:

```txt
Input: nums = [1, 2, 3, 4]

Output: false
```

## Concept prerequisites

1. Iterate through numbers in a list with for-loop

```python3
nums: list[int] = [1, 2, 3]
for num in nums:    # num reference the same iterated object in `nums`
    pass
```

2. Hash Set (`set`) supports O(1) average time complexity `__contains__` (check if number is in set) / and `__setitem__` (place number in set)

```python3
my_set: set[int] = set([1, 2, 3])
my_set.add(4)   # add a number to set, calls __setitem__ dunder method
set_contains_one: bool = 1 in my_set    # check if number is in set, calls __contains__ dunder method
```
