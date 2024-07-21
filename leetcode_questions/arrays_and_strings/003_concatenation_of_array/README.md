# Concatenation of Array

Question Link:
- https://leetcode.com/problems/concatenation-of-array/description/

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

```txt
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

Example 2:

```txt
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
```

Constraints:

```txt
n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
```

## Concept prerequisites

1. `list` has `__add__` implemented, to allow concatenating two lists

```python3
my_list: list[int] = [1,2,3]
my_new_list: list[int] = my_list + my_list
>>> my_new_list
[1, 2, 3, 1, 2, 3]
```

2. `list` has extend, which allows you to extend a list in-place

```python3
my_list: list[int] = [1,2,3]
my_list.extend([1,2,3])
>>> my_list
[1, 2, 3, 1, 2, 3]
```