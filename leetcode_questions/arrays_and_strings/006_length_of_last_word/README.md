# Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

```txt
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

Example 2:

```txt
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

Example 3:

```txt
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

## Prerequisites

1. Splitting a string by empty space gives back a list of words

```python3
my_string: str = "wei xuan makes protein cake"
words: list[str] = my_string.split(" ")
>>> words
['wei', 'xuan', 'makes', 'protein', 'cake']
```

2. Getting the last element of a list of words

Strategy 1: Use `-1` as the index

```python3
words: list[str] = ['wei', 'xuan', 'makes', 'protein', 'cake']
last_word: str = words[-1]
>>> last_word
'cake'
```

Strategy 2: Use index of last word

```python3
words: list[str] = ['wei', 'xuan', 'makes', 'protein', 'cake']
last_word: str = words[len(words) - 1]
>>> last_word
'cake'
```

3. Iterating characters from the back

```python3
weixuan: str = "weixuan"
for index in range(len(weixuan) - 1, -1, -1):
    print(weixuan[index])
n
a
u
x
i
e
w
```