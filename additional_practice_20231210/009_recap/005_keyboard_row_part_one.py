"""
Given a keyboard

QWERTYUIOP
ASDFGHJKL
ZXCVBNM

And a list of words

["DAD", "ALASKA", "GAS", "AARON", "ELSON"]

Return the words whose first character belongs to the 2nd row

ASDFGHJKL

Hint:
- To get the first character of a word: str

first_char: str = word[0]

- To check if a character is in the 2nd row

second_row: str = "ASDFGHJKL"
if first_char in second_row:
    # do something
"""

words: list[str] = ["DAD", "ALASKA", "GAS", "AARON", "ELSON"]
# answer: list[str] = ["DAD", "ALASKA", "GAS", "AARON"]

# first_row: set[str] = set("QWERTYUIOP")
second_row: set[str] = set("ASDFGHJKL")
# third_row: set[str] = set("ZXCVBNM")

answer: list[str] = []
for word in words:
    first_char: str = word[0].upper()
    print(first_char, first_char in second_row)
    if first_char in second_row:
        answer.append(word)
print(answer)
