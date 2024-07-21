# Is Anagram

Question Link:
- https://neetcode.io/problems/is-anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

```txt
Input: s = "racecar", t = "carrace"

Output: true
```

Example 2:

```txt
Input: s = "jar", t = "jam"

Output: false
```

Constraints:

s and t consist of lowercase English letters.

## Concept prerequisites

1. Using a dictionary, as a data structure to count occurrences of characters

```python3
my_string: str = "weixuan"
character_counts: dict[str, int] = {}

for char in my_string:
    character_counts[char] = character_counts.get(char, 0) + 1
>>> character_counts
{'w': 1, 'e': 1, 'i': 1, 'x': 1, 'u': 1, 'a': 1, 'n': 1}
```

2. Comparing two dictionaries by their keys and values, directly, with `==`

3. (Optional) Use collections.Counter as a dictionary on steroids
- Counter's constructor does the iteration of characters for us

```python3
from collections import Counter
my_string: str = "weixuan"
my_counter: Counter = Counter(my_string)
>>> my_counter
Counter({'w': 1, 'e': 1, 'i': 1, 'x': 1, 'u': 1, 'a': 1, 'n': 1})
```