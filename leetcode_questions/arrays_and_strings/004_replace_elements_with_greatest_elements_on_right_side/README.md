# Replace elements with greatest elements on right side

Question Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

```txt
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
```

Example 2:

```txt
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
```

Constraints:

```txt
1 <= arr.length <= 104
1 <= arr[i] <= 105
```

## Concept prerequisites

1. range(min, max_exclusive, step) to iterate a list from front to back, or back to front with an index

Iterating forward

```python3
>>> my_list: list[int] = [1, 2, 3]
>>> for i in range(0, len(my_list), 1):
...     my_list[i] = my_list[i] * 2  # double each item
...     print(my_list[i])
... 
2
4
6
```

Iterating backwards

```python3
>>> my_list: list[int] = [1, 2, 3]
>>> for i in range(len(my_list) - 1, -1, -1):
...     my_list[i] = my_list[i] * 2  # double each item
...     print(my_list[i])
... 
6
4
2
```

2. max() to get the max of two numbers

```python3
max_of_two_numbers: int = max(1, 2)
>>> max_of_two_numbers
2
```

3. Accessing last element of a list

Strategy 1: Use last element's index

```python3
>>> my_list: list[int] = [1,2,3]
>>> last_element: int = my_list[len(my_list) - 1]
>>> last_element
3
```

Strategy 2: Use -1 as the index

```python3
>>> my_list: list[int] = [1,2,3]
>>> last_element: int = my_list[-1]
>>> last_element
3
```